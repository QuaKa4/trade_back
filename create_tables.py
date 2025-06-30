import sqlite3 as sq

def create_table_collections():
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS collections(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name VARCHAR(96) DEFAULT NULL,
    title VARCHAR(765) DEFAULT NULL,
    create_at DATE DEFAULT NULL,
    update_at DATE DEFAULT NULL
    )""")  # collections
def create_table_security_types():
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS security_types(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            trade_engine_id INTEGER,
            trade_engine_name VARCHAR(45) DEFAULT NULL,
            trade_engine_title VARCHAR(765) DEFAULT NULL,
            security_type_name VARCHAR(93) DEFAULT NULL,
            security_type_title VARCHAR(765) DEFAULT NULL,
            security_group_name VARCHAR(93) DEFAULT NULL,
            stock_type VARCHAR(3) DEFAULT NULL,
            create_at DATE DEFAULT NULL,
            update_at DATE DEFAULT NULL,
            FOREIGN KEY (trade_engine_id) REFERENCES engines (id)
            )""")  # security_types
def create_table_engines():
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS engines(
        id INTEGER PRIMARY KEY NOT NULL,
        name VARCHAR(45) DEFAULT NULL,
        title VARCHAR(765) DEFAULT NULL,
        create_at DATE DEFAULT NULL,
        update_at DATE DEFAULT NULL
        )""")  # engines
def create_table_board_groups():
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS board_groups(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        slug VARCHAR(192) DEFAULT NULL,
        title VARCHAR(765) DEFAULT NULL,
        is_default INTEGER DEFAULT NULL,
        is_traded INTEGER DEFAULT NULL,
        create_at DATE DEFAULT NULL,
        update_at DATE DEFAULT NULL
        )""")  # board_groups
def create_table_markets():
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS markets(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        name VARCHAR(45) DEFAULT NULL,
        title VARCHAR(765) DEFAULT NULL,
        create_at DATE DEFAULT NULL,
        update_at DATE DEFAULT NULL
        )""")  # markets
def create_table_durations():
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS durations(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        interval INTEGER DEFAULT NULL, 
        durations INTEGER DEFAULT NULL,
        days INTEGER DEFAULT NULL,
        title VARCHAR(765) DEFAULT NULL,
        hint VARCHAR(765) DEFAULT NULL,
        create_at DATE DEFAULT NULL,
        update_at DATE DEFAULT NULL
        )""")  # durations
def create_table_inflation_key_rates():
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS inflation_key_rates(
            date INTEGER PRIMARY KEY DEFAULT NULL,
            key_rate VARCHAR(12) DEFAULT NULL,
            inflation VARCHAR(12) DEFAULT NULL,
            target VARCHAR(12) DEFAULT NULL
            )""")  # inflation_key_rates
def create_table_security_group():
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS security_group(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name VARCHAR(93) DEFAULT NULL,
            title VARCHAR(765) DEFAULT NULL,
            is_hidden INTEGER DEFAULT NULL,
            create_at DATE DEFAULT NULL,
            update_at DATE DEFAULT NULL
            )""")  # security_group
def create_table_boards():
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS boards(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        board_group_id INTEGER DEFAULT NULL,
        board_id VARCHAR(12) DEFAULT NULL,
        title VARCHAR(381) DEFAULT NULL,
        is_traded INTEGER DEFAULT NULL,
        create_at DATE DEFAULT NULL,
        update_at DATE DEFAULT NULL
        )""")  # boards
def create_table_share_securities():
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS share_securities(
        sec_id VARCHAR(36) DEFAULT NULL,
        board_id VARCHAR(12),
        short_name VARCHAR(30) DEFAULT NULL,
        prev_price DOUBLE DEFAULT NULL,
        lot_size INTEGER DEFAULT NULL,
        face_value DOUBLE DEFAULT NULL,
        status VARCHAR(3) DEFAULT NULL,
        board_name VARCHAR(381) DEFAULT NULL,
        decimals INTEGER DEFAULT NULL,
        sec_name VARCHAR(90) DEFAULT NULL,
        remarks VARCHAR(24) DEFAULT NULL,
        market_code VARCHAR(12) DEFAULT NULL,
        instr_id VARCHAR(12) DEFAULT NULL,
        sector_id VARCHAR(12) DEFAULT NULL,
        min_step DOUBLE DEFAULT NULL,
        prev_wa_price DOUBLE DEFAULT NULL,
        face_unit VARCHAR(12) DEFAULT NULL,
        prev_date DATE DEFAULT NULL,
        issue_size BIGINT DEFAULT NULL,
        is_in VARCHAR(36) DEFAULT NULL,
        lat_name VARCHAR(90) DEFAULT NULL,
        reg_number VARCHAR(90) DEFAULT NULL,
        prev_legal_close_price DOUBLE DEFAULT NULL,
        currency_id VARCHAR(12) DEFAULT NULL,
        sec_type VARCHAR(3) DEFAULT NULL,
        list_level INTEGER DEFAULT NULL,
        settle_date DATE DEFAULT NULL,
        create_at DATE DEFAULT NULL,
        update_at DATE DEFAULT NULL,
        FOREIGN KEY (board_id) REFERENCES boards(board_id)
        )""")  # share_securities NOT KEYED
