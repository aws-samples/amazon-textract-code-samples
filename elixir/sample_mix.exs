defmodule Elixir.MixProject do
  use Mix.Project

  def project do
    [
      app: :elixir,
      version: "0.1.0",
      elixir: "~> 1.12",
      compilers: Mix.compilers(),
      start_permanent: Mix.env() == :prod,
      deps: deps()
    ]
  end

  # ...

  def deps do
    [
      # TODO: Add this into your project and check the latest version from: https://hexdocs.pm/aws/readme.html#installation
      {:aws, "~> 0.13.0"},
      {:hackney, "~> 1.18"}
    ]
  end

  # ...
end
