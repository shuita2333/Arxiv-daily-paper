# 📦 其他研究 | 2026年10月07日

> 本类共 **571** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**351-400**（第 8/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

---

### 351. [Can Prosodic Style Be Inferred from Text Alone? Evidence from Unsupervised Acoustic Clusters](https://arxiv.org/abs/2610.05575)

**<font color=#1a73e8>作者：</font>** Abdul Rehman, Jian-Jun Zhang, Xiaosong Yang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Much of expressive text-to-speech research rests on an untested assumption that written text carries enough information to select an appropriate prosodic style for its delivery. Text-predicted style models improve listener preference, and expressive-appropriateness evaluation presupposes that context constrains style, yet neither measures the assumption itself. This paper tests it as a falsifiable hypothesis against style labels derived from acoustics alone. For each of six speakers in a 1,200-hour conversational corpus, utterances are clustered in the spaces of five speech models, including a prosody-only control, and the cluster of held-out utterances is predicted from twelve text embedding models. Three controls are applied: utterance length is erased from the speech embeddings; accuracy is scored against the majority-class floor of unbalanced clusters rather than uniform chance; and a bag-of-words baseline measures word identity alone. Text predicts the cluster above that floor for all six speakers (+0.111 top-3 accuracy), but bag-of-words achieves three quarters of this. Sentence embeddings add only +0.026, largest for encoders not trained for sentence semantics and reversed by tree-based probes for all others. Acoustic clusters are not compact in text embedding space in any of 360 configurations. The prosody-only space weakens the association for five speakers, but not for the speaker showing it most strongly. Text thus informs these delivery clusters mainly through word choice, whether as a cue to prosody or as a marker of topic and recording situation, and reference-free style selection cannot assume more.

---


### 352. [SteadySplats: Resampling of Low-Variance Gaussians for High-Fidelity Stochastic Rendering](https://arxiv.org/abs/2610.05576)

**<font color=#1a73e8>作者：</font>** Felix Windisch, Thomas Köhler, Lukas Radl 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stochastic order-independent transparency enables efficient and elegant rendering of primitive-based radiance fields like 3D Gaussian Splatting models, but remains impractical due to the inherent visible noise in the output. We propose a principled approach to minimize high-frequency noise, addressing its sources at the representation and image synthesis level. During stochastic rendering, our history-based spatial resampling scheme drastically accelerates image convergence, while temporal importance resampling ensures coherence under camera movement. During training, a color regularizer implicitly reduces the variance along view rays in the 3DGS models. With these properties, our optimized, Vulkan-based renderer effectively mitigates output noise at low and high sample counts, achieving a substantial 13~dB PSNR increase in quality over previous stochastic methods at 1 sample per pixel and quickly converging to sorted 3DGS with an average L1 error of less than $10^{-4}$.

---


### 353. [Generating the Wild: Individual-Consistent Image-to-Video Generation for Wildlife](https://arxiv.org/abs/2610.05587)

**<font color=#1a73e8>作者：</font>** Yuzhuo Li, Di Zhao, Xinyu Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Individual-level wildlife identification often suffers from data scarcity, as varying observations of the same animal under diverse poses, viewpoints, and motions are rarely available. Image-to-video (I2V) generation offers a promising way to mitigate this limitation by synthesizing additional observations from a single reference image. However, existing I2V models mainly emphasize global layout, semantics, and motion, and therefore often fail to preserve fine-grained local appearance cues that distinguish one wildlife individual from another, such as fur texture, stripe boundaries, spot configurations, and contour transitions. We observe that these identity-critical cues are closely related to high-frequency information. To address this challenge, we propose WildIcon, a high-frequency-guided I2V framework for wildlife individual consistency. Specifically, WildIcon introduces a frequency-aware identity encoding branch that extracts individual-specific high-frequency cues from the reference image. Combined with isolated foreground information, the resulting identity tokens are then injected into cross-attention blocks as identity conditioning. Building on a frozen backbone with lightweight identity adaptation, WildIcon preserves fine-grained identity cues visible in the reference image while retaining the motion controllability and semantic fidelity of the base I2V model. In addition, to support the training and evaluation of wildlife individual-consistent I2V, we construct WildlifeVid, a wildlife-centric video dataset with high-quality, temporally coherent clips and individual-level identity labels. Experiments on I2V generation and downstream animal re-identification (ReID) show that WildIcon achieves stronger individual consistency than existing baselines, and that its filtered outputs can serve as useful candidate training augmentations for downstream ReID.

---


### 354. [What Is a Repeated Token Worth? The Scaling Geometry of Multi-Epoch Pretraining](https://arxiv.org/abs/2610.05591)

**<font color=#1a73e8>作者：</font>** Yekun Chai, Haoyi Xiong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As pretraining increasingly repeats data, every run faces three questions: how many epochs to take, how that number should change with model size, and whether anything besides the epoch count matters. We answer them by pricing a repeated token against two references: one epoch on the same data, which gives its value, and fresh data at equal compute, which gives its cost. Against fresh data, the cost of repetition follows a single variable, the number of extra epochs divided by the unique tokens per parameter. Against the same data, a second epoch is worth nearly as much as a fresh one, and repeated tokens fall to half the value of fresh ones after a critical epoch count that grows with the training budget per parameter but hardly with model size. With unique data fixed, the predicted compute-optimal run grows model size and epochs together until loss stops improving, near the critical epoch count. The same variable accounts for the direction of size trends that appear to conflict: larger models tolerate fewer epochs when the corpus is fixed, from about 15 at 127M to 4 at 2B parameters, but not when unique data grow with the model. Counts alone do not determine loss: at identical counts, replaying shards consecutively raises loss by up to 0.46~bits per byte, concentrating repeats on fewer samples also raises it, lower-entropy sources degrade faster with repetition, and re-tokenizing repeats helps only under heavy repetition. These results offer an empirical guide to pretraining when unique data, rather than compute, are the binding constraint.

---


### 355. [When the Cross-Silo Federation Goes Offline: Continual Learning for Site Onboarding with Limited Unlabeled Data](https://arxiv.org/abs/2610.05598)

**<font color=#1a73e8>作者：</font>** Ahmadreza Eslaminia, Klara Nahrstedt, Chenhui Shao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An organization often holds too little labeled data to train a model that generalizes, and the records that would supply the rest sit with organizations that cannot release them. Cross-silo federated learning offers a way through, since participants exchange model parameters rather than records, but it ordinarily settles two aspects of the arrangement in advance, the participating sites and the classes the model can predict, and deployment can breach both. A new site joins after training, once the established sites have finished their engagement and gone offline, and its records arrive unlabeled, mixing conditions the model already recognizes with conditions no participant has observed. We present an autonomous three-stage procedure that expands the model entirely at the joining site: reconstruction experts screen for novelty, clustering separates the flagged records into candidate conditions, and class means describe the old classes, all inside one shared representation. Those classes were learned from records that never leave their owners, so the usual defenses against forgetting are unavailable, and the procedure supplies the evidence they would have carried from either of two dissimilar sources, prototypes held by the federation or records held by the joining site. On a real industrial condition-monitoring dataset, run end to end with no label consulted, either source holds old-class accuracy at 0.868 or above with forgetting at most 0.063, and the two differ by 0.021, so a configuration can be chosen by the disclosure it permits rather than the accuracy it delivers. Both keep old- and new-class accuracy in balance where every alternative we measure gives up one for the other, and both retain more of the old classes than distillation- and regularization-based baselines. The balance still holds with only 6 labeled records per arriving condition and 3 retained per old class.

---


### 356. [Your Unlearning Gives You Away: Identifying Erased Concepts in Diffusion Models](https://arxiv.org/abs/2610.05601)

**<font color=#1a73e8>作者：</font>** Kaiyuan Deng, Yuchen Li, Yang Xiao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing attacks on unlearned diffusion models assume that the erased concepts are known in advance and focus on recovering them. In practice, however, model providers may not disclose which concepts have been removed, and even with access to the original base model, an adversary may still lack a clear target to attack. In this paper, we aim to answer the following critical but overlooked questions: which concepts have been erased from the model, and how many have been erased in total? To this end, we present Tracer, a framework that rapidly and accurately identifies erased concepts and estimates their number. Tracer efficiently identifies erased concepts without generating and classifying images. By combining lightweight spectral analysis of weight footprints, it enables efficient search over large candidate vocabularies. To distinguish multiple erased concepts, we introduce a footprint coverage objective that guides sequential discovery. Tracer estimates the number of erased concepts by detecting a sharp decline in candidate confidence as the selected concepts account for the erasure footprint, without requiring labeled examples for calibration. The framework requires only lightweight linear algebra and limited forward probes, with no prior knowledge of the unlearning algorithm. Experiments across text-to-image and text-to-video backbones and diverse unlearning methods demonstrate that Tracer identifies erased concepts and estimates their number in seconds, achieving 150 to 137,000 times and 133 to 20,000 times speedups over MIA and brute-force search on image and video models, respectively, with substantially higher identification accuracy.

