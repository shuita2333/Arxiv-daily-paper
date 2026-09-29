# 📦 其他研究 | 2026年09月30日

> 本类共 **908** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-908](./part-19.md)

---

### 251. [MassAlloc Attention: Let Attention Allocate Its Own Compute](https://arxiv.org/abs/2609.32712)

**<font color=#1a73e8>作者：</font>** Jingze Shi, Zhangyang Peng, Xianduo Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> FullAttn often assigns negligible normalized mass to much of the causal score space, yet dense kernels execute the complete post-score path after forming each QK tile. We introduce MALA, a fused attention primitive that preserves score access to every legal causal interaction and uses normalized contribution to allocate post-score computation. Forward uses its evolving online-softmax normalizer, while backward reuses the finalized normalizer to derive nested retained support using only standard attention state. A common tolerance governs training and inference, allowing for adaptive retention of the work. MALA reduces low-contribution post-score computation. A matched-work study at 8K isolates the benefit of distribution-adaptive allocation: under exactly matched total post-score work, MALA approaches a per-instance reference-mass oracle, with mean omitted mass of 0.0188% versus 0.0182%. Across context lengths from 1K to 32K tokens, the same tolerance maintains low output and gradient errors relative to the reference. Across a broader controlled associative-recall comparison, MALA closely tracks FullAttn as context grows, reaching 89.67% accuracy at 8K compared with 89.97% for FullAttn. In an attention-operator benchmark at 128K tokens with tensor parallelism, MALA reduces forward and backward latency during training by 2.2x and 3.0x and decoding latency during inference by 1.6x relative to FullAttn. Across scaling-law training from 0.6B to 14B parameters, MALA closely tracks FullAttn in perplexity while reducing total training FLOPs. The resulting 14B models and 32B models from separate continued training achieve comparable knowledge, reasoning, and long-context retrieval scores to FullAttn. These results indicate that allocating post-score computation according to normalized attention contributions can retain the evaluated capabilities of FullAttn while reducing attention computation.

---


### 252. [Region-Local Copula Evidence Fusion for Heterogeneous Remote Sensing Change Detection](https://arxiv.org/abs/2609.32716)

**<font color=#1a73e8>作者：</font>** Zhiyuan Ji, Junjun Yin, Jian Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Superpixel copula models provide stable regional evidence for heterogeneous remote sensing change detection, but a single label per region limits localization within mixed superpixels. This letter develops a region-local copula evidence fusion method that retains the regional decision structure while introducing spatially varying local dependence anomalies. Independently fitted local models characterize departures from unchanged cross-image relationships. Reference ranking and an upper-tail gate transform these anomalies for fusion with continuous regional confidence. We derive the resulting regiondependent local decision threshold and identify a condition under which gating is equivalent to reparameterizing ungated fusion. On Lake and UK, whole-image optimized configurations achieve kappa coefficients of 0.78136 and 0.90817 and improve mixedregion and boundary decisions. Four-fold retrospective spatial validation over ten training subsets confirms complementary local information, with ungated reference fusion increasing mean kappa by 0.00693 and 0.01793. Fixed gating yields a larger UK gain of 0.03353 but only 0.00041 on Lake. These results support regional-local dependence interaction, while showing that calibration and gating have scene-dependent benefits.

---


### 253. [Distributionally Robust Average-Reward Reinforcement Learning: Finite-Sample Guarantees under Weak Communication](https://arxiv.org/abs/2609.32727)

**<font color=#1a73e8>作者：</font>** Chenyu Lu, Zijun Chen, Nian Si  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study distributionally robust reinforcement learning (DR-RL) in the average-reward setting under weak communication. Our main result provides finite-sample guarantees for estimating the robust optimal average reward and learning a near-optimal policy, covering both SA-rectangular and S-rectangular structures with divergence-based and distance-based uncertainty sets. Specifically, for Kullback--Leibler and $f_k$-divergence balls, we establish explicit radius conditions under which the robust average-reward Bellman equation admits a constant-gain solution, while for total variation and Wasserstein balls, any positive radius suffices without requiring the nominal MDP to be weakly communicating. Our algorithm is prior-knowledge-free and achieves sample complexities of $\widetilde O(|\mathcal{S}||\mathcal{A}|p_{\wedge}^{-1}\operatorname{Span}^{2}(u_{\delta}^{\ast})\epsilon^{-2})$ for estimating the robust optimal average reward and $\widetilde O(|\mathcal{S}||\mathcal{A}|p_{\wedge}^{-2}\operatorname{Span}^{2}(u_{\delta}^{\ast})\epsilon^{-2})$ for learning an $\epsilon$-optimal policy. Here, $p_{\wedge}$ is the smallest positive nominal transition probability and $u_{\delta}^{\ast}$ is a robust optimal bias function. We further provide an almost-tight explicit upper bound on $\operatorname{Span}(u_{\delta}^{\ast})$. Finally, we validate the predicted $n^{-1/2}$ convergence rate through numerical experiments.

---


### 254. [Chatbot Engagement Does Not Always Beget Metalearning: Evidence from Three Countries](https://arxiv.org/abs/2609.32739)

**<font color=#1a73e8>作者：</font>** Kokil Jaidka, Insyirah Binte Imam Mujtahid, Peng Qi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Chatbots deliver real-time fact-checks, but whether a chatbot correction leaves anything behind once the chatbot is gone - metalearning, distinct from correcting misbeliefs - is untested. We report a preregistered, three-country randomized experiment (USA, India, Singapore; N ~ 2,200) on out-of-context image misinformation, manipulating a correction's channel affordances (synchronicity, bandwidth) across four conditions: Control, Links-only, Static explanation, and a Socratic Chatbot built on a validated out-of-context detector, with an unaided retest one week later. The Chatbot produced the largest immediate discernment gain (d = 0.097, p = .023). All three interventions reduced sharing of false claims (d ~ -0.12, p < .01). One week later, no advantage persisted: the Chatbot arm declined relative to Control, most sharply in India and Singapore, and in India on claims it never discussed. Decay tracked affordance level and did not vary by country. Engagement mechanisms, we argue, do not substitute for slow AI literacy.

---


### 255. [AnesTRACE: Benchmarking Intraoperative Anesthesia from Multimodal Perception to Multi-step Decision-Making](https://arxiv.org/abs/2609.32740)

**<font color=#1a73e8>作者：</font>** Ziwei Huang, Qi Gao, Zhe Ji 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Intraoperative anesthesia requires systems to interpret evolving multimodal evidence, recommend timely management, and revise decisions as patient states change, yet existing benchmarks usually isolate perception or single-point reasoning. We introduce AnesTRACE, an evaluation suite comprising AnesTRACE-Bench and AnesTRACE-Eval. Built from public perioperative datasets with anesthesiologist annotation, AnesTRACE-Bench evaluates Intraoperative Perception, Single-point Anesthesia Decision-Making, and Multi-step Anesthesia Decision-Making. AnesTRACE-Eval assesses open-ended responses through anesthesiologist-defined criteria for Clinical Correctness, Evidence Grounding, Task Completeness, and Safety, with Temporal Consistency for multi-step decisions; its domain-specific evaluator is trained by supervised fine-tuning and preference alignment on expert-reviewed judgments. Across more than 30 models, fine-grained visual grounding and intervention selection remain difficult: the leading model reaches only 32.2 mIoU for TEE visual grounding and retains a 17.5\% Major/Critical Safety Error Rate in multi-step management. Evaluator alignment with anesthesiologists improves across both training stages, while the best decision quality is accompanied by a 74.3-second P95 Latency. These results show that aggregate performance alone does not establish safe, timely longitudinal decision-making. We release our code at this https URL.

---


### 256. [Predicting the Financial Impact of Supply Chain Risk for Major AI-Related Semiconductor Firms: A Heterogeneous Graph Patch Transformer Approach](https://arxiv.org/abs/2609.32741)

**<font color=#1a73e8>作者：</font>** Jianna Hur, Sagar Samtani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern semiconductor production relies on a globally distributed, multi-tier supply chain in which financial stress at one firm spreads with a delay and eventually affects the revenue, inventory, and profitability of the companies that design AI chips. Most firms see only their direct partners, and prior predictive research has mainly targeted market-based risk measures, so few tools forecast how supply chain stress will appear in reported financials. In this study, we propose a heterogeneous graph patch transformer that forecasts these quarterly changes one and two quarters ahead. Learning from a 15,186-company network over 60 quarters, the proposed model fuses quarterly fundamentals with macro-trade, event, and disaster signals through learned gates, carries risk across supplier, customer, ownership, and headquarters relations through typed, direction-specific propagation, and encodes the propagated histories with patch-based tokenization. In preliminary experiments on 116 focal semiconductor firms, the proposed model achieves the lowest error on every target at both horizons, and its profitability advantage widens at the two-quarter horizon. These forecasts can help supply chain managers and investors act before disruptions appear in reported financials.

