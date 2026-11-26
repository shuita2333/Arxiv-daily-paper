# 📦 其他研究 | 2026年11月27日

> 本类共 **314** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-314](./part-07.md)

---

### 251. [HoMe: Toward Practical Harness Optimization of Memory Systems for AI Assistants](https://arxiv.org/abs/2611.34624)

**<font color=#1a73e8>作者：</font>** Yifei Xu, Li Yu, Zhaoyang Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The behavior of memory systems for long-running AI assistants is governed by a harness, which consists of the code, prompts, and configurations for memory construction, maintenance, retrieval, and answer generation. However, optimizing the harness of a memory system remains largely manual, and unrestricted editing alone does not ensure structural improvements. In this paper, we introduce HoMe, an evaluation-driven framework that iteratively evaluates candidate harnesses and derives each new candidate from any previously evaluated harness by editing any part of it. HoMe combines session-level memory versioning with execution traces to identify shared failure mechanisms across cases and localize them to the responsible sessions and harness components. It encourages early structural exploration through candidate gating and reduces evaluation cost through smoke tests, adaptive sampling, and the reuse of constructed memory. We validate HoMe with the open-source memory system ReMe on two large-scale long-horizon memory benchmarks, LongMemEval-S and BEAM. With six formal candidate evaluations per benchmark, after a full initial evaluation, HoMe discovers harnesses that improve end-task performance over the originally strong harness while consuming far fewer query-time tokens. The code is available at this https URL.

---


### 252. [DecisionReplay: A Corpus and Offline Simulator for Ensembling Decision Models](https://arxiv.org/abs/2611.34627)

**<font color=#1a73e8>作者：</font>** Dean Ariel, Seffi Cohen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Comparing ensembles, routers and cascades requires the output of every model on every item, and its cost. Stored collections built for routing keep no per-option probabilities. We provide a dataset on which ensemble methods, routers and cascades are simulated quickly, without new model calls. DecisionReplay holds the probability vectors of 17 commercial decision models, endpoints that return a probability for every answer option, on 35 benchmarks, with the token counts, billed cost and measured latency of every call, all released. A deterministic simulator replays any policy that selects, combines or cascades them. One well-chosen model per benchmark is hard to beat: pooling all models loses 2.7 accuracy points to it, and stacking gains 1.0 points at 3.4 times its cost. The models are wrong together: two that are both wrong choose the same wrong option in 72% of cases. The best router matches that model at 64% of its cost, and certified early exit cuts the cost of a stacked ensemble by 43% without changing an answer. DecisionReplay makes it cheap and fast to test whether a new method changes these results.

---


### 253. [Predicting acute food crises and discovering actionable drivers with causal machine learning](https://arxiv.org/abs/2611.34629)

**<font color=#1a73e8>作者：</font>** Mélissande Machefer, Michele Ronco, Michele Meroni 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Acute food insecurity is driven by a compound of conflict, adverse climate events, displacement, and economic shocks. We enrich the open-access Harmonized Food Insecurity Dataset with driver variables (monthly, subnational, 80 countries, 2007--2024) and develop missing-data-resilient machine learning pipelines forecasting crisis occurrence at 3, 6, and 9-month lead times using both FEWS NET and, for the first time at scale, IPC/CH classifications. Pipelines, evaluated through nested cross-validation, outperform no-skill baselines by 15 to 50 percentage points in PR-AUC, with performance correlated with crisis prevalence rather than the classification system. TreeSHAP-based explainability reveals compound, geography-specific predictive signal profiles, with three recurrent forecasting archetypes. Comparing predictive importance against doubly robust causal estimates of actionable drivers, we find that acute conflict events, having the weakest predictive signals, emerge as primary causal drivers of crisis classification whilst agroclimatology is the sole dimension in which predictive importance and causal effect align.

---


### 254. [Carrying Feature Ablations Across Sparse Autoencoder Seeds](https://arxiv.org/abs/2611.34637)

**<font color=#1a73e8>作者：</font>** Karl Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A vision encoder turns an image into one vector per patch, refined layer by layer. A sparse autoencoder (SAE) writes each vector of one layer as a sum of learned directions, most with a coefficient of zero. Researchers call each direction a feature and edit the encoder by removing one feature. An SAE trained from another random seed learns different features. Earlier work matches the two SAEs' features one to one by how closely their directions agree. Matched features can point alike yet respond to different image parts, so removing them may change the encoder differently. We remove a feature and, separately, its match, then compare the changes in the encoder's output on the same held out images. When the second change nearly reproduces the first, we say the removal carries across seeds. A setting fixes a DINOv2 or SigLIP layer and its SAE feature count. At our tolerance, the removal carries for 12% to 70% of matched pairs across three settings. The share is 0% in two controls: an SAE whose directions stay random and, post hoc, matches shuffled among trained features. Post hoc, predicting which removals carry is more accurate with layer contributions than with directions. Some incorrect predictions remain. One persists on independent images. So pairs can be screened at the layer. Measuring the output detects errors this screen misses.

---


### 255. [PRAM: Activating Latent Multimodal Knowledge through Partwise Reasoning](https://arxiv.org/abs/2611.34640)

**<font color=#1a73e8>作者：</font>** Haidong Chen, Ying Guo, Shangze Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Emergent cross-modal classification and retrieval enable transfer between modalities without direct paired supervision. However, existing methods often prioritize sample-level alignment, overlooking local discriminative information and partwise statistical relations. To this end, we propose partwise reasoning across modalities (PRAM), which activates latent multimodal knowledge in frozen encoders by composing partwise statistical relations through a shared pivot modality. Specifically, we first present a multi-granularity covariance regularization module that estimates covariances from global and local vectors in two collections of modality-pivot pairs, stabilizing local estimates through adaptive blending with their cross-part means. Second, we devise a pivot-based spectral relational reasoning module that infers global and partwise statistical relations between target modalities through regularized covariance composition and extracts paired projection directions and their correlation strengths via whitening and spectral decomposition. Finally, we introduce a multi-granularity score fusion module that standardizes and fuses matching scores from global and local relations, incorporating task-specific information on pivot associations and class semantics for class prediction and candidate ranking. Extensive experiments across ten datasets demonstrate that PRAM achieves state-of-the-art performance in 16 classification settings and 19 retrieval settings, while exhibiting highly competitive performance in three sensing scenarios.

---


### 256. [Distractor-Robust Reinforcement Learning via Variational Bisimulation](https://arxiv.org/abs/2611.34641)

**<font color=#1a73e8>作者：</font>** Benjamin Freed, Vivaan Singh, Dean Zadok 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model-based reinforcement learning (MBRL) promises data efficiency and generalization, but typical reconstruction-based objectives encourage models to waste representational capacity on task-irrelevant distractors. We introduce VIBES (Variational Inference for Bisimulation-based Encoded States), a new objective that replaces pixel reconstruction with an adversarial term, which enforces that latent states suffice to predict both rewards and the next latent state. We show that this objective measures how far the encoder is from reward and dynamics sufficiency, and that whenever exact sufficiency is attainable, its global optima induce bisimulation relations on histories. Combined with a fixed-capacity latent bottleneck, this encourages latent states to retain task-relevant information while discarding irrelevant variation. Our method serves as a drop-in replacement for Dreamer's model-learning component, achieves state-of-the-art performance on the Distracting Control Suite, and extends to visually complex manipulation in Realistic ManiSkill. Unlike prior approaches, it does not rely on image-specific augmentations and applies equally well to high-dimensional vector-state tasks, demonstrated on a 100-link swimmer robot. Finally, latent-space analyses (UMAP embeddings and nearest-neighbor probes) confirm that the learned representations are sensitive to task-relevant structure while invariant to distractors.

---


### 257. [Motion Beyond Pixels: Learning Future Visual Representations for Object-Centric Dynamics](https://arxiv.org/abs/2611.34644)

**<font color=#1a73e8>作者：</font>** Chengzhi Zhao, Juelin Li, Zhennan Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many embodied world models predict future states in latent spaces optimized for RGB reconstruction, which do not explicitly prioritize object-level semantics and geometry relevant to motion generation. We present MotionRep, a visual representation world model that jointly generates future DINO representations and 3D object flow, coupling semantic and geometric information with object-centric dynamics. To make high-dimensional DINO features amenable to generative modeling, we introduce DINO-VAE, which combines temporal and channel compression with latent regularization to produce compact latents while preserving semantic and geometric information. Conditioned on an initial observation, object query points, and a language instruction, a unified diffusion transformer predicts future visual representations and 3D object flow through joint attention. MotionRep employs asymmetric modality-specific noise schedules to keep the visual stream ahead of 3D object flow during joint denoising, allowing progressively refined future visual representations to guide flow generation. Experiments on simulated and real-world manipulation benchmarks demonstrate that MotionRep outperforms pixel-based baselines in 3D object flow accuracy and generalization to unseen scenes, while requiring only three denoising steps for inference. These results support predictive visual representations as an effective future-state space for object-centric dynamics modeling.

