# 📦 其他研究 | 2026年06月01日

> 本类共 **317** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-317](./part-07.md)

---

### 1. [Escaping the Linearity Trap: Manifold Detours for Black-Box Adversarial Attacks on Singing Audio Deepfake Detection](https://arxiv.org/abs/2605.30366)

**<font color=#1a73e8>作者：</font>** Yifan Liao, Yule Liu, Zhen Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent Singing Voice Synthesis (SVS) advances enable highly realistic but potentially malicious AI covers, making singing voice deepfake detection (SVDD) crucial. Self-Supervised Learning (SSL)-based detectors achieve state-of-the-art performance by fine-tuning speech SSL backbones to capture singing-specific spoof artifacts. Existing adversarial attacks often fail against SSL-SVDD, creating a false impression of inherent robustness. We reveal this stems from two challenges. First, at the objective level, attacks optimize cross-entropy on local surrogates, crossing surrogate-specific boundaries rather than suppressing shared spoof evidence. Second, at the method level, attacks follow the surrogate's dominant gradient direction. In SSL-SVDD, this aligns with fine-tuned artifact-sensitive directions, limiting transferability to unseen detectors - a geometric failure we term the Linearity Trap. To properly evaluate robustness, we propose MARS (Meta-Adversarial Regression of Semantics), a transfer-based black-box framework tailored to SSL-SVDD. Structurally, MARS shifts to hypothesis-evidence manipulation by constructing a natural semantic anchor from the pre-trained SSL space and an artifact anchor from the fine-tuned space. Algorithmically, MARS escapes the Linearity Trap via bi-level optimization: the inner stage induces tangential exploration, while the outer stage guides the audio toward the natural semantic manifold. Experiments on the CtrSVDD benchmark show MARS improves Attack Success Rate (ASR) in in-distribution transfer (13%), out-of-distribution transfer (10%), and cross-task evaluation (36%), highlighting the urgent need for robust SVDD systems.

---


### 2. [Gait2Hip-60: A Unified Deep Learning Benchmark for Predicting Hip Muscle Forces and Joint Moments from Multi-Cadence Gait Kinematics](https://arxiv.org/abs/2605.30374)

**<font color=#1a73e8>作者：</font>** Jiaqi Zhang, Ji Hou, Qing Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating hip muscle forces and joint moments during gait typically relies on musculoskeletal simulation, which is informative but time-consuming and difficult to apply in clinical settings. This study developed a deep learning framework to predict these hip dynamics parameters directly from lower-limb gait kinematics and compared three representative sequence models under a unified protocol. Gait data were collected from 60 healthy adults under three metronome-guided cadence conditions. Ten bilateral lower-limb joint angles were used as inputs, and OpenSim-derived hip muscle forces and hip joint moments were used as reference outputs. Three deep learning models of LSTM, Transformer, and Mamba were trained and evaluated using the same subject-level split, preprocessing pipeline, and metrics. The best model was then directly tested on an external cohort of 9 patients with osteonecrosis of the femoral head (ONFH) without retraining. In the healthy-subject benchmark, Transformer achieved the best subject-level mean performance for both hip muscle force prediction (RMSE = 1.33 N/kg, MAE = 0.57 N/kg, R2 = 0.819) and hip joint moment prediction (RMSE = 0.11 Nm/kg, MAE = 0.07 Nm/kg, R2 = 0.862), with similar advantages across walking cadences. In zero-shot external validation, Transformer retained moderate predictive ability in ONFH for hip muscle force prediction (RMSE = 1.51 N/kg, MAE = 0.70 N/kg, R2 = 0.537) and hip joint moment prediction (RMSE = 0.17 Nm/kg, MAE = 0.12 Nm/kg, R2 = 0.569). These findings support the feasibility of estimating hip dynamics from gait kinematics, identify Transformer as a strong baseline, and highlight the need for broader pathological validation and improved generalization before clinical application.

---


### 3. [Unicorn: Scaling High-Dimensional Time Series Forecasting via Universal Correlation Modeling](https://arxiv.org/abs/2605.30376)

**<font color=#1a73e8>作者：</font>** Haochen Yuan, Yichen Song, Yunbo Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern time series architectures face a fundamental trade-off: channel-independent models scale well with increasing data volume but ignore critical inter-channel dependencies, while channel-dependent models are expressive but remain ``dimension-bounded'', struggling to generalize across heterogeneous this http URL bridge this gap, we introduce Unicorn (Universal Correlation Network), a framework for scalable, multi-dataset pretraining on high-dimensional time series. At the core of Unicorn is a latent prototype codebook that decouples correlation modeling from specific channel identities. By projecting heterogeneous channels into a shared latent space, UniCorN learns identity-agnostic, reusable interaction patterns that transfer across domains with diverse dimensionalities and semantics. Extensive experiments show that Unicorn significantly outperforms state-of-the-art forecasting architectures, particularly in few-shot transfer scenarios, offering a scalable path toward multivariate time series foundation models.

---


### 4. [Lightweight SAR Ship Detection via Contrastive Distillation](https://arxiv.org/abs/2605.30380)

**<font color=#1a73e8>作者：</font>** Surendar Devasundaram, Saber Latibari Banafsheh, Abhijit Mahalanobis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep convolutional and transformer-based detectors achieve strong performance for SAR ship detection but are often computationally prohibitive for real-time or onboard deployment. Lightweight models offer improved efficiency yet struggle to capture the complex structural relationships inherent in SAR backscatter. Most existing SAR knowledge-distillation approaches rely on feature or logit matching, which enforces localized activation similarity while neglecting the geometric relationships among object representations. We propose a Structured Unified Relational knowledGE distillation framework for SAR Ship detection (SURGE) that transfers relational geometry from a powerful teacher detector to a compact student detector using a contrastive InfoNCE objective in a shared projection embedding space. To the best of our knowledge, this work presents the first transformer-based SAR ship detector knowledge distillation framework in SAR domain. The framework is architecture-agnostic in the sense that it provides a common region-level distillation interface for two-stage, one-stage and transformer-based detectors without modifying their deployed architectures. Experiments on the SSDD and HRSID benchmarks demonstrate that the proposed method yields substantial improvements for two-stage detectors, achieving up to 6.2 mAP and 8.0 AP75 gains over baseline student and even surpassing teacher performance

---


### 5. [Functional MRI Time Series Generation via Wavelet-Based Image Transform and Spectral Flow Matching for Brain Disorder Identification](https://arxiv.org/abs/2605.30387)

**<font color=#1a73e8>作者：</font>** Hwa Hui Tew, Junn Yong Loo, Fang Yu Leong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Functional Magnetic Resonance Imaging (fMRI) provides non-invasive access to dynamic brain activity by measuring blood oxygen level-dependent (BOLD) signals over time. However, the resource-intensive nature of fMRI acquisition limits the availability of high-fidelity samples required for data-driven brain analysis models. While modern generative models can synthesize fMRI data, they often remain challenging in replicating their inherent non-stationarity, intricate spatiotemporal dynamics, and physiological variations of raw BOLD signals. To address these challenges, we propose Dual-Spectral Flow Matching (DSFM), a novel fMRI generative framework that cascades dual frequency representation of BOLD signals with spectral flow matching. Specifically, our framework first converts BOLD signals into a wavelet decomposition map via a discrete wavelet transform (DWT) to capture globalized transient and multi-scale variations, and projects into the discrete cosine transform (DCT) space across brain regions and time to exploit localized energy compaction of low-frequency dominant BOLD coefficients. Subsequently, a spectral flow matching model is trained to generate class-conditioned cosine-frequency representation. The generated samples are reconstructed through inverse DCT and inverse DWT operations to recover physiologically plausible time-domain BOLD signals. This dual-transform approach imposes structured frequency priors and preserves key physiological brain dynamics. Ultimately, we demonstrate the efficacy of our approach through improved downstream fMRI-based brain network classification. The code is available at this https URL .

---


### 6. [A Novel Evaluation Metric for Unsupervised Learning in AIS-Based Maritime Anomaly Detection: MADQI](https://arxiv.org/abs/2605.30388)

