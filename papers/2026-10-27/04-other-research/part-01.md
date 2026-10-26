# 📦 其他研究 | 2026年10月27日

> 本类共 **198** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-198](./part-04.md)

---

### 1. [Rethinking Structured Generation: Can Graph-Based Reasoning Resolve Ambiguity?](https://arxiv.org/abs/2610.31681)

**<font color=#1a73e8>作者：</font>** Ratun Rahman, Atit Pokharel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Structured generation is typically formulated as a deterministic mapping from input to a single structured output. This assumption is fundamentally misaligned with natural language, which often admits multiple structurally distinct yet semantically valid interpretations. As a result, existing methods rely on single-reference supervision that collapses ambiguity into one prediction, leading to unstable and inconsistent outputs under underspecified inputs. We reformulate structured generation as an \textit{ambiguity-aware inference problem}, where the objective is to reason over a set of plausible structured outputs rather than predict a single solution. We show that standard training inherently suppresses valid alternatives, and instead adopt a multi-valid learning framework that preserves ambiguity during optimization. To operationalize this formulation, we construct a candidate space of structured outputs, represent each candidate as a graph capturing entities and their relationships, and perform selection via graph-based reasoning over semantic alignment and relational consistency. This enables principled comparison across competing interpretations beyond token-level likelihoods. Experiments on structured generation benchmarks demonstrate consistent improvements in accuracy, stability, and robustness under varying levels of ambiguity. These results highlight the importance of modeling ambiguity explicitly and suggest a shift from single-output prediction to set-level reasoning in structured generation.

---


### 2. [Multi modal perceived conversation success prediction for spontaneous autistic and non-autistic dyadic interactions](https://arxiv.org/abs/2610.31682)

**<font color=#1a73e8>作者：</font>** Thanushi Withanage, Desi Jones, Noah Sasson 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversation success is important for communication, social bonds, and well-being and is often reduced in autistic-neurotypical conversations. Previous studies have predicted perceived conversation success using acoustic and lexical features in pediatric autism-enriched samples, or using nonverbal behavior in non-autistic group interactions. Other work has characterized prosodic, facial, motor, and turn-taking synchrony in autistic interactions, but has primarily targeted diagnostic classification or group differences. The present study instead predicts participant perceived conversation success from complementary articulatory, facial, acoustic-prosodic, and turn-taking measures across three spontaneous dyadic-interaction datasets including autistic and non autistic individuals. By leveraging multimodal features, we demonstrate that conversational success is inherently multidimensional and requires a multi-faceted analytical framework. Combining these complementary modalities offers the potential to improve prediction of perceived conversation success by capturing information unavailable from any single modality.

---


### 3. [Tradeoff-Aware Territory Design: A Multi-Objective Decision System for Enterprise Customer-to-Seller Allocation](https://arxiv.org/abs/2610.31701)

**<font color=#1a73e8>作者：</font>** Nan Wang, Mitchell Turiel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise customer journeys are shaped not only by product experiences and marketing, but also by recurring resource-allocation decisions. In B2B go-to-market (GTM) organizations, territory carving determines which accounts receive seller coverage, which seller-account relationships are preserved, and how limited field capacity is distributed. Yet the process often remains manual, making it difficult to compare opportunities, value continuity, and evaluate tradeoffs among growth, balance, capacity, and feasibility.
We present a production decision system for tradeoff-aware customer-to-seller allocation in enterprise GTM planning. It integrates three components: a multidimensional account-value layer that combines predictive signals to score opportunity; an observational continuity-valuation layer that estimates the cost of breaking seller-account relationships using a synthetic-control-style counterfactual framework; and a multi-objective optimization layer that allocates coverage to high-value accounts while considering continuity, opportunity balance, and operational constraints.
Deployed as a scenario-based decision-support system, the framework enables planners to inspect and compare allocation tradeoffs. Historical backtesting shows that optimizer-generated scenarios substantially improve assignment compliance while maintaining comparable seller-level opportunity distribution. In production planning, adopted scenarios improved both assignment compliance and opportunity balance relative to the previous baseline. Directing scarce seller capacity toward higher-value accounts also offers incremental revenue potential at enterprise scale. The key contribution is an integrated, inspectable framework that turns territory carving into a governable decision process.

---


### 4. [The Path to NDE 4.0: A Review of Algorithms, Techniques, and Strategies for Autonomous Inspection](https://arxiv.org/abs/2610.31704)

**<font color=#1a73e8>作者：</font>** Ashiqur Rahmana, Venkata Devesh Reddy Seethi, Zachary Kral 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Non-Destructive Inspection (NDI) is a cornerstone of modern quality assurance, critical for ensuring the safety and reliability of infrastructure and manufactured components without causing damage. This paper presents a comprehensive review of the current NDI landscape, analyzing the field through four distinct lenses, namely, computational algorithms, physical techniques, industrial applications, and research objectives. We synthesize a broad range of academic literature to illustrate the rapid evolution from manual, analog interpretation to a digitized, data-centric paradigm known as NDE 4.0. Our analysis highlights the dominance of ultrasound and visual inspection as primary physical techniques, while revealing a significant shift toward deep learning and generative models for automated defect recognition. Despite these technological strides, the industry faces critical bottlenecks, notably the scarcity of standardized open-access datasets and the "black box" nature of AI models, which hinders widespread adoption. By charting these developments and identifying key research gaps, such as the need for explainable AI (XAI) and standardized digital twin protocols, this review offers a strategic roadmap for future research. It concludes that the future of NDI research should focus on the successful integration of intelligent, autonomous fusion of inspection data with advanced sensor technologies into asset lifecycle management.

---


### 5. [Does LeWorldModel Preserve Local Action Geometry?](https://arxiv.org/abs/2610.31716)

**<font color=#1a73e8>作者：</font>** Vasil Vasilev, Siddharth Nayak  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We examine how closely pretrained LeWorldModel (LeWM) reproduces the effects of small action changes. Using matched simulator and model responses, we measure action sensitivity with Gram matrices at three perturbation scales. Across nearly a thousand states from Reacher and OGBench Cube, the most sensitive action directions differ by median angles of about $36^\circ$ and $42^\circ$, respectively, at the smallest scale. Increasing the perturbation tenfold reduces median normalized Gram discrepancy by roughly 70\% on Reacher and 47\% on Cube. Geometry measured in pixels and embeddings varies more across scales than the chosen physical-state geometry. On held-out directions, environment Grams achieve median embedding response errors of 17\% and 28\%, compared with 26\% and 38\% for an isotropic reference with the same trace. LeWM's errors are higher at this scale. These findings support scale-specific evaluation of action sensitivity; its effect on control remains an open question.

---


### 6. [Towards Adversarially Robust Multigraph Neural Networks for Financial Crime Analysis](https://arxiv.org/abs/2610.31718)

**<font color=#1a73e8>作者：</font>** Dennis Heijmans, H. Çağrı Bilgi, Rui Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial transaction networks are naturally represented as multigraphs, where repeated transactions between the same pair of accounts are modeled as distinct edges. Recently proposed multigraph neural network architectures leverage this structure explicitly to achieve a strong performance on anti-money laundering (AML) tasks. However, their robustness to adversaries that manipulate transaction structures to evade detection remains largely unexplored. We present the first scalable framework for structural attacks and adversarial training of multigraph neural networks using node-edge incidence matrices, adapting projected gradient descent and projected randomized block coordinate descent methods to optimize structural perturbations over such matrices. We further introduce a cycle-based regularizer that penalizes changes in the global counts of directed 2- and 3-cycles, providing a structural measure of attack plausibility. Experiments on synthetic pattern-detection and realistic AML datasets show that our learned attacks substantially outperform non-learnable perturbation baselines in reducing detection performance (PR-AUC), while adversarial training consistently improves robustness against these attacks. These results demonstrate that multigraph neural networks are vulnerable to learned structural attacks and that adversarial training provides an effective defense. Our code is available at this https URL.

---


### 7. [End-to-End Differentiable Diffusion Conditioning for Physics-Informed Optimization](https://arxiv.org/abs/2610.31721)

