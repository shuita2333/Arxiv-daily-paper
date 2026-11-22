# 📦 其他研究 | 2026年11月23日

> 本类共 **265** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-265**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-265**

---

### 251. [Hybrid Retrieval for Government Scheme Search in English and Marathi](https://arxiv.org/abs/2611.26514)

**<font color=#1a73e8>作者：</font>** Aishwarya Gunjal, Kanchan Khemnar, Pawan Poojary 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retrieving government schemes requires matching citizens' information needs to formal administrative descriptions, often across languages and terminology. We present a bilingual search system for Maharashtra government schemes and public services that combines BM25 retrieval with sentence-embedding similarity through equal-weight score fusion. The system indexes aligned English-Marathi scheme descriptions and supports multilingual, Marathi-focused, and translation-mediated semantic configurations. Evaluation on manually curated bilingual queries compares BM25, dense retrieval, and hybrid retrieval using IndicSBERT and MahaSBERT. BM25 provides a strong baseline with a mean reciprocal rank (MRR) of 0.864. Hybrid retrieval increases MRR to 0.872 with IndicSBERT and 0.879 with MahaSBERT, whereas the corresponding dense-only systems achieve 0.663 and 0.655. MahaSBERT-based fusion also increases precision from 0.781 to 0.808 while matching BM25 recall at 0.946. These results support the complementary use of lexical and semantic signals in this collection, while showing that improvements over a strong lexical baseline are modest and metric-dependent. The study provides an application-focused analysis of hybrid retrieval for bilingual public-service information access.

---


### 252. [Plan4D: Generative Plannable 4D Worlds](https://arxiv.org/abs/2611.26516)

**<font color=#1a73e8>作者：</font>** Hangwei Zhang, Rujing Dang, Ruimin Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most world models for future prediction prioritize aestetic quality of generated videos, but offer only weak physical grounding and limited geometric consistency over time, due to the lack of explicit 4D modeling. In this paper, we introduce plan4d, a possible next milestone towards building a generative plannable 4D world model that predicts future RGB videos together with dense 4D geometry, including depth, cameras, point clouds, and scene flow from an observed scene context and text-specified actions. Since training data with paired actions and dense 4D annotations is inherently scarce, plan4d leverages the complementary priors of foundational video generators and 3D reconstructors. Specifically, we propose a model-stitching architecture that couples Depth Anything 3 with LongCat-Video and augments it with an auxiliary DPT head for scene-flow prediction. The resulting model allows us to plan and generate complex, long-horizon, and fine-grained actions in a dynamic 3D scenes, while substantially improving both visual fidelity and geometric accuracy of the generated future videos. Extensive experiments on both synthetic and real-world datasets demonstrate that plan4d achieves state-of-the-art performance in generative 4D modeling of environmental reactions. Project Page: this https URL

---


### 253. [The Window Lever: Longer Observation Windows Outweigh the Observed Effects of Data, Capacity, and Architecture in Customer Behavior Forecasting](https://arxiv.org/abs/2611.26521)

**<font color=#1a73e8>作者：</font>** Tara Sowrirajan, Yanqiao Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In our experiments on long-horizon customer-behavior forecasting, a longer observation window outweighed the observed effects of more data, more capacity and newer architectures. The window is the weeks of history a model sees before the week it forecasts from. Going from an 8- to a 16-week window adds a raw +0.070 to 0.107 log-space $R^2$ in every family at 1M. Matched test cohorts, which score the same customer-weeks at every window, show this raw comparison understates the gain in every family they cover. The direction holds on five public datasets, four spanning over a year (ridge and our transformer on all five). On our internal data, longer windows admit up to 10% more and colder training customers, which matching does not fix. Our design does not separate window length from calendar coverage, because every test anchor (the week a forecast is made from) falls in one eight-week band. On training-period anchors, the weekly ridge probe's gain persists outside the holiday season, keeping about 72% of it. We therefore report a robust positive association with longer windows and do not identify the magnitude of a calendar-independent history effect. Of four internally registered predictions, the only fully blind one failed. An activity-mixture model predicted +0.014 from 24 to 32 weeks; the weekly-aggregate probe returned -0.0004. For the sequence families, the other three levers are about an order of magnitude smaller, bounded and unresolved. Their observed effects are at most 0.006 between the nominal 1M and 10M tiers and 0.0052 among five sequence families at 16 weeks with clocks as built, both single-seed on the full test split, and 0.006 for capacity on three-seed means. These are observed intervals, not equivalence bounds. Our claim is the order-of-magnitude contrast between the window and those bounds. A team building on this class of data should start by lengthening the window.

