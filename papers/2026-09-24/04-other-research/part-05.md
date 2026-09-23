# 📦 其他研究 | 2026年09月24日

> 本类共 **275** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-275](./part-06.md)

---

### 201. [COVER: Codec-Robust Video Watermarking with Generative Video Priors](https://arxiv.org/abs/2609.26236)

**<font color=#1a73e8>作者：</font>** Yuxin Cao, Hao Yang, Ziqi Ding 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video watermarking underpins copyright protection and provenance for generated media, yet almost every video is compressed by a codec before it is stored or shared. A codec discards precisely the perceptually redundant components that most watermarks rely on, so the payload is often lost even when the marked video looked flawless beforehand. Existing methods leave this path open, since they treat compression as one entry in a generic list of distortions, while a real codec is not differentiable and cannot enter gradient-based training. We present COVER, the first learned video watermark built around codec compression as its design target, which survives that compression by embedding the payload in the latent space of a frozen generative video autoencoder and recovering it by re-encoding the received video into that same latent space. To make codec robustness trainable, we build a differentiable codec surrogate bank that simulates the dominant degradation modes of practical compression, and we train the embedder and the latent decoder through three shared recovery paths under a fidelity objective that constrains the residual in the pixel and frequency domains. Across four codecs at 12 settings, COVER attains 93.72% average bit accuracy, ranks first on 11 of the 12, improves the strongest prior method by 2.68 points, and lifts the worst operating point from 68.90% to 73.72% while each marked video stays visually close to the source clip that produced it.

---


### 202. [Can You Delete a Year of Market Data? Machine Unlearning Against Exact Retraining Oracles](https://arxiv.org/abs/2609.26242)

**<font color=#1a73e8>作者：</font>** Junyi Ye  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When a data license expires, deleting stored records does not remove influence encoded in a trained forecaster. Machine unlearning seeks to remove this influence without retraining. We benchmark temporal unlearning with 3,200 paired references trained on all data and oracles retrained without the requested period. The grid covers five architectures, four rolling folds, five deletable years, and three experimental deletion levels on an S&P 500 volatility panel. The 2020 COVID crisis year produces the largest memorization gap for every architecture. Removing it improves all three deployable models in every fold, with the largest improvement in the 2022 bear market, while the two non-deployable models respond inconsistently. The target for approximate unlearning is the oracle, not low predictive accuracy on the deleted period. In one Transformer cell, an oracle that never trained on 2020 still predicts it at an information coefficient of 0.51, compared with 0.55 for the reference; pushing predictions toward noise reduces test skill. Across twelve deployable architecture-method pairs, only TSMixer with the hinge method remains near the oracle in every fold, closing 74-118% of the reference-to-oracle gap without a measurable loss of test skill. Method rankings vary across architectures and rolling windows. Audit separation rises with prior memorization but can remain small after exact deletion. The window-level loss comparison reaches at most 0.69, and treating stock-level windows as independent inflates the absolute t-statistic by a median factor of 1.9. These results call for an explicit deletion scope, oracle validation for the relevant architecture and window, and power-aware auditing.

---


### 203. [A Hybrid AI Framework for Academic Advising: Integrating Ensemble-Based Grade Prediction and a Rule-Based Expert System](https://arxiv.org/abs/2609.26243)

**<font color=#1a73e8>作者：</font>** Hamid Saadatfar, Rohollah Hedayati-Nasab, AmirHossein Eshghi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapidly increasing student population has posed serious challenges to the traditional academic advising process. This study designs and implements a multi-purpose intelligent system to support students' academic progress, based on a two-part hybrid framework: (1) an advanced model for grade prediction and (2) a rule-based recommendation engine. Using a dataset containing 416,558 educational records from the University of Birjand, students were first divided into homogeneous clusters using the Gaussian Mixture Model (GMM). Subsequently, a Stacking Ensemble model combining Random Forest, Gradient Boosting, and MLP was trained specifically for each cluster. Evaluation results demonstrated that the Stacking model outperformed base models across all clusters, achieving a final aggregated RMSE of 2.35. The second component is an expert system that provides intelligent recommendations by synergizing educational regulations with the grades predicted by the first component. This system has been implemented as a practical tool on the University of Birjand portal, offering students real-time feedback such as semester GPA prediction, probation risk warnings, and course suggestions for GPA improvement.

---


### 204. [A Multi-Timestep LSTM Ensemble regressor for Enhanced Short-Term Runoff Prediction](https://arxiv.org/abs/2609.26244)

**<font color=#1a73e8>作者：</font>** Hamid Saadatfar, AmirHossein Eshghi, Behnaz Behdani  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurately forecasting river runoff is key to managing water resources, controlling floods, and planning agriculture. This study examines the Ajichay River in northwest Iran, a major tributary of Lake Urmia that has experienced increasing water-related stress in recent years. We introduce a daily runoff prediction model based on Long Short-Term Memory (LSTM) networks. The model combines five LSTM units, each trained on different time intervals ranging from 2 to 6 days, to better capture variations in river flow patterns. To improve performance, each model was fine-tuned using Particle Swarm Optimization (PSO), a population-based optimization algorithm. The proposed approach was evaluated on unseen data from 2017-2018 using $R^2$, RMSE, and MSE as performance metrics. The results showed strong predictive accuracy, with $R^2$ values ranging from 74.95% to 91.42%. In addition, multiple feature-importance methods were applied to identify the most influential variables, providing further insight into the factors that drive runoff variations.

---


### 205. [eBPF Security in the Wild: Structural Concentration, Failure Mechanisms, and Discovery Gaps](https://arxiv.org/abs/2609.26254)

**<font color=#1a73e8>作者：</font>** Baihong Chen, Hua Ming, Weifeng Pan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Extended Berkeley Packet Filter (eBPF) is a security-critical in-kernel execution framework, yet its vulnerability landscape remains fragmented across components, semantic gaps, and testing techniques. We present an empirical study of observed eBPF vulnerabilities. We construct a multi-source dataset from Linux kernel fixing commits, syzbot reports, and public CVE/NVD records, and analyze it through a unified framework covering structural concentration, mechanism-level failure modes, architectural distribution, and discovery gaps in representative techniques. Our results show that the observed eBPF vulnerability landscape is structurally concentrated rather than broadly dispersed across many unrelated weakness types. The dominant portion is associated with a limited set of recurring system-level failures, especially in runtime execution, concurrency, object lifecycle management, and semantic inconsistencies across trusted stages. These failures are unevenly distributed across the eBPF pipeline: Runtime is the dominant exposure surface, whereas the Verifier and JIT are lowerfrequency but structurally distinct security boundaries. A rubric-based comparison of representative techniques and a version-aligned Syzkaller case study on Linux v5.10 show that, despite visible raw coverage of Runtime, Verifier, and JIT, effective exploration is semantically narrow, and observed discoveries concentrate in a small subset of Runtime failures. Overall, raw coverage alone provides an incomplete view of discovery effectiveness.

---


### 206. [Information-Theoretic Decoupled Prompt Tuning for Continual Learning](https://arxiv.org/abs/2609.26257)

**<font color=#1a73e8>作者：</font>** Yunfei Zhang, Wen Wen, Tieliang Gong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning (CL) aims to incrementally acquire knowledge from sequential data while avoiding catastrophic forgetting. Recently, prompt tuning has attracted increasing attention as an efficient approach for adapting pre-trained models to CL tasks. However, existing prompt design paradigms commonly suffer from retrieval dependence and classifier bias, which make model adaptation sensitive to prompt selection and bias predictions toward newly arrived classes. To address these challenges, we propose Decoupled Prompt Tuning for Continual Learning (DPT4CL), which decouples the CLIP textual prompt into a task-shared prompt distribution and class-specific prompts. The task-shared prompt distribution is derived by optimizing an Information Bottleneck objective to facilitate cross-task knowledge transfer and alleviate classifier bias, while class-specific prompts enhance inter-class separability without relying on explicit prompt retrieval. Furthermore, we establish a unified excess risk bound from an information-theoretic perspective, providing theoretical support for the robust generalization and forgetting mitigation of the proposed framework. Extensive experiments on standard CL benchmarks demonstrate that DPT4CL achieves state-of-the-art performance. The source code is available at this https URL

---


### 207. [CRT-Decomposed $Σ$-Protocols for CSIDH](https://arxiv.org/abs/2609.26258)