---


### 357. [Exploring the Effects of Personality in Human-Agent Interactions: A Study on User-Agent Synchrony with Human-based Vocalics](https://arxiv.org/abs/2610.05606)

**<font color=#1a73e8>作者：</font>** ai Alexander Hackney, Jhonathan Sora-Cardenas, Aibek Musaev 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> User trust is paramount in human-agent interactions, as it allows users to feel comfortable being themselves around an agent. The process of building user rapport starts in how an agent was designed, from its modality to the setting, to any of the many features and characteristics that can be tailored. All these aspects can affect whether users will be able to properly interact with the virtual agent and achieve the intended purpose. One such feature that is critical in human-human interactions is personality. A person's personality can strongly influence whether those that interact with them perceive them as trustworthy. This study used virtual agents generated from human voices with known personality traits to evaluate user perceptions. We found that extraverted agents were deemed to be more likeable by users, and that there was no significant effect of user-agent synchrony on user perceptions of the agent. In addition, it was found that user personality, without regard for agent personality, affected user perceptions of the agents. Our observations suggest that user perceptions may depend more on agent-topic synchrony than user-agent synchrony, and contribute to the broader community with considerations for the design of effective human-agent interactions.

---


### 358. [Delay-coordinate reconstruction and conditional-moment causal diagnostics in stochastic systems](https://arxiv.org/abs/2610.05632)

**<font color=#1a73e8>作者：</font>** Jun Ohkubo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Partial observation and delay-coordinate reconstruction are rooted in deterministic dynamical-systems theory, whereas there are many systems with intrinsic stochasticity. We propose a conditional-moment interpretation of delay-coordinate reconstruction for stochastic systems, in which a delay vector is used to reconstruct conditional moments of a future distribution rather than a unique future sample path. Two complementary arguments motivate this viewpoint. First, the probability density of a stochastic differential equation obeys a deterministic Fokker-Planck equation and, under certain assumptions, is represented by an infinite deterministic hierarchy of moments. Hence, a finite-moment closure suggests a Takens-like finite-dimensional approximation. Second, a discussion based on the Koopman operator theory clarifies that the time evolution of an observable in the Mori-Zwanzig formalism yields a conditional expectation in stochastic systems. Then, the orthogonal "noise" term in the coefficient-space Mori-Zwanzig equation vanishes in the stochastic cases; this result is consistent with the moment-based argument. As an application of this stochastic delay-reconstruction viewpoint, we revisit convergent cross mapping (CCM) for diagnosing certain causal relationships. Although CCM based on the embedding theorem cannot generally be applied to stochastic systems, it is possible to examine certain types of causal relationships by using conditional moments. Using coupled logistic systems with additive and multiplicative coupling mechanisms, we discuss how causal relationships are embedded in stochastic systems.

---


### 359. [When Does a Diffusion Model Decide What to Draw ?](https://arxiv.org/abs/2610.05645)

**<font color=#1a73e8>作者：</font>** Snigdha Chandan Khilar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A diffusion model starts from pure noise and removes it step by step. Somewhere along the way it stops being able to become "anything" and becomes committed to, say, a horse rather than a truck. We measure when this happens, and what a trained model gets wrong about it, on CIFAR-10. The most direct measurement is to freeze a half-finished image, restart the generation from that point many times, and count how often each class comes out. We call this probability the committor. Measured this way, the model settles coarse questions (vehicle or animal?) at roughly twice the noise level of fine ones (which animal?). A much cheaper measurement, the noise level at which a classifier's opinion about two classes splits into two distinct groups, gets the order of these decisions right (rank correlation 0.73-0.88) but not their exact timing. We then compare pretrained models with their

---


### 360. [Graph Data Augmentation via Contrastive Generator Inversion ($\texttt{DCBA}$)](https://arxiv.org/abs/2610.05653)

**<font color=#1a73e8>作者：</font>** Mateusz Stolarski, Michał Czuba, Łukasz Kraiński 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graphs provide a natural representation of many complex systems, ranging from social platforms to ecosystems. However, the development of graph-based machine learning methods is often constrained by the limited availability of large and diverse graph datasets. In this paper, we introduce $\texttt{DCBA}$, a model-based approach to graph data augmentation that infers the configuration of a synthetic graph generator from an observed network. We instantiate the proposed framework using the $\texttt{ABCD}$ generator, which produces scale-free networks with community structure. Our model learns a joint representation of graphs and generator parametrisations using a multi-positive contrastive objective with soft negative weighting. The learned representation enables the prediction of an $\texttt{ABCD}$ configuration whose stochastic realisations preserve the macrostructural properties encoded by the generator. Experiments show that $\texttt{DCBA}$ recovers generator parameters more accurately and robustly than an algorithmic inverse-modelling baseline. Its downstream utility is further demonstrated in community detection, where inferred configurations used to fine-tune $\texttt{PRoCD}$ improve AMI on average by $161\%$ on synthetic and $273\%$ on real-world networks.

---


### 361. [Bellman-Centric Learning: Near-Optimal Regret for Linear Bandits with Memory](https://arxiv.org/abs/2610.05659)

**<font color=#1a73e8>作者：</font>** Jingyuan Liu, Huiwen Jia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study linear bandits with memory, where past actions induce endogenous nonstationarity through an arbitrary known, bounded matrix-valued memory map. To trade off exploration and exploitation while accounting for the memory dynamics, we develop RSM-LinUCB, a Bellman-centric algorithm that learns as in linear bandits and plans as in reinforcement learning. This design admits a novel regret decomposition which separates the memory-induced error from the cumulative reward estimation error along the learner's trajectory. We prove a high-probability regret bound of $\widetilde O\big(dRS(M+1)+\sigma d\sqrt T\big)$, where $T$ is the learning horizon, $d$ is the parameter dimension, $M$ is the memory length, $R$ and $S$ bound the memory-map operator norm and reward-parameter norm, respectively, and $\sigma$ is the sub-Gaussian noise scale. Our results reveal that the multiplicative memory-horizon coupling in prior bounds is not intrinsic: memory only contributes an additive cost, up to logarithmic factors. We also prove a matching minimax lower bound, establishing near-optimality. We further extend the algorithm to generalized linear rewards, preserving this separation with near-optimal memory and leading statistical dependence. Our algorithms outperform the baselines in numerical experiments on synthetic instances and semi-synthetic KV- and semantic-cache tasks.

---


### 362. [Scalar Communication via Random Direction Refreshing for Distributed Optimization](https://arxiv.org/abs/2610.05666)

**<font color=#1a73e8>作者：</font>** Mohammadreza Rostami, Solmaz S. Kia  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Distributed optimization over networks requires agents to repeatedly exchange decision variables with their neighbors. When the decision dimension $d$ is large, these exchanges dominate the communication cost, which is critical for bandwidth-constrained agents. Existing remedies quantize or sparsify the exchanged vectors, yet each message still scales with $d$ and the compression error must be compensated by additional states. To address this limitation, we propose a scalar-communication mechanism in which every neighbor message carries a single real number regardless of $d$. Agents regenerate a common random direction from a shared seed, transmit only the inner product of their state with that direction, and act on the resulting rank-one surrogate of their neighbors' states while retaining full local gradients. We develop and analyze the mechanism for an existing continuous-time distributed optimization algorithm. For strongly convex local costs with Lipschitz gradients, we show that the optimizer remains the unique consensus equilibrium, that a fixed direction admits spurious equilibria, and that refreshing the direction at a sufficiently high rate yields exponential mean-square and almost-sure convergence with constant gains and no residual error. The framework admits any isotropic fixed-norm direction distribution, including Rademacher, scaled-coordinate, and sphere-normalized Gaussian directions; all three attain lower fresh-encoding variance than unnormalized Gaussian directions. The effects of the direction distribution and the refresh interval are illustrated in~simulations.

---


### 363. [Sharp Integrality Gaps in Calibration Distance](https://arxiv.org/abs/2610.05679)

