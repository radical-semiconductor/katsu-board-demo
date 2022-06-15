using Microsoft.AspNetCore.Components.Web;
using Microsoft.AspNetCore.Components.WebAssembly.Hosting;
using MudBlazor.Services;
using frontend;

var builder = WebAssemblyHostBuilder.CreateDefault(args);
builder.RootComponents.Add<App>("#app");
builder.RootComponents.Add<HeadOutlet>("head::after");

string baseaddress;
if (builder.HostEnvironment.IsDevelopment())
    baseaddress = builder.Configuration["ApiBaseAddress"] ?? builder.HostEnvironment.BaseAddress;
else
    baseaddress = builder.HostEnvironment.BaseAddress;
builder.Services.AddScoped(sp => new HttpClient { BaseAddress = new(baseaddress) });
builder.Services.AddSingleton<ConfigReader>();
builder.Services.AddMudServices();

await builder.Build().RunAsync();