---


### 257. [LoCoVSR: Local Context Diffusion Posterior Sampling for Video Super-Resolution](https://arxiv.org/abs/2609.32742)

**<font color=#1a73e8>作者：</font>** Matan Ben Chorin, Michael Elad  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video super-resolution (VSR) is an ill-posed inverse problem that aims to reconstruct a high-resolution (HR) video from a noisy, low-resolution (LR) version of it. We present LoCoVSR, a diffusion-based VSR framework that leverages pixel-space denoising diffusion probabilistic models. LoCoVSR integrates the Diffusion Posterior Sampling technique with spatio-temporal context learning, operating in a moving-average form. A localized window of adjacent LR frames is used for recovering each center frame, while applying a shared noise trajectory across all frames. The localized windowing enables processing of long videos without length limitations, supports parallel inference, and prevents error accumulation that may occur in recursive processing. Unlike prior methods, LoCoVSR offers a simple yet very effective VSR solution, avoiding explicit optical flow estimation, or information loss caused by latent space processing. Trained on the VFHQ face dataset, LoCoVSR achieves accurate, temporally consistent and high-quality upscaling with competitive results against recent diffusion-based VSR approaches.

---


### 258. [Retrospective Distillation Attribution via Normalized Response Similarity](https://arxiv.org/abs/2609.32749)

**<font color=#1a73e8>作者：</font>** Minwoo Jang, Jaechang Kim, Minhyeon Oh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Model distillation transfers capabilities through supervised fine-tuning (SFT) on teacher responses, often collected from commercial APIs, raising questions of model provenance. Existing distillation attribution methods have been largely evaluated on students immediately after the SFT step. However, a distilled model may undergo further SFT, preference optimization, or reinforcement learning before release, while an auditor may lack access to the pre-distillation checkpoint required by reference-based attribution. To close this gap, we propose SCOUT, an output-only method that aggregates recurring *syntactic patterns* into candidate profiles, filters low-contrast patterns, and calibrates student--candidate distances against inter-candidate distances. SCOUT supports attribution and abstention using only current texts, without model weights, token likelihoods, or historical checkpoints. Auditing publicly released descendants of distilled models spanning diverse post-training objectives, SCOUT consistently identifies the distillation source. Furthermore, tracing teacher-associated *syntactic signatures* along training trajectories reveals that they emerge during distillation and persist through subsequent preference optimization and reinforcement learning.

---


### 259. [Action Shaping: Policies Absorb What They Can Express](https://arxiv.org/abs/2609.32752)

**<font color=#1a73e8>作者：</font>** Yanjun Chen, Jinghan Wang, Xiaoyu Shen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reward shaping has a theorem: a potential-based term can be removed without changing the optimal policy. The same practice on the action channel, an offset added in training and dropped at deployment, has no theorem. Nothing cancels an action offset, so the correction is kept at deployment or removed without a guarantee. We call it action shaping and state its principle. A trainable policy absorbs an offset its own output layer can reproduce exactly, which is what we mean by express; what is absorbed can be removed with the return intact. Its minimal instance is a zero-initialized linear head behind a learnable gate, added to an actor that trains through a learned action-value function, with no penalty or schedule. The gate rises and then falls on its own, for deterministic and stochastic actors alike, and on 20 tasks removing the head costs almost nothing. The condition is exact reproduction, not capacity: a nonlinear head with more parameters is not absorbed, and in a paired control, one linear path added to a nonlinear base head restores absorption. Exact reproduction gives the loss a flat direction that gradient noise drifts along, and the offset's amplitude indicates, before removal, what dropping the head will cost. Action shaping thus gains the counterpart of the shaping theorem, a condition for absorption, together with the mechanism behind it and a diagnostic that reads it. Policies absorb what they can express, and only that.

---


### 260. [The Extender: A Log-Structured Transformer](https://arxiv.org/abs/2609.32759)

**<font color=#1a73e8>作者：</font>** Jakob Eriksson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce the Extender, a log-structured variant of the standard Transformer architecture. In a standard Transformer, each layer communicates with subsequent layers exclusively via the residual $\mathbf{h}$, a superposition channel. The Extender adds a concatenation channel $\mathbf{x}$: each layer $\ell$ emits both a residual update $\delta_\ell$ which is added to $\mathbf{h}$, and a much smaller extension $\epsilon_\ell$ which is appended to $\mathbf{x}$. While both the FFN and $\mathbf{q}$ see $\mathbf{h}$, the attention $\mathbf{kv}$ projections take only $\mathbf{x}$ as input. As a result, the fully extended $\mathbf{x}$ contains the complete input for the $\mathbf{kv}$ projections of all layers, reducing the persistent attention memory footprint from $2Ld_{model}$ to $\sum|\epsilon_\ell|$. We find that with $|\epsilon_\ell|=32$, the Extender matches Transformer accuracy on short-context (CORE) tasks at 199M-924M parameters, and exceeds Transformer accuracy on long-context (RULER) workloads, again at 924M parameters. For our 1664-wide, 924M model, the Extender's persistent attention memory footprint is $104\times$ smaller than MHA. The memory savings grow with model width.

---


### 261. [From Feed-Forward to Flow: Unifying Reconstruction and Generation Is Easier Than You Think](https://arxiv.org/abs/2609.32761)

**<font color=#1a73e8>作者：</font>** Haoru Wang, Qianfan Shen, Kai Ye 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstruct where the images provide evidence, and generate where they do not: recent success of spatial world models such as Atlas (World Labs Team, 2026) highlights the value of unifying reconstruction and generation in one model. Yet the two have long lived in separate paradigms with distinctive failure modes: feed-forward reconstruction averages ambiguity into blur, while conditional generation invents plausible but scene-inconsistent detail. In this work, we present a unified flow-based formulation for reconstruction and generation, where a shared clean-target predictor performs direct reconstruction at its single-step endpoint and unfolds conditional generation through multi-step flow. A controlled toy study reveals the mechanism: with a single step, the predictor collapses to the conditional mean just like feed-forward methods, favoring consistency over diversity. With multi-step inference, the fidelity of generated details grows with context richness: closer observations reduce ambiguity and yield better-matched details. We further instantiate the formulation in appearance and geometry 3D tasks. JiT-LVSM improves perceptual and distributional quality in novel view synthesis, while JUSt3R retains competitive single-step geometry prediction with additional multi-step inference capabilities that reduces veil and flying-pixel artifacts, producing cleaner surface structure with greater test-time compute. Together, they show that reconstruction and generation can share both a formulation and a backbone, with their behavior governed by denoising configuration---making unification surprisingly simple.

---


### 262. [Mandela-Bench: Multimodal Models Remember Canonical Images Instead of Seeing Them](https://arxiv.org/abs/2609.32763)

**<font color=#1a73e8>作者：</font>** Yicheng Bao, Zhenkun Gao, Xiahui Guo 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Historical photographs and other canonical images can now be edited seamlessly with a single instruction, often leaving no reliable pixel-level trace. In such cases, the only evidence of manipulation may be a fact about what the image depicts. Existing benchmarks instead rely on generator artefacts, image-caption inconsistencies, visual implausibilities, or external references, and therefore do not test whether a model can use its own world knowledge to verify a recognized image. We introduce Mandela-Bench, containing 1,507 edits of canonical images: 1,359 knowledge-only forgeries, each contradicting one verifiable fact, and 148 anchor-free controls that preserve the editing process without introducing a factual contradiction, together with 474 untouched originals. We score not only whether a model detects a forgery, but whether its explanation identifies the inserted entity or the fact being violated. Across 36 multimodal models, from 0.8B parameters to frontier scale, we find a consistent failure mode. When a public figure is removed from a familiar photograph, models still name that person in up to 72.7% of responses. Some models can distinguish the replacement face from the original when shown in isolation, yet still judge the full edited photograph as authentic. Providing the true event and date does not improve knowledge-grounded detection, whereas providing the same information after cropping away the recognizable composition does. Even under explicit verification prompts, only one of the 36 models meets the KGR criterion on at least half of the forged images. These results suggest that the failures cannot be explained by missing knowledge or inadequate perception alone. Instead, they are consistent with recognition biasing verification toward the remembered canonical image rather than the observed edit.

---


### 263. [AnchorMixGAN: Anchor-Aligned Generative Semi-Supervision for DDoS Detection in Cloud-Integrated IoT Networks](https://arxiv.org/abs/2609.32764)

