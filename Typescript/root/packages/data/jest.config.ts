import type { Config } from "jest";

const config: Config = {
  transform: { "^.+\\.ts?$": "ts-jest" },
  testEnvironment: "node",
  testRegex: ".*\\.(test)?\\.(ts)$",
  moduleFileExtensions: ["ts", "js"],
};

export default config;
