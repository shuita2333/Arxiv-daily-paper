# 📦 其他研究 | 2026年05月15日

> 本类共 **328** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-328](./part-07.md)

---

### 151. [ERPPO: Entropy Regularization-based Proximal Policy Optimization](https://arxiv.org/abs/2605.13131)

**<font color=#1a73e8>作者：</font>** Changha Lee, Gyusang Cho  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-Agent Proximal Policy Optimization (MAPPO) is a variant of the Proximal Policy Optimization (PPO) algorithm, specifically tailored for multi-agent reinforcement learning (MARL). MAPPO optimizes cooperative multi-agent settings by employing a centralized critic with decentralized actors. However, in case of multi-dimensional environment, MAPPO can not extract optimal policy due to non-stationary agent observation. To overcome this problem, we introduce a novel approach, Entropy Regularization-based Proximal Policy Optimization (ERPPO). For the policy optimization, we first define the object detection ambiguity under multi-dimensional observation environment. Distributional Spatiotemporal Ambiguity (DSA) learner is trained to estimate object detection uncertainty in non-stationary constraints. Then, we enhance PPO with a novel Entropy Regularization term. This regularization dynamically adjusts the policy update by applying a stronger (L1) regularization in high-ambiguity observation to encourage significant exploratory actions and a weaker (L2) regularization in low-ambiguity observation to stabilize the proximal policy optimization. This approach is designed to enhance the probability of successful object localization in time-critical operations by reducing detection failures and optimizing search policy. Experiments on a testbed with AirSim-based maritime searching scenarios show that the proposed ERPPO improves accuracy performance. Our proposed method improves higher gradient than MAPPO. Qualitative results confirm that ERPPO effectiveness in terms of suppressing false detection in visually uncertain conditions.

---


### 152. [Extending Blockchain Untraceability with Plausible Deniability](https://arxiv.org/abs/2605.13132)

**<font color=#1a73e8>作者：</font>** Eunchan Park, Kyonghwa Song, Won Hoi Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Traditional blockchain untraceability schemes, such as mixers and privacy coins, obscure the sender-receiver relationship by placing transfers within an anonymity set. This paper studies a stronger goal: whether the transfer event itself can be made unobservable by blending into common decentralized-finance (DeFi) activity. We introduce Deniable Covert Asset Transfer (DCAT), a class of transfers that stage common loss-producing events, such as sandwich and arbitrage operations, so that a sender appears to suffer an ordinary loss while the receiver appears to profit from it. We design and validate two DCAT instantiations: a sandwich-based transfer on Ethereum and an arbitrage-based transfer on Arbitrum. Our experiments show that, under the evaluated settings, DCAT transfers are empirically unobservable on both chains. They are syntactically identical to corresponding maximal extractable value (MEV) activities, classified as ordinary extractions by standard MEV detection tools, and leave the sender and receiver unlinked under representative forensic tools. Since syntactic inspection cannot distinguish DCAT from ordinary MEV activity, we examine whether economic semantics provide useful forensic signals. Through a large-scale study of MEV losses on Ethereum and Arbitrum, we show that key semantic features follow power laws. Extreme losses and repeatedly exploited addresses occur in the wild, and thus are not by themselves definitive evidence of collusion. This gives staged transfers plausible deniability and makes fixed-threshold detection prone to false positives. We therefore develop a multivariate statistical method for forensic triage that ranks incidents by the joint rarity of their economic footprint. Applied to real-world DeFi activity, our method narrows a large search space to suspicious cases for manual investigation; we present three such cases to illustrate this prioritization.

---


### 153. [KAST-BAR: Knowledge-Anchored Semantically-Dynamic Topology Brain Autoregressive Modeling for Universal Neural Interpretation](https://arxiv.org/abs/2605.13133)

**<font color=#1a73e8>作者：</font>** Haoning Wang, Wenchao Yang, Shuai Shen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While EEG foundation models have shown significant potential in universal neural decoding across tasks, their advancement remains constrained by the inadequacy modeling of complex spatiotemporal topology, as well as the inherent modality gap between low-level physiological signals and high-level textual semantics. To address these challenges, we propose a Knowledge-Anchored Semantically-Dynamic Topology Brain Autoregressive Model (KAST-BAR), which dynamically aligns physiological representations derived from multi-level brain topology with an expert-level semantic space. Specifically, we design a Dual-Stream Hierarchical Attention (DSHA) encoder that accurately captures the brain's intrinsic non-Euclidean topology by modeling local temporal dynamics with global spatial contexts. On this basis, a Knowledge-Anchored Semantic Profiler (KASP) is proposed to synthesize physically-grounded and instance-level textual profiles, which subsequently drive a Semantic Text-Aware Refiner (STAR) to dynamically reconstruct EEG representations using Latent Expert Queries. By conducting large-scale pre-training on 21 diverse datasets to build a foundation model, KAST-BAR effectively integrates expert-level medical knowledge into EEG signal representations, consistently achieving superior performance across six downstream tasks. Our code is available at this https URL

---


### 154. [Multi-Modal Guided Multi-Source Domain Adaptation for Object Detection](https://arxiv.org/abs/2605.13140)

**<font color=#1a73e8>作者：</font>** Sangin Lee, Seokjun Kwon, Jeongmin Shin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> General object detection (OD) struggles to detect objects in the target domain that differ from the training distribution. To address this, recent studies demonstrate that training from multiple source domains and explicitly processing them separately for multi-source domain adaptation (MSDA) outperforms blending them for unsupervised domain adaptation (UDA). However, existing MSDA methods learn domain-agnostic features from domain-specific RGB images while preserving domain-specific information from the domain-agnostic feature map. To address this, we propose MS-DePro: Multi-Source Detector with Depth and Prompt, composed of (1) depth-guided localization and (2) multi-modal guided prompt learning. We leverage domain-agnostic input modalities, namely depth maps and text, to encode domain-agnostic characteristics. Specifically, we utilize depth maps to generate domain-agnostic region proposals for localization and integrate multi-modal features to align learnable text embeddings for classification. MS-DePro achieves state-of-the-art performance on MSDA benchmarks, and comprehensive ablations demonstrate the effectiveness of our contributions. Our code is available on this https URL.

---


### 155. [A Constraint Programming Approach for $n$-Day Lookahead Playoff Clinching](https://arxiv.org/abs/2605.13142)

**<font color=#1a73e8>作者：</font>** Gili Rosenberg, Kyle E. C. Booth, J. Kyle Brubaker 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In professional sports, a team has clinched the playoffs if they are guaranteed a postseason spot, regardless of the outcomes of any remaining games. As the season progresses, sports fans and other stakeholders are interested in precisely when, and under what conditions, their team will clinch the playoffs. In this paper, we investigate playoff clinching in the context of the National Hockey League (NHL), where it is computationally challenging to produce clinching scenarios due, in part, to complex tie-breakers. We present an algorithm that determines under which combinations of game outcomes in the next $n$ days a team will clinch the playoffs (i.e., "$n$-day lookahead clinching"). Our approach is a custom tree search which employs various preprocessing techniques, pruning strategies, and node ordering heuristics to efficiently explore the space of possible outcomes. The tree search leverages a constraint programming (CP)-based subroutine for inference that determines if a team has clinched the playoffs for some snapshot in time of the regular season (i.e., "0-day lookahead clinching"). This CP subroutine aims to find a counter-example in which the team being evaluated is eliminated, taking into account qualification rules and the NHL's extensive list of tie-breakers. We validate the efficacy of our algorithm using hundreds of scenarios based on public NHL data for the seasons 2021-22 through 2024-25. The methods introduced can be readily extended to other metrics of interest, including mathematical proof of playoff elimination, clinching the President's Trophy, as well as clinching (or being eliminated from clinching) any other seed in the standings.

---


### 156. [Collaborating in Multi-Armed Bandits with Strategic Agents](https://arxiv.org/abs/2605.13145)

