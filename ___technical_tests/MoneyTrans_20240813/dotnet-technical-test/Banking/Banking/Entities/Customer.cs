namespace Banking.Entities
{
    public class Customer
    {
        public long Id { get; set; }

        public string FirstName { get; set; }

        public string LastName { get; set; }

        public string Phone1 { get; set; }

        public string Phone2 { get; set; }

        public CustomerType Type { get; set; }

        public double Balance { get; set; }
    }
}