**<font color=#1a73e8>作者：</font>** Jin Yang, Xufeng Liu, Yong Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Detecting distributed denial-of-service (DDoS) attacks in cloud-integrated IoT networks is difficult when labeled traffic is scarce. Generative semi-supervised learning can supplement the available training data, but prediction shifts induced by synthetic views may affect the targets assigned to real unlabeled flows. We propose AnchorMixGAN, a generative semi-supervised framework that addresses this problem through anchor-aligned target construction. Its Anchor-MAS module treats each real unlabeled flow as an anchor and creates alternative views by replacing one field group at a time with values from generated traffic. A frozen reference classifier predicts the anchor and its views; averaging and sharpening these predictions produces a soft target for the original flow. The flow and its target are then mixed with a labeled example using MixUp, allowing the detector to learn from both the original labeled records and the mixed examples. We analyze how reference-classifier error, view construction, and sharpening affect the target, and derive a bound on the resulting change in cross-entropy at a fixed detector prediction. At the reported 90% training setting with 20% of the training records labeled, AnchorMixGAN attains accuracies of 97.3%, 97.4%, and 96.5% on NSLKDD, BoT-IoT, and CICIoT2023, respectively, exceeding the corresponding MixGAN results by 1.6, 1.0, and 4.4 percentage points.

---


### 264. [Structuring Relations Among Learning Paradigms via Protocol--Objective--Resource Reductions](https://arxiv.org/abs/2609.32766)

**<font color=#1a73e8>作者：</font>** Junwei Su, Changjie Wang, Dongyang Chang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern machine learning spans supervised, transfer, continual, meta-learning, and related regimes that often reuse the same hypothesis classes, architectures, and optimizers but differ in information access, objectives, memory, adaptation, and sample accounting. This makes it difficult to determine whether one paradigm is genuinely distinct, a special case of another, or part of a broader structural hierarchy. We introduce a protocol-objective-resource (POR) framework that separates representational capacity from these design choices. A paradigm is specified by an environment class, observation protocol, admissible learners, performance functional, and resource accounting rule. POR reductions combine environment embeddings, learner compilers, threshold maps, and calibrated resource overheads. Our main theorem shows that such reductions imply worst-case complexity domination on embedded comparison classes, transferring upper bounds forward and lower bounds backward; under labeled-example accounting, this yields sample complexity domination. We also show that calibrated nontrivial accuracy regimes are necessary to avoid vacuous comparisons, and that strengthening the objective can strictly increase minimax sample complexity even with unchanged protocols and learner classes. Instantiating the framework for supervised, transfer, continual, and meta-learning yields canonical special-case relations: continual contains transfer, transfer contains supervised, and meta-learning contains supervised under aligned raw-example accounting. We further derive a non-exact episode-to-example reduction for episodic meta-learning and capture within-paradigm refinements such as replay memory and task identifiers. The framework thus provides a unified language for structuring learning paradigms and transferring complexity guarantees across them.

---


### 265. [You Can't Spot a Deepfake?And Neither Can Your Brain Nor Eyes: A Neurophysiological Framework for Deepfake Exploitation of Cognitive Engagement and Implicit Visual Evaluation](https://arxiv.org/abs/2609.32769)

**<font color=#1a73e8>作者：</font>** Cagri Arisoy, Md Imanul Huq, Amy W. Hays 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deepfakes have rapidly emerged as a pressing threat to information integrity and security because they exploit human trust in visual and auditory perception. Yet, little is known about whether humans and their underlying (sub)conscious neuro-physiological processes can reliably distinguish deepfake from real videos.
We introduce DECEIVE (Deepfake Exploitation of Cognitive Engagement and Implicit Visual Evaluation), a framework that models how deepfake videos are validated as adversarial payloads through behavioral and neuro-physiological screening of viewers, and how attacks can be refined by selecting payloads that evade detection. The framework is dataset agnostic and applies to synthetic or real media. It is inherently dual-use: an adversary with equivalent measurements could iterate on candidate manipulations and retain those that evade human detection. This motivates open, defensive evaluation. Measuring which deepfakes defeat human perception establishes a realistic bound on attacker capability against which detection tooling, provenance and watermarking mechanisms, and user-facing protections can be assessed.
As an instantiation, we conducted an EEG and eye-tracking study in which participants viewed real, deepfake, and look-alike videos drawn from Celeb-DF and a curated celebrity set, while behavioral judgments and implicit responses were recorded. Contrary to expectations of subconscious differentiation suggested by prior work on paintings and phishing websites, no statistically significant neuro-physiological differences emerged between real and deepfake videos, although clear distinctions were observed for look-alike videos. Behaviorally, participants accepted 26.68% of manipulated clips as authentic, rising to 31.94% for familiar identities, confirming the studied deepfakes as effective adversarial payloads within DECEIVE.

---


### 266. [Beyond Gaussian Assumptions: Distribution-Aware Channel Capacity for Effective Connectivity](https://arxiv.org/abs/2609.32774)

**<font color=#1a73e8>作者：</font>** Jianan Jian, Jacob Kang, Nurahmed Multezem 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Effective-connectivity estimation from brain signals often relies on Gaussian residual modeling, which enables tractable estimation but can discard informative distributional structure and distort inferred directed interactions when empirical residuals are non-Gaussian. We show across multiple modalities, species, and experimental conditions that both brain signals and fitted channel residuals frequently deviate from Gaussianity. We therefore introduce a distribution-aware, information-theoretic measure of effective connectivity based on channel capacity under general residual distributions. To estimate the resulting capacity from empirical, potentially non-Gaussian residuals, we develop a dual-flow min-max estimator based on normalizing flows, in which a generator searches over admissible input distributions under a power constraint while an observer estimates output entropy. We provide a theoretical characterization of the estimator, showing that the observer objective recovers differential entropy up to a KL approximation term, that the formulation reduces to classical Gaussian capacity as a special case, and that residual entropy can alter achievable information rates beyond variance; game-gap and error analyses further characterize optimization and approximation sources. In brain-like simulations with known directed connectivity, Dual-flow achieves the highest AUROC and AUPRC across ten conditions spanning diverse network topologies, hidden drivers, feedback, and heterogeneous hemodynamics, compared with Gaussian capacity, Granger causality, VAR-LiNGAM, and GIMME. Applied to multimodal brain signals, the method reveals time- and condition-resolved directed interactions consistent with known neurobiological circuitry. Together, these results establish a principled distribution-aware framework for effective-connectivity estimation beyond Gaussian residual modeling.

---


### 267. [Robust Bayesian Optimization with Q-Exponential Surrogates](https://arxiv.org/abs/2609.32775)

**<font color=#1a73e8>作者：</font>** Richard Cornelius Suwandi, Zhidi Lin, Feng Yin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian optimization (BO) is a widely used framework for optimizing expensive black-box objectives, but standard BO methods often use Gaussian process (GP) surrogates whose Gaussian assumption is sensitive to outliers and heavy-tailed noise. We introduce q-ED-BO, a robust BO method whose surrogate follows a univariate q-exponential (q-ED) distribution, preserving GP-BO's closed-form posterior mean and variance while a shape parameter q controls the tail behavior, recovering the GP at q = 2 and growing heavier-tailed with wider confidence bounds as q decreases. This tractability yields a closed-form q-upper confidence bound (q-UCB) with sublinear regret, and an exact closed-form q-expected improvement (q-EI) that generalizes EI to the heavy-tailed predictive, recovering classical EI at q = 2. Experiments on beamformer and adaptive filter tuning with impulsive outliers show that q-ED-BO matches or exceeds existing baselines on clean data, and under corruption, improves the strongest baseline by approximately 0.7 dB in output SINR and 1.1 to 1.2 dB in misalignment reduction.

---


### 268. [Agentic Network Traffic Monitoring](https://arxiv.org/abs/2609.32778)

**<font color=#1a73e8>作者：</font>** Manuel Tsoukatos, Hayden Jananthan, Jeremy Kepner  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As the use of agentic artificial intelligence increases in nearly every industry, there exists a widening attack surface. It is necessary to monitor agents to ensure that agents are acting in a way that is aligned with the users intent. Auditing an agent's network traffic provides a clear record of the agent interactions. This work presents a novel approach to monitoring the network traffic of agentic systems using complex valued hypersparse traffic matrices by integrating DBOS (DataBase OS), the OneSparse PostgreSQL database, and the GraphBLAS math library. To develop these concepts an agentic simulator was constructed, allowing a varying numbers of AI agents to collectively survey a virtual environment using different strategies. The resulting network traffic matrices enable easy monitoring of the AI agents.

---


### 269. [Learning response-aware patient dynamics for respiratory support](https://arxiv.org/abs/2609.32782)

**<font color=#1a73e8>作者：</font>** Xiaolei Lu, Shamim Nemati  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Respiratory support can shape the short-term physiological trajectory of critically ill patients, but patients receiving the same intervention may follow different physiological trajectories. Clinical patient dynamics models typically predict future states from recent physiology and recorded interventions, while physiological change is mainly represented through the predicted future state. We propose a response-aware patient dynamics model that explicitly represents physiological change during autoregressive state updating. The model decomposes predicted physiological change into state-dependent baseline dynamics and respiratory-support-associated deviations, with room air providing a reference for the decomposition. We provide a formal analysis of this reference-anchored formulation. A response pathway encodes the predicted physiological change and uses it to update the latent patient state across the forecast horizon. Across ICU cohorts from two independent institutions, the proposed model achieves comparable overall trajectory prediction to patient dynamics baselines, with more consistent improvements when physiological states are changing.

