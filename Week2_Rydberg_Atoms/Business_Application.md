![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)


## Step 1: Explain the technical problem you solved in this exercise

<p align="center"><img src="../Week2_Rydberg_Atoms/img/1. IoT.jpg" alt="drawing" width="700" height="500"/></p>

Given a set of objects for instance antennas, satellites, big data, etc, which objects should you choose such that you maximize objects coverage without any overlaps? This problem is an example of an optimization problem known as the maximum independent set problem. The objective is to maximize the number of nodes in a set, so that no edges are contained in the set. 

The maximum independent set problem besides proving the computational complexity of many theoretical problems, serves also as a useful model for real world optimization problems in numerous fields, including information retrieval, signal transmission analysis, classification theory, economics, scheduling, big data, error correcting codes, wireless networks and biomedical engineering [1].

## Step 2: Explain or provide examples of the types of real-world problems this solution can solve

There are several markets where UD-MIS problem can be applied:

### 1.1	Telecommunications.
The global telecom services market size was valued at USD 1,7 trillion in 2020 and is expected to expand at a compound annual growth rate (CAGR) of 5.4% from 2021 to 2028 [2]. 
5G will enable a new set of applications and represents a significant departure from 4G. It is designed to accommodate low-bandwidth applications like sensors in Internet of Things (IoT) as well as high-bandwidth video streaming. The range for a 5G cell site will be around 500 m, much smaller than the 2 to 3 km in 4G. As a result, the cell sites will be much smaller physically and there will have to be many more of them. 

UD-MIS problem can be used as an optimization tool for the efficient location of the growing 5G infrastructure as well for tackling optimization problems in telecommunications traffic big data such as storage organization and information retrieval. The global communication network has undoubtedly been one of the prominent areas for continued technological advancements over the past few decades.

Clients: AT&T Inc., Verizon Communications Inc., Nippon Telegraph and Telephone Corporation (NTT), China Mobile Ltd., Deutsche Telekom AG, SoftBank Group Corp.

### 1.2	Internet of Things
The global Internet of Things (IoT) market size was at $ 330.6 billion in 2020 and is expected to reach $ 875.0 billion by 2025. The IoT is a network of objects connected to the Internet that collect and exchange data using built-in sensors [3]. In 2021, there are more than 10 billion active IoT devices. It’s estimated that the number of active IoT devices will surpass 25.4 billion in 2030. By 2025, there will be 152,200 IoT devices connecting to the internet per minute [4].
The MIS application is discussed in p. 2.

Clients: Accenture PLC, Alcatel-Lucent, Amazon, Atmel Corp.

### 1.3	Cloud Computing
The global cloud computing market size is expected to grow from USD 371.4 billion in 2020 to USD 832.1 billion by 2025 [5].
UD-MIS problem can be used as an optimization tool for the efficient location of the growing data centers networks, but also in big data related optimization fields such as storage organization and information retrieval.

Clients: Amazon, Capgemini, Accenture, Infosys, Tata

### 1.4	Big Data
Big Data Market size was valued at USD 37.69 Billion in 2018 and is projected to reach USD 139.58 Billion by 2026 [6]. 
Big data sets arise in a broad spectrum of scientific, engineering and commercial applications. These include government and military systems, telecommunications, satellite industry, wireless networks, cloud computing, finance, medicine and biotechnology, astrophysics, geographical information systems, etc. 
In many cases, a massive data set can be represented as a very large graph with certain attributes associated with its vertices and edges. Studying the structure of this graph is important for understanding the structural properties of the application it represents, as well as for improving storage organization and information retrieval where MIS can find application. 

Clients: Microsoft Corporation, IBM Corporation, Oracle Corporation, SAP, Amazon Web Services, SAS Institute, Hewlett Packard Enterprise, Dell Technologies, Teradata, Splunk.

### 1.5	Satellite Communications
The global satellite communication market size was valued at USD 66.63 billion in 2020 and is expected to expand at a compound annual growth rate (CAGR) of 9.8% from 2021 to 2028 [7]. At present, several thousand satellites are orbiting the earth. These satellites transfer analog and digital signals carrying data in the form of voices, photographs, and videos to and from one or several locations across the globe.
UD-MIS problem can be used as an optimization tool for the efficient location of the growing satellite network and in big data related optimization fields such as storage organization and information retrieval.

Clients: SES S.A., Viasat, Inc., Intelsat, Telesat, EchoStar Corporation

