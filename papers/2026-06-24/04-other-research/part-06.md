# 📦 其他研究 | 2026年06月24日

> 本类共 **654** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-654](./part-14.md)

---

### 251. [VT-DUDA: Visual Token Conditioning for Diffusion-guided Unsupervised Domain Adaptation](https://arxiv.org/abs/2606.21700)

**<font color=#1a73e8>作者：</font>** Xuan Qi, Daniele Berardini, Dario Serez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised domain adaptation (UDA) aims to learn a target-domain classifier from labeled source data and unlabeled target data under distribution shift. Recent diffusion-based UDA methods approach this problem by synthesizing labeled target-style images and training on the resulting synthetic data. However, their performance depends heavily on the conditioning design: class prompts provide only coarse guidance, while domain adaptation modules mainly control appearance, which may leave target-style synthesis insufficiently specified. We propose VT-DUDA, a visual-token conditioning framework for diffusion-guided UDA. Instead of relying only on text prompts, VT-DUDA uses source images to provide additional instance-level visual context for target-style synthesis. Specifically, VT-DUDA maps each source image to a compact sequence of visual tokens and forms a hybrid conditioning context by concatenating these tokens with the corresponding text embeddings along the cross-attention context dimension of a latent diffusion model. This provides instance-dependent conditioning beyond text alone, while synthesis is performed with the target-domain adapter branch. Because guidance is represented explicitly as a token sequence, the same interface also permits inference-time manipulation of the conditioning signal through token selection and token-strength adjustment. The proposed method preserves the standard diffusion objective and can be integrated into existing adapter-based diffusion frameworks without modifying the backbone. Across Office-31, Office-Home, and VisDA-2017, VT-DUDA improves average target-domain accuracy over strong discriminative and diffusion-based UDA baselines. The results suggest that, in generation-based UDA, a stronger conditioning interface can improve the downstream usefulness of synthetic target-style data.

---


### 252. [When Compression Helps and When It Hurts: Condition-Aware Analysis of Chain-of-Thought Distillation](https://arxiv.org/abs/2606.21704)

**<font color=#1a73e8>作者：</font>** Siyang Lyu, Zhijing Sun, Xinghao Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chain-of-Thought (CoT) distillation transfers multi-step reasoning from large reasoning models to smaller students, but verbose teacher traces inflate both training and inference cost. Existing CoT compression methods fall into two families, selective pruning and generative rewriting, yet prior studies have left key factors entangled: granularity is confounded with importance criteria in pruning, restructuring level is rarely isolated in rewriting, and compression budgets are not systematically evaluated across domains or regimes. We recast CoT compression along three dimensions: importance criterion, restructuring level, and compression budget. Sweeping these across two model families, Math and General domains, and Long-/Short-CoT regimes, we find that (i) importance criterion utility is strictly governed by granularity: step-level criteria converge on a shared reasoning backbone, while token-level pruning requires symbol-aware signals to preserve the logical core; (ii) restructuring level inverts across domains: Math degrades monotonically with structural disruption, while aggressive rewriting acts as a denoiser on General tasks; (iii) training-time compression does not necessarily translate to inference-time savings: Long-CoT students retain verbose habits despite concise supervision, making the training ratio an optimistic lower bound on deployment cost. These findings yield condition-aware guidelines for matching compression to deployment context.

---


### 253. [Structural Assessment for Understanding and Guiding Dataset Distillation in Discrete Token Space](https://arxiv.org/abs/2606.21705)

**<font color=#1a73e8>作者：</font>** Yue Cao, Jianyang Gu, Vyacheslav Kungurtsev 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dataset distillation (DD) has proven to reduce training cost while preserving accuracy. While promising, the factors that make one distilled dataset more effective than another remain poorly understood. In this work, we investigate this question through the lens of discrete visual tokenizers. Whereas many prior DD efforts emphasize matching global data distributions, we suggest that the effectiveness depends on which semantic concepts are captured and how they are composed. Discrete visual tokenizers provide a finite vocabulary that enables direct statistical analysis of such compositional structure. Through quantitative analysis of token-level statistics, we introduce the structural score to measure the adequacy of token compositions. We observe that distilled datasets with balanced token composition yield higher validation performance. On the other hand, divergence from the original data does not necessarily harm performance. We further show that samples with high structural scores in the discrete token space can effectively guide diffusion-based DD. Our findings highlight the importance of token composition in dataset effectiveness, offering a principled complement to distributional similarity considerations in DD.

---


### 254. [Entropy Objectives in Markov Decision Processes](https://arxiv.org/abs/2606.21726)

**<font color=#1a73e8>作者：</font>** S. Akshay, Raghav Goyal, Aditya Neeraje 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We consider the problem of synthesizing control policies that enforce a concentration property on the state distributions of a stochastic system. We present a formalization of this problem in terms of synthesizing strategies for maintaining an entropy-based objective in Markov Decision Processes (MDPs). We first show that even relaxed versions of this problem are complexity-theoretically hard. We then present a sound and (conditionally) relatively complete method to verify and synthesize strategies for such entropy objectives. The main challenge is the non-linear nature of such objectives, and our approach addresses this by exploiting and combining ideas from convex duality and invariant synthesis. We also investigate the role of memory and randomization in ensuring entropy objectives. Finally, we implement our ideas to evaluate our approach empirically on a few illustrative benchmarks.

---


### 255. [Embedding Linear Equality Constraints in Probabilistic Neural Networks for Dynamic Modelling](https://arxiv.org/abs/2606.21728)

**<font color=#1a73e8>作者：</font>** Matthew Marsh, Benoit Chachuat, Antonio del Rio Chanona  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning models are increasingly used to model chemical process systems, yet they often lack principled uncertainty quantification and mechanisms to enforce physical constraints. We propose a probabilistic neural network framework that guarantees satisfaction of linear equality constraints within a given tolerance, while capturing aleatoric uncertainty. Compared to state-of-the-art methods, our formulation demonstrates improved predictive accuracy, uncertainty calibration, and adherence to constraints on reduced data. It also demonstrates competitive performance, but with significantly faster training times when evaluated on large data regimes. We evaluated this on two batch reactor case studies, enforcing mass balances.

---


### 256. [HPP: Hierarchical Programmatic Probing for Long Video Understanding by Decoupling Perception and Reasoning](https://arxiv.org/abs/2606.21734)

**<font color=#1a73e8>作者：</font>** Awais Rauf, Ahmed Hasssan, Greg Slabaugh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding long videos requires fine-grained perception and multi-step, higher-order reasoning over complex, long-range spatio-temporal dynamics. Vision-language models (VLMs) encode video frames into visual tokens and attempt to perform both perception and multi-step planning latently, within a single forward pass. This coupled formulation, however, is bottlenecked by the LLM's limited capacity to discover and execute multi-step strategies in its latent representations. To address this bottleneck, we propose Hierarchical Programmatic Probing (HPP), a framework that decouples semantic perception from higher-order temporal reasoning by reformulating long video understanding as iterative, programmatic exploration of a hierarchically segmented video. Specifically, a coding-capable LLM plans and executes a multi-step strategy in an interactive coding environment, probing the video for information and invoking a VLM for localized perception on demand. To make probing tractable over long videos, we introduce three components: information-density-aware hierarchical segmentation, late-interaction semantic retrieval, and structured probing functions for coarse-to-fine temporal localization. We validate HPP on LongVideoBench, which requires both fine-grained perception and long-range relational reasoning, and show that decoupling the two via iterative programmatic probing yields substantial gains. Further results on EgoSchema, VideoMME, and MLVU demonstrate the effectiveness of our approach across diverse long-video benchmarks.

---


### 257. [Adversarial Domain Prompt Tuning and Generation for Single Domain Generalization](https://arxiv.org/abs/2606.21736)

**<font color=#1a73e8>作者：</font>** Zhipeng Xu, De Cheng, Xinyang Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single domain generalization (SDG) aims to learn a robust model, which could perform well on many unseen domains while there is only one single domain available for training. One of the promising directions for achieving single-domain generalization is to generate out-of-domain (OOD) training data through data augmentation or image generation. Given the rapid advancements in AI-generated content (AIGC), this paper is the first to propose leveraging powerful pre-trained text-to-image (T2I) foundation models to create the training data. However, manually designing textual prompts to generate images for all possible domains is often impractical, and some domain characteristics may be too abstract to describe with words. To address these challenges, we propose a novel Progressive Adversarial Prompt Tuning (PAPT) framework for pre-trained diffusion models. Instead of relying on static textual domains, our approach learns two sets of abstract prompts as conditions for the diffusion model: one that captures domain-invariant category information and another that models domain-specific styles. This adversarial learning mechanism enables the T2I model to generate images in various domain styles while preserving key categorical features. Extensive experiments demonstrate the effectiveness of the proposed method, achieving superior performances to state-of-the-art single-domain generalization approaches.