---


### 258. [A Hard Background Pairing Transfers across Classifiers and Images](https://arxiv.org/abs/2611.34645)

**<font color=#1a73e8>作者：</font>** Karl Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> An image classifier names the object in an image, and its accuracy is the share of images named correctly. A classifier that names a car on a road may miss the same car pasted onto clouds. Composite benchmarks measure such failures by pasting objects cut from photographs onto backgrounds from other photographs. A pairing puts every object label on a different background label, such as truck on sea. The pairing on which some classifiers do worst, their hardest pairing, makes a strict test, but may be hard only for them or only on the photographs used to choose it. We show that the hardest pairing of some classifiers stays hard for others and on new photographs. We split 40 ImageNet classifiers into halves balanced by reported ImageNet accuracy. One half picks its hardest pairing of 8 object and 8 background labels from Common Objects in Context (COCO). The other half, held out of the choice, compares that pairing with random pairings of the same objects and backgrounds. For the 14 held-out classifiers with little net accuracy change after pasting objects back onto their own backgrounds, mean accuracy on composites from new photographs falls from 50.3% over random pairings to 43.7% on the hardest pairing, 6.6 percentage points lower. A benchmark using these composites can compare this pool's held-out classifiers on the fixed and random pairings.

---


### 259. [Atunda: Building an Afrogenic Dance Movement Dataset for AI-Driven Classification](https://arxiv.org/abs/2611.34649)

**<font color=#1a73e8>作者：</font>** Diego Carrascosa, Tristan Pank, Qudus Onikeku 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper introduces Atunda, the first systematically collected video dataset of Afrogenic dance moves, designed for training and evaluating deep learning models for movement classification. The first phase of the dataset includes nearly 400 videos covering 13 distinct dance moves from African and African Diaspora performative culture, making it the first AI-ready resource of its kind. Using this dataset, we train and evaluate various configurations of temporal convolutional neural networks, achieving a classification accuracy exceeding 95%. The baseline results provide a benchmark for future studies in movement classification, especially in the understudied area of Afrogenic performative culture and tradition. This work lays the foundation for developing in the future digital metrics of similarity, automated attribution systems, and tools that preserve and promote the cultural heritage of Afrogenic dances.

---


### 260. [Provably Efficient Concave Utility Reinforcement Learning with Linear Function Approximation](https://arxiv.org/abs/2611.34678)

**<font color=#1a73e8>作者：</font>** Max Qiushi Lin, Ahmed Magd, Sharan Vaswani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Concave utility reinforcement learning (CURL) unifies a diverse range of problems, including standard reinforcement learning (RL), imitation learning, and maximum entropy exploration. Unlike standard RL, CURL generally requires estimating high-dimensional state-action occupancy measures. Consequently, existing methods for CURL either sidestep the exploration problem, are restricted to the tabular setting, or lack computationally efficient policy optimization. To address this, we study CURL in finite-horizon episodic bilinear MDPs, where the transition model admits a low-dimensional representation in known feature spaces. We use the bilinear structure to efficiently estimate occupancy measures via low-dimensional feature expectations, and propose a model-based optimistic concave utility policy optimization (OCUPO) framework. We first instantiate OCUPO in the on-policy setting, where each iteration uses independent trajectories to estimate the concave utility policy gradient, and prove an $\widetilde{O}(\epsilon^{-4})$ sample complexity. To improve sample efficiency, we then instantiate OCUPO in the off-policy setting. We propose a novel backward feature regression subroutine that reuses trajectories collected by past policies to estimate the occupancy measure of the current policy. Under suitable technical assumptions on the policy class (satisfied, e.g., by log-linear policies with sufficiently expressive features), we prove that the resulting algorithm achieves an $\widetilde{O}(\epsilon^{-2})$ sample complexity, up to a controllable projection error. We further extend our framework to linear MDPs and show that the resulting off-policy algorithm retains the same sample complexity. In these settings, the dependence on $\epsilon$ matches that for standard RL with linear function approximation. Moreover, our algorithms do not rely on the integral oracle required by prior work.

---


### 261. [Neural Rendering Compiler: Generative Video Models as Programmable Renderers](https://arxiv.org/abs/2611.34680)

**<font color=#1a73e8>作者：</font>** Yuxia Zhu, Xinglong Xu, Hao Liang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative video models are becoming powerful renderers, yet lack the predictable control interfaces of conventional systems such as HTML/CSS engines or Blender. Their capabilities emerge implicitly from training, making it difficult to determine what they can reliably execute. We present Neural Rendering Compiler (NeurCo), which automatically probes frozen video models to construct model-specific capability manuals describing which semantic requirements they can reliably satisfy. NeurCo represents user intent in a model-agnostic intermediate representation of objects, constraints, events, and cameras, then compiles it into model-specific execution strategies. Reliable requirements remain unchanged, while unreliable ones are selectively rewritten or compiled into alternative execution strategies. We introduce VComBench, a benchmark of 380 compositional, multi-requirement tasks spanning text-to-video, image-to-video, and reference-to-video generation. NeurCo improves requirement satisfaction from 46.8% to 52.3% on Wan and from 66.5% to 69.3% on Minimax H3, and achieves further gains when combined with prompt enhancers, including on Seedance 2.5. Our analysis reveals model-specific differences in control capabilities and trade-offs between controllability and photorealism, highlighting capability-guided compilation as a promising approach to programmable generative video rendering.

---


### 262. [BridgeHammer: DNN Backdoor Attack via CPU-iGPU Shared-memory Rowhammer](https://arxiv.org/abs/2611.34684)

**<font color=#1a73e8>作者：</font>** Yufei Wang, Saion K. Roy, Yunsi Fei  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Heterogeneous systems-on-chips (SoCs) share physical memory between CPUs and integrated GPUs (iGPUs), creating a path for CPU-side memory corruption to compromise the integrity of deep learning models used for iGPU inference. Implanting a backdoor that causes targeted misclassifications on trigger-bearing inputs while retaining accuracy on normal inputs requires carefully selected weight changes. However, realizing these changes presents two challenges: where to induce faults, since vulnerable DRAM locations may not contain the targeted weights, and when to intervene, since memory placement and fault injection must align with different stages of the model deployment lifecycle that involve two distinct computation domains. We present BridgeHammer, a Rowhammer-based backdoor attack that addresses these challenges by coordinating targeted weight placement before zero-copy binding for the iGPU and fault injection before inference. The iGPU then uses the corrupted model for subsequent inferences. We evaluate BridgeHammer on a heterogeneous Intel CPU-iGPU platform using OpenVINO, targeting ResNet-20, VGG-16, and ResNet-50 at both INT8 and FP32 precision. Across all six configurations, BridgeHammer achieves an 88.9% attack success rate (ASR) and 86.3% clean accuracy on average, with reliable target-page placement and bit-flip reproduction. These results demonstrate a new integrity vulnerability on heterogeneous CPU-iGPU SoCs, motivating cross-domain memory integrity protections.

---


### 263. [Evacuation Traffic Prediction for Dynamic Transportation Networks over Multiple Hurricanes: A Generalized Graph Learning Approach](https://arxiv.org/abs/2611.34687)

**<font color=#1a73e8>作者：</font>** Md Nafees Fuad Rafi, Samiul Hasan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High traffic demand during hurricane evacuations causes severe congestion on major highways, leading to delays and safety risks for evacuees. Predicting evacuation traffic in real-time can significantly enhance evacuation management efforts. However, evacuation traffic is highly dynamic and uncertain due to evolving hurricane characteristics and diverse population response. Each hurricane has unique characteristics and evacuation contexts, resulting in different spatial-temporal traffic patterns. Moreover, the structure of detector-based transportation networks varies across multiple hurricanes. Hence, a model trained on the data from one hurricane may not generalize well for others. This study proposes a generalized dynamic graph learning framework using traffic detectors and evacuation data from 12 historical hurricanes. Leveraging the dynamic nature of transportation network, we develop a Graph Convolutional Long Short-Term Memory (GCN-LSTM) model that predicts evacuation traffic up to 6 hours in advance. For an unseen hurricane (Milton, 2024), the model shows strong generalizability, achieving an RMSE of 280.6 and R2 of 0.96 for 1-hour prediction, and an RMSE of 459.8 and R2 of 0.89 for overall 6-hours prediction. We also introduce a modular training approach, where we evaluate performance improvements by sequentially incorporating data from multiple hurricanes. The proposed model outperforms state-of-the-art baseline models for overall 6-hour prediction horizons. Ablation experiments show an 8.4% improvement in RMSE for the proposed dynamic GCN-LSTM model compared to its static counterpart. Traffic management officials can use the developed model to understand future traffic conditions during hurricane evacuation in advance and take proactive measures to reduce delays during evacuation.

