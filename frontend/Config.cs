class ConfigReader
{
    private IConfiguration _config;
    public ConfigReader(IConfiguration config) {
        _config = config;
    }
    public int PollRateMilliSeconds => int.Parse(@_config["PollRateMilliSeconds"]);
}