**<font color=#1a73e8>作者：</font>** Idan Barnea, Ofir Schlisselberg, Yishay Mansour  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study collaborative learning in multi-agent Bayesian bandit problems, where strategic agents collectively solve the same bandit instance. While multiple agents can accelerate learning by sharing information, strategic agents might prefer to free-ride and avoid exploration. We consider a setting with persistent agents that participate in multiple time periods. This is in contrast to most previous works on incentives in multi-agent MAB, which assume short-lived agents, namely each agent has a single decision to make and optimizes their expected reward in that single decision. As in the multi-agent MAB model with incentives, our model does not have monetary transfers, and the only incentives are through information sharing.
We propose \texttt{CAOS}, a mechanism that sustains collaboration as a Nash equilibrium while achieving strong regret guarantees. Our results demonstrate that collaborative exploration can be sustained purely through information sharing, achieving performance close to that of fully cooperative systems despite strategic behavior.

---


### 157. [Understanding Generalization through Decision Pattern Shift](https://arxiv.org/abs/2605.13148)

**<font color=#1a73e8>作者：</font>** Huiqi Deng, Yibo Li, Quanshi Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding why deep neural networks (DNNs) fail to generalize to unseen samples remains a long-standing challenge. Existing studies mainly examine changes in externally observable factors such as data, representations, or outputs, yet offer limited insight into how a model's internal decision mechanism evolves from training to test. To address this gap, we introduce Decision Pattern Shift (DPS), a new perspective that defines generalization through the stability of internal decision patterns and quantifies failure as their deviation from those learned during training. Specifically, we represent each sample's decision pattern as a GradCAM-based channel-contribution vector, which captures how feature channels collectively support a prediction, and we propose the DPS metric to measure its discrepancy from the class-average pattern. Empirical analyses across multiple datasets and architectures show that, (i) decision patterns form a highly structured, class-consistent space with strong intra-class cohesion and low inter-class confusion, enabling direct analysis of a model's decision logic; (ii) the DPS magnitude correlates linearly with the generalization gap (nearly all Pearson r > 0.8), revealing generalization as a systematic drift in the model's internal decision mechanism; (iii) the DPS spectrum organizes diverse generalization degradation scenarios (covering ideal generalization, in-distribution degradation, domain shift, out-of-distribution, and shortcut learning) into a continuous trajectory, providing a unified explanation of their failure modes. These findings open up new possibilities for early generalization-risk detection, failure-mode diagnosis, and channel-level defect localization.

---


### 158. [AcquisitionSynthesis: Targeted Data Generation using Acquisition Functions](https://arxiv.org/abs/2605.13149)

**<font color=#1a73e8>作者：</font>** Ishika Agarwal, Sofia Stoica, Emre Can Acikgoz 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Data quality remains a critical bottleneck in developing capable, competitive models. Researchers have explored many ways to generate top quality samples. Some works rely on rejection sampling: generating lots of synthetic samples and filtering out low-quality samples. Other works rely on larger or closed-source models to extract model weaknesses, necessary skills, or a curriculum off of which to base data generation. These works have one common limitation: there is no quantitative approach to measure the impact of the generated samples on the downstream learner. Active learning literature provides exactly this, in the form of acquisition functions. Acquisition functions measure the informativeness and/or influence of data, providing interpretable, model-centric signals. Inspired by this, we propose AcquisitionSynthesis: using acquisition functions as reward models to train language models to generate higher-quality synthetic data. We conduct experiments on classic verifiable tasks of math, medical question-answering, and coding. Our experimental results indicate that (1) student models trained with AcquisitionSynthesis data achieve good performance on in-distribution tasks (2-7% gain) and is more robust to catastrophic forgetting, and (2) AcquisitionSynthesis models can generate data for other models and for low-to-high resource training paradigms. By leveraging acquisition rewards, we seek to demonstrate a principled path toward model-aware self-improvement that surpasses static datasets.

---


### 159. [GenCape: Structure-Inductive Generative Modeling for Category-Agnostic Pose Estimation](https://arxiv.org/abs/2605.13151)

**<font color=#1a73e8>作者：</font>** Jiyong Rao, Yu Wang, Shengjie Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Category-agnostic pose estimation (CAPE) aims to localize keypoints on query images from arbitrary categories, using only a few annotated support examples for guidance. Recent approaches either treat keypoints as isolated entities or rely on manually defined skeleton priors, which are costly to annotate and inherently inflexible across diverse categories. Such oversimplification limits the model's capacity to capture instance-wise structural cues critical for accurate pixel-level localization. To overcome these limitations, we propose GenCape, a Generative-based framework for CAPE that infers keypoint relationships solely from image-based support inputs, without additional textual descriptions or predefined skeletons. Our framework consists of two principal components: an iterative Structure-aware Variational Autoencoder (i-SVAE) and a Compositional Graph Transfer (CGT) module. The former infers soft, instance-specific adjacency matrices from support features through variational inference, embedded layer-wise into the Graph Transformer Decoder for progressive structural priors refinement. The latter adaptively aggregates multiple latent graphs into a query-aware structure via Bayesian fusion and attention-based reweighting, enhancing resilience to visual uncertainty and support-induced bias. This structure-aware design facilitates effective message propagation among keypoints and promotes semantic alignment across object categories with diverse keypoint topologies. Experimental results on the MP-100 dataset show that our method achieves substantial gains over graph-support baselines under both 1- and 5-shot settings, while maintaining competitive performance against text-support counterparts.

---


### 160. [EvObj: Learning Evolving Object-centric Representations for 3D Instance Segmentation without Scene Supervision](https://arxiv.org/abs/2605.13152)

**<font color=#1a73e8>作者：</font>** Jiahao Chen, Zihui Zhang, Yafei Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce EvObj for unsupervised 3D instance segmentation that bridges the geometric domain gap between synthetic pretraining data and real-world point clouds. Current methods suffer from structural discrepancies when transferring object priors from synthetic datasets (e.g., ShapeNet) to real scans (e.g., ScanNet), particularly due to morphological variations and occlusion artifacts. To address this, EvObj integrates two innovative modules: (1) An object discerning module that dynamically refines object candidates, enabling continuous adaptation of object priors to target domains; and (2) An object completion module that reconstructs partial geometries after discovering objects. We conduct extensive experiments on both real-world and synthetic datasets, demonstrating superior 3D object segmentation performance over all baselines while achieving state-of-the-art results.

---


### 161. [Strikingness-Aware Evaluation for Temporal Knowledge Graph Reasoning](https://arxiv.org/abs/2605.13153)

**<font color=#1a73e8>作者：</font>** Rikui Huang, Shengzhe Zhang, Wei Wei  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Temporal Knowledge Graph Reasoning (TKGR) aims at inferring missing (especially future) events from historical data. Current evaluation in TKGR uniformly weights all events, ignoring that most are trivial repetitions, which overestimate the true reasoning ability. Therefore, the rare outstanding events, whose prediction demands deeper reasoning, should be distinguished and emphasized. To this end, we propose a strikingness-aware evaluation framework, which introduces a rule-based strikingness measuring framework (RSMF) to quantify event strikingness by comparing its expected occurrence with peer events derived from temporal rules. Strikingness is then integrated as a weighting factor into metrics like weighted MRR and Hits@k. Experiments on four TKG benchmarks reveal: 1) All representative models perform worse as event strikingness increases, 2) Path-based methods excel on low-strikingness events and representation-based ones on high-strikingness events, 3) We design an ensemble method whose gains stem from fitting trivial events rather than reasoning improvement. Our framework provides a more rigorous evaluation, refocusing the field on predicting outstanding events.

---


### 162. [Unifying Physically-Informed Weather Priors in A Single Model for Image Restoration Across Multiple Adverse Weather Conditions](https://arxiv.org/abs/2605.13158)

**<font color=#1a73e8>作者：</font>** Jiaqi Xu, Xiaowei Hu, Lei Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image restoration under multiple adverse weather conditions aims to develop a single model to recover the underlying scene with high visibility. Weather-related artifacts vary with the particle's distance to the camera according to the established scene visibility analysis, where close and faraway regions are more affected by falling drops and fog effects, respectively. Existing methods fail to consider this weather-specific physical visual process; thus, the restoration performance is limited. In this work, we analyze the common visual factors in adverse weather conditions and present a unified imaging model that considers the individually visible particles and fog-like aggregate scattering effects. Further, we design a novel weather-prior-based network, which leverages the weather-related prior information to help recover the scene by enhancing the features using the estimated occlusion and transmission. Experimental results in multiple adverse scenarios show the superiority of our method against state-of-the-art methods.

---


### 163. [Empowering IoT Security: On-Device Intrusion Detection in Resource Constrained Devices](https://arxiv.org/abs/2605.13159)

