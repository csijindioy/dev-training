using Banking.Entities;
using System;
using System.Collections.Generic;
using System.Linq;

namespace Banking.Base
{
    public static class Data
    {
        public static List<Customer> Customers { get; set; } = new List<Customer>();

        public static bool IsLoaded() { return Customers.Count > 0; }

        public static Customer GetById(long id)
        {
            return Customers.Find(c => c.Id == id);
        }

        public static IEnumerable<Customer> GetByName(string name)
        {
            return Customers
                .Where(c => c.FirstName.Equals(name, StringComparison.InvariantCultureIgnoreCase)
                    || c.LastName.Equals(name, StringComparison.InvariantCultureIgnoreCase));
        }

        public static long GetCount() { return Customers.Count; }
    }
}