**<font color=#1a73e8>作者：</font>** Ismet Gocer, Zakirul Bhuiyan, Raza Hasan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper introduces a new systematic framework for detecting anomalies in maritime Automatic Identification System (AIS) datasets. These anomalies include abnormal vessel behaviours related to speed, position jumps, time gaps, and turn angles. Although unsupervised learning algorithms such as Isolation Forest are widely used for detecting anomalous vessel movements, they often lack systematic and meaningful evaluation measures. To address this limitation, we propose a novel quality metric called Maritime Anomaly Detection Quality Index (MADQI). The prosed MADQI is a composite index designed to evaluate the anomaly detection performance of machine learning models without requiring labelled data. The proposed framework uses Haversine distance calculations to analyse AIS datasets and identify anomalies based on their spatial and behavioural characteristics. The proposed MADQI evaluation framework integrates four interconnected metrics: Anomaly Rate Consistency (ARC), Physical Plausibility Score (PPS), Score Distribution Separation (SDS), and Extreme Case Evidence (ECE). These metrics are combined through automatic normalisation using multi-chunk evaluation and adaptive scaling techniques. Experimental results on the AIS dataset show that the proposed framework achieved a MADQI score of 80.37%, demonstrating its effectiveness for unsupervised anomaly detection. In particular, the algorithm performed strongly in identifying abnormal vessel behaviour. Among the individual MADQI components, ECE and ARC achieved scores of 0.907 and 1.000, respectively, indicating excellent capability in detecting extreme anomalies and maintaining anomaly rate consistency. Overall, these results are encouraging and demonstrate that the proposed framework provides a reliable and meaningful approach for evaluating unsupervised anomaly detection in maritime AIS data.

---


### 7. [Delayed Repression and Emergent Instability in Adaptive Multi-Agent Systems](https://arxiv.org/abs/2605.30392)

**<font color=#1a73e8>作者：</font>** Igor Itkin  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Regulatory institutions (from content moderation platforms to financial supervisors) observe, deliberate, and intervene only after a characteristic delay. We ask whether this processing lag alone can destabilize a multi-agent system that would otherwise remain stable, without exogenous shocks, coordination among agents, or malicious actors. We study this question in two stages. First, we analyze a delayed replicator equation in which autonomous agents receive a benefit from radical behavior but face punishment based on a lagged institutional alarm signal. We derive a closed-form critical delay threshold beyond which the unique interior equilibrium loses stability through a Hopf bifurcation, and prove via center manifold reduction that the bifurcation is supercritical (producing bounded oscillations, not explosive growth) for the entire sigmoid response-function family. Second, we embed $N=240$ agents on a network and equip them with reinforcement learning (tabular Q-learning), comparing three decision architectures in a factorial design: non-reactive agents (fixed policy), reactive agents (threshold heuristic without memory), and Q-learning agents (adaptive with cumulative value estimates). The results reveal a hierarchy opposite to the naive expectation that learning amplifies instability: non-reactive agents are immune to delay (0% runaway across all tested values), reactive agents collapse catastrophically (96% runaway by delay $\geq 8$ steps), and Q-learning agents achieve partial resilience (66% runaway at delay $= 20$). The destabilizing ingredient is reactivity to delayed signals: agents that immediately exploit low-alarm windows trigger oscillatory feedback loops. Learning buffers this through implicit punishment memory encoded in Q-values

---


### 8. [SANA-Streaming: Real-time Streaming Video Editing with Hybrid Diffusion Transformer](https://arxiv.org/abs/2605.30409)

**<font color=#1a73e8>作者：</font>** Yuyang Zhao, Yicheng Pan, Qiyuan He 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time streaming video-to-video editing (V2V) is critical for interactive applications such as live broadcasting and gaming, yet it remains a formidable challenge due to the stringent requirements for temporal consistency and inference throughput. In this paper, we present SANA-Streaming, a system-algorithm co-designed framework for high-resolution, real-time streaming video editing on consumer GPUs, with the following three core designs: (1) Hybrid Diffusion Transformer architecture introduces softmax attention in part of the blocks to improve local modeling capabilities while preserving the efficiency of linear layers. (2) Cycle-Reverse Regularization is a novel training strategy that enforces semantic consistency by predicting source frames from generated content via flow matching, improving temporal consistency without requiring paired long edited videos. (3) Efficient System Co-design combines fused GDN kernels and Mixed-Precision Quantization (MPQ) optimized for the NVIDIA Blackwell (RTX 5090) architecture. By profiling real-world throughput, our MPQ maximizes Tensor Core utilization while maintaining generation quality. The resulting system achieves real-time 1280 x 704 resolution editing at 24 end-to-end FPS on a single RTX 5090 GPU, with the DiT core running at 58 FPS. Experimental results demonstrate that our co-design approach significantly outperforms existing SOTA methods in both temporal coherence and system throughput.

---


### 9. [DTG-Restore: Training-Free Diffusion Refinement for Generative Video Super-Resolution](https://arxiv.org/abs/2605.30431)

**<font color=#1a73e8>作者：</font>** Hidir Yesiltepe, Koutilya PNVR, Gaurav Pathak 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent progress in video diffusion models has enabled remarkable generative fidelity, yet leveraging these priors for restoration remains limited by the strong coupling between conditional and unconditional branches in standard classifier-free guidance. We introduce a training-free framework that enhances distorted and low-resolution videos by decoupling these signals in time. Our proposed Decoupled Time Guidance (DTG) evaluates the unconditional branch at a cleaner diffusion timestep, providing a lookahead prior that preserves geometry while suppressing replication of warped content. This temporal bias is annealed throughout sampling, allowing the model to transition from structure correction to detail refinement without retraining. Combined with any off-the-shelf restoration module in a plug-and-play manner, our approach improves perceptual coherence and restores plausible structure in AIgenerated and real-world videos alike. To facilitate evaluation, we curate GenWarp480, a benchmark of 4,400 distorted 480p videos synthesized from diverse text-to-video models. GenWarp480 focuses on characteristic generative degradations such as warped faces, body misalignments, and spatial artifacts, providing a purpose-built testbed for assessing robustness to generative errors. Extensive experiments demonstrate that our method achieves significant improvements in structural fidelity and temporal stability without any model training.

---


### 10. [Mitigating Content Shift and Hallucination in GenAI Image Editing via Structural Refinement](https://arxiv.org/abs/2605.30437)

**<font color=#1a73e8>作者：</font>** Luxi Zhao, Michael S. Brown  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative AI (GenAI) image editors, such as Nano Banana, produce visually compelling results for retouching tasks, enabling non-experts to edit images through text prompts alone. However, the generative nature of these models often introduces spatial misalignment, texture distortion, and content hallucination, all of which are detrimental to downstream workflows that require pixel-level fidelity. We identify a problem setting we call "structure-preserving GenAI fusion" for black-box GenAI image retouching: retain the perceptual enhancements of a GenAI output while enforcing structural faithfulness to the original input image. To address this problem, we propose a post-processing framework that fuses an input image with its GenAI-enhanced counterpart by first establishing coarse spatial and photometric correspondences, then performing a fusion stage that transfers desired enhancements while suppressing hallucinated content. In the absence of direct prior work in this setting, we evaluate our framework against representative methods from photorealistic style transfer and image fusion. Our experiments demonstrate that our method better preserves aesthetic quality while maintaining pixel-level structural consistency and the input resolution.

---


### 11. [Cross-Lingual Steering for Figurative Language Generation](https://arxiv.org/abs/2605.30443)

**<font color=#1a73e8>作者：</font>** Linfeng Liu, Tiffany Zhan, Louie Hong Yao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual large language models can generate figurative language, but whether the internal signals driving this behavior are language-specific or reusable across languages is unclear. Using activation steering as a probe, we estimate a direction for a figurative category from figurative--literal activation differences in one language and apply it during generation. Across five figurative categories, six languages, and four multilingual LLMs, these directions steer reliably within their own language, most robustly for metaphor and simile. More importantly, they transfer across languages: a direction learned in one increases the target behavior when applied to another, with German among the most receptive targets. Going further, directions assembled from other languages can match or even surpass a target language's own native direction, while removing this shared component weakens native steering. Together, these results provide direct evidence of a reusable but target-dependent cross-lingual signal for figurative generation.

---


### 12. [Dex2HOI: Dexterous Bimanual Two-Object Interaction Generation](https://arxiv.org/abs/2605.30444)

**<font color=#1a73e8>作者：</font>** Chrysa Pratikaki, Pablo Ruiz-Ponce, Jiankang Deng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in 4D Human-Object Interaction (HOI) generation have enabled increasingly realistic motion synthesis, particularly for single-object manipulation. Yet current research overlooks an inherent property of human behavior: people naturally coordinate both hands and manipulate multiple objects simultaneously. To address this gap, we present Dex2HOI, a unified diffusion model for single- and two-object HOI synthesis from text. At its core, Dex2HOI employs a Dual-Stream Diffusion approach, where each object is processed in a dedicated interaction stream and coordinated through bidirectional cross-attention. To synthesize the final motion, we introduce a Motion Fusion Network integrated with novel hand-relative object representations and contact-aware conditioning applied across the whole sequence. By sampling the diffusion process autoregressively over prefix-conditioned windows, Dex2HOI generates arbitrarily long sequences at real-time speed omitting redundant test-time optimization, achieving up to x540 inference speed-up over prior state-of-the-art methods. Extensive evaluation on both single- and two-object benchmarks demonstrates state-of-the-art quantitative results, marking a step beyond conventional single-object HOI generation and toward expressive multi-object manipulation. Code and models will be released upon acceptance.