**<font color=#1a73e8>作者：</font>** Vasilis Ieropoulos, Eirini Anthi, Theodoros Spyridopoulos 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> IoT devices particularly microcontrollers are challenged by their inherent limitations in processing capabilities, memory capacity, and energy conservation. Securing communication within IoT networks is further complicated by the heterogeneity of devices and the myriad of potential security threats. Our study introduces a lightweight model that utilises machine learning algorithms to achieve a notable detection accuracy of 99% using a decision tree method and 96% using a neural network in identifying cyber threats, including Denial of Service and Man-in-the-Middle attacks which make up the majority of the attacks these devices face. While the decision tree method offers higher accuracy, it requires more computational resources, whereas the neural network approach, despite a slightly lower accuracy, is more memory-efficient. Both methods enhance the real-time monitoring and defence of IoT networks, safeguarding the transmission of data. Additionally, our approach is tailored to conserve memory and optimise computational demands, rendering it suitable for deployment on microcontrollers with limited resources.

---


### 164. [A$_3$B$_2$: Adaptive Asymmetric Adapter for Alleviating Branch Bias in Vision-Language Image Classification with Few-Shot Learning](https://arxiv.org/abs/2605.13161)

**<font color=#1a73e8>作者：</font>** Yiyun Zhou, Zhonghua Jiang, Wenkang Han 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Efficient transfer learning methods for large-scale vision-language models ($e.g.$, CLIP) enable strong few-shot transfer, yet existing adaptation methods follow a fixed fine-tuning paradigm that implicitly assumes a uniform importance of the image and text branches, which has not been systematically studied in image classification. Through extensive analysis, we reveal a Branch Bias issue in vision-language image classification: adapting the image encoder does not always improve performance under out-of-distribution settings. Motivated by this observation, we propose A$_3$B$_2$, an Adaptive Asymmetric Adapter that alleviates Branch Bias in few-shot learning. A$_3$B$_2$ introduces Uncertainty-Aware Adapter Dampening (UAAD), which automatically suppresses image-branch adaptation when prediction uncertainty is high, enabling soft and data-driven control without manual intervention. Architecturally, A$_3$B$_2$ adopts a lightweight asymmetric design inspired by mixture-of-experts with Load Balancing Regularization. Extensive experiments on three few-shot image classification tasks across 11 datasets demonstrate that A$_3$B$_2$ consistently outperforms 11 competitive prompt- and adapter-based baselines.

---


### 165. [GeoBuildBench: A Benchmark for Interactive and Executable Geometry Construction from Natural Language](https://arxiv.org/abs/2605.13167)

**<font color=#1a73e8>作者：</font>** Jinwoong Kim, Rui Yang, Huishuai Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce GeoBuildBench, a benchmark designed to evaluate whether large language models and multimodal agents can ground informal natural-language plane geometry problems into executable geometric constructions. Unlike existing geometry benchmarks that focus on answer correctness or static diagram interpretation, GeoBuildBench treats geometry diagram as an interactive construction task: given a textual problem, an agent must generate a domain-specific language (DSL) program to produce a diagram satisfying explicitly specified geometric objects and verifiable constraints. The benchmark features 489 Chinese textbook-style problems, curated through automated filtering and human validation to ensure text-complete, constructible problem specifications. We evaluate several state-of-the-art multimodal models in a bounded iterative setting and show that, despite reasonable success rates, models frequently exhibit structural hallucinations, missing objects, and failures to satisfy geometric constraints, with limited ability to exploit visual and constraint-based feedback for self-correction. These results highlight geometry construction as a rigorous testbed for grounded, executable reasoning beyond textual or visual plausibility. Our benchmark and code are publicly available.

---


### 166. [Finding the Weakest Link: Adversarial Attack against Multi-Agent Communications](https://arxiv.org/abs/2605.13170)

**<font color=#1a73e8>作者：</font>** Maxwell Standen, Junae Kim, Claudia Szabo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems rely on communication for information sharing and action coordination, which exposes a vulnerability to attacks. We investigate single-victim communication perturbation attacks against Multi-Agent Reinforcement Learning-trained systems and propose methods that use gradient information from the Jacobian to identify which messages, agent, and timesteps are most susceptible to attack and have the greatest impact on the system. We enhance these methods with two proposed adversarial loss functions that trade-off attack success for attack impact which also create more effective perturbations. We empirically demonstrate the effectiveness of our methods against two different multi-agent communication methods in navigation, PredatorPrey, and TrafficJunction environments. Our results show that our novel message selection method achieves a similar or greater impact than random message selection across almost all tested scenarios. Our victim selection, message selection, tempo, and loss functions improve attack effectiveness in half of the thirty scenarios we tested.

---


### 167. [Formal Conjectures: An Open and Evolving Benchmark for Verified Discovery in Mathematics](https://arxiv.org/abs/2605.13171)

**<font color=#1a73e8>作者：</font>** Moritz Firsching, Paul Lezeau, Salvatore Mercuri 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As automated reasoning systems advance rapidly, there is a growing need for research-level formal mathematical problems to accurately evaluate their capabilities. To address this, we present Formal Conjectures, an evolving benchmark of currently 2615 mathematical problem statements formalized in Lean 4. Sourced from areas of active mathematical research, the dataset features 1029 open research conjectures providing a zero-contamination benchmark for mathematical proof discovery, and 836 solved problems for proof autoformalization. Notably, the repository provides a structured interface connecting mathematicians who formalize and clarify problems with the AI systems and humans attempting to solve them. Demonstrating its immediate utility, the benchmark has already been leveraged to make new mathematical discoveries, including the resolution of open research conjectures. We describe our approach to ensuring the correctness of these formalizations in a collaborative open-source project where contributions stem from an active community. In this framework, AI-generated proofs and disproofs serve as a valuable auditing mechanism to iteratively improve the fidelity of the benchmark. Finally, we provide a standardized evaluation setup and report baseline results on frozen evaluation subsets, demonstrating a climbable signal that measures the current frontier of automated reasoning on research-level mathematics.

---


### 168. [When Does Hierarchy Help? Benchmarking Agent Coordination in Event-Driven Industrial Scheduling](https://arxiv.org/abs/2605.13172)

**<font color=#1a73e8>作者：</font>** Ziqi Wang, Yuhao Yang, Zhiwei Ling 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Recent advances in agent and multi-agent systems have shown strong performance on tool use, reasoning, and collaborative tasks. However, existing benchmarks mostly evaluate task completion in weakly coupled environments, and provide limited support for studying coordination in shared, dynamically evolving systems with hierarchy and coupled constraints. This leaves an important question underexplored: when do different coordination paradigms succeed or fail? We introduce Distributed Event-driven Scheduling Benchmark (DESBench), a benchmark for evaluating agent coordination in hierarchical event-driven scheduling. Built on a shared discrete-event driven environment in industrial scheduling, our benchmark captures multi-timescale decision making, partial observability, and dynamically coupled constraints. We define tasks and metrics that evaluate effectiveness, constraint alignment, coordination efficiency, and robustness, and focus on four representative coordination paradigms: centralized, hierarchical, heterarchical, and holonic. These paradigms correspond to distinct mechanisms of information flow, decision authority, and conflict resolution. Our controlled evaluations reveal clear coordination trade-offs: centralized coordination is robust and communication-efficient but scales poorly with difficulty; hierarchical coordination improves efficiency through decomposition but suffers from cross-level misalignment; heterarchical coordination is flexible but communication-heavy; and holonic coordination satisfies constraints well but loses global robustness. These findings demonstrate that coordination design fundamentally shapes agent system behavior in complex environments, revealing structural trade-offs that cannot be captured by outcome metrics alone and underscoring the imperative for more adaptive, principled, and dynamic coordination mechanisms in future MAS research.

---


### 169. [Do Heavy Tails Help Diffusion? On the Subtle Trade-off Between Initialization and Training](https://arxiv.org/abs/2605.13175)