---


### 254. [Deterministic Temporal Embedding for Calcium Imaging Trace Extraction](https://arxiv.org/abs/2611.26522)

**<font color=#1a73e8>作者：</font>** Qi Gao, Julius Beichert, Miriam Ratliff 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable extraction of calcium-dependent fluorescence traces in calcium imaging sequences requires identifying pixels whose fluorescence intensity reflects the same underlying cellular activity. We present a deterministic temporal embedding framework that maps pixel-wise fluorescence traces to a low-dimensional representation in which temporally coherent sources form spatially coherent regions. Starting from a fuzzy-neighborhood graph and spectral initialization, we optimize a class-balanced cross-entropy objective using exact sparse attraction and a deterministic particle-mesh decomposition of the dense repulsive interaction with sparse edge compensation, avoiding stochastic negative sampling. The resulting latent representation is spatially decoded into reliable source supports for trace extraction without imposing an explicit cellular shape prior. Experiments on synthetic and in vivo two-photon calcium imaging data demonstrate robust recovery of irregular and spatially touching sources together with efficient deterministic embedding optimization.

---


### 255. [Backtracking Agent Applications Security Incidents](https://arxiv.org/abs/2611.26525)

**<font color=#1a73e8>作者：</font>** Yicheng Cai, Taegyu Kim, Peng Liu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent applications are increasingly deployed, yet agent-specific attacks pose real threats to them. Upon a security incident, organizations backtrack to identify the CEP (compromise entry point), remediate the damage, and prevent its recurrence. The main artifacts available for backtracking are trajectory logs, which record agent functionalities, and source code; app(lication)-specific function call logs are often fairly limited. However, trajectory logs are at the agent functionality abstraction layer, while the CEP candidates are function calls at the app code execution layer. Due to this semantic gap, the analyst needs to manually inspect the relevant code for each CEP candidate to infer its corresponding agent functionality. In this work, we present Origin, a backtracking tool for the analyst to submit a small number of queries to identify CEPs that existing tools cannot provide. Our approach poses two challenges: (1) define the intermediate abstraction that captures the mapping relationships between the two semantic layers; (2) determine the region-to-variable mapping for constructing the cross-layer graph defined in the intermediate abstraction. Each region is a specific group of agent functionalities. Origin addresses the challenges by (1) the cross-layer dependency graph (CLDG) that connects region-inferred functions at the semantic level to the variables in the low-level taint propagation subgraph, plus the associated query language, and (2) the region inference algorithm. Case studies on five popular agent applications across eight attack incidents show that an analyst using Origin correctly identifies all the CEPs.

---


### 256. [MM-SystemOneBias: Evaluating Bias in Multimodal Jev-Style System One Decision Models](https://arxiv.org/abs/2611.26557)

**<font color=#1a73e8>作者：</font>** Jinzhe Li, Qi Wang, Dandan Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When multimodal decision models determine actions, moderation outcomes, or quality judgments, their reliability depends on preserving semantic decisions across presentation changes, ignoring irrelevant additions, and distinguishing information consistent with task evidence from information that conflicts with it. Existing evaluations study decision-interface biases and multimodal model behavior in separate settings, leaving no common protocol to compare multimodal decision models with their backbones on practical tasks. We introduce \textbf{MM-SystemOneBias}, which evaluates 13 models on 5,323 original instances from nine public datasets and 11 task scenarios using six paired interventions: option order, option label, external judgment, image--text description, irrelevant information, and rating scale. Across seven matched decision-model--backbone pairs, decision models are more stable under option-label, irrelevant-information, and rating-scale changes in all seven pairs; six pairs also show lower option-order flip rates. They incur smaller accuracy losses under incorrect external judgments in all seven pairs and conflicting descriptions in six. In six pairs, they gain less accuracy from correct external judgments and show less favorable accuracy changes under consistent descriptions. Among pairs with unchanged semantic decisions, mean absolute changes in answer probabilities range from 4.56 to 11.55 percentage points, revealing input effects that accuracy alone misses.