---


### 13. [Calibrated Preference Learning: The Case of Label Ranking](https://arxiv.org/abs/2605.30447)

**<font color=#1a73e8>作者：</font>** Santo M. A. R. Thies, Viktor Bengs, Timo Kaufmann 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Calibration, the alignment of predicted probabilities with true outcome frequencies, is essential for reliable decision-making. While extensively studied for classification and regression, calibration has not been formally addressed for probabilistic label ranking, where the goal is to predict a distribution over orderings of a label set. Naively treating rankings as classes ignores their structure and fails to capture important modalities such as pairwise and top-k predictions. We formalize calibration for label ranking and develop a hierarchy of notions covering full rankings, sub-rankings, and top-k rankings. We prove that full-rank calibration implies the others but not conversely, and sub-ranking and top-k calibration are incomparable. Empirically, we find popular label ranking models are often poorly calibrated, with substantial differences between sub-ranking and top-k metrics. Applying our framework to RLHF reward models, we find that calibration correlates strongly but not perfectly with benchmark accuracy, suggesting it captures a meaningful quality dimension beyond top-1 accuracy. These findings motivate future work on understanding the downstream effects of miscalibration and developing methods to correct it.

---


### 14. [VeriGate: Verifier-Gated Step-Level Supervision for GRPO](https://arxiv.org/abs/2605.30451)

**<font color=#1a73e8>作者：</font>** Aakriti Agrawal, Minghui Liu, Furong Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization (GRPO) is an effective recipe for training reasoning models with verifier-based outcome rewards, but its supervision is sparse: when all sampled trajectories for a prompt receive the same verifier reward, the group-relative advantage collapses to zero and learning stalls. Outcome-only rewards also provide no step-level credit assignment, limiting exploration and making it harder to learn robust reasoning. We present VeriGate (Verifier-Gated Step-Level GRPO), a verifier-gated extension of GRPO that addresses these limitations with three design choices. First, VeriGate keeps the verifier in charge whenever verifier rewards induce a meaningful preference among sampled trajectories, and uses process supervision only when verifier rewards are degenerate. Second, instead of collapsing Process Reward Model (PRM) step scores into a single trajectory reward, VeriGate converts them into future-cumulated rewards to assign continuation-aware credit. Third, VeriGate transforms these rewards into group-normalized token-level advantages, restoring informative gradients and fine-grained credit assignment while remaining less susceptible to reward hacking than methods that optimize aggregated PRM scores. Empirically, training on MATH with 1.5B and 7B Qwen2.5-Instruct models and evaluating on six reasoning benchmarks, VeriGate improves average accuracy by about 20% and 12% for 1.5B and 7B models respectively, substantially reduces zero-gradient failures, decreases reward-hacking behavior, and improves reasoning quality relative to outcome-only GRPO and PRM-as-outcome baselines.

---


### 15. [A Unified Framework for Gradient Aggregation in Multi-Objective Optimization](https://arxiv.org/abs/2605.30452)

**<font color=#1a73e8>作者：</font>** Zeou Hu, Kelvin Ho, Yaoliang Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many machine learning problems involve multiple inherent trade-offs that are best addressed by gradient-based multi-objective optimization (MOO) algorithms. Existing methods are often proposed with various motivations, analyzed case by case, and differ algorithmically in how the component gradients are aggregated at each step. In this work, we develop a unifying framework for gradient aggregation in MOO, establishing (optimal) rates of convergence to Pareto stationarity, the standard measure of performance in MOO. Central to our analysis is a sufficient alignment condition, from which we derive a theorem showing that non-conflicting directions, when chosen within the convex hull of gradients, form a fundamental sufficient condition for convergence. We further show that feasibility can be ensured through projection onto the dual cone, broadening the scope of methods that admit convergence guarantees. In parallel, we present a primal optimization perspective of gradient aggregation that encompasses established algorithms, clarifies their theoretical relationships, and enables the design of new variants. As an illustration, we introduce capped MGDA, derived from a CVaR-based formulation, and demonstrate its robustness in adversarial federated learning. Finally, we validate our theory through experiments on synthetic problems and practical benchmarks.

---


### 16. [DisjunctiveNet: Neural Symbolic Learning via Differentiable Convexified Optimization Layers](https://arxiv.org/abs/2605.30456)

**<font color=#1a73e8>作者：</font>** Shraman Pal, Can Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many learning tasks in science and engineering are characterized by sparse datasets, which limits the effectiveness of purely data-driven approaches. At the same time, these problems are often accompanied by rich domain knowledge derived from physical laws, operational requirements, and expert heuristics. Such knowledge is frequently expressed as rules involving logical propositions and linear inequalities. Existing neuro-symbolic methods typically enforce these rules approximately through soft penalties, assume input-independent rules when designing specialized architectures, or rely on non-differentiable post-processing at inference time to achieve hard constraint satisfaction. While recent advances in differentiable optimization layers enable end-to-end feasibility enforcement within neural networks, extending these approaches to logical or mixed-integer rules remains challenging due to inherent nonconvexity. In this work, we propose a unified end-to-end framework for enforcing hard, input-dependent mixed integer linear constraints within neural networks. Our approach represents rules as disjunctive constraints and applies hierarchical convex relaxations to obtain convex hull formulations. These relaxations yield tractable linear constraints that can be embedded as differentiable optimization layers while enabling exact rule satisfaction. We demonstrate the effectiveness of the proposed framework on real-world datasets, achieving perfect rule satisfaction and strong predictive performance.

---


### 17. [Scalable Constrained Multi-Agent Reinforcement Learning via State Augmentation and Consensus for Separable Dynamics](https://arxiv.org/abs/2605.30461)

**<font color=#1a73e8>作者：</font>** Santiago Amaya-Corredor, Miguel Calvo-Fullana, Anders Jonsson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a distributed approach for constrained Multi-Agent Reinforcement Learning (MARL) that combines state-augmented policy learning with distributed consensus over dual variables. Our method targets systems where agents have separable dynamics but must coordinate to satisfy global resource constraints, a setting in which, as we demonstrate empirically, independent learning fails to produce feasible solutions because agents cannot determine appropriate individual contributions toward collective constraint satisfaction. The key technical contribution is showing that lightweight neighbor-to-neighbor consensus over Lagrange multipliers suffices for globally coordinated constraint enforcement while preserving the scalability of independent training. Each agent learns a single augmented policy offline, conditioned on both its local state and a dual variable encoding constraint feedback. During execution, agents reach agreement on this dual variable through local communication alone. We prove that under mild connectivity assumptions, the consensus error among agents' multipliers is bounded, and show that this translates to a bounded constraint violation that decreases with graph connectivity and the number of consensus rounds. Unlike centralized training with decentralized execution (CTDE) approaches, whose complexity grows at least quadratically with agent count, our method scales linearly in both training and execution. Experiments on smart grid demand response demonstrate that consensus coordination is \emph{essential for feasibility}: without it, agents satisfy grid capacity constraints only by indefinitely postponing demand, a degenerate non-solution. With consensus, agents converge to a shared dual variable and satisfy both grid constraints and demand fulfillment, scaling to thousands of agents while CTDE baselines are limited to dozens.

---


### 18. [idSCD: Identifying Training Datasets through Semantic Correlation Descriptors](https://arxiv.org/abs/2605.30462)

**<font color=#1a73e8>作者：</font>** Andrada Gobeaja, Ionut Hodoroaga, Elena Burceanu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can a dataset be recognized from the spurious correlations it induces during training? We argue that datasets leave dataset-specific traces in a model's learned semantic correlation structure: incidental regularities that are predictive within a dataset, but not causal for the underlying task, can be internalized during training. We use this insight to study dataset-level membership inference, moving beyond existing methods that rely on behavioral or distributional evidence such as confidence scores, losses, margins, generated samples, or query responses. We introduce a white-box semantic fingerprinting approach based on semantic correlation descriptors (SCDs), which capture the semantic correlation structure learned by a model and make it comparable across dataset mixtures. In a controlled leave-one-dataset-out diagnostic, SCDs recover dataset-specific changes and perfectly separate matching from non-matching dataset pairs. We then propose a practical SCD-based membership score that tests whether a target dataset is part of a model's training mixture using only the model's SCD and the target dataset's standalone SCD, without requiring leave-one-dataset-out models. Across three diverse experimental settings, with dataset groups for natural language inference, emotion classification, and medical text classification, we test both the advantages and limitations of SCD-based membership inference with different degrees of semantic separation and keyword support between dataset splits. On average, the classifier based on this score achieves the highest performance and the lowest std, outperforming black-box baselines RMIA, Attack-P, and LiRA, as well as the white-box SIF baseline. These results show that dataset membership can be traced through internal semantic correlations, with the largest relative gain exceeding 60% in ROC-AUC when dataset groups expose distinct semantic particularities.