---


### 258. [Cohort Organized Learning: Clustering Through Agreement](https://arxiv.org/abs/2606.21743)

**<font color=#1a73e8>作者：</font>** Finn Henry O'Shea, Maria Elena Monzani  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In this article we describe Cohort Organized Learning (CoOL), a method for clustering data without explicit distance or similarity computations. Herein, we will describe CoOL, derive the gradients determined by expectation maximization to train the networks, show how to monitor convergence during training and evaluate the clusters after training, and discuss a series of examples and use cases. We also discuss CoOL's limitations and future prospects on related tasks. Because CoOL uses neural networks to estimate the clusters, it can be used to cluster any data that can be made compatible and we illustrate this on vector data and images.

---


### 259. [Quantile Adaptive Temperature Scaling for Confidence Calibration](https://arxiv.org/abs/2606.21749)

**<font color=#1a73e8>作者：</font>** Omprakash Chakraborty, Leo Fillioux, Ismail Ben Ayed 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep neural networks often produce poorly calibrated confidence estimates, overstating their certainty even when predictions are incorrect. Temperature Scaling remains the most widely used posthoc calibration method due to its simplicity and effectiveness, yet its global, uniform rescaling of logits fails to correct the highly heterogeneous structure of miscalibration observed across the confidence spectrum. In particular, the largest correctness confidence discrepancies arise in different quantile regions depending on the setting, low confidence predictions, where uncertainty matters most, tend to exhibit the largest correctness confidence discrepancies, which standard TS leaves largely unaddressed. We introduce Quantile Adaptive Temperature Scaling (QaTS), a simple and efficient post hoc calibration method that adapts the temperature as a function of a predictions empirical confidence quantile. By mapping confidences into the quantile space, QaTS normalizes the calibration problem, makes the structure of miscalibration explicit and enables a monotone temperature function that adapts across quantiles while leaving well calibrated high confidence predictions largely unchanged. preserving high confidence behavior. This quantile aware formulation aligns naturally with a reparameterized Expected Calibration Error (ECE) objective and yields a sample wise temperature that is robust across a variety of challenging scenarios, such as class imbalance and distributional shifts. Across a broad range of datasets, architectures, evaluation scenarios and diverse tasks, QaTS consistently, and substantially, outperforms state of the art post hoc calibration methods, delivering more reliable and trustworthy confidence estimates without modifying model predictions.

---


### 260. [AdaPrivate-TS: Private Thompson Sampling for Contextual Bandits with Privacy Amplification](https://arxiv.org/abs/2606.21757)

**<font color=#1a73e8>作者：</font>** Mohammadreza Riyazat, Eranga Ukwatta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present AdaPrivate-TS, a differentially private contextual bandit algorithm that combines Thompson Sampling with batched zCDP composition. Our key insight is that differential privacy noise inflates the posterior covariance in a structured way: adding Gaussian noise $N(0,\sigma^2 I)$ to $b$ yields sampling covariance $v^2 A^{-1} + \sigma^2 A^{-2}$, which Thompson Sampling interprets as increased uncertainty rather than pure corruption. Under event-level privacy (protecting individual interactions) with stochastic contexts, we prove that the privacy cost is only $O(\sqrt{d}\,\log T/\sqrt{\rho})$, logarithmic in $T$, because parallel composition amortizes noise across batches. Additionally, we explore privacy amplification via Poisson subsampling, which can reduce effective noise at stringent privacy budgets. Experiments on synthetic and real-world datasets demonstrate: (1) AdaPrivate-TS achieves 93-99% of non-private performance at $\varepsilon \in [0.5, 5]$, outperforming UCB by 0.5-3.7% and up to 18% with tuned adaptive exploration at extreme $\varepsilon$; (2) privacy amplification provides additional 2-5% gains at low $\varepsilon$; (3) on MovieLens and Jester, AdaPrivate-TS achieves the best overall performance among event-level baselines, dominating at $\varepsilon \geq 2$; (4) under DP-SVD private features, TS's advantage over UCB grows to +11%, confirming noise-as-uncertainty is not limited to reward privacy. We provide rigorous proofs for privacy guarantees under interactive zCDP composition and comprehensive evaluation including convergence curves, 12-seed CIs, and DP-SVD feature ablation.

---


### 261. [From Gradient Clipping to Structural Refinement: Improving DPSGD for Medical Image Segmentation](https://arxiv.org/abs/2606.21763)

**<font color=#1a73e8>作者：</font>** Shiva Parsarad, Parth Shandilya, Isabel Wagner  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image segmentation is widely used for disease detection but relies on sensitive data, raising privacy concerns as trained models can leak information. Differential privacy, typically implemented via Differential Private Stochastic Gradient Descent (DPSGD), provides a solution, though at the cost of reduced utility. Recent DPSGD variants, including Automatic clipping (Auto-S), Normalised SGD with perturbation (NSGD), and Per-sample adaptive clipping (PSAC), have shown promise in image classification, but their behavior in medical segmentation remains underexplored. We evaluate these methods across binary and multi-class tasks and analyze gradient alignment, showing that prior assumptions, particularly for PSAC, do not consistently hold. We further demonstrate that combining clipping strategies with morphological refinement improves segmentation quality under privacy constraints. Finally, we propose an adaptive DP-Morph variant that captures class-specific structures and enhances performance in multi-class settings.

---


### 262. [Motion-Aware Reinforcement Learning For Object Localization](https://arxiv.org/abs/2606.21764)

**<font color=#1a73e8>作者：</font>** Prithvi Raj Singh, Satyendra Singh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present MARLNet (Motion-Aware Reinforcement Learning Network), a PPO-based bounding-box refinement agent that incorporates a constant-velocity motion prior into the observation state and an action smoothness penalty into the reward function. The agent operates on 268-dimensional observations encoding the current proposal, a kinematic prediction, the previous action, and a 256-dimensional EfficientNet-B0 crop feature, and learns a five-dimensional policy controlling coordinate adjustments and a binary termination trigger. Evaluated on Pascal VOC 2012 and VisDrone 2019, MARLNet trains stably across all regularization strengths tested and achieves consistent gains in detection success rate at $\text{IoU} \geq 0.5$: up to $+0.011$ on VOC ($\lambda_\text{phys}{=}0.10$), where the motion prior prevents the overshooting that causes plain PPO to regress on this metric, and $+0.007$ on VisDrone ($\lambda_\text{phys}{=}0.70$), where unconstrained PPO achieves a larger gain ($+0.025$) owing to the weaker base detector. Through reward design ablations and training dynamics analysis, we identify a reward interference in which combining a constant-velocity deviation penalty with an absolute IoU term causes trigger collapse, and show that replacing it with the action smoothness penalty resolves this failure. We further characterize a representational ceiling facing crop-feature refinement agents that share a backbone with their base detector, confirmed through a global-plus-local observation ablation. Project page: this https URL

---


### 263. [Decision-Focused Learning: When and Why Traditional Prediction Models Fail](https://arxiv.org/abs/2606.21773)

**<font color=#1a73e8>作者：</font>** Mo Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Plugging predictions of unknown parameters into downstream optimization problems, often referred to as the ``predict-then-optimize'' paradigm, has long been a standard approach in decision-making under uncertainty. However, improved predictive accuracy does not, in general, translate into improved decision quality. This disconnect has motivated growing interest in decision-focused learning (DFL) within the operations research community. This tutorial reviews recent developments in DFL and highlights key methodological insights, with a particular focus on stochastic linear programming as the downstream decision-making problem. We discuss why several widely used tools in traditional statistical learning are not directly suited to decision-focused settings and must be rethought, including (i) data collection strategies driven purely by predictive uncertainty and (ii) distributional distance measures such as the Wasserstein distance. We summarize properties of DFL that distinguish it from conventional predictive modeling and provide insights into the development of new decision-focused tools.

---


### 264. [A Causal DAG Prior for Synthetic Time-Series Classification Datasets](https://arxiv.org/abs/2606.21776)

