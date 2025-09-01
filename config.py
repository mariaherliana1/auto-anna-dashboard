from src.FileConfig import Files

CONFIG = [
    Files(
        client="gaji-id",
        dashboard="202504/DB/gaji-id.csv",
        output="202504/Processed/gaji-id.csv",
        carrier="Atlasat",
        number1=None,
        number1_rate=0.0,
        number1_rate_type="per_minute",
        number1_chargeable_call_types=[],
        number2=None,
        number2_rate=0.0,
        number2_rate_type="per_minute",
        number2_chargeable_call_types=[],
        rate=720.0,
        rate_type="per_minute",
        s2c=None,
        s2c_rate=0.0,
        s2c_rate_type="per_minute",
        chargeable_call_types=["outbound call", "predictive dialer"],
    ),
]