---


### 19. [Knowledge Graph-Enhanced Zero-Shot Topic Classification: A Multi-Strategy Comparative Study](https://arxiv.org/abs/2605.30465)

**<font color=#1a73e8>作者：</font>** Shahana Akter, Yatharth Vohra, Ankita Shukla 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-label topic classification without labeled training data is a challenging task, specially when documents contain complex relational information. We present a zero-shot multi-label topic classification framework and systematically investigate how per-article knowledge graph augmentation affects its performance. The base framework classifies topics in documents without labeled training data and has four variants: article-only classification, keyword-enhanced classification, and self-consistency decoding variants of both. Then, we augment each base variant with per article knowledge graph. This graph is extracted from the input document through a pipeline similar to KGGen based on subject-predicate-object triples. We test all eight methods, four base and four graph augmented on fifteen LLMs and eight multi-label datasets across different domains. For the base framework, keyword-enhanced classification (AK) is the best performing method, and six out of fifteen LLMs surpass the sentence-encoder baseline. Graph augmentation has positive and negative impacts on small and large models, respectively. This shows that larger models already contain enough relational information from pretraining. Furthermore, the self-consistency decoding variant does not show performance improvements in any experiment while increasing computation costs about fivefold.

---


### 20. [Can Subgraph Explanations Be Weaponized to Steal Graph Neural Networks?](https://arxiv.org/abs/2605.30470)

**<font color=#1a73e8>作者：</font>** Ojas Nimase, Jiate Li, Yue Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Machine Learning as a Service (GMLaaS) platforms increasingly implement explainability interfaces to meet regulatory transparency requirements. However, this transparency creates exploitable vulnerabilities for model extraction attacks. We present the first model extraction attack specifically designed for graph classification under strict black-box constraints where the attacker observes only discrete class labels and binary explanation masks (no probability scores, gradients, or confidence values). Our method (1) uses model explanation outputs to guide Monte Carlo edge sensitivity estimation toward decision boundaries, with Hoeffding concentration guarantees on estimation accuracy and (2) exploits explanation subgraphs to efficiently narrow the boundary search space. Extensive experiments on benchmark graph datasets across multiple domains demonstrate our method's superiority over comparable baselines. These findings demonstrate that such explainability interfaces create exploitable attack surfaces, informing both defensive mechanisms and policy frameworks for explainable AI mandates. The implementation code is provided in this https URL.

---


### 21. [Universal Multiclass Transductive Online Learning](https://arxiv.org/abs/2605.30479)

**<font color=#1a73e8>作者：</font>** Steve Hanneke, Hongao Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider the problem of universal transductive online classification with a possibly unbounded label space. This setting considers online learning, with the sequence of instances (without labels) known to the learner in advance. We say a concept class $\mathcal{H}$ is learnable if there is a learning algorithm $\mathcal{A}$, such that for every realizable sequence, the number of mistakes made by $\mathcal{A}$ grows at most sublinearly with the number of predictions. We characterize the learnability of this setting and show that there are only two possible optimal rates for the learnable classes: either bounded or increasing logarithmically. We introduce a new combinatorial structure, called ``Level-Constrained-Littlestone-Littlestone (LCLL) tree'', which, along with the indifference property, characterizes the learnability. We also extend the learnability result to the agnostic case and the case where only the stochastic process that generates the instance sequence is known.

---


### 22. [Discovering a Zeta Map Algorithm on Dyck Paths via Mechanistic Interpretability](https://arxiv.org/abs/2605.30482)

**<font color=#1a73e8>作者：</font>** Xiaoyu Huang, Blake Jackson, Kyu-Hwan Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning is increasingly used in mathematical discovery, but in mathematics the desired output is often not a prediction itself, but an explicit construction that can be checked independently. We study this setting through the zeta map on Dyck paths, a classical bijection in the combinatorics of the q,t-Catalan numbers. We train a deliberately small one-layer, one-head encoder-decoder transformer on this map and analyze its learned computation using mechanistic interpretability tools, including decoder cross-attention analysis, linear probing, and causal intervention. The analysis reveals a level-based mechanism: encoder representations make path levels linearly accessible, while the decoder selects and traverses input positions in a structured way. Translating these signals into combinatorics leads to the scaffolding map, an explicit peak-centered traversal algorithm for Dyck paths. We prove that this algorithm agrees with the zeta map, modulo a reversal convention in the labeling. This gives a controlled example of AI-assisted mathematical discovery in which mechanistic interpretability turns model behavior into a precise, human-verifiable combinatorial algorithm.

---


### 23. [Graph-Conditioned Mixture of Graph Neural Network Experts for Traffic Forecasting](https://arxiv.org/abs/2605.30486)

**<font color=#1a73e8>作者：</font>** Amirhossein Ghaffari, Saeid Sheikhi, Ekaterina Gilman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatio-temporal forecasting on sensor graphs is commonly tackled with a single backbone architecture applied uniformly across all nodes, although graph regions can exhibit different dynamics. Road segments differ in functional class, structure, and traffic behavior, suggesting that node-wise expert specialization can be useful. We propose GC-MoE, a graph-conditioned mixture of experts framework that assigns each node a personalized combination of frozen forecasting experts based on graph topology and the recent traffic input window. GC-MoE combines frozen pretrained spatio-temporal GNN experts with an input-aware, spatially contextualized router while training only a lightweight routing module. We also study a bounded graph-conditioned output refinement layer as an optional extension and include node-adaptive ST-LoRA adapters only as an ablation diagnostic. Across four standard benchmarks (PEMS04, PEMS07, METR-LA, and PEMS-BAY), GC-MoE improves MAE over a zero-parameter ensemble baseline, with competitive RMSE and MAPE, while training only ~17K parameters on top of 1.5M frozen expert weights. The implementation is available at this https URL.

---


### 24. [A Novel Global Context-aware Deep Neural Network for Enhanced Brain Tumor Segmentation using Magnetic Resonance Images](https://arxiv.org/abs/2605.30510)

**<font color=#1a73e8>作者：</font>** Sourjya Mukherjee, Ananya Bhattacharjee, R. Murugan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Brain cancer's severity necessitates precise brain tumor segmentation, which is crucial for effective brain tumor diagnosis. Manual identification, burdened by high costs, labor, and error risks, highlights the need for automated methods. In this study, we introduce the Global Context-aware Squeeze and Excite Residual UNet (GCSER-UNet), which facilitates a fusion of spatial and channel-wise attention and thus enhances the model's capacity to capture intricate spatial dependencies and contextual information. GCSER-UNet efficiently extracts tumor segments from multimodal MRI slices, delivering exceptional performance. Evaluations on benchmark databases exhibit its superiority, achieving a notable 94 percent dice score on the TCGA LGG dataset, surpassing the state-of-the-art dice score of 91.8 percent. In the BraTS 2020 dataset, the proposed GCSER-UNet ensemble approach yielded dice scores of 95 percent, 92 percent, and 90 percent for the tumor regions - Whole Tumor (W), Tumor Core (T), and Enhancing Tumor (E), respectively. The current state-of-the-art dice scores were 94 percent, 93 percent, and 88 percent. These compelling outcomes highlight the efficacy of GCSER-UNet in precise brain tumor segmentation and thus can aid neurologists in effective brain cancer management and treatment planning.

---


### 25. [MAAT: Multi-phase Adapter-Aware Targeted Unlearning](https://arxiv.org/abs/2605.30514)

**<font color=#1a73e8>作者：</font>** Suryash Yagnik, Shubham Gaur, Saksham Thakur 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine unlearning evaluation is structurally skewed: Why-type questions, which probe causal and relational knowledge, comprise less than 0.06% of CounterFact, 0.6% of ZSRE, and less than 1.3% of TOFU, MUSE, and WMDP-Cyber. This near-zero representation means that methods that fail on causal knowledge can score highly in aggregate, and this failure is undetectable without balanced evaluation. We present 5WBENCH, a balanced 5,000-sample benchmark with 1,000 examples per 5W category (Who, What, When, Where, Why), making causal unlearning failures quantifiable for the first time. Using 5WBENCH, we show that no existing baseline simultaneously achieves high forgetting and high retention on Why-type questions: aggressive forgetting degrades retained knowledge, while conservative methods fail to forget causal facts. Why-type difficulty stems from multi-hop reasoning chains (44% of Why entries vs. less than or equal to 2% for others) and gradient dilution over 40.1-token answer spans. We present MAAT (Multi-phase Adapter-Aware Targeted Unlearning), a three-phase framework operating on LoRA adapter weights, combining gradient-projected ascent, SVD rank-dimension pruning, task vector negation, and hybrid KL-hidden-state retain repair. MAAT is the first method to simultaneously achieve high forgetting and high retention on Why-type causal knowledge, reaching a new operating point on the forget-retain Pareto frontier. We make our code publicly available.