**<font color=#1a73e8>作者：</font>** Franco Martino O'Rourke, Ana Trisovic, Dimitris Bertsimas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A Prior-data fitted Network learns the posterior predictive induced by its training prior; bringing this paradigm to multivariate time-series classification therefore calls for a synthetic generator that produces complete labelled datasets with temporal structure. We introduce a causal prior that synthesizes each dataset from a randomly sampled DAG over typed nodes across two modalities (tabular attributes and time series), natively producing multivariate, multi-class TSC datasets with cross-modal causal structure across channels, timesteps and labels, a regime not addressed by existing synthetic priors. To validate the prior, we finetune TabPFN v2.5 with minimal adaptations and evaluate on 75 UCR/UEA datasets within TabPFN's operating regime. Finetuning on our generator significantly outperforms both the unmodified upstream model and a tabular-only ablation of the same prior (Wilcoxon signed-rank $p=3.0\times 10^{-8}$ on ROC-AUC), isolating the contribution of the cross-modal temporal structure.

---


### 265. [CalVerT: Augmenting Agents with Calibrated Verifier Telemetry Improves Action and Learning in Knowledge-Intensive Tasks](https://arxiv.org/abs/2606.21777)

**<font color=#1a73e8>作者：</font>** Ashwin Vinod, Ying Ding, Elias Stengel-Eskin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents in knowledge intensive question answering take retrieval and reasoning actions with incomplete knowledge about whether their current answer is uncertain, unsupported, or already complete. This produces two failure modes: committing to confident but unsupported answers, which hurts accuracy, and over-retrieving when the evidence in hand already suffices, resulting in wasted compute. To give agents a more complete picture of the state space they are operating in, we introduce calibrated verifier telemetry (CalVerT), which augments the agent's state with additional telemetry: a calibrated self-confidence score and a grounding verifier score. We show that CalVerT can improve agents in both training-free and training-based settings. On four QA benchmarks, we find that CalVerT raises F1 by triggering retrieval in cases where agents over-rely on parametric knowledge, while cutting redundant retrieval in cases where agents have sufficient context to answer. We show that CalVerT can augment existing QA frameworks without training. Moreover, CalVerT also improves trained systems: by simply augmenting an agent's state with telemetry, we observe improvements after reinforcement learning, as compared to an agent with identical training but no CalVerT telemetry.

---


### 266. [FrogBard-512: Design and Experimental Evaluation of a Four-Voice Permutation-Based Hash Function](https://arxiv.org/abs/2606.21779)

**<font color=#1a73e8>作者：</font>** Victor Duarte Melo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> FrogBard-512 is an experimental 512-bit hash function based on a custom 2048-bit permutation organized as four 512-bit voices. The sequential mode uses a 1024-bit rate, a 1024-bit capacity, 128-byte message blocks, and a 16-round permutation. Each round combines public round constants, four AES-derived affine-equivalent byte substitutions, ARX quarter-rounds, a parity-dependent cross-voice mixing layer, and fixed lane permutations. The design also includes a separately domain-separated tree mode with 1 MiB leaves, multithreaded processing, and an AVX2 backend for four independent equal-length messages.
This paper gives a self-contained description of the construction, constant generation, padding, finalization, tree encoding, implementation profiles, and conformance vectors. It also reports an experimental evaluation covering fixed-vector tests, streaming equivalence, permutation inversion, scalar and SIMD agreement, sanitizer runs, Valgrind-based memory and race analysis, randomized API testing, libFuzzer, AFL++, reduced-round diffusion measurements, and large-stream statistical testing with PractRand and Dieharder.
The reported results provide evidence of implementation consistency and the absence of obvious statistical defects in the tested configurations. They do not establish collision resistance, preimage resistance, indifferentiability, or structural security. FrogBard-512 remains a research prototype and has not undergone independent cryptanalysis.

---


### 267. [What Do Lorentz-Equivariant Jet Taggers Learn?](https://arxiv.org/abs/2606.21790)

**<font color=#1a73e8>作者：</font>** Jay Agarwal, Siddharth Khare, Dhruv Kumar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study what Lorentz-equivariant jet taggers learn internally, using equivariance tests, linear probes and grade ablations across five models including L-GATr, L-GATr-slim and LLoCa-T. Linear probes show that equivariant models suppress frame-dependent pseudorapidity to zero while encoding jet mass and N-subjettiness strongly. Grade ablations on L-GATr reveal that bivector channels are negligible for top-quark tagging while vector-like channels are dominant but seed variable, consistent with the network exploiting multiple representational pathways. These results characterize which physical features and algebraic grade structures carry discriminative information in equivariant taggers and may inform future development of such models.

---


### 268. [Discretizing Reward Models](https://arxiv.org/abs/2606.21795)

**<font color=#1a73e8>作者：</font>** Vijay Viswanathan, Shiqi Wang, Devamanyu Hazarika 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite their widespread use, the role of reward models in shaping reinforcement learning is poorly understood. Reward models offer a tempting promise: they automatically estimate response quality in the absence of verifiers or human judges. Unlike "verifiable rewards" which typically produce binary scores, reward models typically produce continuous scores, allowing them to be sensitive to fine-grained differences in responses. However, we show this apparent strength is a serious weakness: many popular reward models are oversensitive, assigning different scores to equally good responses. Theoretically, we show that seemingly perfect reward models can be highly oversensitive; empirically, this oversensitivity can lead to bad policies. In place of existing notions of "reward model accuracy," we propose evaluating reward models using distinct measures of "discriminative ability" and "specificity" (the complement of oversensitivity). As a solution, we describe a training-free algorithm that uses Monte Carlo dropout on any neural reward model to produce discrete reward clusters. Theoretically, we prove there exist discretizations that reduce oversensitivity at minimal expense of discriminative ability; empirically we show, in both controlled and natural RL settings, that discretizing rewards leads to less reward hacking and better policies than training on the original rewards.

---


### 269. [Causal Variational Deep Embedding: A Family of Interventional Generators for Confounded Images](https://arxiv.org/abs/2606.21806)

**<font color=#1a73e8>作者：</font>** Jingyuan Chen, Kangrui Ruan, Junzhe Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep generative models reproduce the observational distribution of their training data, inheriting any spurious associations it contains. A common source is an unobserved confounder that shapes both an attribute the user wants to control at sampling time and an attribute expected to vary in response. Existing causal generative approaches resolve the resulting ambiguity by imposing structural assumptions strong enough to single out one interventional distribution; in image domains, such assumptions are rarely warranted, and the data is generally consistent with a set of distinct causal mechanisms -- a feasible region of interventional distributions. We propose CauVaDE (Causal Variational Deep Embedding), built on a canonical augmented SCM in which the unobserved confounder collapses, without loss of generality, into a discrete latent cluster of bounded support while continuous variation is absorbed into independent noises. We prove that this canonical class is dense, in both observational and interventional Wasserstein distance, in the class of augmented SCMs compatible with a given causal diagram, and instantiate it as a mixture variational autoencoder whose cluster variable plays the role of the canonical confounder. An entropy regularizer with weight $\gamma$ on the cluster posterior then traces a family of candidate causal effects that fit the observational data to comparable likelihood while spanning the feasible region. Experiments on image data benchmarks show that CauVaDE produces diverse interventional samples and improves FID against an unconfounded reference.

---


### 270. [Causal Gaussian Processes for Robust Treatment Effect Evaluation with Unobserved Confounding](https://arxiv.org/abs/2606.21809)

**<font color=#1a73e8>作者：</font>** Junzhe Zhang, Jingyuan Chen, Elias Bareinboim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The presence of confounding bias poses a key challenge in policy evaluation, as the target causal effects of actions are not identifiable (i.e., underdetermined) from observational data. On the other hand, existing confounding-robust evaluation strategies require detailed prior knowledge about the environment or apply only to discrete treatments and outcomes. This paper investigates causal effect evaluation over the continuous domain from confounded observations, while requiring only basic temporal ordering between the treatment and the outcome. We introduce a universal discretization of the exogenous domains that approximates the observational and interventional distributions of any causal model with arbitrary accuracy using a finite number of latent states. Building on this newfound universal approximation property, we develop a novel family of Causal Gaussian process (CGP) models that effectively approximate the observational and interventional distributions of any causal model with confounded observations.

---


