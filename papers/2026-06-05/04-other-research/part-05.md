# 📦 其他研究 | 2026年06月05日

> 本类共 **265** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-265](./part-06.md)

---

### 201. [Signed Dual Attention: Capturing Signed Dependencies in Time Series Forecasting](https://arxiv.org/abs/2606.04833)

**<font color=#1a73e8>作者：</font>** Balthazar Courvoisier, Tristan Cazenave  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Initially developed for natural language processing, Transformer architectures and attention mechanisms are now central to a wide range of deep learning models, including applications in time series forecasting. A standard attention mechanism, however, implicitly assumes homophilic interactions, limiting its ability to model data with positive and negative dependencies, such as time series. In this work, we introduce the Signed Dual Attention, a novel attention formulation that captures both positive and negative relational patterns without additional parameters. By leveraging a dual message-passing scheme inspired by correlation structures, Signed Dual Attention propagates both supportive and contrastive information within a single shared block, effectively achieving the expressiveness of two head attention without additional parameters. This module can be seamlessly integrated into existing architectures and can yield performance gains in certain situations, requiring signed relational modeling. This approach opens a pathway toward more expressive and parameter-efficient transformers.

---


### 202. [Prediction Under Imperfect Compression: A Theory of Approximate MDL](https://arxiv.org/abs/2606.04834)

**<font color=#1a73e8>作者：</font>** Qian Li, Xinyu Mao, Shang-Hua Teng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Minimum Description Length (MDL) formalizes the principle of Occam's razor by optimizing the total description length: $L(\mathrm{model})+L(\mathrm{data} \ | \ \mathrm{model})$. For sequential prediction, the MDL method repeatedly selects a model with a minimum objective score of the observed prefix for the next step prediction. Classical MDL prediction theory shows that exact optimization of the MDL objective indeed provides a strong compression guarantee that supports reliable prediction. However, practical machine learning usually can only find models by approximately optimizing the objective function. To bridge this gap, this paper addresses the following fundamental question: Under what forms of approximation and regularization does approximate MDL still guarantee reliable sequential prediction? This work offers a principled characterization. We prove that for any approximation with additive slack $C$ of the more general form of the balanced MDL objective: $\lambda\cdot L(\mathrm{model})+L(\mathrm{data} \ | \ \mathrm{model})$, the cumulative expected squared prediction error is finite for all $\lambda\ge1$. The case $\lambda>1$ is proved by an affinity-telescoping argument, while the boundary case $\lambda=1$ is proved by a likelihood-ratio stopping argument based on exact static MDL bounds. Our results establish that classical MDL regularization remains robust to any fixed additive optimization error. Furthermore, we establish that our characterization of the approximate MDL framework is sharp: When $0<\lambda<1$, overfits can happen to incur infinite cumulative expected error in the universal class of estimable measures, and hence a strong form of model-complexity regularization is necessary. In addition, model selection may fail in every regularized regime $\lambda >0$, under multiplicative approximation, and thus, additive approximation is both sufficient and essential.

---


### 203. [3D Temporal Analysis for Autism Spectrum Disorder Screening During Attention Tasks](https://arxiv.org/abs/2606.04836)

**<font color=#1a73e8>作者：</font>** Inam Qadir, Elizabeth B Varghese, Dena Al-Thani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate Autism Spectrum Disorder (ASD) screening for school-age children is crucial to identify cases that may have been missed earlier and to enable timely interventions supporting social, cognitive, and academic development. Current ASD screening relies on subjective assessments and 2D analysis methods that fail to capture spatial displacement patterns characteristic of ASD behaviors. In this study, a novel 3D temporal analysis framework is presented, built on top of DECA (Detailed Expression Capture and Animation), a 3D modeling framework, to extract comprehensive head pose parameters (including translational components $T_x, T_y, T_z$) and facial expressions independent of pose variations. LSTM and GRU-based temporal classifiers were trained on the extracted 3D features from video data collected from 39 participants (19 ASD, 20 TD) aged 7-12 years during Virtual Reality-Continuous Performance Test tasks. The GRU-based models demonstrated superior performance, with 3D head pose features achieving 83.9\% accuracy and 3D facial features reaching 81.4\% accuracy, outperforming 2D baseline approaches by 10.7\% and 7.5\%, respectively. Furthermore, multimodal fusion of 3D head pose and facial features with PCA-based dimensionality reduction achieved the highest accuracy of 84.6\%, outperforming unimodal approaches. This work establishes a foundation for objective, automated screening tools addressing current diagnostic limitations in ASD identification for school-age populations.

---


### 204. [Uncertainty-Aware End-to-End Co-Design of Neural Network Processors: From Training and Mapping to Fabrication](https://arxiv.org/abs/2606.04850)

**<font color=#1a73e8>作者：</font>** Yuyang Du, Yujun Huang, Gioele Zardini  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Designing a neural network processor is an end-to-end co-design problem: network architecture and training budget determine the inference workload; hardware mapping decisions determine chip area, latency, and energy; and these characteristics govern fabrication yield and manufacturing cost. In practice, these decisions are made in separate stages, and existing co-design methodologies are tightly coupled to specific algorithms, making it difficult to improve one component without reworking the entire pipeline. This paper presents a unified framework, grounded in monotone co-design theory, that composes four interoperable design blocks spanning network training, chip mapping, wafer-level fabrication, and compute resource allocation. Each block exposes only a functionality-resource interface to the rest of the system, so any block can be refined without structural changes elsewhere. A central contribution is the treatment of uncertainty: rather than collapsing stochastic outcomes into point estimates, the framework introduces Confidence, the inverse of success probability, as an explicit and optimizable resource alongside cost, time, and power. Three case studies validate the approach. The first recovers Pareto-optimal implementations across heterogeneous application scenarios. The second confirms that Confidence functions as a continuously tunable design knob rather than a post-hoc diagnostic. The third demonstrates that improving a single block's implementation set automatically propagates to the global Pareto front, without modifying the co-design diagram.

---


### 205. [Rethinking Incompleteness: Formalizing Protocol Divergence and Train-Once Learning for Robust IMVC](https://arxiv.org/abs/2606.04857)

**<font color=#1a73e8>作者：</font>** Haolu Liu, Xiyue Wang, Xuanting Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard IMVC evaluation retrains separate models for different missing-data configurations. We show that this paradigm obscures a fundamental vulnerability: missing rate alone is insufficient to characterize data incompleteness. Specifically, we show that protocols with identical nominal missing rates can differ by up to $50\times$ in their proportion of fully observed samples, inducing drastically different learning regimes. We formalize this phenomenon as incompleteness divergence, providing measures that capture structural disparities across missing-data protocols. We further prove that for a broad class of reconstruction-based objectives, learning becomes structurally ill-posed when the proportion of complete samples falls below a critical threshold, leading to near-random performance. To bypass this theoretical bound, we propose CRAFT (Complete-data Robust Attention-masked Fusion Transformer). CRAFT shifts the burden of robustness from the loss function to the architecture via two key properties: (i) per-sample independence, which removes reliance on complete-sample co-occurrence, and (ii) mask-aware variable-length fusion, which aggregates only observed views through attention masking. This design allows a single model, trained once on complete data, to generalize to diverse missing patterns at inference time without retraining. Extensive experiments on seven benchmarks show that CRAFT matches or outperforms per-configuration baselines while reducing training overhead by $8.8\times$, demonstrating that robustness to missing data can be achieved as an inherent architectural property. Code (CRAFT) and our imvc-audit toolkit are available at this https URL and this https URL.

---


### 206. [Learning Empirically Admissible Neural Heuristics for Combinatorial Search](https://arxiv.org/abs/2606.04860)