**<font color=#1a73e8>作者：</font>** I. Dey, I. Cherkaoui  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We construct a zero-knowledge proof of knowledge for the CSIDH group action that exploits the Chinese Remainder Theorem (CRT) structure of the ideal class group, available whenever the group structure is known exactly, as for CSIDH-512. We prove perfect completeness, perfect special honest-verifier zero-knowledge, and 2-special soundness, in which the secret is recovered from two accepting transcripts by one subtraction and one modular inversion per CRT component; no rewinding loop, lattice reduction, or heuristic sampling appears in the extractor. Because each round admits exactly two responses, Unruh's transform yields a non-interactive proof with straight-line extraction in the quantum random oracle model (QROM), removing the multiplicative forking-lemma loss. We instantiate the scheme on the CSIDH-512 class group, verify the algebraic layer by machine over the exact 258-bit modulus ($10^4$ random instances, all passing), and report protocol-level simulations in the exponent model: Monte Carlo soundness rates matching the proven $2^{-t}$ bound within 95\% confidence at every tested $t$, serialized signature sizes within 1.6\% of the formulas, instrumented action counts, and a scaled meet-in-the-middle attack whose measured cost follows the predicted $\sqrt{q}$ law. We further prove two delimiting results: CRT decomposition cannot enlarge the per-round challenge space, and publishing the CRT hop curves lowers classical key-recovery cost from about $2^{128.6}$ to about $2^{67.3}$ group action evaluations. The construction is therefore correct and structurally complete today, but quantitatively secure only on future parameters whose class number has large prime factors. We compare against CSI-FiSh, CSI-Otter, and Tanuki; a tightly secure blind signature from this proof of knowledge is left to future work.

---


### 208. [Mode Collapse Is Cheap to Detect: A Ground-Truth-Free Pre-Flight Check for Neural Samplers](https://arxiv.org/abs/2609.26272)

**<font color=#1a73e8>作者：</font>** Jian Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural samplers are trained against an unnormalised target $\tilde\pi=e^{-E}$ with no samples from $\pi$, which leaves the practitioner with no way to tell whether an expensive training run has silently dropped part of the target. The diagnostics in common use are computed from the model's own draws and are therefore confined to the model's support: we exhibit a sampler whose self-normalised effective sample size is $0.99$ while it misses $87\%$ of the target mass. We argue that \emph{detecting} missing mass is a strictly easier problem than sampling it: detection needs one point per missed basin plus a local curvature estimate, whereas correction needs the sampler retrained. We turn this into a pre-flight check that consumes a few percent of the sampler's own training budget and uses only $E$, $\nabla E$ and $\nabla^2 E$. On Gaussian-mixture, Many-Well and rotated anisotropic Many-Well targets with exactly computable ground truth, the check estimates the missing mass to within $10^{-3}$ at $2.7\%$ of training cost, where a tuned annealed SMC reference needs $70$--$280\%$ of training cost to do worse. It also applies unchanged to a controlled-SDE sampler that has no tractable density, where ESS and the ELBO cannot be formed at all. The estimator carries a \emph{self-diagnostic} that, without ground truth, is conservative in the safe direction: across $60$ configurations it clears $16$, of which $15$ are accurate to $10^{-2}$ or better. We are explicit about what this does and does not license: the check cheaply produces evidence of missing mass, and sometimes evidence that the search has stabilised, but it cannot certify a run, and its thresholds are heuristic. We then map the boundary of the method on a real physical landscape, LJ-13, and report where it fails and why.

---


### 209. [JAMPR+/L2D: scalable neural heuristic for constrained vehicle routing problems in dynamic environment](https://arxiv.org/abs/2609.26275)

**<font color=#1a73e8>作者：</font>** Andrew Soroka, Alex Meshcheryakov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The vehicle routing problems with real-world constraints (we consider vehicles capacity limits, time windows constrains, pickup-and-delivery multi-depo --- CPDPTW) pose significant computational challenges. While classical exact and heuristic methods remain effective to solve problems of small/medium size ($N\lesssim100$), they often lack adaptability and scalability for larger logistics tasks. In this work, we show how JAMPR+/L2D RL deep learning model, proposed in to solve large CPDPTW problems can be adopted in the case of substantial changes of graph distance matrix. We test performance of JAMPR+/L2D model for medium-sized CVRP and VRPTW problems on CVRPLIB benchmarks: JAMPR+/L2D outperforms the state-of-the-art heuristic HGS in over 85\% of instances, achieving improvement in objective gap. We show that the JAMPR+/L2D model trained on CPDPTW problem, generalizes well for tasks with simpler constraints (CVRP, VRPTW), for different problem sizes and for moderate changes in distance matrixes. For more substantial changes in distance matrixes, we propose here to make fast finetuning of JAMPR+: on ORTEC data (for CPDPTW) the proposed strategy remarkably reduces the objective gap without full model retraining, what will give both accuracy and rapid inference of the model in the practical routing scenarios with distance matrix changes.

---


### 210. [FISSION: Label Augmentation for Bot Detection](https://arxiv.org/abs/2609.26279)

**<font color=#1a73e8>作者：</font>** Sen Yang, Ignacy Nieweglowski, Aviv Yaish  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Bot accounts and coordinated influence operations are often discovered via heuristic methods, leaving a dearth of reliable ground-truth labels for training detection systems. To address this challenge, we study a natural question: can we generate labels to assist in learning embeddings in which bots and accounts from the same coordinated operation are close? We present FISSION, a method to generate labels by splitting each account's activity into positively labeled sub-accounts. Given this label source, we train detection models which preserve behavioral regularities recurring across positive sub-accounts. We evaluate FISSION and show it outperforms prior methods in detecting Wikipedia sockpuppets and Twitter/X bots.

---


### 211. [On the Effect of Bit-Level Parameter Perturbations in Machine Learning and Deep Learning Models](https://arxiv.org/abs/2609.26280)

**<font color=#1a73e8>作者：</font>** Akanksha Raghapur, Mark Stamp  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this chapter, we investigate how classical machine learning models respond to small, targeted modifications in their parameters. We compare and contrast these results to analogous experiments on deep learning models. For classical learning models, we consider Hidden Markov Models (HMM) and Support Vector Machines (SVM), and for comparison, we conduct analogous experiments involving Multilayer Perceptrons (MLP) and Long Short-Term Memory (LSTM) networks. When applied to the Drebin Android malware dataset, our results show that classical models are brittle, in the sense that a limited set of selected parameters can have a dramatic effect on model behavior. In a related set of experiments, we investigate the steganographic capacity of these same learning models, that is, the proportion of bits in model parameters that can be overwritten without having a significant adverse affect on a model. We find that classical models offer limited steganographic capacity due to their compact, parameter-efficient, and relatively sensitive parameter structure. In contrast, neural networks are parameter-redundant, enabling higher steganographic capacity, where modifications can be distributed across many parameters with minimal impact on performance. These results highlight differences in how classical and neural models respond to parameter changes, with clear implications for both robustness and hidden information embedding. Overall, this work provides a framework for understanding parameter sensitivity and steganographic capacity across different classes of learning models.

---


### 212. [Image-Based Techniques and Ensemble Soft Voting for Malware Classification](https://arxiv.org/abs/2609.26281)

**<font color=#1a73e8>作者：</font>** Sushant Rakesh Lokhande, Fabio Di Troia, Martin Jurecek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In this chapter, we investigate image-based malware family classification using an ensemble learning framework and a soft voting strategy. We consider malware binaries that have been converted into images using eight distinct conversion strategies. Three complementary feature extraction tracks are applied to these images: handcrafted descriptors combining Histogram of Oriented Gradients (HOG) and Haralick texture features along with 38 statistical features; dense embeddings obtained from three pretrained neural networks (VGG16, ResNet50, and ViT-B/16), where each pretrained model is used as a frozen feature extractor with its classification head removed; and 512-dimensional embeddings derived from a custom Convolutional Neural Network (CNN) trained directly on the malware images. Each of the three feature extraction techniques is evaluated with machine learning classifiers across all eight image conversion types. The best individual results are 77.8% accuracy for the handcrafted features, 73.8% for the pretrained neural network track, and 74.8% for the custom CNN track. Then we consider various soft voting ensemble strategies, and we find that the best-performing soft voting pool--consisting of fifteen voters selected on a dedicated validation split--achieves 80.2% accuracy across the 17 malware families under consideration, a statistically significant improvement of 2.4 percentage points over the best individual model. A quantitative diversity analysis confirms that the different feature representations are complementary, with the handcrafted descriptors being the strongest contributors.

---


### 213. [Neural Fingerprints for Malware Analysis: An Image-Based Metric Learning Approach with Application to Cross-Domain Classification](https://arxiv.org/abs/2609.26282)