**<font color=#1a73e8>作者：</font>** Hamza Cherkaoui, Hélène Halconruy, Antonio Ocello  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent works have proposed incorporating heavy-tailed (HT) noise into diffusion- and flow-based generative models, with the goals of better recovering the tails of target distributions and improving generative diversity. This motivation is intuitive: if the data are heavy-tailed, HT noise may appear better matched than light-tailed (LT) Gaussian noise. However, replacing Gaussian noise by HT noise also changes the underlying estimation problem. In this paper, we revisit this paradigm through a combined theoretical and empirical study, establishing sampling-error bounds for two representative diffusion models driven by HT and LT noise. We show that HT noise makes the statistical estimation problem harder, leading to less favorable sampling-error bounds. We support these findings with experiments on synthetic and real-world datasets, empirically recovering the predicted error trade-off. Our results call into question a growing design trend in generative modeling and challenge the use of HT noise to improve rare-region exploration.

---


### 170. [Does Engram Do Memory Retrieval in Autoregressive Image Generation?](https://arxiv.org/abs/2605.13179)

**<font color=#1a73e8>作者：</font>** Jinghao Wang, Qiyuan He, Chunbin Gu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The Engram module -- a hash-keyed, O(1) associative memory injected into Transformer layers -- was recently shown to improve large language model pretraining, with the appealing interpretation that it provides a content-addressed shortcut to recurring local token patterns. We ask whether this interpretation transfers to autoregressive (AR) image generation, or whether the observed gains, if any, come from a different mechanism. We adapt the Engram module to vision with 2D spatial $n$-gram hashing, gated fusion, and KV-cache-compatible incremental inference, and inject it into a class-conditional AR generator trained on ImageNet 256x256. Across a sweep of backbone-to-memory budget ratios $\rho{\in}[0.17, 0.90]$, every Engram-augmented variant trails the pure AR baseline in FID, indicating that the module saves backbone FLOPs but does not, by itself, improve sample quality. We then probe how the module is used. A gate-clamp sweep shows that disabling the Engram pathway entirely is catastrophic, yet a tiny constant gate (g=0.10) matches or beats the learned gate -- inconsistent with a heavily content-addressed recall mechanism. A donor-probe experiment shows that swapping the hash inputs for matched, adversarial, or random same-class exemplars produces statistically indistinguishable next-token distributions, while collapsing or randomising the table degrades them by two to three orders of magnitude. Finally, training a model from scratch with the entire memory table frozen to $\mathcal{N}(0, 1)$ noise costs only $\Delta\text{FID}{=}0.10$ and actually raises Inception Score. Together, these findings indicate that the Engram in AR image generation behaves not as a content-addressed retriever but as a gated architectural side-pathway: a hash-keyed residual stream whose benefit is dominated by the pathway itself, with the learned table contributing only a small distributional refinement.

---


### 171. [Stable Attention Response for Reliable Precipitation Nowcasting](https://arxiv.org/abs/2605.13181)

**<font color=#1a73e8>作者：</font>** Penghui Wen, Zexin Hu, Sen Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Precipitation nowcasting remains challenging due to the highly localized, rapidly evolving, and heterogeneous nature of atmospheric dynamics. Although recent methods increasingly adopt attention-based architectures in both unimodal and multimodal settings, they mainly emphasize stronger representation learning and prediction capacity, while paying less attention to the stability of attention responses across samples. In this work, we show that cross-sample instability of attention-response energy is an important and previously underexplored source of forecasting unreliability. Empirically, inaccurate forecasts are associated with larger attention-response energy variance across heads and layers. Theoretically, we show that cross-sample variability can propagate through self-attention, and enlarge a lower bound on prediction error. Based on this insight, we propose HARECast, a Head-wise Attention Response Energy-regulated framework for precipitation nowcasting. HARECast explicitly models head-wise attention-response energy and stabilizes it through a group-wise regularization objective that reduces cross-sample fluctuations. The proposed formulation is generic and applicable to both unimodal and multimodal nowcasting architectures. We instantiate HARECast in a standard forecasting pipeline with reconstruction branches and a diffusion-based predictor, and evaluate it on commonly used benchmarks--SEVIR and MeteoNet. Experimental results demonstrate that HARECast achieves state-of-the-art performance.

---


### 172. [DiffST: Spatiotemporal-Aware Diffusion for Real-World Space-Time Video Super-Resolution](https://arxiv.org/abs/2605.13182)

**<font color=#1a73e8>作者：</font>** Zheng Chen, Ruofan Yang, Jin Han 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based models have shown strong performance in video super-resolution (VSR) and video frame interpolation (VFI). However, their role in the coupled space-time video super-resolution (STVSR) setting remains limited. Existing diffusion-based STVSR approaches suffer from two issues: (1) low inference efficiency and (2) insufficient utilization of spatiotemporal information. These limitations impede deployment. To address these issues, we introduce DiffST, an efficient spatiotemporal-aware video diffusion framework for real-world STVSR. To improve efficiency, we adapt a pre-trained diffusion model for one-step sampling and process the entire video directly rather than operating on individual frames. Furthermore, to enhance spatiotemporal information utilization, we introduce cross-frame context aggregation (CFCA) and video representation guidance (VRG). The CFCA module aggregates information across multiple keyframes to produce intermediate frames. The VRG module extracts video-level global features to guide the diffusion process. Extensive experiments show that DiffST obtains leading results on real-world STVSR tasks. It also maintains high inference efficiency, running about 17$\times$ faster than previous diffusion-based STVSR methods. Code is available at: this https URL.

---


### 173. [N-vium: Mixture-of-Exits Transformer for Accelerated Exact Generation](https://arxiv.org/abs/2605.13190)

**<font color=#1a73e8>作者：</font>** Aleksander Lorenc, Frédéric Berdoz, Joël Mathys 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Improving the inference efficiency of autoregressive transformers typically means reducing FLOPs per token, usually through approximations that degrade model quality. We introduce N-vium, a mixture-of-exits transformer that partially parallelizes computation across depth on standard hardware, increasing effective FLOPs per second rather than minimizing compute per token. N-vium attaches prediction heads at multiple depths and defines the next-token distribution as a learned mixture over these exits, with token-adaptive routing. This formulation strictly generalizes the standard transformer, which is recovered exactly when routing assigns zero mass to all intermediate heads. Sampling from the mixture is exact, and complete KV caches are recovered by deferring the upper-layer computation and batching it with later tokens. We pretrain N-vium at scales up to 1.5B parameters. Our largest model reaches 57.9% wall-clock speedup over a parameter- and data-matched standard transformer at no perplexity cost.

---


### 174. [FIKA-Bench: From Fine-grained Recognition to Fine-Grained Knowledge Acquisition](https://arxiv.org/abs/2605.13193)

**<font color=#1a73e8>作者：</font>** Geng Li, Yuxin Peng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained recognition in everyday life is often not a closed-book classification problem: when encountering unfamiliar objects, humans actively search, compare visual details, and verify evidence before deciding. Existing benchmarks primarily evaluate visually recognition, leaving this active external knowledge acquisition ability underexplored. We study fine-grained knowledge acquisition, where a system must seek, verify, and use external evidence to answer open-ended fine-grained recognition questions. We introduce FIKA-Bench, a leakage-aware and evidence-grounded collection of 311 public-source and real-life instances. To ensure high quality, every example is filtered against frontier closed-book models to remove memorized cases and audited to eliminate image-answer leakage, retaining only samples supported by verified evidence. Our evaluation of latest Large Multimodal Models (LMMs) and agents reveals that the task remains a formidable challenge: the best system reaches only 25.1% accuracy, with no model exceeding 30%. Crucially, we find that merely equipping models with tools is insufficient to bridge this gap; agent failures are predominantly driven by wrong entity retrieval and poor visual judgement. These results show that reliable knowledge acquisition needs better agent designs that focus on fine-grained recognition.

---


### 175. [ECG-NAT: A Self-supervised Neighborhood Attention Transformer for Multi-lead Electrocardiogram Classification](https://arxiv.org/abs/2605.13194)