**<font color=#1a73e8>作者：</font>** Siddharth Sahay  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Finding optimal solution paths for combinatorial puzzles like the Rubik's Cube, sliding tile puzzles, and Lights Out remains a classical challenge in artificial intelligence. Heuristic search algorithms, such as A* , guarantee path optimality only when using an admissible heuristic-one that never overestimates the true remaining cost-to-go. Deep reinforcement learning (RL) methods like DeepCubeA train deep neural networks to approximate cost-to-go heuristics. However, standard mean-squared error (MSE) training regularly yields overestimations, violating admissibility and compromising solution optimality. In this paper, we introduce a generalizable framework for learning validation-calibrated admissible neural heuristics. We train a value network using an underestimating Admissible Bellman Operator combined with an Asymmetric Loss function to penalize overestimation. To account for residual neural function approximation errors, we propose a post-hoc calibration safety offset computed over validation scrambles. We demonstrate that our calibrated neural heuristics achieve no observed admissibility violations under the evaluation protocol and preserve path optimality in practice while reducing search node expansions by up to 83.0% on a 2 by 2 Rubik's Cube, 19.9% on a 3 by 3 Lights Out grid, and 1.9% on an 8-Puzzle compared to standard analytical baselines.

---


### 207. [IRIS-GAN: Staged Specialist Detection of Deepfake Faces](https://arxiv.org/abs/2606.04863)

**<font color=#1a73e8>作者：</font>** Jaume M. Trenchs, Veronica Sanz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce IRIS-GAN, a specialist forensic detector for synthetic face images under cross-generator shift. Rather than addressing universal synthetic-image detection, we focus on faces generated by generative adversarial networks (GANs), which are state-of-the-art in deepfake content, and train the detector through staged exposure to increasingly demanding GAN families while retaining earlier generators. The final model reaches fake-detection rates above 99% across the GAN families considered and classifies an external real-face dataset with 98.9% accuracy. Grad-CAM analysis further reveals measurable generator-dependent spatial response patterns, which remain informative for a secondary heatmap-only classifier. Out-of-family tests on diffusion-generated faces confirm that IRIS-GAN is a specialist detector, with some capability to reach non-GAN deepfakes. These results establish staged training as an effective strategy for robust GAN-face forensics.

---


### 208. [Provably Reduced Sample Cost in Prior-Guided Hyperparameter Optimization](https://arxiv.org/abs/2606.04866)

**<font color=#1a73e8>作者：</font>** Leona Hennig, Jasmin Brandt, Lukas Fehring 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale hyperparameter optimization (HPO) in automated machine learning (AutoML) consumes substantial computational resources, raising growing concerns about scalability and energy efficiency. Existing methods use prior information heuristically to accelerate both black-box and multi-fidelity settings, but they lack a characterization of how prior informativeness quantitatively reduces sample complexity. In this work, we provide the first distribution-dependent sample complexity bounds for multi-fidelity HPO with priors through the formal lens of fixed-budget best-arm identification. By modeling priors directly over arm means as configuration performance, we derive explicit, distribution-dependent error bounds that quantify the relationship between priors and evaluation budget. Our analysis shows that informative priors, which concentrate probability mass on near-optimal arms, yield reductions in the number of required evaluations, whereas baseline performance is recovered with uninformative or misleading priors. We conduct proof-of-concept experiments on a synthetic benchmark and on LCBench, a common multi-fidelity HPO benchmark for deep learning, to confirm our theoretical results, achieving up to 90% budget reduction while retaining solution quality. Together, our results provide a principled foundation for prior-guided and compute-efficient green AutoML.

---


### 209. [Recent Advances and Trends in Learning-based 3D Representations](https://arxiv.org/abs/2606.04871)

**<font color=#1a73e8>作者：</font>** Adrien Schockaert, Hamid Laga, Hazem Wannous 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The selection of an appropriate 3D representation is a fundamental design decision that dictates the efficiency, quality, and capabilities of modern computer vision and graphics pipelines for tasks such as 3D reconstruction, novel-view synthesis and rendering, shape and motion analysis, recognition, and generation. While traditional representations (\eg meshes, point clouds, and volumetric grids) remain standard outputs of 3D sensors (\eg LiDAR and 3D scanners) and are widely used in downstream applications (\eg editing and simulation), recent neural and primitive-based representations (\eg 3D Gaussian Splatting) offer compact and differentiable alternatives opening a wide range of opportunities in applications such as games, AR/VR, autonomous driving, robot navigation, and medical imaging, to name a few. The goal of this paper is to survey the main families of 3D representations from discrete explicit formats to continuous implicit fields based either on neural rendering or primitive splatting. For each type of representation, we present the general formulation and its variants, discuss its benefits and limitations, and highlight key applications. We conclude the paper by outlining the open challenges and potential directions for future research. Distinct from recent surveys that broadly cover 3D object and scene reconstruction, this paper provides a focused analysis on the evolution of 3D representations themselves. We specifically emphasize the paradigm shift toward implicit representations, offering a novel perspective on how these emerging formats fundamentally alter 3D/4D workflows.

---


### 210. [Hierarchical Space Partition for Surface Reconstruction](https://arxiv.org/abs/2606.04891)

**<font color=#1a73e8>作者：</font>** Minjie Tang, Xiangfei Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating compact polygonal models from point clouds is a key problem in 3D vision and computer graphics. However, due to inherent limitations of LiDAR scanning (e.g. range constraints and occlusions), critical scene information is often missing, leading to degraded reconstruction accuracy. To address this, we propose a plane assembling strategy that effectively recovers missing details while maintaining model compactness. We classify all the planes extracted from the scene into three categories: highly visible, barely visible, and invisible. The invisible planes, which are recovered by scene structure analysis, indicate the missing details. The three types of planes correspond to the three growth priorities. Each plane grows according to the priority level, and the space is partitioned progressively, namely, the hierarchical partition. Subsequently, we generate a watertight polygonal mesh from the partition via a min-cut-based optimization. Finally, comparisons on public datasets show the effectiveness and superiority of our method against mainstream approaches. The project page is available at this https URL.

---


### 211. [ODYSSEY: Reestablishing Confidentiality in Confidential Blockchain via Delegated Execution](https://arxiv.org/abs/2606.04892)

**<font color=#1a73e8>作者：</font>** Ju Yang, Weili Wang, Jianyu Niu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Confidential blockchains leveraging Trusted Execution Environments (TEEs) have garnered extensive attention for transaction confidentiality. In this paper, we first taxonomize two classes of attacks against confidential blockchains, i.e., execution-inference and execution-replay attacks, which exploit TEEs' long-lasting side-channel and state-continuity issues to compromise the confidentiality of existing consortium blockchains. Then, we present ODYSSEY, a confidential blockchain that efficiently mitigates these attacks. The core innovations of ODYSSEY are the following: (1) Its delegation model: clients delegate transaction execution to their designated trustees, while other participants synchronize only the execution results, which significantly reduces the attack surface while preserving confidentiality and system performance. (2) Two novel techniques to improve ODYSSEY's efficiency and security: location-aware concurrent execution and delegation failure handler. Finally, we develop a prototype of ODYSSEY on FISCO BCOS, an enterprise-grade consortium blockchain platform. We have conducted various experiments, and our evaluation results show that in a WAN environment with 3 nodes, ODYSSEY can achieve about 4k throughput while keeping latency as low as 0.4-0.5s.

---


### 212. [Channel Fracture: Architectural Blind Spots in Scheduled Cross-Agent Memory Injection for Multi-Agent Orchestration Systems](https://arxiv.org/abs/2606.04896)

**<font color=#1a73e8>作者：</font>** Levent Liu  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent AI orchestration systems increasingly rely on persistent memory to maintain context across sessions, agents, and tasks. When one agent must inject knowledge into another agent's memory -- a common requirement in hierarchical team architectures -- the delivery mechanism must be architecturally sound. We report the discovery of a systematic failure mode we term channel fracture: a condition where scheduled (cron) agents in orchestration frameworks are silently unable to write to the target agent's persistent memory due to hardcoded memory isolation guards. Through experiments on a production Hermes Agent deployment with five specialized profiles, we tested three injection channels: (A) direct SQLite database writes, (B) target-agent self-writes via memory tools, and (C) cron-delegated writes. Channel C failed completely due to two architectural constraints: skip_memory=True hardcoded at the scheduler layer and dynamic registration of memory tools contingent on _memory_manager initialization, which is bypassed in cron execution contexts. We propose CADVP (Cross-Agent Delivery Verification Protocol) v1.1, a 13-dimension verification framework with a veto-level channel confirmation check (CC-0) that prevents false-positive delivery assurance. We articulate two design principles: the inverse verification principle and the channel matching principle.