**<font color=#1a73e8>作者：</font>** Manasa Deshagouni, Sayma Akther, Martin Jurecek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Identifying the family of a newly observed malware sample is a core task in threat intelligence, yet conventional classifiers must be retrained whenever a new family appears. This chapter develops an image-based metric learning approach that instead learns to extract discriminative neural fingerprints--fixed-length embeddings--from malware-as-image representations, so that family membership can be determined by nearest-neighbor search in the embedding space. The central advantage of this formulation is zero-shot capability: because the learned embedding induces a similarity metric rather than a fixed set of class boundaries, families that were never seen during training can be recognized by comparison against a gallery, with no retraining. We demonstrate this directly by training an encoder on MalNet-Images-Tiny and MalImg combined (453 families, 96,769 images) and evaluate it zero-shot on a held-out 17-family grayscale dataset with no family overlap. Using a lightweight CNN with multi-proxy anchor loss, this model attains 73.1% retrieval@1 and 90.5% open-set AUROC on families the encoder has never seen. We benchmark our embedding approach against two conventional paradigms in a same-domain setting, where all three are competitive at classifying malware into families. We further show that the learned embeddings transfer across datasets. Unlike classifiers, our embedding approach also yields interpretable similarity scores and scales to large galleries via Facebook AI Similarity Search (FAISS). Finally, we provide a comprehensive evaluation of the learned embedding space using retrieval@k, cluster purity, silhouette score, separation ratio, few-shot accuracy, and open-set detection metrics, along with robustness analysis under image perturbations.

---


### 214. [A Throughput-Oriented Analytical Model for Post-Quantum Security Protocols](https://arxiv.org/abs/2609.26284)

**<font color=#1a73e8>作者：</font>** Ignazio Pedone, Stefano Pirandola  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Growing awareness of the impact of quantum threat on classical cryptography directly translates into a growing demand for accurate network simulation tools capable of estimating the integration effects of quantum-safe cryptography in current systems. In particular, the adoption of Post-Quantum Cryptography (PQC) has a direct impact on the performance of network endpoints and transmission overhead. This also affects the scalability of widely adopted security protocols such as TLS and SSH. In this paper, we present a throughput-oriented analytical model that provides a tight upper bound on the maximum sustainable rate of post-quantum secure connection establishment in TLS and SSH. This model takes into account both endpoint and network capacity constraints, decomposing the handshake process into dominant cryptographic operation time and network transmission time. Identifying the bottleneck allows us to derive the achievable throughput in terms of handshakes per second. The experimental results provided show the accuracy of the model against the data obtained from an experimental testbed using, among others, NIST standard primitives from FIPS 203, 204, and 205, including ML-KEM and ML-DSA. Finally, we integrate our model into a network environment and demonstrate how it can be leveraged to enable efficient resource allocation among multiple endpoints, optimizing PQC traffic in multiple-unicast scenarios.

---


### 215. [Quantifying Protocol-Induced Uncertainty in Comparative Predictive-Model Evaluation: Evidence from Large-Scale Daily PM10 Forecasting](https://arxiv.org/abs/2609.26288)

**<font color=#1a73e8>作者：</font>** Rafael da Silva, Kiersten Monahan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Comparative studies of predictive models often end by ranking candidate models, yet these rankings depend on evaluation protocols whose influence is rarely treated as a source of uncertainty. We formalize this problem as protocol-induced ranking uncertainty and introduce a framework that compares ranking displacement caused by switching protocols with displacement produced by conventional choices within a fixed protocol. We quantify these effects using the Protocol Sensitivity Score (PSS) and a full-refit intraprotocol reference.
We validate the framework in a large-scale sequential prediction study of daily PM10. Static-split and rolling-origin evaluation are compared across 425 European background stations and 365 US EPA monitors. Switching protocols produces mean PSS values of 0.801 and 0.772 and changes the selected model at 35.3% and 31.5% of stations, respectively. In Europe, intraprotocol perturbations with identical scored targets produce PSS values of 0.072 and 0.230, with winner-swap rates of 0.8% and 4.9%. Between-protocol displacement is therefore substantially larger than the selected within-protocol references. Expanding the candidate set from three to nine models increases the between-protocol winner-swap rate to 60.2% in Europe. The pattern also persists under a frozen protocol applied to held-out background and non-background stations. These results show that model-selection conclusions can depend materially on legitimate evaluation choices. We recommend reporting ranking stability under a small set of defensible intraprotocol perturbations alongside claims of model superiority.

---


### 216. [Dual-Frontier: When Can an Agent Trust Its World Model?](https://arxiv.org/abs/2609.26293)

**<font color=#1a73e8>作者：</font>** Huatai Zhu, Qiang Chen, Ziqian Kou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learned world models are becoming essential to general-purpose agents: by predicting action consequences, they support planning and decision-making while reducing reliance on costly trial and error. This reliance creates a fundamental ambiguity: when a world-model-guided decision fails, the trajectory alone may not reveal whether the agent's decision rule or the world model caused the loss. We formalize this failure-attribution problem as a counterfactual decomposition of return loss and prove that its components are not identifiable from passive interaction, even for finite-horizon planners. This obstruction motivates Dual-Frontier, a learning principle that admits a world-model-guided decision only when its predicted advantage exceeds a certified bound on decision-relevant world-model error; otherwise, evidence is allocated to world-model verification. Action-conditioned value bounds and a closed-loop extension guarantee non-decreasing return for admitted decisions. Calibrated gates and simultaneous confidence sequences support adaptive evidence reuse, with sufficient and necessary verification bounds. Controlled learned-model experiments validate the predicted failure modes and certification behavior, while cross-backbone tool-use benchmarks instantiate the same verify-then-promote rule in realistic agent world-model pipelines, consistently improving decision quality and reliability.

---


### 217. [ForeDrive: Foresight-Guided End-to-End Autonomous Driving with a Planning-Relevant Latent World Model](https://arxiv.org/abs/2609.26299)

**<font color=#1a73e8>作者：</font>** Sinuo Wang, Zichong Gu, Yuhan Huang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing latent world models are typically optimized for future predictability, yet the resulting representations are not necessarily useful for planning in autonomous driving. Predictions are commonly used for pretraining or auxiliary supervision rather than as direct conditioning signals for trajectory generation. We propose ForeDrive, which learns a planning-relevant latent representation and couples it asymmetrically to a Diffusion Transformer (DiT) planner. The planner consumes multi-horizon latent future representations learned with a JEPA-style world model; planning gradients update the shared online encoder, while stop-gradient routing trains the latent predictor with forecasting losses only. Because predicted futures have varying reliability across horizons and BEV trajectories are misaligned with image tokens, we use gated visual fusion, future-status injection, and Trajectory-Adaptive Bias (TAB) to inject future latents as guidance without overriding the current observation. Trained with pure imitation learning and using only the current front-view image as visual input at inference, ForeDrive attains 89.9 PDMS on NAVSIM v1 and 90.0 one-stage EPDMS on NAVSIM v2, without reinforcement learning or an external trajectory scorer.

---


### 218. [Staged Multi-step UTXO Workflows via Recursive Invariants](https://arxiv.org/abs/2609.26305)

**<font color=#1a73e8>作者：</font>** Shuyang Tang, Sherman S. M. Chow, Hongfei Fu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Stateless UTXO-style execution validates transactions using local and referenced data, enabling parallel validation and predictable serialized-size/weight accounting. Multi-step workflows thread state across outputs, and a prepared next-step transaction may become stale if another valid spend confirms first. Explicit state threading therefore shifts consistency maintenance, off-chain tracking, and transaction rebuilding to the protocol boundary, increasing coordination cost and latency. Recursive invariants (RIs), our proposed transaction-level logic and toolchain, address this gap by expressing workflow rules as transaction-level predicates over a transaction's inputs and indexed successor positions referenced by the RI. An accepted transaction realizing such a successor position re-checks the predecessor's RI one step later, carrying the workflow rule forward without shared mutable application state or executable output logic. Thus, multi-step protocol rules preserve validation-time locality and admit explicit cost accounting, while cross-transaction guarantees arise from repeated one-step checking. Not all successor clauses are checkable at validation time, so our small statically typed domain-specific language (DSL) uses three-valued semantics (true, false, unknown) to defer future-dependent obligations until checkable. Co-designed with this DSL, our framework formalizes UTXO validation and ledger extension, identifies the validation-time-evaluable one-step fragment, and proves the deduction system sound w.r.t. the three-valued semantics. We give validation and ledger-extension algorithms for this model. We implement a prototype RI interpreter and benchmarking toolchain for six workloads. Six practice-motivated case studies exhibit roughly linear cumulative validation-cost proxy growth and illustrate staged workflow constraints without preconstructing each successor.

---


### 219. [CHiME-9 ECHI: A Machine Learning Challenge for Enhancing Conversations to Address Hearing Impairment](https://arxiv.org/abs/2609.26306)