**<font color=#1a73e8>作者：</font>** Mahsa Gazeran, Sayvan Soleymanbaigi, Fatemeh Daneshfar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electrocardiogram (ECG) arrhythmia classification remains challenging due to signal variability, noise, limited labeled data, and the difficulty in achieving both accuracy and efficiency in models. While self-supervised learning reduces label dependency, most methods target either global contextual features or local morphological patterns, but rarely implement hierarchical multi-scale feature extraction. ECG signals require architectures that simultaneously capture fine-grained beat-level morphology and broader rhythm-level dependencies with computational efficiency. To overcome this limitation, this paper proposes the Electrocardiogram Neighborhood Attention Transformer (ECG-NAT), a novel self-supervised learning approach tailored for multi-lead ECG classification. Our two-stage approach begins with generative pretraining, using a masked autoencoder to reconstruct partially masked ECG signals across multiple diverse datasets, enabling the model to learn robust, domain-invariant representations from unlabeled data. This is followed by discriminative fine-tuning with a dual-loss function that combines supervised contrastive and cross-entropy losses, aligning representation learning with label prediction. The hierarchical attention mechanism efficiently captures multi-scale temporal features from localized beat morphology to broader rhythm patterns at low computational cost. ECG-NAT achieves robust performance on benchmark datasets, with 88.1\% accuracy using only 1\% labeled data, demonstrating strong efficacy in low-resource settings. The framework combines superior classification performance with computational efficiency, making it practical for real-time ECG diagnosis. The code will be made available upon acceptance at: this https URL.

---


### 176. [McCast: Memory-Guided Latent Drift Correction for Long-Horizon Precipitation Nowcasting](https://arxiv.org/abs/2605.13197)

**<font color=#1a73e8>作者：</font>** Penghui Wen, Yu Luo, Lintao Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing precipitation nowcasting methods typically adopt an autoregressive formulation, where future states are predicted from previous outputs. However, such an approach accumulates errors over long rollouts, causing forecasts to drift away from physically plausible evolution trajectories. Although various studies have attempted to alleviate this problem by improving step-wise prediction accuracy, they largely neglect the global temporal evolution of meteorological systems and lack mechanisms to actively correct drift during rollouts. To address this issue, we propose McCast, a memory-guided latent drift correction method for precipitation nowcasting. Rather than treating memory as an unordered dictionary of latent states for passive conditioning, McCast leverages temporally organized memory to actively correct autoregressive latent evolution. Specifically, McCast introduces a Drift-Corrective Memory Bank (DCBank) that explicitly estimates the temporally consistent drift corrections to calibrate the divergent trajectory. DCBank performs drift correction in two stages: a Corrective Latent Extractor first predicts an initial correction from the current prediction and a reference latent state, and a Correction-Aware Memory Retrieval module then refines the initial correction using temporally organized historical memory. By explicitly correcting latent evolution, instead of improving step-wise prediction accuracy only, McCast produces more temporally coherent and reliable long-horizon forecasts. Experiments on two widely used benchmarks, SEVIR and MeteoNet, show that McCast achieves state-of-the-art performance, particularly in challenging long-horizon forecasting scenarios.

---


### 177. [A Hybrid Tucker-LSTM Tensor Network Model for SOC Prediction in Electric Vehicles](https://arxiv.org/abs/2605.13200)

**<font color=#1a73e8>作者：</font>** Han Wang, Ying Wang, Bing Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate state of charge estimation is critical for the success of electric vehicle battery management strategies, but it is well known that conventional estimators suffer from two fundamental shortcomings: cumulative errors that grow over time and reliance on simplified battery models that do not reflect real world dynamics. Therefore, this paper presents a novel hybrid approach combining Tucker tensor decomposition with LSTM networks, using full - lifecycle EV field data for SOC prediction. The inputs are charge status, mileage, voltage, current, cell differentials, and temporal features. Tucker decomposition is skillfully used to reduce dimensionality while maintaining the temporal structure, hence allowing a direct, fair comparison with standard LSTM. The result is unequivocal: Tucker - LSTM outperforms the baseline on all metrics, with MSE dropping 70.5\% (from 21.07 to 6.22 ), MAE improving 48.7\% (from 3.37\% to 1.73\%), RMSE falling from 4.59\% to 2.49\%, and $R^2$ rising from 0.918 to 0.976. Since the experimental results demonstrably demonstrate that tensor decomposition compresses high-dimensional battery data very well without loss of predictive fidelity, this paper naturally opens up a new direction for tensor-based analytics in electric vehicle battery management.

---


### 178. [Switching Successor Measures for Hierarchical Zero-shot Reinforcement Learning](https://arxiv.org/abs/2605.13207)

**<font color=#1a73e8>作者：</font>** Stefan Stojanovic, Alexandre Proutiere  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hierarchical reinforcement learning can improve generalization by decomposing long-horizon decision-making into simpler subproblems. However, existing approaches often rely on restrictive design choices, such as fixed temporal abstractions or goal-conditioned objectives, which largely confine them to goal-reaching tasks and limit their applicability to general reward functions. In this paper, we introduce switching successor measures, an extension of successor measures that enables hierarchical control in zero-shot reinforcement learning without additional supervision, fixed horizons, or manually designed subgoals. We show that switching successor measures arise naturally from classical successor measures while preserving their underlying structure. Building on this result, we propose FB $\pi$-Switch, an algorithm that extracts both a high-level subgoal-selection policy and a low-level control policy directly from forward-backward (FB) representations, allowing hierarchical behavior to emerge from a single learned representation. Experiments on both goal-conditioned and general reward-based tasks show that FB $\pi$-Switch improves over non-hierarchical baselines and matches state-of-the-art hierarchical methods in goal-conditioned settings. These results demonstrate that structured successor representations provide a flexible foundation for hierarchical zero-shot reinforcement learning beyond goal-reaching tasks. Our project website is available at: this https URL.

---


### 179. [Hierarchical Attacks for Multi-Modal Multi-Agent Reasoning](https://arxiv.org/abs/2605.13213)

**<font color=#1a73e8>作者：</font>** Hao Zhou, Tiru Wu, Yan Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-modal multi-agent systems (MM-MAS) have gained increasing attention for their capacity to enable complex reasoning and coordination across diverse modalities. As these systems continue to expand in scale and functionality, investigating their potential vulnerabilities has become increasingly important. However, existing studies on adversarial attacks in multi-agent systems primarily focus on isolated agents or unimodal settings, leaving the vulnerabilities of MM-MAS largely underexplored. To bridge this gap, we introduce HAM$^{3}$, a Hierarchical Attack framework for multi-modal multi-agent systems that decomposes attacks into three interconnected layers. Specifically, at the perception layer, HAM$^{3}$ mounts attacks by perturbing visual inputs, textual inputs, and their fused visual-textual representations. At the communication layer, it performs communication-level attacks that corrupt message content and interaction topology, such as manipulating shared context or communication links to distort collective information flow. At the reasoning layer, it conducts reasoning-level attacks that interfere with each agent's cognitive pipeline, biasing reasoning trajectories and ultimately compromising final decisions. We evaluate HAM$^{3}$ on the GQA benchmark through multi-agent systems built on distinct reasoning paradigms including ReAct, Plan-and-Solve, and Reflexion. Experiments demonstrate that our framework achieves an Attack Success Rate of up to 78.3%, with reasoning-layer attacks being the most effective. More than half of the successful attacks lead multiple agents to produce consistent errors. These findings offer valuable insights for building more robust and interpretable multi-agent intelligence.

---


### 180. [Backdoor Channels Hidden in Latent Space: Cryptographic Undetectability in Modern Neural Networks](https://arxiv.org/abs/2605.13214)

**<font color=#1a73e8>作者：</font>** Marte Eggen, Eirik Reiestad, Kristian Gjøsteen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent cryptographic results establish that neural networks can be backdoored such that no efficient algorithm can distinguish them from a clean model. These guarantees, however, have been confined to stylised architectures of limited practical relevance, leaving open whether comparable undetectability extends to modern, end-to-end trained networks. We construct such an attack mechanism for state-of-the-art architectures, closely aligned to the cryptographic notion of undetectability, by identifying backdoor channels as learned latent directions, and show that the question of undetectability reduces to a hypothesis test between two unknown distributions over model parameters, which we conjecture to be intractable in practice. The consequence of this reframing is significant: if exploitable channels within a network's latent space are statistically indistinguishable from naturally learned directions, an attacker need not introduce foreign structure but can instead exploit the geometry the network already possesses. Demonstrating the approach on ResNet and Vision Transformer architectures trained on standard image classification datasets, the attack achieves both consistently high success rates with negligible clean accuracy degradation, and resists a comprehensive suite of post-training defences, none of which neutralise the backdoor without rendering the model unusable. Our results establish that cryptographic backdoors need not be artefacts requiring exotic architectures or artificial constructions, but identifiable as latent properties inherent to the geometry of learned representations.

---


### 181. [Skill-Aligned Annotation for Reliable Evaluation in Text-to-Image Generation](https://arxiv.org/abs/2605.13223)