---


### 26. [OmniMem: Scalable and Adaptive Memory Retrieval for Long Video Generation](https://arxiv.org/abs/2605.30519)

**<font color=#1a73e8>作者：</font>** Lin Zhao, Yushu Wu, Yifan Gong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive (AR) video generation extends videos by producing latent chunks sequentially, but scaling to long videos requires repeated access to a growing historical KV cache. Existing methods reduce this cost by truncating the KV cache or compressing it into implicit memory, but both lose explicit access to query-relevant historical details. We propose OmniMem, an explicit full-range memory retrieval framework that performs sparse KV retrieval over the historical cache. To make this practical for chunk-based AR video generation, OmniMem addresses two issues: (i) local bias in sparse KV selection and (ii) Union Explosion in memory access. Adaptive Window Exclusion removes local-window blocks from the selection candidates when sufficient long-range history is available, preserving the sparse budget for informative long-range retrieval. Query-Shared KV Selection reduces cross-query diversity, while Per-Head Scattered KV Access avoids expanding head-specific selections into a large selected KV buffer. This allows each attention head to retrieve non-contiguous KV blocks according to its own selection pattern. Experiments on long-video generation show that OmniMem improves Dynamic Degree by 52.3% and preserves strong consistency over strong baselines, while maintaining comparable memory usage.

---


### 27. [Revisiting Padded Transformer Expressivity: Which Architectural Choices Matter and Which Don't](https://arxiv.org/abs/2605.30523)

**<font color=#1a73e8>作者：</font>** Anej Svete, William Merrill, Ryan Cotterell 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work describes what transformers can and cannot compute through connections to boolean circuits, but existing results lack exact characterizations and are sensitive to modeling choices. Padded transformers -- to whose input filler symbols such as ``...'' are appended -- emerge as a useful gadget for establishing equivalences to circuit classes by providing polynomial space for adaptive parallel computation. However, only a limited set of padded transformer idealizations has been studied, leaving open how robustly these equivalences hold under changes to attention type, model width, and uniformity. We find that, under practical assumptions, padded transformers are surprisingly robust to all of these, and identify numeric precision and model depth as the main factors affecting expressivity. Concretely, we prove that polynomially padded $\text{L-uniform}$ constant-precision transformers are equivalent to $\text{L-uniform AC}^0$, while growing-precision ones achieve $\text{L-uniform TC}^0$ regardless of width. Furthermore, looping enables sequential processing analogous to circuits: $\log^d N$-looped constant-precision transformers reach $\text{FO-uniform AC}^d$, and growing-precision ones reach $\text{FO-uniform TC}^d$. Interestingly, growing width or precision beyond logarithmic does not increase expressivity, and all our results hold for both softmax and average hard attention transformers.

---


### 28. [Generalistic or Specific Embeddings, Which is Better? An Empirical Study on Search for Clinical Coding in Non-English Languages](https://arxiv.org/abs/2605.30529)

**<font color=#1a73e8>作者：</font>** David Rey-Blanco, Roberto Cruz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sentence-embedding models for semantic search are overwhelmingly developed and evaluated on English corpora. When applied to clinical retrieval in other languages -- particularly retrieval of ICD-10-CM / CIE-10 codes -- recall degrades in ways often masked by aggregate benchmarks. We study whether large generative language models can serve as data factories to close this gap. We build a two-stage retriever (bi-encoder followed by cross-encoder reranker), fine-tuned from a Spanish biomedical encoder (PlanTL-GOB-ES/bsc-bio-ehr-es) on Gemini-generated synthetic data covering English, Spanish, Catalan, Italian, Portuguese and French, and evaluate against BioBERT-ST and the un-tuned Spanish encoder. The bi-encoder alone matches BioBERT-ST on MRR (0.876 vs. 0.866) and overtakes it on R@3 (0.650 vs. 0.626) and R@5 (0.804 vs. 0.790) without English biomedical pretraining. Adding a cross-encoder reranker lifts aggregate R@5 to 0.822 and dominates on four of five languages (+0.017 Spanish, +0.033 Catalan, +0.018 French, +0.037 Portuguese) at the cost of a small English regression. The trade-off is clinically acceptable: Portuguese reaches R@5 = 0.829 vs. BioBERT-ST's 0.714. Contributions: an open recipe for building domain-specific medical retrievers from LLM-generated data; quantification of the learning gain (MRR 0.755 to 0.876, +15.9% with ~19,500 synthetic pairs); and a characterisation of where gains concentrate by language and rank.

---


### 29. [DisasterLex: An Expert Concept-to-Schema Knowledge Graph for Geospatial Reasoning in Disaster Analytics](https://arxiv.org/abs/2605.30538)

**<font color=#1a73e8>作者：</font>** Yiming Xiao, Ankit Basu, Kai Yin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Disasters are inevitable and increasingly costly, and effective response depends on querying structured tabular data: precise, information-dense records of hazard, exposure, vulnerability, and lifeline infrastructure that underpin disaster management. Current text-to-SQL methods enable natural-language access to such tables but transfer poorly to the disaster domain, where queries span heterogeneous geospatial schemas and require reasoning over causal relations. We introduce DisasterLex, a knowledge-graph-mediated framework that inserts an Expert Knowledge Graph (EKG) of curated concepts and typed causal edges between the user query and the database, bridged to schema by concept-to-table links. The orchestration runs four stages (identifying query entities, routing to the operational domain, planning over causal edges, and grounding the SQL), restricting the schema passed to the model at each step. We instantiate it on a disaster-analytics database (36 geospatial tables, 150 columns) with an EKG of 107 concepts, 117 causal edges, and 52 concept-to-schema links, evaluated on a 75-query test set. On all seven base models spanning proprietary and open-weight families, DisasterLex beats four state-of-the-art baselines (LightRAG, HippoRAG 2, ReFoRCE, CHESS) by 1.4x to 2.75x, with absolute scores of 1.65 to 3.56 (of 5.0). Error analysis shows baseline failures cluster in routing and multi-table SQL composition, the operations our orchestration explicitly addresses. Code, data, and the EKG artifact are available at this https URL and on Zenodo at this https URL.

---


### 30. [SubsurfaceGen: Procedural Generation of Field-Scale Earth Models and Seismic Data](https://arxiv.org/abs/2605.30541)

**<font color=#1a73e8>作者：</font>** Joseph Stitt, Pratik Rathore, Madeleine Udell 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Full waveform inversion (FWI) is the gold standard for subsurface imaging, with applications from carbon sequestration to energy and mineral exploration to earthquake hazard assessment. Machine learning approaches to FWI need field-scale, geologically diverse, and physically realistic training data, but existing resources such as Marmousi, SEAM, and OpenFWI fall short on spatial extent, temporal extent, geological diversity, and physical realism. We address these limitations with SubsurfaceGen, a GPU-accelerated generator for 3D velocity models and seismic data. Along with SubsurfaceGen, we release a paired dataset of 4,276 2D velocity slices, 5 s wavefields, and 8 s shot gathers drawn from 42 realistic, field-scale 3D velocity models, each spanning 10 km x 10 km laterally and 6.19 km deep at 10 m resolution. The dataset spans six geological settings -- four built with SubsurfaceGen and two drawn from prior sources -- relevant for carbon sequestration and hydrocarbon exploration. We use this dataset to evaluate neural operators on wavefield prediction and encoder-decoders on end-to-end velocity inversion, holding out one geological setting for out-of-distribution testing. These experiments surface failure modes at field-scale and demonstrate how SubsurfaceGen and the associated dataset can impact ML-based FWI.

---


### 31. [On-Device Generative AI for GDPR-Compliant Visual Monitoring: Natural Language Alerts from Local Object Detection](https://arxiv.org/abs/2605.30544)