**<font color=#1a73e8>作者：</font>** Zinan Wang, Xinhao Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the offline gap between deterministic calibration distance C and its fractional relaxation L for binary unit-weight sequences under total absolute-change cost. We sharpen the offline comparison C <= L + O(sqrt(T)) (Qiao and Zheng, 2024, Theorem 2) to the sharp worst-case order Theta(T^(1/3)). If Delta_T is the supremum of C - L over length-T inputs, then T^(1/3)/1000 <= Delta_T <= 41T^(1/3) for T >= 216. The upper bound holds for every input, while each T >= 216 has a rational lower-bound input. For every input with m distinct forecasts, C <= L + m, and the unrestricted-sample worst-case sparse order is Theta(m). For rational forecasts and accuracy, with binary-encoded multiplicities of separately assignable unit identities, a grid-free polynomial-bit-time procedure returns B <= L <= U, U - B < eta, and an exactly calibrated compact repair of cost at most U + m <= L + m + eta.

---


### 364. [Automatic Speech Recognition for Low-Resource Sinhala: A Critical Review of Methods, Challenges, and Future Directions](https://arxiv.org/abs/2610.05681)

**<font color=#1a73e8>作者：</font>** Chanuka Dinuwan, Sanath Jayasena, Buddhika Karunarathne  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic speech recognition (ASR) for low-resource languages remains a major challenge. Sinhala, the primary language of Sri Lanka with about 16 million speakers, illustrates the difficulty: agglutinative morphology, a 54-phoneme inventory, subject-object-verb (SOV) syntax and scarce annotated speech data limit both conventional and modern ASR systems. This paper presents the first critical review of Sinhala ASR research, tracing its development from Hidden Markov Models (HMMs) through deep neural networks to self-supervised pre-trained models such as wav2vec 2.0, XLS-R, Whisper and Massively Multilingual Speech (MMS). We compare existing Sinhala systems with related low-resource ASR work on Tamil, Malayalam and Hindi in terms of architecture, training data, word error rate (WER) and robustness to real-world acoustic conditions, and we assess self-supervised and transfer learning as responses to scarce labeled data. We show that most reported WERs are not directly comparable because they differ in corpus, data split and scoring, and that the only controlled comparison in the literature attributes an 18.1% relative WER reduction to corpus correction alone. We also discuss context-aware ASR that draws on phonological, syntactic and semantic knowledge. We identify six research gaps: (1) the lack of large annotated corpora covering multiple dialects and acoustic conditions; (2) weak contextual modeling of Sinhala morphosyntax; (3) high WER in real-world conditions; (4) the absence of standardized benchmarks; (5) the lack of parameter-efficient fine-tuning studies; and (6) the absence of annotated code-switched Sinhala-English speech resources. We outline a research agenda to address these gaps, intended as a roadmap for researchers working on Sinhala and other morphologically rich languages.

---


### 365. [Do Time-Series QA Systems Read the Time Series? Evidence Use and Reasoning Reliability](https://arxiv.org/abs/2610.05686)

**<font color=#1a73e8>作者：</font>** Zhuomin Chen, Jingchao Ni, Xu Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In recent years, time-series question answering (QA) systems have made significant progress. However, generating a correct answer does not show whether retaining the supplied numerical series improves task performance, nor whether the prediction is sensitive to changes in that input. While some systems provide rationales, answer accuracy also does not show whether their numerical claims are grounded in the supplied series or whether the stated inference is valid. In this work, we focus on evaluating four time-series QA systems: TimeOmni-1, ChatTS, TimeOmni-VL, and Time-MQA. First, for three systems with released evaluation data, we reproduce their reported results and compare the performance of the systems with their backbones. Then, we introduce a benchmark named COMMON-TSQA, which collects public evaluation datasets from existing time-series benchmarks and unifies their sample representation, task definitions, and answer schemas, while evaluating each system through its own interface under common evaluation criteria. The evaluation uses the original condition and six interventions while keeping the question and target fixed. Our analysis shows that aggregate performance alone can obscure how systems use numerical evidence. Similar task-level scores can arise despite substantial changes in individual predictions. Some interventions induce simple fallback behavior rather than preserved task ability. We also evaluate rationales for factual grounding, inference validity, and consistency with the final answer. We find that rationales often contain time-series claims unsupported by the input. Moreover, the rationale audit shows that agreement between a rationale and its final answer can coexist with incorrect numerical descriptions or invalid intermediate inferences.

---


### 366. [Square-Root Regret for Adversarial Multiplayer Bandits without Collision Information or Shared Randomness](https://arxiv.org/abs/2610.05688)

**<font color=#1a73e8>作者：</font>** Chenyu Gan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study adversarial multiplayer bandits with $K$ arms and $2\le m<K$ labeled players, without collision information, shared randomness, or an external communication channel. We design a constructive communication and synchronization protocol with a Monte Carlo public constructor. With probability at least $1-CN^{-32}$ over preprocessing, where $N=2Km(T+1)$, its fixed published output satisfies \[
R_T\le C K^{5/2}\sqrt T\log^2(2Km(T+1)) \] simultaneously for every oblivious reward sequence chosen after preprocessing. Here $R_T$ is expected regret over the players' private execution randomness. Positive reward observations establish a common learning schedule and synchronize players before learning begins. The cost of delayed communication is charged to the support of positive rewards, ensuring that periods with little useful feedback incur only limited regret. A slow--fast learning procedure then maintains valid reward estimates while assignments and scores are exchanged.

---


### 367. [Toward AI Trustworthiness: Finding Analytically Proven Forward-Invariant Sets for AI-Controlled Systems](https://arxiv.org/abs/2610.05689)

**<font color=#1a73e8>作者：</font>** Haoyang Song, Xikun Yang, Qixin Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neural-network (NN) controllers are increasingly used in nonlinear control systems, but their highly nonlinear behavior makes them difficult to explain and verify, raising trustworthiness concerns in safety- and mission-critical applications. A key step toward certifiable trustworthiness is to find a Forward-Invariant Set (FIS): a state-space region such that any trajectory starting inside remains inside. If the FIS excludes unsafe states, safety can be guaranteed for initial states within it. Finding an analytically proven FIS for a given AI-controlled system with a fixed controller is difficult. We propose a framework that uses an Invertible Neural Network (INN) to transform the original state space into a latent space where a regular-shaped FIS is more likely to exist. We train the INN so that a preferred hyper-rectangular candidate becomes invariant in the latent space, then formally verify it. We prove that, whenever verification succeeds, both the latent-space candidate and its inverse-transformed counterpart in the original state space are analytically proven FISs. We evaluate the approach on 45 AI-controlled systems across three representative control testbeds. Our method finds certified FISs for all 45 systems, whereas an adapted state-of-the-art baseline finds none. It is also faster on 40 of the 45 systems, and the centers of the resulting FISs roughly match domain-expert preferences.

---


### 368. [Second-Order Problem Solving for Recursive Self-Improvement in Formal Verification](https://arxiv.org/abs/2610.05701)

**<font color=#1a73e8>作者：</font>** Yuxuan Jiang, Aditya Vempaty, Ashish Jagmohan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recursive self-improvement (RSI) enables agents to iteratively optimize their workflows via execution feedback. However, standard RSI typically operates as a first-order optimizer: it repeatedly patches surface-level parameters in response to immediate failure symptoms, often leading to trial-and-error thrashing without resolving underlying mechanisms. To address this limitation, we introduce SO-RSI, a framework that elevates workflow optimization to a second-order diagnostic inquiry, investigating why failures occur before committing to structural interventions. SO-RSI passively monitors execution traces for three structural anomalies (recurrence, opposing edits, and expectation mismatch) to trigger targeted mechanism investigations. By executing lightweight diagnostic probes and maintaining persistent inquiry memory across RSI rounds, SO-RSI accumulates causal evidence to guide systematic workflow edits rather than parameter patches. Across Lean 4 proof generation and Verus-based verifiable code generation, SO-RSI improves final held-out pass rates over Naive RSI by 21.8 and 25.8 percentage points under matched 24-hour search budgets. Behavioral analyses further confirm that SO-RSI substantially suppresses failure recurrence and eliminates unproductive zero-progress optimization loops.

---


### 369. [Difference Feature Map Distillation: Transferring Inter-Sample Relational Knowledge Towards Efficient Transformer-Based Tracking](https://arxiv.org/abs/2610.05707)

**<font color=#1a73e8>作者：</font>** Zhicheng Ding, Xinyu Chu, Qing Tian  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In autonomous driving perception, visual object tracking systems must satisfy stringent latency and power constraints while remaining robust in complex and dynamic environments. Although transformer-based trackers achieve state-of-the-art accuracy, their substantial computational and memory overheads hinder deployment on real-time, resource-constrained platforms. To move toward this goal, we propose Difference Feature Map Knowledge Distillation (DFM-KD), a novel relational distillation framework tailored for transformer-based visual object tracking. Unlike conventional feature distillation methods that minimize point-wise discrepancies (e.g., mean squared error) between teacher and student feature representations, DFM-KD transfers knowledge through inter-sample feature differences, explicitly aligning the relational structure of the feature space. By distilling how the teacher models appearance variation and consistency across samples, rather than enforcing similarity in absolute activations, DFM-KD enables the student to better capture the structural dynamics of visual changes within a batch. As a result, the distilled model exhibits enhanced feature robustness and improved tracking performance. Extensive experiments demonstrate that DFM-KD consistently outperforms conventional feature-level distillation methods in both tracking precision and success rates.