**<font color=#1a73e8>作者：</font>** Ricardo Luna Gutierrez, Vineet Gundecha, Rahman Ejaz 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimizing high-dimensional physical systems under expensive evaluations and complex constraints is a central challenge in science and engineering. In offline model-based optimization (MBO), methods must improve designs using only a fixed dataset and no test-time access to the true objective. However, existing methods typically suffer from conservatism, unconstrained surrogate exploitation, or function as static inference-time samplers that cannot refine candidates against precise physical objectives. In this paper, we propose Differentiable Diffusion Conditioning (D2C) for offline MBO, which leverages the fact that deterministic sampling makes the reverse denoising chain differentiable with respect to the conditioning signal. D2C turns a frozen conditional diffusion model into an end-to-end gradient-based optimizer by directly optimizing conditioning variables at test time via gradients from frozen surrogate objectives and physics-informed penalties backpropagated through the reverse chain. We implement this idea in a composed proposer-evaluator framework and evaluate it on laser pulse optimization for inertial confinement fusion, sustainable data-center workload scheduling, and four Design-Bench tasks. Our method achieves the strongest results on the two real-world tasks and the best average rank across four Design-Bench tasks.

---


### 8. [Cognitively Constrained Partners for Zero-Shot Coordination in Real-Time Partitioned Control](https://arxiv.org/abs/2610.31726)

**<font color=#1a73e8>作者：</font>** Ash Simmons, George De Ath, Richard M. Everson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Effective human-machine teaming requires agents that coordinate with unpredictable human partners. Reinforcement learning from live human feedback or large behavioural datasets is expensive, while purely simulated training overfits to artificial conventions and fails at Zero-Shot Coordination with real people. We propose a framework for training teaming agents against Cognitively Constrained Partners: simulated partners whose diversity emerges from procedural constraints grounded in human physiological literature, specifically reaction delays and perceptual limitations, rather than from reward shaping or historical training checkpoints. In a modified Lunar Lander environment, we report preliminary evidence that these partners play more like real people than unconstrained agents do, and that agents trained against them match the strongest cross-play baselines while being the only ones whose performance does not depend on how their training partners were generated. We also describe a human-participant study designed so that its rankings can be compared directly against cross-play, testing how well that standard evaluation predicts real human-agent teaming.

---


### 9. [ConsMSA: Semantic Distribution Consistency Learning for Multimodal Sentiment Analysis](https://arxiv.org/abs/2610.31731)

**<font color=#1a73e8>作者：</font>** Pan Wang, Lipeng Ke, Huajun Ying 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal sentiment analysis (MSA) aims to predict human sentiments by integrating signals from different modalities such as text, video, and audio. However, raw multimodal sequences often suffer from semantic inconsistency--exhibiting redundancy or conflicts within and across modalities--which hinders robust understanding and increases computational cost. To this end, we introduce ConsMSA, which explicitly formalizes semantic distribution consistency across both $\textit{intra}$- and $\textit{inter}$-modality, providing a consistency-aware mechanism for robust and efficient multimodal sentiment prediction. Specifically, ConsMSA projects multimodal token features into a shared sentiment space to compute an Intra- and Inter-modality Consistency Score ($I^2CS$). By coupling this score with predictive relevance, we formulate consistency-aware importance signals that are utilized: (i) as a consistency regularizer to align latent distributions during training, (ii) to derive semantic-aware weights for adaptive multimodal token reweighting, and (iii) as a practical criterion to prune redundant or conflicting tokens. Extensive experiments on CMU-MOSI, CMU-MOSEI, and CH-SIMS demonstrate that ConsMSA achieves state-of-the-art performance while remaining robust under aggressive token compression--retaining only 10% of tokens yields comparable accuracy. These results establish semantic distribution consistency as a promising foundation for synergizing predictive robustness with computational efficiency.

---


### 10. [Toward an Agentic AI Approach to Public Health Data Collection](https://arxiv.org/abs/2610.31746)

**<font color=#1a73e8>作者：</font>** Xueyi Zhang, Hongru Du, Ensheng Dong  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Disease surveillance increasingly integrates automated data collection, yet predefined sources and procedures require manual adaptation as reporting practices change. We explore agentic artificial intelligence (AI) as an approach to coordinating surveillance data collection across heterogeneous sources. Specifically, we built a multi-agent framework that integrates source discovery, source assessment, evidence structuring, event linking, and validation. Three retrospective applications illustrate its promise. The workflow recovered all 13 individual cases in a hantavirus outbreak, with links to 85 distinct publisher domains compared with 28 in the reference benchmark, reconstructed Canadian measles counts with a final total 0.33% below the national reference and higher cumulative counts on 79.8% of comparable days, and increased the share of days with recent Sierra Leone mpox reports from 28.2% to 65.6% by incorporating attributed media. These demonstrations also reveal limitations in record completeness and accuracy, while prospective gains in timeliness remain untested. We envision agentic AI as a complementary layer of public health data infrastructure, coordinating evidence-linked collection under surveillance goals and standards defined by public health professionals.

---


### 11. [AudioLift: Audio-Driven Single Image to Full-Head Gaussian Avatar via Multi-view Video Generation](https://arxiv.org/abs/2610.31747)

**<font color=#1a73e8>作者：</font>** Zhuoyuan Jiang, Weijie Lyu, Xiaoyuan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing 3D talking avatar methods mainly rely on parametric face models including 3DMM or FLAME, whose compact motion representations limit their ability to synthesize extreme expressions and to model accessories such as headwear. We introduce AudioLift, a two-stage framework that uses generated multi-view videos as the intermediate representation for audio-driven avatar generation without parametric face models or per-instance optimization. Our framework combines a synchronized multi-view video generation stage with an inconsistency-robust Gaussian reconstruction stage to recover coherent full-head geometry from a single portrait image. Extensive experiments demonstrate that AudioLift produces 3D talking avatars capable of capturing more extreme facial expressions than existing methods, with improved geometric completeness and strong multi-view consistency across the full $360^\circ$ viewing range.

---


### 12. [SyncVid: World-Equivariant Diffusion for Synchronized Video Generation](https://arxiv.org/abs/2610.31765)

**<font color=#1a73e8>作者：</font>** Farhad G. Zanjani, Animesh Karnewar, Fatih Porikli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating multiple videos of a dynamic scene from a single reference video requires synthesizing both observed and unobserved content consistently across viewpoints. Existing camera-control methods for video diffusion typically rely on architectural mechanisms, including camera embeddings, cross-view attention, and geometric conditioning. Although effective for static scene content, these approaches often struggle with the fine-grained, dynamic geometry that must remain coherent across views and over time. We synchronize the diffusion process itself by sampling the Gaussian noise prior in a canonical 3D space derived from the source video and rasterizing it into target cameras, rather than sampling independently in each 2D image plane. Our method, SyncVid, lifts a monocular video into a canonical 4D representation, associates noise with scene geometry and unseen space, and rasterizes the resulting structured noise into arbitrary views. Because rendering can introduce local correlations, we further propose a cross-view-consistent whitening procedure that decorrelates neighboring pixels while preserving correspondence across views. The structured noise serves as the diffusion prior for a LoRA-adapted pretrained video diffusion model, requiring no architectural modifications. By enforcing spatiotemporal and cross-view coherence at the source of stochasticity, SyncVid generates synchronized videos and improves both perceptual quality and cross-view consistency in our experiments. Project page: this https URL.

---


### 13. [Not All Retained Clients Are Equal: Client Selection for Federated Unlearning](https://arxiv.org/abs/2610.31786)

**<font color=#1a73e8>作者：</font>** Thanh Linh Nguyen, Quoc-Viet Pham  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated unlearning (FU) aims to remove a designated target client's influence from a trained model without the prohibitive cost of retraining from scratch. Existing methods largely treat unlearning as a post-hoc, stateless operation, overlooking that client influence is path-dependent: contributions made during training, particularly during critical learning periods (CLPs), can have disproportionate and persistent effects. Moreover, knowledge overlap and intermittent client availability make relying on all retained clients inefficient and impractical. We introduce PDF, a path-dependent client-selection framework based on the insight that retained clients are not equally valuable for unlearning. During training, PDF maintains lightweight, target-agnostic, CLP-weighted histories summarizing each client's accumulated update direction and global-model alignment. Upon an unlearning request, these histories identify and rank retained clients that are globally informative yet weakly coupled to the target, enabling retraining-based unlearning with only the top-$k$ clients over a small number of rounds. Experiments on FMNIST, CIFAR-10, and CIFAR-100 under IID and non-IID settings show that PDF achieves effective forgetting and strong retained utility with substantially fewer retained clients. In particular, PDF achieves $0\%$ forgetting accuracy with retraining-like MIA AUC on non-IID CIFAR-10, improves retained accuracy by up to $6.91$ percentage points over the strongest competing FU baseline on CIFAR-100, and reduces communication by approximately $69\%$ and computation by $57$--$61\%$ relative to Retrain.