**<font color=#1a73e8>作者：</font>** Abdelrahman Eldesokey, Merey Ramazanova, Ahmad Sait 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image (T2I) generation has advanced rapidly, making reliable evaluation critical as performance differences between models narrow. Existing evaluation practices typically apply uniform annotation mechanisms, such as Likert-scale or binary question answering (BQA), across heterogeneous evaluation skills, despite fundamental differences in their nature. In this work, we revisit T2I evaluation through the lens of skill-aligned annotation, where annotation strategies reflect the underlying characteristics of each evaluation skill. We systematically compare skill-aligned annotation against uniform baselines and show that it produces more consistent evaluation signals, with higher inter-annotator agreement and improved stability across models. Finally, we present an automated pipeline that instantiates the proposed evaluation protocol, enabling scalable and fine-grained evaluation with spatially grounded feedback. Our work highlights that improving the foundations of image evaluation can increase reliability and efficiency without simply scaling annotation effort. We hope this motivates further research on refining evaluation protocols as a central component of reliable model assessment.

---


### 182. [ReTool-Video: Recursive Tool-Using Video Agents with Meta-Augmented Tool Grounding](https://arxiv.org/abs/2605.13228)

**<font color=#1a73e8>作者：</font>** Xiao Liu, Nayu Liu, Junnan Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video understanding requires active evidence seeking, motivating tool-augmented video agents for temporal reasoning, cross-modal understanding, and complex question answering. Existing video agents have improved video reasoning with retrieval, memory, frame inspection, and verifier tools, but they still face two limitations: (1) a coarse tool space that lacks fine-grained operations for compositional reasoning; and (2) a flat action space that forces high-level video intents into primitive executable tool calls. In this paper, we address these challenges with two complementary designs. First, we construct a MetaAug-Video Tool Library (MVTL), an extensible tool library with 134 registered tools, including 26 base tools for general multimodal signal processing and 108 meta tools for filtering, aggregation, reranking, formatting, and other intermediate-result operations. MVTL supports dual-level access to both structured video information and raw modal evidence, enabling diverse video reasoning scenarios. Second, we propose ReTool-Video, a recursive tool-using method that grounds high-level video intents into executable tool chains. In ReTool-Video, matched actions are executed directly, while unmatched intents are delegated to a resolver for parameter repair, tool substitution, or decomposition. This allows abstract actions such as temporal merging, cross-modal verification, or repeated-event aggregation to be progressively translated into concrete multimodal operations at runtime. Experiments on MVBench, MLVU, and Video-MME w/o sub. show that ReTool-Video consistently outperforms strong baselines. Further analysis demonstrates that recursive grounding and fine-grained meta tools improve the stability and effectiveness of complex video understanding.

---


### 183. [Improving Code Translation with Syntax-Guided and Semantic-aware Preference Optimization](https://arxiv.org/abs/2605.13229)

**<font color=#1a73e8>作者：</font>** Yuhan Wu, Huan Zhang, Wei Cheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs have shown immense potential for code translation, yet they often struggle to ensure both syntactic correctness and semantic consistency. While preference-based learning offers a promising alignment strategy, it is hindered by unreliable semantic rewards derived from sparse test cases or restrictive reference translations. We argue that a robust semantic reward for code translation must be derived directly from the source code. In this paper, we propose CTO to improve code translation with syntax-guided and semantic-aware preference optimization. Through contrastive learning, we train a cross-lingual semantic model to directly assess functional equivalence between source and translated code. By formulating code translation as a multi-objective optimization problem, this robust semantic signal is seamlessly unified with compiler-based syntactic feedback within the direct preference optimization framework. Extensive experiments on C++, Java, and Python translations demonstrate that CTO significantly outperforms existing baselines and alternative preference optimization strategies.

---


### 184. [Doppler Prompting for Stable mmWave-based Human Pose Estimation](https://arxiv.org/abs/2605.13233)

**<font color=#1a73e8>作者：</font>** Shuntian Zheng, Jiaqi Li, Xiaoman Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Millimeter-wave (mmWave) enables privacy-preserving, illumination-robust human pose estimation (HPE), with each mmWave frame represented as a range-angle-Doppler tensor, providing spatial magnitude for localization and Doppler signatures for motion-related cues. However, existing mmWave-based HPE methods either underutilize or naïvely fuse Doppler signatures with spatial magnitude, disregarding their distinct physical semantics. As a result, non-human Doppler signatures can be misinterpreted as human motion cues, leading to jittery trajectories. We propose PULSE, which converts Doppler signatures into confidence-aware motion prompts and injects them into spatial magnitude reasoning through constrained interactions. By screening Doppler prompts before they influence prediction, PULSE first suppresses spurious spectral motion cues and then uses the screened prompts to stabilize prediction. Across three datasets spanning single- and multi-person settings, PULSE consistently improves pose accuracy and temporal stability, indicating that controlled Doppler prompting is a practical direction for stable mmWave HPE.

---


### 185. [A Hybrid Framework for Natural Language Querying of IFC Models with Relational and Graph Representations](https://arxiv.org/abs/2605.13236)

**<font color=#1a73e8>作者：</font>** Rabindra Lamsal, Sisi Zlatanova, Haowen Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Building Information Modeling (BIM) is widely used in the Architecture, Engineering, and Construction (AEC) industry, but the complexity of Industry Foundation Classes (IFC) limits accessibility for non-expert users. To address this, we introduce IfcLLM, a hybrid framework for natural language interaction with IFC-based BIM models. It transforms IFC models into complementary representations: a relational representation for structured element properties and geometry, and a graph representation for topological relationships. These representations are integrated through iterative retry-and-refine LLM reasoning. We implement the framework using an open-weight LLM (GPT OSS 120B), supporting reproducible and deployment-oriented workflows. Evaluation on three IFC models with queries derived from 30 scenarios shows first-attempt accuracy of 93.3%-100%, with all failures recovered using a fallback LLM. The results show that combining complementary representations with iterative reasoning enables more accessible natural language querying of IFC data while supporting routine BIM analysis tasks.

---


### 186. [Automatic Detection of Reference Counting Bugs in Linux Kernel Drivers](https://arxiv.org/abs/2605.13246)

**<font color=#1a73e8>作者：</font>** Joe Hattori, Naoki Kobayashi, Ken Sakayori  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Reference counting bugs in Linux kernel drivers can lead to severe resource mismanagement and security vulnerabilities. We introduce DrvHorn, a novel automated tool to detect these bugs by reducing reference counting verification to an assertion checking problem leveraging the Linux driver interface. Through efficient modeling of the Linux kernel and aggressive program slicing, DrvHorn discovered 545 bugs, of which 424 were previously unknown, across all platform drivers in v6.6 Linux kernel, with a lower false positive rate of 29.9% compared to prior studies. To address the root causes of these newly discovered bugs, we submitted patches to the Linux kernel, and 45 of them were merged.

---


### 187. [X-Restormer++: 1st Place Solution for the UG2+ CVPR 2026 All-Weather Restoration Challenge](https://arxiv.org/abs/2605.13258)

**<font color=#1a73e8>作者：</font>** Youwei Pan, Leilei Cao, Yingfang Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we present our winning solution for the 8th UG2+ Challenge (CVPR 2026) Track 1: Image Restoration under All-weather Conditions. Our method is built upon the strong baseline framework X-Restormer, which effectively captures both channel-wise global dependencies and spatially-local structural information through its dual-attention design (Multi-DConv Head Transposed Attention and Overlapping Cross-Attention). To further boost the restoration performance, we propose several key improvements. First, we integrate the spatially-adaptive input scaling mechanism from Restormer-Plus to dynamically adjust the spatial weights of the input image, enhancing spatial adaptability. Second, to better preserve structural details and edge information, we introduce a novel Gradient-Guided Edge-Aware (GGEA) loss, which is combined with L1 and Multi-Scale SSIM losses in a unified training objective. Third, we significantly expand the training data by incorporating an extra 24,500 degraded-clean image pairs from FoundIR and WeatherBench alongside the original WeatherStream dataset. With these strategies, our proposed method successfully ranks the 1st place in the challenge.

---


### 188. [Unified generalization analysis for physics informed neural networks](https://arxiv.org/abs/2605.13260)