---


### 257. [GEOHunter: Mapping a Generative Engine Optimization Network in the Wild](https://arxiv.org/abs/2611.26564)

**<font color=#1a73e8>作者：</font>** Sean Tang, Peiran Wang, Ying Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Generative engines synthesize retrieved web pages into answers, recommendations, and rankings. Generative engine optimization (GEO) services sell visibility in these answers by publishing promotional articles on user-generated-content (UGC) platforms for paying clients. Such promotion raises concerns in medical and financial domains, where misleading advice can cause harm. To study the severity of this problem, we measure one such paid-content operation across three major Chinese UGC platforms, uncovering 1,985 accounts associated with the network comprising 466,357 inferred promotional placements. We find that the network promotes products across diverse categories through a growing pool of accounts, conducting coordinated campaigns spanning months across multiple platforms while evolving its listicle content over time. Across nine generative engines from both the US and China, we find that 4.5% to 20% of retrievable cited pages are attributable to the network, depending on how strictly attribution is drawn. On eight of these engines, its clients are named in 52% of answers, against 68% for category leaders. Our work demonstrates the effectiveness of UGC GEO placement at influencing generative engine outcomes, and reveals content-level defenses as insufficient against coordinated UGC placements, where account-level and platform-level signals are necessary for proper defense.

---


### 258. [ProtoDiffusion: Token-per-Layer Generative Modeling of Multi-Layer Images](https://arxiv.org/abs/2611.26586)

**<font color=#1a73e8>作者：</font>** Adrià Ciurana Lanau, Harleen Hanspal, Lusine Abrahamyan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graphic designs are ordered compositions of RGBA layers whose separation enables selection, movement, and reuse. Existing layered models represent each layer with a full-canvas or region-sized spatial latent grid, so representation size grows with the cumulative spatial extent of the layers. We present ProtoDiffusion, a latent-diffusion framework built on ProtoVAE, a multi-layer variational autoencoder that encodes a design into one shared spatial prototype and one candidate vector per layer. Each candidate conditions a shared decoder to reconstruct its corresponding RGBA layer. For $N$ layers, the representation contains $HW+N$ tokens before backbone-specific packing, compared with $NHW$ for full-grid-per-layer representations. ProtoDiffusion jointly denoises the prototype and a fixed set of candidate slots, conditioned on an image or text, with bounding boxes as optional layout guidance. The model leaves unneeded slots empty and determines the number of layers and, in absence of boxes, their layout, requiring neither as input. The same architecture supports both image-to-design and text-to-design. ProtoVAE achieves high-fidelity reconstruction from its compact shared latent representation, reaching 40.43 dB PSNR on layer crops. On the LayerD evaluation split, image-to-design achieves RGB L1 scores of 0.040 with bounding boxes and 0.057 without, with box-guided alpha soft IoU (0.850) comparable to the strongest fine-tuned baseline (0.871). On merged images, text-to-design reaches 66.41 FID versus 86.84 for FLUX.2 [klein], achieves a 0.860 text-accuracy score, and runs $19.1\times$ faster than the same-backbone generation-then-decomposition cascade.

---


### 259. [Active Feature Acquisition by Distilling an Oracle Teacher](https://arxiv.org/abs/2611.26598)

**<font color=#1a73e8>作者：</font>** Yang Meng, Zixin Ding, Robert L. Grossman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Acquiring every feature of an instance is often costly: a measurement can carry a monetary price, a time delay, or a privacy cost. Active Feature Acquisition (AFA) addresses this by learning a policy that decides, per instance, which features to acquire under a budget. Existing AFA methods train this policy by optimizing a self-constructed utility target rather than distilling an explicit teacher. We construct this teacher explicitly. At training time the label and the unobserved feature values are available, and together they determine the teacher in closed form: an oracle that ranks every candidate by its effect on the downstream predictor's error. OracleImitator distills this ranking into a deployable policy by soft-target imitation. Across multimodal medical diagnosis and the AFABench benchmark, OracleImitator matches or outperforms existing AFA methods across the budget range, recovering 90% of the attainable accuracy gain at under a quarter of the acquisition cost. Because the teacher is an explicit algorithmic object rather than an implicit optimization target, we can also measure directly how much of its ranking is recoverable by a policy restricted to what is visible at deployment.