---


### 264. [PoVi: Agentic Poetry-to-Video Generation with Knowledge Grounding and Figurative Understanding](https://arxiv.org/abs/2611.34690)

**<font color=#1a73e8>作者：</font>** Yuxia Zhu, Shiying Zhang, Lingzhuang Sun 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Poetry-to-video generation requires more than translating text into visual scenes. Poetic language is highly compressed, often depends on historical and cultural knowledge, and frequently conveys meaning through metaphor, imagery, and other non-literal expressions. We introduce PoVi, a benchmark and agentic framework for grounded poetry-to-video generation, evaluating semantic grounding, discourse coherence, and audiovisual realization. PoVi reconstructs poem semantics into an evidence-bounded representation and progressively transforms them into narration, interpretation, character assets, and shot-level visual plans, followed by narration-aligned video generation. Across three planning backbones and four video generators, PoVi consistently improves over single-call generation, with the largest gains on implicit background knowledge and metaphorical relations. PoVi provides a testbed for studying knowledge-grounded, long-horizon multimodal generation beyond direct text-to-video synthesis.

---


### 265. [ShowNow: Fine-Grained Speculative Streaming for Responsive World Models](https://arxiv.org/abs/2611.34693)

**<font color=#1a73e8>作者：</font>** Yiren Song, Guian Fang, Mike Zheng Shou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive world models must generate video continuously while responding promptly to user actions. Real-time throughput alone leaves input latency unresolved: coarse generation blocks delay action updates, and generation after input adds work to the response path. We introduce ShowNow, a fine-grained speculative streaming framework that uses computation available during playback to prepare action-conditioned futures before input arrives. Single-latent commitment enables frequent decisions, while configurable preparation covers one to eight actions. We construct a matched multi-future dataset to train alternative continuations from a common state; shared-history tree execution and fused commitment make their preparation efficient. On a single H100, our 5B model sustains 480p generation at 16 fps with eight prepared futures. In ViZDoom, the complete ShowNow deployment reduces median input-to-display latency from 620 to 208 ms relative to the native-block SolarWM-FT deployment. Matched-policy experiments reduce restart empty ticks from 1.56% to 0.09% (94%) and improve on-time responses to action changes. These results establish complementary roles for fine-grained commitment and advance preparation, with measured trade-offs in visual fidelity and long-horizon consistency. ShowNow turns playback-time computation into responsive visual interaction. Project: this https URL.

---


### 266. [Distance from the Truth: Why Fragmented Merchant Underwriting Misses Risk, and What Source-Attributable Evidence Changes](https://arxiv.org/abs/2611.34696)

**<font color=#1a73e8>作者：</font>** Russell Lessard, Jeremy Blackburn, Tim Hines 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Merchant underwriting becomes vulnerable when evidence is evaluated without enough visibility into its source, freshness, relationship to the applicant, or meaning for the proposed activity. Individually favorable checks do not necessarily establish that the same business is operating the merchant account, that its representative may bind it, or that its settlement instructions are authorized. We describe three failure modes of fragmented underwriting: distance from the source, the gap between a decision and the evidence needed to justify it; the correlation gap, in which material relationships among the person, legal entity, owners or controllers, representative, business activity, and settlement destination are not evaluated when each signal is considered alone; and point-in-time controls, in which a historical verification is treated as present eligibility. We map these failure modes to identity-proofing, customer-due-diligence, sanctions, third-party-risk, card-network, and Nacha requirements, and propose a merchant-underwriting application of the ChainIT Transaction Truth Architecture built on provenance, correlation, and persistence. The application keeps a logically unified evidence record that identifies what was checked, the subject and relationship involved, the relevant times, the applicable policy, the decision, and any exceptions, and it keeps evidence validation, applicant verification, organizational authority, and the institution's risk judgment separate. We also set out a proposed evidence and decision receipt, a defined 90-day shadow enrollment pilot with adjudicated outcome measures and deliberate control-failure tests, and a ten-question self-assessment. Proposed controls, illustrative scenarios, and pilot measures are identified as such and are not represented as observed production results.

---


### 267. [Effect of class proportion shifts on classifier curvature](https://arxiv.org/abs/2611.34702)

**<font color=#1a73e8>作者：</font>** Maxim Bolshim, Alexander Kugaevskikh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Changing the class mix can alter mean loss without changing the classifier. To distinguish this reweighting from changes in the model itself, we studied ten-class CIFAR-10 classification in separate branches for two target classes, measuring the trace of the loss Hessian with respect to the output-layer parameters on fixed images of each target class. Across ten new initialisations, after 60 updates to the output layer with frozen features, the trace changed by -0.152% on average in branches where the target class share rose from 10% to 19%, and by +0.071% in branches where it fell to 1%, relative to each branch's initial trace. These changes do not isolate the effect of class share from that of the assigned training images. We developed a forecast based on initial class gradients after examining the first experiment's results and then tested it prospectively without modification. For direct increases from 10% to 19%, rather than increases after a deficit, its mean absolute error was 0.022 percentage points on the initial-trace scale, compared with 0.152 for a zero-change forecast and 0.104 for equally weighted gradients. Using the assigned class proportions improved the forecast of how much the trace would change.

---


### 268. [When the Proxy Is Wrong: Mismatch-Corrected Bandits for Adaptive Data Sampling](https://arxiv.org/abs/2611.34707)

**<font color=#1a73e8>作者：</font>** Amine Saadi, Elissa Mhanna, Raphaël Féraud 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data allocation methods often use a small proxy model to select training data for a larger target model. However, this proxy can rank data differently from the target, leading to suboptimal training performance. To address this problem, we model the mismatch between the proxy and target models and incorporate it into the allocation decision. To do so, the problem is cast as a multi-fidelity bandit, where each arm is a data intervention. The proxy reward is observed every round, whereas the target reward is revealed only on rare audits of the same update. These paired observations identify arm-wise mismatches without assuming a shared offset or preservation of rankings. Mismatch-corrected bandits correct the proxy with paired residuals, audit only uncertain decisions, and pace the audit budget over training. From a theoretical viewpoint, we prove a regret decomposition and lower bounds under stationarity. These bounds show that proxy-only allocation can incur linear regret and that a minimum number of paired audits is necessary. Under abrupt changes, using the audit budget early can also incur linear regret. A sliding-window policy that spreads audits over training achieves regret of order $\sqrt{\Gamma_T T\log T}$ where $\Gamma_T$ denotes the number of change points. Experimentally, we test the approach in a closed-loop proof of concept on CivilComments-WILDS, where BERT-Small guides the training of BERT-Large. Mismatch correction improves worst-group accuracy over a target-only policy with the same target-model budget. Spreading audits over training improves worst-group accuracy by 6.3 to 10.5 percentage points at the same audit count.

---


### 269. [From Shared Patterns to Individual Evidence: Two-Stage Reasoning for Emerging Entities in Temporal Knowledge Graphs](https://arxiv.org/abs/2611.34708)

**<font color=#1a73e8>作者：</font>** Jinchuan Zhang, Lei Gao, Hongyu Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Temporal knowledge graphs (TKGs) continually introduce emerging entities whose interaction histories evolve from zero-shot debuts into sparse, bursty few-shot trajectories. However, current paradigms are fragmented: pattern-transfer methods lack catalog-wide event memory, whereas online memory models suffer from endpoint-role asymmetry that degrades unseen-answer ranking. Furthermore, sparse early interactions exhibit both long-range dispersion and local redundancy under skewed distribution. To address these challenges, we propose INSPIRE (Integrating Shared Patterns and Individual Evidence for Reasoning), a two-stage forecasting framework over a known catalog. In Stage I, INSPIRE learns an availability-aware shared-pattern predictor that fuses event-updated memory across the full candidate catalog while applying coordinated query- and catalog-side masking. Subsequently, Stage II freezes this predictor and optimizes a lightweight individual-evidence adapter (EA) combining textual semantic priors with correlation-weighted long-range event statistics under support- and role-balanced co-answer supervision with prior-odds debiasing and soft residual alignment. In addition, we decompose evaluation by endpoint roles and track longitudinal emerging-answer cohorts via query-micro and answer-entity macro metrics. Across four benchmarks based on the ICEWS and GDELT event datasets, INSPIRE improves Emerging MRR by 16.73%-88.83% over the strongest baselines. Relative to paired Stage I predictors, EA further increases Emerging MRR by 8.28%-32.63%, Answer-new MRR by 7.81%-41.24%, and cohort macro MRR by 9.64%-39.94%, gains attributed to semantic priors and candidate-level score competition suppressing mismatched established competitors without zero-support prior shortcuts. The official code is publicly available at this https URL.