---


### 14. [PnP*: A certifiable solver for Perspective-n-Point](https://arxiv.org/abs/2610.31797)

**<font color=#1a73e8>作者：</font>** Bang-Shien Chen, Caitrin E. Eaton, David M. Rosen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Estimating a camera pose from 3D-2D correspondences - Perspective-n-Point - is one of the most fundamental problems in computer vision. Existing methods either solve a minimal problem or replace the objective with an easier one. Surprisingly, no scalable certifiable solver for the actual Maximum Likelihood Estimation (MLE) exists. We propose PnP*, the first practical solver that guarantees efficient computation and returns a certifiable globally optimal solution. We prove that the underlying convex relaxation is exact under moderate noise, which to our knowledge is the first stability guarantee for any relaxation for the MLE of PnP. Furthermore, we reduce the relaxation by exploiting chordal sparsity pattern and quotient ring reduction such that the relaxation is tractable and scalable. The stability and scalability results are verified numerically, as PnP* returns a provably correct camera pose at over 10 Hz.

---


### 15. [StackGen3D: Stable 3D Block Stack Generation from Multiview Silhouettes](https://arxiv.org/abs/2610.31803)

**<font color=#1a73e8>作者：</font>** Xiaopeng Zhang, Luzhe Sun, Yiqing Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating physically stable 3D structures from visual specifications requires resolving geometric ambiguity while accounting for physical interactions among objects. We present StackGen3D, a framework for generating stable block assemblies conditioned on a given block inventory and three orthographic silhouettes. Our approach consists of two stages. First, we develop a physics-informed graph neural network (PI-GNN) that models support relations between blocks and serves as a fast stability predictor for curating a diverse dataset of stable structures. Second, we train a conditional flow-matching model on this dataset to capture the multimodal distribution of block configurations consistent with the target silhouettes. At inference time, lightweight geometric selection and refinement reduce inter-block penetration without physics simulation. Preliminary experiments show that the PI-GNN generalizes from simple stacks to complex structures substantially better than a parameter-matched multilayer perceptron. For structure generation, Best-of-10 selection improves physical stability from 45.3% to 72.4% while achieving a silhouette IoU of 0.970. These results highlight the potential of combining relational physical reasoning, scalable data curation, and conditional generative modeling for creative 3D assembly.
Project website: [this https URL](this https URL)

---


### 16. [Patronizing and Condescending Language Detection in English and Mandarin](https://arxiv.org/abs/2610.31808)

**<font color=#1a73e8>作者：</font>** Xinyi Vicky Xiang, Catherine Qingyun Wang, Paula Cortés Lemos  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Patronizing and condescending language (PCL) is a form of harmful language that belittles and assumes pity for vulnerable groups, reinforcing negative societal stereotypes. However, unlike overt hate speech, it is often difficult to detect, even for human judges. This paper proposes a system for the automated detection of PCL. Our first approach uses static word embeddings and a convolutional neural network for classification, while our second approach uses pre-trained BERT embeddings fine-tuned for the PCL task. Our second approach was considerably more successful, and achieved an F1 score of 0.528 over the development set.

---


### 17. [SILMARILS-MV: Information-Theoretically Secure Multi-Verifier Signatures with Dealer-Free Key Issuance and Linear Aggregation for Permissioned Blockchains](https://arxiv.org/abs/2610.31814)

**<font color=#1a73e8>作者：</font>** Khadijeh Bagheri, Hassan Khodaiemehr, Chen Feng  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Permissioned blockchains authenticate transactions, votes and quorum certificates with computationally secure signatures, and post-quantum replacements inflate consensus traffic by orders of magnitude. Information-theoretic alternatives have required a trusted authority, quantum channels, per-signature interaction, or single-use keys with bounded transfer. We present SILMARILS-MV, a multi-verifier unconditionally secure signature in which a signature is the vector $\alpha = A\,e(m)$ and each verifier holds a secret functional $c_i = \Gamma^T \lambda(x_i)$ derived from virtual anchors $\Gamma$ that nobody learns. Against unbounded adversaries corrupting up to $\omega$ verifiers and any signers, and observing every decision, an honest verifier accepts a forged or invalid signature with probability at most $Q/q + 1/(q-1)$, a bound that is tight in its leading term. The scheme is strongly unforgeable, non-repudiable, transferable across unboundedly many hops, and linearly aggregatable. Keys are issued by the validators through perfectly secure MPC for $t < n/3$, without broadcast. To scale, we let the committee itself sign: in threshold notarization, finality certificates have constant size $32(\omega+1)$ bytes and per-validator issuance cost no longer depends on $n$. Arbiter-verified keys give clients 32-byte signatures, robust redistribution supports membership changes and share refresh, and verifiers can be enrolled retroactively. A certificate verifies in 2.4 microseconds. In an analytic normal-case model at 1000 validators, threshold notarization needs 71 KiB of authentication traffic per validator per block, 22x less than ML-DSA-44 for admitted verifiers. In a Rust HotStuff prototype with 100 validators, SILMARILS-MV commits 2.8x more transactions per second than ML-DSA-44 with 67x less cryptographic CPU, and Monte-Carlo attacks match the bounds.

---


### 18. [What the Query Remembers: Query Abstraction Governs Lexical and Dense Retrieval of Classical Arabic Poetry](https://arxiv.org/abs/2610.31821)

**<font color=#1a73e8>作者：</font>** Omar Farouk Zouak, Selma Mani, Larbi Said Chikh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How well a poetry archive can be searched depends on what the user still remembers, not only on what the model understands. We show this for Classical Arabic poetry, benchmarking nine dense encoders and BM25 over two corpora, three indexing modes and two evaluation protocols. Which retriever wins is governed by how much of a poem's wording the query still carries. On tip-of-the-tongue queries BM25 leads every dense encoder, including an 8B state-of-the-art model (0.746 vs. 0.717 Recall@5); on abstract queries it falls to eighth out of ten (0.392 vs. 0.748). Editing the wording of the same queries shows that this ranking largely reflects query composition: adding one remembered half-verse raises BM25 by 38 points, rewriting the quoted words by hand leaves BM25 level with the 8B encoder, and BM25's sensitivity to remembered wording is significantly steeper than that of the strongest dense encoder. The same axis controls explanation augmentation, whose effect swings from +37 to -39 points. The mechanism splits by system type: lexical containment predicts BM25's behaviour, while embedding proximity predicts dense encoders. Finally, the field's two standard protocols, known-item retrieval and thematic relevance, dissociate on the same systems, a result reproduced by two blind human annotators and by two open-weights judges, one of them under a rubric with no literal-match criterion. A benchmark that reports one protocol, or one query register, can give a materially wrong picture. Code and data are available at this https URL.

---


### 19. [SPECMEM: Accelerating Agentic Tool Calling via Live Memory Management](https://arxiv.org/abs/2610.31840)

**<font color=#1a73e8>作者：</font>** Zihe Song, Wenting Zhao, Ye Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tool-calling agents are mostly optimized for accuracy; in deployment, however, their growing cost is latency: every tool call is decoded autoregressively. Speculative decoding accelerates this without changing the output, and retrieved past calls make strong drafts under real use, where each user's behavior tends to repeat. Yet existing systems keep no cross-session memory, or build the draft store once and never update it. We propose SpecMem, a tool-call memory kept alive and managed throughout deployment: verified calls are written back online into bounded per-user stores with LRU eviction, and a side-effect gate defers irreversible calls until verification confirms. On multi-session, multi-user query streams served by three open-weight models, a frozen store steadily loses acceptance while SpecMem holds it: a 27% gap in mean accepted tokens (+11% to +34% across benchmarks, tracking how much novel work arrives after the store is built) and up to 1.74x wall-clock speedup. Ablations attribute the gain almost entirely to keeping the store live; local per-user scoping adds no acceptance but closes a measured cross-user leakage channel, and gating on declared side effects, rather than on retrieval confidence, is what eliminates irreversible mistakes.