---


### 213. [CDPM-Align: Multi-Scale Guidance-Aligned Diffusion Pretraining for Robust Few-Shot Anatomical Landmark Detection](https://arxiv.org/abs/2606.04898)

**<font color=#1a73e8>作者：</font>** Roberto Di Via, Irina Voiculescu, Francesca Odone 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Anatomical landmark detection is a fundamental task in medical image analysis supporting a wide range of diagnostic and interventional workflows. Although recent methods have achieved sub-millimetric localisation, accuracy alone is not sufficient for clinical deployment, requiring reliability and robustness in prediction. Despite its clinical relevance, the impact of representation learning in this context is still underexplored. In this work, we introduce CDPM-align, a multi-scale guidance-aligned conditional diffusion pre-training for anatomical landmark detection. Our experimental setup focuses on a few images and a few annotation regimes. Specifically, we employ three popular heterogeneous small-scale benchmark datasets for representation learning via conditional generative pre-training. Furthermore, we consider low-annotation scenarios for the downstream task of landmark detection, with 10 and 25 annotated images, reflecting realistic trade-offs between clinical effort and resource constraints for annotations. Our results confirm that generative pre-training enables the model to learn a robust representation. This improves both accuracy and uncertainty on the downstream tasks, advancing towards safe and efficient clinical deployment.

---


### 214. [DIST-FL: Enhancing Security for TEE-based Aggregation in Federated Learning](https://arxiv.org/abs/2606.04899)

**<font color=#1a73e8>作者：</font>** Guanlong Wu, Ju Yang, Zhen Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Trusted Execution Environments (TEEs)-aided federated learning protocols emerge as promising solutions to counter server-side adversaries and ensure the trustworthiness of the server. In this paper, we dissect existing protocols and demonstrate that server-side adversaries can still manipulate client selection and replay aggregation to compromise system robustness and privacy, by exploiting TEE limitations, i.e., state rollback and I/O manipulation. To this end, we present DIST-FL, a distributed system of servers guarded by multiple TEEs forming an append-only ledger for privacy-preserved, robust FL aggregation. Specifically, DIST-FL ensures operation linearizability to thwart state rollback attacks and incorporates inputs from reliable servers to mitigate I/O manipulation threats. We implement DIST-FL and conduct evaluations in WAN settings. Experimental results demonstrate that DIST-FL can effectively counter the proposed attacks and match the single-TEE's performance while offering a 6x throughput boost over its counterparts, leveraging TEE's computational advantages.

---


### 215. [CLIF: Cross-layer LEO-ISL Fingerprinting for Physical and Network Attack Detection in Dense LEO Constellations](https://arxiv.org/abs/2606.04901)

**<font color=#1a73e8>作者：</font>** Varun Kohli, Arijit Bhattacharjee, Samar Shailendra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Low-Earth Orbit (LEO) mega-constellations such as Starlink by SpaceX and Kuiper by Amazon rely on optical Inter-Satellite Links (ISLs) for autonomous mesh routing to provide low-latency telecommunication, Internet of Things (IoT), and security services globally. As commercial operators and governments deploy increasingly dense constellations and form multi-operator peering coalitions, ISL integrity becomes critical to both commercial availability and national security. However, there is a lack of real-world data for LEO constellations and existing real-time security approaches focus strictly on physical layer security, leaving blind spots in the coverage of network-layer and composite attacks. In this paper, we present a cross-layer, lightweight behavioral fingerprinting framework that fuses onboard physical-layer measurements with network-layer data to detect anomalies at low computational overhead. We construct an orbital simulation covering the first shells of Starlink (1,584 satellites), Kuiper (1,156 satellites), and a joint multi-operator peering scenario (2,740 satellites), injecting ten attack types that span spoofing, traffic manipulation, and routing subversion at varying severity. We evaluate three unsupervised, per-satellite detectors among which our Mahalanobis-distance-based detector achieves 99.5% recall on Starlink, 99.4% on Kuiper, and 94.8\% on the multi-operator constellation, while maintaining False Positive Rates (FPR) below 0.7%. Our results demonstrate that cross-layer feature fusion is not only necessary for comprehensive security of LEO constellations but highly cost-effective for large-scale networks while fitting into the strict onboard energy budgets of resource-constrained satellites.

---


### 216. ['Your AI Text is not Mine': Redefining and Evaluating AI-generated Text Detection under Realistic Assumptions](https://arxiv.org/abs/2606.04906)

**<font color=#1a73e8>作者：</font>** Nils Dycke, Marina Sakharova, Nico Daheim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although it is generally agreed that AI-generated text poses a broad societal risk, there is no common understanding in the AI-generated text detection literature on what constitutes harmful use. Rather, existing datasets and approaches often define their own criteria and make their own assumptions, sometimes implicitly, and often only loosely related to real-world needs and applications. To address this gap, we here systematically define various notions of AI-generated text and their characteristics. To study these, we collect AITDNA - a new benchmark of human-machine co-constructed texts that is annotated with detailed genesis information, such as the entire edit and AI-interaction history. We benchmark various machine-generated text detectors and find that they often only perform well for specific notions but not as broad detectors. We release code and data publicly.

---


### 217. [TeeDAO: A Decentralized Autonomous Organization for Heterogeneous TEEs](https://arxiv.org/abs/2606.04912)

**<font color=#1a73e8>作者：</font>** Pinshen Xu, Wentao Dong, Guoxing Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Trusted Execution Environments (TEEs) have emerged as a critical technology for safeguarding sensitive data and ensuring code integrity in modern computing systems. However, relying on a single TEE implementation makes systems vulnerable to a central point of attack. Building distributed-trust systems leveraging heterogeneous TEEs helps disperse trust but still faces threats from centralized management and adaptive mobile adversaries. To address these challenges, this paper introduces TeeDAO, a novel three-layer framework that automatically organizes multiple heterogeneous TEE instances and provides unified interfaces to support diverse applications, while ensuring long-term guarantees of availability, integrity, and confidentiality. TeeDAO couples BFT-ordered governance with heterogeneity-aware Distributed Proactive Secret Sharing (DPSS) and Secure Multi-Party Computation (MPC) so that attestation-driven committee changes are consistently reflected in secret recovery, resharing, and computation across a dynamic committee of heterogeneous TEEs. We implement a prototype of TeeDAO, integrating COBRA's DPSS scheme with the HotStuff BFT consensus protocol, and adapt it for Intel SGX, TDX, and Hygon CSV. Evaluations demonstrate that TeeDAO achieves up to 1.8x higher key-value store throughput in a large cluster with 61 nodes compared to state-of-the-art systems, efficient autonomous management, and minimal computation overhead (<18%) for multi-party computation tasks.

---


### 218. [Worker Utility as Hysteresis: A Preisach Model of Transaction Acceptance in Gig Labour Markets](https://arxiv.org/abs/2606.04916)

**<font color=#1a73e8>作者：</font>** Piotr Frydrych  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Worker utility is not observed -- only its consequence is. Each gig transaction produces a single bit: accepted or rejected. We argue this structure points directly to the Preisach hysteresis model as the natural representation of latent worker preferences. The Preisach operator models aggregate output as an integral over a population of binary threshold elements -- precisely the structure that emerges when heterogeneous workers each carry a private acceptance wage. We estimate two latent utility surfaces: acceptance utility U_1(X) and rejection utility U_0(X), via a dual-output neural network (shared layers 256->128, margin loss enforcing U_1 >= U_0). Classification reduces to the Preisach gap U_1(X) - U_0(X), passed into an XGBoost classifier alongside clip-stabilised price-to-threshold encodings. On 36,891 gig transactions, this pipeline achieves Jaccard = 0.827 and ROC AUC = 0.799. The price-to-threshold encoding accounts for +11.0 pp AUC over raw utility features. The model confirms the directional asymmetry hysteresis predicts: price decreases depress completion rates more than equivalent increases raise them. Applied to the full dataset, the model's recommendations simultaneously reduce the total wage bill by 21.3% and increase expected fill rate by 9.7 pp. For 74.2% of transactions, P(accept) already exceeds 0.80; reducing the wage keeps it above threshold (mean post-cut P = 0.972), releasing cost savings (median 31%). For the remaining 25.4%, a median 7% wage increase recovers +43 pp acceptance. A model without an explicit indifference zone cannot execute both moves simultaneously.