**<font color=#1a73e8>作者：</font>** Robert Sutherland, Thomas Kuebert, Marko Lugger 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This work presents the task and results of the CHiME-9 challenge for Enhancing Conversations to address Hearing Impairment. The challenge considers the scenario of four-party conversations in a noisy, cafeteria-style environment with interfering speech sources and sound effects. Participants are provided with audio recordings made with Meta Aria glasses and hearing aid microphones, and clean speech samples of the conversation participants. The task is to extract the speech of the conversation partners from the noisy multi-channel recordings with the goal of improving the intelligibility and quality of the speech, evaluated using objective metrics and subjective listening tests. This paper reviews submissions from seven teams and ranks them on a combination of subjective intelligibility and quality. Results show that while the objective metrics do not reflect listener performance, the top systems were able to make substantial improvements over the challenge baseline in both intelligibility and quality ratings.

---


### 220. [PreGS: A Parameter-Transfer-Based Multi-Expert Graph Neural Network for Node Classification](https://arxiv.org/abs/2609.26310)

**<font color=#1a73e8>作者：</font>** Zhicong Cai, Yinglong Zhang, Xiaoying Hong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks have achieved strong performance in node classification by aggregating information from graph neighborhoods. However, a single aggregation mechanism may be insufficient to capture diverse structural patterns across graph datasets. Moreover, independently training multiple structural branches can introduce substantial overhead without necessarily producing stable node representations. To address these issues, this paper proposes PreGS, a parameter-transfer-based multi-expert graph neural network framework. PreGS first pretrains a multi-head graph attention network (GAT) and transfers the linear transformation weights of its first-layer attention heads to multiple GraphSAGE experts. The transferred experts are frozen and used as complementary structural branches. The fused raw node features, GAT head representations, and GraphSAGE expert representations are fed into a multilayer perceptron (MLP), whose output is further fused with the pretrained GAT logits. Based on PreGS, we further develop PreGSv2, which introduces source-level weighting and a structural gating mechanism for adaptive multi-source feature integration. Experiments on eight public graph datasets show that PreGS and PreGSv2 achieve competitive performance against representative graph neural network baselines. Ablation, parameter-transfer, sensitivity, aggregator, visualization, and training-time analyses further validate the effectiveness and stability of the proposed framework. The code and datasets are available at this https URL.

---


### 221. [Leveraging Vision-Based Point Cloud Map Priors for Camera-Based 3D Object Detection and Online Vectorized HD Mapping](https://arxiv.org/abs/2609.26325)

**<font color=#1a73e8>作者：</font>** Markus Käppeler, Rohit Mohan, Abhinav Valada  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-based 3D object detection and online vectorized HD mapping provide compact scene representations for autonomous driving, but both depend on accurate metric geometry and remain limited by depth ambiguity. Over long-term deployment, observations from repeated traversals can be accumulated into persistent point cloud priors that provide geometric context beyond the current observations. Existing explicit point cloud prior approaches, however, rely on LiDAR-based map construction and therefore require expensive 3D ranging sensors. We propose a framework that constructs a static point cloud prior map from previous camera traversals using Pi3X and augments each point with DINOv3 features. At runtime, a local prior patch is retrieved using global localization, encoded with a sparse voxel backbone, and fused in bird's-eye view (BEV) with lifted multi-view camera features. Task-specific sparse transformer heads then predict 3D objects and vectorized map elements from the fused representation. On Argoverse 2, the vision-based prior improves a strong baseline from 0.287 to 0.299 CDS and from 0.669 to 0.750 vectorized mapping mAP. Ablations show that semantic DINOv3 features are particularly important for vectorized mapping. These results demonstrate that vision-built geometric-semantic priors provide an effective form of long-term scene memory for camera-based perception, improving both tasks without LiDAR for prior-map construction or online inference.

---


### 222. [On the Role of the Projector in Contrastive Self-Supervised Learning: Last-Layer Rank Dynamics Drive Representation Quality](https://arxiv.org/abs/2609.26334)

**<font color=#1a73e8>作者：</font>** Siladittya Manna, Priyangshu Mandal, Umapada Pal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The dimensional collapse of representations in self-supervised contrastive learning is an ever-present issue. One notable technique to prevent such a collapse of representations is using a multi-layered perceptron network called Projector. In several works, the projector has been found to heavily influence the quality of representations learned in a self-supervised contrastive pre-training task. However, the question still lingers. What role does the projector play? Assuming the projector mitigates dimensional collapse, what prevents the terminal layer of the base encoder from functioning as the projector in the absence of an explicit multi-layer perceptron (MLP) head? In this work, we intend to study what happens inside the projector by examining the rank dynamics of the same and the encoder through empirical study and analysis. Through mathematical analysis, we observe that the effect of rank reduction predominantly occurs in the last layer. Motivated by this insight, we propose a weight regularization strategy applied specifically to the last layer. We demonstrate that this targeted approach yields better performance than applying orthogonal weight regularization across the entire network (WeRank), both with and without a projector. Our method improves Top-1 accuracy by more than 1% on SimCLR on the ImageNet100 dataset and consistently outperforms baseline SimCLR variants on CIFAR datasets, supporting our interpretation of the projector's role.

---


### 223. [Designing and Analysing Argument Mining Pipelines: Towards a Comprehensive Assessment](https://arxiv.org/abs/2609.26338)

**<font color=#1a73e8>作者：</font>** Siddharth Bhargava, Sara Tonelli, Patricia Martín-Rodilla  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Argument Mining (AM) transforms natural language into its underlying argument structures. This transformation is typically realized through a sequence of AM tasks that form an end-to-end AM pipeline. However, AM approaches often differ in how they conceptualize these tasks, making direct comparisons between them difficult and opaque. This calls for a more nuanced, task-level analysis of AM approaches to enable clearer comparison and assessment.
This work presents a preliminary meta-study that systematically reviews several state-of-the-art end-to-end AM works and analyzes their pipelines through a triple-perspective framework---a linguistic, computational and domain perspective---to understand how the pipelines model arguments as structures, computes them, and integrates domain knowledge. We further propose a general design to the linguistic and computational perspectives, illustrating how key AM tasks are designed for modeling and computation of argument structures. Our proposed framework lays the groundwork for methodology-centered descriptions across AM approaches, facilitating deeper understanding and more systematic comparisons in future research.

---


### 224. [Geometry-Aware Hyperbolic Residual Quantization](https://arxiv.org/abs/2609.26342)

**<font color=#1a73e8>作者：</font>** Alessio Colombo, Melika Ayoughi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Residual Vector Quantization turns continuous representations into discrete, multi-level token sequences. Yet most methods operate in Euclidean space, despite the coarse-to-fine structure of the resulting codes and the latent hierarchies present in many data domains. Hyperbolic geometry offers a natural alternative for hierarchical representations, but naive hyperbolic extensions introduce geometric inconsistencies: non-associative hyperbolic addition prevents consistent residual aggregation, while standard straight-through gradient estimation ignores the geometry of the latent space. We propose a geometry-aware hyperbolic residual quantization that addresses these issues in both the forward and backward passes. In the forward pass, Hyperbolic Residual Aggregation restores the telescoping behavior of residual quantization on the Poincare ball. In the backward pass, a discounted Hyperbolic Straight-Through Estimator routes the reconstruction gradient through the quantizer as a single geometric block, avoiding unstable recursive gradient transport across residual stages. Evaluations on hierarchical prediction, recommendation, image tokenization, and neural audio coding tasks show that our method improves the stability and structural organization of hyperbolic residual codes over naive hyperbolic baselines. At the same time, we observe a clear structure-compression trade-off: Euclidean residual quantization remains preferable for pure compression, while geometry-aware hyperbolic quantization is most useful for hierarchically organized discrete latent spaces.

---


### 225. [Blaming Across the Aisle: Political Contrasting and Blame Attribution in the Danish Parliament](https://arxiv.org/abs/2609.26346)

**<font color=#1a73e8>作者：</font>** Markus Lundsfryd Jensen, Rune Egeskov Trust, Kenneth Christian Enevoldsen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Political discourse is widely perceived to be growing more hostile, yet robust evidence remains scarce. This study examines blame attribution in the Danish Parliament from 1997 to 2026, combining a purpose-built classifier, BlameBERT (F1: 0.80), with multilevel statistical modeling. The classifier is constructed using an annotation-efficient pipeline for blame attribution in low-to-mid resource languages. The results reveal a banana-shaped trajectory, with blame declining until around 2016 before entering a significant and sustained increase in recent years (2019-2026). Government status consistently influenced blame attribution - an effect we term political contrasting - with opposition parties blaming substantially more than governing parties. This effect was moderated by ideology: The blame-dampening effect of governing was less pronounced among right-wing parties, and ideological extremity amplified blame more strongly on the right. In recent years, the interaction between political wing and ideological extremity intensified, suggesting an ideological hardening of the blame rhetoric concentrated on the right of the political spectrum. Taken together, these patterns suggest that the perceived rise in harsh political language reflects not merely a general rhetorical drift, but an ideologically asymmetric hardening of political discourse. A sensitivity analysis showed that the conclusions were robust to varying classification thresholds.

