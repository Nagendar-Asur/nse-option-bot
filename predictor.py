def get_suggestions(symbol, chain_data):
    if not chain_data:
        return None

    # Example logic: pick CE with highest OI near ATM
    ce_candidates = [row.get('CE') for row in chain_data if 'CE' in row]
    ce_candidates = sorted(
        [c for c in ce_candidates if c and c.get('openInterest')],
        key=lambda x: x['openInterest'], reverse=True
    )

    if ce_candidates:
        top = ce_candidates[0]
        strike = top['strikePrice']
        price = top['lastPrice']
        return f"Buy {strike} CE @ ₹{price} (OI: {top['openInterest']})"
    return None