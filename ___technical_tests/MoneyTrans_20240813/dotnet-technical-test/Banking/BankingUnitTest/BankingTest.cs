using Banking;
using Banking.Base;
using Banking.Entities;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using System.Linq;

namespace BankingUnitTest
{
    [TestClass]
    public class BankingTest
    {
        private readonly string _path = "D:\\Dev\\Projects\\dotnet-technical-test\\customers.csv";
        private readonly BankingSystem _bs;

        public BankingTest()
        {
            _bs = new BankingSystem();
            _bs.Initialize(_path);
        }

        [TestMethod]
        public void BankingDoubleInitialization()
        {
            Assert.ThrowsException<Exception>(() => _bs.Initialize(_path));
        }

        [TestMethod]
        public void SearchCustomerByName()
        {
            Assert.IsTrue(_bs.SearchCustomers(null, "meaghan").Count().Equals(1));
        }

        [TestMethod]
        public void FeeBothCustomerInternalAmount50()
        {
            Assert.IsTrue(_bs.CalculateFees(34, 22, 50).Equals(0));
        }

        [TestMethod]
        public void FeeBothCustomerInternalAmount100()
        {
            Assert.IsTrue(_bs.CalculateFees(34, 22, 100).Equals(5));
        }

        [TestMethod]
        public void FeeInternalGiverExternalBeneficiaryAmount75()
        {
            Assert.IsTrue(_bs.CalculateFees(34, 76, 75).Equals(10));
        }

        [TestMethod]
        public void TransferExternalGiver()
        {
            Assert.ThrowsException<Exception>(() => _bs.Transfer(187, 188, 3));
        }

        [TestMethod]
        public void TransferNegativeAmount()
        {
            Assert.ThrowsException<Exception>(() => _bs.Transfer(39, 4, -20));
        }

        [TestMethod]
        public void TransferExceedBalance()
        {
            Assert.ThrowsException<Exception>(() => _bs.Transfer(41, 75, 40));
        }

        [TestMethod]
        public void TransferInternalGiverExternalBeneficiary()
        {
            Customer giver = Data.GetById(41);
            Customer receiver = Data.GetById(75);

            // Check balance before transfer
            Assert.IsTrue(giver.Balance.Equals(40));
            Assert.IsTrue(receiver.Balance.Equals(74));

            // Transfer 10 amount from customer id 41 to customer id 75
            _bs.Transfer(41, 75, 10);

            Assert.IsTrue(giver.Balance.Equals(20));
            Assert.IsTrue(receiver.Balance.Equals(84));
        }

        [TestMethod]
        public void TransferBothCustomerInternal()
        {
            Customer giver = Data.GetById(500);
            Customer receiver = Data.GetById(499);

            // Check balance before transfer
            Assert.IsTrue(giver.Balance.Equals(499));
            Assert.IsTrue(receiver.Balance.Equals(498));

            // Transfer 90 amount from customer id 500 to customer id 499 with 0 fee
            _bs.Transfer(500, 499, 90);

            Assert.IsTrue(giver.Balance.Equals(409));
            Assert.IsTrue(receiver.Balance.Equals(588));

            // Transfer back 90 amount from customer id 499 to customer id 500 with 0 fee
            _bs.Transfer(499, 500, 90);

            Assert.IsTrue(giver.Balance.Equals(499));
            Assert.IsTrue(receiver.Balance.Equals(498));

            // Transfer 120 amount from customer id 500 to customer id 499 with 5 fee
            _bs.Transfer(500, 499, 120);

            Assert.IsTrue(giver.Balance.Equals(374));
            Assert.IsTrue(receiver.Balance.Equals(618));

            // Transfer back 120 amount from customer id 499 to customer id 500 with 5 fee
            _bs.Transfer(499, 500, 90);

            Assert.IsTrue(giver.Balance.Equals(464));
            Assert.IsTrue(receiver.Balance.Equals(528));
        }
    }
}