---


### 20. [IFC-SSL-Bench: Benchmarking Self-Supervised Learning for Annotation-Efficient Multispectral Imaging Flow Cytometry](https://arxiv.org/abs/2610.31848)

**<font color=#1a73e8>作者：</font>** Angelo Jovin Yamachui Sitcheu, Roxana-Teodora Fetescu, Thomas Lautenschlager 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Imaging Flow Cytometry (IFC) generates large multispectral datasets, yet the need for expert annotations bottlenecks the development of supervised deep learning models. While Self-Supervised Learning (SSL) offers a solution, its application to IFC remains fragmented and lacks systematic benchmarking. To address this, we present IFC-SSL-Bench, a modular framework for evaluating SSL in IFC. We benchmark six SSL approaches across four backbones on two heterogeneous datasets. By assessing downstream classification performance across annotation regimes of the training sets (1%-100%), we quantify annotation efficiency and identify optimal configurations for high-dimensional biological imaging. SSL matches the performance of fully supervised baselines trained on 100% of annotated data while using as little as 5% of annotations for morphological classification, with advantages in low-data regimes below 5%. Across both datasets, the contrastive approach MoCo-v2 paired with ConvNeXt backbones emerged as the top-performing configuration, with ConvNeXtV1-T best for immunological synapse classification and ConvNeXtV2-T for morphological classification. We identify a clear pattern in transfer dynamics: ImageNet initialization benefits morphological classification, consistent with its visual similarity to natural images, whereas random initialization better captures the more domain-specific immunological synapse classification. SSL elevates class-specific F1-scores by over 35 percentage points for structurally complex classes at 1% of annotated data. We synthesize these insights into a unified set of guidelines for deploying self-supervised workflows in high-throughput IFC, and release the benchmark as a resource for future work.

---


### 21. [Cautious Conflict-Free Inverse Gradient Methods](https://arxiv.org/abs/2610.31855)

**<font color=#1a73e8>作者：</font>** Damian Hattler, Qiang Liu, Nils Thuerey  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Partial differential equations (PDEs) are indispensable tools for modeling complex phenomena in physics and engineering. Physics-Informed Neural Networks (PINNs) have emerged as a powerful alternative to traditional numerical solvers by directly incorporating physical constraints into neural network loss functions. Despite their advantages, PINN training requires multi-objective optimization, which often leads to significant gradient conflicts among boundary, initial, and residual loss terms. The Conflict-Free Inverse Gradient (ConFIG) method addresses these conflicts; however, integrating ConFIG with adaptive optimizers such as Adam introduces a critical vulnerability: the conflict-free direction generated by ConFIG is further processed by the optimizer, and the resulting weight update may no longer be conflict-free with respect to the task gradients. To address this issue, Cautious ConFIG is proposed as a concise three-line extension to the ConFIG algorithm that empirically restores the conflict-freeness guarantee prior to the weight update. The method is evaluated on three PINN benchmarks: the 1D Viscous Burgers' equation, the 1D Nonlinear Schrödinger equation, and the 2D Kovasznay flow. Experimental results demonstrate consistent performance improvements over the standard ConFIG baseline. Additionally, the stabilizing effect of cautious masking and its reaction to conflict severity, task number, and optimizer lag are investigated using a simple toy system.

---


### 22. [Mining Frames: Association Rule Mining as an Unsupervised Framework for News Framing Detection](https://arxiv.org/abs/2610.31874)

**<font color=#1a73e8>作者：</font>** Hager Hesham Mustafa  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Computational framing analysis is dominated by supervised classifiers that require large annotated corpora and predefined frame taxonomies, limiting their use for non-English languages, novel events, and low-resource settings. This paper presents Association Rule Mining (ARM) as an unsupervised, annotation-free framework for news framing detection. Each document or sentence is treated as a transaction of lexical items, and high-lift co-occurrence rules are read as candidate framing signals (Gamson and Modigliani's condensing symbols), confirmed in context by journalist-researchers. The primary validation is Framing Gaza: 25,512 English-language articles from 16 US, UK, French, and German outlets covering the first year of the Gaza war (October 2023 to October 2024), analyzed with Apriori (mlxtend), platform-weighted support, POS-filtered n-grams, and lift-based scoring. ARM inductively surfaces interpretable patterns without predefined categories: a cross-platform military frame, {israeli, strike} to {kill}, appears as a closed rule in 14 of 16 outlets, and a month-by-month analysis recovers event-driven framing pivots (e.g., the April 2024 World Central Kitchen strike) with no prior event labeling. A systematic headline-body divergence is identified, with headlines carrying concentrated, high-lift editorial framing and body text reproducing institutional, procedural language. A methodological validation on the Seven Days project (1,575 Arabic articles on the 2026 Iran war) shows that FP-Growth enables sentence-level analysis with far lower memory overhead. Findings were validated through editorial uptake: two published investigative stories (Daraj Media; Saheeh Masr). Preprocessing code is released openly; the full pipeline is documented but withheld to preserve operational deployability.

---


### 23. [Effectiveness of Curriculum Learning Depends on Reward Sparsity and Competing Optima](https://arxiv.org/abs/2610.31884)

**<font color=#1a73e8>作者：</font>** John J. Vastola, Ann Huang, Satpreet H. Singh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While animals and people tend to learn a task more quickly and reliably when they first train on simpler versions of it, curriculum learning's effectiveness in artificial settings varies, and appears substantially greater in reinforcement learning than in supervised learning. In this work, we construct and analyze a minimal model of policy learning to better understand why. We consider an open-loop, episodic target interception task whose parameters---especially how close the agent must be to the target to receive an informative reward signal---can be chosen so that the agent either receives informative rewards frequently ('dense' rewards) or rarely ('sparse' rewards). We mathematically and numerically analyze the dynamics of REINFORCE-based policy learning in both cases. In the dense reward case, curricula have only marginal benefits; in the sparse case, curricula can be required for learning to occur at all. We find that this is especially true when the agent has the conflicting goals of minimizing effort and accumulating high reward, since this can produce distinct reward landscape optima which compete with one another. Our characterization of useful curricula in this setting indicates that they address two issues: they (i) make rewards less sparse to speed up learning, and (ii) shape the reward landscape to steer agents away from bad local optima.

---


### 24. [Scaling Transformer Energy-based Models For High Quality Image Synthesis](https://arxiv.org/abs/2610.31889)

**<font color=#1a73e8>作者：</font>** Jungsoo Lee, Alexi Gladstone, Yilun Du  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Energy-Based Models (EBMs) are a flexible class of generative models that decouple probabilistic modeling from the generation process. This decoupling directly enables compositional generation and inference-time scaling, where sample quality can be refined simply by increasing sampling steps. However, severe challenges in high-dimensional sampling and training instabilities with deep architectures have restricted EBMs to low-dimensional regimes. To resolve these bottlenecks, we introduce the Transformer Energy-Based Model (TEM), a scalable transformer energy function operating entirely within a latent space. On top of this backbone, we extract energies at multiple layers and sum them, composing complementary constraints from local texture to global semantics. Furthermore, two components make this high-quality at scale: Positive Representation Alignment (PRA), which supervises TEM's intermediate representations with a vision foundation model, and advanced sampling strategies that improve sample quality at inference. TEM-XL achieves an FID-50K of 3.82 on class-conditional ImageNet 256$\times$256 without classifier-free guidance, showing that a contrastive EBM can generate high-fidelity images. On ImageNet 512$\times$512, TEM achieves an FID-50K of 8.24, demonstrating that the approach scales to higher resolution. We further validate the core promises of EBMs: compositional generation, zero-shot inpainting, and out-of-distribution detection.

---


### 25. [Automated Nucleus Segmentation in Histology Images: An Attention U-Net Approach with Comprehensive Preprocessing and Inference Pipelines](https://arxiv.org/abs/2610.31902)

