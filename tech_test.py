TOTAL_BTC_SUPPLY = 21_000_000
INITIAL_BLOCK_REWARD = 50
HALVING_INTERVAL = 210_000
SAT_CONVERSION = 100_000_000

def calculate_btc_supply():
    block_reward = INITIAL_BLOCK_REWARD
    total_btc_mined = 0
    total_blocks = 0
    halving_count = 0

    while total_btc_mined < TOTAL_BTC_SUPPLY:
        halving_count += 1
        btc_mined_in_this_period = block_reward * HALVING_INTERVAL

        if total_btc_mined + btc_mined_in_this_period > TOTAL_BTC_SUPPLY:
            btc_mined_in_this_period = TOTAL_BTC_SUPPLY - total_btc_mined
        
        total_btc_mined += btc_mined_in_this_period
        total_blocks += HALVING_INTERVAL

        block_reward_in_sats = block_reward * SAT_CONVERSION
        total_supply_in_sats = total_btc_mined * SAT_CONVERSION
        percentage_mined = (total_btc_mined/TOTAL_BTC_SUPPLY)*100

        print(f"Halving #{halving_count}")
        print(f"Block reward: {block_reward}")
        print(f"Block reward in SATS: {block_reward_in_sats:,.0f} SATS")
        print(f"Total supply in SATS: {total_supply_in_sats:,.0f} SATS")
        print(f"Percentage of total supply mined: {percentage_mined:.8f}%\n")

        block_reward /= 2

calculate_btc_supply()