---


### 370. [From Pixels, Without Pre-training: Joint Generative and Self-Supervised Representation Learning in One Model](https://arxiv.org/abs/2610.05711)

**<font color=#1a73e8>作者：</font>** Vicente Balmaseda, Ching-Long Lin, Tianbao Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Strong image generation models are conditioned on class labels, aligned to frozen pretrained encoders, or built on separately trained autoencoders. While effective, generation then depends on supervision or pretraining: labels must be annotated, and encoders or autoencoders pretrained for the target domain. We study joint generative and self-supervised representation learning in a single model, enabling self-conditioned generation without labels or pretrained models. This is challenging because the objectives are mismatched: contrastive learning consumes clean augmented views and favors coarse, invariant semantics, while flow matching consumes noisy images and must preserve the fine detail and spatial layout that contrastive learning discards. We propose SCION (Self-conditioned Generation on Self-supervised representation), whose core is a single pixel-space encoder conditioned on the flow timestep and an embedding. For representation learning, this conditioning embedding is a learned global vector shared across images, with the encoder's [CLS] token yielding the semantic representation trained by the contrastive loss. For generative training, the conditioning embedding is the image's own [CLS] representation, while patch tokens pass through a decoder to predict the image. To sample without a reference image at inference, we jointly learn a prior over the embedding. Gradient-norm balancing and stop-gradient mechanisms enable joint optimization in one run. SCION is self-supervised and self-contained, with no labels or pretrained models. On ImageNet 256x256, with the JiT-B recipe and no representation guidance, SCION reaches 8.92 FID, surpassing class-unconditional iREPA, which aligns to pretrained DINOv2 (46.44), and RCG, which conditions on it (14.27). With JiT-L, SCION achieves 5.89 FID without guidance and 3.47 with representation guidance, outperforming RCG with the ADM recipe (6.24).

---


### 371. [SimpleMark: Fast Multi-Bit Text Watermarking under f -Divergence Constraints](https://arxiv.org/abs/2610.05712)

**<font color=#1a73e8>作者：</font>** Benjamin D. Kim, Wanrong Zhang, Weitong Ruan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We introduce a framework for multi-bit text watermarking with security defined directly through $f$-divergence from the base language model distribution. Unlike prior approaches that focus on average-key distortion-freeness or a particular statistical distance, our formulation supports general $f$-divergences, including total variation and KL divergence, and enforces the guarantee for each realized key and embedded message. We develop a coding-based watermarking scheme that optimally biases next-token distributions subject to a prescribed divergence budget, and characterize the resulting tradeoff between embedding rate, decoding reliability, and statistical security. Experimentally, we compare our method against prior multi-bit watermarking schemes across modern language models and payload regimes. Our approach achieves substantially lower watermark detectability while maintaining competitive message-recovery performance and generation quality. Our results provide a unified view of secure multi-bit watermarking and recover several commonly used security notions as special cases.

---


### 372. [ReMaD: Tuning-free Domain Adaptation for Classification and Out-of-Distribution Detection](https://arxiv.org/abs/2610.05718)

**<font color=#1a73e8>作者：</font>** Elijah Bolluyt, Cristina Comaniciu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Reduced-rank Mahalanobis Distance (ReMaD), a novel prototypical distance-based refinement to classification and out-of-distribution (OOD) detection using pretrained models without finetuning. We use embeddings of the target dataset to fit closed-form distribution statistics in the model's latent space which can classify in-distribution samples and detect OOD samples, all without training or prior knowledge of the OOD data. Building on prototype classification and OOD detection, we analyze the distribution properties of large pretrained models when processing new datasets; based on this analysis, we formulate a simple modification to Mahalanobis Distance to adapt models' latent space distributions to new domains by removing unused features, without the finetuning or hyperparameter searches required by other adaptation procedures. We demonstrate the efficacy of this method to adapt existing large pretrained image embedding models to new classification domains outside their trained capabilities by testing across four target datasets, with competitive performance in both classification and OOD detection.

---


### 373. [Inferring physical fields in coupled systems with unknown parameters from incomplete observations using physics-constrained attentive neural operators](https://arxiv.org/abs/2610.05723)

**<font color=#1a73e8>作者：</font>** Shilun Wei, Xiaoqiang Sun, Wei Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Given incomplete measurements of a single physical field in a coupled system with unknown parameters, can we infer its full physical state and identify the underlying parameters? This problem is challenging because multiple coupled fields must be reconstructed simultaneously from limited observations of only one, while the system parameters are unknown. In this work, we propose a machine learning framework for full-field reconstruction and parameter identification of unknown physical systems from sparse observations of a single physical field. Specifically, the cross-attention encoder propagates sparse sensor observations onto a regular grid to construct a sensor-conditioned latent representation, while a Fourier neural operator (FNO) decoder captures global spatial dependencies to reconstruct all coupled physical fields. The network parameters and unknown physical parameters are jointly optimized by minimizing observation losses, governing equation residuals, and boundary/initial condition constraints. The proposed approach is validated on two- and three-dimensional lid-driven cavity flows, a two-dimensional cylinder wake, and a two-dimensional non-ideal magnetohydrodynamics problem, demonstrating the recovery performance of unobserved fields and physical parameters from incomplete observations.

---


### 374. [T-JEPA: A Temporal Joint-Embedding Predictive Architecture for Learning Better Remote Sensing Representations](https://arxiv.org/abs/2610.05731)

**<font color=#1a73e8>作者：</font>** Bowen Peng, Li Liu, Yongxiang Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Earth observation (EO) data provide rich temporal supervision, yet existing remote sensing foundation models mainly exploit sequential observations through imposing predefined pairwise relations or aggregating holistic reconstruction context. We seek to further exploit the sparse and nonuniform temporal sampling inherent in EO sequences as supervisory signals. To this end, we propose T-JEPA, a temporal joint-embedding predictive architecture that learns time-gap-conditioned latent transitions. A shared single-frame encoder processes each observation, while a temporal predictor estimates the complete target latent field from a masked source latent representation and the actual elapsed time. Across multiple temporal intervals, these predictive constraints organize observed states into structured latent trajectories. Asymmetric metadata injection mitigates shortcut learning, and direct supervision across multiple temporal scales proves more effective than recursively rolling out intermediate states. In parallel, masked pixel reconstruction provides complementary supervision for preserving spatial details. Under matched pre-training data and throughput, T-JEPA achieves leading transfer performance on both static and temporal tasks. Analyses further reveal that T-JEPA learns representations with time-gap-dependent transition predictability and coherent latent dynamics, while maintaining strong cross-period consistency, representation diversity, and semantic discriminability.

---


### 375. [Robust Local Optimization Done Right](https://arxiv.org/abs/2610.05743)

**<font color=#1a73e8>作者：</font>** James Pritts, Kevin Köser  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RANSAC scoring and local optimization (LO) impose different robustness requirements, motivating the separation of hypothesis selection from refinement. We systematically isolate the effects of robust-loss shape, incorrectly specified inlier scales, and optimization strategy on essential matrix, fundamental matrix, and homography estimation. A profile-marginal score marginalizes the nuisance inlier scale and selects an inlier partition, from which we estimate the scale that sets the LO loss width; this makes LO robust to an inlier scale specified too large, whereas one specified too small degrades selection itself. Refinement needs gradient from correspondences the seed currently rejects: optimizers that reweight from current residuals stay pinned to their seed, whereas methods with broad basins recover strongly perturbed seeds yet degrade accurate score-selected hypotheses, so basin size alone is insufficient to assess RANSAC LO. Joint half-quadratic optimization balances the two and is the most consistent strategy across model classes. An optimizer matched to the profile-marginal score, which never decreases it, does not reach the best accuracy, challenging the prescription that scoring and refinement objectives should match. Composed from these findings, our RANSAC reduces the median essential-matrix pose error of a state-of-the-art RANSAC on PhotoTourism from 2.23 degrees to 1.58 degrees with a correctly specified inlier scale and from 38 degrees to 6.2 degrees when it is grossly misspecified (128x too large).

---


### 376. [A new design of a fall detection system integrating landmark identification and deep learning techniques](https://arxiv.org/abs/2610.05749)