**<font color=#1a73e8>作者：</font>** Akshat G, Divyansh Gupta, Tusar Kanti Mishra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Objectives: In the area of digital pathology, nucleus segmentation is an essential step for quantitative analysis; however, high nuclear density and staining heterogeneity in histology images pose a great challenge.
Methods: This study implements a lightweight Attention U-Net model on the MoNuSeg 2018 dataset to overcome these challenges. The proposed pipeline integrates comprehensive image and mask preprocessing, including stain deconvolution and multi-pass mask smoothing, with a high-fidelity overlapping patch-stitching strategy during inference on high-resolution images.
Results: The model achieved an Intersection over Union (IoU) score of 0.8745 on full-resolution, unseen test images. This result demonstrates the effectiveness of attention mechanisms in enhancing feature localization and validates the stitching methodology for generating seamless and accurate segmentation maps.
Conclusion: Attention U-Net is an effective and competitive method for automated, scalable nucleus delineation in challenging clinical contexts.

---


### 26. [PixGR: Pixel-Space Generative Decoding for Fast Feed-Forward 3D Reconstruction](https://arxiv.org/abs/2610.31908)

**<font color=#1a73e8>作者：</font>** Ranran Huang, Wenjing Bian, Weixun Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present PixGR, an efficient framework that integrates lightweight pixel-space generative modeling into feed-forward 3D Gaussian reconstruction to model scene uncertainty. Context observations are encoded once into a scene latent representation, which conditions generative decoding from noisy target views to produce a shared 3D Gaussian representation. We formulate this process using pixel-space flow matching, enabling end-to-end optimization of 3D reconstruction with direct pixel-space generative supervision through differentiable rendering. This avoids VAE-based latent compression and error propagation inherent in previous two-stage pipelines. To preserve feed-forward efficiency, PixGR caches the scene representation and performs iterative inference using a lightweight DiT decoder. Experiments demonstrate that PixGR outperforms regression-based approaches in challenging sparse-view settings, particularly with widely spaced observations and view extrapolation. Meanwhile, it maintains sub-second inference and remains competitive with substantially heavier pretrained generative models. Our project page is available at this https URL.

---


### 27. [Topological Equivalence of Spectral and Density Cluster Hierarchies](https://arxiv.org/abs/2610.31909)

**<font color=#1a73e8>作者：</font>** Sajjad Hashemian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We compare two canonical ways to recover hierarchical clustering from an underlying density $f$: the \emph{density cluster tree} given by connected components of superlevel sets $\{f\ge\lambda\}$, and a \emph{spectral hierarchy} obtained by applying single linkage to diffusion distances induced by a Laplacian operator. We give conditions under which, at an appropriate diffusion time, the diffusion hierarchy is \emph{topologically equivalent} to the density cluster tree up to a monotone rescaling of heights. It further shows that a $k$-NN graph implementation inherits this equivalence from uniform approximation of diffusion distances, yielding a finite-sample reduction from spectral graph constructions to density-level-set topology.

---


### 28. [Decode Late, Multiply Once: Rethinking the Dot Product for Quantized Weights](https://arxiv.org/abs/2610.31913)

**<font color=#1a73e8>作者：</font>** Jonathan Tapson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large neural networks are increasingly deployed with 1-4 bit weights and 16- or 32-bit activations, yet their dot products still use one multiplier per element. We show that a length-n dot product with k-bit weight codes can be computed with n+2^k additions and at most 2^k decodes and 2^k multiplications. Each weight code is used directly as an address offset that selects one of 2^k accumulators; each activation is added into the selected accumulator; and the accumulated sums are decoded and multiplied only once, at the end, in a fused decode-and-multiply step. The decoded weight vector is never formed. The refactoring is exact for integer arithmetic, works with integer or floating-point operands and with arbitrary, including nonlinear, decoders, and extends to group-wise scales and to matrix and tensor products. The multiplier count falls by n/2^k, while total arithmetic energy improves by a smaller, bounded factor that we quantify with a cost model. We describe a scatter-accumulate processing element (SA-PE) that replaces the MAC unit in a weight-stationary systolic array, with a load/stream/reduce/drain schedule in which a small, time-shareable multiplier runs only 2^k times per tile. Because decoded weights are not stored, local weight memory shrinks by up to w_d/k for w_d-bit decoded weights. An RTL implementation synthesized for FPGA and compared with a matched MAC array shows that an unshared SA-PE is larger than a MAC PE, and that the saving appears when the reduction multiplier is shared across PEs. Software models confirm exact integer equivalence and floating-point error no worse than the conventional pipeline. We do not claim the underlying identity is new, and we discuss related work on weight sharing and lookup-based kernels.

---


### 29. [Incomparable Minima in Agent Tool Authorization](https://arxiv.org/abs/2610.31914)

**<font color=#1a73e8>作者：</font>** Xin Xu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> An agent that needs a tool needs authority to call it, and every proposal for governing that authority has to answer one question: of two grants that both let the agent finish a task, which one is smaller? Over-privilege benchmarks score agents against this answer, and permission solvers compute it. We check the question against the authorisation tables that Microsoft and Google publish, covering 22,305 Microsoft Graph endpoint bindings and 23,852 Google API methods, on tasks generated from each table's own resource structure. For 29.8-33.3% of Graph tasks and 3.2% of Google resource tasks the question has no answer, because the minimal sufficient grants form an antichain, a set of grants none of which authorises a subset of what another does. In its two main authorisation modes, Microsoft's shipped privilegeLevel rates 67.4-74.4% of these incomparable pairs equal. Google ships no such scale, so on Google we apply a reconstruction of the FORTIS privilege ladder, which rates 90.7-98.7% equal. Applying the same reconstruction to Graph attributes much of that difference to the scale rather than the corpus: its form based on the HTTP verb alone rates 92.0% of Google pairs and 89.0-92.0% of Graph pairs equal. Four risk measures (operations, writes, services reached, administrative surface) order 28.7% of incomparable Google pairs and 15.7-23.4% of Graph pairs in opposite directions, so for those pairs the ranking has no measure-independent answer. Offered pools of minimal and larger grants, 6 frontier models pick a minimal grant on 99.0% of 1,708 decisions, a grant smallest under all four measures on 66.7%, and on 22.1% a grant that another option matches or beats on every measure. We propose that benchmarks report which minimal grant an agent chose and that deployments show the alternatives to whoever approves the grant.

---


### 30. [Not an Accident: Exploiting Safety Filter Inadequacy in Humanoid Robots](https://arxiv.org/abs/2610.31923)

**<font color=#1a73e8>作者：</font>** Tiffany Bao, Shangtao Li, Yifan Sun 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As humanoid robots move from research laboratories toward deployment in human-centered environments such as homes, hospitals, and warehouses, safe operation around nearby people and objects becomes a fundamental requirement. Safety filters have emerged as a promising technique to address this challenge by providing mathematical guarantees that generated control actions do not result in collisions.
This paper shows that these guarantees hold only when the safety parameters are configured correctly. However, correct parameter configurations are task- and environment-specific, and no general method exists to determine them across diverse deployments. As a result, safety filters shipped with humanoid robots can fail after deployment in specific scenarios. We show that attackers can exploit these failures through only normal user interactions without any additional privileges or capabilities. To demonstrate this risk, we present goal insertion attacks and develop SIREN, an automated tool that identifies vulnerable inserting goals for a given task and environment. Experimental results show that SIREN identifies attacks in all vulnerable scenarios in the SPARK dataset. Compared with a baseline approach, SIREN discovers three times as many attacks. We also show that SIREN is able to generate attacks against a real humanoid and cause it to collide while executing tasks. These results demonstrate that current safety filters introduce exploitable vulnerabilities that can cause safety violations, which reveals that existing safety mechanisms can themselves become a source of safety risk for humanoid robots.

---


### 31. [Towards Trustworthy AI-Enabled Emergency Medical Dispatch: Uncertainty-Aware Ambulance Travel Time Estimation](https://arxiv.org/abs/2610.31944)

**<font color=#1a73e8>作者：</font>** Muhammad Adil Abid, Johan Holmgren, Fabian Lorig 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Emergency medical dispatch increasingly relies on AI-enabled decision support systems when making ambulance dispatch decisions. In this process, accurate ambulance travel time estimates are essential for timely resource allocation and prehospital care. However, existing ambulance travel time estimation approaches typically produce only single point predictions. Consequently, they do not indicate how reliable an individual estimate is or how much uncertainty it carries. This limitation is particularly problematic in safety-critical emergency medical service dispatch operations, where trips with similar expected travel times may exhibit substantially different levels of uncertainty. Furthermore, real-world ambulance trip logs may contain domain-specific artefacts, such as co-located healthcare facilities and physically implausible travel speeds. These artefacts can degrade point prediction accuracy and affect the prediction task on which subsequent uncertainty estimation depends. To address these challenges, we propose an uncertainty-aware methodology for ambulance travel time estimation and evaluate it through a retrospective real-world scenario study using two years of ambulance trip data from the Skåne region in Sweden. The proposed methodology moves beyond average-case point predictions by generating context-adaptive prediction intervals with stable empirical coverage across the evaluated operationally important contexts. The resulting prediction intervals provide explicit information about predictive uncertainty that can support more transparent and risk-sensitive ambulance dispatch decision-making.