---


### 270. [Reading, Not Adapting: Unlocking Frozen Visual Knowledge for AI-Generated Image Detection](https://arxiv.org/abs/2611.34719)

**<font color=#1a73e8>作者：</font>** Yuncheng Guo, Ying Dong, Xiaodong Gu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generalization to unseen image generators has driven efforts to adapt pretrained visual representations for detection. Yet recent findings show that vision foundation models already encode transferable detection knowledge, while further adaptation can impair generalization. This motivates a shift from backbone adaptation to knowledge readout. Conventional linear probing offers a direct way to read this knowledge but is limited to final-layer RGB features. Multi-cue detectors broaden the evidence base, but their designs introduce other tradeoffs: adaptation may compromise pretrained transferability, heterogeneous encoders complicate feature integration, and late fusion precludes intermediate cross-view interaction. To overcome these limitations, we propose ReMoT, a Mixture-of-Transformers-inspired framework that reads complementary knowledge from spatially aligned RGB and wavelet views within a fully frozen visual foundation. ReMoT employs staged joint attention to enable controlled local and global cross-view interaction, while learnable fusion queries progressively read complementary evidence across Transformer depth without writeback. ReMoT achieves 91.2% average accuracy across eight benchmark groups with 3,074 trainable parameters, attaining the highest overall average among the evaluated methods. These results support structured knowledge readout as a promising alternative to backbone adaptation. Code is available at this https URL.

---


### 271. [Robust Recourse under Causal Graph Ambiguity](https://arxiv.org/abs/2611.34723)

**<font color=#1a73e8>作者：</font>** Muyan Anna Li, Juliette Sinnott, Mohammad Kohandel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal algorithmic recourse recommends actions to reverse unfavorable decisions by modeling how interventions change an individual's features. Existing methods typically assume one causal graph that describes the system and account for uncertainty in the causal mechanisms. However, there usually exist several graphs that fit the same data but can predict different effects for the same action. Certain actions may achieve recourse across multiple graphs, but as the set of potential graphs grows, a single best action may become infeasible.
We propose Worst-Case Recourse and Graph-Weighted Recourse to find a low-cost action that succeeds across all candidate graphs or a specified fraction of graph weight, respectively. Assuming a set of plausible graphs, for each graph we fit Gaussian process structural equations and assess success using the posterior mean--standard-deviation criterion. We use gradient-based search to determine minimal cost actions and check the validity of the actions on fresh posterior samples. In synthetic and semi-synthetic benchmarks, relaxing robustness, the requirement that an action succeed under every candidate graph, can increase the number of valid recommendations for recourse and lower costs of actions for both methods. In the 20-node GP benchmark, relaxation increases the number of factual instances offered recourse (coverage) from 341 to 436 out of 1,000, while the number of true successes, actions that flip the decision under the generating model, falls from 251 to 184, illustrating the coverage--validity trade-off. Accounting for graph ambiguity can help decision-makers recommend actions that remain effective even when the causal mechanisms of the system are not fully known.

---


### 272. [LiDAR Intensity Reconstruction with Limited Real Data: An Architecture Benchmark under Fixed-Epoch Training](https://arxiv.org/abs/2611.34724)

**<font color=#1a73e8>作者：</font>** Christopher M. Coovrey, Aniruddha Bora  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physics-derived simulation can supplement scarce real-world LiDAR intensity measurements, but its effectiveness depends on the learning architecture and the amount of real training data available. We benchmark nine neural architectures for LiDAR intensity reconstruction from depth, semantic labels, incidence angle, and material reflectance, using real SemanticKITTI and synthetic VoxelScape range-image data. All models follow a fixed 20-epoch protocol; this controls the number of training passes, not the computational cost across architectures. We report mean absolute error (MAE), mean squared error (MSE), peak signal-to-noise ratio (PSNR), structural similarity (SSIM), inference timing, and spectral-energy agreement. We also evaluate four selected architectures with fixed-size training mixtures containing 0\%, 1\%, 5\%, 10\%, 20\%, 50\%, or 100\% real frames. With real-only training, UNet-V2 achieves the best reported reconstruction metrics (MAE 0.234, MSE 0.140, PSNR 8.64 dB, and SSIM 0.647), followed by a denoising diffusion model (DDPM). In several mixtures containing 1--10\% real data, DDPM achieves lower error and higher image-quality metrics than the evaluated deterministic alternatives, whereas UNet-V2 leads with 100\% real data. Spectral analysis additionally reveals architecture-dependent discrepancies across frequency bands. These findings characterize reconstruction trade-offs under the stated data mixtures and fixed-epoch protocol, without establishing compute-matched superiority or isolating the diffusion objective from backbone differences.

---


### 273. [Bigger Model or Bigger Table? How Much Backbone a Chorus N-gram Module Replaces](https://arxiv.org/abs/2611.34725)

**<font color=#1a73e8>作者：</font>** Szymon Kocur  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We ask how much of a transformer's backbone the Chorus N-gram module replaces. Chorus adds hashed tables of token bigrams and trigrams to its input and attention. We train models of 16M to 349M parameters on 1.34 billion tokens of Polish printed before 1918 and find the size of a plain model with the same held-out loss. A separate learning-rate search for each kind of model cuts Chorus's gain at 47M by about a third. With tables about as large as the backbone, Chorus then matches a plain model 1.34 times its size at 16M and 1.16 to 1.20 times from 107M to 349M. With these tables, each added parameter replaces at most 0.31 backbone parameters. Chorus trains slower than a plain model of its size and faster than one of the same loss. On a fact quiz the two differ about as much as two seeds of one model. The results rest on one corpus, one 8,000-token vocabulary and a fifth of an epoch.

---


### 274. [Hierarchical Graph Metanetworks](https://arxiv.org/abs/2611.34726)

**<font color=#1a73e8>作者：</font>** Ioannis Kalogeropoulos, Giorgos Bouritsas, Yannis Panagakis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The emerging field of weight space learning has demonstrated the potential to enable metanetworks, i.e. models that process neural network (NN) data, to support several steps of the machine learning lifecycle, from model optimisation to evaluation and adaptation. However, this potential has yet to materialise beyond small-scale MLPs or CNNs: most current models, including message-passing based graph metanetworks (GMNs), operate exclusively at the finest level of granularity, processing every neuron and weight of the input model. Their cost therefore scales with the number of parameters. Yet NNs are inherently organised hierarchically, with neurons forming layers and layers forming blocks and modules. Additionally, several of their properties, such as Lipschitz upper bounds and generalisation measures, are compositions of layer- and block-level quantities. To incorporate this inductive bias, we introduce Hierarchical Graph Metanetworks (H-GMNs), which leverage the input architecture's hierarchy to coarsen and refine the graph using permutation-symmetry-preserving pooling and un-pooling layers. Further, we extend H-GMNs to Transformers by introducing a graph construction that preserves permutation symmetries and enables multi-level pooling. Our evaluation includes new ResNet-18, ViT and varying ViT model zoos of up to 86M parameters, on tasks spanning model evaluation (an analytic Lipschitz bound proxy, generalisation and robustness prediction), testing (backdoor detection) and editing (pruning). Experimental results show that, compared to non-equivariant alternatives and flat GMNs, H-GMNs are markedly more sample-efficient, and their cost remains nearly constant as metanetwork depth grows, allowing deeper and more expressive processing where flat GMNs run out of memory, without compromising accuracy, which in certain cases considerably improves.

---


### 275. [WorldInteract: Controllable Streaming Video Generation for Multi-Material Interactions](https://arxiv.org/abs/2611.34730)

