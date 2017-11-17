#What is Eventgen?

**The Splunk Event Generator is a utility which allows its users to easily build real-time event generators.**

**Eventgen's overarching goals:**
* Eliminate the need for one-off, hand-coded event generators
* Allow every type of event or transaction to be modeled
* Allow users to build configuration-based event generators, quickly and robustly without having to write code
* Ability to be executed inside of Splunk (relying on a comment event generation framework) as well as outside of Splunk
* Event output can easily be directed to a Splunk input (modular inputs, HEC, etc.), a text file, or any REST endpoint in an easily extendible way
* Easily configurable to make fake data look as real as possible, either by rating events and token replacements by time of the day or by allowing generators to replay real data substituting current time by generating at the exact same timing intervals as the original data
* For scenarios that can't be built using simple token replacements, allow developers to more quickly build sophisticated event generators by simply writing a generator plugin module but re-using the rest of the framework
* Scale up to consume 100% of even of the largest machine