**<font color=#1a73e8>作者：</font>** Yuka Hashimoto, Tomoharu Iwata  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-Informed Neural Networks (PINNs) and their variational counterparts (VPINNs) are neural networks that incorporate physical laws, making them useful for scientific problems. Existing generalization analyses for PINNs and VPINNs remain limited, often requiring restrictive assumptions such as stability conditions or linear ellipticity. In this paper, we derive generalization bounds for neural networks that involve differentiation with respect to input variables, covering PINNs and VPINNs under a unified framework. We apply Taylor expansion to represent nonlinear differential operators as linear operators on a high-dimensional space, enabling the use of Koopman-based analysis and showing that high-rank networks can generalize well even in settings involving differential operators. We also show that the nonlinearity of the differential operator exponentially enlarges the bound, highlighting its significant impact on generalization.

---


### 189. ["It became a self-fulfilling prophecy": How Lived Experiences are Entangled with AI Predictions in Menstrual Cycle Tracking Apps](https://arxiv.org/abs/2605.13261)

**<font color=#1a73e8>作者：</font>** Wendy Zhou, Pelin Karaturhan, Alexandra Weilenmann 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In menstrual cycle tracking apps (MCTAs), AI-based predictions and insights have become increasingly popular. These features enable users to receive personalized information about their bodies and mental states. However, there is currently little research on how these predictive AI features and explanations affect users' lived experiences. This paper examines human-AI entanglement in MCTAs through 14 semi-structured user interviews and a group autoethnography. These methods uncover the processes leading to this phenomenon. Our results reveal that: (1) users understand their lived experiences in light of AI predictions, although these predictions can be faulty due to imperfect logging practices, (2) the user interface features and AI explanations do not support awareness or critical engagement with this entanglement and meaning-making, and (3) non-normative MCTA users report a sense of isolation in this entangled interaction. Based on our findings, we propose design implications for predictive AI features and explanations.

---


### 190. [Chem-GMNet: A Sphere-Native Geometric Transformer for Molecular Property Prediction](https://arxiv.org/abs/2605.13262)

**<font color=#1a73e8>作者：</font>** Deepak Warrier, Raja Sekhar Pappala  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern SMILES-based chemical language models obtain strong MoleculeNet performance by treating SMILES as generic text and compensating with multi-million-molecule self-supervised pretraining. We ask: when a domain carries structural priors as rich as chemistry's, does it warrant a domain-native transformer rather than a generic one rescued by scale? We answer affirmatively with \textbf{GM-Net} (Geometric Measure Network), a transformer family in which every module is replaced by a sphere-native counterpart, and instantiate it as \textbf{Chem-GMNet}. Three blocks follow: SH-Embedding (tokens as learnable directions on $S^{k-1}$ lifted through a Gegenbauer feature map); DualSKA (a per-head fusion of a linear-time gated Sphere-Flow recurrence whose persistent state we prove is the truncated multipole expansion of the input distribution, and a softmax Sphere-Kernel branch over the same Schoenberg-valid kernel); and SH-FFN (sphere projection $\to$ Gegenbauer lift $\to$ moment readout). On canonical DeepChem scaffold splits, against same-shape ChemBERTa-2 baselines under the chemberta3-faithful protocol: (i) random-initialised, Chem-GMNet wins on 7 of 10 MoleculeNet endpoints at $\sim\!35\%$ fewer parameters; (ii) pretrained on the same 10M-SMILES ZINC corpus as ChemBERTa-2 MLM-10M, it matches or beats the public release on 6 of 8 shared endpoints (5/7 excluding a known ClinTox release anomaly). A $(k,L)$ ablation shows that increasing the sphere dimension from $k\!=\!8$ to $k\!=\!10$ at fixed $L\!=\!3$ lowers ESOL RMSE to $0.938$ at scratch, beating pretrained ChemBERTa-2 MLM-10M on this endpoint without any pretraining at all.

---


### 191. [LightSplit: Practical Privacy-Preserving Split Learning via Orthogonal Projections](https://arxiv.org/abs/2605.13265)

**<font color=#1a73e8>作者：</font>** Mert Cihangiroglu, Alessandro Pegoraro, Phillip Rieger 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Split learning (SL) enables collaborative training by partitioning a neural network across clients and a central server, but the cut-layer interface introduces a key challenge: high-dimensional activations incur substantial communication overhead while exposing representations vulnerable to reconstruction attacks. Existing approaches typically address efficiency or privacy in isolation, relying on additional mechanisms such as sparsification, quantization, or noise injection. We propose LightSplit, which limits information exposure and reduces communication overhead by applying a lightweight fixed orthogonal random projection at the cut layer. Based on Shannon's information theory, this projection acts as an information bottleneck that restricts instance-specific information and suppresses exploitable per-sample signals. By transmitting low-dimensional projections instead of raw activations, the server operates on lifted representations without requiring architectural modifications, ensuring compatibility with existing SL architectures. By avoiding additional trainable components on the client, the method remains lightweight and suitable for edge devices while preserving end-to-end differentiability via exact gradient propagation. As the projection is non-invertible, part of the original representation is irreversibly discarded at the client, LightSplit reduces the information available for reconstruction and limits information exposure. We extensively evaluate LightSplit on state-of-the-art benchmarks in both IID and non-IID settings across varying projection dimensions and client scales. Our results show that the method retains more than 95% of the baseline accuracy at up to 32x reduction in transmitted dimensionality while maintaining stable training dynamics.

---


### 192. [D-VLA: A High-Concurrency Distributed Asynchronous Reinforcement Learning Framework for Vision-Language-Action Models](https://arxiv.org/abs/2605.13276)

**<font color=#1a73e8>作者：</font>** Yucheng Guo, Yongjian Guo, Zhong Guan 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid evolution of Embodied AI has enabled Vision-Language-Action (VLA) models to excel in multimodal perception and task execution. However, applying Reinforcement Learning (RL) to these massive models in large-scale distributed environments faces severe systemic bottlenecks, primarily due to the resource conflict between high-fidelity physical simulation and the intensive VRAM/bandwidth demands of deep learning. This conflict often leaves overall throughput constrained by execution-phase inefficiencies. To address these challenges, we propose D-VLA, a high-concurrency, low-latency distributed RL framework for large-scale embodied foundation models. D-VLA introduces "Plane Decoupling," physically isolating high-frequency training data from low-frequency weight control to eliminate interference between simulation and optimization. We further design a four-thread asynchronous "Swimlane" pipeline, enabling full parallel overlap of sampling, inference, gradient computation, and parameter distribution. Additionally, a dual-pool VRAM management model and topology-aware replication resolve memory fragmentation and optimize communication efficiency. Experiments on benchmarks like LIBERO show that D-VLA significantly outperforms mainstream RL frameworks in throughput and sampling efficiency for billion-parameter VLA models. In trillion-parameter scalability tests, our framework maintains exceptional stability and linear speedup, providing a robust system for high-performance general-purpose embodied agents.

---


### 193. [Differentiable Learning of Lifted Action Schemas for Classical Planning](https://arxiv.org/abs/2605.13282)

**<font color=#1a73e8>作者：</font>** Jonas Reiter, Jakob Elias Gebler, Hector Geffner  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Classical planners can effectively solve very large deterministic MDPs represented in STRIPS or PDDL where states are sets of atoms over objects and relations, and lifted action schemas add or delete these atoms. This compact representation yields strong search heuristics and provides an ideal setting for structural generalization, since lifted relations and action schemas give rise to infinitely many domain instances. A central challenge is to learn these relations and action schemas from data, and recent approaches have addressed this problem using different types of observations. In this work, we develop a novel neural network architecture for learning action schemas from traces where states are fully observed but action arguments are unobserved. The problem is a simplification but an important step towards learning planning domains from sequences of images and action labels, and we aim to solve this simplification in a nearly perfect manner. The challenge lies in learning the action schemas while simultaneously identifying the action arguments from observed state changes. Our approach yields a robust differentiable component that can then be integrated into larger neuro-symbolic models. We evaluate the architecture on various planning domains, where the learned lifted action schemas must recover the ground-truth structure. Additionally, we report experiments on robustness to observation noise and on a variation related to slot-based dynamics models.

---


### 194. [Byzantine-Robust Distributed Sparse Learning Revisited](https://arxiv.org/abs/2605.13283)