**<font color=#1a73e8>作者：</font>** Tri Nhut Do, Thi Thuy Le  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This article introduces an innovative system that integrates landmark identification with deep learning to enhance fall detection accuracy and reliability. By utilizing advanced computer vision techniques, such as Media Pipe for spatial recognition, the system effectively differentiates between routine movements and actual falls. The integration of landmarks with a deep learning prediction algorithm minimizes false alarms, ensuring timely responses to genuine falls. Comprehensive experimentation underscores the system's versatility across various scenarios, emphasizing its potential to improve safety and independence for older adults. The training process demonstrates a steady increase in accuracy, stabilizing by the 40th cycle, while error rates decline significantly during the initial cycles. Real-time experiments, involving both male and female participants aged 8 to 50, recorded a remarkable 95% detection rate of falls, demonstrating the system's effectiveness and promising future applications in elder care and smart health monitoring environments.

---


### 377. [Vision-enabled detection of safety helmet compliance in construction zones](https://arxiv.org/abs/2610.05756)

**<font color=#1a73e8>作者：</font>** Tri Nhut Do*, Ba Loc Pham  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In the rapidly evolving field of construction management, worker safety remains a top priority. This paper introduces an innovative vision-based system for real-time detection of helmet compliance, specifically designed for construction sites, utilizing advanced computer vision techniques and machine learning algorithms within the YOLO (you only look once) framework. Our system leverages high-resolution video feeds from strategically positioned cameras to monitor adherence to safety regulations regarding helmet usage. By employing deep learning methodologies, the system effectively identifies individuals not wearing helmets, thereby significantly mitigating the risk of head injuries among workers. Our training and validation results revealed an impressive precision exceeding 97% at mAP@0.5 for both helmeted and non-helmeted individuals. Furthermore, our experiments demonstrate exceptional detection accuracy, demonstrating the system's resilience under varying lighting conditions and diverse worker movements. The consistent decrease in loss and improvement in metrics throughout training validates the effectiveness of the YOLOv8 model in enhancing recognition performance. The implications of this research extend beyond mere regulatory compliance, opening avenues for innovative applications in occupational safety management. This study highlights the critical role of technology in protecting lives and lays the groundwork for future advancements in smart construction environments.

---


### 378. [A Three-Dimensional Reverse-Projection Method for Sparse Point Cloud Completion and Its Application to High-Speed Train Nose Reconstruction](https://arxiv.org/abs/2610.05758)

**<font color=#1a73e8>作者：</font>** Xiaozhen Ma, Zhao Tang, Hanbin Lai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Holes in LiDAR scans of environments with glass windows remain an unresolved problem in three-dimensional reconstruction. This study presents a pipeline for point cloud acquisition, filtering, completion, and surface reconstruction to address sparse sampling and missing window regions in scans of a high-speed train nose. FAST-LIVO2 provides the initial point cloud through multisensor odometry and mapping, and moving least squares (MLS) smooths the observations. We then introduce three-axis projection-based subdivision and interpolation with reverse hole boundary identification, referred to as three-axis reverse completion. The method interpolates missing regions from observations around each hole. Greedy projection triangulation, Poisson surface reconstruction, and a Marching Cubes-based pipeline generate meshes from the completed point cloud. Experiments on a proportionally scaled display model of a high-speed train nose show that the proposed method fills missing point cloud regions around the glass windows. Under the evaluation setting used in this study, greedy projection triangulation yields lower geometric distance errors than the other two reconstruction pipelines. The pipeline supports non-contact digital modeling of train nose geometry and provides a practical approach to reconstructing objects with glass windows.

---


### 379. [Controllable Road Marking Generation](https://arxiv.org/abs/2610.05771)

**<font color=#1a73e8>作者：</font>** Zhiyu, Yufan Zhang, Ruichen Tan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lane and road markings provide critical guidance for vehicle navigation and multi-agent coordination, yet authoring them at scale remains a manual workflow that limits quantitative analysis and scenario testing. We introduce Controllable Road Marking Generation, which synthesizes a missing center-region marking layout from a drivable-area mask, optional outer-ring markings, and a textual description. Our benchmark uses deterministic, metadata-derived prompts and three output channels: lane dividers, road dividers, and pedestrian crossings. We develop a conditional bird's-eye-view (BEV) pipeline that combines (i) a text-conditioned latent rectified-flow DiT trained with a topology-aware auxiliary loss, (ii) Gaussian-blurred training targets that stabilize learning of thin, sparse markings, and (iii) Structured Gaussian Render (SGR), a training-free post-process that recovers crisp divider geometry by extracting polylines, fitting cubic Bézier curves, and re-rendering them as anisotropic super-Gaussian primitives. On 4,597 Argoverse~2 test tiles, our system achieves Buffered F1 of 80.8 and clDice of 50.2, compared with 38.8 and 24.6 for an adapted state-of-the-art mask-refinement baseline. On Waymo dataset, it yields 88.0 Buffered F1 and 66.2 clDice. Component ablations show complementary connectivity gains from topology-aware supervision and SGR. Text-editing experiments reveal that stronger guidance improves edit success but also increases changes to non-target structures. We see this framework as a step toward simulation-ready road-marking variation, automated map completion, and early-stage infrastructure design exploration.

---


### 380. [Smart Navigation for Visual Prostheses in Virtual Reality: An End-to-End Framework for Priority-Based Scene Translation and Path Guidance](https://arxiv.org/abs/2610.05772)

**<font color=#1a73e8>作者：</font>** Mohamed H. Abdellatif, Fatma S. Elsharkawy, Nouran H. Qassem 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Visual prosthetics provide a promising direction for partial restoration of functional vision for people with total retinal blindness. However, existing systems face significant challenges in translating complex visual scenes into meaningful perceptions due to limited spatial resolution, leading to difficulties in scene understanding. Furthermore, existing solutions don't adequately account for user requirements and concerns, and this creates a significant gap between user expectations and the developed solutions. To address these gaps, we conducted interviews with 10 blind human subjects. These interviews essentially indicated that the main key challenge for these people is outdoor navigation. In this paper, we present an end-to-end smart navigation system for visual prostheses users. Our approach employs a three-stage framework. First, an object detector is implemented to identify and localize points of interest for navigation tasks in pedestrian environments, and simultaneously generate the safest paths available to the users. Second, the detected objects are abstracted into simple geometric shapes suitable for low-spatial-resolution vision. The detected objects are filtered based on a multi-criteria priority scoring function. Finally, this information is encoded into optimized stimulation parameters, which are fed into the visual prosthesis implants to generate enhanced phosphene representations for obstacle avoidance and path planning. This whole system is validated with sighted participants using virtual reality to simulate outdoor navigation. Our smart navigation system improves user independence while taking into account the limitations of visual prosthetics.

---


### 381. [A Spatiotemporal Semantic Importance-Guided Unified Compression and Editing Framework for AI-Generated Videos](https://arxiv.org/abs/2610.05779)

**<font color=#1a73e8>作者：</font>** Xihua Sheng, Dong Liu, Chang Wen Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-generated videos are rapidly increasing in volume, duration, and resolution, creating growing demands for efficient storage and transmission. Unlike natural videos captured from the physical world, AI-generated videos are samples from a learned generative distribution, where semantic structures are critical to content consistency, while many local textures and stochastic details can be plausibly regenerated. This distinction suggests that compression should preserve semantically important spatiotemporal information rather than reconstruct every pixel of a particular generative sample. Beyond reconstruction, AI-generated videos also create a practical need for prompt-based editing, where users expect to modify generated content while preserving its original spatiotemporal semantics. Motivated by these observations, we propose a unified compression and editing framework for AI-generated videos that incorporates a frozen video generator as a reusable generative prior. Within this framework, we design three spatiotemporal semantic importance-guided techniques that respectively address what to transmit, how much to transmit, and how to use the transmitted side information. First, an innovation selection method projects the latent discrepancy using spatiotemporal semantic importance, so that the selected innovations prioritize semantic invariants over replaceable generative variations. Second, a frame-adaptive bit allocation method estimates the nonuniform semantic demands of latent frames and allocates more innovations to frames requiring stronger semantic preservation. Third, a unified reconstruction and editing method continuously adjusts the influence of the transmitted side information, enabling the same compressed representation to provide strong guidance for faithful reconstruction or serve as a flexible semantic anchor for structure-preserving prompt-driven editing.

---


### 382. [CLARA: Can AI Assess Developmental Appropriateness in Children's Stories?](https://arxiv.org/abs/2610.05783)

