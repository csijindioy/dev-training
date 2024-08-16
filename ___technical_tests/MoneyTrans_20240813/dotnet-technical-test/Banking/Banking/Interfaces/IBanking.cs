using Banking.Entities;

namespace Banking.Interfaces
{
    interface IBanking
    {
        /// <summary>
        /// Load csv file with data of customers
        /// </summary>
        /// <param name="path"></param>
        /// <exception cref="AlreadyInitialiseException">Occurs when is initialised more than once time</exception>
        void Initialize(string path);


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
        void Transfer(long giverId, long beneficiaryId, double amount);

        /// <summary>
        /// Calculate fee with correspond data parameters.
        /// </summary>
        /// <param name="giverId"></param>
        /// <param name="beneficiaryId"></param>
        /// <param name="amount"></param>
        /// <returns>Fee value</returns>
        /// <exception cref="ExternallGiverException">Exception will be throught when giver is external</exception>
        double CalculateFees(long giverId, long beneficiaryId, double amount);

        /// <summary>
        /// Count number of customer in banking system
        /// </summary>
        /// <returns>long with total of customers</returns>
        long CountCustomers();

        /// <summary>
        /// Return all customer filtered by data parameters
        /// </summary>
        /// <param name="name">Name to search</param>
        /// <param name="id">Id to search</param>
        /// <returns>List of customer filtered</returns>
        Customer[] SearchCustomers(long? id = null, string name = null);
    }
}