**<font color=#1a73e8>作者：</font>** Ahmed Hatem, Caoliwen Wang, Robert Hoang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models aim to create interactive physical worlds that capture how diverse materials move and interact. Yet material-dependent dynamics remain underexplored in controllable video generation, limiting reliable control in scenes with different materials. We present WorldInteract, a streaming video generation framework that decomposes cross-material interaction into material-dependent behavior generation and contact response computation. External pushes and contact impulses are expressed through a shared velocity-increment interface, allowing material behaviors learned from interaction-free videos to be reused in interacting scenes. A physics controller predicts contacts and computes velocity increments from estimated masses and restitution coefficients, while a causal generator executes these increments using learned material behaviors. This separation enables cross-material interaction without supervised contact videos spanning diverse material pairings and contact configurations. We train the generator on 30k simulated interaction-free videos spanning 22 material classes and introduce Material-Aware RL, using verifiable physical rewards to refine material behavior and control execution. WorldInteract substantially outperforms state-of-the-art methods on Physics-IQ and delivers more reliable push control on real-world images.

---


### 276. [From NP-Hardness to Exact Tractability Through Sample Abundance](https://arxiv.org/abs/2611.34734)

**<font color=#1a73e8>作者：</font>** Mojtaba Soltanalian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Additional observations can make exact optimization tractable without changing the objective or feasible set. We establish this phenomenon for noisy parity fitting, a worst-case NP-hard problem, with uniformly sampled rank-one sign tensor entries, independent fair factor signs and independent errors. For fixed interaction order $k\ge3$, $n$ signs per block, logarithmic mean degree and known channel biases, $O(n/(\log n)^{1/(k-2)})$ further readings of the same source suffice with high probability for exact optimization in $O(n\log^2 n)$ worst-case work. The leading coefficient is sharp for weak recovery by depth-$O(\log\log n)$ local estimators with independent reading marks. A common signed-field law determines the gain over the generating source, the number of tied optima and the dimension needed for later reweightings. The geometry of the remaining coordinates determines the sharp radius of local verification for high-scoring assignments with high probability.

---


### 277. [Was the Model Given the Right Action? Auditing and Repairing Action Interfaces in Navigation World Models](https://arxiv.org/abs/2611.34739)

**<font color=#1a73e8>作者：</font>** Ajmain Istiak Apon, Md Mehedi Hasan, Sejuti Rahman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models are evaluated by predicting future observations from actions. These evaluations assume that actions are prepared the same way as during training, but an unchecked mismatch can make a model appear less accurate than it is. We audit this assumption in Navigation World Models (NWM) and find three interacting differences between its training and rollout code. Correcting the inputs, without retraining, reduces mean visual prediction error by 42%, measured with DreamSim on the RECON navigation dataset. The correction also changes the ranking of NWM checkpoints in an exploratory analysis and removes or reduces two alternative models' measured advantages. Correcting only the normalization offset instead increases error, showing why interacting mismatches must be checked together. To test whether sensitivity to input preparation extends beyond NWM, we deliberately introduce encoding errors into two alternative models; both become less accurate. We introduce ActRosetta, a tool that checks whether action encoding matches training, identifies supported causes of disagreement, and repairs inputs when sufficient information is available. Repair helps little where predictions barely respond to actions, the tool's diagnosis has limited coverage, and improved control remains unproven. For any action-conditioned world model, the lesson is the same: before reporting rollout error, verify that evaluation encodes actions exactly as training did.

---


### 278. [BRIAR: Martingale Belief Smoothing on Bifurcation-Guided Reasoning Trees](https://arxiv.org/abs/2611.34746)

**<font color=#1a73e8>作者：</font>** Tianyi Yang, Haoran Zhang, Yifan Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has rapidly advanced long-chain reasoning, yet standard policy optimizers distribute rollout compute and gradient credit blindly across a trajectory. On hard problems, an early misstep derails the remaining trace, whereas on solvable problems, the policy keeps generating redundant verification long after the answer is already determined. We trace both pathologies to a single structural fact: under an on-policy verifier, the true prefix pass probability $V^\pi(u)$ along a reasoning trace forms a $[0,1]$-bounded Doob martingale whose learnable credit variance is strictly conserved and bounded above by $V^\pi(u)(1-V^\pi(u))$, vanishing at both the derailed ($V^\pi\to 0$) and absorbed ($V^\pi\to 1$) boundaries. We introduce BRIAR (Bifurcation-guided Rollout and Inference on Adaptive Reasoning trees), a tree-structured RLVR framework built directly around this martingale geometry. First, BRIAR expands discourse-aligned reasoning trees along an upper-confidence outcome-bifurcation frontier, steering rollouts away from absorbed rumination and toward unresolved decision points. Second, it models latent node values with boundary-scaled heteroscedastic edge variances and computes exact global posteriors in linear $\mathcal{O}(|V|)$ time via two-pass Rauch--Tung--Striebel (RTS) tree belief smoothing, eliminating $\mathcal{O}(m^3)$ matrix inversions while gating out spurious boundary noise. Third, BRIAR detects minimal absorbed frontier nodes and applies zero-sum log-length centered suffix advantages strictly post-absorption, leaving pre-absorption derivations provably invariant.

---


### 279. [Reading Fine-Tuning Diffs Through Lenses: Model Diffing for Backdoor Detection](https://arxiv.org/abs/2611.34758)

**<font color=#1a73e8>作者：</font>** Maximilian Petrowitsch, Ben Connors, Chris Kapulkin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a common scoring system based on token readouts to evaluate weight, activation and output-based model diffing methods for backdoor detection in fine-tuning processes. We also improve existing weight and activation based methods by incorporating the $J$-lens and its refinement, the $J{+}{+}$-lens. We test our setup in experiments where we compare a backdoored model with the base model from which it was fine-tuned. Our results show that incorporating the $J{+}{+}$-lens improves the weight-based method in all our settings, while the $J$-lens improves its ranks within single layers. The strongest single method is $\Delta W J{+}{+}$, the weight difference decoded through the $J{+}{+}$-lens of the base model, which ranks a token naming the backdoor among its first ten tokens in 11 of our 12 settings. Moreover, we show that output and activation based methods such as ADL and Diff Mining can easily break if the backdoored model is penalised during fine-tuning for giving the backdoor's words probability on clean inputs, whereas the weight-based methods are not affected. Conversely, permuting the hidden units or training only the layers that read the residual stream hides the backdoor from the weight-based methods but not from ADL and Diff Mining. No single method resists both attacks.

---


### 280. [Adaptive Reliability Reserves for Residential Battery Fleets](https://arxiv.org/abs/2611.34779)

**<font color=#1a73e8>作者：</font>** Maruthi Vemula, Neeraj Praneeth Gajula  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In a Houston 2024 replay, replacing a fixed 20 percent battery reserve with a county-risk threshold raises observed five-hour backup coverage from 75.0 percent to 86.5 percent and adds USD 10.2 in modeled annualized margin per home (paired 95 percent interval: USD +1.7 to USD +21.7). The paired coverage-gain interval includes zero. This is a conditional simulation result, not measured company reliability. Residential batteries face this tradeoff because market discharge consumes energy also needed for household outages. We release HomeFleet-ERCOT, combining observed prices and county outages with identified simulated homes and causal controller inputs. We compare independent-home optimization with 21 proximal policy optimization (PPO) training runs; ten promise-cost candidates span 31.1 percent-96.3 percent backup coverage. Of these, 10 have lower modeled margin than fixed 20 percent, and 3 also have lower coverage. Chronological, geographic, fleet, and storm tests examine transfer. An alert charging override has a conditional energy-and-power sufficiency guarantee, but only 19.5 percent of 41 county mass-outage episodes provide enough continuous warning for every battery preset. Synthetic tests include short, missed, and false warnings, load uplift, capacity loss, and dropout. A static AC audit retains existing feeder violations; aging comparisons expose model sensitivity. The released benchmark, controllers, and checkpoints provide a reproducible basis for comparing these tradeoffs. This work supports the design of residential battery programs that assess market value and household backup service together.

---


### 281. [Comparative Study of Deep Learning Architectures for Brain Tumour Classification](https://arxiv.org/abs/2611.34781)