### 1.6. Error Correcting Memory
ECC Memory market valuation to Reach USD 13.08 Billion by 2025 at a 6.6% CAGR [8].
Error correcting codes lie in the heart of digital technology, making cell phones and modems possible. They are also of a special significance due to increasing importance of reliability issues in internet transmissions. We deal with binary codes of given length correcting certain types of errors. For such codes, a graph can be constructed, in which each vertex corresponds to a binary vector and the edges are built in the way, that each independent set corresponds to a correcting code. The problem of finding the largest code is thus reduced to the maximum independent set problem in the corresponding graph. Exact solutions and estimates for the size of largest error-correcting codes of larger length can be computed by designing and applying even more efficient, possibly parallel, algorithms for solving maximum independent set problem to optimality.

Clients: Kingston Technology Corporation (US), Other World Computing (OWC) (US), Micron Technology Inc. (US), Samsung Electronics Co Ltd (South Korea)

### 2.	Proposal.
The proposal we make to the telecom and IoT network providers (total market size app. $US2 trillion) is as follows:

The combination of high-density small cell sites and low-latency applications makes 5G different. One of the most critical differences is in how routing will expand and become integrated with the transport network. Since the networks will be Internet Protocol based and there are stringent requirements including latency, service providers expect to use routing extensively. Fundamentally, using routing for the service intelligence will be critical to ensure the performance of the various applications running on the 5G transport network. Routing must be flexible and very cost effective, which is driving a high interest in virtual routing [9]. A large mobile provider for instance has tens of thousands of cell sites and that number will increase dramatically with 5G deployments. This fact underscores the importance of routing to building robust services as the locations increase by another order of magnitude [10]. Operators recognize that they need to add routing. The Telecom Infra Project (TIP) members have defined a set of requirements for a Distributed Cell Site Gateway (DCSG) that pushes routing out to the cell site itself [10]. In order to optimize routing on the cell sites MIS can be used for optimal placement of the cell sites themselves. In addition, a new routing protocol design might be needed to accommodate the challenges and opportunities that come with 5G.

Internet of Things (IoT) is an example of low-power and lossy networks (LLNs). The routing protocol for LLNs is a standard routing framework for IoT. Typically, devices forming an LLN possess limited energy, scarce resources, operate in mostly harsh environment and in such a network radio transmission coverage is limited. Therefore, if an LLN is required to cover a relatively large geographical area, multi-hop communication is required. This results in a requirement that devices in a network should rely each other data packets. Hence, a routing protocol to discover and maintain multipoint-to-point (MP-to-P), point-to-point (P-to-P) and point-to-multipoint (P-to-MP) data forwarding paths is needed. An IoT communication architecture using industrial process control as an example use case is depicted in Fig 1.

<p align="center"><img src="../Week2_Rydberg_Atoms/img/2. IoT communication architecture.jpg" alt="drawing" width="700" height="500"/></p>
Fig. 1 IoT communication architecture [11].

In the industrial process control, status of different devices is regularly reported to a central entity/gateway. Hence, there is a need for multipoint-to-point (MP-to-P) communication. Similarly, the central entity sends different control commands to different devices, thus there is a need for point-to-multipoint (P-to-MP) communication. Usually, in an industrial process control system, devices need to communicate with each other to successfully complete a task, hence there is a need for point-to-point (P-to-P) communication. Invariably, the central entity is connected to the Internet, and it stores important information in one of the servers reachable through the Internet or local network. Moreover, a user can interact with the central entity over the Internet to accomplish relevant tasks.

It is known that control overhead of the routing protocol for LLNs (RPL) can result in the protocol’s poor performance in P-to-P and P-to-MP communications especially in its non-storing mode of operation. Moreover, LLNs have dense node deployments. Hence, lowering the control message overhead may not achieve a performance objective. There is a need for a multi-gateway communication architecture that partitions a network in different subnets, and each subnet is under the control of a different gateway. This also highlights the need for inter-gateway communication mechanism so that nodes in different subnets can communicate with each other [11].

There are routing challenges related to node deployment: Unlike conventional networks where network topologies are determined in the beginning of network construction node deployment in Wireless Sensor Networks (WSNs) is either deterministic or randomized. In deterministic deployment, network topologies are decided in advance and remain nearly the same during their lifetime and thus data can be routed through pre-determined paths. However, in randomized deployment, sensor nodes are randomly scattered creating an unknown and unstable network topology. Data routing in this type of node deployment inherently possesses no prior knowledge of network topology and thus requires processing more routing data [12].