---


### 270. [Learning When to Recur: Token-Adaptive Recursion for Imbalanced Ophthalmic Domain Incremental Learning](https://arxiv.org/abs/2609.32785)

**<font color=#1a73e8>作者：</font>** Nanxi Yu, Kang Li, Ye Du 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Domain incremental learning is essential for adapting ophthalmic deep learning models to sequential clinical domains while preserving diagnostic expertise. Existing domain incremental learning methods predominantly address the domain shift induced by style variations. However, they often overlook the severe class imbalance inherent in real-world clinical scenarios, such as clinical referral systems. Institutions in these systems encounter drastic fluctuations in class priors, resulting in label distribution shift, a critical form of domain shift that triggers severe catastrophic forgetting. To address these challenges, we propose ToRe, a rehearsal-free and parameter-efficient framework that leverages frozen ophthalmic foundation models for robust incremental adaptation. ToRe employs a parameter isolation strategy to decouple domain-specific optimization paths, thereby helping mitigate catastrophic forgetting driven by both label distribution shift and style variations. Simultaneously, it introduces token-adaptive recursion that adaptively allocates additional computational depth across tokens, allowing simple tokens to exit the recursion loop early while subjecting complex tokens, such as those associated with lesions, to deeper recursive processing. This mechanism enhances the feature representations for minority classes, thereby supporting generalization throughout the domain incremental learning process. Extensive evaluations on nine heterogeneous datasets demonstrate that ToRe consistently outperforms state-of-the-art methods in overall performance across the three benchmarks, while maintaining near-zero forgetting. Together, these results support the applicability of ToRe to dynamic and imbalanced clinical environments. The code is available at this https URL

---


### 271. [Hierarchical Frequency-Domain Compression of Implicit Geometric Representations for Large-Scale Point Clouds](https://arxiv.org/abs/2609.32789)

**<font color=#1a73e8>作者：</font>** Manlin Yao, Jiabin Liu, Guan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale point cloud representations of complex geome tries incur prohibitive computational and memory costs, necessitating compressed implicit representations. To ad dress this, we propose a unified framework comprising im plicit geometric field representation, hierarchical frequency domain compression, and conditional high-frequency predic tion. Specifically, an unordered point cloud is mapped to an implicit field defined within its physical bounding box. A smooth Fourier pyramid is then constructed, where com pact low-frequency components capture the global geometry. Inter-scale high-frequency residuals are encoded to preserve the spatial information required for reconstructing fine geo metric details. To restore the high-frequency information lost during compression, we develop a hierarchical 3D neural net work. The reconstructed implicit field is converted back into a point cloud through isosurface extraction. Experiments on a complex-boundary point cloud with more than eight mil lion points demonstrate that the proposed method achieves a higher compression ratio than existing point cloud compres sion methods while maintaining comparable reconstruction quality.

---


### 272. [FedHV: Low-Overhead Hypervolume Weighting for Federated Multi-Objective Optimization](https://arxiv.org/abs/2609.32790)

**<font color=#1a73e8>作者：</font>** Amirardalan Dehghanpour, Seyed Mohammad Azimi-Abarghouyi, Christopher G. Brinton  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Task-wise federated multi-objective optimization (FedMOO) trains a shared model for competing prediction objectives under heterogeneous data, partial participation, and communication constraints. Existing methods commonly derive task weights from gradient or update geometry. This requires task-specific information or iterative server-side optimization. We introduce FedHV, which maps reference-relative objective slacks to closed-form inverse-slack weights. Each client optimizes one weighted loss and returns objective estimates with its model update. The protocol adds exactly 2m auxiliary scalars per participating client, yielding Theta(d + m) total per-client communication, compared with the Theta(md) task-specific communication of FSMGDA, and requires no additional synchronization stage. We analyze the resulting one-round-delayed weights under client heterogeneity, multi-step local updates, partial participation, and finite-sample objective reports. Under a fixed-horizon positive-slack reference condition, with the prescribed horizon-dependent step size and vanishing report error, FedHV achieves an O(T^(-1/2)) rate for the average squared log-hypervolume gradient norm; persistent report error determines the resulting stationarity neighborhood. The same bound controls the squared Pareto-stationarity residual. Across six Dirichlet-partitioned non-IID settings from four vision benchmark families and three training seeds, FedHV exceeds FSMGDA and FedCMOO in mean accuracy in five settings. Among these methods and uniform scalarization, it achieves the highest worst-task accuracy in four settings and improves the difficult CIFAR-10 objective in both CIFAR10-MNIST settings.

---


### 273. [Latent Space Is Not Flat: Rethinking Latent Structure for 3D Medical Image Synthesis](https://arxiv.org/abs/2609.32794)

**<font color=#1a73e8>作者：</font>** Haowen Xue, Hao Chen, Hexuan Hu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent generative models make 3D medical image synthesis computationally practical by generating in a compressed space. However, we show that the common flat Euclidean assumption induced by $\ell_2$ objectives is imprecise: latent-space geometry is so strongly anisotropic that equal-magnitude errors can produce drastically different decoded distortions. We further find that this anisotropy has a clear feature: sensitive variation concentrates in a low-rank subspace. The dominant low-rank components capture the overall structure, encoding long-range, spatially coordinated variation while remaining resistant to local noise. Its orthogonal residual, in contrast, mainly captures local and image-specific variation. Motivated by this asymmetry, we introduce Latent Structure Flow (LSF). At each block, LSF decomposes the latent state into structure and residual, models structural changes with global context, and predicts residual variation locally while preserving a direct path for the input structure. LSF changes only the generator, leaving the frozen codec and pointwise training objective unchanged. Across cross-modality synthesis and tumor inpainting tasks, LSF outperforms all compared baselines on both global and tumor-specific metrics, demonstrating the benefit of explicitly modeling latent-space structure for 3D medical image synthesis.

---


### 274. [Derivative-Informed Training of Neural Operators On-the-Fly via Sketched Tangent Consistency](https://arxiv.org/abs/2609.32797)

**<font color=#1a73e8>作者：</font>** Xinhan Yang, Lu Lu, Shancong Mou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Derivative-informed training improves neural operators by directly supervising their input-output sensitivities, which is crucial when neural operators are used as differentiable surrogates for inverse problems, PDE-constrained optimization, design, and control. However, existing methods rely on offline-generated derivative labels, making data generation slow, storage-intensive, and difficult to adapt across datasets, resolutions, or perturbation bases. We propose sketched tangent consistency loss (sTCL), an on-the-fly derivative-informed training objective that, for PDEs with a known and differentiable residual, enforces sensitivity consistency directly from the governing equation without offline tangent labels or neural-operator architecture changes. sTCL uses randomly sketched input perturbations to provide a lightweight derivative-level physics constraint during training. However, raw forward-sensitivity residual penalties can fail for stiff, ill-conditioned, indefinite, or coupled saddle-point tangent operators. To address this, we introduce lightweight operator-aware loss-conditioning mechanisms selected by a simple tangent-operator decision rule. Across Helmholtz, nonlinear diffusion-reaction, Burgers, Allen-Cahn, and Navier-Stokes, with the same neural-operator backbone for all methods, the PDE-specific sTCL losses achieve solution and Jacobian accuracy comparable to offline derivative-informed training (DIFNO) while eliminating the offline derivative-data generation and storage pipeline. These results show that on-the-fly derivative-informed training need not merely amortize offline tangent-solve cost into training; with appropriate sketching and loss design, sTCL provides an effective drop-in path to derivative-informed neural operators. Code is available at this https URL.

---


### 275. [Adaptive and Resilient Dual-Layer Resource Slicing for Hovering Aerial Backhaul Networks](https://arxiv.org/abs/2609.32798)

**<font color=#1a73e8>作者：</font>** Chuan-Chi Lai, Jen-Hsiang Li  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> This paper investigates adaptive and resilient dual-layer resource slicing in hovering aerial agent (HAA)-assisted backhaul networks for heterogeneous 5G/6G services, including enhanced mobile broadband (eMBB), ultra-reliable and low-latency communications (URLLC), and massive machine-type communications (mMTC). To address the complex coupling of this dual-layer architecture in non-stationary environments, we propose the resilient adaptive priority orchestration enhanced twin delayed deep deterministic policy gradient (RAPO-TD3) framework. We introduce a novel double soft-max projection mechanism to map the continuous action space into physically feasible bandwidth distributions, ensuring strict constraint adherence. Additionally, a resilient adaptive priority orchestration (RAPO) mechanism is embedded to safeguard mission-critical URLLC latency. Crucially, we establish a rigorous mathematical foundation proving that our framework ensures Lipschitz continuity and satisfies the Robbins-Monro conditions for stable asymptotic convergence. Extensive simulations under non-stationary traffic demonstrate that our RAPO-TD3 framework achieves superior performance relative to PPO, DDPG, and traditional solvers. Notably, via the RAPO mechanism, our approach maintains URLLC satisfaction levels closely approaching theoretical optima even during 500% demand surges. Furthermore, scalability evaluations indicate that sub-millisecond execution latencies strictly satisfy the 1 ms URLLC budget, demonstrating the performance efficacy of our proposed framework.