---


### 260. [Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth](https://arxiv.org/abs/2611.26603)

**<font color=#1a73e8>作者：</font>** Peiyun Hu, Marko Mihajlovic, Lyndon Duong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Depth Pro 2, an approach to estimating dense metric depth for images and video at full resolution. By analyzing prior methods for monocular depth estimation, we find that they commonly trade off temporal consistency and boundary sharpness: multi-frame methods favor consistency, single-frame methods favor sharpness. To overcome this trade-off, we train a single, scalable network that processes both images and video and predicts depth maps at native resolution. Depth Pro 2 produces depth maps that are metrically accurate, sharp, and temporally consistent all at once, outperforming prior work in all of these dimensions. We release a family of models that define a new Pareto frontier in terms of metric accuracy, sharpness, temporal consistency, and runtime. We release code and weights at this https URL

---


### 261. [Bio-PM-Guided Synthetic IMU Generation](https://arxiv.org/abs/2611.26607)

**<font color=#1a73e8>作者：</font>** Deepali Singh, Deepesh Parpani, Aviral Gupta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Collecting and labeling inertial measurement unit (IMU) data for human activity recognition (HAR) is expensive, and models trained on one group of subjects often fail to generalize to unseen individuals. Even with balanced data, classifiers struggle to distinguish dynamically similar activity classes and benefit from targeted augmentation. We explore whether synthetic IMU data generated in the representation space of a pretrained biosignal encoder, Bio-PM \cite{b1}, can serve as a practical augmentation source. Rather than synthesizing raw signals, we leverage Bio-PM's frozen encoder to convert 10-second IMU windows into token embedding sequences and train class-conditional decoders in this space: (1) an autoregressive transformer decoder that predicts tokens sequentially, and (2) a diffusion decoder that learns the token distribution through a denoising objective. We analyze generation realism through distributional metrics and embedding-space visualizations, evaluate downstream utility through leave-one-subject-out HAR classification, and present a PatchDecoder for approximate raw waveform reconstruction. Our diffusion decoder achieves a Train-on-Synthetic-Test-on-Real (TSTR) macro-F1 of 0.68, demonstrating that generated tokens are realistic enough to train a classifier that transfers to real data. Combining synthetic-token augmentation with a 320-dimensional gravity-aware feature representation raises LOSO macro-F1 from 0.729 to 0.809 over a real-only baseline across 51 subjects on the WISDM benchmark, with statistically significant gains concentrated in the most challenging activity classes. These results demonstrate that high-fidelity generation in a pretrained encoder's representation space is achievable and practically useful for cross-subject HAR augmentation.

---


### 262. [One Prior, Two Dynamics: Repurposing Video Diffusion Transformers for Self-Supervised Latent Action Learning](https://arxiv.org/abs/2611.26617)

**<font color=#1a73e8>作者：</font>** Yuxin Jiang, Wenqiang Sun, Jiaqi Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Videos reveal how the world changes, but rarely the actions that cause those changes. Latent action learning recovers such supervision from visual transitions, yet often learns the underlying dynamics largely from scratch. We ask whether a pretrained video generator can instead provide the prior for both inverse and forward dynamics. We introduce O$^{2}$LaF, built on a simple principle: one prior, two dynamics. We initialize both models from the same pretrained video DiT and adapt them to their distinct roles: a feed-forward transition encoder with learnable action queries for inverse dynamics, and a causal, action-conditioned video generator for forward dynamics. By controlling information access and optimizing both dynamics end-to-end through a compact bottleneck, O$^{2}$LaF learns transferable actions from unlabeled videos. Across navigation and robotic manipulation, O$^{2}$LaF sets a new state of the art in few-shot action probing and enables stronger zero-shot action transfer across visual contexts and embodiments. Beyond generative video priors, we further extend our framework to predictive representation priors such as V-JEPA2, achieving competitive performance. Our findings suggest a broader paradigm for latent-action learning: repurposing pretrained video models to discover transferable actions and predict their consequences.