Routing mechanism for networks of low power and limited computation capability devices are still under research and development. Some possible research directions are protocols exploiting the redundancy of devices and protocols that allow processing data near data resources to reduce traffic load [10]. With our QC powered platform we help telecom and IoT network service providers to reduce cost and latency and hence be closer and faster to clients needs. How do we do this? With our patented hybrid algorithms we find the optimal configuration of cell sites and routing protocol subnets, close to the data source and in the virtual core. Due to the algorithm’s information retrieval and scheduling capabilities we construct optimal communication channels, thus allowing for smooth integration of 5G and IoT.


<p align="center"><img src="../Week2_Rydberg_Atoms/img/3. Routing Protocl Optimazation.jpg" alt="drawing" width="700" height="500"/></p>
Fig. 2 IoT Routing Protocol Optimization close to the data source or in the virtual core.


## Additional Applications

Expanding from the mainstream communciation network providers.  There is also additional application of our technology for rapidly changing local mesh networks, and satelite broadband internet providers.

Examples: 
- Mesh Networks
  - Amazon SideWalk
  - Apple's Find My Network
- Satelite Networks
  - [Starlink](https://www.starlink.com/)
  - [Project Kuiper from Amazon](https://www.aboutamazon.com/news/company-news/amazon-receives-fcc-approval-for-project-kuiper-satellite-constellation)
- Aid distribution

## Resources

[1] [Butenko, S. 2003. Maximum Independent Set and related problems with applications](http://ufdcimages.uflib.ufl.edu/UF/E0/00/10/11/00001/butenko_s.pdf)

[2] [Global Telecom Services Market](https://www.grandviewresearch.com/industry-analysis/global-telecom-services-market#:~:text=The%20global%20telecom%20services%20market%20size%20was%20valued,rate%20%28CAGR%29%20of%205.0%25%20from%202020%20to%202027)

[3] [Global IoT Market](https://www.marketdataforecast.com/market-reports/internet-of-things-iot-market)

[4] [45 Fascinating IoT Statistics](https://dataprot.net/statistics/iot-statistics/)

[5] [Cloud Computing Market](https://www.marketsandmarkets.com/Market-Reports/cloud-computing-market-234.html#:~:text=%5B322%20Pages%20Report%5D%20The%20global%20cloud%20computing%20market,due%20to%20the%20recent%20COVID-19%20pandemic%20is%20imminent)

[6] [Big Data Market Size](https://www.verifiedmarketresearch.com/product/global-big-data-market-size-and-forecast-to-2025/#:~:text=Big%20Data%20Market%20size%20was%20valued%20at%20USD,a%20CAGR%20of%2017.8%25%20from%202019%20to%202026) 

[7] [Satellite Communication Market](https://www.grandviewresearch.com/industry-analysis/satellite-communication-market#:~:text=The%20global%20satellite%20communication%20market%20size%20was%20valued,rate%20%28CAGR%29%20of%209.2%25%20from%202020%20to%202027)

[8] [ECC Memory Market Valuation](https://www.globenewswire.com/news-release/2021/06/15/2247668/0/en/ECC-Memory-Market-Valuation-to-Reach-USD-13-08-Billion-by-2025-at-a-6-6-CAGR-Asserts-Market-Research-Future-MRFR.html)

[9] [5G Transport Networks and Routing](https://voltanet.io/routing-in-5g-transport-networks/)

[10] [Integrating Routing in 5G Transport](https://www.lightwaveonline.com/5g-mobile/article/14036779/integrating-routing-in-5g-transport)

[11] [Farooq, M. 2020 RIoT: A Routing Protocol for the Internet of Things. The Computer Journal, Volume 63, Issue 6, June 2020, Pages 958–973](https://academic.oup.com/comjnl/article/63/6/958/5808800)

[12] [Trang,T. Routing protocols in Internet of Things](https://wiki.aalto.fi/download/attachments/59704179/trang-tran-routing-protocols-in-iot.pdf?version=1&modificationDate=1324369299000)


# Our Team 

**Matthew Bishara**: I have a background in physics, and currently work in the electric energy sector on computing solutions to optimization problems.

**Brandom Hiles** I have a background in physics, and currently working in the software engineering field mainly working in the API/Database layer.

**William Ngana** 

**Silvia Tzenkova** I have a background in environmental and energy engineering, and currently working on developing hybrid emotion prediction platform.

**Stephen Zhu** I have background in economics, and currently working on developing hybrid emotion prediction platform.


# [Business Proposal](https://drive.google.com/file/d/15tyrOhC6v0zhvc9e9txAAcULB_Ahq2TV/view?usp=sharing)