---


### 276. [Progressive Risk Estimation for Accident Anticipation](https://arxiv.org/abs/2609.32811)

**<font color=#1a73e8>作者：</font>** Samet Hicsonmez, Eray Çakar, Nermin Samet 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accident anticipation aims to recognize anomalous driving cues before a crash while avoiding false alarms during normal driving. Existing approaches typically formulate this task as binary classification, focusing on whether an accident will occur rather than when it will occur. We propose PRE-ACT, a framework that models accident risk as a continuously evolving signal that increases as the crash approaches. By explicitly enforcing temporal ordering and distance-to-accident awareness, our method progressively raises risk while suppressing premature alarms, leading to significant improvements on MM-AU subsets and Nexar. We further introduce a Separation Score to evaluate the global behavior of predicted risk curves beyond local temporal windows. Code and visualizations are available at this https URL.

---


### 277. [Change the Product, Keep the Parameters: Associative Algebra Layers for Transformers](https://arxiv.org/abs/2609.32814)

**<font color=#1a73e8>作者：</font>** Ilya Koziev, Ivan Oseledets  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fast matrix multiplication algorithms keep the product fixed and search for a cheaper way to evaluate it. We instead ask whether a Transformer's learned projections can use a different, cheaper product altogether. Building on an associative-algebra construction that replaces ordinary matrix multiplication with a sparser interaction table over the same weight blocks, we construct a family with quadratic arithmetic in the matrix dimension when the physical block size remains fixed, and derive finite-shape constraints for GPU execution. The construction is provably optimal for its bilinear rank by the Alder--Strassen bound and can be realized as row-typed rectangular projections compatible with causal masking and KV-cached decoding. We provide an empirical test of this approach by training two approximately 110M-parameter decoder-only Transformer LMs from the same recipe and 12.3B-token budget, differing only in their feed-forward layer: one uses ordinary dense matrix multiplication and the other uses the associative-algebra product. Across four prompt domains, the algebraic model achieves a 6.2--7.8\% increase in end-to-end generation throughput, while obtaining lower scores on all three reported downstream metrics. We treat these results as a feasibility and trainability check for the proposed approach at small scale, leaving further investigation to future work.

---


### 278. [Rank Collapse Is Recoverable, Growing $|Q|$ Is Not: Out-of-Sample Early Warning for Value Divergence in High-UTD Soft Actor-Critic](https://arxiv.org/abs/2609.32819)

**<font color=#1a73e8>作者：</font>** Tianqi Bu, YuXuan Peng, Junteng Tu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Raising the update-to-data (UTD) ratio breaks off-policy critics in two ways grouped as "plasticity loss": collapsing representations and growing value magnitude $|Q|$. We separate them in Soft Actor-Critic (SAC) with scaled critics (width 2048, no normalization). Collapse is survivable: at UTD ratio 16, HalfCheetah critics with most units dormant keep learning, and the training guard, which stops runs whose loss or $|Q|$ explodes, never flags them. Within one high-UTD SAC configuration, runs start close together, and how far a critic's $\log_{10}|Q|$ has climbed by step 15k, its early growth, ranks the runs by how soon the guard flags them. At 15k, a flagged run's $|Q|$ sits a median of over a hundredfold below its flag level, yet the climb's rate already orders the flags (Harrell's C and out-of-sample AUC 0.78 on Walker2d, 0.98 on Ant, at UTD ratio 4). Dormancy does not. Aborting on this rate saves about a tenth of held-out Walker2d compute and stays net-positive live. A LayerNorm critic lowers the rate, removes the flag on Walker2d at UTD ratio 4 and lowers the return.

---


### 279. [Unlocking Geodesic Gromov-Wasserstein Distances for 3D Modeling](https://arxiv.org/abs/2609.32824)

**<font color=#1a73e8>作者：</font>** Krzysztof Marcin Choromanski, Derek Long, Ananya Parashar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> \textit{Gromov-Wasserstein Distances} (GWDs) provide quantitative ways of comparing probabilistic distributions defined on different metric spaces by applying techniques from the optimal transport theory. As such, GWD can be potentially useful in a large variety of applications ranging from graph matching problems to 3D object detection. However its practical use at scale is significantly limited by cubic time complexity computations involving dense intra-space distance matrices. Even though in the Euclidean metric spaces several techniques (e.g. involving scalable kernel methods) were proposed to address it, to the best of our knowledge, analogous techniques for general geodesic distances on manifolds, or shortest-path distance on graphs in their discretized variants, were not developed. In this paper, we present \textbf{E}fficient \textbf{G}eodesic \textbf{Gro}mov-\textbf{W}asserstein methods (EGGroW), a new class of efficient algorithms designed to calculate geodesic Gromov-Wasserstein distances with entropic Sinkhorn-like approaches, leveraging recently introduced \textit{GenusSink} methods \citep{genussink} and the theory of random features. We provide important downstream applications, namely: 3D pose estimation and 3D template detection. In the latter setting, we formulate a partial 3D template recovery as a staged problem: capacity-constrained scene selection is followed by semi-relaxed recovery of template visibility and correspondence. Our empirical findings show that EGGroW provides accurate solutions when standard Euclidean-based techniques fail and is characterized by light computational footprint, as our theoretical analysis predicts.

---


### 280. [Retimed Bellman Flows: Escaping the Impossible Triangle of Velocity Bootstrapping](https://arxiv.org/abs/2609.32828)

**<font color=#1a73e8>作者：</font>** Boyang Xu, Shengzhe Chen, Hao Yan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow critics learn return distributions by transporting Gaussian noise to Bellman endpoints via continuous velocity fields. While velocity bootstrapping stabilizes training by querying a successor teacher, existing methods face a structural dilemma: on straight paths, no residual-free same-time affine mapping can preserve Gaussian initial noise while maintaining an unbiased target. To overcome this limitation, we introduce Retimed Bellman Flows (ReBF). ReBF queries the teacher critic at a dynamically shifted earlier flow time, aligning intermediate student and teacher trajectories. By combining this retimed clock with fresh, decoupled noise generation, ReBF constructs a provably conditionally unbiased velocity target that preserves the Bellman fixed point and contracts under Wasserstein distances. Empirically, ReBF reduces $W_1$ distance to ground-truth return distributions by up to $7.7\times$ on synthetic MRPs and outperforms existing flow critics across 38 challenging OGBench and D4RL offline reinforcement learning tasks.

---


### 281. [Over-the-Air Federated Learning in Heterogeneous Mobile Wireless Networks](https://arxiv.org/abs/2609.32832)

**<font color=#1a73e8>作者：</font>** Ming Xiang, Nicolò Michelusi, Yonina C. Eldar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Over-the-air computation has emerged as a scalable and efficient solution for deploying federated learning algorithms in wireless networks by exploiting waveform superposition for simultaneous model aggregation. Most existing work struggles with heterogeneous fading channels. These approaches either enforce unbiased updates from all devices or allow partial device contributions, requiring careful tuning of the convergence bound to mitigate bias under specific fading models. However, the former significantly amplifies receiver noise due to the weakest channel, whereas the latter is sensitive to fading model mismatch and converges only to a biased objective. To tackle these challenges, we propose FedOAG, which employs algorithmic components to automatically satisfy energy constraints via gradient normalization and evenly mix devices' updates through implicit gossiping. Importantly, FedOAG does not require transmission from all devices, nor does it rely on a specific fading model or knowledge of time-varying statistical channel distributions. We show that FedOAG converges to a stationary point of an unbiased non-convex objective at the best possible rate $O(1/\sqrt{T})$ for any stochastic first-order method. We corroborate our analysis with numerical experiments over dynamic wireless conditions on real-world datasets.

---


### 282. [Permutation-Equivariant Flow Matching for Alignment-Free Neural Weight Generation](https://arxiv.org/abs/2609.32833)

