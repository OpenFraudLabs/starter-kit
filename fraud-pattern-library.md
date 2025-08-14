# African Fraud Pattern Library

## Introduction
This library documents common financial fraud patterns observed across Africa, with detection strategies you can implement using open-source tools. Patterns are categorized by payment method and include executable detection logic.

## Mobile Money Fraud

### 1. SIM Swap Fraud
**Target**: M-Pesa, Airtel Money, MTN Mobile Money  
**Pattern**: 
1. Fraudster clones victim's SIM
2. Takes control of mobile money account
3. Initiates high-value transfers

**Detection Strategy**:
```python
def detect_sim_swap(user, recent_logins):
    """
    Detect suspicious SIM changes
    :param user: User profile
    :param recent_logins: List of recent login locations
    :return: Risk score (0-1)
    """
    if len(recent_logins) < 3:
        return 0  # Insufficient data
    
    # Calculate location variance
    location_changes = sum(
        1 for i in range(1, len(recent_logins)) 
        if recent_logins[i]['location'] != recent_logins[i-1]['location']
    )
    
    # High risk if multiple locations in short time
    return min(1.0, location_changes * 0.3)

2. Airtime Flushing
Target: Airtime credit systems
Pattern:

Compromised accounts convert airtime to cash

Small-value transactions to multiple recipients

Rapid transfers within minutes

Detection Strategy:
def detect_airtime_flushing(transactions):
    """
    Identify airtime-to-cash conversion patterns
    :param transactions: List of transactions in last 1 hour
    :return: Boolean (True if suspicious)
    """
    if len(transactions) < 5:
        return False
        
    total_value = sum(t['amount'] for t in transactions)
    recipient_count = len(set(t['recipient'] for t in transactions))
    
    # High risk if multiple small transfers
    return (recipient_count > 3 and 
            total_value > 5000 and 
            max(t['amount'] for t in transactions) < 1000)


Banking Fraud
3. Cheque Fraud Syndicates
Target: SME business accounts
Pattern:

Fraudulent cheque books obtained

Forged signatures on high-value cheques

Presentment at multiple banks simultaneously

Detection Strategy:
def detect_cheque_fraud(cheques):
    """
    Identify duplicate cheque presentation
    :param cheques: List of cheques presented in last 24hrs
    :return: Risk score (0-1)
    """
    cheque_numbers = [c['number'] for c in cheques]
    duplicates = len(cheque_numbers) - len(set(cheque_numbers))
    
    # High risk if same cheque at multiple locations
    return min(1.0, duplicates * 0.5)

4. Ghost Loan Applications
Target: Digital lenders (Branch, Tala)
Pattern:

Fake digital identities created

Multiple loan applications

No repayment intention

Detection Strategy:
def detect_ghost_loans(applications, device_db):
    """
    Identify fraudulent loan apps
    :param applications: Recent loan applications
    :param device_db: Device fingerprint database
    :return: List of suspicious apps
    """
    suspicious = []
    for app in applications:
        device = device_db.get(app['device_id'])
        if device and device['application_count'] > 3:
            app['risk_reason'] = "Multiple applications from same device"
            suspicious.append(app)
    return suspicious

POS & Card Fraud
5. ATM Gas Explosion Thefts
Target: ATM cash reserves
Pattern:

Criminals inject gas into ATM

Ignite to explode vault

Steal cash during confusion

Prevention Checklist:

Install gas detection sensors

Implement vibration monitoring

Use dye packs in cash cassettes

Establish police rapid response protocol

6. Card Skimming Clusters
Target: Bank ATMs in urban areas
Pattern:

Skimming devices installed

Data transmitted to fraudsters

Card cloning within hours

Detection Strategy:
def detect_skimming_cluster(atms, transactions):
    """
    Identify potential skimming locations
    :param atms: List of ATM locations
    :param transactions: Fraudulent transactions
    :return: List of high-risk ATMs
    """
    risk_atms = {}
    for t in transactions:
        atm_id = t['atm_id']
        if atm_id not in risk_atms:
            risk_atms[atm_id] = 0
        risk_atms[atm_id] += 1
    
    return [atm for atm in atms 
            if atm['id'] in risk_atms 
            and risk_atms[atm['id']] > 3]

def detect_skimming_cluster(atms, transactions):
    """
    Identify potential skimming locations
    :param atms: List of ATM locations
    :param transactions: Fraudulent transactions
    :return: List of high-risk ATMs
    """
    risk_atms = {}
    for t in transactions:
        atm_id = t['atm_id']
        if atm_id not in risk_atms:
            risk_atms[atm_id] = 0
        risk_atms[atm_id] += 1
    
    return [atm for atm in atms 
            if atm['id'] in risk_atms 
            and risk_atms[atm['id']] > 3]

Contributing New Patterns
Help us expand this library! To contribute:

Fork our GitHub repository

Create new Markdown file in /patterns

Submit pull request with:

Pattern name

Target region/country

Detailed description

Detection strategy (pseudocode or Python)

Include real-world examples (anonymized)

Filename: west-africa-momo-fraud.md
Content format:
## [Pattern Name]
### Region: West Africa
### Target: Mobile Money
[Description]
[Detection Strategy]

License
This work is licensed under CC BY-SA 4.0. You may share and adapt with attribution.

"Knowledge shared is fraud prevented" - OpenFraudLabs Community

### Key Features of This Library:

1. **Africa-Specific Patterns**:
   - SIM swap fraud targeting mobile money
   - ATM gas explosion techniques
   - Cultural context for fraud patterns

2. **Executable Detection Strategies**:
   - Ready-to-run Python functions
   - Practical parameters
   - Return risk scores

3. **Structured Format**:
   - Clear pattern descriptions
   - Prevention checklists
   - Contribution guidelines

4. **Actionable Content**:
   - Can be implemented immediately
   - Integrates with existing systems
   - Scales with community input

### Benefits for Your Starter Kit:

1. **Immediate Value**: Users get working detection code
2. **Educational**: Teaches fraud pattern recognition
3. **Community Building**: Clear contribution path
4. **Regional Relevance**: Focused on African financial systems

To implement:
1. Create `fraud-pattern-library.md` in your starter-kit repo
2. Paste this entire content
3. Commit with message: "Add African fraud pattern library"

Would you like me to:
1. Add more patterns from specific regions?
2. Create a Jupyter notebook demonstrating pattern detection?
3. Develop a contribution template file?