**<font color=#1a73e8>作者：</font>** Prisha Gupta, Pradeep Kumar Gupta  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate and early classification of brain tumours from magnetic resonance imaging (MRI) is essential for treatment planning, yet many published deep learning studies are trained and tested on small, single-source datasets, reporting accuracies that may not hold outside these datasets. This study compares six deep learning architectures for four-class classification (healthy, meningioma, glioma and pituitary tumour): a baseline convolutional neural network (CNN), an attention-based CNN, ShuffleNet, and EfficientNet-B0, ResNet-50 and Xception augmented with the Convolutional Block Attention Module (CBAM). The models were trained on a corpus assembled from four publicly available MRI datasets. Because these datasets carry no patient identifiers, a leakage-aware pipeline was developed that removes exact duplicates using MD5 hashing (550 images) and near-duplicates using perceptual hashing (8,024 images), and assigns visually similar images to the same fold during 5-fold group cross-validation. A leave-one-dataset-out (LODO) test on a fully held-out dataset was used to measure cross-dataset generalisation. Under a conventional random split, ShuffleNet achieved 97.1% accuracy with 1.2M parameters. Under leakage-aware group K-fold cross-validation, ShuffleNetV2 (98.41%) and EfficientNet-B0 (98.23%) were statistically indistinguishable (paired t-test, p = 0.19), and both significantly outperformed the custom CNNs. On the held-out dataset, accuracy dropped for every model: EfficientNet-B0 generalised best (78.4%), while ShuffleNetV2 fell to 66.2%. Glioma-meningioma confusion was the dominant error mode, and Grad-CAM maps showed that predictions were driven by tumour regions. These results indicate that in-distribution accuracy alone overstates real-world performance and that leakage-aware and cross-dataset evaluation should be reported alongside it.

---


### 282. [Generation as Reverse Encoding](https://arxiv.org/abs/2611.34782)

**<font color=#1a73e8>作者：</font>** Cheng Shi, Sibei Yang, Hanzhong Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained visual representations accelerate generative learning by abstracting away appearance and spatial detail. Yet the same abstraction makes the return to pixels far harder, shifting much of the burden onto a larger decoder. We ask why the representation-to-pixel path should be learned independently when the encoder already provides a learned pixel-to-semantics path (the semantic encoding path). We introduce RevFlow, based on the principle of generation as reverse encoding. RevFlow uses intermediate representations of a frozen encoder as successive generative targets, first generating deep semantic representations, then shallow representations that retain appearance and spatial detail, before decoding to pixels. To learn these transitions without training a separate generator for each stage, we develop HyC-DiT, a unified generative model with a standard DiT backbone shared across stages and stage-specific condition injection. We further show that native matching in semantic representation space enables few-step generation. RevFlow accelerates both learning and sampling. On ImageNet $256 \times 256$, RevFlow reaches 1.96 FID at 690M and 1.74 FID at 1.55B after only 5 training epochs. It also achieves 30.25 dB reconstruction PSNR with an 89M decoder. After a short native-matching adaptation phase, RevFlow-XL achieves 2.85 FID using a single sampling step in each stage. Our code repository is at this https URL

---


### 283. [CIRKDV2: Cross-Image Relational Knowledge Distillation with Contextual Modeling for Efficient Semantic Segmentation](https://arxiv.org/abs/2611.34795)

**<font color=#1a73e8>作者：</font>** Chuanguang Yang, Yu Wang, Chengqing Yu 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing Knowledge Distillation (KD) methods for semantic segmentation often guide the student to mimic the teacher's structured information generated from an individual image. However, they ignore the global semantic relations across various images that are valuable for KD. This paper proposes Cross-Image Relational KD V2 (CIRKDV2), which focuses on transferring structured pixel-to-pixel, pixel-to-region, and channel-to-channel relations modeled from global images in the dataset. A large teacher network often constructs a well-structured feature space in terms of global contextual dependencies. CIRKDV2 makes the student mimic the better structured semantic relations of the teacher, thus improving the feature representational capability. Beyond relational distillation, we further propose contextual feature distillation by using context aggregation to augment student pixel embeddings to match the semantic level with the teacher. This avoids the semantic gap problem between the teacher and student occurred in traditional feature distillation studies. Experimental results on Cityscapes, ADE20K, Pascal VOC, and COCO-Stuff-164K demonstrate that CIRKDV2 outperforms the state-of-the-art semantic segmentation distillation methods by large margins across various network architectures. Our code and pre-trained models are publicly available at this https URL.

---


### 284. [Split-RL: Local Conflict Resolution in Reinforcement Learning](https://arxiv.org/abs/2611.34799)

**<font color=#1a73e8>作者：</font>** Benjamin Fuhrer, Chen Tessler, Gal Dalal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) policies are often trained by mixing contradictory feedback that is localized in space and time. For example, a robot may prioritize speed in open areas versus precision in tight gaps. We introduce Split-RL, a Gradient Boosting Trees (GBT) algorithm that uses guidance labels to locally isolate these conflicting signals. Standard neural networks (NNs) lack the structural mechanism to do this, as their parameters share feedback from all sources. While GBT provides the inductive bias to explicitly partition the state-space per objective, standard tree-fitting procedures aggregate contradictory gradient signals before they reach the leaves. Split-RL leverages this bias to integrate guidance labels into tree construction, routing these updates into disjoint state-space regions and preventing signal interference. Such labels can arise from heuristics, sensor-derived events, or existing rule-based systems, allowing Split-RL to incorporate rule-derived structure while retaining a learned policy. We theoretically show how early gradient aggregation loses objective-specific information and characterize when the Split-RL score isolates conflicting updates. We focus on constrained RL and offline RL with mixed datasets, each balancing two objectives that conflict locally. Across domains with spatial, rare-event, and temporal conflicts, Split-RL consistently outperforms existing methods by meeting the episodic cost budget while maintaining competitive rewards. In offline settings, Split-RL localizes the tradeoff between imitation and policy improvement, outperforming other methods and achieving near-expert performance across varying dataset sizes.

---


### 285. [Guidance as Variance Matching](https://arxiv.org/abs/2611.34801)

**<font color=#1a73e8>作者：</font>** Ali Backour, Artem Lukoianov, Frank Permenter 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Guidance repels the prediction of a diffusion model away from a weaker reference prediction. It substantially improves sample quality, but its mechanism remains poorly understood. We first find that, at the scales used in practice, guidance does not improve the prediction of the posterior mean (the model's training target); it makes the prediction worse, while samples improve. Second, posterior-mean predictions have less variance than the data, and we find that guidance restores it. We introduce variance-matched guidance: a closed-form rule that picks the guidance scale by matching the variance of the guided predictions to that of the data. Without tuning, it recovers the hand-picked scales of eleven widely used models across image, video, audio, motion, and world generation; to our knowledge, no previous explanation of guidance predicts them. Applied per noise level, it yields a schedule without tuned hyperparameters that users prefer to hand-crafted ones on SD 3.5 Medium. Third, we offer an interpretation of the mechanism behind guidance: each model makes a random error in predicting the posterior mean, and guidance rescales the difference of these errors into a sample with the posterior's covariance, which improves sampling. This view also suggests two new hypotheses that our experiments support: guidance can work with negative scales, and guiding a model with its own checkpoint needs a larger scale than guiding it with an independently trained model.

---


### 286. [Barron Smoothness for Layers in Deep Neural Networks](https://arxiv.org/abs/2611.34805)

**<font color=#1a73e8>作者：</font>** G. Welper  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In order to bound approximation errors for deep neural networks, we split the problem into two steps: First the selection of optimal infinite width limits for each layer and second an optimal discretization of all layers to obtain finite sized networks. We show that in expectation, the latter problem is equivalently characterized by a layer wise generalization of Barron norms. Moreover, we provide an analysis of the optimization landscape and show that local minima are characterized by an equidistribution principle akin to similar ideas in adaptive spline and finite element approximation.

---


### 287. [WorldExpand: Building Coherent 3D Worlds via Sparse Joint Panoramic Expansion](https://arxiv.org/abs/2611.34810)

**<font color=#1a73e8>作者：</font>** Yuyang Yin, Chenjie Cao, Xuhui Zuo 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Constructing complete 3D worlds from a single panorama is challenging because large portions of the scene remain unobserved. Existing panoramic-video methods expand spatial coverage through dense sequential generation, but neighboring frames contain substantial redundancy, long trajectories accumulate errors, and independently generated directions may be inconsistent. We present WorldExpand, which formulates single-panorama world expansion as the generation of sparse, complementary, and high-resolution panoramic observations. This representation concentrates the generation budget on informative scene regions and preserves the fine-grained details required for 3D construction. WorldExpand addresses two key challenges: where to observe and how to synthesize. Our Coverage-Guided View Selection identifies informative target locations using scene-adaptive quadrants and warp-based coverage scores, while our Joint Panoramic Diffusion uses Gaussian-splatting-based geometric warps to jointly synthesize four pose-grounded and cross-view-consistent panoramas. A diagnostic-guided global--local attention schedule retains global attention only in sensitive layers, reducing the training and inference costs of high-resolution joint generation. The resulting posed panoramas can be directly fed into an existing reconstruction pipeline to build an explicit 3D representation. Experiments show that WorldExpand recovers content behind occluders and around distant corners, improves both novel-view synthesis and downstream 3D reconstruction metrics across various datasets, and generalizes robustly to diverse in-the-wild scenes. WorldExpand runs significantly faster than the state-of-the-art panoramic-video method while producing higher-resolution observations with stronger cross-view consistency.