---


### 219. [Reproducing, Analyzing, and Detecting Reward Hacking in Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2606.04923)

**<font color=#1a73e8>作者：</font>** Xuekang Wang, Zhuoyuan Hao, Shuo Hou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rubric-based reinforcement learning (RL) uses an LLM-as-a-Judge (LaaJ) to score model outputs according to rubrics as rewards. However, policy models may exploit latent biases in the judge, leading to reward hacking and ineffective or unsafe training outcomes. In real-world rubric-based RL, such hacking behaviors are often subtle and entangled with multiple judge biases, making them difficult to analyze, detect, and mitigate. In this paper, we introduce CHERRL, a controllable hacking environment for rubric-based RL. By injecting known biases into LaaJ, CHERRL enables stable reproduction of reward hacking, explicit observation of reward divergence, and precise identification of hacking onset. This provides a clean experimental testbed for studying the mechanisms and mitigations of reward hacking in rubric-based RL. To demonstrate its utility, we analyze different judge biases from the perspectives of discoverability and exploitability, and explore an agent-based system for automatically detecting reward hacking onset from training logs. The code and environment are publicly available at this https URL.

---


### 220. [Scene-Centric Unsupervised Video Panoptic Segmentation](https://arxiv.org/abs/2606.04925)

**<font color=#1a73e8>作者：</font>** Christoph Reich, Oliver Hahn, Nikita Araslanov 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video panoptic segmentation (VPS) aims to jointly detect, segment, and track all objects while partitioning the video into semantically consistent regions. We introduce the task setting of unsupervised VPS, omitting any human supervision. Existing unsupervised scene understanding works mainly focused on image segmentation tasks; the video domain remains underexplored. We propose VideoCUPS, the first unsupervised VPS approach. VideoCUPS generates temporally consistent panoptic video pseudo-labels from scene-centric videos by exploiting unsupervised depth, motion, and visual cues. Training on these pseudo-labels using a novel Video DropLoss yields an accurate, unsupervised VPS model. To benchmark progress, we introduce a comprehensive evaluation protocol and four competitive baselines, extending state-of-the-art unsupervised panoptic image and instance video segmentation models to VPS. VideoCUPS outperforms all baselines and demonstrates strong label-efficient learning. With VideoCUPS, our evaluation protocol, and baselines, we provide a strong foundation for future research on unsupervised VPS.

---


### 221. [AdaKoop: Efficient Modeling of Nonlinear Dynamics from Nonstationary Data Streams with Koopman Operator Regression](https://arxiv.org/abs/2606.04930)

**<font color=#1a73e8>作者：</font>** Naoki Chihara, Ren Fujiwara, Yasuko Matsubara 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-time data analysis requires the ability to accurately and adaptively address nonlinear dynamics in a nonstationary data stream while preserving computational efficiency. However, nonlinear dynamics are so complex that capturing dynamically changing nonlinear patterns and utilizing them for downstream tasks under strict time constraints is nontrivial. To bridge the gap between nonlinear complexity and computational tractability, this study applies Koopman operator theory, which states that nonlinear dynamics can be represented as linear transitions in an infinite-dimensional space. Building upon finite-dimensional approximations of this operator, we present AdaKoop, an efficient streaming algorithm for modeling nonlinear dynamics over nonstationary data streams. Our approach utilizes a probabilistic framework grounded in Koopman operator theory, treating both raw observations and reproducing kernel Hilbert space (RKHS) features as emissions from latent vectors. This dual-view formulation allows nonlinear dynamics to be expressed as a tractable linear system. Therefore, AdaKoop enables the efficient and stable modeling of nonlinear dynamics in a streaming fashion, avoiding the prohibitive computational costs of iterative nonlinear optimization. Furthermore, to address nonstationarity in data streams, AdaKoop adaptively detects the switching of patterns via statistical hypothesis testing for abrupt pattern shifts and incrementally updates model parameters to handle continuous changes. Extensive experiments on a total of 71 practical benchmark datasets across various domains demonstrate that AdaKoop outperforms state-of-the-art methods in terms of real-time forecasting accuracy and computational efficiency.

---


### 222. [Mean-based algorithms: A lower bound and regret](https://arxiv.org/abs/2606.04931)

**<font color=#1a73e8>作者：</font>** Julius Durmann, Amelie Kleber  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mean-based algorithms are a class of online learning algorithms that assign low probability to actions with low average rewards. Recent work indicates these algorithms converge favorably to serially undominated actions, which approximate Nash equilibria in economic games. However, empirical studies also show slower convergence compared to established algorithms in bandit-feedback scenarios.
We study mean-based algorithms when the time horizon is unknown and only bandit feedback is available. In this setting, we provide the first lower bound on the algorithm-defining sequence $\gamma_t$ that formally establishes a limit on how fast these algorithms can learn. Additionally, we propose two mean-based algorithms: one generalizes $\epsilon$-greedy, and the other extends the mean-based Exp3 to unknown horizons. Our experiments show that mean-based algorithms, although slightly slower, can perform competitively with other bandit-feedback algorithms.
We further analyze the relationship to no-regret algorithms. Depending on the choice of $\gamma_t$, the intersection with no-regret algorithms is non-trivial, and we show that algorithms exist that are both mean-based and no-regret. This adds context to the "exploitability" of this class of algorithms that previous contributions suggest.

---


### 223. [What Type of Inference is Active Inference?](https://arxiv.org/abs/2606.04935)

**<font color=#1a73e8>作者：</font>** Wouter W. L. Nuijten, Mykola Lukashchuk, Thijs van de Laar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Active inference casts decision-making as inference, with the Expected Free Energy (EFE) unifying goal-directed and information-seeking behavior. Recent work showed that EFE minimization can be written as Variational Free Energy (VFE) minimization on a generative model augmented with epistemic priors. We prove that the VFE of the augmented model can be rewritten as the VFE of the predictive model plus explicit entropy-correction terms, making the EFE contribution transparent. We then show that proper EFE-based planning requires combining these epistemic corrections with a planning correction that turns marginal inference into policy optimization, yielding a full variational characterization of EFE-based planning. This clarifies which corrections are needed for cross-entropy planning and for full EFE-based planning. The same entropy-corrected formulation leads to a detailed message-passing scheme for EFE-based planning together with simpler ablations. Experiments on three grid-world environments show that the planning correction already helps when observations are decisive, whereas the additional observation-side epistemic corrections matter most when observations are merely suggestive.

---


### 224. [Clinical Assistant for Remote Engagement Link (CARE-link): A Web-Based Electronic Health Records Software for Managing Diabetes](https://arxiv.org/abs/2606.04952)

**<font color=#1a73e8>作者：</font>** Prince Ebenezer Adjei, Joshua Teye Tettey, Toufiq Musah 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> CARE-link is an open-source, web-based clinical support platform designed to improve the management of gestational diabetes by linking clinicians and patients through an LLM-mediated workflow. The system aggregates patient-generated data outside the hospital, summarizes relevant clinical information, and delivers context-aware decision support to clinicians. For patients, CARE-link provides clear explanations of management plans and delivers timely lifestyle guidance through a WhatsApp interface. The integrated dual-facing design aims to promote continuous monitoring, support individualized care, and reduce the burden of in-clinic follow-ups. Built with a modular architecture, the platform can be adapted to other chronic conditions requiring longitudinal tracking and behavioral support. CARE-link has the potential to enhance clinical oversight, promote patient compliance, and strengthen continuity of care particularly in resource-constrained settings.

---


### 225. [NLLog: Lightweight, Explainable SOC Anomaly Detection via Log-to-Language Rewriting](https://arxiv.org/abs/2606.04957)