---


### 263. [PlayCraft: Designing Engaging Games from Agent Play Experience](https://arxiv.org/abs/2611.26624)

**<font color=#1a73e8>作者：</font>** Weihao Cheng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent AI agents can generate playable games, but these games are not necessarily engaging. Mastery is a key source of engagement, yet designing for it requires extensive human play and tuning. We propose PlayCraft, an automated framework that uses a vision-based agent to play games and draws on its detailed play experience to revise them for mastery. Starting from an initial game, PlayCraft alternates between playing and crafting. In the playing stage, a player agent watches the game screen, uses the controls, and pursues the game objective over repeated episodes while retaining memory. After each episode, it reports its progress, outcomes, decisions, and reflections. In the crafting stage, a crafter agent uses these reports to revise the game. It estimates player abilities, predicts performance at different proficiency levels, and compares those predictions with a target learning progression. It diagnoses the game and addresses the gaps by giving players meaningful opportunities to improve through better decisions and execution. We evaluate games in fresh runs with player agents across three intelligence settings, measuring learning gain and learning slope. Compared with the initial games, PlayCraft yields larger learning gains and steeper learning slopes in most games. It also outperforms the baselines on the macro-average of each metric at every intelligence setting.

---


### 264. [RL Post-Training in Diffusion Transformers Is Activation Steering](https://arxiv.org/abs/2611.26627)

**<font color=#1a73e8>作者：</font>** Tuna Han Salih Meral, Kaan Oktay, Alec Helbling 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) post-training substantially improves the visual quality, text rendering, and compositional accuracy of diffusion transformers. Because capabilities such as rendering requested text or composing multiple objects are inherently prompt-dependent, a natural hypothesis is that improving them requires learning complex, input-dependent transformations. To isolate how much of these gains an input-independent shift explains, we probe each RL-tuned model with a deliberately simple parameterization: a fixed set of steering vectors added to the block outputs of the frozen base model. On SD3.5-M, these vectors hold 65x fewer parameters than the RL-tuned LoRA (0.29M against 18.8M). We fit them to match the velocity predictions of public RL-tuned checkpoints, with no reward in the objective. Although the vectors are identical for every prompt, token, and sampling seed, they recover 90.0-96.3% of the reward gains of six RL-tuned image models, and 89.8% and 111.9% on two RL-tuned video models. Initialized at zero and trained with online RL, the vectors alone exceed the reward gains of weight-based RL on text rendering (OCR) and human preference (PickScore) on SD3.5-M. A constant shift thus suffices for most of the gain of policy-gradient RL post-training: without new input-dependent transformations, it steers the pretrained generator toward what it can already compute.

---


### 265. [Posterior Matching Distillation](https://arxiv.org/abs/2611.26629)

**<font color=#1a73e8>作者：</font>** Hidir Yesiltepe, Julius Berner, Arash Vahdat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion distillation accelerates image and video generation by compressing a pretrained teacher's iterative sampling process into a few network evaluations. Distribution-based methods achieve this by matching the student's output distribution to the teacher's. This matching is often driven by reverse-KL objectives, whose mode-seeking bias favors dominant teacher modes at the expense of diversity across samples. We introduce Posterior Matching Distillation (PMD), a new member of the distribution-based distillation family that combines mode-covering posterior sampling with any-step generation. At zero population loss, PMD recovers the teacher's full posterior of clean images at each trained noise level. Its stochastic student supports any-step sampling budgets within the trained timestep grid without further training. To learn these posteriors, PMD matches exponentially reweighted averages of student samples conditioned on a fixed noisy state to corresponding teacher posterior means. Under Gaussian corruption, exponentially tilted posterior mean is a single teacher evaluation at a shifted input. We prove that, matching tilted means over an open neighborhood uniquely identifies the full posterior. PMD thus supervises the entire conditional distribution through a family of mean constraints, without any auxiliary student-score network. Experiments on SDXL and FLUX.2 [klein] 4B demonstrate that PMD achieves the best FID among 4-step methods on both models, while maintaining competitive or leading performance across prompt-alignment and perceptual-quality metrics.

---


> [!TIP]
> 当前位于：**251-265**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-265**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