---


### 226. [HYDRA: Proactive Android Malware Drift Adaptation via Hierarchical Graph Contrastive Learning](https://arxiv.org/abs/2609.26352)

**<font color=#1a73e8>作者：</font>** Han Chen, Hanchen Wang, Hongmei Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Concept drift, driven by the rapid evolution of Android malware, severely degrades the performance of machine learning detectors. Current adaptation strategies are often reactive, responding only after performance has dropped and imposing a significant manual annotation burden, or they are proactive but rely on unstable adversarial training and incomplete, single-level graph representations. To overcome these limitations, we propose HYDRA (Hybrid Drift Adaptation), a proactive adaptation framework that learns drift-invariant representations from hierarchically structured data. HYDRA first models applications using a hybrid graph structure, combining fine-grained Control Flow Graphs (CFGs) and coarse-grained Function Call Graphs (FCGs) to capture comprehensive behavioral patterns. It then introduces a novel cross-domain contrastive learning objective that aligns historical (source) and new (target) data distributions. By generating pseudo-labels for unlabeled target samples, our method pulls representations of semantically similar applications together, regardless of their domain, within a single, stable optimization process. This approach unifies feature learning and domain alignment, eliminating the need for complex adversarial objectives. Extensive experiments on large-scale, time-ordered malware datasets demonstrate that HYDRA achieves substantially lower False Negative and False Positive Rates than state-of-the-art baselines while requiring up to 87.5% fewer labeled samples. Our work thus offers a robust and efficient solution to combat concept drift in security applications.

---


### 227. [Formally Modeling the Terrapin Attack on SSH](https://arxiv.org/abs/2609.26358)

**<font color=#1a73e8>作者：</font>** Jörg Schwenk, Fabian Bäumer, Marcus Brinkmann  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Terrapin attack against SSH channel integrity (USENIX Security 2024) used a novel attack vector: attacks on the channel state. Surprisingly, not all AEAD modes of SSH were equally affected by this attack, and it remained an open question if "unaffected" meant "secure". Existing formal models for secure channels are based on stateful encryption. However, these models do not define what the channel state is and how it is used as input to the different AEAD modes.
In this paper, we propose a formal model for channel integrity under partially chosen state. Applied to the Terrapin attack, the chosen state is the SSH sequence number. It uses an abstract stateful encryption interface, for which we provide pseudocode descriptions for the eight most prominent AEAD modes used in SSH. By varying the SND oracle, we can model ciphertext-only (CO; the Terrapin attack), known-plaintext (KPA), and chosen-plaintext (CPA) attacks. This allows us to establish concrete bounds on the security of the AEAD modes. We find that all three Encrypt-then-MAC (EtM) modes and ChaCha20-Poly1305 in SSH are insecure in the CO model. AES-GCM is the only cipher secure in all three model variants. Going beyond Terrapin, we show that Encrypt-and-MAC (EaM) with a CBC cipher is secure, even in the KPA model. In particular, we describe a novel BEAST-like chosen-plaintext attack on the channel integrity of EaM-CBC, which separates the KPA and CPA models for this scheme.

---


### 228. [FairMean: Promoting Fairness in Distributed Learning under Label Poisoning Attacks](https://arxiv.org/abs/2609.26377)

**<font color=#1a73e8>作者：</font>** Huigan Zheng, Jiaojiao Zhang, Yongxiang Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fairness-aware distributed learning prioritizes clients with large losses to reduce performance disparities, but label poisoning can create large losses, thereby inducing a fairness--robustness conflict. We propose FairMean to manage this conflict. FairMean weights client gradients using a bounded, nondecreasing function of local loss. The increasing weights prioritize high-loss clients to promote fairness, while the upper bound prevents excessive loss-induced amplification of poisoned-client gradients. In the absence of label poisoning, we show that minimizing the FairMean objective is more conducive to solution fairness than minimizing the standard average-loss objective. Under label poisoning, we establish an average-stationarity bound whose attack-dependent term is proportional to the square of the poisoned-client fraction. Experiments show that FairMean promotes fairness by reducing accuracy variance while improving worst-client accuracy.

---


### 229. [Layout-Guided Masking for GROBID: Lightweight Structural Gains in Large-Scale Scientific PDF Ingestion](https://arxiv.org/abs/2609.26381)

**<font color=#1a73e8>作者：</font>** Luca Foppiano, Sana Khamassi, Vipul Gupta  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transforming scholarly PDFs into machine-readable fulltext remains a bottleneck for large-scale information systems. Recent vision-based parsers improve accuracy, but need GPUs and may introduce noise into the extracted text. GROBID, a modular font-stream parser running on CPU, is the de-facto standard for structuring scientific articles and underpins several of the largest open scholarly corpora. We pair it with a lightweight CPU detector localising figure, table, and paratext (header, footer, page number) regions, encoded as typed-area masks whose tokens are routed to GROBID's specialised models or discarded. On two PMC corpora, Bioinformatics (1,926 articles) and Materials Science (2,595), scored against JATS with a section-aware structural protocol, our extension improves over plain GROBID on most metrics (NS $+0.025$/$+0.013$; $+0.086$ paragraph recall on Materials Science, $d_z{=}1.08$), and caption-linked figure recovery improves on both corpora. On the external Table-BRGM benchmark, table detection recovers F1 $0.16 \to 0.94$ and table structure follows (GriTS-Top $0.27 \to 0.78$, below the strongest GPU system). On body text, against four vision-based systems (Docling, MinerU, olmOCR, this http URL), it has the best paragraph precision on both corpora, the best section detection on Materials Science, and a character error rate within 0.004 of the best GPU parser. End-to-end on CPU, it costs $2.7$--$3.2\times$ less than the cheapest GPU system (Docling) and $10$--$14\times$ less than generative parsers.

---


### 230. [Learning to Defer with Guidance on Real World Medical Data](https://arxiv.org/abs/2609.26384)

**<font color=#1a73e8>作者：</font>** Emma Sun, Joshua Strong, Alison Noble  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Medical image interpretation is high-volume and time-consuming, and while AI interpretation can reduce workload, fully autonomous deployment carries potential safety concerns and low specificity may in practice lead to increased clinician workload. Learning to Defer (L2D) addresses this by selectively routing cases between autonomous prediction and human experts by learning from input features and AI model and human performance. While theoretical guarantees have been proven for L2D, its performance has not been validated on real-world medical datasets with human reader annotations. We evaluate the predictor-rejector formulation of two-stage L2D, where the AI predictor model is fixed and separate from the trainable routing or rejector model, on Collab-CXR, a multilabel chest X-ray dataset with multiple human annotations per case. This is the first work to look at L2D in the context of real-world medical imaging data with human annotations. We further introduce a new setup, L2D with Guidance, where the decision space is extended to three choices: predict autonomously, defer to a human expert, or defer to a human expert and provide AI guidance. We compare multiple rejector architectures and loss functions, and different input feature availabilities. This is reproduced on two larger datasets, VinDr-CXR and CheXpert. Our results show that two-stage L2D with Guidance outperforms classic two-stage learning to defer, as well as human-alone, AI-alone and AI-guided human baselines. Notably, this performance is achieved with simpler loss functions compared to formally defined L2D surrogate loss functions in current literature.

---


### 231. [Double Descent and Malign Overfitting in Diffusion Models](https://arxiv.org/abs/2609.26392)

**<font color=#1a73e8>作者：</font>** Raphaël Urfin, Tony Bonnaire, Giulio Biroli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conventional wisdom in deep learning holds that overparameterization---having more parameters $p$ than training samples $n$---is benign: larger models generalize better and, even without regularization, interpolating models generalize well, the test error following a double-descent curve. One might expect the same benign overfitting for diffusion models, whose training reduces to regression, i.e. to minimizing a quadratic score-matching loss. Yet the opposite is observed: overfitting here is catastrophic, driving the model into a memorization regime. We resolve this paradox by combining experiments on U-Nets trained on CelebA with a random-features model for which we derive closed-form learning curves. We show that with a fixed number $m$ of noise realizations per training sample, an interpolation peak does occur, but at $p\sim nm$ rather than at $p\sim n$ as in standard regression. The rise of the test loss, however, sets in much earlier, at $p\sim n$, independently of $m$. This overfitting is malign because, although the implicit regularization of training is fully at work, it drives the model toward the empirical score, which memorizes the training set, rather than toward the true score. A bias-variance decomposition pinpoints the mechanism: the bias of the score estimator starts to grow at $p\sim n$; past the peak the variance decays, as in regression, whereas the bias keeps growing and both saturate at a large value. Since diffusion models are trained with $m\gg1$, the peak is pushed to very large model sizes, and therefore sit on the rising branch that precedes it, where malign overfitting is already in play. Nevertheless, overparameterization remains beneficial when paired with regularization: in the random-features theory and in U-Net experiments, optimally regularized large models---via a ridge penalty or early stopping, respectively---outperform any unregularized models.