**<font color=#1a73e8>作者：</font>** Arkadi Piven, Yam Eitan, Guy Bar-Shalom 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A trained neural network can be represented by a parameter vector in high dimensions. Learning distributions over these vectors enables the generation of new models across various tasks and architectures. A central challenge is permutation symmetry: permuting hidden neurons can produce distant parameter vectors representing the same function. This introduces variations that a generative model must account for when learning from trained networks. Existing methods typically address this using networks derived from a common base model or costly approximate neuron alignment. We instead parameterize a flow-matching velocity field with a permutation-equivariant Graph Meta Network, enabling direct learning from independently trained networks without alignment. Extensive experiments show that our method closely reproduces the joint statistics of accuracy, functional similarity, and weight similarity of independently trained collections, providing evidence of generation beyond checkpoint memorization. A single conditional model also generates task-specific networks on heterogeneous architectures and generalizes to unseen hidden-width configurations. On a tabular domain-shift task, intermediate conditioning produces individual networks with performance comparable to logit ensembles across both domains. Taken together, our results show how permutation equivariance enables learning from diverse collections of independently trained networks without permutation alignment.

---


### 283. [HamiFormer: Dual-Expert Diffusion Fields with Affine Symplectic Maps](https://arxiv.org/abs/2609.32838)

**<font color=#1a73e8>作者：</font>** Haoxiang Huang, Xiang Liu, Shuwei Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting smooth dynamics and collisions requires modeling continuous evolution and abrupt state changes. We introduce HamiFormer, a dual-expert diffusion field combining whole-window denoising with residual-corrected Hamiltonian propagation. Their mixed-state feedback attenuates the direct contribution of inherited autoregressive error: each mixed state guides subsequent propagation within the jointly refined window. Parallel Local Affine Scan (PLAS) amortizes iterative refinement across rectified-flow steps and evaluates derivatives in parallel across physical time. PLAS's affine symplectic maps achieve lower solver error and runtime than sequential explicit Euler in our evaluation. A Regime Model Tree specializes residuals and routing to balance typical-state accuracy against large tail errors. Our analysis gives conditions for physically consistent refinement and warm-start tracking, and finite-window error bounds under diffusion feedback. In 192-step evaluations, HamiFormer reduces normalized phase-space MSE by 26.3% against PhysiFormer on HamiBalls-1 and 21.4% against DiT on HamiBalls-2, with comparable model capacities. Disjoint-interval comparisons show the lowest late-horizon position and momentum errors among baselines on both datasets. Project page: this https URL.

---


### 284. [VCRE-Fib: View-Conditioned Regional Evidence for Fine-Grained Ultrasound Grading of Schistosoma japonicum-Associated Liver Fibrosis](https://arxiv.org/abs/2609.32840)

**<font color=#1a73e8>作者：</font>** Ziyang Xu, Shuli An, Hao Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate assessment of Schistosoma japonicum-associated liver fibrosis is essential for disease management and long-term follow-up in endemic regions. Ultrasound provides non-invasive imaging, but complex local echogenic patterns and anatomical structures make fine-grained grading challenging. Existing deep learning methods can predict fibrosis scores, yet directly incorporating acquisition views and regional cues into grading while retaining spatial information for inspection remains an open problem. Here we present VCRE-Fib, a view-conditioned regional evidence framework that integrates anatomical context, local information, and global image assessment for fine-grained ultrasound grading. The framework forms view-conditioned local grading evidence before spatial pooling, uses weak localization to guide its aggregation, and combines it with global predictions. Image-only inference jointly returns a fibrosis score, acquisition view, and candidate abnormal-region map. We developed and evaluated the method on a re-curated cohort of 108,709 ultrasound images from 6,373 patients across 35 centers. On a patient-disjoint test set of 4,107 images from 240 patients across four centers, VCRE-Fib reduced the prespecified composite grading risk by 7.115% relative to SFibAI trained and evaluated on the same data split. Image-level mean absolute error decreased from 0.391 to 0.378, alongside lower patient-max, patient-median, and center-balanced risks. The full model also achieved lower composite grading risk than variants that separately removed view conditioning or weak localization. These results support incorporating anatomical context and regional evidence into ultrasound grading while exposing spatial predictions for inspection alongside severity estimates.

---


### 285. [Beyond Temporal Smoothing: Spatial Energy Budgets Stabilize One-Step Diffusion Editing](https://arxiv.org/abs/2609.32841)

**<font color=#1a73e8>作者：</font>** Shengxiao Zhou, Lei Luo, Jian Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> One-step text-guided diffusion editing is efficient but prone to spatially misallocated updates that distort the edited object and alter the background. Existing methods often improve stability by averaging the editing field across timesteps. We instead identify spatial energy misallocation as a distinct and measurable failure mode: across two independent noise draws, the residual field is essentially unrepeatable, making the background field unreliable for direct transport, while its total energy still sets a usable magnitude for the draw at hand. BudEdit turns that magnitude into an explicit budget and reallocates it to edit-relevant regions selected jointly by residual energy and cross-attention, controlling where editing energy is spent rather than averaging over timesteps. The resulting training-free, inversion-free editor spends the budget on transport and reuses it to scale a correction in a lower-noise gated refinement. The budgeted injection field matches its prescribed budget exactly and vanishes on the identified background support, by construction. On PIE-Bench with SD-Turbo, BudEdit outperforms ChordEdit under each method's reported default settings on all 11 evaluated metrics, including a $2.1$\,dB gain in background PSNR, $31$\% lower DINO, and $36$\% lower LPIPS, while improving all five editing-quality metrics and reporting the lowest runtime in the comparison.

---


### 286. [SynCo: Learning Cross-Modal Synergy by Contrasting Interaction Residuals](https://arxiv.org/abs/2609.32846)

**<font color=#1a73e8>作者：</font>** Yavuz Yarici, Ghassan AlRegib  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal contrastive learning is a dominant paradigm for learning transferable representations from unlabeled data, but standard objectives primarily capture information that is redundant between modalities. Partial Information Decomposition (PID) shows that task-relevant information in multimodal data decomposes into three components: redundancy shared between modalities, uniqueness specific to each modality, and synergy available only from their joint observation. Recent frameworks extend contrastive learning to capture all three components, yet synergy remains undertrained in practice. We propose SynCo (Synergy Contrastive Learning), a method that directly addresses synergy undertraining through dedicated supervision on an interaction residual. SynCo fits a linear projector to predict the fused representation from independently computed unimodal features, and the resulting interaction residual, which removes the linearly unimodal-predictable component, receives dedicated contrastive supervision at negligible computational cost. On the controlled Trifeature benchmark, SynCo achieves state-of-the-art synergy capture with a $+5.98\%$ gain over the baseline, and on real-world benchmarks from MultiBench, DARai, and MM-IMDb, SynCo consistently outperforms or matches prior methods across diverse modality combinations and task types. The method operates as a plug-in to existing contrastive multimodal frameworks without modifying the underlying fusion architecture and can further improve synergy capture when combined with other methods.

---


### 287. [Logic Gate Networks and Lookup Table Networks as Lightweight Hardware Classifiers for Inter-patient ECG Arrhythmia Classification](https://arxiv.org/abs/2609.32854)

**<font color=#1a73e8>作者：</font>** Wout Mommen, Lars Keuninckx, Siddharth Patil 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep Differentiable Logic Gate Networks (LGNs) and Lookup Table Networks (LUTNs) offer a promising approach for very low power inference due to their use of simple binary logic operations instead of arithmetic. In this work, we generalize the logic gates of LGNs to more than two input pins, naturally arriving at networks consisting of $N$-input LUTs. To obtain a differentiable expression for training the $N$-LUT entries, we adopt the Boolean equation of a $2^N$:1 multiplexer (MUX) and optimize its input parameters during training. We investigate the applicability of LGNs and LUTNs to inter-patient ECG arrhythmia classification using the MIT-BIH data set. The proposed models achieve up to 94.41\% accuracy and a $j\kappa$ index of 0.683 on a four-class task, showing a competitive performance compared to existing CNN-, SVM- and SNN-based methods. Our LGNs and LUTNs only require an estimated 2.89k to 6.17k FLOPs, including preprocessing and readout, which is three to six orders of magnitude less than state-of-the-art methods. We verified our design, which consists of the preprocessing pipeline and a 6-LUTN classifier, by implementing it on a Xilinx Zynq-7000 ZedBoard. The complete system consumes a dynamic energy of 8.25 $\mu$J/inference, of which only 0.46 nJ is utilized by the LUTN classifier. These results show that both LGNs and LUTNs can be employed as lightweight hardware-based classifiers for inter-patient ECG arrhythmia classification.

---


### 288. [PolyTopoBench: A Benchmark for Complex Vector Polygon Generation from Remote Sensing Imagery](https://arxiv.org/abs/2609.32856)