**<font color=#1a73e8>作者：</font>** Sijing Yin, Zirui Wang, Qian Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Assessing the developmental suitability of children's narratives is important for educational recommendation and developmental literacy research, yet such assessment typically relies on subjective and difficult-to-scale human judgment. This raises an important question: Can AI systems approximate human developmental judgments of children's stories? To study this problem, we introduce CLARA, a cognitively grounded framework for developmental narrative understanding through structured annotation across cognitive (COG), language (LAN), and social-emotional (SEL) dimensions, together with a bilingual benchmark resource containing 1107 Chinese--English children's stories with normalized silver developmental references and structured developmental annotations. We evaluate CLARA through benchmark comparison, component analysis, translated bilingual consistency analysis, and blinded human evaluation with educators. Experimental results show that structured developmental annotation achieves substantially stronger alignment with developmental references and human judgments than readability-based methods and direct prompting baselines. Overall, our findings suggest that AI systems can approximate certain aspects of human developmental judgment when guided by structured developmental annotation, while also highlighting the importance of interpretability and human oversight in educational NLP.

---


### 383. [Adaptive Utilization of Low-Rank Adaptation via Conditioned Gating](https://arxiv.org/abs/2610.05800)

**<font color=#1a73e8>作者：</font>** Guang Yang, Changhao Guan, Chao Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Low-Rank Adaptation (LoRA) achieves parameter-efficient fine-tuning by constraining model updates to a low-rank subspace and has been widely used in practice. However, LoRA typically employs a shared low-rank update across tokens, which limits its ability to fully exploit the adaptation subspace for tokens from different sequences. To address this issue, we propose an adaptive utilization of Low-Rank Adaptation (U-LoRA), which employs conditioned gating to explicitly learn effective token-level utilization of the limited low-rank adaptation subspace. Specifically, U-LoRA generates utilization coefficients along low-rank directions for each token and jointly coordinates and constrains them using sequence-level contextual information, thereby inducing more consistent adaptive patterns within a sentence. To further enhance training stability, we introduce a bias-corrected exponential moving average (EMA) historical prior that calibrates utilization signals across optimization steps, suppressing noise caused by batch-to-batch fluctuations. The effectiveness of our method arises from a better utilization of the existing low-rank subspace via input-conditioned strategies, rather than from expanding the subspace. Experiments on mathematical reasoning and natural language understanding benchmarks demonstrate that U-LoRA achieves competitive performance under comparable parameter budgets when with strong LoRA baselines and recent variants.

---


### 384. [Gauss-Map Variation for Image Denoising: Geometric Analysis and an Anderson--Accelerated Majorization--Minimization Method](https://arxiv.org/abs/2610.05801)

**<font color=#1a73e8>作者：</font>** Haibin Su  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a Gauss-map variation (GMV) model for image denoising that measures the spatial variation of the tangent-plane projectors of the scaled image graph. We establish an equivalent representation of the regularizer in terms of the corresponding Gauss map and, using differential geometric tools including tubular coordinates and the Frenet frame, analyze its behavior across general $C^2$ and piecewise $C^2$ boundaries. The resulting estimates provide edge- and corner-contrast preservation properties. To solve the proposed model, we introduce a bilinear decomposition involving a unit normal field and a scalar magnitude field and develop an Anderson-accelerated majorization--minimization algorithm. The normal field subproblem admits an explicit pointwise majorization--minimization update, which is combined with an Anderson acceleration. For both $L^1$ and $L^2$ data fidelity terms, we establish sufficient decrease and boundedness of the iterates and prove that the generated sequence converges to a critical point of the penalized model. Numerical experiments on synthetic and natural images demonstrate the boundary preserving capability of the proposed model and its competitive performance in removing Gaussian and impulsive noise.

---


### 385. [DiMOS: Doob-Guided Inference-Time Multi-Objective Search for Scientific Design](https://arxiv.org/abs/2610.05808)

**<font color=#1a73e8>作者：</font>** Ziqing Wang, Qijie Zhu, Weimin Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific design often requires jointly satisfying multiple objectives and constraints. Pretrained masked diffusion models provide a generative foundation for this task, but fine-tuning them to meet these objectives and constraints incurs additional training costs, motivating inference-time guidance with frozen models. However, such guidance faces two challenges: pass-or-fail constraints and black-box reward models may provide no useful gradients, while jointly satisfying multiple requirements can leave a small feasible region, making feasible designs difficult to find within a limited inference budget. To address these challenges, we introduce DiMOS, a training-free framework for multi-objective scientific design. Using joint rewards from candidate completions, DiMOS performs approximate Doob-guided local resampling without requiring reward gradients. To allocate computation efficiently, it uses budget-efficient trajectory search to focus computation on promising continuations. Across six DNA, protein, and RNA tasks, DiMOS attains the highest joint success rate at comparable generation times, up to $1.98\times$ the strongest baseline on DNA and protein, while maintaining high sequence uniqueness and naturalness.

---


### 386. [Image resolution enhancement for advanced semiconductor nodes](https://arxiv.org/abs/2610.05809)

**<font color=#1a73e8>作者：</font>** Lucas Rencker, Omid Tajalizadehkhoob, Khalid Elsayed 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Advanced semiconductor nodes are pushing the limits of feature sizes and require metrology with sub-nm resolution without compromising on the throughput as needed for in-line process control. Recently, high-throughput scanning probe microscopy (SPM) based metrology and inspection tools capable of meeting these needs have been introduced to the market and qualified for use in HVM. While innovative measurement methods and tool architecture have allowed for a leap of improvement in throughput, the next step in further reducing imaging time can be obtained through the application of machine learning for enhancing the resolution of measured images for extraction of relevant parameters. In this work, we provide the general framework under which a neural network-based resolution enhancer is designed and used for SPM images. We showcase the effectiveness of this framework using measurements performed on Line/Space structures with a pitch of 200 nm. For the reusability of a pre-developed pre-trained model, we additionally leverage transfer learning and show that a new model for slightly differing structures can be re-trained and calibrated with a smaller data set of measurements performed on Line/Space structures with a pitch of 100 nm.

---


### 387. [Online AutoML: Evaluating Poisoning Attacks on Adversarial Training Defense Strategy in IoT Networks](https://arxiv.org/abs/2610.05810)

**<font color=#1a73e8>作者：</font>** Chukwunonso Henry Nwokoye, Khalil El-Khatib, Li Yang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine learning (ML)-powered poisoning attack vectors are adversarial maneuvers whereby an attacker intentionally inserts, corrupts, or alters training data to distort an ML model's learning process. The objective is to diminish model efficacy, instill biases, induce misclassifications, or include concealed backdoors that may be attacked during implementation. In streaming contexts, poisoning attacks pose significant risks since models perpetually update based on incoming streams of data. An assailant may incrementally introduce harmful samples into this data stream, leading the model to assimilate erroneous features over time without timely identification. Therefore, this study is aimed at evaluating the efficacy of the adversarial training (AT) defense approach against poisoning attacks (label flip and noise injection) using an online AutoML pipeline for Internet of Things (IoT) networks. Specifically, poisoning attacks (label flip and noise injection) were applied to streaming-capable AutoML learners (Hoeffding Tree (HT), Leveraging Bagging (LB), Adaptive Random Forest (ARF), Hoeffding Adaptive Tree (HAT), and Streaming Random Patches (SRP)). Under the strongest poisoning rate (PR = 1.0), AT-SRP achieved the highest F1-score against label flip poisoning (0.904), while AT-LB achieved the highest F1-score against noise-injection poisoning (0.933). Finally, several drift detection methods were used for rolling accuracy and prequential evaluation.

---


### 388. [Feature identification for parameter extraction and defect detection using machine learning](https://arxiv.org/abs/2610.05812)

**<font color=#1a73e8>作者：</font>** Yan Guo, Helda Pahlavani, Artem Khachaturiants 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Process control of advanced semiconductor nodes is not only pushing the limits of metrology equipment requirements in terms of resolution and throughput but also in terms of the richness of data to be extracted to enable engineers to finetune the process steps for increased yield. The move towards 3D structures requires extraction of critical dimension parameters from structures which can vary largely from layer to layer. For in-line process control, the necessary automation forces the development of layer and equipment-specific dedicated image processing algorithms. Similarly, with the increase in stochastic defects in the EUV era, detection of defects at the nm scale requires the identification of features captured in low resolution to meet the throughput requirements of HVM fabs, which can again lead to custom algorithm development. With the emergence of ML-based image processing methods, this process of algorithm development for both cases can be accelerated. In this work, we provide the general framework under which the images obtained from high-speed scanning probe microscopy-based systems can be used to train a network for either feature detection for parameter extraction or defect identification.

---


### 389. [Plan Canvas: Fixed Reasoning Regions for Continuous Language Flows](https://arxiv.org/abs/2610.05815)