**<font color=#1a73e8>作者：</font>** Samuel Ndichu, Tao Ban, Seiichi Ozawa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> System-generated logs underpin security monitoring, yet their rigid template-based format hinders both automated analysis and human comprehension. We present NLLog (Natural-Language Log), a lightweight pipeline that deterministically rewrites parsed templates into WHO-WHAT-SEVERITY sentences, pools them with term-frequency-inverse-document-frequency weighting, classifies sessions with tree ensembles, and back-projects evidence with TreeSHAP for analyst review. On Hadoop Distributed File System (HDFS) and Blue Gene/L (BGL) corpora, NLLog exceeds two reproduced matched-protocol baselines; across HDFS, BGL, and the AIT Alert Data Set, it sustains low false-positive rates with commodity-hardware latency suitable for security operations center triage. Coverage, sparse-versus-dense, faithfulness, and adversarial ablations show that fallback sufficiency is corpus-dependent, that an enrollment-time coverage check can surface refinement requirements before deployment, and that an auditable deterministic rewrite combined with lightweight dense encoding provides a measurable representation layer for log-anomaly detection and triage.

---


### 226. [Be Fair! Can Machine Learning Engineering Agents Adhere to Fairness Constraints?](https://arxiv.org/abs/2606.04971)

**<font color=#1a73e8>作者：</font>** Anna Richter, Julia Stoyanovich, Sebastian Schelter  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning engineering (MLE) agents promise to automate end-to-end ML pipeline development from raw data and natural language instructions, potentially making ML accessible to non-technical domain experts. However, in sensitive and regulated domains, this abstraction creates a responsibility gap: end-users may lack visibility into design choices that affect correctness, robustness, fairness, and regulatory compliance. We argue that existing benchmarks are insufficient to assess whether MLE agents can be safely applied in such settings. We propose desiderata for a responsibility-centered evaluation framework and conduct an exploratory study on melanoma classification, focusing on fairness across skin tones as a responsibility constraint. When evaluating two recent MLE agents, we find that agent-generated pipelines show high variance and consistently underperform manually designed baselines in both predictive quality and fairness, despite fairness-oriented prompts. These preliminary results suggest that further research is needed towards redesigning MLE agents to allow humans to guide the search process and reliably assess the compliance and quality of the generated ML pipelines.

---


### 227. [DeliChess: A Multi-party Dialogue Dataset for Deliberation in Chess Puzzle Solving](https://arxiv.org/abs/2606.04987)

**<font color=#1a73e8>作者：</font>** Xiaochen Zhu, Georgi Karadzhov, Tom Stafford 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-party dialogue is a critical setting for studying collaborative reasoning and decision-making, yet existing datasets rarely focus on structured, in-depth complex reasoning tasks. We introduce DeliChess, a novel dataset of group deliberation dialogues in which participants collaboratively solve multiple-choice chess puzzles. Each group first completes the puzzle individually, then engages in a multi-party discussion before submitting a revised collective answer. The dataset includes 107 dialogues with full transcripts, pre- and post-discussion choices, and metadata on puzzle difficulty and move quality. We evaluate performance using three metrics based on chess engine evaluations, and find that deliberation significantly improves group accuracy. We further analyse the role of probing utterances (i.e., messages that elicit proposals, justifications, or strategic reflection) using a classifier trained on prior deliberation data. While probing makes group performance more variable after discussion, it does not consistently lead to better performance. Our dataset offers a rich testbed for modelling group reasoning, dialogue dynamics, and the resolution of differing perspectives and opinions in a well-defined strategic domain.

---


### 228. [What Can Eye Gaze Teach Us About Real-World Cycling? Insights From the Oxford RobotCycle Project](https://arxiv.org/abs/2606.04989)

**<font color=#1a73e8>作者：</font>** Benjamin Hardin, Efimia Panagiotaki, Daniele De Martini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Although much is known about the physical danger of cycling situations, less is understood about the perceived danger of cycling. Furthermore, perception of danger may be filtered at a subconscious level and therefore difficult for one to self-report. To this end, these subconscious perceptions can be revealed through physiological metrics such as eye gaze. This paper explores the perceived safety of cycling in Oxford, United Kingdom and explores the ability of wearable eye tracking glasses to produce insights about the differences in perception under different environments and events. This paper finds that eye gaze patterns change between using bike lanes, car lanes and shared bus lanes, representing different cognitive challenges of each lane type. This paper presents that different intersections have significantly different eye gaze patterns which may have implications for cyclist stress. Finally, eye gaze patterns differ in the presence of events such as passes and pedestrians in the road compared to when cycling with no events. This paper draws conclusions on the benefits and limitations of using wearable eye trackers to estimate stress and cyclist workload.

---


### 229. [Multi-Camera AR Guidance System for Surgical Instrument Handling and Assembly: Investigating Workload and Efficiency](https://arxiv.org/abs/2606.04992)

**<font color=#1a73e8>作者：</font>** Shiyu Li, Julian Kreimeier, Hannah Schieber 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The handling and assembly of instruments during surgery imposes high cognitive demands on scrub nurses, particularly when instruments are unfamiliar. We present a supporting guidance system for surgical instrumentation that combines multi-camera 6D pose estimation with augmented reality in-situ visualization on a head-mounted display without the requirement for additional markers. Pose estimation and consecutive camera calibration are achieved through known objects. The 6D pose estimation network is trained purely on synthetic data, aiming for better generalizability and real-world applicability. The AR guidance displays tooltip localization cues and step-wise assembly animations. Via gaze-based selection and a foot pedal, users can switch between assembly steps in intraoperative use.
In a technical evaluation, our approach outperforms state-of-art 6D pose estimation. A user study with 29 scrub nurses was conducted in a surgical simulation of knee arthroplasty, comparing the system against a paper manual. AR guidance significantly reduced the perceived workload compared. Objectively, AR guidance reduced task completion time by 21.3\% (4.76 minutes). Specifically, scrub nurses less experienced with the instrument set benefited when using the system. Error frequencies were comparable between conditions. Qualitative feedback highlighted improved process clarity, reduced information overload, and perceived independence. To summarize, our marker-free multi-camera AR guidance approach for surgical instruments can, subjectively and objectively, improve intraoperative instrumentation performance, particularly for untrained scrub nurses.

---


### 230. [New Benchmarking Shows Limited Generalization Power of TCR Antigenic Epitope Prediction Models](https://arxiv.org/abs/2606.04994)

**<font color=#1a73e8>作者：</font>** Yiming Liao, Yiheng Li, Ning Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate computational prediction of T cell receptor (TCR) antigen specificity would transform the study of T cell biology and enable scalable immune engineering, yet existing models lack sufficient sensitivity and specificity for broad applications. A major limitation is the absence of rigorously defined, unseen benchmark datasets that allow unbiased evaluation of model performance and generalizability. Here, we describe two complementary classes of datasets that meet this criterion and argue that they provide both a robust framework for model assessment and a foundation for next-generation TCR-antigen prediction algorithm development.

---


### 231. [GARL: Game-Theoretic Reinforcement Learning for Multi-Agent Strategic Prioritisation](https://arxiv.org/abs/2606.05002)

**<font color=#1a73e8>作者：</font>** Yuxiao Ye, Yiwen Zhang, Huiyuan Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based multi-agent systems are increasingly used for strategic decision-making tasks. In such settings, performance depends not only on individual model capabilities, but also on the policies by which agents interact and adapt. Multi-agent reinforcement learning can optimise these interaction policies, but its reward design often remains task-specific and weakly grounded in interaction structure. To address this gap, we propose GARL, a GAme-theoretic Reinforcement Learning framework for multi-agent strategic prioritisation. GARL formalises strategic prioritisation as a two-stage game: competing agents first allocate strategic resources over a shared candidate set, and a higher-level arbiter then produces the final ranking. The resulting game-theoretic utilities are converted into role-specific reinforcement signals, allowing policy optimisation to be guided by structured interaction. We instantiate GARL on issues-in-dispute ranking, where the goal is to prioritise core issues in legal proceedings. Experiments show that GARL improves ranking performance, enables small open-source LLMs to become competitive with a strong closed-source LLM under the same candidate-ranking setting, and yields gains in legal-domain competence and broader strategic decision-making. Overall, GARL demonstrates how game-theoretic interaction structure can be turned into reinforcement-learning objectives, providing a principled approach to policy optimisation in multi-agent strategic prioritisation.