def create_table_index_securities():
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS index_securities(
        sec_id VARCHAR(36) DEFAULT NULL,
        board_id VARCHAR(12) NOT NULL,
        name VARCHAR(384) DEFAULT NULL,
        decimals INTEGER DEFAULT NULL,
        short_name VARCHAR(288) DEFAULT NULL,
        lat_name VARCHAR(288) DEFAULT NULL,
        annual_high DOUBLE DEFAULT NULL,
        annual_low DOUBLE DEFAULT NULL,
        currency_id VARCHAR(12) DEFAULT NULL,
        calc_mode VARCHAR(36) DEFAULT NULL,
        created_at DATE DEFAULT NULL,
        updated_at DATE DEFAULT NULL,
        FOREIGN KEY (board_id) REFERENCES boards (board_id)
        )""")  # index_securities NOT KEYED
def create_table_index_histories():
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS index_histories(
        board_id VARCHAR(12) UNIQUE NOT NULL,
        sec_id VARCHAR(36) UNIQUE,
        trade_date DATE UNIQUE DEFAULT NULL,
        short_name VARCHAR(189) DEFAULT NULL,
        name VARCHAR(189) NOT NULL,
        close DOUBLE UNIQUE DEFAULT NULL,
        open DOUBLE UNIQUE DEFAULT NULL,
        high DOUBLE UNIQUE DEFAULT NULL,
        low DOUBLE UNIQUE DEFAULT NULL,
        value DOUBLE UNIQUE DEFAULT NULL,
        duration INTEGER(32) DEFAULT NULL,
        yield DOUBLE DEFAULT NULL,
        decimals INTEGER(32) DEFAULT NULL,
        capitalization DOUBLE DEFAULT NULL,
        currency_id VARCHAR(9) DEFAULT NULL,
        divisor DOUBLE DEFAULT NULL,
        trading_session VARCHAR(9) DEFAULT NULL,
        volume DOUBLE DEFAULT NULL,
        created_at DATE DEFAULT NULL,
        updated_at DATE DEFAULT NULL,
        FOREIGN KEY (board_id) REFERENCES boards (board_id),
        FOREIGN KEY (sec_id) REFERENCES index_securities (sec_id),
        FOREIGN KEY (name) REFERENCES index_securities (board_id)
        )""")  # index_histories