---


### 232. [AI-Generated Email Drafts Shift Culturally Distinctive Communication Styles in Professional Email](https://arxiv.org/abs/2609.26403)

**<font color=#1a73e8>作者：</font>** Shintaro Sakai, Alice Gao, Yuichi Shoda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI assistants that support email composition may shift cultural communication norms, such as the directness typical of low-context cultures like the US versus the indirectness and contextual sensitivity central to high-context cultures like Japan. Yet it remains unknown to what extent people adopt and edit AI drafts inconsistent with their cultural communication norms. We address this through a preregistered within-subject experiment in which Japanese and American participants wrote workplace emails in their native language without AI, with a low-context AI, and with a high-context AI. We found that Japanese participants wrote emails with significantly more high-context markers (politeness, apologies) than Americans. But AI drafts shifted participants' emails toward the draft's style, with larger shifts when the draft was culturally misaligned: Japanese drifted most under low-context drafts, Americans most under high-context drafts. These findings suggest AI drafts risk overwriting cultural communication norms unless they adapt to users' communication styles.

---


### 233. [Reliability Theory for AI Control](https://arxiv.org/abs/2609.26419)

**<font color=#1a73e8>作者：</font>** Grant Molnar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliability theory gives a mature language for layered systems, but its formal tools are not yet standard in frontier AI control. We apply them to Google DeepMind's defenses against rogue deployment. The same control stack can have cubic, quadratic, or linear rare-failure suppression depending on its failure domains. Birnbaum importance identifies which component improvements buy the most nominal reliability, while prevention changes the population on which recovery is demanded. These results give concrete guidance about what to separate, improve, measure, and test.

---


### 234. [Enriching Speech Emotion Representations with Conversational Context](https://arxiv.org/abs/2609.26422)

**<font color=#1a73e8>作者：</font>** Arthur Peuvot, Romaric Besançon, Gaël de Chalendar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Detecting emotions is necessary for building systems that can accurately and adaptively interact with humans. Speech Emotion Recognition (SER) has become an important research focus to develop intelligent spoken interfaces. However, most studies predict emotions at the utterance level, ignoring the conversational context, along with the emotional flow and speaker interactions it carries. In this paper, we introduce ACERT (Averaged Contextual Emotion Representation through Time), a module that integrates a flexible-length window of conversational context to better capture emotional evolution in spoken interactions. To evaluate the robustness of this method, we conducted experiments on datasets spanning diverse emotionally expressive styles and contexts. ACERT outperforms current state-of-the-art (SOTA) approaches on IEMOCAP, establishes the first context-aware benchmark on SAFE, and obtains strong results on MELD for unweighted, class-balanced metrics. Ablation studies show that ACERT's gains come from emotional and conversational continuity, rather than from speaker identity or acoustic conditions.

---


### 235. [DeepFEAv2: Deep Learning for Transient Finite Element Analysis Beyond Structured Meshes](https://arxiv.org/abs/2609.26426)

**<font color=#1a73e8>作者：</font>** Georgios Triantafyllou, Panagiotis G. Kalozoumis, Dimitris K. Iakovidis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Finite Element Analysis (FEA) is widely used for transient mechanical simulations, but its high computational cost limits real-time and high-resolution applications. Deep learning surrogate models can reduce this cost; however, many existing approaches are restricted to steady-state prediction or cannot jointly predict Node- and Element-based Outputs (NEO) over time. The state-of-the-art DeepFEA framework has addressed these issues but remains limited to structured finite element (FE) meshes. To overcome this limitation, this study proposes DeepFEAv2, a deep learning surrogate framework that enables prediction of transient FEA simulations across different FE mesh topologies and element types. The main contributions of DeepFEAv2 are: (a) a module that uses the FE connectivity matrix to organize input features by element and arrange them into an input sequence guided by the mesh topology; (b) a novel neural network architecture designed to process the input sequence and jointly predict NEO over time; and (c) a FEA-informed optimization strategy for regularizing these NEO predictions. DeepFEAv2 was evaluated on structured and unstructured 3D linear elastic datasets, as well as on a pressure-driven aortic valve dataset. DeepFEAv2 achieved R^2 values up to 0.99 and normalized errors as low as 0.38%. Compared with DeepFEA, it achieved up to 38.0% relative increase in R^2 and up to 87.1% reduction in normalized error. DeepFEAv2 also performed inference up to three orders of magnitude faster than traditional FEA. These results demonstrate that DeepFEAv2 can efficiently model transient FEA simulations across increasingly complex FE settings, providing a scalable surrogate framework for transient FEA.

---


### 236. [The Source of Disturbance Matters: External, Internal, and Control-Generated Noise in Adaptive Regulation](https://arxiv.org/abs/2609.26428)

**<font color=#1a73e8>作者：</font>** Veronique Ziegler  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Adaptive regulation can itself perturb the state it is intended to stabilize. In replicated simulations of an adaptive agent, we compare external disturbance, persistent internally generated disturbance, and control-generated disturbance under regulation-first and disturbance-first ordering. Persistent internal disturbance produces the largest exposure and regulatory burden within the tested parameter grid. When positive controller updates generate an immediate disturbance cost, increasing that cost produces a nonmonotonic response: effective disturbance initially rises, variability across stochastic runs increases over an intermediate range, and corrective activity becomes strongly suppressed at higher costs. The results show how disturbance source and timing shape exposure and controller burden in this model. They motivate testing adaptive agents with distinct disturbance sources and assessing regulatory activity alongside exposure.

---


### 237. [Latent Dataset Distillation for Human Motion Prediction](https://arxiv.org/abs/2609.26430)

**<font color=#1a73e8>作者：</font>** Ge Tian, Guang Li, Takahiro Ogawa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dataset distillation (DD) compresses a large training set into a compact synthetic set while preserving downstream training utility. Although DD has been widely studied for images and recently extended to time-series forecasting, its application to human motion prediction remains largely unexplored. Human motion is high-dimensional and structurally coupled, and gradient matching (GM) in the original motion space optimizes many correlated variables without a prior on pose plausibility or temporal dynamics, which frequently yields implausible and unstable synthetic motions. To address this limitation, we propose a latent DD framework that regularizes distillation with a learned motion prior. Motions are first compressed by a residual-quantized variational autoencoder (RVQ-VAE), and distillation then updates only a learnable latent bank through the frozen quantizer and decoder. The pretrained decoder restricts synthetic motions to its output space, while residual quantization progressively refines the latent approximation across multiple codebooks and alleviates the representational bottleneck of single-stage vector quantization. Experiments on Human3.6M, CMU, and 3DPW with two prediction backbones show that the proposed framework outperforms direct GM in 27 of 30 evaluated settings and random subsets in every setting, and produces visibly more plausible synthetic motions in qualitative comparisons.

---


### 238. [One-Step Generative Surrogate Models via Block-Triangular Joint Drifting](https://arxiv.org/abs/2609.26435)

**<font color=#1a73e8>作者：</font>** Nicholas Geissler, Shreya Jha, Ricardo Baptista 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Drifting provides a direct route to one-step generative models, but applying it directly to stochastic transition modeling requires multiple samples of the next state conditioned on the same current state. Standard trajectory data, however, typically provide only one realized next state for each observed current state and therefore do not provide an empirical approximation of the corresponding conditional distribution over possible next states. We introduce block-triangular joint drifting, which instead applies a projected drift field to the empirically accessible joint distribution of consecutive states. Importantly, the block-triangular architecture preserves the current-state marginal while making its second component a direct sampler of the conditional distribution of possible next states. The resulting surrogate generates stochastic trajectories with one model evaluation per time step, without auxiliary generative steps between time steps. Numerical experiments demonstrate accurate marginal and trajectory-dependent statistics and favorable accuracy-cost tradeoffs compared with deterministic, diffusion-, flow-, and distillation-based generative surrogate models.

---


### 239. [Mammo-LIFE: Longitudinal Mammographic Imaging and Clinical Feature Enrichment for Post-Radiotherapy Outcome Prediction](https://arxiv.org/abs/2609.26443)

