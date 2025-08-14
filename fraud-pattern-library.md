# 🌍African Fraud Pattern Library

![OpenFraudLabs Banner](./assets/banner-animation.gif)

![OpenFraudLabs](https://img.shields.io/badge/OpenFraudLabs-Active-green)
![Python](https://img.shields.io/badge/Python-Detection-blue)


## 🚀Introduction
This library documents common financial fraud patterns observed across Africa, with detection strategies you can implement using open-source tools. Patterns are categorized by payment method and include executable detection logic.

---



## 📑 Table of Contents
- [Mobile Money Fraud](#mobile-money-fraud)
- [Banking Fraud](#banking-fraud)
- [POS & Card Fraud](#pos--card-fraud)
- [Contributing New Patterns](#contributing-new-patterns)
- [Key Features](#key-features-of-this-library)
- [Benefits](#benefits-for-your-starter-kit)
- [License](#license)

---

## Mobile Money Fraud

### 1️⃣ SIM Swap Fraud
**Target**: M-Pesa, Airtel Money, MTN Mobile Money  

**Pattern**: 
1. Fraudster clones victim's SIM  
2. Takes control of mobile money account  
3. Initiates high-value transfers  

**Animated Demo**: *(insert gif or link here)*

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
    
    location_changes = sum(
        1 for i in range(1, len(recent_logins)) 
        if recent_logins[i]['location'] != recent_logins[i-1]['location']
    )
    
    return min(1.0, location_changes * 0.3)
```

---

### 2️⃣ Airtime Flushing
**Target**: Airtime credit systems  

**Pattern**:
- Compromised accounts convert airtime to cash  
- Small-value transactions to multiple recipients  
- Rapid transfers within minutes  

**Animated Demo**: *(insert gif or link here)*

**Detection Strategy**:
```python
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
    
    return (recipient_count > 3 and 
            total_value > 5000 and 
            max(t['amount'] for t in transactions) < 1000)
```

---

## 🏦 Banking Fraud
### 3️⃣ Cheque Fraud Syndicates
**Target**: SME business accounts  

**Pattern**:
- Fraudulent cheque books obtained  
- Forged signatures on high-value cheques  
- Presentment at multiple banks simultaneously  

**Detection Strategy**:
```python
def detect_cheque_fraud(cheques):
    """
    Identify duplicate cheque presentation
    :param cheques: List of cheques presented in last 24hrs
    :return: Risk score (0-1)
    """
    cheque_numbers = [c['number'] for c in cheques]
    duplicates = len(cheque_numbers) - len(set(cheque_numbers))
    
    return min(1.0, duplicates * 0.5)
```

---

### 4️⃣ Ghost Loan Applications
**Target**: Digital lenders (Branch, Tala)  

**Pattern**:
- Fake digital identities created  
- Multiple loan applications  
- No repayment intention  

**Detection Strategy**:
```python
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
```

---

## POS & Card Fraud

### 5️⃣ ATM Gas Explosion Thefts
**Target**: ATM cash reserves  

**Pattern**:
- Criminals inject gas into ATM  
- Ignite to explode vault  
- Steal cash during confusion  

**Prevention Checklist**:
- Install gas detection sensors  
- Implement vibration monitoring  
- Use dye packs in cash cassettes  
- Establish police rapid response protocol  

---

### 6️⃣ Card Skimming Clusters
**Target**: Bank ATMs in urban areas  

**Pattern**:
- Skimming devices installed  
- Data transmitted to fraudsters  
- Card cloning within hours  

**Detection Strategy**:
```python
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
```

---

## Contributing New Patterns
Help us expand this library! To contribute:

1. Fork this repository  
2. Create new Markdown file in `/patterns`  
3. Submit a pull request with:
   - Pattern name  
   - Target region/country  
   - Detailed description  
   - Detection strategy (pseudocode or Python)  
   - Include real-world examples (anonymized)  

**Filename example**: `west-africa-momo-fraud.md`  
**Content format**:
```markdown
## [Pattern Name]
### Region: West Africa
### Target: Mobile Money
[Description]
[Detection Strategy]
```

---

### Key Features of This Library:
- **Africa-Specific Patterns**: SIM swap, ATM gas explosions, regional fraud context  
- **Executable Detection Strategies**: Ready-to-run Python functions, practical parameters  
- **Structured Format**: Clear pattern descriptions, prevention checklists, contribution guidelines  
- **Actionable Content**: Can be implemented immediately and scales with community input  

---

### 🎯Benefits for Your Starter Kit:
1. Immediate Value: Working detection code  
2. Educational: Teaches fraud pattern recognition  
3. Community Building: Clear contribution path  
4. Regional Relevance: Focused on African financial systems  

---

### License
This work is licensed under **CC BY-SA 4.0**. You may share and adapt with attribution.

> "Knowledge shared is fraud prevented" — OpenFraudLabs Community