---


### 32. [LOCI: Localized Continuous Control for Multi-Subject Image Editing](https://arxiv.org/abs/2610.31950)

**<font color=#1a73e8>作者：</font>** Sai Vidyaranya Nuthalapati, Shlok Kumar Mishra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent instruction-following image editors such as Flux.1-Kontext enable text-driven editing but lack fine-grained control over where and how much an edit is applied. Existing approaches provide either continuous but global control or spatially localized editing at a fixed strength. To our knowledge, none jointly supports explicit spatial localization, continuous per-region strength, and independent simultaneous control of multiple subjects. We present LOCI (LOcalized Continuous control for multi- subject Image editing). Given a multi-subject image with per-subject regions and instructions, LOCI edits each subject at an independently chosen, continuously adjustable strength, for instance gradually aging one person while adding a beard to another with minimal cross-region leakage. LOCI pairs subject-level attention binding for spatial isolation with a Regional LoRA layer that replaces the LoRA's scalar coefficient with a per-token scaling vector aligned to the spatial layout. A single adapter is trained at one suppression point, and continuous edit strengths follow by rescaling its regional residual at inference. Experiments on multi-subject scenes demonstrate that LOCI achieves strong edit fidelity with significantly reduced cross-region interference compared to baselines, while maintaining continuous control over edit strength

---


### 33. [STEP: Surgical Point Tracking from Sparse Endpoints and Pseudo-trajectories](https://arxiv.org/abs/2610.31951)

**<font color=#1a73e8>作者：</font>** Bing Fan, Anwesa Choudhuri, Zhongpai Gao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surgical point tracking requires persistent correspondence through tissue deformation and occlusion, yet dense trajectory annotations are costly to obtain. We present STEP, a two-stage framework that learns from surgical video and sparse physical endpoints. First, a frozen offline teacher generates candidate trajectories, and temporal reversibility and stereo consistency select dense supervision for a causal student. Second, a robust physical endpoint loss anchors terminal correspondence, while a round-trip loss constrains temporal consistency. A gradient-free prefix exposes training to accumulated drift, while a final differentiable window bounds activation memory. The trained tracker processes a single RGB stream with fixed weights. In STIR-to-VL-SurgPT transfer, temporal-stereo union selection reduces endpoint error by 7.0% relative to unfiltered trajectories. On a post-hoc diagnostic of 29 VL-SurgPT clips excluded from the endpoint-training manifest, STEP reduces endpoint error from 31.52 to 16.80 pixels relative to dense-label fine-tuning. These results support combining curated trajectories with physical observations to train surgical point trackers.

---


### 34. [Beyond Heuristics and Commercial Navigation: An AI-Augmented Decision-Support for Ambulance Travel Time Estimation](https://arxiv.org/abs/2610.31968)

**<font color=#1a73e8>作者：</font>** Muhammad Adil Abid, Johan Holmgren, Fabian Lorig 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate ambulance travel time estimation is critical for emergency medical dispatch, yet existing decision-support practices often rely on static lookup tables or simplified assumptions regarding how ambulance travel time differs from ordinary passenger-car travel. For instance, they assume ambulances simply travel a fixed percentage (e.g., 5%) faster than ordinary passenger cars. However, such assumptions are rarely validated using real ambulance operational data and may fail to capture the effects of trip priority, temporal context, and origin-destination. We address these limitations using historical ambulance trips from the Skåne region in Sweden. Our analysis reveals that ambulance travel times vary substantially by hour, day, and trip priority, and that commercial navigation systems fail to capture emergency-specific dynamics. We contribute a machine learning system to more accurately estimate ambulance travel time. To make the system interpretable, we explored SHapley Additive exPlanations and permutation importance techniques to ensure that our system captures operationally meaningful patterns.

---


### 35. [Reproducible Evaluation as the Substrate for Safe Prompt Compression in Production Agents](https://arxiv.org/abs/2610.31972)

**<font color=#1a73e8>作者：</font>** Prabal Vashisht, Zheng Hu, Ying Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating conversational agents that act on live, mutable enterprise data is hard: replayed sessions drift as backend state changes, and a benchmark built today can silently go stale as the data it describes moves on. We present an offline evaluation harness for a production conversational agent that stays reproducible despite the live data it operates on changing, and that can be regenerated on demand once it goes stale. We then use this harness as the fitness function for GEPA-based prompt optimization under a correctness gate that guards against reward hacking. Applied to a production merchant-facing agent, correctness-gated compression shrinks the agent's full prompt surface by 3.5-7.6% without regressing held-out task correctness, consistently across three independent subject-model families, and for one, correctness measurably improves.

---


### 36. [Spectra: Multi-Scale Implicit Decomposition for Deepfake Detection](https://arxiv.org/abs/2610.31979)

**<font color=#1a73e8>作者：</font>** Dhananjaya Jayasundara, Kartik Narayan, Vishal M. Patel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deepfakes increasingly undermine trust in digital media, yet existing detectors often struggle to generalize across unseen manipulation techniques, compression levels, and dataset shifts. Most approaches rely on RGB appearance, frequency-domain artifacts, or their combination, learning cues present in the final synthesized image. While effective in-distribution, such cues are frequently generator-specific and can diminish as synthesis models evolve. We argue that a complementary perspective can be obtained through implicit neural representations (INRs), which expose how an image is reconstructed rather than merely how it appears. By fitting an INR to an image and analyzing its internal activations, one can reveal reconstruction dynamics that are difficult to observe in the image domain alone and may capture more intrinsic differences between genuine and synthetic content. To this end, we propose Spectra, a deepfake detection framework that combines semantic visual representations with artifact-aware cues derived from INR reconstruction. Spectra extracts multi-level reconstruction heatmaps from image-specific INRs and jointly models them with semantic features through a bidirectional fusion mechanism. This enables direct interaction between image semantics and reconstruction artifacts, allowing the model to identify forgery cues that are less dependent on specific generation pipelines. Extensive experiments on multiple deepfake benchmarks demonstrate improved robustness and cross-dataset generalization, consistently outperforming detectors based solely on RGB appearance or semantic representations. Furthermore, we show that the proposed representation extends beyond deepfake detection to face presentation attack detection, highlighting its potential as a unified framework for facial attack detection.

---


### 37. [Compatible Likelihoods for Flow Matching on Manifolds](https://arxiv.org/abs/2610.31981)

**<font color=#1a73e8>作者：</font>** Lucas Ng, Georgios Batzolis, Mark Girolami  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On the simplest non-Euclidean manifold, the 1D flat torus, we exhibit a distribution where a recently proposed extension of Riemannian flow matching is globally optimized by a velocity field that pushes samples away from the data distribution. We trace this failure mode to a property we call compatibility; a likelihood-based flow matching objective is compatible if its population minimizer recovers the marginal velocity field induced by the data and coupling. We give a general condition for compatibility, apply it to existing methods, and bound the worst-case error in terms of a residual component vanishing under compatibility. Next, we note that existing compatible objectives put density on velocities that are infeasible on compact manifolds. We propose an objective built from an exponential family over endpoints, with the conditional velocity as sufficient statistic, which is both compatible and supported only on feasible velocities. This manifests as a reweighting of the flow matching loss which, on constant-curvature manifolds, treats errors in flow speed and direction differently. Empirically, our method recovers the correct velocity field on the test case, outperforms prior methods on high-dimensional product tori, and obtains substantial NLL improvements over prior work on two of four standard geospatial benchmarks on the sphere at moderate runtime overhead. On a large dataset of high-dimensional human poses, our method outperforms prior work according to sample-based metrics.

---


### 38. [Interpreting Physics in Video Encoders using Multi-Object Interaction Videos](https://arxiv.org/abs/2610.31983)