**<font color=#1a73e8>作者：</font>** Farnoush Bayatmakou, Maryam Hosseini, Reza Taleei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Artificial Intelligence (AI)-powered Computer-Aided Diagnosis (CAD) systems have substantially improved breast cancer screening, diagnosis, and prognosis. Comparatively, postradiotherapy outcome prediction using paired longitudinal mammograms has received considerably less attention. This is largely due to the limited availability of well-annotated longitudinal datasets. Longitudinal mammograms, coupled with paired pre- and post-treatment information, provide a unique opportunity to characterize treatment-induced breast tissue changes following radiotherapy. The resulting learned representations can serve as a valuable asset for advancing personalized radiotherapy planning and post-treatment management. In this context, we propose Mammo-LIFE, a patient-level multimodal framework for post-radiotherapy outcome prediction that combines longitudinal mammographic features with patient-level clinical variables. The imaging branch processes paired pre- and post-treatment mammograms acquired from the four standard views using a mammography-specific encoder adapted via Low-Rank Adaptation (LoRA). Within each view, preand post-treatment representations are explicitly compared through a longitudinal comparison module to capture treatment-related changes. The resulting view-level embeddings are then aggregated using learned view-attention pooling to form a unified patient-level mammographic representation. Selected clinical variables are subsequently combined with the image-derived prediction probability through a late-fusion strategy. To evaluate the effectiveness of combining paired longitudinal mammograms with clinical information, experiments were conducted on an in-house clinical cohort using patient-level stratified five-fold cross-validation.

---


### 240. [Recursive self-improvement of AI research agents](https://arxiv.org/abs/2609.26457)

**<font color=#1a73e8>作者：</font>** Dhruv Srikanth, Bingchen Zhao, Dixing Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are beginning to automate research and development across the AI stack, from improving training efficiency to optimizing inference. A natural next step is to improve the research efficiency of the agents themselves. When an AI research agent's own code is the object of optimization, each accepted rewrite becomes the agent that the next round edits. We refer to this loop as recursive self-improvement. Its significance lies in a long-standing trend, in which increased cumulative spending on R&D yields diminishing returns. Sustained self-improvement offers a way to counter this trend. We present AIDE^2, a system that implements this loop for a frontier AI research agent. It proposes changes to its own code, benchmarks modified versions of itself on a suite of AI R&D tasks, and keeps the changes that perform best on hidden evaluations. In an autonomous 8-day run, AIDE^2 discovered seven successive improvements, ranging from a new search policy to memory mechanisms that compress and manage the agent's growing context. These gains generalize to four held-out benchmarks spanning machine learning engineering, heuristic algorithm engineering, and physics-based weather forecasting, the last of which is out of distribution from the selection tasks. On all four, the strongest discovered agent matches or exceeds a human-engineered production research agent that ranks among the strongest on FML-Bench. On a separate held-out task family, the discovered agents also exhibit reduced reward hacking, a property the loop never explicitly optimized for: the rate falls from 55% to 32% during the run, 7 percentage points below the human-engineered agent. Together, these results show that an AI research agent can improve its own research efficiency through recursive self-improvement, and that these gains transfer to tasks and domains the loop never encountered.

---


### 241. [Code Plans, Diffusion Renders: Open-Ended Generative World Modeling](https://arxiv.org/abs/2609.26458)

**<font color=#1a73e8>作者：</font>** Zixun Fang, Yawen Shao, Kai Zhu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce \textbf{CoDeR}, a new paradigm for world modeling. Unlike existing video world models that implicitly represent world dynamics through visual observations, our system explicitly constructs an executable world with code and employs video generation models for visual realization. Specifically, we coordinate five complementary roles to translate high-level concepts into structured world rules, executable dynamics, and perceptual observations. This design enables \textit{long-term memory}, \textit{open-ended interactions}, \textit{autonomous world evolution}, and \textit{multi-agent scenarios}, where multiple entities can act, interact, and evolve persistently beyond the current observation. Extensive experiments demonstrate that our framework substantially extends the capabilities of existing world models, enabling long-term memory, open-ended interactions, autonomous evolution, and persistent multi-agent dynamics, while achieving state-of-the-art performance across multiple evaluation settings. Code and model weights will be made publicly available. Project Page: \href{this https URL}{CoDeR}.

---


### 242. [Can We Predict Anomaly Detection Performance from Embedding-Space Geometry?](https://arxiv.org/abs/2609.26460)

**<font color=#1a73e8>作者：</font>** Kevin Wilkinghoff, Zheng-Hua Tan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Anomaly detection systems are often trained using normal data alone, while model selection and evaluation typically require labeled anomalies. We study whether anomaly detection performance can be predicted without access to anomalous data. For kNN-based detectors, we derive a lower bound on the area under the ROC curve (AUC) that relates detection performance to the separation between inlier and outlier scores and to their respective variances. Under a local scaling model, we use this bound to characterize how density variation, intrinsic-dimensional heterogeneity, and cross-domain mismatch contribute to score variability. We then investigate anomaly-free model selection and show that inlier score variance alone does not reliably predict performance across different representations. To address this limitation, we introduce simple pseudo-anomaly probes that provide a reference for estimating relative score separation. Experiments on the DCASE 2022-2025 benchmarks, spanning four embedding models and 208 candidate systems, show that pseudo-anomaly-based estimators substantially improve anomaly-free model selection. In particular, diverse pseudo-anomalies enable anomaly-free model selection to outperform conventional development-set selection under domain shift. These results show that embedding-space geometry contains predictive information about anomaly detection performance while also highlighting the representation-dependent nature of inlier-only performance estimates.

---


### 243. [Reproducible AI Requires Reproducible Randomness](https://arxiv.org/abs/2609.26461)

**<font color=#1a73e8>作者：</font>** Anthony Bertrand, Tom Schmitt, Engelbert Mephu Nguifo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pseudorandom number generators (PRNGs) constitute indispensable computational tools across multiple scientific domains, including Monte Carlo simulations, stochastic computing, and artificial intelligence (AI). The reproducibility of such applications critically depends on the ability of PRNG implementations to generate identical sequences across software environments when initialized from the same internal state. These algorithms enable the simulation of stochastic processes while providing deterministic and repeatable behaviour, thereby facilitating reproducible experiments. Modern PRNG implementations may be initialized through either a seed or, more accurately, an initial state that exceeds the capacity of a conventional integer seed. However, reliance on a simple seed alone frequently proves insufficient to ensure consistent program execution traces across different implementations. A natural assumption is that transferring the complete internal state of a generator should guarantee identical outputs regardless of the software library used. This study examines the validity of this assumption by investigating whether complete initial states can ensure cross-library fidelity and portability of PRNG streams. We focus on two widely deployed generators, Mersenne Twister and Philox, and evaluate their implementations across four major Python ecosystems-Random, NumPy, PyTorch, and TensorFlow. We compare the sequences produced by these implementations against those generated by the original reference algorithms under identical initialization conditions. Our results demonstrate that reproducibility cannot be assumed from PRNG state transfer alone, even when implementations claim to follow the same underlying algorithm. While fidelity was successfully achieved for several implementations, significant discrepancies were observed in others. Most notably, the Philox implementation in PyTorch exhibits fundamental incompatibilities with the reference algorithm, preventing exact reproduction of generator outputs across environments. These findings challenge the common expectation that access to a full internal state of a PRNG is sufficient to ensure reproducibility across software stacks. They further highlight that implementation-specific design choices can introduce hidden barriers to experimental replication, particularly in AI workflows that rely on multiple frameworks. This work shows that implementation fidelity of a PRNG is a necessary condition for scientific reproducibility and makes two primary contributions. First, it identifies practical guidelines for achieving reliable PRNG usage and reproducibility within the Python scientific and AI ecosystem. Second, it evaluates the extent to which cross-library portability and fidelity can be recovered through user-level techniques, without requiring modifications to library source code.

---


### 244. [Complementary Roles of Radiomics and Foundation Representations in Renal Cell Carcinoma Classification: A Comparative Study of 2D and 3D CT Encodings](https://arxiv.org/abs/2609.26463)

**<font color=#1a73e8>作者：</font>** Yuan Liang, Sourav Bhattacharjee, Abraham Campbell  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate preoperative subtype classification of renal cell carcinoma (RCC) from contrast-enhanced computed tomography remains clinically challenging. Radiomics provides structured tumour descriptors, whereas foundation representations offer transferable image features. However, it remains unclear whether radiomics still adds value beyond pretrained representations, and how 2D and 3D MedVAE encoders compare in this setting.
We compared handcrafted radiomics, 2D MedVAE, 3D MedVAE, and their fusion for binary clear-cell RCC versus non-clear-cell RCC classification on KiTS23 under a unified preprocessing pipeline. Concatenation, cross-attention, and gated fusion were evaluated as representative integration strategies, and radiomics feature importance was analysed to support decision-centric interpretability.
Fusion consistently improved discrimination over image-only MedVAE branches. The best overall performance was achieved by 3D gated fusion, with an AUC of 82.7\%, outperforming the best 2D fusion model (79.6%), the radiomics baseline (74.4%), and the single-modality MedVAE branches. Ablation analysis further showed clear gains of the full fusion model over both image-only and radiomics-only variants, indicating complementary contributions from radiomics and image representations.
These findings suggest that radiomics remains relevant for RCC CT classification in the presence of foundation representations, and that its integration with MedVAE is more effective in the 3D setting. More broadly, the study supports a complementary role for radiomics and foundation representations in clinically meaningful imaging decision support.