---


### 232. [M$^3$Eval: Multi-Modal Memory Evaluation through Cognitively-Grounded Video Tasks](https://arxiv.org/abs/2606.05008)

**<font color=#1a73e8>作者：</font>** Jie Huang, Ruixun Liu, Sirui Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As multi-modal models advance towards long-form video understanding, memory emerges as a critical capability. Despite substantial efforts in developing video datasets and benchmarks, existing works primarily focus on perception and reasoning, without systematically evaluating memory: what models retain, how faithfully information is preserved, and how robust memory remains under interference. To address this gap, we introduce M$^3$Eval, the first comprehensive evaluation framework and benchmark for probing different memory dimensions in multi-modal models. Grounded in cognitive psychology, our design features carefully constructed tasks that isolate key aspects of memory. Leveraging M$^3$Eval, we conduct extensive experiments across representative multi-modal models, revealing consistent weaknesses and distinctive behaviors. We find that models struggle to maintain disentangled representations when processing parallel video streams, exhibit interference patterns differing substantially from those observed in human memory, ground memory sources more reliably in the spatial domain than the temporal domain, and demonstrate limited symbolic memory. Collectively, our benchmark provides a valuable resource for future research, while our findings highlight memory as a fundamental yet underexplored capability and offer insights for designing more effective memory mechanisms in multi-modal models. Our code and dataset are available at this https URL.

---


### 233. [CIPER: A Unified Framework for Cross-view Image-retrieval and Pose-estimation](https://arxiv.org/abs/2606.05011)

**<font color=#1a73e8>作者：</font>** Yurim Jeon, Dongseong Seo, Seung-Woo Seo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-view geo-localization estimates the geographic location of a ground image by matching it against an aerial image database. Existing methods tackle this through either large-scale retrieval or precise pose estimation, but not both: retrieval-based methods enable wide-area search at the cost of localization accuracy, while pose estimation methods achieve high precision within only a narrow search space. Naively cascading these pipelines introduces error propagation and inconsistent feature representations. We formulate cross-view geo-localization as a unified problem requiring simultaneous city-scale retrieval and precise 3-DoF pose estimation. We propose CIPER (Cross-view Image-retrieval and Pose-estimation transformER), a single architecture that jointly performs both tasks through mutually beneficial feature learning. CIPER uses a shared transformer encoder with task-specific tokens to disentangle global retrieval features from spatial localization cues. To bridge the large domain gap between ground and aerial views, we introduce a two-way transformer pose decoder that uses ground features as spatial queries for bidirectional cross-attention. A set prediction strategy further enables stable 3-DoF regression under a unified multi-task objective. Experiments on VIGOR, KITTI, and Ford Multi-AV demonstrate competitive performance, especially under limited field-of-view and arbitrary orientation conditions. Code is available at this https URL.

---


### 234. [TaDA: Calibrated Probe Gating for Task-Domain LoRA Merging](https://arxiv.org/abs/2606.05016)

**<font color=#1a73e8>作者：</font>** Huy Quoc To, Fuyi Li, Guangyan Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Combining a task LoRA adapter with a domain LoRA adapter into a single unified model is a practical yet largely unexplored challenge. Existing methods treat both adapters as symmetric peers, applying uniform weights across all layers. We argue that task and domain adapters exhibit a consistent depth-dependent asymmetry across transformer architectures. Domain dominance increases with layer depth, while shallower layers retain stronger task-relevant signals. Motivated by this observation, we propose $\textbf{TaDA}$ ($\textbf{Ta}$sk-$\textbf{D}$omain LoR$\textbf{A}$ Merging), a training-free algorithm that exploits this structure through calibrated probe-guided per-layer gating and per-component subspace-aware merging. The gating assigns individual weights per layer and projection type using a probe signal proved invariant to adapter weight magnitude. The merging discards conflicting singular directions before combining the remaining components. $\textbf{TaDA}$ produces a standard rank-$r$ LoRA adapter with zero inference overhead. On six scientific QA benchmarks with Llama-2-7B, TaDA achieves an average accuracy of 0.452, outperforming DARE-TIES by +3.6 percentage points and obtaining the best result on all six benchmarks. On six image classification benchmarks with ViT-L/16, TaDA reaches 85.9\% average accuracy, improving over the strongest merging baseline while leading in three of the six individual benchmarks.

---


### 235. [Handwriting Extraction and Analysis of Signature Lists in Swiss Popular Initiatives](https://arxiv.org/abs/2606.05018)

**<font color=#1a73e8>作者：</font>** Marco Peer, Thomas Gorges, Mathias Seuret 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Popular initiatives and referendums are central to Swiss democracy, yet the validation of handwritten signature lists remains a labor-intensive manual process. This paper investigates the potential of automated document analysis methods, including OCR and AI-based handwriting analysis, to support this task. We propose a pipeline combining template-based line segmentation with text recognition and writer retrieval techniques, evaluated on a dataset of 443 handwritten entries from 418 writers. Results show that OCR struggles with out-of-vocabulary handwriting, with a CER of 29.6% for first names. In contrast, writer retrieval performs more robustly, reaching an mAP of 50.6%. Furthermore, our experiments indicate that off-the-shelf OCR systems are not sufficiently reliable for transcription of handwritten signature data, particularly for short, out-of-vocabulary entries such as names or addresses. However, writer retrieval methods can effectively identify visually similar entries across signature lists, making them a suitable tool for supporting the detection of potential duplicate submissions based on handwriting similarity.

---


### 236. [Enhancing the MADDPG Algorithm for Multi-Agent Learning via Action Inference and Importance Sampling](https://arxiv.org/abs/2606.05021)

**<font color=#1a73e8>作者：</font>** Marc Walden, Jason Liu, Shaashwath Sivakumar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate multi-agent deep reinforcement learning and propose two enhancements to the Multi-Agent Deep Deterministic Policy Gradient (MADDPG) algorithm. First, we introduce a novel Action Inference mechanism that enables each agent to predict other agents' intended actions, thereby improving the accuracy and stability of its own policy. Second, we apply an importance sampling strategy, using geometric distribution, in the replay buffer to prioritize more recent and informative experiences, which helps mitigate the non-stationarity inherent in multi-agent environments. We evaluate both modifications on the discrete-action Predator-Prey task provided by the PettingZoo library, a flexible Python interface for general multi-agent reinforcement learning benchmarks. Our results indicate that Action Inference is effective in improving learning stability and inter-agent cooperation and that importance sampling using geometric distribution can lead to significant improvements in exploration efficiency over standard MADDPG. Code available at this https URL

---


### 237. [Scaling Expert Feedback with Reflective Edit Propagation in Compositional Knowledge Bases](https://arxiv.org/abs/2606.05023)

**<font color=#1a73e8>作者：</font>** Jiajing Guo, Xueming Li, Jorge Piazentin Ono 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Domain-specific knowledge bases (KBs) encode vertical expertise and proprietary information that organizations depend on, but curating them at scale is a persistent challenge. Although Large Language Models (LLMs) can draft initial entries efficiently, technical accuracy still requires human expert validation, and reviewing entries one by one at scale is impractical. We present Reflective Agent for Identifier Dictionary (RAID), a novel system that transforms individual expert edits into systematic knowledge updates. Unlike traditional "correct-and-save" paradigms, RAID utilizes a reflective agent to infer the underlying semantic intent behind a single expert edit and propagates that correction across the entire KB through a three-step architecture: Intent Inference, Reflection-based Planning, and User Controlled Execution. We evaluated the reflection and propagation performance on a public dataset and conducted a user study with subject matter experts with proprietary data. The evaluation shows RAID's technical feasibility in capturing expert intent and its potential to scale specialized expertise across industrial knowledge bases.

---


### 238. [Anchor3R: Streaming 3D Reconstruction with Transient Anchors for Long-Horizon Visual Mapping](https://arxiv.org/abs/2606.05035)