**<font color=#1a73e8>作者：</font>** Gudrun Schappacher-Tilp, Nicoletta Kaehling, Jan Kornberger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual monitoring systems that rely on cloud-based AI inference expose raw image data to external services, creating fundamental tensions with the data-minimisation principle of the General Data Protection Regulation (GDPR). This paper presents a proof-of-concept privacy-by-design pipeline that resolves this tension by confining all inference entirely to the edge device. A YOLOv5n-seg model compiled for a Hailo-8L AI accelerator delivers real-time object detection on a Raspberry Pi 5, from which raw pixel buffers are immediately discarded after inference. A stateful trigger engine forwards minimal JSON event payloads to a locally hosted instance of Phi-3 Mini (3.8B parameters, Q4_0 quantisation), which synthesises one-to-two sentence natural-language alerts for a human operator. No image data crosses the network boundary at any point; only the generated text alert is transmitted. We describe the full system architecture and implementation, report measured inference latency and resource utilisation on the target hardware, and present representative generated alerts. The results demonstrate that combining a dedicated neural-network accelerator with an on-device large language model on a single-board computer is not only feasible but produces practically deployable, human-readable monitoring output while aligning with GDPR Art. 5(1)(c) by design.

---


### 32. [Refining Word-Based Grammatical Error Annotation for L2 Korean](https://arxiv.org/abs/2605.30545)

**<font color=#1a73e8>作者：</font>** Jungyeul Park, Kyungtae Lim, Wonjun Oh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Korean grammatical error correction (K-GEC) presents a structural mismatch between word-based evaluation and the morpheme-level locus of many learner errors. Postpositions and verbal endings are bound to lexical hosts, but they encode grammatical relations that must be represented in correction and evaluation. This paper refines word-based grammatical error annotation for L2 Korean by addressing three connected problems in existing resources: surface target realization, Korean-specific edit annotation, and single-reference evaluation. We reconstruct target sentences from the National Institute of Korean Language (NIKL) L2 corpus under morphologically constrained realization rules and convert its morpheme-level annotations into word-level \texttt{m2} edits. We then define a Korean ERRANT-style annotation scheme that preserves the MRU core while distinguishing functional morpheme errors, spelling errors, word boundary errors, and word order errors. We also augment the KoLLA corpus with an additional reference correction, yielding a multi-reference evaluation setting for Korean GEC. Empirical validation shows that the refined NIKL targets yield lower perplexity, the converted \texttt{m2} files achieve higher agreement with source-target edit representations, and the refined resources improve KoBART-based correction under the same model setting. Multi-reference KoLLA evaluation further reduces the penalty imposed on valid corrections that diverge from a single reference, especially for neural and prompted GEC systems. These results show that Korean GEC evaluation depends not only on correction models, but also on reference data and edit annotations that reflect Korean morphology, spacing, and correction variability.

---


### 33. [MATraM: A Multi-Activity Transport and Mobility Agent-Based Model for Activity Modifications](https://arxiv.org/abs/2605.30547)

**<font color=#1a73e8>作者：</font>** Yahya Gamal, Ricardo Colasanti, Gary Polhill 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> This paper introduces the Multi-Activity Transport & Mobility (MATraM) Agent-Based Model (ABM), a novel framework designed to advance activity-based transport modelling by incorporating dynamic activity adaptation. Traditional transport models simulate system performance using varying levels of abstraction, including flow-based, queue-based, and interaction-based mobility representations. While these approaches differ in their treatment of movement and congestion, they typically rely on pre-defined trip patterns that limit responsiveness to changing conditions. In particular, conventional activity-based models generate trips from fixed daily schedules, constraining their ability to capture behavioural flexibility and uncertainty. MATraM addresses this limitation by enabling agents to flag activities modification requests in response to sub-optimal travel conditions, such as increased travel times. By coupling with an activity scheduling and modification framework, the model integrates adaptive decision-making into the generation and execution of daily activity schedules. This allows for a more realistic representation of how individuals adjust their behaviour in response to transport system dynamics, leading to emergent mobility and congestion patterns. The ABM is presented following the ODD protocol, outlining its purpose, structure, and implementation. MATraM includes detailed representations of agents, their activity schedules, and the transport network, alongside submodels governing routing, scheduling, and behavioural adaptation. By bridging activity-based modelling with interaction-based mobility simulation, MATraM provides a flexible and extensible platform for exploring transport dynamics under uncertainty. This work contributes to the development of next-generation transport models capable of capturing the complex interplay between individual behaviour and system-level outcomes.

---


### 34. [Early Prediction of Future Behavioral Strategy from Process Traces](https://arxiv.org/abs/2605.30550)

**<font color=#1a73e8>作者：</font>** Robert Kasumba, Dennis Barbour, Chien-Ju Ho  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive systems often need to make task-specific decisions about people from limited evidence: a tutor may need to anticipate how a learner will approach a new problem, a game may need to adapt when a player enters a new level, and a human-AI system may need to infer whether a partner will persist with a plan or switch goals. These decisions depend on person-level tendencies that shape how people solve related tasks, but such tendencies are difficult to infer from standard behavioral evidence. One approach is to use aggregate outcome summaries, such as scores, completion rates, or productivity; these summaries are compact and available across tasks, but can collapse distinct behavioral processes into similar outcomes. Another approach is to use process-level traces, which record how behavior unfolds; however, process modeling within one task can entangle stable person-level tendencies with task-specific layout and affordances. In this work, we study early cross-task behavioral inference: whether partial source-task process traces can reveal transferable person-level structure that predicts strategy in a held-out target task. We introduce a Process-Level Latent Variable Model (PLVM), which encodes task-specific traces and fuses them into a shared person-level latent representation for cross-task prediction. In PowerWash Simulator, a naturalistic telemetry dataset of human gameplay, PLVM uses partial traces from two cleaning tasks to predict locally persistent Zone Planner behavior versus frequent Zone Hopper behavior in the held-out Fire Station level. Controlled simulations with known latent types show that cross-task fusion helps when source tasks reveal complementary dimensions of a shared latent process. These results suggest that process-level cross-task modeling can support early prediction of target-task strategy when observing sufficient target-task behavior is impractical.

---


### 35. [Destruction is a General Strategy to Learn Generation; Diffusion's Strength is to Take it Seriously; Exploration is the Future](https://arxiv.org/abs/2605.30553)

**<font color=#1a73e8>作者：</font>** Pierre-André Noël  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> I present diffusion models as part of a family of machine learning techniques that withhold information from a model's input and train it to guess the withheld information. I argue that diffusion's destroying approach to withholding is more flexible than typical hand-crafted information withholding techniques, providing a rich training playground that could be advantageous in some settings, notably data-scarce ones. I then address subtle issues that may arise when porting reinforcement learning techniques to the diffusion context, and wonder how such exploration problems could be addressed in more diffusion-native ways. I do not have definitive answers, but I do point my fingers in directions I deem interesting. A tutorial follows this thesis, expanding on the destroy-then-generate perspective. A novel kind of probabilistic graphical models is introduced to facilitate the tutorial's exposition.

---


### 36. [Seeing Isn't Knowing: Do VLMs Know When Not to Answer Spatial Questions (and Why)?](https://arxiv.org/abs/2605.30557)

**<font color=#1a73e8>作者：</font>** Yue Zhang, Zun Wang, Han Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial reasoning is a fundamental capability for vision-language models (VLMs) deployed in real-world environments. However, visual observations are inherently limited representations of a 3D world: occlusion can render objects invisible, and perspective can make geometric properties misleading. Despite this, existing spatial reasoning benchmarks typically assume that observations are sufficient and reliable, focusing on whether models produce correct answers rather than whether they recognize when a question cannot be answered and what additional observations would be needed. In this work, we challenge this assumption by constructing a controlled evaluation framework, SpatialUncertain, and introducing two types of observation challenges: (1) occlusion, which hides target information, and (2) perspective ambiguity, which produces misleading visual cues. For each configuration, we design spatial questions that are answerable under clean observations but require abstention under the introduced challenges. We further evaluate whether models can identify which additional viewpoints would resolve perspective ambiguity. Our results across a diverse set of frontier open- and closed-source VLMs reveal two consistent failure modes. First, models are prone to overconfident answering, attempting to solve spatial reasoning tasks even when visual evidence is incomplete or misleading, with average accuracy around 30\% under occlusion and below 10\% under perspective ambiguity. Second, even when additional views are available, some models perform near random chance in identifying which would provide reliable evidence. Together, our findings call for moving beyond answer correctness toward evaluating whether models know when to abstain and how to seek reliable evidence.

---


### 37. [Transforming and Encoding FTS for SAT Solving: What Helps, What Hurts (Extended Version)](https://arxiv.org/abs/2605.30563)

**<font color=#1a73e8>作者：</font>** João Filipe, Álvaro Torralba, Gregor Behnke  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Factored tasks are a classical planning representation that extends SAS+ with limited forms of disjunctive preconditions, conditional effects, and angelic nondeterminism. This allows for a more compact representation of tasks than traditional formalisms such as STRIPS or SAS+, and supports a wide range of task transformations. However, existing planning approaches for factored tasks have been limited to heuristic search methods.
In this work, we investigate how to encode factored tasks in SAT. We propose several ways to encode the tasks, focusing on different strategies for translating the factored transition relation into propositional logic. We also analyze how to exploit parallelism at various levels in this setting and study the impact of common task transformations on the performance of SAT-based planners.