### 271. [RAPID: A Reproducible Multi-Agent Pipeline for Interpretable Disaster Damage Assessment from Satellite and Street-View Imagery](https://arxiv.org/abs/2606.21819)

**<font color=#1a73e8>作者：</font>** Yifan Yang, Wenjing Gong, Kaili Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Due to the increasing frequency and intensity of extreme climate events, there is a clear demand for intelligent, scalable, and autonomous approaches to disaster damage assessment. Existing methods, largely based on supervised learning and task-specific fine-tuning, struggle to generalize under domain shifts, long-tailed data distributions, and heterogeneous geospatial data sources, especially in disaster scenarios. They also often lack the ability to integrate and reason across multimodal geospatial information, such as satellite images and street-view images. In this paper, we introduce RAPID, a reproducible multi-agent pipeline for interpretable disaster damage assessment, including damage-level assessment, damage-type interpretation, and actionable suggestions for response, remediation, and recovery. RAPID coordinates specialized agents to perform cross-view understanding, image restoration, structured damage recognition, and geographical reasoning across heterogeneous data modalities. Without task-specific fine-tuning, RAPID supports zero-shot damage assessment by jointly using complementary information from remote sensing and ground-level perspectives. The system produces fine-grained, interpretable assessments and automatically generates location-specific, decision-relevant disaster reports to support early-stage emergency response. We evaluate RAPID across hurricanes, floods, wildfires, and earthquakes using multiple cross-view imagery inputs, including pre- and post-disaster street-view images, post-disaster remote sensing imagery, and street-view image pairs. Experiments show that RAPID achieves 0.92 overall accuracy for multi-disaster type classification and up to 0.627 for cross-view damage severity prediction, highlighting its potential as a foundational framework for autonomous disaster intelligence.

---


### 272. [Local Causal Attribution of Chain-of-Thought Reasoning](https://arxiv.org/abs/2606.21821)

**<font color=#1a73e8>作者：</font>** Dennis Wei, Yannis Belkhiter, Erik Miehling 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding the causal structure of a language model's thought process is a problem of significant importance for both transparency and safety. In this work, we take a local approach toward this goal by analyzing the causal relationships among individual components, termed units, of a given, specific chain-of-thought trace. We construct a structural causal model on these units and relate each unit to the log probability of generating (subsequent) output units. Our algorithm, termed AttriCoT, is a black-box method that performs attribution by estimating importance parameters in the structural causal model using $O(U)$ forward passes through the model, where $U$ is the number of units. Evaluation of perturbation curves across 5 datasets and 4 reasoning models shows that AttriCoT produces attributions that are more faithful to the model's behavior than alternative methods. The attribution results also reveal notable differences in thought structure between models and domains.

---


### 273. [Mat-Pref: Verifiable-Reward Training Improves Compositional Reasoning in Inorganic Materials](https://arxiv.org/abs/2606.21830)

**<font color=#1a73e8>作者：</font>** Sarrah R. Mikhail Leung, Taehan Kim, Jeongbin Park  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from verifiable rewards (RLVR) has driven rapid progress in mathematical and code reasoning, but when extended to science, existing benchmarks do not decompose what generalizes: do gains reflect structural transfer, property transfer, or memorization? We introduce Mat-Pref, a benchmark of 10,837 ionic-substitution questions across 11 inorganic structure families, grounded in density functional theory calculations from the Materials Project, with three evaluation splits that isolate in-distribution performance, generalization to entirely held-out structure families, and cross-property transfer: applying band-gap reasoning to hosts seen during training only through formation-energy supervision. Four zero-shot frontier models (70-671B parameters) remain in the 33-54% range on every split, confirming that scale alone does not resolve the compositional chemical reasoning this task demands. A two-stage pipeline of supervised fine-tuning followed by Group Relative Policy Optimization (GRPO) lifts Qwen3-8B to 65.2% in-distribution and 71.6% on held-out families, exceeding zero-shot Qwen3-235B by over 20 percentage points on both structural-generalization splits. Self-consistency sampling shows that the SFT policy can already produce correct answers but cannot reliably surface them as the modal response; GRPO reshapes the distribution so that correct answers become modal rather than merely reachable, and this sharper commitment is visible mechanistically: logit lens analysis reveals a ${\sim}$20pp advantage in answer crystallization at the critical decision layer. We formalize this observation as a distractor-permutation consistency metric under which GRPO narrows the gap between lenient scoring (at least one permutation correct) and strict scoring (all permutations correct) from 24.0 to 14.3 percentage points.

---


### 274. [Beyond Flat Labels: Level-Restricted Contrastive Learning for Hierarchical Fine-Grained Vision Classification](https://arxiv.org/abs/2606.21838)

**<font color=#1a73e8>作者：</font>** Zhiyuan Tao, Srikumar Sastry, Matthew J Thompson 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal contrastive learning has enabled zero-shot visual classification by aligning images with textual categories. However, in hierarchically structured label spaces, existing methods often produce predictions that are inconsistent across taxonomic levels. For example, a model may predict a fine-grained category whose parent category contradicts its simultaneously predicted higher-level label. By analysis, the issue originates from false negative labels when contrastive comparison involves multiple taxonomic levels. To this end, we propose to restrict contrastive comparisons to categories within the same taxonomic level. In addition, we adopt a group-balanced design, ensuring each taxonomic level receives adequate optimization. As a result, the proposed framework improves both hierarchical consistency and classification accuracy from coarse to fine granularity. We train our model with TreeOfLife-10M based on BioCLIP and evaluate it across multiple hierarchical classification benchmarks, where the model demonstrates significantly improved hierarchical consistency in both Euclidean and hyperbolic spaces. Notably, on iNaturalist 2021 (iNat21), our method improves average accuracy across levels by 30.47% over the baseline, highlighting its effectiveness for hierarchical zero-shot classification.

---


### 275. [Measuring What Persists: Conditioning Mechanisms and a Geometric Framework for AI Agent Identity](https://arxiv.org/abs/2606.21843)

**<font color=#1a73e8>作者：</font>** Andrew Tanner  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents in long-context applications drift from their specified identity. Current methods detect this only after qualitative degradation is visible. We present a geometric framework for measuring identity structure using $\sqrt{\mathrm{JSD}}$ metric spaces and magnitude homology from enriched category theory, where identity is non-geodesic structure and drift is its relaxation toward the geodesic.
Validated on a persistent AI agent, the framework's strongest empirical finding is a two-mechanism conditioning structure: cross-condition distances reveal an identity-vacuum cluster where the identity specification fills a behavioral void, and a safety-basin cluster where it displaces from post-training attractors. An equilateral probe baseline confirms that the identity specification creates measurable behavioral richness (55 unique response patterns vs. 1 for the base model) at maximum probe separation. A first-order perturbation theory for equilateral configurations predicts magnitude changes from perimeter changes alone, with shape perturbations first-order cancelled by the $S_n$ symmetry; the formula is self-consistent at the observed perturbation amplitudes.
A drift experiment measuring magnitude decrease under context pressure was subsequently found to reflect repetitive-padding artifacts rather than genuine context-length drift; diverse padding produces no measurable deformation through 150K tokens. The magnitude homology framework's full diagnostic promise -- detecting anisotropic contraction and structural collapse via homological simplification -- is architecturally grounded in the perturbation theory and selection rules but remains empirically unconfirmed.

---


### 276. [Mind the Intention: Task-Aware Backdoor Attacks for Forecast-Driven Distribution Network Operations](https://arxiv.org/abs/2606.21846)

**<font color=#1a73e8>作者：</font>** Yuxuan Chen, Haipeng Xie, Yichi Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Accurate distributed energy resources (DERs) forecasting is critical for downstream optimal operations. However, such forecast-based operation can be highly vulnerable to cyberattacks. While existing research mainly focuses on adversarial attacks, we pivot to a more controllable and persistent threat: backdoor attacks. In time series forecasting, a backdoored model generates an attacker-specified target pattern whenever a trigger is embedded in historical inputs. This paradigm naturally fits the entire DER forecast-optimization-operation chain. In this paper, we investigate whether and how backdoor attacks can compromise distribution network operations and propose GridTroj, a unified backdoor framework tailored for this scenario. Unlike standard time series backdoor approaches that train a poisoned model to match a predefined target only in terms of forecasting error, GridTroj explicitly incorporates the attacker's intention and optimizes the attack toward operational disruption. Specifically, GridTroj coordinates two key modules. The Intention Planner designs operation-damaging targets and poisoning strategies, while the Backdoor Realizer constructs the corresponding network architecture and training strategy to learn the trigger-target association. Experiments on three downstream optimization tasks demonstrate that GridTroj can effectively compromise grid operations and outperforms existing baselines. Our code is available at this https URL.