**<font color=#1a73e8>作者：</font>** Miaohe Niu, Pengxiang Li, Jingbo Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continuous language flows generate text by denoising all positions of a target canvas together. The natural way to add reasoning to such a model is to write a trace ahead of the answer, but the trace length changes from question to question. The answer start is therefore unknown during denoising, and the model has to decide the trace length, the place of every trace token, and the answer at the same time. We propose Plan Canvas to fix the boundary between the trace and the answer. A plan region of fixed capacity holds a compact trace, supervised padding fills its unused positions, and the answer starts at a fixed position. The fixed regions also allow separate denoising clocks for the plan and for the answer. With the trace text, backbone, and canvas length of the free-trace baseline held fixed, Plan Canvas improves accuracy on ProsQA and on Deep ProsQA, a graph benchmark with longer proofs. On Deep ProsQA, accuracy rises from 73.0\% to 87.0\%, the share of questions answered with a valid path rises from 30.8\% to 59.1\%, and the gain is largest on the longest proofs.

---


### 390. [Level-of-Token Diffusion](https://arxiv.org/abs/2610.05816)

**<font color=#1a73e8>作者：</font>** Kiyohiro Nakayama, Brian Chao, Jan Ackermann 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image and video diffusion models allocate equal computation to every region, even when the intended scene calls for varying levels of detail. The spatial distribution of detail can often be anticipated before generation, indicating where computation can be reduced. We introduce Level-of-Token (LoT) Diffusion, a framework that turns this knowledge into an explicit multiresolution token layout (Level-of-Token layout) for adaptive and efficient generation. Tokens represent rectangular patches of varying sizes and shapes, allocating finer tokens where detail is needed and coarser tokens elsewhere. We adapt pretrained diffusion transformers to LoT layouts through a patch-wise asymmetric flow parametrization and embeddings for multiresolution tokens, preserving full-resolution flow prediction at every denoising step while processing only a reduced token sequence. LoT Diffusion enables layout-adaptive generation while preserving pretrained generative priors. We demonstrate LoT with layouts derived from semantic masks, bounding boxes, texture variance, and depth-of-field cues, as well as agentic plans. Across image and video generation, LoT offers favorable quality-efficiency tradeoffs, with significant speedups determined by the layout's token budget. Our project website is at this https URL.

---


### 391. [Usefulness of Quantile-Aware Diffusion Modeling for Highly Imbalanced Tabular Data](https://arxiv.org/abs/2610.05825)

**<font color=#1a73e8>作者：</font>** Abu Talha, Peng Liu, Souradyuti Paul  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classification problem in the context of highly imbalanced data is a major challenge in many real-world applications (e.g., FinTech, healthcare, etc.). In these cases, the vast majority of instances belong to a single class and a small fraction represent the minority class (often the most critical class). Recently, diffusion models have emerged as powerful approaches to reduce the degree of ``imbalanced-ness'' in the dataset; they work by generating synthetic data by capturing complex data distributions using iterative transformations. However, standard diffusion models are not inherently suited to highly skewed or heavy-tailed data, due to inbuilt quadratic error loss, which lacks the structural sensitivity to capture rare, extreme values, and minority-class nuances. We propose a novel approach, namely, Quantile-TabDDPM, based on a quantile-regularized denoising objective that combines the standard quadratic error loss with a quantile loss term to explicitly capture rare events while preserving the theoretical grounding of the original denoising objective. We extensively evaluated our approach on a real-world credit card transaction dataset characterized by extreme class imbalance. The results demonstrate that the integration of diffusion-based synthetic data generation with a quantile-regularized denoising objective provides a robust and effective framework for fraud detection in highly imbalanced datasets.

---


### 392. [Data-Driven Personas for Survey Simulation: Insights into Simulation Alignment Across Data-Access Regimes](https://arxiv.org/abs/2610.05828)

**<font color=#1a73e8>作者：</font>** Dongryeol Lee, Weronika Łajewska, Leonardo Perelli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> However, many existing steering approaches rely on target-domain human data for fine-tuning or prompting that is costly to collect and raises privacy concerns. In this paper, we study demographic group-level survey simulation, where personas induced from heterogeneous, anonymized public behavioral data condition agents that simulate responses of individuals from specific demographic groups. We examine whether representative personas can be induced from diverse sources and analyze how the domain, scale, and granularity of the source data affect survey simulation alignment. We find that personas induced from out-of-domain sources rarely outperform simulations conditioned only on basic demographic information, largely due to population mismatch. However, when personas are accurately assigned to the target demographic groups, alignment improves substantially. Finally, personas induced from target-domain survey data generalize better as more survey question history becomes available, suggesting that richer behavioral evidence enables more stable persona trait inference that transfers to better unseen questions simulation alignment.

---


### 393. [Selecting Long-Horizon Trajectories for Reliable and Efficient Terminal-Agent Training](https://arxiv.org/abs/2610.05831)

**<font color=#1a73e8>作者：</font>** Cuong Dang, Hoang Anh Just, Ruoxi Jia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Terminal agents are commonly trained by imitating long teacher trajectories, yet how much of each trajectory to supervise remains unexplored. We study the \emph{supervision horizon}, the number of trajectory tokens retained for training, and show that it is a key design axis for reliability and cost. Reliability improves with longer horizons but saturates: on Terminal-Bench, a 12K-token horizon solves more tasks than 16K ($29\pm0.7$ vs.\ $26\pm0.8$) while requiring 30\% less training time. The horizon also shapes agent behavior: short horizons cause premature termination, intermediate horizons yield productive error recovery, and long horizons induce over-persistence. We analyze this saturation through a bias--complexity bound, in which longer supervision reduces temporal supervision bias but increases finite-sample estimation error from more heterogeneous late-stage histories. Guided by this analysis, we propose \emph{selective long-horizon refinement}, which first trains on short prefixes and then refines only on continuations that are most likely under the warm-start model. It consistently outperforms full long-horizon training. At 16K, it raises successful attempts from $110\pm2.7$ to $126\pm2.1$ and tasks solved in at least six of eight attempts from $9\pm0.7$ to $14\pm0.6$; with half of the long-horizon data, it still reaches $122\pm2.4$ while cutting training time by 23\%. The gains transfer across benchmarks, from $64\pm2.6$ to $73\pm2.1$ on Terminal-Bench v2.0 and from $137\pm2.7$ to $155\pm2.2$ on OpenThoughts-TBLite. For long-horizon supervision, selecting the right trajectories matters more than training on all of them.

---


### 394. [HiER-BLS: A Hierarchy-Guided and Error-Correcting Robust Incremental Broad Learning System](https://arxiv.org/abs/2610.05834)

**<font color=#1a73e8>作者：</font>** Gongli Zhang, C. L. Philip Chen, Zhulin Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Broad Learning System (BLS) supports analytical training and incremental expansion, but its growth needs guidance on which inputs new blocks should learn from. Weight errors pose a further challenge by displacing learned outputs across class boundaries. We propose HiER-BLS to couple hierarchy-guided representation growth with error-correcting learning. Successive blocks focus on inputs selected by feature importance and correlation while preserving earlier representations. The evolving branch guides encoded learners through subspace size and sample confidence, so its learning experience informs both their feature views and supervision. For finite broad readouts, we show how codeword correlations transform fitted class scores. Prediction preservation depends on the distance from the actual output to the nearest decoding boundary relative to the model's sensitivity to weight errors. Experiments on five image and five tabular datasets demonstrate improved classification performance over representative BLS variants. Component studies show that hierarchy guidance benefits the encoded branch even when the guiding branch has lower standalone accuracy, with further gains from combining their scores. Longer codes continue to improve accuracy under stronger Gaussian weight errors after clean accuracy has largely saturated.

---


### 395. [Adaptive-Shot Hybrid Quantum Anomaly Detection for Tactile Internet Security: Reliability-Aware Measurement Allocation Under Resource Constraints](https://arxiv.org/abs/2610.05835)

**<font color=#1a73e8>作者：</font>** Mubassir Serneabat Sudipto, Shakil Ahmed, Ashfaq Khokhar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tactile Internet (TI) security analytics must balance reliable thresholded decisions with constrained computational and measurement resources. We study this tension for finite-shot hybrid quantum anomaly inference and introduce the Adaptive-Shot Variational Quantum Circuit (AS-VQC) policy. This validation-calibrated policy begins each record at 128 shots and cumulatively escalates through 256, 512, and 1024 shots only when the finite-shot anomaly score remains close to a validation-selected security threshold. The quantum scorer is evaluated as an off-path security analytics component rather than part of the haptic critical path. Using a 4,875-record CESNET-TimeSeries24-derived aggregate-flow benchmark, leakage-safe random, entity-group-disjoint, and temporal holdouts, and five trained quantum neural network (QNN) checkpoints per holdout, the primary AS-VQC-95 (beta = 0.95) policy averages 129.2, 276.9, and 131.2 shots per record, saving 87.4%, 73.0%, and 87.2% of the uniform 1024-shot baseline (Fixed-1024), respectively. The decision disagreement with analytic (exact-expectation) inference is 0.771%, 0.409%, and 0.635%, lower than both the uniform 128-shot baseline (Fixed-128) and a matched-budget shuffled-allocation control. Fixed-1024 remains more decision-stable, establishing a measurable reliability-resource trade-off rather than cost-free equivalence. A more conservative AS-VQC-99 (beta = 0.99) further reduces disagreement while using fewer than 512 average shots across all holdouts. These results show that finite quantum measurements can be treated as an inference resource and concentrated on boundary-sensitive TI-security decisions while exposing checkpoint-dependent escalation under unseen-entity conditions.