**<font color=#1a73e8>作者：</font>** Ayushi Mehrotra, Sai Vidyaranya Nuthalapati  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video encoder models are increasingly used as world models for physical AI, where a policy plans by rolling out the latent, so what physics the latent holds bounds what the agent can plan over. Moreover, existing interpretability work probes quantities belonging to a single object; the quantities that make physics relational, such as momentum transfer, restitution, and friction, are defined between bodies and have not been examined. We probe relational physics attributes in two frozen self-supervised video encoders (V-JEPA2 and VideoMAE) under two-body settings and test if they transfer across environments. Our early findings are mixed. Both encoders separate elastic from inelastic collisions reliably. V-JEPA2's own predictor is less likely to predict a collision that creates kinetic energy compared to one that loses it. Momentum-violation detection appears in only one of the two encoders, a kinetic-energy readout survives a change of environment for V-JEPA2 but not for VideoMAE, and neither model holds a friction coefficient that survives a change of geometry.

---


### 39. [WADE: An LSTM-Based Anomaly Detection Engine for WebAssembly Applications](https://arxiv.org/abs/2610.31984)

**<font color=#1a73e8>作者：</font>** Ilaria Campestrini, Stefano Zanero, Engin Kirda  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> WebAssembly (Wasm) enables near-native performance for web applications through a portable and sandboxed execution model. However, its limited runtime protection mechanisms (e.g., the lack of stack canaries and address space layout randomization (ASLR)) leave Wasm applications vulnerable to traditional attacks.
We present WADE (WebAssembly Anomaly Detection Engine), a system that detects anomalous runtime behaviors in browser-executed WebAssembly applications. WADE monitors function-level execution traces collected under benign conditions and trains a Long Short-Term Memory (LSTM) network to learn the normal execution behavior of each application. At runtime, the model flags deviations from these learned patterns as potential attacks. Unlike signature-based approaches, WADE builds application-specific behavioral models, enabling detection of both known and previously unseen attacks without per-vulnerability signatures.
We evaluate WADE on a dataset of 67 WebAssembly applications spanning ten vulnerability classes, achieving zero false negatives and a 0.42% false positive rate.

---


### 40. [GELLI: A Generator for Experiential Language Learning Interactions](https://arxiv.org/abs/2610.31987)

**<font color=#1a73e8>作者：</font>** Danilo Symonette, Alan Y. Cheng, Taiga Ikedo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Learning a second language requires extensive practice across situations personal to each learner, yet the most effective existing approaches --- narrative situations designed around specific learning goals and delivered through media --- demand substantial authoring effort, limiting practice to the scope of what was built. We present GELLI, a system that generates narrative practice worlds from a learner's goals: situated scenes with characters to converse with, support alongside the interaction, and reflection, all produced at runtime with no pre authored content. In a within-subjects study with 40 learners of Japanese, GELLI produced greater vocabulary recall and confidence than expert-authored videos targeting the same goals, with no significant difference in speaking performance. Learners turned remembered or imagined situations into experiences they could shape and learn through. Support made experimentation feel safe, while unexpected narrative developments and language suggestions gave them new possibilities to pursue beyond what they initially intended to practice.

---


### 41. [REDAR: Reinforcement-Driven Adaptive Regularisation for Class Incremental Learning](https://arxiv.org/abs/2610.31991)

**<font color=#1a73e8>作者：</font>** Akila Ayanthi, Darshana Priyasad, Tharindu Fernando 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Regularisation-based class-incremental learning (CIL) methods control the stability-plasticity trade-off through fixed coefficients tuned offline, independently of the continual learning objective and blind to phase-specific variations in data volume, task difficulty, and class similarity. We argue this is a fundamental mismatch and propose REDAR: Reinforcement-Driven Adaptive Regularisation for Class Incremental Learning, which treats regularisation strength selection as a sequential decision problem. At each incremental phase, a lightweight reinforcement learning (RL) agent observes a compact state of current performance metrics and incoming data statistics, and outputs the distillation coefficients for that phase. To respect CIL's constraint on historical data access, the policy is trained entirely on pseudo-CIL tasks constructed from the initial phase, then deployed on the incremental sequence without further adaptation. Experiments on CIFAR-100 and Tiny-ImageNet demonstrate that REDAR reduces forgetting and improves forward transfer over fixed and heuristic baselines, and that policies trained on short pseudo-task horizons transfer effectively to longer incremental runs.

---


### 42. [Gaze Under Strain: How Oculomotor Behavior Tracks Cybersickness Progression in VR](https://arxiv.org/abs/2610.32019)

**<font color=#1a73e8>作者：</font>** Nevzat Umut Demirseren, Mehedi Hasan Raju, Oleg Komogortsev 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Cybersickness remains a major barrier to comfortable, accessible virtual reality (VR). Arising from mismatches between visual and vestibular signals, it places sustained demands on gaze stabilization and visual processing. Because gaze is the mechanism through which users actively sample the virtual environment, cybersickness-induced disruptions may alter both what users perceive and how discomfort itself emerges. Yet, how eye-movement behavior evolves alongside discomfort during prolonged VR exposure remains poorly understood. We present a behavioral analysis of eye-tracking data from 19 participants navigating a realistic virtual environment over a 20-minute session, with discomfort rated repeatedly throughout the experiment. Linear mixed-effects models examined gaze constructs spanning fixation stability, visual exploration, and gaze allocation as functions of discomfort, exposure duration, and their interaction. Our results show that fixation stability degraded progressively with increasing discomfort, with the effect strengthening over time. Visual exploration showed no marginal discomfort effect but exhibited significant discomfort-by-time interactions, indicating that saccadic behavior adapts dynamically rather than responding uniformly to discomfort. Gaze allocation was not associated with discomfort but shifted systematically with time. These findings show that cybersickness does not uniformly disrupt gaze. Instead, different aspects of eye-movement behavior respond differently and change in ways that only become visible when discomfort is tracked repeatedly over time. Understanding how gaze evolves during cybersickness progression provides the behavioral grounding needed to better interpret how discomfort shapes the user's visual experience of immersive environments and to design more sensitive detection approaches.

---


### 43. [BARC-Bench: Benign Asks, Risky Consequences](https://arxiv.org/abs/2610.32024)

**<font color=#1a73e8>作者：</font>** Kangkang Li, Kelvin Luu, Lily Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Task instructions from users for agents are inherently underspecified, especially regarding safety boundaries--creating behavioral risks. To study these risks, we introduce BARC-Bench, a collection of 110 tasks across nine simulated workspace environments where benign requests leave openings for unsafe actions. In this benchmark, we evaluate agent behavior against safety boundaries established by workspace records, implicit environmental context, and unstated social norms. For example, an agent asked to schedule off-boarding discussions must arrange the meeting without prematurely revealing an employee's resignation through a shared calendar invitation. Evaluating four frontier model configurations across five attempts per task reveals that models are not consistently safe: the share of tasks completed safely on all five attempts ranges from 9.1% to 72.7%, with even the strongest configuration producing a safety violation on 27.3% of tasks. These results highlight an asymmetric operational risk: while models frequently complete complex workflows, their inability to consistently respect unstated boundaries presents a substantial barrier to safe autonomous delegation.

---


### 44. [PPO vs. SAC: A Comparative Study for Cooperative Motion Control of Dual-Arm Space Robots](https://arxiv.org/abs/2610.32034)

**<font color=#1a73e8>作者：</font>** Nasim Fallahiarezoodar, Zheng H. Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The growing population of orbital debris has intensified interest in active debris removal and on-orbit servicing, for which dual-arm space manipulators offer improved grasping stability and load distribution relative to single-arm systems. However, coordinating two manipulators under inter-arm collision avoidance, orientation alignment, and sensing uncertainty remains challenging. This paper develops a coordinated reinforcement learning framework for cooperative motion planning of a dual-arm space manipulator in a target-reaching task with inter-arm collision-avoidance constraints. A centralized state representation combines joint-space, end-effector, and target-relative information, while a multi-objective reward function promotes target-reaching accuracy, orientation alignment, motion smoothness, synchronized task completion, and collision avoidance. Within this framework, Proximal Policy Optimization (PPO) and Soft Actor-Critic (SAC) are compared as representative on-policy and off-policy algorithms, and the learned policies are further evaluated for generalization to previously unseen target configurations. Across five random seeds, SAC substantially outperforms PPO within the considered fixed-base simulation scenarios: it reaches an 80% success threshold in every seed (median 1.6M environment steps) whereas PPO does not reach it within a 4M-step budget, and it attains a higher mean success rate (78.6% versus 7.4%) with lower position and orientation errors and tighter bimanual synchronization. Both algorithms degrade on unseen boundary targets, but SAC retains most of its performance while PPO's collapses. The results also expose a failure mode of PPO: under the two-phase shaped reward, it tends to converge to a reward-loitering local optimum rather than committing to the precision task. This behavior highlights the sensitivity of on-policy learning to reward shaping.