---


### 277. [Keyless Attention: Value-Space Routing and Value-Only Caching for Efficient Transformers](https://arxiv.org/abs/2606.21848)

**<font color=#1a73e8>作者：</font>** Xin Gao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose Keyless Attention, an attention mechanism that eliminates the key projection entirely, operating over queries and values only. This yields a Value-Only Cache that reduces KV cache memory and access overhead by exactly 50% over standard attention, while matching or exceeding standard attention's decode throughput. Beyond efficiency, we introduce Depth-$m$ Attention Factorization: standard attention computes a depth-2 factorization of the attention bilinear form, while Keyless Attention realizes a depth-$m$ instance of this family. At m=3, Keyless Attention matches the projection matrix count of standard attention via a value-space routing matrix that replaces the key projection and introduces a coupling between routing and retrieval. Experiments across five models and four architectures (GPT-2 280M, GPT-2 557M, Pythia 410M, Qwen2 1.5B, and Llama 3.2 1B) show that Keyless Attention matches or outperforms standard QKV attention on perplexity in 4 out of 5 models. On downstream zero-shot evaluation (GPT-2 557M), Keyless Attention outperforms on 4 out of 5 commonsense reasoning benchmarks, while achieving 50% KV cache reduction throughout.

---


### 278. [Prompt-Calibrated SAM 3 for Open-Vocabulary Remote Sensing Semantic Segmentation](https://arxiv.org/abs/2606.21863)

**<font color=#1a73e8>作者：</font>** Yanghui Song, Nanqing Liu, Haonan Yin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary semantic segmentation (OVSS) in remote sensing images aims to segment categories beyond a fixed label space. Recent SAM 3-based methods provide a promising training-free foundation, yet three key issues remain: (1) a single class-name prompt lacks sufficient semantic coverage for complex remote sensing categories; (2) expanding each category into multiple prompts introduces redundant online text encoding; and (3) directly aggregating multiple prompt responses propagates noisy activations into the final prediction. To address these issues, we propose ProC-SAM3, which calibrates SAM 3's prompt interface for remote sensing OVSS from three complementary aspects. First, we construct an offline prompt pool where a Category Matcher groups MLLM-generated candidates into per-category sets, and Expansion Constraints further refine each set using category-specific prior knowledge. Second, the resulting text embeddings are cached and reused across all test images, eliminating repeated text encoding. Third, we introduce Presence-Guided Residual Fusion to gate unreliable decoder outputs by prompt presence and confidence, followed by peak-preserving class aggregation that retains fine-grained activations for small and sparse objects. Experiments on eight benchmarks show that ProC-SAM3 achieves an average mIoU of 56.1%, outperforming the previous best training-free method by 3.9 percentage points. Code will be available at this https URL.

---


### 279. [ForEx: A Formal Verification Framework for Explainable Reasoning in Logical Fallacy Detection and Annotation](https://arxiv.org/abs/2606.21867)

**<font color=#1a73e8>作者：</font>** Pei-Cing Huang, Chienyu Liu, Chan Hsu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current evaluations of Large Language Models (LLMs) on logical fallacy detection focus on predicted labels, but do not establish whether those labels are supported by the reasoning the models provide. We propose ForEx (Formal Verification for Explainable Reasoning), a framework that translates LLM-generated explanations into Lean4 and verifies whether the translated rationale is derivable under encoded premises, not the logical validity of the original natural language argument. To distinguish prediction outcomes from the formal status of the supporting reasoning, we introduce the LLM Argument Verification Matrix, which separates label consistency from formal verification status. Experiments on LOGIC-Climate show that over 90% of LLM outputs can be translated into formal reasoning chains that pass verification, while agreement with human annotations remains around 20%. These results expose a systematic gap between formal derivability and label agreement, a distinction invisible to prediction-based metrics. ForEx moves LLM evaluation beyond label correctness toward machine-checkable analysis of formalized reasoning chains.

---


### 280. [WiSP: A Working-Set View of Mixture-of-Experts Serving on Extremely Low-Resource Hardware](https://arxiv.org/abs/2606.21868)

**<font color=#1a73e8>作者：</font>** Jiamu Zhang, Liang Wu, Mayank Darbari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern Mixture-of-Experts (MoE) models place most of their parameters in expert layers, yet only a small fraction of those experts are used for any token. The unused weights must still be stored where the GPU can reach them. On commodity GPUs the common fix is layer-level CPU offloading, which keeps memory low but streams all of a layer's experts across PCIe on every forward pass, losing much of MoE's sparsity benefit. We cast low-resource MoE serving as a working-set management problem on the GPU: routed expert weights and the key-value (KV) cache are two streams of memory demand competing for limited VRAM. We realize this in WiSP (Working-Set Paging), a routing-aware expert pager that plugs into an unmodified serving engine with byte-identical outputs. Keeping resident only the experts a workload reuses, WiSP reaches up to 1.95x the decode throughput of static offload at the same memory budget when the model does not fit. We also find that prefetching experts from predicted routing helps little in single-stream decode: the bottleneck is PCIe bandwidth, not prediction accuracy. This shifts the question from prefetching to allocation: how should VRAM be split between experts and the KV cache? We answer with MV-WSA (Marginal-Value Working-Set Allocation), which equalizes marginal latency benefit per byte subject to a KV admission floor. MV-WSA runs either as an offline configurator or as an online controller that resizes both pools while serving. In real serving the offline configurator is the only policy we test that does well on both prefill and decode; in trace-driven simulation it stays within a few percent of a per-workflow oracle while fixed splits are about 20% worse. The online controller adds a further 1.20x without changing model outputs.

---


### 281. [Protein contacts are already in the attention: a single-forward-pass alternative to the Categorical Jacobian](https://arxiv.org/abs/2606.21876)

**<font color=#1a73e8>作者：</font>** Rome Thorstenson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Categorical Jacobian (CJ) of Zhang et al. (2024) reads protein contacts from a language model by perturbing every residue with every alternative amino acid, about 19L forward passes. We show the signal it reconstructs is already concentrated in a small subset of attention heads: averaging the top-K contact-relevant heads, selected on as few as 10 labeled proteins, recovers contacts in one forward pass and beats CJ on leakage-clean data for every bidirectional model where CJ is defined, and matches or beats it in-distribution (the exceptions being the smallest 8M model and a statistical tie on ESM Cambrian). Ablations localize the gain to labeled head selection, not averaging: at a matched label budget the unweighted mean ties a supervised L1 logistic regression on the same heads, so the parameter-free mean is selection's minimal form, not the source of the advantage. Our primary test is leakage-clean: on a CAMEO split where neither selection nor evaluation touches data the models have plausibly memorized, the head readout beats CJ on ESM-2-650M by +9 pp (N=29, p<0.001), with the within-model margin reproducing across architectures on a wider pretraining-aware set. Both methods fall 30-36 percentage points from their in-distribution Zhang numbers to the leakage-clean numbers, consistent with substantial pretraining overlap inflating prior numbers (a CAMEO-vs-Zhang difficulty shift contributes too, so we read it as an upper bound on the leakage component). We additionally introduce representation-CJ, a hidden-state generalization of the Jacobian for architectures without a masked-LM head; show that the optimal K tracks how diffusely a model spreads its contact heads; and find that both methods lose the contact signal on both causal LMs we test (ProGen2), suggesting attention-encoded pair structure may depend on bidirectional pretraining.

---


### 282. [A Verifiable Search Is Not a Learnable Chain-of-Thought](https://arxiv.org/abs/2606.21884)