---


### 288. [HOG-WAM: Improving Visual Robustness through Future Gradient Prediction](https://arxiv.org/abs/2611.34811)

**<font color=#1a73e8>作者：</font>** Boxuan Dong, Yupeng Qian, Ying Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World-action models jointly predict future observations and actions, yet visual corruption can disrupt the resulting policies. We introduce HOG-WAM, which adds future Histograms of Oriented Gradients (HOG) as structural supervision derived directly from demonstration images. An auxiliary HOG diffusion transformer (DiT) module reads RGB features through asymmetric attention, allowing its objective to shape the visual representation used for control. The module is used only during training and removed at inference, preserving FastWAM's RGB-to-action architecture. We evaluate four controlled observation corruptions through a visual-corruption extension of RoboTwin, termed RoboTwin-Plus; HOG-WAM achieves the highest success among the compared policies under all four. Mixed-noise success increases from 78.86% to 82.86% relative to FastWAM, with comparable performance on clean scenes. On LIBERO Plus, overall success increases from 74.49% to 75.26%, with the largest gain under sensor noise, from 74.14% to 78.89%. Across four Franka tasks, average success increases from 40% to 59% under clean observations and from 17% to 24% under noisy observations. A representation ablation favors combining RGB observations with auxiliary HOG prediction over replacing RGB with HOG. These findings support future-gradient prediction as complementary supervision for visually robust control, with larger absolute gains on physical tasks than in simulation. Code is available at this https URL.

---


### 289. [Transferring Architecture as an Optimization Prior](https://arxiv.org/abs/2611.34816)

**<font color=#1a73e8>作者：</font>** Vighnesh Subramaniam, Boris Katz, Brian Cheung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Initialization determines the optimization "fate" of a model, going far beyond just setting the scale of its weights. It establishes a fundamental initial geometry over the input data, dictating certain aspects such as which examples are considered close and which representations gradient descent will naturally refine first. In this paper, we view the initial geometry of a network as an optimization prior and ask whether a network can change its optimization prior by referencing a completely different architecture. To investigate this question, we use an initialization procedure where a target network is aligned to the representational geometry of a randomly initialized guide network before any downstream training occurs. Crucially, alignment to the guide network cannot transfer learned features, never receives gradients, and does not use labels. We demonstrate that this cross-architecture transfer of "fate" benefits the target network in two key domains: (1) instilling the optimization benefits of depth into shallow networks by aligning them to deeper networks, and (2) transferring representational granularity by using fine-resolution networks to shape the geometry of networks with coarser representations. In both cases, the alignment results in improved downstream performance of the target network. Ultimately, this demonstrates that a model's architectural destiny can be decoupled from its physical structure and explicitly modified at initialization.

---


### 290. [Deep Reinforcement Learning for Multi-UAV Data Harvesting Under Variable Team Sizes and Agent Loss](https://arxiv.org/abs/2611.34818)

**<font color=#1a73e8>作者：</font>** Thiago de Souza Lamenza, Bruno José Olivieri de Souza, Markus Endler  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Collecting data from wireless sensors can be challenging when limited communication infrastructure prevents them from offloading their measurements. In such settings, unmanned aerial vehicles (UAVs) can exploit their mobility to harvest data locally, while coordinated UAV teams can provide efficient and redundant coverage of remote areas. Multi-agent reinforcement learning (MARL) enables such teams to learn decentralized coordination policies. However, training separate policies for different team and sensor populations is costly, and fixed-population policies may be vulnerable to agent failures. This work proposes F-MADDPG, a flexible variant of Multi-Agent Deep Deterministic Policy Gradient (MADDPG) that supports data harvesting with varying numbers of wireless sensors and UAVs. The framework also accommodates unexpected catastrophic failures that permanently remove agents during a mission. We compare F-MADDPG with a MADDPG baseline that uses multilayer perceptrons (MLPs) and evaluate training strategies based on team-size sampling and exposure to agent terminations. The results show that F-MADDPG learns across the evaluated population sizes, completes missions faster than the baseline on average, benefits from inverse-cardinality team-size sampling compared with uniform sampling, remains effective after permanent agent losses, and gains no consistent benefit from exposure to failures during training.

---


### 291. [Gradient TD($λ$) for Non-Linear Function Approximation](https://arxiv.org/abs/2611.34826)

**<font color=#1a73e8>作者：</font>** Sujeet Lahane  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal difference (TD) learning is central to reinforcement learning. Many methods use semi-gradient TD, which may diverge, or develop algorithms with mean-squared Bellman or TD-error objectives that are difficult to analyze. Gradient TD algorithms overcome these challenges by using projection of the value function and present convergent off-policy algorithms. However, the algorithm for $\lambda$-return was limited to linear function approximation. Here, we extend the same to non-linear function approximation, which is desirable since many strong modern function approximators are complex and non-linear. Recent works have derived similar algorithms with a generalized projected Bellman error objective. Alternatively, we continue working with the projected Bellman error.

---


### 292. [Beyond Feature Fusion: Sensor-Grounded Semantic-Spiking Learning for Robust Object Detection](https://arxiv.org/abs/2611.34828)

**<font color=#1a73e8>作者：</font>** Hanwen Liang, Wenxuan Liu, Wenxin Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Underexposure weakens object details, and overexposure obscures boundaries. Spike cameras encode light into high-frequency binary streams. Long-window spike counts give stable appearance cues, while short observations reveal changes in firing rates from sparse measurements. We propose SPIRE, a sensor-grounded semantic-spiking framework for illumination-robust object detection from a single spike stream. SPIRE builds an appearance view from the full packet through detection-oriented illumination adaptation and constructs a sequence of cumulative views from progressively longer prefixes. Each prefix supplies a rate map, an edge map, and a rate difference that tracks changes as spikes accumulate. At selected scales, ANN features and spike-derived initialization jointly set the initial membrane potentials and firing thresholds, allowing semantic cues to shape the responses during temporal encoding. Local spike-count contrasts supervise both branches during training. The residual between measured and ANN-predicted contrasts combines with the spiking features to produce a bounded correction to the fused feature pyramid. On simulated VOC and COCO, SPIRE-D outperforms the strongest baseline by 4.00-5.50 AP50 points across the four under- and overexposure settings. On real PKU-Vidar-DVS recordings, it achieves 67.07 AP50 and 40.10 AP75. SPIRE-D also uses 50.4% fewer MACs than SPFD.

---


### 293. [Not all world models can doubt: how training objective and architecture shape epistemic uncertainty in JEPA and RSSM world models](https://arxiv.org/abs/2611.34830)

**<font color=#1a73e8>作者：</font>** Simon Baur, Wojciech Samek, Jackie Ma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models predict how an environment responds to actions, so that candidate actions can be evaluated before execution. Executed actions, or decisions, taken in this manner are only as reliable as the model's predictive capabilities, and predictions in turn are only reliable within the model's experience. Epistemic uncertainty (EU) is the signal that marks where that experience ends. In this work we offer an extensive empirical study on how training objectives and architectures shape epistemic uncertainty of world models. More precisely, we present a controlled comparison of post-hoc EU (last-layer Laplace and ensembles) between two dominant models of different paradigms: 1) LeWorldModel (LeWM): A joint-embedding predictive architecture (JEPA), which predicts the next embedding without a decoder, and 2) DreamerV3: A recurrent state-space model (RSSM), which reconstructs the observation from a recurrent latent state. In ten simulated visual-control environments, we follow a controlled state perturbation of the environment state through every stage of the models up to the final EU estimate. We find that the RSSM attenuates the state perturbation through two mechanisms before it reaches an estimator on the predictor feature. Its recurrent update averages over context, so a change in a single frame reaches the state at a fraction of its size and recovers only as the change persists. Its reconstruction objective weights an entity by the pixels it covers, so a small object can be lost due to the training objective. The JEPA has neither mechanism and passes the change through all stages to the uncertainty. We further show that this translates to gaps in five uncertainty related downstream tasks, from unfamiliar-state detection to uncertainty-penalised planning: the RSSM uncertainty misses deviations that its own posterior registers, whereas the JEPA uncertainty reports what its model sees.

---


### 294. [Full Structure Recovery of Linearized Reed-Solomon Codes](https://arxiv.org/abs/2611.34835)