**<font color=#1a73e8>作者：</font>** Yuxuan Wang, Lixin Zhang, Kangqiang Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We revisit Byzantine robust distributed estimation for high-dimensional sparse linear models. By combining local $\ell_1$-regularized robust estimation with robust aggregation at the server, the framework applies to pseudo-Huber regression, quantile regression, and sparse SVM. We show that the resulting estimators yield non-asymptotic guarantees and attain near-optimal statistical rates under mild conditions, while remaining communication-efficient. Simulations confirm strong robustness in estimation, support recovery and classification accuracy under various Byzantine attacks.

---


### 195. [Delightful Exploration](https://arxiv.org/abs/2605.13287)

**<font color=#1a73e8>作者：</font>** Ian Osband  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most exploration algorithms search broadly until uncertainty is resolved. When the action space is too large to resolve within budget, practitioners default to $\varepsilon$-greedy, which bounds disruption but spends its override blindly. We introduce \textit{Delight-gated exploration} (DE), a host--override rule that spends exploratory actions only when their prospective delight (expected improvement times surprisal) exceeds a gate price. This practical heuristic recovers a classical result: Pandora's reservation-value rule for costly search, with surprisal setting the effective inspection cost. Resolved arms exit the gate, fresh arms shut off above a prior-determined threshold, and selected linear-bandit overrides consume finite information budget. Across Bernoulli bandits, linear bandits, and tabular MDPs, the same hyperparameters transfer without retuning, and DE shows much weaker regret growth than Thompson Sampling and $\varepsilon$-greedy in the tested unresolved regimes. Delight improves acting for the same reason it improves learning: it prices scarce resources by the product of upside and surprisal.

---


### 196. [What properties of reasoning supervision are associated with improved downstream model quality?](https://arxiv.org/abs/2605.13290)

**<font color=#1a73e8>作者：</font>** Mikołaj Langner, Dzmitry Pihulski, Jan Eliasz 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Validating training data for reasoning models typically requires expensive trial-and-error fine-tuning cycles. In this work, we investigate whether the utility of a reasoning dataset can be reliably predicted prior to training using intrinsic data metrics. We propose a suite of quantitative measures and evaluate their predictive power by fine-tuning 8B and 11B models on semantically distinct variants of a Polish reasoning dataset. Our analysis reveals that these intrinsic metrics demonstrate strong and significant correlations with downstream model performance. Crucially, we find that the predictors of utility are scale-dependent: smaller models rely on alignment-focused metrics to ensure precision, whereas larger models benefit from high redundancy, utilizing verbose traces to solve complex tasks. These findings establish a scale-aware framework for validating reasoning data, enabling practitioners to select effective training sets without the need for exhaustive empirical testing.

---


### 197. [IndicMedDialog: A Parallel Multi-Turn Medical Dialogue Dataset for Accessible Healthcare in Indic Languages](https://arxiv.org/abs/2605.13292)

**<font color=#1a73e8>作者：</font>** Shubham Kumar Nigam, Suparnojit Sarkar, Piyush Patel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most existing medical dialogue systems operate in a single-turn question--answering paradigm or rely on template-based datasets, limiting conversational realism and multilingual applicability. We introduce IndicMedDialog, a parallel multi-turn medical dialogue dataset spanning English and nine Indic languages: Assamese, Bengali, Gujarati, Hindi, Marathi, Punjabi, Tamil, Telugu, and Urdu. The dataset extends MDDial with LLM-generated synthetic consultations, translated using TranslateGemma, verified by native speakers, and refined through a script-aware post-processing pipeline to correct phonetic, lexical, and character-spacing errors. Building on this dataset, we fine-tune IndicMedLM via parameter-efficient adaptation of a quantized small language model, incorporating optional patient pre-context to personalise multi-turn symptom elicitation. We evaluate against zero-shot multilingual baselines, conduct systematic error analysis across ten languages, and validate clinical plausibility through medical expert evaluation.

---


### 198. [Img2CADSeq: Image-to-CAD Generation via Sequence-Based Diffusion](https://arxiv.org/abs/2605.13293)

**<font color=#1a73e8>作者：</font>** Shiyu Tan, Zixuan Zhao, Hao Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Boundary Representation (BRep) is the standard format for Computer-Aided Design (CAD), yet reconstructing high-quality BReps from single-view images remains challenging due to the complexity of topological constraints and operation sequences. We present Img2CADSeq, a multi-stage pipeline that overcomes these limitations by encoding CAD sequences into a three-level hierarchical codebook. Guided by an importance prioritization, this strategy values profiles over details, compressing long sequences into a stable discrete latent space. To bridge the modality gap, we leverage a coarse-to-fine point cloud intermediate, aligning 2D visual features with 3D CAD sequences via contrastive learning to condition a VQ-Diffusion model. Supported by newly introduced CAD-220K and PrintCAD datasets, our approach ensures robust industrial domain adaptation. Extensive experiments demonstrate that Img2CADSeq significantly outperforms state-of-the-art methods, producing standard STEP files that can be directly used in commercial CAD software.

---


### 199. [Discrete Diffusion for Complex and Congested Multi-Agent Path Finding with Sparse Social Attention](https://arxiv.org/abs/2605.13296)

**<font color=#1a73e8>作者：</font>** Yuanzhe Wang, Tian Zhi, Zihang Wei 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-Agent Path Finding (MAPF) is a coordination problem that requires computing globally consistent, collision-free trajectories from individual start positions to assigned goal positions under combinatorial planning complexity. In dense environments, suboptimal initial plans induce compound conflicts that hinder feasible repair. For repair-based solvers like LNS2, initial plan quality critically affects downstream repair, yet this factor remains underexplored. We propose DiffLNS, a hybrid framework that integrates a discrete denoising diffusion probabilistic model (D3PM) with LNS2. The D3PM serves as an initializer with sparse social attention that learns a spatiotemporal prior over coordinated multi-agent action trajectories from expert demonstrations and samples multiple joint plans. Operating directly on the categorical action space, our discrete diffusion preserves the MAPF action structure and samples from a multimodal joint-plan distribution to produce diverse drafts well suited for neighborhood repair. These drafts act as warm starts for downstream repair, which completes unfinished trajectories and resolves remaining conflicts under hard MAPF constraints. Experimental results show that despite being trained only on instances with at most 96 agents, the initializer generalizes to scenarios with up to 312 agents at inference time. Across 20 complex and congested settings, DiffLNS achieves an average success rate of 95.8%, outperforming the strongest tested baseline by 9.6 percentage points and matching or exceeding all baselines in all 20 settings. To the best of our knowledge, this is the first work to leverage discrete diffusion for warm-starting an LNS-based MAPF solver.

---


### 200. [PaMM: Periodic Motif Memory for Atomistic Models with an Explicit Local-Structure Interface](https://arxiv.org/abs/2605.13297)

**<font color=#1a73e8>作者：</font>** Ryan Dong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Periodic crystals repeatedly instantiate similar local coordination motifs across translated cells and chemically related structures, but current equivariant atomistic models usually encode these patterns only implicitly in dense edge features. We introduce PaMM, a periodic motif memory that augments the UMA eSCN-MD edge encoder with explicit pair and triplet lookup features. Pair motifs are keyed by $(Z_j, Z_i, b_r)$ and triplet motifs by $(Z_j, Z_i, Z_k, b_\theta)$, hashed into fixed-size tables and fused with the baseline edge representation through lightweight gate-only and affine-equipped variants. We evaluate PaMM in a matched UMA-S OMAT setting and focus on a narrow question: whether explicit motif memory helps at a fixed intermediate training budget. At the 10k-step checkpoint, both PaMM variants improve over the plain baseline; gate-only gives the best energy MAE, while the affine-equipped variant gives the best force MAE. A matched 20k follow-up keeps the same operating-point picture. Aligned controls show that the gain weakens for pair-only, triplet-only, random-bucket, and parameter-matched MLP alternatives, suggesting that the benefit is tied to structured pair/triplet organization rather than generic added capacity. A within-OMAT24 source-family evaluation also shows small but consistent gains across held-out generation families. We therefore make a focused claim: in the studied UMA-S + OMAT regime, explicit pair/ triplet motif memory is a useful inductive bias for periodic atomistic modeling. We do not claim broad cross-dataset transfer, a uniquely preferred fusion variant, or strong scientific interpretability beyond a more inspectable local-structure interface.

---


> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-328](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
