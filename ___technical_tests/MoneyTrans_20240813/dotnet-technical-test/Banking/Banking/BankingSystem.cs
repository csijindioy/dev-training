using Banking.Base;
using Banking.Entities;
using Banking.Interfaces;
using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Threading;

namespace Banking
{
    public class BankingSystem : IBanking
    {
        /// <summary>
        /// Calculate fee with correspond data parameters.
        /// </summary>
        /// <param name="giverId"></param>
        /// <param name="beneficiaryId"></param>
        /// <param name="amount"></param>
        /// <returns>Fee value</returns>
        /// <exception cref="ExternallGiverException">Exception will be throught when giver is external</exception>
        public double CalculateFees(long giverId, long beneficiaryId, double amount)
        {
            double fees = 0;

            var gCustomer = Data.GetById(giverId);
            var rCustomer = Data.GetById(beneficiaryId);

            if (gCustomer.Type == CustomerType.Internal
                && rCustomer.Type == CustomerType.Internal
                && amount > 0 && amount <= 100)
            {
                fees += 0;
            }

            if (gCustomer.Type == CustomerType.Internal
                && rCustomer.Type == CustomerType.Internal
                && amount >= 100)
            {
                fees += 5;
            }

            if (gCustomer.Type == CustomerType.Internal
                && rCustomer.Type == CustomerType.External)
            {
                fees += 10;
            }

            return fees;
        }

        /// <summary>
        /// Count number of customer in banking system
        /// </summary>
        /// <returns>long with total of customers</returns>
        public long CountCustomers()
        {
            return Data.GetCount();
        }

        /// <summary>
        /// Load csv file with data of customers
        /// </summary>
        /// <param name="path"></param>
        /// <exception cref="AlreadyInitialiseException">Occurs when is initialised more than once time</exception>
        public void Initialize(string path)
        {
            if (Data.IsLoaded())
            {
                throw new Exception("Customers list already loaded!");
            }

            using (var reader = new StreamReader(path))
            {
                while (!reader.EndOfStream)
                {
                    var line = reader.ReadLine();
                    var values = line.Split(';');

                    if (values[0].Contains("id"))
                    {
                        continue;
                    }

                    Customer customer = new Customer
                    {
                        Id = Convert.ToInt64(values[0]),
                        FirstName = values[1],
                        LastName = values[2],
                        Phone1 = values[9],
                        Phone2 = values[10],
                        Type = values[13] == "internal" ? CustomerType.Internal : CustomerType.External,
                        Balance = Convert.ToDouble(values[14])
                    };

                    Data.Customers.Add(customer);
                }
            }
        }

        /// <summary>
        /// Return all customer filtered by data parameters
        /// </summary>
        /// <param name="name">Name to search</param>
        /// <param name="id">Id to search</param>
        /// <returns>List of customer filtered</returns>
        public Customer[] SearchCustomers(long? id = null, string name = null)
        {
            if (id is null && name is null)
            {
                throw new ArgumentNullException("Both 'id' and 'name' arguments are null. Search cannot be executed.");
            }

            if (id != null && name != null)
            {
                throw new Exception("Both 'id' and 'name' arguments have some values. Search cannot be executed.");
            }

            if (id != null)
            {
                var result = new List<Customer>
                {
                    Data.GetById(id.Value)
                };

                return result.ToArray();
            }

            return !string.IsNullOrEmpty(name)
                ? Data.GetByName(name).ToArray()
                : new List<Customer>().ToArray();
        }

        /// <summary>
        /// Transferring money from one customer to another.
        /// </summary>
        /// <param name="Sender"></param>
        /// <param name="beneficiary"></param>
        /// <param name="amount"></param>
        /// <exception cref="SenderExternalException">Exception will be throught when sender is external of banking system</exception>
        /// <exception cref="InvalidAmountException">Exception will be throught when amount value is not greater than 0</exception>
        /// <exception cref="NotMoneyAvailableException">Exception will be throught when amount + fee value is greater of customer balance</exception>
        /// <exception cref="ExternallGiverException">Exception will be throught when giver is external</exception>
        public void Transfer(long giverId, long beneficiaryId, double amount)
        {
            var gCustomer = Data.GetById(giverId);
            var rCustomer = Data.GetById(beneficiaryId);

            if (gCustomer is null)
            {
                throw new Exception("Giver Id does not exist!");
            }

            if (rCustomer is null)
            {
                throw new Exception("Beneficiary Id does not exist!");
            }

            if (gCustomer.Type != CustomerType.Internal)
            {
                throw new Exception("Giver customer is not internal!");
            }

            if (gCustomer.Balance.Equals(0))
            {
                throw new Exception("Giver balance is 0. Transfer cannot be executed.");
            }

            if (amount < 0)
            {
                throw new Exception("Amount cannot be 0 nor negative. Transfer cannot be executed.");
            }

            double feesAmount = CalculateFees(giverId, beneficiaryId, amount);

            if (amount + feesAmount > gCustomer.Balance)
            {
                throw new Exception("Insufficient funds!");
            }

            rCustomer.Balance += amount;
            gCustomer.Balance -= amount + feesAmount;
        }
    }
}