---


### 396. [CACFG: Curvature-Aware Classifier-Free Guidance and Optimal Control](https://arxiv.org/abs/2610.05845)

**<font color=#1a73e8>作者：</font>** Max Collins, Dasith de Silva Edirimuni, Jordan Vice 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models generate samples by learning to reverse a fixed corruption process, and classifier-free guidance (CFG) is the standard mechanism for conditioning this process on a desired class or prompt. CFG can be applied at varying guidance strengths, and while higher strengths improve image quality and conditional alignment, too high a guidance strength can degrade image quality and diversity. Furthermore, CFG violates principled diffusion sampling dynamics, and existing explanations for why it works despite the violation disagree on the underlying theory or do not extend to deterministic samplers used in practice. We address both these issues. We first frame CFG sampling as a continuous-time optimal control problem, treating the sampling trajectory as a sequence of controls chosen to maximise the probability of the desired condition. Solving the resulting Hamilton--Jacobi--Bellman equation shows that CFG is recovered under specific path costs when using an unconstrained control set. We argue this lack of constraint is responsible for CFG's failure at high guidance strengths, since it permits the sampling path to move arbitrarily far from the current image estimate. To fix this, we propose curvature-aware CFG (CACFG), which constrains the control set to a hypersphere informed by the Gaussian regularisation used when training variational autoencoders. We show that the control inputs produced by CFG sampling routinely violate this bound, and that across diffusion models, datasets, and guidance schedules, CACFG achieves superior generative quality at mid-to-high guidance strengths with a less severe quality-diversity tradeoff than regular CFG.

---


### 397. [RepICL: Reusable In-Context Prediction Across Heterogeneous Representation Spaces](https://arxiv.org/abs/2610.05852)

**<font color=#1a73e8>作者：</font>** Yu-Hsiang Liu, Kuan-Yu Chen, Chih-Sheng Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Frozen representations are widely reused for downstream classification, yet each new task typically requires fitting a new predictor. We ask whether the few-shot prediction procedure itself can instead be learned once and reused across datasets and representation spaces. To study this question, we introduce RepShiftBench, comprising 1,218 encoder--dataset tasks across text, image, and audio, with separate evaluation of generalization to unseen datasets, unseen encoders, jointly unseen datasets and encoders, and unseen modalities. The benchmark exposes a substantial gap: Logistic Regression fitted independently on each episode outperforms every evaluated in-context learner across all settings. We introduce RepICL, a meta-trained in-context learner that canonicalizes each episode through episodic whitening before prediction. Its inductive variant, RepICL-I, surpasses Logistic Regression in all 12 benchmark settings, while RepICL-T substantially outperforms existing transductive methods. Ablations identify episodic whitening as the primary source of these gains, while showing that it is not a universally beneficial preprocessing step. Across both variants, the gains concentrate on queries for which simple support prototypes favor the wrong class or provide little separation between the true class and competing classes. Transduction provides its largest additional gains when limited support coverage gives a misleading view of class separation. Together, these results demonstrate that a shared few-shot prediction procedure can generalize beyond the representation spaces observed during training.

---


### 398. [The Blind Spot Paradox: When Adaptive Classifiers Defeat Drift Detectors](https://arxiv.org/abs/2610.05853)

**<font color=#1a73e8>作者：</font>** Raphaël Minato, Fabrice Popineau, Arpad Rimmel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Monitoring concept drift from an adaptive classifier's error stream creates an operational conflict with the model's own update loop. When internal adaptation outpaces evidence accumulation, accuracy recovers before cumulative detectors (CUSUM, Page-Hinkley) can reach threshold. Instrumenting an Adaptive Random Forest (ARF) shows that surviving trees absorb 98.6% of the post-drift error transient through incremental leaf updates alone. The first background tree swap accounts for just 0.71% of this erased error volume, but drops external detection rates by 31 percentage points. We derive the finite-horizon boundary where cumulative evidence fails to cross threshold and measure a critical magnitude floor ($\Delta e_c = 0.120$) below which false-alarm budgets preclude detection. This failure manifests as missed shifts on stationary streams and false-alarm flooding triggered by internal tree swaps on noisy baselines. We validate on synthetic shifts, ARMA-GARCH series (ProteuS), and tabular benchmarks (BAF, INSECTS); on the synthetic sweep at a standard threshold, the blind spot appears at $\Delta e \approx 0.25$, showing why classical benchmarks like SEA ($\Delta e \le 0.21$) failed to reach it.

---


### 399. [TurboPairFormer: Fast and Stable Protein Folding Model Training with an Optimized Triangle Attention Kernel](https://arxiv.org/abs/2610.05854)

**<font color=#1a73e8>作者：</font>** Yide Ran, Chelsea Lowman, Jan Domański 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Triangular attention is a core computation in AlphaFold3-style biomolecular models, with cubic cost in token count. Its shared pair bias adds a gradient reduction across attention slices to the usual reductions over queries and keys. The open-source backends we examine handle these reductions through repeated probability recomputation, floating-point atomics, or full score-gradient storage. Separately, computing the softmax backward correction from BF16-rounded forward outputs loses numerical precision. We present TurboPairFormer, a triangular attention implementation for NVIDIA Hopper GPUs that addresses both issues. Our key-tile-parallel backward algorithm recomputes each probability tile once for the query, key, value, and pair-bias gradients, using ordered partial reductions for deterministic accumulation without floating-point atomics or full score-gradient storage. Output-residual compensation retains a BF16 approximation of the output-rounding residual to compute the backward correction more accurately in FP32, without changing the BF16 output. With BF16 inputs at crop sizes 384, 640, and 768 and head dimensions 16 and 32, TurboPairFormer achieves the lowest mean query, key, and pair-bias gradient RMSE against an FP64 reference among the implementations compared in this paper. Residual compensation reduces these RMSE values by 28-47% in controlled ablations. All four gradients are bitwise identical across five repeated calls in all 600 input cases under fixed execution conditions. Integrated into OpenFold3 with our triangle multiplication kernels, TurboPairFormer achieves the lowest GPU computation time per optimizer step among the evaluated backend configurations on 16 H100 GPUs, with speedups of $1.73\times$ over OpenFold3's Triton backend and $1.13\times$ over cuEquivariance at crop size 768.

---


### 400. [Weave Mamba Fusion: Global Cross-Scale Interaction for Lightweight Face Detection](https://arxiv.org/abs/2610.05865)

**<font color=#1a73e8>作者：</font>** Dohun Kim, Jinmyung Jung  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feature pyramid methods, from FPN to BiFPN, have achieved strong performance in face detection by fusing multi-scale features. However, detecting faces under unconstrained conditions, such as small scale, occlusion, and extreme pose, remains difficult, as it requires global cross-scale dependencies that local fusion cannot model. State space models such as Mamba provide global context with linear complexity by scanning features as a sequence, and therefore offer a promising direction for this problem. Nevertheless, such a scan needs the two pyramid scales combined into a single feature map, and the way they are combined determines whether cross-scale structure is preserved. Summation collapses the two scales before the scan, so the scan has no cross-scale structure to exploit, while concatenation keeps both scales but at far higher cost. To address this, we propose \textbf{Weave Mamba Fusion (WMF)}, which interleaves two adjacent pyramid scales column by column so that each step of a horizontal bidirectional SS2D scan moves from one scale to the other. With partial-channel processing and parameter-free de-weaving, WMF enables efficient cross-scale interaction while preserving feature structure. Integrating WMF into every fusion node yields \textbf{WeaveBiFPN}, the neck of our \textbf{WeaveFace} detector. On WIDER FACE, WeaveFace achieves 91.41\% mean AP with only 0.34M parameters and 1.16 GFLOPs, outperforming prior detectors under 0.5M parameters. Its largest gains are on the Hard subset, where it reaches 87.14\% AP. The code is publicly available at \url{this https URL}.

---


> [!TIP]
> 当前位于：**351-400**（第 8/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