---


### 38. [Procedural Generation of First Person Shooter Maps using Map-Elites](https://arxiv.org/abs/2605.30570)

**<font color=#1a73e8>作者：</font>** Simone de Donato, Pier Luca Lanzi, Daniele Loiacono  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We investigate the application of MAP-Elites (a well-known quality diversity algorithm) to design levels for First-Person Shooter (FPS) games. We consider two well-known map representations (All-Black and Grid-Graph) and introduce two novel representations (Point-Line and Spatial-Layout) that improve the characterization of FPS maps. We define a series of metrics to describe maps' topological properties (which solely depend on maps' layout), and emergent properties (which must be evaluated through actual gameplay). We perform an in-depth analysis to identify the most suitable features to guide MAP-Elites illumination process. We apply MAP-Elites with Sliding Boundaries (MESB) to evolve populations of FPS maps. Our results show that the new representations can generate maps with higher diversity and quality than the representations previously used for evolving FPS maps.

---


### 39. [Zeroth-Order Non-Log-Concave Sampling with Variance Reduction and Applications to Inverse Problems](https://arxiv.org/abs/2605.30573)

**<font color=#1a73e8>作者：</font>** M. Berk Sahin, Behzad Sharif, Abolfazl Hashemi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sampling from high-dimensional, non-log-concave distributions with unnormalized densities remains a fundamental challenge in machine learning, particularly in black-box settings where gradient information is inaccessible or computationally prohibitive. While Langevin dynamics provides a principled framework for sampling when gradients are accessible, its extension to the black-box settings suffers from high variance and lacks non-asymptotic convergence guarantees for non-log-concave sampling. To address these limitations, we propose a variance-reduced zeroth-order Langevin sampling method. Our method employs a gradient estimator that substantially reduces the variance of the classical batched zeroth-order estimator and eliminates the unfavorable dimensional dependence of the batch size required for accurate estimation, enabling practical and stable sampling. We establish the first non-asymptotic convergence guarantees for zeroth-order non-log-concave sampling in terms of $\varepsilon$-relative Fisher information, and, under a Poincaré inequality assumption, squared total variation distance. We further propose ZO-APMC, a posterior sampling algorithm for black-box inverse problems with pre-trained score-based generative priors, establishing the first non-asymptotic convergence guarantees for such methods. We validate our theory through synthetic experiments and demonstrate strong empirical performance on practical linear and nonlinear inverse problems.

---


### 40. [Probing the Prompt KV Cache: Where It Becomes Dispensable](https://arxiv.org/abs/2605.30574)

**<font color=#1a73e8>作者：</font>** Vinayshekhar Bannihatti Kumar, Manoj Ghuhan Arivazhagan, Disha Makhija 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prior KV cache compression schemes empirically demonstrate that the prompt cache is partially redundant during decoding, dropping or summarising entries with little accuracy loss. We ask when and what kind of redundancy: at which layers, after how many decoding steps, and in what form can the prompt span KV cache be replaced without breaking the task. A controlled splice intervention swept over layer cutoff and decoding steps shows this redundancy is about form (chat template scaffolding) rather than content. Replacing the upper layer prompt span KV cache with KV cache from a chat template scaffold whose user content is a neutral filler recovers near clean accuracy, while zeroing the same slots collapses accuracy. The dissociation replicates across the Qwen3, Gemma 3, and Llama 3 families on multiple datasets.

---


### 41. [Uncertainty-Aware and Temporally Regulated Expert Advice in Reinforcement Learning for Autonomous Driving](https://arxiv.org/abs/2605.30576)

**<font color=#1a73e8>作者：</font>** Ahmed Abouelazm, Felix Klingebiel, Philip Schörner 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Exploration in reinforcement learning for autonomous driving is inherently unsafe: agents must experience novel behaviors to learn, yet exploration can lead to collisions or off-road driving. We propose an uncertainty-aware framework that leverages expert advice to guide exploration while avoiding long-term dependence. Advice is triggered when epistemic or aleatoric uncertainty exceeds adaptive thresholds derived from rolling buffers, ensuring advice evolves with the agent's confidence. A commitment-cooldown strategy with a stochastic early-stop heuristic regulates the duration and frequency of guidance, exposing the agent to coherent maneuvers without exhausting the advice budget. Expert and agent experiences are combined in a shared replay buffer within an off-policy implicit quantile network (IQN) backbone, enabling efficient reuse of expert trajectories. Experiments in CARLA show that our method outperforms the IQN baseline, improving success by 5-7% and reducing failures, demonstrating that risk-sensitive uncertainty coupled with regulated expert integration enables safer and more efficient exploration for sensor-based RL policy learning in unsignalized intersection navigation.

---


### 42. [AdvScene: Rethinking Adversarial Patch Evaluation Through Scene Robustness](https://arxiv.org/abs/2605.30578)

**<font color=#1a73e8>作者：</font>** Xiaoyong, Yuan, Zhang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Adversarial patches are physical patterns attached to real objects to mislead AI vision systems. Their real-world risk is not determined by a single successful prediction, but by whether they remain effective after deployment under changing viewpoints, distances, and scene conditions. We refer to this property as scene robustness, the effectiveness of a deployed patch across conditions in a real environment. Yet existing evaluations do not measure scene robustness well: real image benchmarks are realistic but fixed, while simulators are controllable but not grounded in a specific real scene.
We present AdvScene, a scene-grounded framework for measuring the scene robustness of adversarial patches in reconstructed real environments. AdvScene reframes evaluation as operational measurement: given a fixed deployed patch, it characterizes the patch's operational envelope - where and when the attack succeeds - as a function of viewpoint, distance, and scene context. A key challenge is that the attack is typically defined only in a single anchor view, while evaluation requires a representation that remains faithful under viewpoint changes. We formalize this as a constrained lifting problem and introduce Adversarial Patch-to-Scene Embedding (APSE), which resolves cross-view ambiguity while preserving attack-critical appearance and enforcing locality, target-surface attachment, and cross-view consistency. We validate AdvScene using real-world physical data and conduct a comprehensive evaluation of existing adversarial patches. Our results show that AdvScene reveals substantial scene-dependent variation in attack effectiveness that is not captured by existing image-centric or simulator-based evaluations.

---


### 43. [Speculative Decoding Across Languages](https://arxiv.org/abs/2605.30580)

**<font color=#1a73e8>作者：</font>** Nirajan Paudel, Michael Ginn, Luc De Nardi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding has become a crucial component of large language model (LLM) inference, enabling faster generation by drafting multiple tokens and verifying them in parallel. However, small draft models tend to suffer from disproportionately poor multilingual capabilities. Thus, when generating text in a non-English language, speculative decoding is far less effective.
We compare three strategies to improve speculative decoding efficiency for eleven languages: finetuning the draft model on task-specific data (translation); finetuning the draft model on unlabeled monolingual corpora; and training simple n-gram draft models on the same monolingual corpora. We evaluate efficiency on translation (from English into the target language) and the held-out task of story generation. We find that while task-specific distillation can significantly improve efficiency, distilled models generalize poorly to a new task. Meanwhile, n-gram draft models, despite lower acceptance rates, consistently provide large speed-ups due to much faster draft generation.

---


### 44. [Prior Availability in Industrial Visual Sim-to-Real: A Review of CAD-Guided and CAD-Unavailable Regimes](https://arxiv.org/abs/2605.30581)

**<font color=#1a73e8>作者：</font>** Chenxi Tao, Seung-Kyum Choi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Industrial visual sim-to-real is often described as transferring from synthetic images to real images, but industrial deployment usually involves a broader mismatch between available evidence and required decisions. A system may be built from CAD renderings, simulated RGB-D observations, normal reference images, synthetic defects, pretrained feature spaces, or language prompts, yet deployed under different sensors, lighting, materials, fixtures, calibration, production variation, and rare defect modes. This review reframes industrial visual sim-to-real as a domain-gap problem organized by prior availability. We distinguish CAD-available settings, where explicit object geometry can support rendering, calibration, pose estimation, segmentation, and test-time geometric verification; CAD-unavailable settings, where geometry is replaced by normal-reference appearance, feature distributions, teacher-student residuals, synthetic anomaly assumptions, foundation features, or vision-language priors; and boundary-prior settings, where approximate models, templates, reference views, or semantic correspondences preserve only part of the CAD role. This framing connects CAD-based detection and 6D pose-estimation literature with industrial anomaly and surface-inspection literature that is usually reviewed separately. To make the taxonomy concrete, we use empirical anchors on T-LESS/BOP, MVTec AD, and VisA. The anchors show that CAD render count alone does not close transfer; source-distribution design, detector capacity, and small real calibration can matter more. They also show that CAD at test time creates a distinct verification channel through mask, pose, and depth consistency, whereas CAD-unavailable inspection relies on calibrated normality and feature deviation. The review therefore argues against a single cross-task leaderboard and instead asks what prior grounds the deployment decision.

