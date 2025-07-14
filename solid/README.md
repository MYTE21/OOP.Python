# 🪖 SOLID Principles

SOLID Principles is a set of five design principles that help make your code cleaner, more maintainable, and easier to 
scale. These principles are especially relevant in object-oriented programming.

SOLID stands for:
- `[S]` Single Responsibility
- `[O]` Open/Closed
- `[L]` Liskov Substitution
- `[I]` Interface Segregation
- `[D]` Dependency Inversion

# 💂🏻‍♂️ Single Responsibility (SRP)

> Purpose: `One class = One job`

A class should have only one reason to change.

In the [base.py](base.py), add_item and total_price is the part of the Order. Alternatively, the pay method should not 
be a part of this class, as this is not about the order, it's about the payment.
This creates way to many responsibility (function) in the class.
We need to fix that!
(if we add bitcoin or cash as a payment method in the future in present implementation, we have to 
change the Order class. This is not good.)

> How?
> We create a separate class for payment.

also, pay method has so many if-else statements. we should remove this by creating methods for each condition in the 
new class.

# 📭 Open/Closed (OCP)

> Purpose: Open for extension, closed for modification.

Software should be open for extension but closed for modification.

Now, if we want to add new payment methods (bitcoin, Apple Pay), we have to modify the payment class. This violates 
the open/closed principle.

We can solve this by making `paymentprocessor` as the abstract class and make debit and credit inherent
the abstract class.

# 🎲 Liskov Substitution (LSP)

> Purpose: Subtypes should replace base types safely

Objects of a superclass should be replaceable with instances of its subclasses.


In the code the `PayplaPaymentProcessor` use email address instead of security code. But the abstract class has 
`security_code` parameter.
This violates the Liskov substitution principle.

> solve: we remove the `security_code` from the abstract class. Create constructor for each child class and put the 
> parameter there.

# 🚦 Interface Segregation (ISP)

> Purpose: No forced methods.

Clients should not be forced to depend on interfaces they do not use.

# 🧩 Dependency Inversion (DIP)

> Purpose: Depend on abstractions, not concretions.

High-level modules should not depend on low-level modules. Both should depend on abstractions. This allows for flexible and decoupled code.

In the code, instead of the `Order` class directly depending on a specific payment processor, it should depend on an abstract payment processor interface. Concrete payment processors (like debit, credit, PayPal) implement this interface. This way, you can add new payment methods without changing the `Order` class.