---


### 45. [Rethinking Representation Geometry in Supervised Contrastive Learning under Long-Tailed Data](https://arxiv.org/abs/2610.32039)

**<font color=#1a73e8>作者：</font>** Joonhyeok Jeong, Jy-yong Sohn, Kibok Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supervised contrastive learning and its balanced variants have demonstrated their effectiveness for representation learning under long-tailed distributions. However, although prior analyses suggest that their optimal representations may exhibit a regular simplex geometry, whether such a geometry is indeed exhibited remains insufficiently understood. In this work, we present a theoretical framework for these objectives that characterizes whether a regular simplex is formed at the optimum. By applying this to representative objectives, we show that these objectives fail to form a regular simplex at the optimum because they remain dependent on the number of samples per class. Motivated by this analysis, we introduce structural balancing that can be applied to contrastive objectives, and propose a fully balanced contrastive objective that provably forms a regular simplex geometry at its optimum. Both theoretical and empirical results demonstrate that the proposed method yields a more balanced representation space and improves performance on long-tailed recognition and transfer learning tasks.

---


### 46. [NUViT: Vision Transformers for Fourier Space Data](https://arxiv.org/abs/2610.32041)

**<font color=#1a73e8>作者：</font>** Jeffrey Gu, Robert C. Heeter, Ellen D. Zhong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) have demonstrated strong performance in many computer vision tasks but do not naturally extend beyond the natural image domain. One important example is Fourier-space data, which is used to represent a rich and diverse set of modalities, including medical imaging and microscopy. Standard ViT tokenization partitions an image into square patches on a Cartesian grid, which poorly fit the frequency and phase structure of Fourier-space data. We introduce Non-Uniform ViT, a simple, general-purpose vision transformer that redesigns image tokenization, data representation, and positional encoding to respect this structure. Experiments on Fourier-domain image classification, 2D crystal lattice identification, MRI annotation, and cryo-EM protein heterogeneity analysis show that NUViT consistently captures the structure of Fourier data better than standard architectures.

---


### 47. [X-Dubbing: Speech-to-Speech Translation under Temporal and Visual Constraints](https://arxiv.org/abs/2610.32042)

**<font color=#1a73e8>作者：</font>** Jeongsoo Choi, Ji-Hoon Kim, Junseok Ahn 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-lingual dubbing aims to convert source speech into target-language speech that remains synchronized with the original video. The key to this task is to produce a faithful translation that is naturally speakable within the source timing, which is non-trivial because languages differ in duration, rhythm, and articulation. In this paper, we propose X-Dubbing, which formulates the task as a joint problem of time-aware speech-to-text translation and video-aware text-to-speech. Specifically, our method consists of a Dubbing Translator that generates temporally structured scripts and a Voice Actor that renders them in synchrony with the source video, both grounded in a language-agnostic timing budget. We further refine the translator with dubbing-aware feedback from the synthesized speech, encouraging scripts that yield well-synchronized dubbing. This design requires no paired dubbing data, as the two components are trained on speech-text and monolingual audio-visual data respectively. Extensive experiments show that X-Dubbing outperforms recent baselines across diverse metrics, including isochrony and audio-visual correspondence.

---


### 48. [ACVA-Bench: Beyond Prompt Following in Abstract Concept Visualization Ability for Text-to-Image Models](https://arxiv.org/abs/2610.32058)

**<font color=#1a73e8>作者：</font>** Mengyan Wang, Jiyuan An, Yining Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image (T2I) models have achieved remarkable progress in image quality and instruction following, prompting growing research interest in their capacity for deep understanding that goes beyond literal prompt matching. However, without an explicit visual scheme provided, it remains unclear and has not been systematically evaluated whether T2I models can autonomously translate abstract concepts lacking a fixed visual referent, such as "loyalty," into visual representations that are accurate, diverse, and distinguishable from closely related concepts. We define this capability as Abstract Concept Visualization Ability (ACVA) and introduce ACVA-Bench, a category-balanced benchmark grounded in psycholinguistic norms of abstract concepts, which examines models' ACVA along three dimensions semantic sufficiency, representational diversity, and conceptual distinctiveness under a low-intervention setting that withholds concrete objects, scenes, or visual metaphors. Since abstract concepts lack a unique reference image, conventional evaluation metrics that rely on reference-image matching are difficult to apply. To address this, we propose a fine-grained visual-semantic evaluation method constrained by concept semantics, which decomposes concept semantics into independently verifiable visual-semantic questions to assess the semantic representation quality of generated images, with its validity further confirmed by human evaluation. Benchmarking results on mainstream T2I models show that these models rely on a small set of prototypical visual patterns, leaving room for improvement in representational diversity and conceptual distinctiveness for abstract concepts, thereby providing an interpretable and reproducible evaluation foundation for future research.

---


### 49. [Concept Acupuncturist: An Efficient and Precise Concept Erasure Method for Diffusion Models via Sparse Autoencoders](https://arxiv.org/abs/2610.32059)

**<font color=#1a73e8>作者：</font>** Yiran Xiahou, Siliang Qin, Kai Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based image generation models produce high-quality images but may generate harmful or policy-violating content, motivating machine unlearning (MU) to selectively remove target concepts while preserving general capabilities. However, existing MU approaches often struggle with the distributed and entangled nature of concept representations, leading to inefficient optimization and imprecise edits when applied through large-scale fine-tuning over full diffusion trajectories. To bridge this gap, we propose Concept Acupuncturist (ConceptACP), a novel MU framework that integrates interpretability-guided analysis with inference-free fine-tuning for efficient and precise concept removal. By establishing mappings between semantic concepts and cross-attention blocks in the U-Net denoiser and localizing the most concept-relevant block for targeted optimization, ConceptACP avoids full diffusion trajectory optimization, thereby improving fine-tuning efficiency. To mitigate concept entanglement, we propose a feature-level correction mechanism based on Sparse Autoencoders (SAEs), where SAE-derived sparse, semantically meaningful feature activations are manipulated to construct targeted correction signals, which are then projected back to the output space of the corresponding block and used as supervision for precise concept removal. Consequently, ConceptACP eliminates the need for external inference-time modules while achieving efficient and fine-grained unlearning. Instantiated on SDXL-Turbo, ConceptACP improves the forgetting success rate by 36.34 percentage points in the standard one-step generation setting on average over the best-performing baseline, while preserving image quality and prompt fidelity, and generalizes effectively across other Stable Diffusion backbones. Our code is available at this https URL.

---


### 50. [DBCM: Dual-Branch Calibration Module for Test-Time Adaptation in Time Series Forecasting](https://arxiv.org/abs/2610.32071)

**<font color=#1a73e8>作者：</font>** Jaebyeong Jeon, Kunwoo Kang, Sang Yup Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Non-stationarity induces test-time distribution shifts in time series forecasting (TSF), resulting in forecast residuals between predictions and the corresponding ground truth. Recent works on test-time adaptation for TSF address this by introducing lightweight calibration modules around frozen forecasters, updated using observations that become incrementally available at test time. Existing approaches typically employ channel-wise adapters, implicitly assuming that forecast residuals are inherently channel-specific. However, we observe that forecast residuals often exhibit substantial shared structure across channels, suggesting that fully independent channel-wise parameterization may be redundant. Motivated by this observation, we propose the Dual-Branch Calibration Module (DBCM), which shares adaptation capacity across channels through a shared adapter while retaining limited channel-specific flexibility through a low-rank channel-wise adapter, further enhanced by channel mixing and nonlinear gated modulation. Extensive experiments show that DBCM consistently outperforms prior methods across diverse datasets, horizons, and backbones.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-198](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