**<font color=#1a73e8>作者：</font>** Zeping Liu, Ni Lao, Weiwei Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vector polygon generation converts visual inputs, e.g., remote sensing (RS) images, into vectorized polygonal geometries, supporting applications such as autonomous driving, vector map construction, and remote sensing. Early pipelines predict raster masks and post-process them into polygons, which prevents end-to-end optimization and may miss small objects or introduce inaccurate vertices. Recent methods directly generate vector polygons, but most focus on simple exterior contours, while they either cannot represent complex polygons with holes or fail to preserve their topology. In this paper, we propose PolyTopoBench, a unified evaluation framework for vector polygon generation from RS images with explicit emphasis on complex polygons. PolyTopoBench evaluates both exterior and interior rings, and benchmarks 11 representative methods, including segmentation-based polygonization pipelines, vision foundation model baselines, and specialized vector polygon generators, on two RS-image datasets covering buildings, roads, vegetation, and unvegetated regions. Experiments show that existing methods often recover simple exterior boundaries but degrade substantially on polygons with holes or multiple rings. These results reveal complex polygon generation as an unresolved challenge and motivate topology-aware benchmarks and model designs. Code and data are available at this https URL.

---


### 289. [Is H&E Image-to-Spatial Transcriptomics Simpler Than It Looks?](https://arxiv.org/abs/2609.32857)

**<font color=#1a73e8>作者：</font>** Duc T. Nguyen, Thanh Ha Do, Phuong M. Cao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Predicting spatial gene expression from routine H&E histology offers a scalable route toward spatial molecular profiling. Recent work has pursued increasingly sophisticated architectures to capture spatial context and richer expression structure. At the same time, simple estimators have shown strong performance in several studies, but what they already solve and where additional complexity is needed remain unclear. We study this behavior through the structure of prediction error under the mean-squared error (MSE) objective. Differences in average expression across genes can account for a substantial part of aggregate prediction performance, while a key unresolved error lies in recovering variation within each slide. Decomposing MSE into slide-level and within-slide components, we find that the within-slide component has lower residual-normalized parameter sensitivity in controlled neural experiments. This motivates Component-Guided Loss (CGL), which increases supervision of the within-slide component. CGL-Linear is a closed-form affine instantiation that achieves overall state-of-the-art performance across HEST-1k cohorts and gene-panel sizes. The same within-slide supervision improves existing neural models. These results suggest that substantial gains can come from aligning the training objective with prediction-error structure rather than increasing model complexity.

---


### 290. [Muon Under Gradient Noise and the Limits of Orthogonalization Near Optima](https://arxiv.org/abs/2609.32861)

**<font color=#1a73e8>作者：</font>** Xiaohui Xie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon replaces the momentum buffer of each weight matrix by its orthogonal polar factor. We ask what this orthogonalization does near an optimum, where minibatch noise dominates the gradient. Under a Gaussian noise model, the expected Muon update becomes a scaled gradient step, so a linear method with a suitably matched learning rate reproduces Muon's first-order mean response. The stochastic update is a different matter: after the response is matched, Muon retains a nonlinear residual that is uncorrelated with the input noise and contributes additional covariance. A Hermite expansion shows how momentum acts on this residual. Its higher-order components decorrelate faster than the linear component, so momentum suppresses the residual's accumulated covariance relative to the linear part, but never eliminates it. In a local quadratic surrogate that evaluates the residual on the stationary noise buffer, the residual adds stationary covariance and raises the stationary loss floor at every stable step size, while leaving the contraction dynamics unchanged. Simulations of the full nonlinear recursion on quadratics and measurements on frozen transformer gradients support each step of this picture. Together, the results make a theoretical case for replacing orthogonalization by response-matched momentum SGD once optimization becomes noise-dominated.

---


### 291. [SV2V-RSim: A Comprehensive Benchmark for Self-Selective V2V Cooperative Perception with Near-Realistic Data](https://arxiv.org/abs/2609.32863)

**<font color=#1a73e8>作者：</font>** Yulu Wu, Chao Wei, Jujun Cheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vehicle-to-Vehicle (V2V) cooperative perception enhances autonomous driving by enabling vehicles to share information beyond their direct line of sight. However, existing V2V datasets are limited by a small number of participating agents, static collaborator selection strategies, and a significant domain gap between simulated and real-world environments. To overcome these challenges, we introduce SV2V-RSim, a large-scale, multi-modal, near-realistic simulation dataset engineered to elevate agent diversity and realism. Additionally, we present the Select Vehicles Adaptively (SVA) module, which optimizes collaborator selection to balance perception performance against communication bandwidth constraints. Our dataset is generated using the Unreal Engine 5-based simulator that integrates high-fidelity 3D assets, diverse environments, and intricate traffic scenarios. All vehicles within a specified range of the ego vehicle are equipped with sensor suites, enabling dynamic and adaptive collaborator selection. SV2V-RSim encompasses four maps, four weather conditions, six time periods from sunrise to night, 203K LiDAR frames, 402K RGB frames, and 788K annotated 3D bounding boxes across 17 object classes, supporting a range of cooperative perception tasks such as 3D object detection, segmentation, and depth estimation. Benchmarking on recent cooperative perception algorithms demonstrates that SVA achieves a superior performance-bandwidth trade-off, while sim-to-real experiments and No-Reference Image Quality Assessment validate the dataset's high realism and practical effectiveness. Our dataset and code will be publicly available.

---


### 292. [Staying on the Attractor: Supervising Neural Surrogates of 3D Turbulence Where They Leave It](https://arxiv.org/abs/2609.32864)

**<font color=#1a73e8>作者：</font>** Yilong Dai, Shaswata Mitra, Raj Patel 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural surrogates are trained to predict 3D turbulent flows in place of direct numerical simulation (DNS). For chaotic flows, the goal is short-term pointwise accuracy followed by long-term physical and statistical fidelity. However, small prediction errors can carry a surrogate away from the flow's attractor. Off-attractor states are poorly represented in training data, leaving their evolution weakly constrained. The learned dynamics can then amplify deviations and lead to blow-up, freezing, or statistical drift. We propose off-attractor supervision (OAS) to supervise neural surrogates where they leave the attractor. OAS teaches the model how the true Navier-Stokes dynamics would evolve from these states. Each selected state is paired with its own future computed by DNS. Three generators select a few hundred states for relabeling. The first collects states from the surrogate's own rollouts. The second uses surrogate attacks to target freezing, excessive amplification, and violations of incompressibility and energy balance. The third perturbs training states along an amplified direction and a strongly damped random direction of the dynamics. All attacks run on the surrogate alone, and DNS relabeling is performed offline once per selected state. Experiments on $128^3$ turbulence show that OAS increases the median time to failure from 21 to 721 steps. The compared baselines achieve medians of at most 110 steps, and the advantage holds across training seeds. OAS also achieves the lowest pointwise error at step 15 and the best long-horizon statistics among the compared methods. OAS integrates physical models into neural simulation by extending supervision from fixed reference trajectories to states where the surrogate is likely to fail. This principle can guide the development of more reliable scientific surrogates when deployment takes models beyond the coverage of their training data.

---


### 293. [Improving Video Sparse Attention with Fine-grained Router and Sparse Rebasing](https://arxiv.org/abs/2609.32882)

**<font color=#1a73e8>作者：</font>** Peiyuan Zhang, Guoqiang Wei, Yilong Zhao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present VSA2, a frontier trainable sparse attention for video DiTs. VSA2 includes a variety of new architectural features and training procedures that we apply across all stages of the DiT development cycle, including pretraining, RL, and inference, to produce a DiT with comparable or better quality than a full attention counterpart. Architecturally, VSA2 introduces a fine-grained router that improves the precision of identifying critical tokens and supports dynamic computation by allowing each query to attend to a variable number of key-value pairs. In training, we identify a Hard-to-Easy Curriculum, where models trained under high sparsity and later evaluated with lower sparsity during inference not only generalize effectively, but also outperform models trained with full attention in motion quality. VSA2 is also flexible: it can replace full attention during the middle of progressive low-to-high resolution pretraining, rebasing early-stage full-attention checkpoints. Experiments show that VSA2 reduces attention computation by half over VSA with lower loss. On 720p videos, it accelerates attention by 8.9x and end-to-end generation by 4.62x compared to the FlashAttention-3 baseline, while achieving comparable or better video quality.

---


### 294. [Refreshing Less, Selecting Better: Reusing Stale Gradient Features for Efficient Influence-Based Data Selection](https://arxiv.org/abs/2609.32888)

**<font color=#1a73e8>作者：</font>** Jianchang Su, Yifan Zhang, Wei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gradient-based data selection methods such as LESS score each candidate by the alignment between its gradient and a target validation gradient, and recomputing per-example gradient features at every new checkpoint dominates their cost. Across three selection seeds, two model families, two candidate pools, and two target tasks, features cached at a post-warmup checkpoint and paired with fresh validation gradients preserve the ranking 40 optimizer steps later with Spearman correlation from 0.952 to 0.991, while the top-10% subset they induce misses 10 to 22% of the examples that full recomputation selects. We therefore propose Cached Diverse Influence Selection (CDIS), which recomputes gradient features for the top-ranked fraction $p$ of candidates under the stale scores, fits an affine calibration on the recomputed examples, and selects the final subset under source and length quotas. A refresh fraction at or above the selection fraction recovers the exact top-$k$ subset whenever the calibrated stale scores have bounded error, and the budget curves follow this rule: at $p=0.3$ the recovered top-$k$ subset coincides with full recomputation in every setting, allocating the same budget per stratum recovers the stratified subset at 0.92 to 1.00, and gradient-stage wall-clock drops 3.5 to 3.6 times. Iterating the cache over four checkpoints keeps top-$k$ overlap at 0.98 or higher at 1.9 gradient features per example against 4 for full recomputation, and stale-to-recomputed agreement on the refreshed examples provides a free check for unsafe reuse. Downstream, unconstrained top-$k$ selection collapses to a single data source and scores 13 points below random selection on GSM8K. CDIS scores 12 points above random selection with paired confidence intervals that exclude zero and trails full recomputation by 4.3 points, one training-run standard deviation, at 3.4 times lower selection cost.