**<font color=#1a73e8>作者：</font>** Peilin Tao, Chong Cheng, Yuansen Du 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-horizon online visual mapping is a core capability for robot perception, requiring continuous camera-motion and scene-geometry estimation from visual streams under bounded memory and computation. Recent feed-forward 3D reconstruction models provide strong geometric priors, but their streaming variants often predict poses in a fixed coordinate system tied to the first frame or a persistent scene memory. This fixed-gauge design leads to train--test mismatch, attention bias toward early anchors, and accumulated drift on sequences much longer than those seen during training. We propose \emph{Anchor3R}, a streaming 3D reconstruction framework that treats feed-forward reconstruction as current-centric local measurement prediction rather than persistent global-gauge regression. At each time step, Anchor3R predicts window-relative poses and a local pointmap in the current-frame coordinate system, turning streaming reconstruction into relative-pose measurement generation. These measurements support online pose updates, while loop-closure reinsertion and motion averaging align the trajectory and transform local pointmaps into a coherent global reconstruction. Experiments on indoor, outdoor, driving, and RGB-D benchmarks show that Anchor3R improves long-horizon pose accuracy and dense reconstruction quality over existing streaming baselines, while supporting bounded-memory online inference.

---


### 239. [In-Context Graphical Inference](https://arxiv.org/abs/2606.05042)

**<font color=#1a73e8>作者：</font>** Zehua Cheng, Wei Dai, Jiahao Sun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Marginal inference in discrete graphical models forces a choice between exactness and scalability: exact algorithms are intractable for high-treewidth graphs, while iterative approximations (Belief Propagation, variational methods) sacrifice convergence guarantees on frustrated topologies. We argue that this dichotomy stems from a mismatched inductive bias: iterative methods abandon the sequential elimination structure that makes exact inference correct. We introduce In-Context Graphical Inference (ICG-I), an autoregressive Graph Transformer that restores this structure by mimicking Variable Elimination with learned, Tensor- Train-compressed intermediate factors, paired with a Dirichlet output layer and Weighted Conformal Prediction for calibrated, distribution-free coverage guarantees under topological shift. We prove that TT compression errors propagate at most lincarly through the autoregressive chain, that the Dirichlet-Multinomial loss is a proper scoring rule, and that WCP maintains coverage with a quantifiable degradation under estimated density ratios. We conducted intensive experiments to evaluate ICG-I and achieved state-of-the-art performance across all benchmarks. ICG-I reduces MAE from 0.041 (best baseline) to 0.020 on standard instances and achieves 0.048 on N=500 frustrated spin glasses where BP diverges entirely.

---


### 240. [Graph Cascades: Contagion-Based Mesoscopic Rewiring for Structure-Aware Graph Machine Learning](https://arxiv.org/abs/2606.05046)

**<font color=#1a73e8>作者：</font>** Meher Chaitanya, My Le, Luana Ruiz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Graph Cascades, a mesoscopic rewiring strategy for Graph Neural Networks (GNNs) and Graph Transformers (GTs) that captures intermediate-scale graph structure beyond purely local edges or fully global attention. Using contagion-based diffusion processes, Graph Cascades constructs, in O(|V|+|E|) time, an auxiliary graph where node pairs supported by repeated multi-hop reinforcement are promoted to direct neighbors. We theoretically characterize when reinforcement-based rewiring helps: sufficient conditions under which reinforcement-based edge selection is more label-aligned than direct adjacency, an SBM witness in which two-hop reinforcement is perfectly homophilic, and a formalization of mesoscopic connectivity via graph effective resistance. Empirically, across node-classification benchmarks, Graph Cascades improves multiple GNN and sparse-GT backbones, with the most reliable gains observed on heterophilic and moderate- to high-degree homophilic graphs. The theoretical conditions also identify regimes where mesoscopic rewiring is unlikely to be beneficial -- low-degree regular graphs and graphs with structural bottlenecks -- and these predictions match the observed failures. We additionally observe tight correlations between performance and structural properties in the rewired graphs.

---


### 241. [Boosting Self-Consistency with Ranking](https://arxiv.org/abs/2606.05054)

**<font color=#1a73e8>作者：</font>** Maria Marina, Daniil Moskovskiy, Sergey Pletenev 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-consistency improves large language models by sampling multiple reasoning paths and selecting the most frequent answer, but majority voting often fails to recover correct answers that are already present among the samples. We address this limitation with Ranking-Improved Self-Consistency (RISC), which reformulates answer selection in self-consistency as a ranking problem. Instead of relying on a single uncertainty or confidence signal, RISC uses a lightweight LambdaRank model to score candidate answers with five carefully designed features that capture answer frequency, semantic centrality, and reasoning-trace consistency. We evaluate RISC on three datasets under a range of test-time budgets. Across datasets, RISC consistently achieves a better accuracy-efficiency trade-off than standard self-consistency and strong baselines, with particularly large gains on question answering benchmarks. Further analysis shows that the proposed features are individually useful and, more importantly, complementary, highlighting the value of learning to combine multiple informative signals for test-time answer selection.

---


### 242. ["A Glimpse, Not a Gaze": Using Generative AI to Balance Privacy and Awareness in Inter-generational Caregiving](https://arxiv.org/abs/2606.05055)

**<font color=#1a73e8>作者：</font>** Zixi Christina Li, Keiko Katsuragawa, James R. Wallace  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As older adults increasingly prefer to age in place, their adult children often assume the role of informal caregivers. This dynamic creates a distinct tension between the adult child's need for awareness and the older adult's fundamental right to privacy. Traditional monitoring technologies, such as raw video feeds, often compromise the older adult's autonomy. To address this challenge, this study explores the use of generative Artificial Intelligence (GenAI) to create abstract, privacy-preserving ``visual summaries'' of daily activities. We design a 10-day Experience Sampling Method (ESM) study with dyads consisting of older adults and their adult children. Through daily smartphone prompts, participants report their current context and evaluate pre-generated AI sketches, indicating their willingness to share or receive these images. Follow-up interviews will further investigate participants' boundary-setting behaviours. This research aims to quantify the privacy mismatch between generations and provide actionable design guidelines for applying visual abstraction in AI-mediated caregiving tools, ultimately supporting inter-generational connection while protecting user dignity.

---


### 243. [FLAGG: Flexible Autoregressive Graph Generation](https://arxiv.org/abs/2606.05067)

**<font color=#1a73e8>作者：</font>** Samuel Cognolato, Alessandro Sperduti, Luciano Serafini  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Deep Graph Generation's panorama spans two extremes: one-shot and sequential models. The former generates nodes and edges jointly, while the latter samples them autoregressively. Each method performs better in different graph domains depending on size and topology, but neither is applicable to all graph categories. For instance, one-shot methods struggle with generating large graphs, while sequential methods underperform on smaller graphs. A possible way to overcome these limitations is to flexibly combine the two methods in a unique system. In this work, we propose the FLAGG (Flexible Autoregressive Graph Generation) framework, which sequentially generates portions of graphs with one-shot models. FLAGG can apply any one-shot model to make it autoregressive, allowing flexibility in choosing the sequential policy. This policy is specified through a stochastic node removal process, which an Insertion Model learns to reverse. We evaluate FLAGG with the DiGress one-shot model on several data sets of different graph sizes and domains. We show that the approach outperforms both one-shot and autoregressive baselines in terms of sampling quality.

---


### 244. [MaCo-GAN: Manifold-Contrastive Adversarial Learning for Single Image Super-Resolution](https://arxiv.org/abs/2606.05068)

**<font color=#1a73e8>作者：</font>** Daeyoung Han, Seongmin Hwang, Moongu Jeon  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conventional Generative Adversarial Networks (GANs) for Single Image Super-Resolution (SISR) often struggle with hallucinated artifacts, largely because standard discriminators evaluate overall image naturalness rather than strict conditional realism. To address this, we propose MaCo-GAN, a novel manifold-contrastive GAN framework that replaces the conventional adversarial loss with a supervised contrastive objective. A core component of our method is a dynamic fake sample synthesizer that transforms ground truth (GT) data into a spectrum of challenging, perceptually plausible fake images that strictly maintain low-resolution (LR) correspondence. Utilizing these synthesized samples, we establish a robust contrastive minimax game: the generator is trained to attract its predictions toward on-manifold fakes (low distortion) and repel them from off-manifold fakes (high distortion), while the discriminator optimizes the exact opposite. By simply replacing the adversarial loss of a baseline SR model with our proposed objective, we demonstrate consistent improvements in the perception-distortion trade-off across various benchmarks. Extensive ablation studies validate the effectiveness of our framework and provide deep insights into the dynamics of this conditional contrastive game.