---


### 245. [PP-Net: A Hybrid Physical-Prior Neural Network for Scattered Light Removal in Biomedical Images on Embedded Devices](https://arxiv.org/abs/2609.26474)

**<font color=#1a73e8>作者：</font>** Yongfei Guo, Tingjin Chu, Mengzhuo Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scattered light is common in biomedical images, yet its removal remains challenging. The difficulty arises from three aspects: first, aligned scattered-light-free biomedical ground truth is often unavailable; second, scattering is coupled with weak illumination and sensor-induced noise; and third, many learning-based restoration models are computationally expensive for embedded devices in Internet of Medical Things (IoMT) scenarios. To address these issues, this paper proposes PP-Net, a hybrid physical-prior neural network for biomedical scattered light removal. The proposed method consists of three components: DFN-Net suppresses sensor-induced noise, ASAP estimates the scattering map and recovers a physics-based prior map, and GF-Net refines the prior map by fusing it with the denoised observation. To reduce the dependence on paired biomedical ground truth, a progressive synthetic training and cross-domain transfer strategy is developed. Experiments show that the physical-prior branch improves the peak signal-to-noise ratio (PSNR) by up to 1.26 dB on paired synthetic benchmarks. Under joint noise-and-scattering degradation, PP-Net improves PSNR by more than 10.8 dB and the structural similarity index measure (SSIM) by more than 0.62 compared with representative baseline methods. On real W2S biomedical images, the proposed method reduces the average Natural Image Quality Evaluator (NIQE) score by 43.3\%. Edge deployment with RKNN conversion and INT8 quantization achieves an average inference latency of approximately 200 ms per $512\times512$ image over 360 test images. These results demonstrate that PP-Net provides an effective and deployable solution for microscopic imaging, endoscopic inspection, and edge-assisted biomedical analysis in IoMT scenarios.

---


### 246. [When Recursive Models Finish Computing](https://arxiv.org/abs/2609.26487)

**<font color=#1a73e8>作者：</font>** Hare Krishna, Shubham Singh, Stephen Ebert 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recursive models can continue updating their latent states beyond their nominal inference budget, so an incorrect output at that budget does not show whether computation is unfinished or has entered a persistently unsuccessful regime. We study the dynamics of completion in attention- and MLP-based Tiny Recursive Models (TRMs) on 1,000 hard Sudoku puzzles. Extending recurrence from the nominal 16 steps to 512 steps increases cumulative exact-solve accuracy from 59.2% to 87.5% for the attention model and from 74.4% to 91.9% for the MLP model, solving more than two-thirds of the puzzles unsolved in the nominal budget. Across both architectures, latent-state motion drops sharply after the first exact solution. Completed states are typically locally contractive along the trajectory direction, even though the same local Jacobian retains strongly expanding directions. We characterize this phenomenon as trajectory-conditioned anisotropic stability. Perturbation experiments confirm this directional stability across both models. The multi-step fate of the maximally expanding direction differs: it is absorbed within 16 steps in the attention model but persists longer in the MLP model. The anisotropic-stability pattern also holds for a second attention checkpoint. Together, these results distinguish nominal-budget failure from completed computation and identify a common dynamical signature of completion across two recurrent architectures.

---


### 247. [Radiomics-Conditioned Modulation of RenalCLIP Features for Clear Cell Renal Cell Carcinoma Classification](https://arxiv.org/abs/2609.26492)

**<font color=#1a73e8>作者：</font>** Yuan Liang, Sourav Bhattacharjee, Abraham Campbell  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiomics provides quantitative descriptions of tumour appearance that may complement disease-specific foundation models in small labelled cohorts. We investigate this complementarity for computed tomography-based classification of clear cell renal cell carcinoma. Our framework uses radiomics to modulate RenalCLIP features through feature-wise linear modulation (FiLM), while retaining a direct radiomics contribution. Internal testing and external validation compare it with conventional fusion strategies and reference classifiers. The FiLM model achieves an area under the receiver operating characteristic curve (AUC) of 0.804 internally and 0.854 externally, with the highest mean AUC among the evaluated RenalCLIP fusion strategies in both cohorts. Pathway ablations examine the contributions of conditional modulation and the direct radiomics residual, while feature permutation highlights the role of tumour texture. These findings support radiomics as a useful complement to RenalCLIP in a small labelled cohort and identify FiLM as an effective approach to integrating their representations for robust renal tumour classification.

---


### 248. [Gap-Free Streaming PCA Beyond Rank-One Updates: Near-Optimal Rates and Applications to Differential Privacy](https://arxiv.org/abs/2609.26508)

**<font color=#1a73e8>作者：</font>** Anming Gu, Syamantak Kumar, Kevin Tian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Streaming principal component analysis (PCA) seeks to recover a leading spectral subspace in a single pass over a data stream. We give a new analysis of the ubiquitous Oja's algorithm [Oja82] for the most general, gap-free variant of this problem, where no eigengap assumptions are made on the underlying mean matrix, complemented by a nearly-matching lower bound. Prior works achieving near-optimal rates for streaming PCA either required gap assumptions [JJK+16, HNWW21], or were limited to rank-one updates [AZL17, Lia23]. Our proof only uses a second moment bound on the individual stochastic updates, bypassing the almost sure bounds needed by prior near-optimal analyses, and the analogous offline matrix Bernstein bound. We also extend our result to a Rayleigh quotient notion of approximate PCA, addressing an open question of [JJK+16]. As our main application, we give gap-free differentially private PCA guarantees for sub-Gaussian data, settling Conjecture 1.1 of [Bro26] up to logarithmic factors.

---


### 249. [Do Vision Model See Like the Brain? A Comparison Across EEG Encoding Model](https://arxiv.org/abs/2609.26512)

**<font color=#1a73e8>作者：</font>** Shashank Baghel, Kshitij Dwivedi, Dinesh Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Convolutional neural networks (CNNs) and vision transformers are both used to model the human visual system, but whether the two architectures diverge at a specific point in network depth is unclear. We compared six CNNs and two vision transformers by computing the Pearson correlation (r) between each model's predicted and measured EEG response at every layer or block, in ten participants viewing 200 natural images. For the transformer models, we also tested four token representations, from the classification (CLS) token alone to CLS combined with all patch tokens. CNNs showed strongest correspondence at the earliest layers, weakening at deeper layers, particularly later in the post-stimulus response. Transformers instead sustained strong correspondence at their deepest blocks, though not at their earliest ones. This advantage depended on token representation: pooled representations gave weaker peak correlations (r approx 0.48-0.51) than representations retaining all patch tokens (r=0.640 for CLIP-ViT-B/32, r=0.656 for DINOv2-ViT-B/14). Controlled comparisons showed architecture, not training objective, drove this effect: MoCo-v1 and ResNet-50 (matched architecture) performed nearly identically (r=0.673, 0.670), whereas CLIP-RN50 and CLIP-ViT-B/32 (matched objective) diverged until patch tokens were preserved. We propose that CNN training's classification bottleneck compresses brain-relevant information at depth, unlike transformers' self-attention and non-classification objectives. A spatial topography analysis showed a common occipital-dominant pattern across all models, indicating these differences reflect signal strength and persistence rather than distinct brain regions. Patch-preserving transformer representations sustain brain-predictive correspondence where CNNs collapse.

---


### 250. [Notes on Fourier-Bessel wavelets](https://arxiv.org/abs/2609.26537)

**<font color=#1a73e8>作者：</font>** Marcel Venturotti, Georgios Exarchakis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> These notes develop the mathematical foundations and construction of a Fourier-Bessel wavelet family inspired by the disk harmonics of Shaqfa et al.[9]. We begin with the relevant properties of Bessel and modified Bessel functions and introduce the wavelet properties required for the construction. We then derive the Fourier-Bessel disk harmonics as solutions to the Helmholtz equation on the unit disk subject to a Neumann boundary condition.
Building on this basis, we construct a wavelet family by applying a Gaussian spatial envelope and introducing a zero-mean correction for the zeroth angular order. We derive the corresponding normalisation constants for $L^2$-based applications and discuss $L^1$-based normalisation for frequency-domain peak consistency. Finally, we derive a closed-form Fourier-domain representation of the resulting wavelets.
The main motivation is the approximately linear spacing, which converges to $\pi$ between consecutive radial eigenvalues. Rather than replacing the conventional dyadic organisation of wavelet families, this construction lays out the foundation to explore whether a more uniform radial frequency allocation can be useful for applications in which broad and balanced frequency coverage is desirable.

---


> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-275](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