---


### 45. [AI for Monitoring and Classifying Data Used in Research Literature](https://arxiv.org/abs/2605.30582)

**<font color=#1a73e8>作者：</font>** Rafael Macalaba, Aivin V. Solatorio  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While platforms like Google Scholar and Semantic Scholar track citations for academic papers, no comparable infrastructure exists for monitoring dataset usage in research literature, leaving the landscape of data use largely opaque. Addressing this gap is critical for transparency, reproducibility, and monitoring of impact, yet progress is hindered by inconsistent citation practices, scarce labeled data, and ambiguous references to datasets in the wild. Traditional NLP approaches struggle with these challenges, motivating the shift toward more adaptive, semantically rich models. Building on prior work using LLMs for data mention detection and synthetic data for bootstrapping training, this paper presents an updated methodology for scalable dataset monitoring. We introduce a multitask GLiNER-based framework that jointly performs dataset mention extraction, relation identification, and usage-context classification. To address label scarcity, the pipeline leverages synthetic data generation to produce training examples and LLM-based revalidation to filter incorrect mentions and enforce labeling consistency, together improving reliability, coverage, and output consistency across the training pipeline. This work advances the development of open-source tools for monitoring data use in research literature, contributing to the broader goal of generalizable, unconstrained dataset citation tracking.

---


### 46. [Benchmarking Machine Learning Uncertainty Quantification Methodologies for Predicting Turbine Gas Temperature Degradation](https://arxiv.org/abs/2605.30585)

**<font color=#1a73e8>作者：</font>** Jostein Barry-Straume, Changmin Son, Adrian Sandu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Effective prognostics and health management of modern engines relies on accurate turbine gas temperature predictions and robust uncertainty quantification to ensure reliability and safety. This paper investigates five major approaches for constructing prediction intervals -- namely the Delta method, Bayesian Monte Carlo Dropout, Bootstrap method, Lower-Upper Bound Estimation, and Mean-Variance Estimation -- as a means of capturing the uncertainty in neural network predictions of turbine gas temperature. Each approach is implemented within a unified experimental framework that employs cross-validation for hyperparameter selection, repeated train-test splits for performance robustness, and multiple metrics to evaluate both the accuracy and tightness of the intervals. In particular, Coverage Probability, Normalized Mean Prediction Interval Width, and the Coverage Width-based Criterion are measured to comprehensively assess each method's reliability and sharpness. Experiments conducted on a representative turbine gas temperature dataset reveal distinct trade-offs among the five methods in terms of interval coverage, width, and stability. These findings provide a practical guide for selecting and tuning prediction interval methods in engine health management and prognostics, ensuring both interpretability and precision in real-world applications.

---


### 47. [Learning Transferable Predictability Representations](https://arxiv.org/abs/2605.30592)

**<font color=#1a73e8>作者：</font>** Diyali Goswami, Auroop R. Ganguly  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the problem of assigning a scalar score to a short trajectory window that reflects its position on an ordered continuum of predictability regimes, spanning structured deterministic dynamics to unstructured stochastic noise. Existing methods address deterministic-versus-stochastic discrimination within a single system and do not produce scores with a consistent numerical interpretation across systems. We formalize this as ordinal estimation over a five-level predictability ladder and identify a structural source of cross-system ambiguity: ranking supervision alone leaves the score coordinate unfixed up to a monotone reparameterization, which we term the gauge freedom of ordinal scoring. We propose the Gauge-Fixed Ordinal Network (GON), a temporal convolutional model trained with an anchor-and-variance objective that pins level-wise score means to shared target coordinates. GON operates on 2-jet features that expose local trajectory geometry, preserved by smooth flows and disrupted by stochastic surrogate procedures. On five held-out dynamical systems, initializing from a pretrained GON checkpoint consistently outperforms training from scratch across all window budgets, with adaptation depth reflecting geometric proximity to the training family. Zero-shot scores retain ordinal structure at the stochastic boundary, where surrogate procedures most strongly disrupt nonlinear geometry, and pretrained initialization consistently beats scratch across all window budgets. Pairwise discrimination and globally coherent ordinal scoring are distinct properties requiring a stable score coordinate for cross-system transfer, with direct implications for predictability assessment, model selection, and early-warning diagnostics across natural and engineered dynamical systems.

---


### 48. [Scientific Machine Learning for Engine Health Management and Remaining Useful Life Prediction](https://arxiv.org/abs/2605.30593)

**<font color=#1a73e8>作者：</font>** Jostein Barry-Straume, Changmin Son, Adrian Sandu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Engine Health Management (EHM) depends on reliable forecasting of Remaining Useful Life (RUL) and on tracking thermal indicators such as turbine gas temperature (TGT). In practice, real-world fleet data are heterogeneous and non-stationary, and point predictions alone are insufficient for risk-aware maintenance decisions. This paper presents a multi-task scientific machine learning framework for turbine prognostics that jointly predicts turbine gas temperature untrimmed (TGTU), Delta Turbine Gas Temperature (DTGT), and RUL, with quantified uncertainty in the form of prediction intervals whose empirical coverage is evaluated. A shared sequence encoder (convolutional front-end with residual bidirectional LSTM layers and attention pooling) feeds task-specific heads, including mean--variance estimation for probabilistic regression and, optionally, a survival head for threshold-based event modeling. The framework is designed to be tunable via a small set of practitioner-facing parameters (e.g., DTGT thresholding rules and RUL target construction) so that deployment can align with in-house policies and proprietary criteria. The predictive performance of the proposed framework is evaluated using both point and interval metrics, including mean absolute error (MAE), prediction interval coverage probability (PICP), mean prediction interval width (MPIW), and the coverage--width criterion (CWC). Results are reported both in aggregate and stratified by flight phase and maintenance segment to highlight operational-context effects and to support uncertainty-aware monitoring.

---


### 49. [Improving Relative Representations with Learned Anchors and Whitened Inner Products](https://arxiv.org/abs/2605.30596)

**<font color=#1a73e8>作者：</font>** Oscar Thorsted Svendsen, Nikolaj Holst Jakobsen, Fabian Mager 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Independently trained neural models typically converge to incompatible latent representations, creating a fundamental barrier to highly modular AI systems. While Relative Representations (RR) address this by mapping absolute coordinates to a shared space defined by similarities to common anchor points, traditional implementations rely on randomly sampled anchors and cosine similarity, which frequently fail to capture the anisotropic geometries of modern architectures like Transformers. In this work, we propose a robust framework for cross-model communication based on two improvements. We learn anchors as robust semantic prototypes and utilize a geometry-aware similarity metric which preserves discriminative magnitude information and is invariant to affine shifts. Our approach demonstrates significant gains in performance and consistency across vision and language tasks. Notably, it enables nearly lossless information transfer and stable zero-shot communication even between highly heterogeneous architectures, such as small language models of varying scales.

---


### 50. [ScaleMAP: Preserving Local Density and Neighborhood Structure in Low-Dimensional Embeddings](https://arxiv.org/abs/2605.30597)

**<font color=#1a73e8>作者：</font>** Rajas Poorna, Marcus T. Cicerone  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Nonlinear dimensionality-reduction methods such as UMAP and PaCMAP adaptively normalize local distances during graph construction, erasing neighborhood scale from the data. This distorts more than relative cluster sizes: sparse structures like bridges between transitioning cell types and narrow spectral spikes in hyperspectral images can be suppressed or lost entirely. DensMAP adds a density penalty to correct this, but this penalty competes with UMAP's attraction-repulsion forces, scattering points far from their neighborhoods. ScaleMAP takes a different approach: each pairwise embedding displacement is divided by the geometric mean of the two endpoints' original-space local radii, re-injecting scale information as a change of variables rather than as a competing objective. Across standard benchmarks and scientific datasets from transcriptomics, hyperspectral imaging, and flow cytometry, ScaleMAP matches DensMAP on density preservation while maintaining UMAP-level neighborhood preservation. In transcriptomic data, it recovers sparse bridges between cell populations that UMAP collapses; in flow cytometry, it faithfully represents density structure across 17 orders of magnitude. The same principle applied to PaCMAP yields consistently improved density preservation, suggesting the approach generalizes beyond UMAP.

---


> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-317](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