def create_table_share_histories():
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS share_histories(
        board_id VARCHAR(12) UNIQUE NOT NULL,
        trade_date DATE UNIQUE DEFAULT NULL,
        rade_session_date DATE UNIQUE DEFAULT NULL,
        sec_id VARCHAR(36) UNIQUE DEFAULT NULL,
        short_name VARCHAR(189) DEFAULT NULL,
        num_trades DOUBLE DEFAULT NULL,
        value DOUBLE DEFAULT NULL,
        open DOUBLE DEFAULT NULL,
        low DOUBLE DEFAULT NULL,
        high DOUBLE DEFAULT NULL,
        legal_close_price DOUBLE DEFAULT NULL,
        wa_price DOUBLE DEFAULT NULL,
        close DOUBLE DEFAULT NULL,
        volume DOUBLE DEFAULT NULL,
        market_price_2 DOUBLE DEFAULT NULL,
        market_price_3 DOUBLE DEFAULT NULL,
        admitted_quote DOUBLE DEFAULT NULL,
        mp_2_val_trd DOUBLE DEFAULT NULL,
        market_price_3_trades_value DOUBLE DEFAULT NULL,
        admitted_value DOUBLE DEFAULT NULL,
        waval DOUBLE DEFAULT NULL,
        trading_session INTEGER DEFAULT NULL,
        currency_id VARCHAR(9) DEFAULT NULL,
        trend_clspr DOUBLE DEFAULT NULL,
        created_at DATE DEFAULT NULL,
        updated_at DATE DEFAULT NULL,
        FOREIGN KEY (sec_id) REFERENCES share_securities(sec_id)
        FOREIGN KEY (board_id) REFERENCES boards (board_id)
        )""")  # share_histories
def create_table_share_market_quotes():
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS share_market_quotes(
        sec_id VARCHAR(36) UNIQUE NOT NULL,
        board_id VARCHAR(12) UNIQUE NOT NULL,
        bid DOUBLE DEFAULT NULL,
        bid_depth DOUBLE DEFAULT NULL,
        offer DOUBLE DEFAULT NULL,
        offer_depth DOUBLE DEFAULT NULL,
        spread DOUBLE DEFAULT NULL,
        bid_depth_t INTEGER DEFAULT NULL,
        offer_depth_t INTEGER DEFAULT NULL,
        open DOUBLE DEFAULT NULL,
        low DOUBLE DEFAULT NULL,
        high DOUBLE DEFAULT NULL,
        last DOUBLE DEFAULT NULL,
        last_change DOUBLE DEFAULT NULL,
        last_change_percent DOUBLE DEFAULT NULL,
        qty INTEGER DEFAULT NULL,
        value DOUBLE DEFAULT NULL,
        value_usd DOUBLE DEFAULT NULL,
        wa_price DOUBLE DEFAULT NULL,
        last_cng_to_last_wa_price DOUBLE DEFAULT NULL,
        wap_to_prev_wa_price_percent DOUBLE DEFAULT NULL,
        wap_to_prev_wa_price DOUBLE DEFAULT NULL,
        close_price DOUBLE DEFAULT NULL,
        market_price_today DOUBLE DEFAULT NULL,
        market_price DOUBLE DEFAULT NULL,
        last_to_prev_price DOUBLE DEFAULT NULL,
        num_trades INTEGER DEFAULT NULL,
        vol_today INTEGER DEFAULT NULL,
        val_today INTEGER DEFAULT NULL,
        val_today_usd INTEGER DEFAULT NULL,
        etf_settle_price DOUBLE DEFAULT NULL,
        trading_status VARCHAR(32) DEFAULT NULL,
        update_time DATETIME DEFAULT NULL,
        last_bid DOUBLE DEFAULT NULL,
        last_offer DOUBLE DEFAULT NULL,
        l_close_price DOUBLE DEFAULT NULL,
        l_current_price DOUBLE DEFAULT NULL,
        market_price_2 DOUBLE DEFAULT NULL,
        num_bids DOUBLE DEFAULT NULL,
        num_offers DOUBLE DEFAULT NULL,
        change DOUBLE DEFAULT NULL,
        time DATETIME DEFAULT NULL,
        high_bid DOUBLE DEFAULT NULL,
        low_offer DOUBLE DEFAULT NULL,
        price_minus_prev_wa_price DOUBLE DEFAULT NULL,
        open_period_price DOUBLE DEFAULT NULL,
        seq_num BIGINT DEFAULT NULL,
        sys_time DATE DEFAULT NULL,
        closing_auction_price DOUBLE DEFAULT NULL,
        closing_auction_volume DOUBLE DEFAULT NULL,
        issue_capitalization DOUBLE DEFAULT NULL,
        issue_capitalization_update_time DATETIME DEFAULT NULL,
        etf_settle_currency VARCHAR(12) DEFAULT NULL,
        val_today_rur DOUBLE DEFAULT NULL,
        trading_session VARCHAR(12) DEFAULT NULL,
        trend_issue_capitalization DOUBLE DEFAULT NULL,
        data_version INTEGER DEFAULT NULL,
        created_at DATATIME DEFAULT NULL,
        updated_at DATE DEFAULT NULL,
        FOREIGN KEY (boards_id) REFERENCES boards (id),
        FOREIGN KEY (boards_id) REFERENCES share_securities (sec_id)
        )""")  # share_market_quotes

with sq.connect("database.db") as connect:
    cursor = connect.cursor()
    create_table_engines()
    create_table_boards()
    create_table_collections() # share_market_quotes
    create_table_markets()
    create_table_durations()
    create_table_board_groups()
    create_table_index_histories()
    create_table_index_securities()
    create_table_inflation_key_rates()
    create_table_security_group()
    create_table_board_groups()
    create_table_share_securities()
    create_table_share_market_quotes()
    create_table_share_histories()