---


### 245. [RIDE: An Open Dataset and Benchmark for Train Delay Prediction](https://arxiv.org/abs/2606.05070)

**<font color=#1a73e8>作者：</font>** Clément Elliker, Mathis Le Bail, Clément Mantoux 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Train delay prediction is an important problem for both passengers and railway operators, yet progress in the field remains difficult to assess due to the lack of standardized datasets, prediction targets, and evaluation protocols. To address this gap, we introduce RIDE, an open dataset and benchmark for train delay prediction built at nationwide scale over the Belgian railway network. RIDE covers 94.5M train events, 3.6M journeys, and 35.7M weather records from 2023 to 2025. It is organized as a layered data pipeline from raw railway and weather sources to two public releases: a reusable intermediate relational dataset and model-ready benchmark datasets. The benchmark standardizes the prediction task and the training and testing data. It also provides a unified evaluation protocol that supports direct comparison across models. Using this framework, we provide the first comprehensive comparative evaluation of non-learning, statistical learning, and deep learning models. We show that learning-based methods clearly outperform non-learning models, with graph neural networks achieving the best mean performance, while the strongest learning-based models remain relatively close to one another. Beyond aggregate mean absolute error (MAE) and root mean squared error (RMSE), the framework also provides breakdowns by prediction horizon and delay change, enabling more detailed analysis of model behavior across forecasting regimes.

---


### 246. [InstantRetouch: Efficient and High-Fidelity Instruction-Guided Image Retouching with Bilateral Space](https://arxiv.org/abs/2606.05071)

**<font color=#1a73e8>作者：</font>** Jiarui Wu, Yujin Wang, Ruikang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Language-guided photo retouching aims to adjust color and tone while preserving geometry and texture. Recently, diffusion-based retouching shows a superior visual quality, but often struggles with both fidelity issues due to its generative nature and efficiency because of its iterative sampling process. In this work, we propose an efficient and fidelity-preserving retouching method using bilateral space manipulation, which is both compact and content-decoupled. Specifically, instead of directly editing pixels or image latents, our model predicts a low-resolution bilateral grid of affine transforms, which are sliced using a learned guidance map and then applied to the full-resolution image. This approach yields both high fidelity and improved efficiency. To retain strong priors of a pretrained generative model, we distill a multi-step diffusion model into our bilateral grid framework using Variational Score Distillation, complemented by a prompt alignment loss to guide instruction-following behavior. Additionally, we introduce a new benchmark and evaluate our method across multiple dimensions: fidelity, instruction following, and efficiency. Compared to the latest retouch methods, like Gemini-2.5-Flash (Nano-Banana), our method can avoid content drift, significantly improve latency, and generate visually pleasing edits, while maintaining a high level of fidelity. Project page: this https URL.

---


### 247. [Learning What Not to Impute: An Uncertainty-Aware Diffusion Framework for Meaningful Missingness](https://arxiv.org/abs/2606.05073)

**<font color=#1a73e8>作者：</font>** Lixing Zhang, Yidong Ouyang, Weifu Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Missing value imputation is a fundamental task in machine learning, with most existing methods assuming that all missing entries correspond to unobserved regular values. In many real-world datasets, however, missingness may arise from two distinct sources: some entries are meaningfully missing (intrinsically absent and semantically valid), while others are missing due to the observation process and should be imputed. We formalize this distinction as a selective imputation problem, where the goal is to jointly infer which missing entries should be preserved and which should be recovered. To address this challenge, we propose Diff-Joint, a diffusion-based framework that jointly models tabular data together with a latent missingness mask. The method alternates between conditional sampling and uncertainty-aware aggregation to iteratively refine both imputed values and missingness labels. Empirical results on synthetic and real-world datasets demonstrate that Diff-Joint effectively identifies meaningfully missing entries while achieving competitive imputation accuracy and improved downstream task performance.

---


### 248. [Attention-Augmented LSTMs for Automatic Homophonic Ciphertext Decipherment](https://arxiv.org/abs/2606.05078)

**<font color=#1a73e8>作者：</font>** Micaella Bruton, Meriem Beloucif, Beáta Megyesi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Homophonic substitution ciphers replace each plaintext letter with one of several possible ciphertext codes, deliberately weakening letter-frequency patterns and making automated decipherment difficult. This paper evaluates whether an attention-augmented Long Short-Term Memory (LSTM) model can learn such mappings in a historically motivated shared-key setting: all ciphertexts draw from the same known homophonic code pool, while individual keys use different consistent subsets of that pool. Using synthetic ciphertexts generated with ChronoFidelius from historical English and Swedish texts dated 1500--1899, we test performance across ciphertext lengths, centuries, variable-length codes, and simulated transcription errors. Models are trained only on aligned ciphertext--plaintext pairs, without external language models, frequency statistics, or key-search heuristics. Results show near-perfect character-level decryption accuracy across both languages and all periods, including short and noisy ciphertexts. The model also fails predictably on ciphertexts outside the shared pool, indicating that it functions as a practical tool for decipherment and key-space verification when key reuse is suspected.

---


### 249. [AutoLab: Can Frontier Models Solve Long-Horizon Auto Research and Engineering Tasks?](https://arxiv.org/abs/2606.05080)

**<font color=#1a73e8>作者：</font>** Zhangchen Xu, Junda Chen, Yue Huang 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific and engineering progress is fundamentally a long-horizon iterative process: proposing changes, running experiments, measuring outcomes, and continuously refining artifacts. Yet existing benchmarks for frontier models primarily evaluate either single-turn responses or short-horizon agent trajectories, failing to capture the challenges of sustained iterative improvement over extended time horizons. To address this gap, we introduce AutoLab, a new benchmark for ultra long-horizon closed-loop optimization. AutoLab consists of 36 realistic, expert-curated tasks spanning four diverse domains: system optimization, puzzle & challenge, model development, and CUDA kernel optimization. Each task begins with a correct but deliberately suboptimal baseline and challenges agents to improve it within a strict wall-clock budget. Evaluating 17 state-of-the-art models reveals the dominant predictor of success is not the quality of an agent's initial attempt, but its persistence in repeatedly benchmarking, editing, and incorporating empirical feedback. While claude-opus-4.6 exhibits strong long-horizon optimization capabilities, most frontier models, including several proprietary ones, either terminate prematurely or exhaust their budgets with minimal progress. These results underscore the importance of time awareness and persistent iteration in autonomous agents. We open-source the full benchmark, evaluation harness, and task artifacts, to accelerate research toward truly capable long-horizon agents.

---


### 250. [Bernoulli CUSUM and Bayes-Optimal Detection Ceilings for Trust Fraud in Sparse Rating Networks](https://arxiv.org/abs/2606.05090)

**<font color=#1a73e8>作者：</font>** Talal Ashraf Butt  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Sequential trust detection in rating networks relies on continuous observation models that fail on real data. On Bitcoin-OTC, 56\% of ratings take a single value under standard mapping, breaking the distributional assumptions that parametric detectors require. This paper makes three contributions. It derives a Bayes-optimal F1 detection ceiling for per-node sequential detectors using empirically measured observation parameters. At Bitcoin-OTC's median in-degree of 2, this ceiling falls to 0.451 for strategic attacks, explaining why unsupervised methods cluster near $F1 \approx 0.4$. The analysis shows that detector-model matching, not information content, determines performance: binary models retain 86\% of mutual information while enabling exact parametric fit. A dual-regime architecture is presented where Bernoulli CUSUM detects behavioral shifts and triggers asymmetric scoring. Ablation reveals a co-design constraint: the modulation mechanism improves AUC by 0.030 on binary observations but degrades it by 0.094 on continuous observations. The combined system achieves AUC 0.749 on Bitcoin-OTC and 0.796 on Bitcoin-Alpha, beating GaaSTrust on all 8 attacks ($p < 0.003$), with founder-label AUC of 0.999.

---


> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-265](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