---


### 295. [Measurement-Gated Provenance Attenuation for Frozen EEG Representations](https://arxiv.org/abs/2609.32889)

**<font color=#1a73e8>作者：</font>** Anuar Aimoldin, Yankai Chen, Ayana Mussabayeva 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Frozen EEG representations retain acquisition signatures as well as neural activity. Source predictability alone does not identify what should be removed: it can reflect measurement effects or genuine biological and population differences, which should not be erased. We propose Measurement-Gated Provenance Attenuation (MGPA), built on one principle: measurement evidence determines where correction may act, and preserved information determines what it should aim for. Paired measurement contrasts define a gate outside which nothing changes; inside it, the source score is moved to the value the preserved coordinates already predict: for a fixed affine score, this keeps the same information as any target set by those coordinates and needs the least expected squared movement. Closed-form and critic-guided iterative constructions apply it without source identity or encoder retraining. Three studies test the principle at increasing distance from its assumptions. Under controlled reference changes, where the source-task association is known, MGPA brings source to near chance with task performance unchanged, whereas erasing what predicts source (LEACE) lowers frozen-task AUROC from .753 to .656 while barely touching source; ablations attribute the attenuation to the gate's directions and 2.7x less movement to the conditional target. Across recordings from different devices and electrodes, iterative correction lowers source accessibility while preserving or improving task performance. Finally, one iterative map selected on one task and reused unchanged on existing heads for two others raises their worst-association AUROC (lowest over device-label shifts) by .057 and .019 over LEACE, at a cost to those heads while the training association holds. A reusable correction shows its value in how an existing predictor behaves once acquisition cues stop being reliable, not only in what a probe can read.

---


### 296. [Optimizing H-Graph Hybridization for Diffusion-Guided RRT](https://arxiv.org/abs/2609.32897)

**<font color=#1a73e8>作者：</font>** Omer Talmi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sampling-based motion planners guided by diffusion models produce high-quality trajectories in a single run, yet the stochastic diversity available at inference time is left largely unexploited. We present two inference-time diversification strategies for a fixed, pretrained DiTree model, combined via H-Graph hybridization, and evaluate them on a holonomic AntMaze robot across 15 maze scenarios. The first, factorial diversity, sweeps the random seed and Diffusion Goal Bias (DGB) parameter, the second, refinement-only diversity, sweeps the diffusion refinement strength (RS) that controls how much an RRT-generated trajectory is edited. Because a single-run baseline only partially succeeds, we additionally compare H-Graph results with pool-based statistics. H-Graph improves the mean pool length of the factorial and refinement-only diversities by 18.8% and 14.5%, respectively. In addition, it also improves the best individual candidate's lengths by 9.7% and 6.8%, respectively. And last, compared with the successful baseline's trajectory length, it improves the results by 18.2% and 19.9%, respectively. These results show that inference-time parameter variation is a reliable, training-free source of path diversity, and that H-Graph hybridization reliably converts this diversity into shorter, higher quality trajectories.

---


### 297. [When Less Compute Is More: Adaptive Early Exit Improves Pretrained Outlier Detection](https://arxiv.org/abs/2609.32898)

**<font color=#1a73e8>作者：</font>** Tianyang Zhou, Leman Akoglu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretrained tabular foundation models process every dataset at a fixed depth, with inference costs growing with dataset size. To address this, we present the first study of depth-adaptive early-exit for pretrained outlier detection models. While early-exit is typically motivated by efficiency, we uncover a surprising benefit: exiting at the optimal intermediate layer can also improve detection performance on diverse real-world benchmarks by 4.7-7.3% on average, consistent across three distinct foundation models. First, we investigate the factors driving these gains, and identify a key mechanism: context pollution, i.e., the presence of outliers among in-context samples. Our analysis reveals that nearby in-context samples exert increasing influence on query predictions at greater depths, consistent with a retrieval-based view of these models. In effect, early-exit alleviates the adverse effects of retrieving accurate-yet-polluted neighbors, with gains of 13-21% when context pollution matches the natural outlier rate. Motivated by these findings, we pretrain a plug-in router to select a dataset-specific exit layer, using query outlier labels as privileged information available only during router training. The router operates post hoc, leaving the base model parameters and prediction head unchanged. Experiments on three large real-world benchmarks show that, on clean context, the router recovers up to 45% of the oracle gain with up to 1.8x speedup across three pretrained backbones, with larger gains as context pollution increases.

---


### 298. [Rethinking the Fully Hyperbolic Vision Transformer in Polar Coordinates](https://arxiv.org/abs/2609.32899)

**<font color=#1a73e8>作者：</font>** Ahmad Bdeir, Niels Landwehr  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperbolic space can embed intrinsic hierarchies in data with low distortion due to the exponential growth of volume with distance from the origin. However, current Lorentz transformer blocks are formulated in ambient coordinates, where numerical errors increase at large radii due to instability in the Lorentzian inner product, leading many models to limit the radius to avoid this issue. This prevents us from utilizing the regions of hyperbolic space that motivate the geometry. To address this, we revisit the components of the transformer block in polar coordinates, where hyperbolic operations such as distance calculation and attention centroids can be computed without the numerical cancellation in their ambient-coordinate formulations. Specifically, we propose a polar fully connected layer that separately maps an embedding's direction and radius, allowing the radius of a feature to be learned rather than determined by the norm of a linear map. We additionally introduce horospherical shifts as relative positional encodings whose query-key distances grow logarithmically with the token gap. Finally, we reformulate the residual connection as average radius Lorentz boosts. Combining these components, we develop a fully hyperbolic transformer that substantially improves performance over Euclidean and hyperbolic baselines on standard vision tasks. We further evaluate our model on ImageNet and demonstrate its ability to generalize to other datasets using pre-trained weights, similar to Euclidean counterparts.

---


### 299. [Predicting the Next State Is Not Enough: JEPA Representations for Lean Theorem Proving](https://arxiv.org/abs/2609.32908)

**<font color=#1a73e8>作者：</font>** Aarnav Choudhary  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural theorem provers must both propose tactics and decide which valid successor states to explore. We study whether one-step Lean transitions provide a self-supervised signal for branch ordering. A JEPA-style model predicts latent successor representations and scores only kernel-validated, nonterminal successors generated by a fixed pretrained ByT5 proposer. JEPA achieves higher Top-1 than matched InfoNCE on a same-theorem ranking diagnostic(50.18% versus 31.55%), but averages 282.3 of 987 solved theorems across three seeds versus 308 for proposer ordering, while requiring more tactic checks. In this setting, accurate one-step transition ranking is therefore insufficient as a long-horizon search value. The controlled evaluation separates representation from proposal quality and treats kernel-checked proof completion as the primary endpoint.

---


### 300. [AgentTell: Behavioural Side-Channel Leakage in Browser-Use Agents](https://arxiv.org/abs/2609.32915)

**<font color=#1a73e8>作者：</font>** Asif Shahriar, Md Nafiu Rahman, Sadif Ahmed 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Browser-use agents often carry information in their context as they move between websites. While it may be necessary for task completion, it also creates a privacy risk, especially when the information contains a private fact regarding the user. For example, an agent may learn a user's affiliation after reading a membership record. If it later selects a registration option specific to that affiliation on another website instead of a general option, the information gets leaked. In this work, we define and study behavioural side-channel leakage in browser-use agents, where an agent's actions inadvertently reveal private information (secret) retained from a prior website, despite an explicit instruction not to disclose it. We introduce AgentTell, a benchmark of 20 scenarios and 100 tasks in which an agent acquires a secret on one website and then completes a task on another website that offers secret-specific actions alongside a general action that reveals nothing. Our evaluation across 9,760 sessions on six backbones shows that agents carrying a secret reveal it through their actions in 61.1% of sessions. Even when agents explicitly state in memory that the secret must not be shared, they still reveal it in 56.7% of those sessions. Moreover, in 34.5% of leaking sessions, their final responses falsely assure users that the secret was not disclosed. These findings show that agents often fail to recognize side-channel leakage as a privacy risk.

---


> [!TIP]
> 当前位于：**251-300**（第 6/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-908](./part-19.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