**<font color=#1a73e8>作者：</font>** Harsh Patel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> It is tempting to assume any task solvable by a short program can be taught to a model as its chain-of-thought: write the steps out, fine-tune, and the model follows. This paper shows the assumption fails for an identifiable class of procedures. The testbed is nine reasoning tasks, each from a deterministic generator; public and hidden splits share generators, so held-out data proxies test accuracy. I reverse-engineer the generators into Python solvers, render them as chain-of-thought, and distill into a rank-<= 32 LoRA over a 30B (3.5B-active) Nemotron model. Forward-computable tasks install readily: lookup/arithmetic and an 8-bit boolean task transfer (>= 0.99 and 0.68). Cryptarithm does not: distilling its backtracking search holds at 0.01-0.07 across eleven chain-of-thought designs, RL from verifiable rewards, and self-training, even though a search solver answers 71% of instances. This is not a capability gap. The model does the arithmetic on 97-100% of lines and ranks the correct cipher in its top eight on 71%; it cannot carry the search forward as a left-to-right derivation. Fine-tuning learns the shape of a verifiable elimination step while its verdicts become unconditional templates, correct only 16-57% of the time ("verdict-as-token"). The ceiling holds across backbones from 3B to 671B and across fine-tuning and prompting; a controlled intervention isolates the cause: revealing the cipher key, which turns the derivation forward, lifts the same instances from 0.03 to 0.57. When a procedure's only solution is search over information-free structure, no faithful forward chain-of-thought exists to imitate. The task becomes learnable only by removing the search, precomputing its combinatorial core into a catalog and reducing the trace to recall plus verification; the 1st-place solution reaches Private LB 0.92 this way. What distills is memorization and verification, not search.

---


### 283. [AI-Mediated Negotiation: Design Reflections and Lessons](https://arxiv.org/abs/2606.21886)

**<font color=#1a73e8>作者：</font>** Veda Duddu, Jash Rajesh Parekh, Andy Mao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Conversational AI promises a new kind of preparation for high-stakes workplace negotiations -- personalized, interactive, and capable of simulating realistic resistance. That promise is intuitive. We built Trucey, a theory-driven coaching system, to test it. The system encoded four assumptions: that articulation supports clarification, that personalization builds strategic competence, that chunked delivery reduces cognitive load, and that structured scaffolding removes metacognitive burden. A pre-registered experiment (N=267) and interviews (N=15) complicated each of them. Notably, the static handbook we included as a passive control outperformed both AI conditions on empowerment and usability. We reflect on why: each assumption encoded a specific model of how preparation unfolds, and the findings revealed that conversational AI imposes a linear execution model on a task that is fundamentally recursive. We identify an unexamined scope condition on established HAI design guidelines and close with a sequencing principle -- map before path, path before simulation -- for future AI coaching design.

---


### 284. [Ranking-and-Selection with Multiple Correct Answers and Non-Answerable Estimates](https://arxiv.org/abs/2606.21889)

**<font color=#1a73e8>作者：</font>** Qiaoqiao Wang, Wei You  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study fixed-precision ranking-and-selection in structured settings where the answer may be non-unique and where noisy estimates may temporarily admit no valid answer at all. This phenomenon arises naturally in problems such as multi-fidelity ranking-and-selection and identifying a Condorcet winner from pairwise comparisons. To address this, we propose a unified framework based on answer-wise acceptance sets, restricted generalized likelihood ratio stopping, and an answer-pitfall decomposition that yields a max-max-min characteristic value and a common sampling principle. We introduce ENDS, a general procedure that combines estimation, nomination, pitfall detection, and cost-aware information-directed selection. We instantiate ENDS for various problems by deriving explicit formulas. Extensive numerical experiments show that this unified recipe performs well across a broad range of pure-exploration problems and offers a practical framework and proof-of-concept algorithmic recipe.

---


### 285. [AgroSense 2.0: Cross-Modal Transformer Fusion with Geospatial Raster Integration and Interpretable Multi-Task Learning for Precision Crop Recommendation](https://arxiv.org/abs/2606.21892)

**<font color=#1a73e8>作者：</font>** Vishal Pandey, Rishav Tewari, Ruzina Haque Laskar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Crop recommendation systems in precision agriculture have long suffered from a fundamental modality gap: visual soil characterization and chemical nutrient profiling are typically treated as independent inference problems, with fusion often reduced to late-stage feature concatenation. AgroSense~2.0 addresses this limitation through three architectural advances. First, we introduce continental-scale geospatial integration via a seven-band soil raster (\texttt{india\_soil\this http URL}) spanning India, encoding Nitrogen, pH, SOC, Clay, Sand, Silt, and Bulk Density as $32\times32$ spatial patches, a modality entirely absent from prior work. Second, we replace naive feature concatenation with a cross-modal Transformer fusion module, where tabular nutrient features attend over image representations via multi-head attention, enabling richer inter-modal dependency modeling than shallow fusion. Third, we adopt a multi-task objective jointly optimizing soil classification and crop recommendation through a shared backbone, improving generalization via complementary cross-task signal. To enhance interpretability, we apply TreeSHAP to the tabular branch, revealing crop-conditioned nutrient sensitivity: humidity and rainfall emerge as the most influential features globally, while crop-specific profiles diverge meaningfully rainfall dominates rice, nitrogen and potassium dominate maize, and humidity and nitrogen dominate coffee. These explanations provide transparency into model decisions and surface both agronomically consistent patterns and dataset-specific divergences worth further study. Together, these contributions establish AgroSense~2.0 as a more principled, interpretable, and geospatially grounded framework for precision agriculture.

---


### 286. [Olfactory-Inspired Sparse Combinatorial Coding for Low-Resource Named Entity Recognition](https://arxiv.org/abs/2606.21895)

**<font color=#1a73e8>作者：</font>** Bhushan Deshpande  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Named Entity Recognition (NER) in low-resource languages suffers from limited supervision and a lack of high-quality pretrained embeddings. Biological olfaction, which relies on sparse combinatorial coding through receptor and glomerular organization, offers a compelling paradigm for learning robust representations under uncertainty. In this paper, we introduce a receptor-glomerular bottleneck - a novel, biologically-inspired olfactory architecture - between standard token embeddings and a BiLSTM-CRF sequence model. We evaluate our architecture across six multilingual datasets trained entirely from scratch (without pre-trained embeddings) under varied data-scale conditions, including a strict 1k-sentence low-resource control. Our results demonstrate that introducing a representation bottleneck yields F1 score improvements under severe data scarcity, primarily by acting as a powerful regularizer. Under the 1k capped training condition, at least one olfactory-inspired configuration achieves the highest mean F1 score across all six datasets. While these improvements represent near-ties with generic bottleneck controls for most languages, the olfactory architecture provides a significant advantage in languages like Bangla (+6.23% F1 over standard baseline and +8.47% F1 over the best control baseline) where generic bottlenecks degrade performance. We also observe improvements in the ultra-low-resource Telugu setting (+4.43% F1) at full-scale, and find that sparse specialization naturally emerges within the receptor layer. Our findings suggest that structured sparse coding inspired by olfactory networks serves as an effective inductive bias and regularizer when representations must be learned from limited or noisy supervision.

---


### 287. [Continuous Behavioral Authentication via Multi-Expert BERT Log Analysis for Secure Data Sharing](https://arxiv.org/abs/2606.21900)

**<font color=#1a73e8>作者：</font>** Stergios Lantzos, Ilias Syrigos, Apostolos Apostolaras 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Continuous authentication for mobile and zero-trust systems requires nonintrusive evidence confirming the enrolled user-device context remains valid after initial login. This paper presents a BERT log analysis framework for continuous behavioral authentication using Android system logs. The proposed pipeline parses logcat streams into event templates and dynamic variables, pre-trains a domain-adapted BERT encoder on Android log syntax, and fine-tunes three expert models for network/device identity, battery-transition timing, and Wi-Fi topology. The expert confidence scores are fused through a log-space transformation and a 5-nearest-neighbor distance classifier to generate a normality score that is provided to a Policy Decision Point (PDP) for risk-aware access control. Experiments on normal traces, controlled anomaly injections, and benign Wi-Fi perturbations indicate that multi-expert BERT log analysis can detect semantic, battery-timing, and topology deviations in the evaluated setting while maintaining sub-1% False Positive Rate (FPR). The results suggest that Android system logs are a practical sensor-free signal for continuous authentication and user-device context assurance.

---


### 288. [Which Review Aspect Has a Greater Impact on the Duration of Open Peer Review in Multiple Rounds? -- Evidence from Nature Communications](https://arxiv.org/abs/2606.21904)