**<font color=#1a73e8>作者：</font>** Valentina Astore, Martino Borello, Alain Couvreur  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Linearized Reed-Solomon codes (LRS) are optimal sum-rank-metric codes that generalize both Reed-Solomon and Gabidulin codes, and benefit from excellent decoding capabilities, making them potentially interesting candidates for post-quantum code-based cryptography. Previous works have investigated the underlying geometric structure of LRS codes, identifying geometric invariants that distinguish them from random codes. Other works have proposed approaches to recovering the LRS structure from an arbitrary generator matrix, together with additional data. However, both the distinguishers and the recovery techniques proposed so far are either not fully general, or have a prohibitive computational complexity. In this paper, we propose a polynomial-time procedure for the full structure recovery of LRS codes from the sole knowledge of an arbitrary generator matrix. Our results show that, like their Hamming and rank metric counterparts, LRS codes cannot be used as they are for McEliece-like encryption. Our approach combines Overbeck-type attacks with suitable matrix manipulations and shortening techniques to recover the evaluation parameters across different ranges of code dimensions.

---


### 295. [Diffusion Steering via Adaptive Reward Estimation and Resampling](https://arxiv.org/abs/2611.34839)

**<font color=#1a73e8>作者：</font>** Abinitha Gourabathina, Sana Tonekaboni, Marzyeh Ghassemi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion models can generate images that satisfy complex prompts, yet often produce images that omit requested objects, attributes, or relationships. We ask if models can more reliably generate text-aligned images by redistributing probability toward their more successful outcomes. We propose TrailMix, a training-free method that uses the base model's distribution of possible outcomes to adaptively guide generation toward better text alignment. During denoising, TrailMix generates inexpensive lookahead images from parallel trajectories (trails) and scores their alignment with the prompt using an external judge. The resulting distribution of reward scores allows us to estimate how strongly to steer generation toward a desired alignment level. We use these estimates to reweight and resample trajectories, favoring more promising outcomes. Across three text-to-image benchmarks, TrailMix outperforms existing baselines, with particularly strong gains on rare multi-object compositions. We further extend TrailMix to targeted image editing and introduce SEAM-Bench (Semantic Editing and Attribute Maintenance), a systematic benchmark evaluating whether semantic edits preserve other image content. Experiments on SEAM-Bench and existing benchmark PIE-Bench demonstrate the effectiveness of our approach for controlled image editing. Our results show how a model's own possible outcomes can inform reliable and controllable generation.

---


### 296. [Provably Efficient Offline Discounted Reinforcement Learning under Recursive Entropic Risk](https://arxiv.org/abs/2611.34840)

**<font color=#1a73e8>作者：</font>** Amirparsa Bahrami, Oliver Mortensen, Mohammad Sadegh Talebi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study risk-sensitive reinforcement learning in finite discounted infinite-horizon Markov Decision Processes with recursive entropic risk measures (ERM), parameterized by $\beta\neq 0$. We consider both risk-averse ($\beta>0$) and risk-seeking ($\beta<0$) settings. We consider the offline RL setting, where the agent is provided with a fixed dataset and wishes to learn a near-optimal policy using this dataset. We introduce a model-based algorithm, called ERM Value Iteration Lower Confidence Bound (ERM-VI-LCB) and derive a PAC-type bound on its sample complexity. We also establish a corresponding lower bound, demonstrating that exponential dependence on $|\beta|/(1-\gamma)$ asserted by the upper bound is unavoidable in the worst case. The presented bounds provide the first rigorous sample complexity guarantees for offline RL under recursive ERM across both risk-averse and risk-seeking regimes.

---


### 297. [DRBench Pro: A Knowledge-Centric Benchmark for Professional Deep Research Agents](https://arxiv.org/abs/2611.34852)

**<font color=#1a73e8>作者：</font>** Han Huang, Yuchen Yan, Xingyu Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deep research agents gather information from multiple sources and synthesize it into reports on complex, open-ended questions. Existing benchmarks assess report quality along several dimensions, but lack a dedicated knowledge-centric evaluation of which research directions a report covers and how deeply it explores them. We introduce DRBench Pro, a benchmark that makes structured knowledge coverage the primary evaluation target. Our automated pipeline builds local knowledge trees from Wikipedia and uses sampled subgraphs to generate research queries and evidence-grounded rubrics. Each rubric corresponds to a relation in the tree, preserving the structure of the knowledge being evaluated. Agents receive only the research query. This structure allows us to measure breadth across major research directions and depth along related knowledge chains, with their geometric mean giving overall coverage. The benchmark includes 144 cases across 24 domains and 44,102 rubrics. Evaluating 16 deep research agents reveals different strengths in breadth and depth, with the best-performing agent reaching 57.04% overall coverage. Rubric judgments agree closely with human annotations, and agent rankings remain stable across the tested metric configurations.

---


### 298. [TIDE-Flow: Fine-Grained Temporal Evidence and Structured Displacement Matching for Spike Optical Flow](https://arxiv.org/abs/2611.34854)

**<font color=#1a73e8>作者：</font>** Hanwen Liang, Wenxuan Liu, Wenxin Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spike cameras capture high-speed motion through an integrate-and-fire mechanism, providing fine-grained temporal observations without exposure blur. However, their binary streams encode accumulated illumination rather than instantaneous intensity, making reliable motion estimation challenging. Existing spike-based methods exploit temporal aggregation to construct motion representations, but this process may weaken fine-grained firing patterns. Meanwhile, correlation-based estimators often rely on learned matching features without explicitly characterizing the spatial distribution and ambiguity of candidate displacements. To address these challenges, we propose TIDE-Flow, a spike-based optical flow estimation framework that jointly exploits Temporal Integration Evidence (TIE) and Displacement Evidence Encoding (DEE). TIE combines raw spike patterns, multi-scale firing statistics, temporal moments, and boundary-aware interval cues, preserving complementary temporal information before spatial feature compression. DEE further integrates structured candidate-grid features with explicit displacement statistics to characterize matching geometry and competing correspondences. Both components are incorporated into a difference-correlation recurrent refinement framework, enabling effective temporal motion modeling and correspondence estimation. Extensive experiments demonstrate the effectiveness of TIDE-Flow, with controlled ablations validating the contributions of temporal and displacement evidence modeling.

---


### 299. [Model Weights, Airlocks and Sandboxes: A Call for Technical Validation of Re-identification Tests under the EDPB Anonymisation Guidelines](https://arxiv.org/abs/2611.34859)

**<font color=#1a73e8>作者：</font>** Rickard Brännvall, Henrik Forsgren, Erik Ylipää 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Guidelines 02/2026 on anonymisation of the European Data Protection Board (EDPB), published for consultation in July 2026, assess anonymity relative to the entities that may access data. They bring AI models into scope and call for testing, but do not say how a re-identification test should be designed or validated, or how far its result counts as evidence. Building on our reply to the consultation, we describe a framework based on a secure processing environment whose outputs are reviewed before release (an airlock), and distinguish forms of release and three types of evidence: formal, empirical and indirect. We raise seven open questions, each with a scenario, and examine their technical side in three settings: the release of model weights (the trained parameters of a machine learning model), review at an airlock, and regulatory sandboxes, in which an authority supervises development and testing. In each setting the assessment depends on how far a test result can be relied on, since a failed re-identification attempt may mean only that the test was too weak. Drawing on measurement practice in other regulated fields, we call for re-identification tests to be validated as measurement methods, with stated detection limit, bias and uncertainty.

---


### 300. [DocDUR-Net: Degradation-Aware Unified Document Image Restoration](https://arxiv.org/abs/2611.34860)

**<font color=#1a73e8>作者：</font>** Haowei Xu, Peirong Zhang, Xuhan Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Captured document images often suffer from diverse degradations caused by uncontrolled imaging conditions, which reduce readability and obscure fine text structures. Single-degradation restoration methods are usually trained and deployed for individual degradation types, and therefore require model selection before restoration. Unified restoration models alleviate the need to maintain multiple restoration networks by sharing one network across tasks, but representative unified document image restoration methods still depend on external task selection. This dependency limits automatic document image restoration. We propose DocDUR-Net, a degradation-aware unified restoration network that derives restoration guidance directly from the input image. It introduces a Degradation Perception Module (DPM) to extract degradation representations and predict degradation weights, and Degradation Prior-guided Adaptive Feature Fusion (DP-AFF) to combine learnable degradation priors with degradation features extracted from the input. The resulting guidance is injected into a shared restoration backbone, enabling adaptive restoration without external task selection. DocDUR-Net also supports a manual mode with explicit task selection. Experiments on document image restoration benchmarks show that DocDUR-Net achieves the best average PSNR of 29.405 dB and SSIM of 0.960 among unified methods while remaining competitive with single-degradation methods.

---


> [!TIP]
> 当前位于：**251-300**（第 6/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-314](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
