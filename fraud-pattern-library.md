# Common African Fraud Patterns

## 1. Mobile Money Flip
- **Target**: M-Pesa, MTN Mobile Money
- **Pattern**: Small test transfers → Large reversal requests
- **Detection**: Flag consecutive <$1 → >$100 transactions

## 2. POS Terminal Swap
- **Target**: Retail merchants
- **Pattern**: Device tampering + transaction cloning
- **Detection**: GPS location mismatch between terminal and transaction

## 3. Airtel Ghost Loans
- **Target**: Airtime lending apps
- **Pattern**: Fake identity → Multiple loan applications
- **Detection**: Device fingerprinting + velocity checks