**<font color=#1a73e8>作者：</font>** Haomin Zhou, Ruxue Han, Jiangtao Zhong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Purpose: Peer review is essential to scientific publishing, but increasing submission volumes have placed growing pressure on reviewers and editors. This study examines the relationship between sentiment toward specific review aspects and peer review duration. It also investigates how this relationship varies across disciplines and review rounds, with the aim of supporting targeted manuscript revision and improving review efficiency.
Design/methodology/approach: We adopt a two-stage approach. First, fine-grained aspects are extracted from peer review reports, and a sentiment classification model is used to determine the sentiment associated with each aspect. Second, correlations between aspect-level sentiment and peer review duration are analyzed. Sentiment scores are also calculated for different review rounds to determine whether these relationships change over successive rounds.
Findings: Review sentiment has a weak but statistically significant negative correlation with peer review duration, indicating that more positive reviews tend to be associated with shorter review periods. Aspects concerning Evaluation and Results and Impact and Research Value show relatively stronger correlations with review duration. The relationships between aspect-level sentiment and review duration also differ significantly across review rounds.
Originality/value: This study connects the textual content of peer review reports with the temporal characteristics of the review process. By identifying review aspects that are more closely associated with review duration, it provides evidence that may help authors prioritize revisions and assist reviewers and editors in improving review efficiency. The findings contribute to reducing the burden of peer review and accelerating scholarly communication and knowledge dissemination.

---


### 289. [Fidelity- and Perception-Aware Local Implicit Attention for Arbitrary-Scale Image Super-Resolution](https://arxiv.org/abs/2606.21910)

**<font color=#1a73e8>作者：</font>** Yu-Syuan Xu, Hao-Lun Sun, Hao-Wei Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Arbitrary-scale image super-resolution (ASISR) aims to reconstruct high-resolution images from low-resolution inputs over a continuous range of upscaling factors. While traditional pixel-regression approaches often produce overly smooth results that lack realistic details, recent diffusion methods can produce sharper and more realistic textures. However, these diffusion techniques frequently introduce the risk of structural hallucinations. To address these issues, we propose Fidelity- and Perception-Aware Local Implicit Attention (FPLIA), a framework that effectively integrates fidelity-oriented features into a diffusion pipeline to produce realistic and faithful reconstructions for ASISR. We introduce a Fidelity and Perception Attention Module (FPAM), which applies both self-attention and cross-attention to fidelity-oriented and perceptual features to enhance representational capacity. To further exploit their complements, we design a Fidelity and Perception Select Module (FPSM) that adaptively selects the most representative features for RGB values prediction. We conduct extensive experiments to validate the effectiveness of these components. Both qualitative and quantitative results show that FPLIA delivers superior perceptual realism while maintaining reconstruction accuracy on standard ASISR benchmarks. The source code is accessible at the following repository: this https URL.

---


### 290. [Data Pruning: Redundant, Problematic, and Interdependent Samples](https://arxiv.org/abs/2606.21916)

**<font color=#1a73e8>作者：</font>** Leon Freese, Marthinus W. Theunissen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The performance of deep learning models is affected by not only data quantity but also data quality. Data pruning is a process by which practitioners can reduce the size of a dataset by only keeping the most important training data points, thereby achieving similar test set performance. We empirically investigate two popular data pruning methods under noisy and noiseless conditions and show that these methods fail in the presence of significant label noise. We highlight that the success of data pruning is distinctly affected by three factors: redundancy in the dataset, the presence of problematic samples, and interdependence between samples. We perform a detailed investigation on commonly used benchmark classification datasets and neural network architectures. We find that our observations are consistent across data distributions and training protocols.

---


### 291. [Selective Ensemble Based on Preference-Directed Multi-Objective Bandits](https://arxiv.org/abs/2606.21929)

**<font color=#1a73e8>作者：</font>** Lanjihong Ma, Zhen-Yu Zhang, Masashi Sugiyama 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Selective ensemble for modern machine learning systems requires choosing promising model candidates under limited evaluation budgets, while downstream tasks often specify only partial preferences over capabilities such as accuracy, robustness, and reasoning. This setting naturally gives rise to a sequential decision problem under partially specified linear preferences. We formalize it as preference-directed multi-objective bandits (PDMOB), where admissible trade-offs are represented by a polyhedral preference cone. Based on this formulation, we introduce Pareto $C$-optimality, which recovers standard Pareto optimality and single-weight scalarization as special cases. We then propose the preference-directed upper confidence bound (PrefUCB) algorithm, which maintains directional confidence intervals to guide exploration. We analyze both indicator-based and gap-weighted regret, and establish instance-dependent logarithmic bounds for both criteria, recovering the optimal logarithmic dependence on the horizon $T$ in classical special cases. Experiments on large pre-trained model selective ensemble tasks and online asset allocation under institutional mandates validate the efficacy of our method.

---


### 292. [MindTailor: Personalized Emotional Support via Post History-Grounded Case Formulation and Collaborative Refinement](https://arxiv.org/abs/2606.21930)

**<font color=#1a73e8>作者：</font>** Suhyun Han, Kyunghyun Cho, JinYeong Bak  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As mental health concerns continue to rise globally, social media has emerged as a vital space where individuals seek emotional support. While prior work on personalized emotional support has leveraged seekers' emotional states, personas, and situational context, these approaches primarily capture the seeker's current state, overlooking the formative experiences that shape present concerns. In this work, we propose MindTailor, a framework that generates personalized emotional support responses by constructing a case formulation from the seeker's post history and iteratively refining responses through collaborative critique among counselor agents grounded in distinct counseling strategies. To enable research on this history-aware task, we construct ReddiSupp, a dataset of 798 Reddit posts paired with seekers' prior post histories. Through LLM-as-a-Judge evaluation, expert human evaluation, and a user study with seekers, we demonstrate that MindTailor outperforms baselines across these evaluations, improving empathy, personalization, understanding, and achieving the highest overall preference.

---


### 293. [CoSA: Correlation-Guided Change Attention with Learnable Residual Gating for Remote Sensing Change Detection](https://arxiv.org/abs/2606.21932)

**<font color=#1a73e8>作者：</font>** Abdirashid Omar, Jonghyuk Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing change detection (CD) from bi-temporal imagery is critical for applications such as urban monitoring, disaster assessment, and environmental management, yet robust localization remains challenging under sparse changes, noisy labels, and appearance variations. In this paper, we propose Context Sampling Attention (CoSA), a lightweight decoder-side refinement module that explicitly leverages bi-temporal feature correlation as a control signal for adaptive change-aware feature enhancement. This differs from conventional attention mechanisms that rely on implicit feature weighting without explicit temporal control. In the implemented FC-Siam setting, CoSA computes normalized same-location cross-correlation between paired decoder features, converts low correlation into a change gate, and injects the resulting gated residual at native 1/8 and 1/16 feature scales through learnable residual scaling. This design enables effective discrimination between stable and ambiguous regions without relying on computationally expensive global attention. Extensive experiments on four benchmark datasets (LEVIR-CD, S2Looking, DSIFN, and CLCD) demonstrate consistent improvements over strong baselines, achieving 1.5-2.6% gains in changed-class F1 while introducing negligible parameter overhead. Ablation studies confirm that multiscale placement and learnable residual gating are both important for peak performance. These results indicate that CoSA establishes a practical and effective refinement paradigm for enhancing temporal discriminability in Siamese change detection frameworks.

---


### 294. [Artic-O: End-to-End Articulated Object Reconstruction via Latent Geometry Learning](https://arxiv.org/abs/2606.21938)

**<font color=#1a73e8>作者：</font>** Xuyang Wang, Zhenyu Li, Jian Ding 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing articulated objects from sparse images requires recovering complete geometry, movable parts, and motion parameters. Recent methods typically separate geometry reconstruction, part reasoning, and articulation estimation into different stages. This separation can weaken consistency between shape, active parts, and motion, while also incurring substantial inference cost. We introduce Artic-O, an end-to-end, feed-forward framework for articulated object reconstruction via latent geometry learning. Instead of fitting geometry in image or view space, Artic-O maps sparse multi-state observations into a pretrained latent geometry space, where a frozen flow-matching decoder provides a complete-shape prior for recovering visible and occluded structures. To connect geometry with articulation, Artic-O fuses visual tokens, geometry latents, and point-wise decoder features in an image-grounded part-reasoning module for active-part segmentation and articulation prediction. We further train the model with a geometry-to-articulation curriculum and a decoupled two-pass strategy to balance reconstruction and part-level supervision. On PartNet-Mobility, Artic-O achieves strong reconstruction quality while being substantially more efficient than LARM, a strong prior method. It reduces Chamfer Distance, improves F-score, and achieves comparable or better articulation accuracy across most joint metrics, while reducing inference time from 9 minutes to about 0.3 seconds per object.

---


### 295. [DevoTG: Temporal Graph Neural Networks for Modeling C. elegans Developmental Connectomics](https://arxiv.org/abs/2606.21940)

**<font color=#1a73e8>作者：</font>** Jayadratha Gayen, Bradly Alicea  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding how a nervous system wires itself from birth to adulthood is a fundamental challenge in developmental neuroscience. We present DevoTG, a temporal graph framework that applies Temporal Graph Neural Networks (TGNs) to two complementary representations of C. elegans neural development: a Continuous-Time Dynamic Graph (CTDG) of cell division events derived from cell lineage data, and a Discrete-Time Dynamic Graph (DTDG) of the developing synaptic connectome spanning eight reconstructed electron-microscopy datasets. On the lineage prediction task, our TGN achieves a mean test AUC of 0.839 +/- 0.007 (5 seeds; validation AUC 0.937 +/- 0.001), outperforming a static GNN with the identical architecture by 26 AUC points (0.577 +/- 0.080), demonstrating that temporal memory is the decisive factor. Applied to the connectome DTDG, DevoTG identifies three connection stability classes (stable, developmental, and variable) across 225 neurons and 858 to 2,496 connections over development (L1 birth to adult), providing a temporal-graph-theoretic complement to the individual-variability classification of Witvliet et al. Analysis of hub command interneurons AVA, AVB, and AVE reveals their persistent centrality and how their integration roles are progressively reinforced across larval stages. Accompanying interactive visualizations (3D animated networks, centrality heatmaps, and a spatiotemporal lineage graph) make developmental dynamics accessible for biological hypothesis generation. DevoTG is open-source and designed for extension to other developing nervous systems. Code is publicly available at this https URL.

---


### 296. [ScalePredictor: Instance-aware Scale Learning for Accurate Quantization of Vision Transformers](https://arxiv.org/abs/2606.21947)

**<font color=#1a73e8>作者：</font>** Changjun Li, Runqing Jiang, Lian Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers have achieved remarkable success in many fields, yet their deployment on edge devices remains challenging due to their substantial computational demands. Post-Training Quantization (PTQ) offers an attractive solution by compressing models using a small calibration set with minimal training overhead. However, most existing PTQ works adopt a static quantization paradigm that is uniformly applied to all instances. Given the substantial diversity of natural images, the activation distributions vary significantly across samples, making these methods inherently suboptimal. In this paper, we propose ScalePredictor, a dynamic quantization framework for accurate and efficient quantization scale learning of ViTs. We first reveal a hidden correlation between the distribution range of shallow-layer activations and the optimal scales of deeper layers. Based on this, we develop a scale learning mechanism that integrates an efficient range extraction approach to capture robust range statistics at the shallow stage, which are then fed into a Taylor-motivated polynomial scale projection module to generate all quantization scales simultaneously. With the efficiency of polynomial approximation, ScalePredictor introduces insignificant computational overhead while avoiding costly just-in-time calibration. Extensive experiments on ImageNet demonstrate that ScalePredictor consistently outperforms prior PTQ methods, achieving a more favorable accuracy-efficiency trade-off. Code and additional results are shown in the supplementary materials.

---


### 297. [CapRiCorn-1K: A Comprehensive Benchmark for Video Captioning and Subject Referential Consistency Across Temporal Scales](https://arxiv.org/abs/2606.21949)

**<font color=#1a73e8>作者：</font>** Xinlong Chen, Jiafu Tang, Yue Ding 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate and comprehensive video captions with consistent subject references are critical for downstream understanding and generation tasks. However, few existing benchmarks can objectively and comprehensively evaluate these properties across diverse durations and scenarios, thereby hindering the advancement of video captioning models. To bridge this gap, we propose CapRiCorn-1K, a comprehensive benchmark designed to evaluate both video captioning quality and subject referential consistency across long temporal horizons and diverse video domains. To accommodate varied evaluation needs, our benchmark supports both audiovisual and visual-only settings. Extensive experiments on CapRiCorn-1K reveal that current models generally struggle to generate accurate and comprehensive captions while maintaining consistent subject references. Moreover, as video duration increases, both the overall caption quality and subject referential consistency decline. Notably, our evaluation metrics exhibit strong correlations with the performance of downstream understanding and generation tasks conditioned on the generated captions, further validating their effectiveness. The project is available at this https URL .

---


### 298. [On the Curse of Dimensionality in Private Sparse Covariance Estimation and PCA](https://arxiv.org/abs/2606.21951)

**<font color=#1a73e8>作者：</font>** Syamantak Kumar, Shourya Pandey, Purnamrita Sarkar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study high-dimensional differentially private (DP) covariance estimation in the operator norm, and principal component analysis (PCA), under $k$-row-column sparsity ($k$-RCS) of the covariance matrix. In the non-private setting, it is known that $\mathsf{poly}(k, \log d)$ samples suffice to solve both of these problems. However, the only comparable result known under DP (Wang et al. 2021) requires $\Omega(d)$ samples under standard parameterizations of the problem. We investigate when this curse of dimensionality is inherent for sparse covariance estimation tasks under DP.
On the upper bound front, we show that a $\mathsf{poly}(k, \log d)$ sample complexity for PCA is possible under DP, if we also posit sparsity of the leading eigenvector. We complement this result with $\mathsf{poly}(d)$ lower bounds under DP for both sparse covariance estimation and PCA, establishing an exponential gap between the private and non-private variants of these problems when $k = \mathsf{polylog}(d)$. To our knowledge, no such separation has previously been demonstrated for any sparse estimation problems in private high-dimensional statistics. Our techniques are flexible enough that they imply stronger lower bounds even for the well-studied problem of standard DP PCA, without sparsity assumptions.

---


### 299. [Are Multilingual Models Actually Improving? Isolating True Cross-Lingual Transfer](https://arxiv.org/abs/2606.21954)

**<font color=#1a73e8>作者：</font>** Prasoon Bajpai, Eleftheria Briakou, Colin Cherry 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-lingual transfer is a model's ability to generalize capabilities from well-represented source languages to under-represented target languages. Existing measures of a model's transfer strength conflate improvements in transfer with general improvements to accuracy in the source language. We advocate for an alternate metric that reliably captures transfer strength called Hardness Adjusted Transfer (HAT) Score, and use it to derive multiple insights on factors influencing transfer strength. Our analysis across twenty diverse language models and three popular mainstream multilingual benchmarks argues that 1) transfer in small models is not broken, 2) we are making slower than expected progress in cross-lingual transfer with model size, and 3) we have made clear progress over time.

---


### 300. [Denoising-Enhanced Coarse-to-Fine Infrared Small Target Detection with Attention Prior-Guided Knowledge Distillation](https://arxiv.org/abs/2606.21956)

**<font color=#1a73e8>作者：</font>** Houzhang Fang, Ruixuan Huang, Qiuhuan Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared small target detection (IRSTD) in high-resolution images is crucial for many practical applications, such as surveillance of unmanned aerial vehicles (UAVs) and UAV-based ground monitoring. However, IRSTD remains challenging due to the small size and weak features of targets, as well as significant interference from complex dynamic backgrounds. Existing detection methods often suffer from redundant computations on non-target background regions and insufficient exploitation of target context information, which limits their performance in complex backgrounds. To address these issues, we propose an efficient coarse-to-fine infrared small target detection framework with attention prior-guided knowledge distillation, termed ECFNet. In the coarse stage, we design a region binary classification network (RBCN) on grid-based multi-scale feature maps to efficiently recognize target-containing context region proposals while suppressing complex backgrounds. Moreover, we introduce a novel denoising-assisted training strategy that incorporates noisy ground-truth (GT) masks into the feature maps of RBCN and trains the network to reconstruct the GT masks through a denoising task, thereby enhancing its ability to distinguish target proposals from background regions and accelerating convergence. In the fine stage, we customize a lightweight target detector to the coarse stage's region proposals for balancing accuracy and efficiency. Furthermore, we propose a knowledge distillation strategy guided by the teacher-student cross-attention prior. This mechanism directs the student to focus on critical target regions, thereby enhancing the discriminative feature representation for infrared small targets. Extensive experiments on three real infrared datasets demonstrate that our method outperforms both existing single-stage and two-stage approaches while maintaining high real-time processing efficiency.

---


> [!TIP]
> 当前位于：**251-300**（第 6/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-654](./part-14.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
