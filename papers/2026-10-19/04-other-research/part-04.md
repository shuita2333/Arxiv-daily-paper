# 📦 其他研究 | 2026年10月19日

> 本类共 **278** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-278](./part-06.md)

---

### 151. [Kolmogorov-Arnold Networks: Curse of Dimensionality and Structural Bias](https://arxiv.org/abs/2610.21480)

**<font color=#1a73e8>作者：</font>** Yunhao Ni, Yuxin Guo, Jie Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kolmogorov-Arnold networks (KANs) have a dimension-independent approximation exponent when the target admits a sufficiently smooth representation by univariate edge functions. We ask whether this favorable scaling belongs to the architecture or to the assumed target class. For arbitrary-depth standard spline-KANs, we prove a worst-case lower bound on isotropic Sobolev balls: below a dimension-independent accuracy threshold, the required number of spline coefficients grows at least exponentially with input dimension. Existing composition-matched MLP results, by contrast, show that favorable exponents on low-arity targets are not exclusive to KANs. We also revisit empirical comparisons. On four scaling-law targets, spline-KAN approximants constructed from known decompositions transfer exactly to MLPs with the cubic ReLU activation $\sigma(x)=(\max\{0,x\})^3$, although their full dense parameter counts are larger. In controlled ridge-profile scans, KANs have a strong advantage when each nonlinear component depends on one input coordinate. When a component couples multiple input coordinates, this advantage may narrow sharply. At tight budgets, interacting targets often favor MLPs. In the random-label test on MNIST, ReLU-MLPs fit the randomized training labels more efficiently than spline-only KANs. Together, these results locate favorable scaling in target structure and a compatible inductive bias, not a general KAN-specific escape from the curse of dimensionality.

---


### 152. [AI-Driven Disaster Response and Displacement Monitoring](https://arxiv.org/abs/2610.21482)

**<font color=#1a73e8>作者：</font>** Noora Al-Emadi, Muhammad Imran, Yin Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> ARTIFICIAL INTELLIGENCE (AI) has demonstrated its potential across a wide range of humanitarian tasks, offering scalable and data-driven solutions to some of the world's most pressing challenges. For instance, in addressing climate change, AI-powered models are being used for faster and more accurate global weather forecasting, control and design of renewable energy, and monitoring deforestation. Machine learning algorithms analyze satellite imagery and socioeconomic data to predict poverty and promote sustainable development. AI has also transformed disaster response and conflict monitoring, providing innovative solutions for assessing damage and urgent needs and tracking displacement.

---


### 153. [Context Matters! Social, Spatial, and Semantic Coordination with an Embodied Agent in Immersive Analytics](https://arxiv.org/abs/2610.21484)

**<font color=#1a73e8>作者：</font>** Andrew Cunningham, Nicolas Barbotin, Adam Drogemuller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Embodied AI agents in Augmented Reality (AR) could enable more natural collaboration in immersive analytics by engaging users through spatial, conversational, and visual interaction. However, designing such agents requires careful attention to context. We propose a preliminary conceptual framework for context-aware design of embodied agents structured around three dimensions of spatial, social, and semantic. This framework is further categorised into embeddedness (how agents are situated in the contexts) and awareness (how agents perceive and respond to the contexts). To explore this, we present Cobot, an embodied AI agent designed as a design probe. Cobot supports context-sensitive interaction through features such as gaze cues, spatial sound, and task-aware behaviour. We reflect on its design and identify implications for future contextaware embodied agents.

---


### 154. [Phase Kernel Lifts Capacity of Dense Associative Memory](https://arxiv.org/abs/2610.21493)

**<font color=#1a73e8>作者：</font>** Yifei Zhao, Ying Tang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dense associative memory underlies modern attention mechanisms; however, Modern Hopfield Networks (MHNs) with linear kernels yield overlapping attractor basins and spurious states under high memory load, limiting their theoretically exponential storage capacity in practice. We construct a class of nonlinear phase kernels that modify the energy landscape and retrieval dynamics, and prove that these kernels preserve exponential storage capacity and local fixed-point convergence under given conditions on kernel smoothness, memory separation, and memory distributions. The framework is instantiated by the Sigmoidal Phase Hopfield Network (S-Hop), which guarantees monotone energy descent and mitigates practical capacity loss. S-Hop has $8.3\times$ and $4\times$ gains in one-step noisy retrieval load over Uniform Hopfield Networks (U-Hop) on CIFAR-10 and TinyImageNet respectively, and reaches a $50\times$ gain in first-failure load for ImageNet. The results demonstrate that phase kernels provide a principled route to robust dense associative memory.

---


### 155. [FilterFusion: Prior-Guided Adaptive Filter Fusion for Efficient Video Denoising](https://arxiv.org/abs/2610.21505)

**<font color=#1a73e8>作者：</font>** Wenlong Yang, Weihang Yuan, Canran Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world video denoising for communication systems must handle mixed degradations such as sensor noise, compression artifacts, and motion-induced inconsistency while remaining deployable under tight latency budgets. Purely deep models often achieve high accuracy but come with significant computational cost, whereas classical filters are robust and efficient but insufficiently adaptive. We present FilterFusion, a prior-guided multi-frame denoising framework that combines temporally-aware learned features with an interpretable bank of denoising branches. The model predicts a low-cost guidance signal and uses it to adaptively mix a compact set of denoising responses at the original resolution. The lightweight design uses only 109K parameters and explicitly injects temporal variance and spatial variance cues into the low-resolution controller. On CRVD (real sensor noise), it reaches 34.72 dB PSNR and 0.9330 SSIM with only 0.18 GFLOPs (network-only). Because the filter-bank operations are simple and regular (Gaussian blur, median, weighted sum), a straightforward compiled C implementation of the synthesis path achieves 17.9ms per frame (55.9 FPS) on a single CPU thread at 1080p---exceeding real-time and 122--252 times faster than lightweight CNN baselines that require over 2 seconds per frame. The results demonstrate a strong quality-efficiency-speed trade-off and a practical route to real-time denoising through low-resolution control and explicit filter-based synthesis.

---


### 156. [QREF: Improving DeepSearch Agents by Aligning Search with Reasoning via Query Refinement and Evidence Filtering](https://arxiv.org/abs/2610.21512)

**<font color=#1a73e8>作者：</font>** Yujia Chen, Yuhui Wang, Junzhe Wang 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> DeepSearch agents achieve strong performance on complex information-seeking tasks through iterative search and reasoning. However, they often issue intent-misaligned, under-constrained, or redundant search queries, resulting in poor evidence coverage and accumulating retrieval noise. To mitigate these limitations, we propose QREF, a plug-and-play Query Refiner and Evidence Filter. Specifically, the Query Refiner rewrites search queries according to the current reasoning intent while ensuring complementary coverage across each search batch. The Evidence Filter retains evidence relevant to both the current search batch and the reasoning objective, reducing distracting retrieval results. We initialize the Query Refiner with supervised fine-tuning and optimize it through reinforcement learning based on interactions with a real-world web search environment, reducing ineffective queries. Comprehensive experiments demonstrate that our approach improves the performance of DeepSearch agents across four challenging benchmarks, achieving average relative Pass@1 improvements of 33.55% on WebSailor and 11.04% on TongyiDeepResearch without modifying architectures or retraining their reasoning policies. Compared with the original DeepSearch backbone without QREF, the RL-trained refiner reduces the fraction of query batches that lack discriminative retrieval anchors by 95%. Compared with the SFT-trained refiner, it also lowers the filter-based ineffective query ratio.

---


### 157. [On the Robustness of Gossip Protocols in Modern Blockchains](https://arxiv.org/abs/2610.21526)

**<font color=#1a73e8>作者：</font>** Wenting Li, Jannik Albrecht, Frederik Armknecht 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern platforms such as Ethereum and Polkadot nowadays execute Byzantine fault-tolerant consensus protocols over large validator committees, often comprising hundreds of nodes. At this scale, complete graph topologies for connecting nodes are impractical, leading systems to adopt various gossip mechanisms, often in an ad hoc manner.
In this paper, we study the robustness of widely deployed gossip protocols used in committee-based blockchains against realistic network adversaries. We show, both analytically and through extensive empirical measurements, that the graph parameters commonly chosen to instantiate random graphs are insufficient to guarantee that enough honest nodes receive consensus messages for quorum formation in existing protocols. Motivated by this finding, we empirically assess the robustness of Bitcoin's Erdős-Rényi (ER) graphs, Polkadot's grid topology, Ethereum's GossipSub, and Solana's chunk- and tree-based disseminations. Our results reveal surprising tradeoffs: Solana's dynamic trees are bandwidth-efficient in benign settings but fragile under adaptive attacks; Polkadot's grid achieves strong robustness at the cost of high bandwidth overhead; GossipSub is both bandwidth-efficient and resilient to adaptive adversaries, yet highly sensitive to parameter choices; and ER graphs provide a strong robustness-efficiency tradeoff, e.g., when the (average) fanout degree exceeds 15 for networks up to 5000 nodes.

---


### 158. [Activation-Adjacent Layer Normalization: Effects on Approximation Power](https://arxiv.org/abs/2610.21527)

**<font color=#1a73e8>作者：</font>** Yunhao Ni, Yuxin Guo, Jie Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Layer normalization (LN) and root mean square normalization (RMSNorm) depend on their inputs and remain nonlinear at inference. Inserting either next to an activation may therefore change the function a network represents. We study when shallow activation-normalized (AN) and preactivation-normalized (PN) networks can approximate a prescribed width-$N$ one-hidden-layer MLP. Viewing RMSNorm as input-dependent scaling, we use width augmentation to locally linearize normalization on compact feature sets. For AN networks, an unbounded activation range allows width $N+1$, while every continuous nonconstant activation admits width $N+r$ with error $O_f(r^{-1})$. For PN networks, affine parameters or, without them, degree-one positive homogeneity recover width $N+1$; general continuous activations admit width $N+r$ with error tending to zero. The corresponding LN constructions use centered coordinate pairs, yielding widths $N+2$ and $N+2r$, respectively. We prove that $N+1$ for RMSNorm and $N+2$ for LN are also the worst-case bound for approximations, and show that applicable universal-approximation theorems for ordinary MLPs transfer to these normalized architectures. Numerical experiments recover the predicted approximation rates for both normalizations across all five settings and illustrate the shifted-ReLU finite-width obstruction.

---


### 159. [Agent Status Protocol (ASP): A Lightweight Specification for State Reporting in Multi-Agent Systems](https://arxiv.org/abs/2610.21538)

**<font color=#1a73e8>作者：</font>** Diego Gosmar, Deborah A. Dahl, Emmett Coin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Agent Status Protocol (ASP) defines a lightweight way for heterogeneous AI agents to report their operational state to a status server, and for observers such as dashboards to receive that state as soon as it changes. Agents push small JSON events over HTTP POST; the server exposes the aggregated state to observers over Server-Sent Events (SSE). Because an agent that has crashed, hung or been compromised cannot be trusted to report its own failure, ASP does not rely on self-reports alone: the server infers liveness from missed heartbeats, can detect agents that are alive but no longer making progress, and accepts observations from supervisors, guardrails, operators and peers, some of which take precedence over what the agent says about itself while others are shown alongside it. ASP models state along independent dimensions (lifecycle, health, task, floor, governance), so that an agent can be, for example, online, degraded, working on a task and waiting for the floor at the same time. It reuses existing vocabularies: task states from the Agent2Agent (A2A) protocol, floor states from the Open Floor Protocol (OFP), and attribute conventions from the OpenTelemetry GenAI semantic conventions. This paper presents version 0.1 of ASP as a proposal, not as an approved standard. It is a working draft intended to open a discussion, and the authors invite comments, alternative proposals and independent implementations from the community.

---


### 160. [A Systematic and Validated Translation of the Perceived Empathy of Technology Scale to Chinese](https://arxiv.org/abs/2610.21541)

**<font color=#1a73e8>作者：</font>** Matthias Schmidmaier, Jingyao Zheng, Jie Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The Perceived Empathy of Technology Scale (PETS) allows evaluation of empathic behavior in intelligent systems, a concept increasingly applied in human-AI interaction, particularly in emotional and mental health support applications. To support intercultural research and development, PETS is already available in multiple languages, as research suggests cultural and language-based differences in the expression and perception of empathy. Given the substantial Chinese-speaking population and the growing focus on cross-cultural HCI research, we present a validated translation of PETS into Putonghua (Mandarin) with Simplified Chinese. Based on established back-translation methodologies as used in previous PETS translations, our process included multiple independent translations, expert panel reviews, and empirical testing with a total of N=400 participants from an English and a Chinese sample. Through confirmatory factor analysis and invariance testing we show that the Chinese PETS retains the original two-factor structure with high reliability, with support for configural, metric, and scalar invariance. Beyond validation, empathic system behavior was rated equivalently across languages, while non-empathic behavior drew substantially higher ratings from Chinese participants, suggesting its absence is read less consistently across cultures than its presence. This validated Chinese version enables researchers and practitioners to assess empathy perceptions among Chinese-speaking users, supporting culturally appropriate empathic technology development.

---


### 161. [Federated Art Chase: Privacy Leakage and Data Poisoning in Federated Fine-Tuning](https://arxiv.org/abs/2610.21547)

**<font color=#1a73e8>作者：</font>** Vasileios Perifanis, Nikolaos Pavlidis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) is increasingly used to adapt a pretrained, centrally fine-tuned model to data that remain on user devices, beyond training a model from scratch. In this report, prepared for the 4th Federated Machine Learning International Summer School, we study the privacy and integrity of this approach with a reproducible pipeline. An ImageNet-pretrained MobileNetV4-Conv-Small model is fine-tuned centrally on ten Quick, Draw! classes (97.50% test accuracy) and then adapted with head-only FedAvg over ten non-IID clients, which raises client training accuracy from 90.34% to 91.49% while preserving global accuracy. We evaluate four adversarial scenarios. First, from a single one-step client update, an honest-but-curious server recovers the complete private label set, but its reconstructions follow class prototypes rather than the private drawings (mean SSIM 0.130). Second, from a one-round FedAvg aggregate, label-count recovery falls from 87.5% with one client to 75.0% with five and ten clients, below the 80.0% of an uninformed uniform guess. Third, under FedAvg, a backdoor injected by 30%, 50%, and 100% of the clients reaches an attack success rate (ASR) of 21.9%, 31.3%, and 54.7% at a cost of at most 0.8 percentage points of clean accuracy, whereas label flipping is effective only when most of the source-class data are relabeled. Fourth, FLTrust with a root set retained from centralized fine-tuning lowers the backdoor ASR to 1.8% and 4.0% at 30% and 50% malicious clients and the label-flipping ASR from 12.6% to 0.8% without measurable clean-accuracy loss, but provides no protection when every client is malicious. The report closes with a live session in which participants draw, fine-tune, and poison the model through Indigma's FedMaestro orchestrator. Code and executed notebooks, runnable on Google Colab, are at this https URL.

---


### 162. [Finite-Time Guarantees for Constrained Reinforcement Learning under Partial Observability](https://arxiv.org/abs/2610.21548)

**<font color=#1a73e8>作者：</font>** Valentina Zaccaria, Philip Jordan, Tingting Ni 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study reinforcement learning in constrained partially observable Markov decision processes (CPOMDPs), where an agent maximizes reward subject to a cost constraint using only incomplete information about the underlying state. The lack of state observability may require optimal policies to depend on arbitrarily long observation-action histories, making planning and learning challenging. We leverage recent advances in finite-memory approximations of POMDPs and represent finite history windows as states of a constrained MDP. We then develop a primal--dual algorithm that provides the first non-asymptotic guarantees that jointly bound average reward suboptimality and constraint violation in the original CPOMDP. A key challenge is that this finite-window approximation affects both reward values and the set of feasible policies. Under a filter-stability assumption, we derive bounds relating optimality and feasibility in the finite-state model to those in the original CPOMDP, with approximation errors that decay geometrically with the window length. Experiments in partially observable gridworlds demonstrate the effectiveness of our approach.

---


### 163. [Rethinking Classifier-Free Guidance for TI2I Flow Matching](https://arxiv.org/abs/2610.21550)

**<font color=#1a73e8>作者：</font>** Andreas Floros, Elena Koritska, Teofilo de Campos 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study Text-and-Image-to-Image (TI2I) flow matching methods for controllable image editing. In a broader generative modeling context, Classifier-Free Guidance (CFG) is established as a key component responsible for high quality outputs. However, we argue that its role in TI2I modeling is poorly understood. Specifically, we make the surprising observation that the CFG mechanism is implicitly harmful for editing in the noisy phase of flow modeling, hindering instruction following and controllability. We propose a simple correction in the early flow steps, enabling a richer alignment-preservation tradeoff at no extra cost. The effectiveness of our approach is demonstrated on both pixel-space and latent TI2I flows.

---


### 164. [Uncertainty Quantification in Pairwise Difference Learning for Classification](https://arxiv.org/abs/2610.21554)

**<font color=#1a73e8>作者：</font>** Mohamed Karim Belaid, Maximilian Rabus, Eyke Hüllermeier  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Instead of learning a mapping from instances to outcomes in the standard way, the key idea of pairwise difference learning (PDL) is to learn a function that takes two instances as input and predicts the difference between the respective outcomes. Given a function of this kind, predictions for a query instance are derived from every training example and then averaged. We propose a version of PDL for the task of classification and propose a suitable meta-learning technique for this purpose. Moreover, we address the problem of uncertainty quantification, i.e., of representing and quantifying the uncertainty of a PDL classifier's predictions in a faithful manner. Building on recent work on the decomposition of total uncertainty into aleatoric and epistemic components, we propose different ways of extending corresponding measures to the setting of PDL, depending on how and to what extent uncertainty is represented by the underlying base learner. In large-scale empirical studies, we analyze both the predictive accuracy and the uncertainty awareness of our PDL classifier.

---


### 165. [A Quantum Machine Learning Approach to Content-Based Media Recommendation](https://arxiv.org/abs/2610.21562)

**<font color=#1a73e8>作者：</font>** Mina Abbaszadeh, Ouissal Moumou, Anna Pearson 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We use quantum machine learning techniques to develop a content-based media recommender system and evaluate its performance on TV programmes using textual descriptions from one week of BBC iPlayer data. Grounded in the Quantum Natural Language Processing framework (QNLP), programme synopses are mapped to variational quantum circuits using their semantic structure. The parameters of these circuits are trained via a supervised pairwise similarity learning task.
We benchmark the quantum recommender against a classical BiLSTM baseline trained on the same dataset and objective. While both models achieve comparable performance on the similarity learning task, the quantum model requires significantly fewer parameters (47k vs. 17.8M). When the BiLSTM is constrained to a matching parameter budget, its performance degrades substantially (by 3.63 percentage points in Mean Average Precision (MAP)), indicating that the structured quantum representation provides a highly parameter-efficient alternative in this setting. We demonstrate the feasibility of executing the trained models on quantum hardware by deploying the circuits on Quantinuum's System Model H2 (and accompanying emulator) using a SWAP-test-based protocol. The results confirm that the similarity signal is preserved under realistic, noisy conditions. Taken together, these findings highlight the potential of variational quantum circuits for recommendation tasks and represent a practical step toward their real-world deployment.

---


### 166. [Sharp and Stable Label-Free Calibration Certificates from Logical Coherence](https://arxiv.org/abs/2610.21567)

**<font color=#1a73e8>作者：</font>** Takahiro Kato  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Query-conditioned probabilistic predictors answer logically related questions one at a time, and labels to check their calibration are often missing. For each restriction on what a bettor's stakes may use, a minimax theorem identifies, for finitely supported laws of the answers, the sharp label-free lower bound on the corresponding calibration residual. On bundles of different events its mean, marginal and joint stages can separate strictly, and a bundle's bound cannot be attributed to one question without assumptions on the others. The sharp marginal bound is discontinuous in the answers, and no label-free lower bound continuous in the Wasserstein distance stays within a constant factor of it. Lipschitz stakes give a stable bound, sharp for a smooth calibration residual and, for every positive Lipschitz constant, positive exactly when the sharp marginal bound is. On i.i.d. streams, projected online gradient ascent at fixed nodes gives fixed-horizon certificates whose shortfall is bounded by grid, learning and statistical terms, and predictable betting gives anytime-valid ones. In a preregistered study of four predictors on two data sets, all seven confirmatory certificates were positive (the eighth pair did not pass the pilot). A certificate shows only that calibration is at least this bad; zero means "not refuted".

---


### 167. [Decoupled Safety Control: A Safety-Control Algorithm for Training-Free Safety Guidance](https://arxiv.org/abs/2610.21569)

**<font color=#1a73e8>作者：</font>** Huilin Zhou, Ruoxi Cheng, Yuhang Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models achieve strong performance in text-to-image generation, but they can still produce unsafe content. Training-free safety guidance offers a practical inference-time alternative that intervenes during sampling without modifying model weights. However, many existing safeguards still rely on a coupled safety-control chain. In this chain, the same unsafe condition simultaneously specifies what should be avoided, indicates the current unsafe signal, constructs the intervention, and determines when that intervention remains active. This coupling can work when unsafe factors are explicit, but becomes less reliable once harmful and benign semantics are entangled in the current generation state, often leaving residual unsafe content or unnecessarily degrading benign-generation quality or prompt fidelity. We address this problem with Decoupled Safety Control (DSC), a plug-in safety-control algorithm for training-free safety guidance. DSC reformulates training-free safety guidance as an explicit state-dependent control process, so the executed intervention is determined from the current generation state rather than inherited directly from a single unsafe condition. Experiments on standard safety benchmarks show that DSC improves representative latent- and text-space safeguards, achieving stronger unsafe-content suppression while preserving benign-generation quality and maintaining efficient inference.

---


### 168. [Learning to Search for Executable Patternmaking from Certified Programs](https://arxiv.org/abs/2610.21579)

**<font color=#1a73e8>作者：</font>** Zhuotao Xu, Chi Zeng, Liying Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent models generate sewing patterns from images or text, and program-based representations make these patterns executable. These systems produce a finished pattern and do not model how a patternmaker turns one pattern into another. In practice a new style is made by editing an existing pattern: lengthening the bodice, moving a dart, swapping a sleeve. Pattern archives record the results of such edits and none of the steps. We observe that the steps can be recovered by searching over editing actions until one pattern becomes the other. A deterministic compiler makes the recovered steps checkable. To this end, we present SemDraft, the first framework that learns to search for executable patternmaking programs from paired before-and-after sewing patterns without recorded editing steps. Specifically, a bounded search recovers a program of editing actions and certifies it only after three checks: it recompiles from scratch, every pair of its actions is classified as ordered or interchangeable, and an independent replay reaches the same pattern. The certified programs then train a model that ranks candidate actions inside the same search. On two frozen draws of 80 order-sensitive cases, with every other search component fixed, the learned ranker certifies 63 and 64 cases within 1,000 search executions, against at most 53 and 52 for non-learned rankers.

---


### 169. [Transfer Learning in Bandits from Unknown Adaptive Policies: Problem-Dependent Lower and Upper Bounds](https://arxiv.org/abs/2610.21582)

**<font color=#1a73e8>作者：</font>** Adrien Prevost, Timothee Mathieu, Waris Radji 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transfer learning in stochastic multi-armed bandits is typically studied assuming that prior data forms a fixed offline dataset or is generated by a known source. In practice, historical observations come from a previous adaptive decision process whose policy is unknown. We study this setting for bounded rewards in $[0,1]$.
Before the online game starts, the learner receives, for each arm $k$, $N'_k$ observations drawn i.i.d.\ from an unknown distribution $\nu'_k$, collected by an arbitrary and possibly data-dependent strategy, so the sample sizes $N'_k$ may be random. Source and target means satisfy $|\mu_k-\mu'_k|<L_k$ for known constants $(L_k)_k$.
We derive an asymptotic problem-dependent lower bound and propose KL-UCB-Transfer, which combines online and historical data and achieves logarithmic regret with an improved leading constant whenever $\mu'_a<\mu_1-L_a$, and recovers the classical KL-UCB guarantee otherwise. Since bounding the source-target discrepancy is often unrealistic, we relax the assumption to the one-sided condition $\mu_k-\mu'_k<L_k$ and show that logarithmic regret can survive under misspecification, characterizing three regimes ranging from improvement to a degraded logarithmic bound to a loss of guarantee. Simulations illustrate the practical benefits of exploiting process-generated historical data.

---


### 170. [LOADBench: A Large Open Analog Dataset and Benchmark for Machine Learning in IC Design](https://arxiv.org/abs/2610.21591)

**<font color=#1a73e8>作者：</font>** M. Leibl, F. Azevedo, S. Uhlich 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Machine learning (ML) for analog IC design is constrained by limited open data and the absence of standardized evaluation: results reported in different papers are typically obtained on bespoke, often closed, datasets and with ad-hoc metrics, leaving comparisons across methods unreliable. We address both gaps with a large opensource dataset and a suite of standardized benchmarks. The dataset contains more than 100 operational amplifier (opamp) topologies (1-, 2-, and 3-stage) in the SkyWater130 PDK, each shipped with structural and functional annotations, topology-specific sizing constraints (symmetry and sizing rules), an Ngspice testbench, and a multi-objective NSGA-II sizing run producing around 103 Pareto-optimal and 106 intermediate sizing-performance pairs per topology. On top of this data we define six benchmark tasks with precise protocols: inverse sizing, topology selection, sub-circuit classification, structural circuit generation, Pareto-membership prediction, and multi-objective optimization. Thus, the data presented here constitutes the most comprehensive dataset for ML development in over four decades of analog IC design automation. The dataset, ground-truth annotations, and reference implementations of the metric-defining routines are released under an open license, enabling reproducible and directly comparable evaluation across heterogeneous analog design automation methods.

---


### 171. [Learning Intrinsic Dynamics in Latent World Models](https://arxiv.org/abs/2610.21612)

**<font color=#1a73e8>作者：</font>** Jiamin Shi, Yuanhong Zhang, Zhiyang Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning intrinsic dynamics---the relationship between actions and their consequences---is essential for world models. However, visual variations unrelated to the underlying control process can obscure this relationship in learned representations. We investigate the connection between action predictability, defined as the ability to reconstruct an action from consecutive latent states, and the preservation of intrinsic dynamics. Our central hypothesis is that encouraging action predictability discourages representations from discarding the distinctions between different actions and their consequences. We provide two complementary forms of evidence for this connection. Theoretically, we derive a positive lower bound on squared inverse prediction error when the encoder merges distinguishable outcomes of different actions from the same state and appearance, and show that forward prediction can still be exact on those transitions. Empirically, controlled appearance-diversity comparisons, supervision interventions, and latent probes support the role of action prediction in preserving control-relevant transition information. We instantiate action predictability with Concat IDM, which predicts actions from concatenated latent states and updates the shared encoder using action labels already available in offline trajectories, without changing the test-time planner. Across three independent training runs on Push-T with 24 appearances, Concat IDM increases planning success from 9.1% to 77.2%; its paired improvement is 52.9 percentage points larger than that observed with a single appearance. Together, these findings support action predictability as an inductive bias toward intrinsic dynamics and demonstrate the practical benefits of Concat IDM for latent planning under visual diversity.

---


### 172. [A Decision-Aware Evaluation Protocol for Uncertainty in Medical Image Segmentation](https://arxiv.org/abs/2610.21616)

**<font color=#1a73e8>作者：</font>** Saket Maganti, Shreyank N Gowda  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical segmentation uncertainty is often evaluated with calibration error or pixel-level error-detection scores, but these metrics do not show whether uncertainty improves downstream review decisions. We propose a decision-aware evaluation protocol that separates uncertainty estimation from deferral policy and evaluates their combination under fixed review budgets: which pixels, regions, or images should be accepted, and which should be reviewed. The protocol reports fixed-budget error reduction, risk-coverage behaviour, region-level review proxies, structural failure modes, probability-derived baselines, and sensitivity to review assumptions. We instantiate it across retinal vessel, skin lesion, and polyp segmentation with multiple backbones and uncertainty estimators. Under matched inference budgets and canonical multi-layer MC Dropout, test-time augmentation (TTA) gives a stronger error-detection signal across matched MC--TTA comparisons, including architecture and dropout-placement checks. However, estimator rankings are not universal. For example, probability-derived scores remain competitive, deep ensembles can outperform TTA, learned deferral helps mainly when the base estimator is weak, and rankings can change with review unit, uncertainty target, correction assumptions, and cost model. Structural and second-observer analyses further show that boundary and thin-structure failures are partly tied to annotation ambiguity. These findings support evaluating uncertainty as an estimator-policy-review configuration, not as a standalone score map. Code: this https URL

---


### 173. [Local Temporal Contrasts on Human Motion Data Induce a Latent Geometry](https://arxiv.org/abs/2610.21630)

**<font color=#1a73e8>作者：</font>** Lourenço A. Rodrigues, Felix Putze  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series such as recordings of human motion data often encode structure across multiple temporal scales, and when a latent state determining this sequence evolves, this structure needs to survive in the representation space for downstream use. Yet the currently prevalent attention-based encoders paired with sequence-level pooling have made single-vector, pointwise comparison the default mode of inference, discarding the trajectory a sequence traces through the representation space. We propose recovering this geometric structure directly, without relying on forecasting-based objectives, by training an encoder model (SemTAC) with a temporal-neighborhood contrastive loss: representations that satisfy local consistency everywhere must give rise to a coherent global structure, letting inference happen at temporal scales beyond those seen during training. We evaluate SemTAC against four baselines on a five-step motion sequence discrimination task: the same architecture trained with a classification or a standard contrastive objective, and two established self-supervised time-series methods, TS-TCC and TS2Vec. At the full sequence length all five are broadly competitive, but on incomplete, truncated sequences SemTAC holds a large advantage: a median F1 of 0.77 one step before the sequence completes, against 0.27-0.70 for the four baselines. A hyperparameter-matched ablation attributes this effect specifically to the temporal-contrastive objective. SemTAC's representation trajectories are also the only ones among these five to exhibit interpretable geometric structures, exceeding a no-structure chance baseline on a displacement-smoothness metric which we introduce. This is evidence that its objective, not classification accuracy alone, produces genuinely temporally-ordered trajectories.

---


### 174. [Anchor3DGS: Feed-Forward 3D Gaussian Splatting with Compact Anchor-Based Representation](https://arxiv.org/abs/2610.21634)

**<font color=#1a73e8>作者：</font>** Sheng Ye, Jiangke Lin, Fudong Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent feed-forward 3D Gaussian Splatting (3DGS) methods have enabled effective multi-view 3D reconstruction by predicting Gaussian primitives in a single forward pass. However, existing approaches predominantly adopt a pixel-aligned paradigm that predicts one Gaussian per input pixel, coupling the Gaussian count to the input resolution and number of views. This also leads to redundant primitives in textureless regions and insufficient coverage in geometrically complex areas. We present Anchor3DGS, a pose-free feed-forward 3DGS framework that replaces pixel-aligned prediction with a compact anchor-based representation. Guided by information entropy, our method places a set of 3D anchors in the scene, concentrating them in regions of higher visual complexity while maintaining broad spatial coverage. Each anchor performs occlusion-aware aggregation of multi-view image features, exchanges information with other anchors, and is decoded into a set of local Gaussians. A lightweight feature enhancement module further refines the coarse RGB output from Gaussian splatting and improves rendering fidelity. Extensive experiments on diverse benchmark datasets demonstrate that our Anchor3DGS achieves state-of-the-art novel view synthesis quality while only using an order of magnitude fewer Gaussian primitives.

---


### 175. [Spurious Attention Heads in Vision Transformers: Mechanistic Identification of Annotation-Driven Bias in Medical Chest X-Ray Analysis](https://arxiv.org/abs/2610.21638)

**<font color=#1a73e8>作者：</font>** Joshua Muhumuza, Cornelius Kalenzi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers deployed in medical imaging exploit spurious correlations, yet the internal mechanisms remain unidentified and impossible to fix. We apply mechanistic interpretability to locate one such mechanism in ViT-Base 16: a single attention head (L8H10) that functions as a dedicated annotation-reader on chest X-rays, attending to corner text rather than lung pathology in 62% of 200 COVID-19 images. Causal validation via inpainting confirms annotation content rather than luminance or edge density drives the behaviour, increasing lung attention 1.52 times upon removal in affected images ($p{<}0.0001$). The finding replicates across NIH ChestX-ray14 (79%), DeiT-Base (88%), and ViT-Large 16 (80%), establishing spurious annotation-attending heads as a consistent property of ViT-family architectures across two datasets and three architectures. Full fine-tuning does not suppress the behaviour and may entrench it: 98.4% of spurious images remain spurious and the spurious rate rises marginally, as the shortcut is reinforced rather than removed. Critically, single-head ablation produces $p{=}0.340$ and multi-head ablation of all three identified carriers produces $p{=}0.532$, meaning a causally verified annotation-reading circuit is completely invisible to output-level evaluation. Mechanistic auditing finds what behavioural testing cannot.

---


### 176. [DIAL: Dynamic and Informed Adjustment of the Native Stochastic Law for Reliable Weather Ensembles](https://arxiv.org/abs/2610.21639)

**<font color=#1a73e8>作者：</font>** Yucheng Wang, Haonan Guo, Tianhao Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ensemble weather forecasts can look reliable in global averages while hiding too little spread in some cases and too much in others. These errors vary across variables, spatial scales, lead times, and weather states. Adapting randomness during forecasting can correct these errors, but training fixes stochastic behavior beforehand and output calibration acts afterward. Inference guidance also acts during forecasting, but typically scores ensemble members separately rather than the ensemble as a whole. Reliability feedback arrives at the end, and tracing it backward through many chaotic forecast steps is expensive and unstable. We therefore introduce Dynamic and Informed Adjustment of the Native Stochastic Law (DIAL), which controls a frozen model's native stochasticity. DIAL learns from past forecasts to predict whether each variable and scale needs more or less spread. As a forecast develops, it estimates how possible noise changes will affect later forecast accuracy and reliability. It combines these predictions to make small noise updates at each step. This loop avoids retraining the weather model and full backpropagation through the forecast. We evaluate DIAL on FourCastNet 3 (FCN3) using later ERA5 years unseen during training. DIAL provides better scale-resolved reliability than learned postprocessing and reward-based control baselines. Relative to the unmodified Native FCN3 reference, DIAL achieves an 8.27% improvement in the primary multiscale continuous ranked probability score (CRPS).

---


### 177. [SCMerge: Spatial-Consistency-Aware Token Pair Merging for Efficient Semantic Segmentation](https://arxiv.org/abs/2610.21642)

**<font color=#1a73e8>作者：</font>** Junfeng Ren, Yi Gong, Yuan Zeng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformer architectures have showcased impressive performance on semantic segmentation, yet their quadratic attention complexity hinders practical applications. Recent works have focused on merging tokens to reduce sequence length and thus improve transformer efficiency. However, existing token merging methods primarily rely on feature similarity to identify similar tokens, overlooking spatial consistency, which may introduce segmentation errors in semantic segmentation. In this work, we propose SCMerge, a training-free token merging method that jointly considers feature similarity and spatial consistency in pairing similar tokens. The pairwise tokens are then merged within the encoder, and the resulting token sequences are reconstructed onto the original patch grid after decoding. The proposed method is flexible and can be plugged into existing vision Transformer-based semantic segmentation pipelines. Extensive experiments on the benchmark datasets ADE20K, Pascal Context, and Cityscapes show that SCMerge consistently achieves a better trade-off between segmentation accuracy and efficiency than baseline methods.

---


### 178. [Efficient Pairwise Difference Learning: A Comparative Study of Encoding Strategies and Training Pair Selection](https://arxiv.org/abs/2610.21644)

**<font color=#1a73e8>作者：</font>** Bernard Georges, Mohamed Karim Belaid, Manuel Rodrigues  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pairwise Difference Learning for Classification (PDC) enhances supervised learning in low-data regimes by training a binary similarity classifier on pairs of instances rather than individual samples, effectively inflating the training set from $n$ to $O(n^2)$ examples. However, the PDC framework leaves critical implementation choices underspecified, particularly regarding input representation and pair selection strategies. This work systematically investigates these design decisions through extensive empirical evaluation. We compare four feature encoders (paired features, triplet with relative difference, absolute difference, and a novel triplet with absolute difference) alongside four pair selection strategies ranging from exhaustive to kernel-thinning-based schemes. Experiments across nearly 200 benchmark classification datasets using Decision Tree, Multilayer Perceptron, Gaussian Naive Bayes, and Support Vector Classifier as base models reveal that the proposed triplet with absolute difference encoder ($\phi_{\mathrm{3dabs}}$) achieves the highest average F1 scores. More notably, restricting training to upper-triangle pairs reduces computational time by approximately 40% with negligible accuracy loss. Kernel thinning-based selection provided no accuracy benefits while substantially increasing computational overhead. Overall, PDC configurations outperformed base models in 94% of tested cases, though no single configuration dominated universally, suggesting dataset-specific optimization remains an open challenge.

---


### 179. [Digital Typhoon Dataset V3: Benchmarking for Multi-spectral Extension and Analyzing Systematic Bias in Intensity Regression](https://arxiv.org/abs/2610.21654)

**<font color=#1a73e8>作者：</font>** Asanobu Kitamoto, Victor Le Louarn, Noelia Falczuk 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents the Digital Typhoon Dataset V3, a new version of the longest typhoon satellite image dataset spanning nearly 50 years, designed to benchmark machine learning models on long-term spatio-temporal data. The latest addition to Dataset V3 is multispectral satellite data, enabling multi-channel models. We investigate data-splitting strategies and present benchmarking results for the Northern and Southern Hemispheres. Experimental results show that, under the current dataset construction and experimental setting, multi-channel inputs do not clearly outperform single-channel inputs for pressure regression. Among the evaluated model architectures, image types, and spectral channels, ResNet-18, full-resolution images, and Channel 1 generally provide the best single-channel performance for pressure regression. Performance also differs between the WP and AU datasets by regression target, with lower RMSE on WP for pressure regression and on AU for wind regression. These results highlight the importance of considering dataset-specific and task-specific characteristics when interpreting benchmark performance. Additionally, we analyzed systematic bias in intensity regression, which leads to underestimation of intensity for strong typhoons. We tested imbalance-aware weighting strategies, including inverse-density weighting inspired by BalancedMSE, and showed that these approaches are not sufficient to remove the bias. The dataset is publicly available at this http URL and this https URL.

---


### 180. [Approaching Backpropagation Accuracy with Weight Perturbation on MNIST](https://arxiv.org/abs/2610.21665)

**<font color=#1a73e8>作者：</font>** Patrick Inoue  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weight perturbation (WP) estimates learning directions from random parameter perturbations and a scalar change in loss, without backpropagating derivatives. We examine how batch size, training duration, and estimator stabilization affect its attainable accuracy in fully connected MNIST networks. In the shallow configuration, large-batch training reaches approximately 97\% test accuracy, compared with an early backpropagation (BP) reference near 97.5--98\%. The same comparison exposes a substantial efficiency gap: under a ten-epoch budget, shallow WP reaches 90.2\%, whereas the reported BP reference reaches 97.4\%. Epoch-indexed curves show diminishing returns from increasing batch size beyond 4,000. Learning-rate reduction and averaging independent perturbation-based updates also stabilize deeper networks, although their recorded results do not establish BP-level accuracy. We distinguish these empirical findings from a finite-horizon approximation argument: under stated regularity conditions, population WP can approximate a fixed gradient-descent trajectory arbitrarily closely at any fixed finite depth. Positive classification margins then suffice to preserve the reference predictions on a finite test set with arbitrarily high probability. Together, the results identify near-BP accuracy as a configuration- and budget-dependent possibility, rather than evidence of equal efficiency or an unconditional accuracy guarantee across depth.

---


### 181. [Edit4D: Editable 4D Scene Generation with Textual Control](https://arxiv.org/abs/2610.21668)

**<font color=#1a73e8>作者：</font>** Chanwoo Kim, Tackgeun You, Hwasup Lim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Edit4D, an editable text-to-4D scene generation framework that constructs 4D scenes from separate background and dynamic character representations. Recent advances in generative models have enabled text-driven dynamic scene synthesis, but editable 4D scene generation remains challenging due to the need to preserve spatial geometry and temporal dynamics. Existing approaches typically generate holistic scene videos, where the background and dynamic characters are coupled, making object-level editing and flexible camera control difficult. Edit4D addresses these limitations through a stage-specific generation pipeline. Given a user instruction, Edit4D first decomposes it into stage-specific prompts for background, dynamic character, and scene-character composition. Using these prompts, we synthesize multi-view scene images with text-to-image and camera-conditioned generative priors and reconstruct a background 3D Gaussian splatting representation. We then generate a character image, animate it with an image-conditioned video prior, reconstruct a 4D mesh, and bind Gaussian primitives to obtain a character representation. Finally, both components are composed through text-guided segmentation and contact-aware optimization. A global scene refinement is then performed to improve harmonization and rendering consistency. By integrating stage-specific components, Edit4D enables controllable camera motion, flexible object-level editing, and the practical construction of editable 4D scenes. Project page: this https URL

---


### 182. [Classical methods for modern applications: synthetic tabular data generation using lightweight discrete response continuous latent variable model](https://arxiv.org/abs/2610.21674)

**<font color=#1a73e8>作者：</font>** Bartosz Barzdajn, Mateusz Krzysztoń  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we present a lightweight algorithm for modelling tabular data containing both continuous and discrete variables. The method uses empirical marginal distributions and a selected quantile function to transform the data into a continuous latent space, where a distribution of choice, e.g. a multivariate Gaussian, can be efficiently estimated and applied. While this approach is closely related to classical well-established machine learning methods, we present a novel adaptation that fits well within the contemporary computational ecosystem. Unlike in the case of deep architectures, it results in a simple implementation with few dependencies, robust training/estimation, as well as efficient sampling. The transformation preserves complex marginal distributions and correlations, providing high-fidelity models, especially for data with unimodal distributions. One of the key characteristics of the proposed approach is its continuous representation of discrete variables. While highly desirable, this introduces a significant challenge, since a single observation corresponds to a region rather than a point in the latent space. We show that this ambiguity naturally leads to a Monte Carlo expectation-maximisation (MCEM) formulation, whose auxiliary objective can be expressed as a weighted latent-space likelihood. This, in turn, allows conventional maximum-likelihood estimators to be used within an efficient and robust optimisation procedure.

---


### 183. [ShiftQAT: Quantization-Aware Training for the Numerical Contract of a Fixed-Function Edge CNN Accelerator](https://arxiv.org/abs/2610.21695)

**<font color=#1a73e8>作者：</font>** Oguzhan Buyuksolak, Osman Erman Okman, Mehmet Gorkem Ulkar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fixed-function CNN accelerators make edge inference fast and energy-efficient, but they execute only networks that obey a precise numerical contract. On the MAX7800x family, this contract requires power-of-two, per-tensor, symmetric scales, 8-bit activations and biases, integer-only arithmetic, and one statically configured shift per layer. We present ShiftQAT, the quantization-aware training (QAT) flow we developed for this family, which produces networks satisfying the contract by construction. It is the default training path of ai8x-training, the family's open-source training toolchain. ShiftQAT resolves residual, concatenation, and weight-sharing dependencies so that activation scales propagate statically and each layer's requantization reduces to one offline-configured shift. It also trains weights and biases on a joint power-of-two grid that fits the 8-bit bias budget. Among the compared methods, only ShiftQAT satisfies all of the contract's scaling constraints, including signed 8-bit activation storage. Even so, on ImageNet it matches the W8A8 accuracy drop of less constrained QAT methods and stays within 2.9 percentage points of FP32 at W4A8. On MAX78002 silicon, ShiftQAT-trained MobileNetV2 and ResNet-18 classify ImageNet images in 14.6 and 8.4 ms at 5.1 and 2.8 mJ per inference.

---


### 184. [Bridging the Markerless Tracking Validation Gap: Intraoperative X-ray Workflow Integration](https://arxiv.org/abs/2610.21696)

**<font color=#1a73e8>作者：</font>** Connor Daly, Salvatore Russo, Jinendra Ekanayake 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Markerless intraoperative tracking of spinal anatomy via RGB-D sensors is a promising alternative to invasive bone-anchored fiducials, yet no existing clinical dataset provides independent subsurface ground truth for validating these methods. We address this gap with a clinically viable pipeline that derives per-vertebra 6-DoF pose from routine intraoperative C-arm fluoroscopy, co-registered to the RGB-D camera frame through a multimodal fiducial array detectable in both imaging modalities. Critically, the pipeline requires no additional radiation, instrumentation, or deviation from standard surgical workflows, relying solely on the fluoroscopic images already acquired during routine level checks. A calibrated transform chain links the vertebral pose recovered via multi-view 2D-3D CT-to-fluoroscopy registration to the RGB-D coordinate frame, enabling direct comparison of any markerless registration estimate against a subsurface reference. Ex vivo validation against optically tracked ovine vertebrae confirms end-to-end accuracy of 2.06 +- 0.29 mm and 3.35 +- 0.93 degrees, sufficient to serve as independent ground truth for methods with substantially larger errors. We demonstrate the pipeline's utility by evaluating two markerless registration strategies on clinical data spanning 11 vertebrae across 1,500 frames from three surgical sequences: the first such evaluation against an independent subsurface reference in a clinical setting. The proposed framework provides reusable infrastructure for benchmarking emerging markerless tracking methods on real surgical data.

---


### 185. [Mixture of Multi-Sequence Feature Difference for Contrast-Enhanced MRI Synthesis](https://arxiv.org/abs/2610.21703)

**<font color=#1a73e8>作者：</font>** Jonghun Kim, Junmo Kwon, Hyunjin Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contrast-enhanced magnetic resonance imaging (CE-MRI) is crucial for accurately diagnosing and segmenting brain tumors. However, the acquisition of CE-MRI requires injecting contrast agents, which poses potential health risks and increases scan costs. Here, we propose a CE-MRI synthesis method from non-contrast sequences, reducing both risk and cost. Unlike existing methods that rely on channel-wise concatenation to fuse multi-sequence information for synthesis, we introduce a Mixture of Feature Difference (MoFD) module. The proposed module uses a dynamic weighting strategy to adaptively select and aggregate informative features from both individual source sequences and explicit differences among them. Quantitative and qualitative evaluations demonstrate that our proposed method outperforms baselines in terms of image fidelity and perceptual quality on the UCSF-PDGM and UPenn-GBM datasets. Our method successfully reconstructs tumor regions and achieves segmentation performance comparable to that obtained with real CE-MRI. Our ablation studies show that although adversarial learning improves perceptual quality, a regression-based variant of our method achieves higher structural fidelity.

---


### 186. [International Multi-Centre Validation of Unsupervised Domain Adaptation for Precise Discrimination between Normal and Abnormal Retinal Development](https://arxiv.org/abs/2610.21719)

**<font color=#1a73e8>作者：</font>** Zhanhan Tu, Nikhil Reddy, Helen J. Kuht 等 30 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Arrested retinal development can cause childhood visual impairment, but grading optical coherence tomography scans is difficult to standardise across devices and centres. We developed and evaluated an unsupervised domain adaptation model to classify normal and abnormal retinal development across different OCT systems. This retrospective multicentre study used OCT scans from five centres in four countries and the UK Biobank. Data covered four OCT devices, including table mounted and handheld systems. A ResNet50 based Domain Adversarial Neural Network was trained using labelled images from a source device and unlabelled images from a target device. We evaluated six source to target pairings and compared model performance with seven clinician graders. A separate Heidelberg Spectralis dataset was reserved for external evaluation. Across validation sets, accuracy ranged from 87.75% to 96.06%, sensitivity from 88.68% to 98.38%, and specificity from 78.00% to 98.02%. The best performing model, adapted from TM OCT1 to HH OCT1, achieved 96.06% accuracy and an area under the receiver operating characteristic curve of 0.994, with a 95% confidence interval from 0.981 to 0.999. Several models also maintained discrimination on the unseen Heidelberg device. Unsupervised domain adaptation enabled OCT classification across devices without labelled target device data. The approach may support more consistent assessment of retinal development and large scale analysis of existing imaging datasets.

---


### 187. [In-Context Preference-Conditioned Pareto Set Learning from Limited Offline Data](https://arxiv.org/abs/2610.21736)

**<font color=#1a73e8>作者：</font>** Yiming Yao, Liang Zhao, Qingfu Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-objective optimization involves diverse preferences over conflicting objectives. Rather than returning a finite set of trade-off solutions, preference-conditioned Pareto set learning seeks to map a specified preference directly to a corresponding Pareto optimal solution. Yet in many real-world scenarios, optimization must proceed offline without further objective evaluations, leaving only a limited static dataset that sparsely covers the decision and objective spaces. Existing methods either optimize separately for each preference or train a problem-specific Pareto solution model, requiring repeated search across preferences or repeated training across problems. We introduce in-context preference-conditioned Pareto set learning (ICPSL), a framework that amortizes both preference-wise solution search and problem-specific model construction. ICPSL pretrains a foundation-style hypernetwork on a large and diverse set of synthetic prior data. Given the offline observations of an unseen problem, the pretrained hypernetwork learns to generate a problem-specific, preference-conditioned Pareto solution model in a single forward pass. The generated model can then be reused to predict solutions for arbitrary preferences without problem-specific training or preference-wise search. Experiments on synthetic and real-world problems show that ICPSL produces high-quality Pareto solutions while providing substantial speedups in problem-specific solution-model construction.

---


### 188. [SceneWeave: Audience-Guided Scene Exploration for Dramatic Adaptation](https://arxiv.org/abs/2610.21737)

**<font color=#1a73e8>作者：</font>** Aolin Li, Xiao Xu, Haihua Xie  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Adapting prose into a script requires transforming narration and inner experience into scenes that convey relationships and psychological contradictions. Planning specifies intended effects but leaves their realization in dialogue and action unresolved. Drawing on screenwriters' accounts of revising scenes and their connections to the surrounding work, we present SceneWeave, which uses alternative scene drafts to revise the adaptation as a whole. It writes contrasting treatments of a focal scene, compares the interactions they create, and revises characterization, preceding preparation, subsequent development, and scene order before generating the complete script. The central contribution is to use actual scene writing to inform adaptation decisions and propagate their consequences across the work. We also develop a task-specific writing model and a human-preference model for comparing script drafts. The writing model learns from adaptation examples and human preferences; the preference model combines human and synthetic supervision. Blind reader comparisons favor SceneWeave over a baseline workflow and description-based controls, while content assessment indicates reduced narrative redundancy and strong psychological treatment.

---


### 189. [Reliable Knowledge Acquisition for Continual Learning Agents](https://arxiv.org/abs/2610.21739)

**<font color=#1a73e8>作者：</font>** Yixu Huang, Jiaqi W. Ma  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As agents powered by foundation models move into open-ended environments, continual learning from experience becomes essential. For agents built on models with fixed parameters, this learning requires reusing prior task experience in context to improve performance and efficiency on future tasks. Existing memory and experience-learning systems typically focus on either retained facts or procedures, and lack a mechanism for establishing the reliability of claims extracted from the ongoing task stream. Indeed, we find that approximately 12--33\% of entries produced by representative systems harm future task performance when reused. To address these limitations, we propose \textbf{RIKA} (Reliable Knowledge Acquisition), which combines hierarchical extraction of factual, conceptual, procedural, and metacognitive knowledge with Evidence-based Knowledge Admission, which uses source evidence and subsequent experience to govern which claims enter the task agent's context, without additional validation tasks. Across six task streams from Continual Learning Bench and four model backbones, RIKA achieves the highest aggregate score on every backbone.

---


### 190. [Sparse Federated Echo State Networks for Time-Series Classification via Smooth-L1 Regularization](https://arxiv.org/abs/2610.21742)

**<font color=#1a73e8>作者：</font>** Gengcheng Lyu, Manuel Röder, Frank-Michael Schleif  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Echo State Networks (ESNs), as lightweight implementations of reservoir computing, provide efficient solutions for temporal data processing in resource-constrained environments. While standard ESNs offer computational efficiency, their dense readout layers inflate the stored model and the per-sample inference cost. This paper introduces a Smooth-L1 regularized ESN (SL1ESN) that promotes sparsity in the readout layer while preserving differentiability for gradient-based optimization. The method employs a twice-differentiable Smooth-L1 approximation compatible with Newton's method, which we exploit both for centralized training and for a second-order (Newton-step) federated aggregation scheme. Under a single fixed shrinkage threshold shared by every dataset and both settings, experiments on seven time-series classification benchmarks show that SL1ESN learns readouts that are $77$--$95\%$ sparse in the centralized setting and $75$--$95\%$ sparse in the federated one, while staying within $0.7$ accuracy points of the strongest dense baseline on five of the seven benchmarks in the centralized setting and within $1.6$ points on the same five in the federated one, and the second-order federated update converges in only a few rounds. The resulting sparsity compresses the stored model, the per-sample inference cost, and the server-to-client broadcast by a comparable factor. These results demonstrate the practical value of sparse readouts for edge computing and IoT deployments.

---


### 191. [The Dormant Spiking Neuron: A State-Driven Mechanism for Efficient Spiking Neural Networks](https://arxiv.org/abs/2610.21748)

**<font color=#1a73e8>作者：</font>** Ruichen Ma, Yicai Chen, Pujun Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spiking neural networks (SNNs) offer a compelling pathway toward energy-efficient artificial intelligence, fundamentally anchored in presynaptic input-driven sparsity. However, a substantial yet chronically overlooked source of computational overhead persists: the continuous subthreshold dynamics of postsynaptic neurons. Quantitative analysis reveals that up to 44% of neurons in an ImageNet-trained ResNet-18 model reside in a deeply inhibited state, imposing a persistent computational burden despite having a negligible probability of firing. To address this inefficiency, the Dormant Spiking Neuron (DSN) model is introduced. By incorporating a state-driven dynamic gate, the DSN allows a neuron to enter a dormant state when its membrane potential falls below a predefined negative threshold, dynamically pruning redundant computations at the instance level. Crucially, this dormancy mechanism is directly integrated into the neuronal dynamics and trained end-to-end via backpropagation through time using surrogate gradients, enabling the network to actively learn a robust dormancy policy that adaptively preserves critical information flow. Extensive experiments across static and neuromorphic datasets demonstrate that the DSN framework consistently reduces computational energy by 40% to over 70%. Notably, on the large-scale ImageNet dataset, the DSN outperforms state-of-the-art static pruning techniques at comparable reported cost reductions and simultaneously improves the corresponding baseline SNN accuracy by 1.34%. By establishing a trainable, state-driven sparsity paradigm orthogonal to conventional input-driven methods, the DSN unlocks synergistic efficiency gains, presenting an effective approach for advancing neuromorphic computing.

---


### 192. [Harmful Partial Interventions and Benign Leakage in Concept-based Models](https://arxiv.org/abs/2610.21750)

**<font color=#1a73e8>作者：</font>** Gregory Verghese, Christopher J. Soelistyo, Mateo Espinosa Zarlenga 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence systems deployed in high-risk settings increasingly require models that support meaningful human oversight. Concept-based models (CMs) offer a promising framework by enabling users to inspect and intervene on intermediate, human-understandable concepts. However, concept interventions can counterintuitively worsen downstream predictions, a failure mode we formalise as intervention harm. We distinguish harm after all concepts have been intervened on from harm under partial interventions, the more likely practical use case. Modern CMs often achieve high accuracy by encoding, or leaking, additional task-relevant information in their intermediate concept representations. Recent work argues that such leakage can be benign with respect to intervention harm when concept representations satisfy two conditions: sufficiency and localisation. We prove that these criteria are not sufficient to guarantee that concept interventions improve downstream performance. Across controlled and real-world settings, we find that concept supervision incompleteness is associated with increased intervention harm. Importantly, optimising the model when all concepts are intervened on, a previously proposed leakage mitigation objective, reduces endpoint harm but does not reliably prevent harmful partial corrections. Hence, we introduce a complementary monotonic intervention objective that directly penalises increases in task loss along partial intervention trajectories. Combining endpoint and monotonic intervention training substantially reduces the prevalence and magnitude of partial intervention harm while preserving concept and task predictive performance.

---


### 193. [Beyond Source Prompts: Towards Visually Grounded AI-Generated Video Quality Assessment](https://arxiv.org/abs/2610.21758)

**<font color=#1a73e8>作者：</font>** Kehao Zhou, Yixuan Li, Yuxuan Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in generative artificial intelligence have accelerated video generation technologies. However, AI-generated videos (AIGVs) remain susceptible to various distortions, highlighting the need for dedicated video quality assessment methods. Content semantics play an important role in AIGV quality assessment, with source prompts typically used as textual references. However, these prompts may not accurately reflect the generated video content, resulting in a discrepancy between the intended textual description and the generated result. To address this limitation, this paper proposes VGCap, an AIGV quality assessment framework guided by visually grounded captions that align better with generated content. Specifically, we introduce two forms of captions: a global caption obtained by minimally revising the source prompt based on multi-frame visual evidence, and prompt-independent segment captions that describe localized temporal content. Together, these captions provide complementary textual evidence for assessing spatial quality, temporal quality, and text-video alignment. Experimental results on the LGVQ and FETV datasets show that VGCap outperforms representative baselines across all three dimensions. Further ablation studies on caption sources and temporal components confirm the effectiveness of visually grounded captions for each quality dimension, while highlighting the benefits of segment-level features for temporal quality prediction. The source of VGCap will be available at this https URL.

---


### 194. [Q($γ_H$): Entropy-Guided Horizon Mixing in Multi-Discount Q-Learning](https://arxiv.org/abs/2610.21764)

**<font color=#1a73e8>作者：</font>** Arwa Albelaihi, Abdulrahman Altahhan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A fixed discount factor in Q-learning imposes a single planning horizon throughout training, despite the differing demands of early exploration and long-term credit assignment. We propose Q($\gamma_H$), a multi-horizon Q-learning framework that maintains multiple discount-specific heads and adaptively combines them at control time using an entropy-derived confidence signal. The resulting state-dependent mixing weights shift control from shorter- to longer-horizon heads as policy confidence increases, enabling adaptive horizon mixing without modifying individual Bellman updates. Across classical control and deep reinforcement-learning benchmarks, Q($\gamma_H$) shows its strongest improvements on delayed-credit tasks relative to strong fixed-discount baselines. By decoupling horizon adaptation from the underlying learning updates, Q($\gamma_H$) provides a lightweight framework for adaptive planning-horizon control in reinforcement learning, avoiding the need for manual discount-factor selection while remaining compatible with standard value-learning methods.

---


### 195. [FuseAdapt: Parameter-Efficient Multimodal Fusion for Semantic Segmentation with Missing Modalities](https://arxiv.org/abs/2610.21779)

**<font color=#1a73e8>作者：</font>** Xin Zhang, Robby T. Tan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal semantic segmentation benefits from complementary sensors, but this benefit is fragile when some modalities are degraded or missing at test time. Many existing methods rely on dedicated fusion modules or multi-branch cross-modal encoders, and the fusion often becomes unreliable when modalities are absent, leading to substantial performance drops. We propose \textbf{FuseAdapt}, a parameter-efficient framework that performs fusion within the adaptation space of a frozen vision foundation model (VFM), exploring whether VFM priors can serve as an effective shared backbone for multi-modal segmentation. Instead of attaching a standalone fusion network, FuseAdapt assigns each modality a lightweight adaptation branch and performs \emph{adaptation-space fusion} by keeping Q/V low-rank adaptation private to each modality and routing only FFN low-rank residual activations across modalities inside the frozen backbone. The pretrained VFM remains fixed while modality-specific corrections and explicit cross-modal interaction are learned through the adaptation paths. To handle missing modalities, we further introduce \textbf{Predictive Modality Modeling (PMM)}, a direct representation-level objective for cross-modal redundancy. During training, PMM masks a target modality and predicts its embedding from the visible ones, supervised by a teacher target computed under full-modality input. PMM is used only during training and adds no inference-time overhead. Across three multi-modal segmentation benchmarks (MCubeS, DELIVER, MUSES), FuseAdapt consistently improves both modality-complete and modality-incomplete segmentation with a small trainable budget, yielding up to +3.01 mIoU under full modalities and +12.56 mIoU under missing modalities over prior state-of-the-art. Project page: this https URL.

---


### 196. [DINO-FIL: Multi-Layer Transformer Fusion for Generative Inpainting Forgery Localization](https://arxiv.org/abs/2610.21780)

**<font color=#1a73e8>作者：</font>** Simon Freitter, David Fischinger, Silvia Poletti 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose DINO-FIL, a transformer-based framework for pixel-level localization of generative image forgeries. The method leverages multi-layer representations from a pretrained DINOv3 ViT-H+/16 encoder combined with a lightweight fusion decoder to capture both semantic structure and fine-grained texture inconsistencies introduced by image editing. By aggregating intermediate transformer features across depths, the model improves sensitivity to subtle, spatially localized artifacts that are often missed by standard single-layer approaches. We evaluate DINO-FIL in a cross-dataset setting, training on B-Free and testing on Beyond the Brush, CocoGlide, TGIF, and SAGI-D. The model achieves strong generalization, outperforming existing baselines on average and on four of five evaluated datasets, while maintaining a high true negative rate on pristine images.

---


### 197. [NICE Toolbox: Nonverbal Interpersonal Communication Exploration Toolbox](https://arxiv.org/abs/2610.21786)

**<font color=#1a73e8>作者：</font>** Aleksandr Evgrashin, Carolin Schmitt, Timo Lübbing 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding human communication is a long-standing goal in psychological research. People express themselves through many verbal and nonverbal channels: posture, gesture, gaze, facial expression, and speech. Measurement and annotation of these signals has traditionally required time-consuming manual work by trained human labellers. The Nonverbal Interpersonal Communication Exploration (NICE) Toolbox is a free, open-source Python framework that automatically measures these signals by combining existing state-of-the-art computer vision and speech-processing methods into a single software package. It includes support for multi-camera systems, interchangeable detection algorithms, 2D and 3D visualization of detector outputs, evaluation on the user's custom data, and export to third-party software. With the release of this tool, we aim to make data exploration of interpersonal communication signals scalable, reproducible, and accessible for psychological research.

---


### 198. [Single-stage joint diffusion of sky images and clear-sky index for ultra-short-term irradiance forecasting: what the frame-to-irradiance stage discards](https://arxiv.org/abs/2610.21795)

**<font color=#1a73e8>作者：</font>** Kanawut Suwandee, Suwichaya Suwanwimolkul  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sky-image irradiance forecasting is dominated by a two-stage design: a video-prediction model forecasts future sky frames, and a separately trained regressor maps those frames to irradiance. We propose a single-stage alternative that co-denoises the future sky-image and clear-sky-index sequences in one diffusion process, with an irradiance head that reads a denoised preview of the future sky rather than the noised diffusion state. The forecaster needs no regression stage and runs from sky images and deterministic covariates alone, with no measured irradiance at its input --- the situation at a site with a camera but no pyranometer. On 2023 SIRTA data the model reaches a pooled RMSE of $104.1$~W\,m$^{-2}$ and a skill score of $+0.34$ on the continuous ranked probability score (CRPS) against smart persistence, higher than any of twelve baseline configurations, and retains that skill when retrained on 2021--2022. On the model's own generated frames, a separately trained regressor reaches $150.6$~W\,m$^{-2}$ against the joint head's $104.1$: roughly $46$~W\,m$^{-2}$ that joint training recovers and a cascade discards. Point accuracy is competitive but not best: a deterministic network that also reads measured irradiance attains $97.6$~W\,m$^{-2}$. The model's CRPS skill leads that network's in every sky-condition tertile, by $0.26$ to $0.30$.

---


### 199. [Teaching DINOv3 About Partial 3D Geometry: A Self-Supervised Geometry-Aware Approach](https://arxiv.org/abs/2610.21802)

**<font color=#1a73e8>作者：</font>** Viktoria Ehm, Dongliang Cao, Riccardo Marin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Partial shape matching is a crucial yet underexplored problem in 3D vision, with significant relevance to real-world scenarios where shapes are often only partially observed. Existing feature descriptors face difficulties in this setting, as traditional representations either struggle with the boundaries of partial shapes or heavily depend on the shape's spatial position. While existing approaches have employed DINO features for partial shape matching, these features are not inherently suited for handling partial observations. In this work, we propose a method to refine DINO features using LoRA-based self-supervised learning, enabling the generation of feature descriptors that are robust to partiality. Our features substantially improve performance on partial shape matching compared to traditional or vision foundation features. Additionally, when integrated into existing partial shape matching pipelines, we achieve state-of-the-art results on partial shape matching and left-right prediction benchmarks.

---


### 200. [Co2In: a Bi-level Memory Incremental Learning Framework with Knowledge Encoding, Consolidation, and Integration](https://arxiv.org/abs/2610.21804)

**<font color=#1a73e8>作者：</font>** Wenju Sun, Qingyong Li, Boyang Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Incremental learning (IL) aims to continually acquire new knowledge (plasticity) while retaining previously learned information (stability). However, striking a balance between plasticity and stability remains a significant challenge for intelligent systems. The human brain achieves exceptional balance, owing to various memory units that collaboratively encode and store information. Inspired by human memory mechanisms, this paper introduces an IL framework with knowledge enCoding, Consolidation, and Integration (Co2In). Co2In is designed as a bi-level memory architecture: a working memory for adaptive knowledge acquisition and a long-term memory dedicated to the persistent retention of information. The two memory modules work cooperatively during IL. The working memory first learns from new data to encode knowledge into parameters. Subsequently, Co2In performs a consolidation process to identify underlying patterns in the learned parameters and re-express them into a compact knowledge representation. Next, the knowledge representation and the identified patterns are transformed into separate network layers and integrated into the long-term memory. These designs empower Co2In to accumulate knowledge with high plasticity and stability. We evaluate Co2In on CIFAR-10, CIFAR-100, and Tiny-ImageNet under exemplar-free Class-IL and Task-IL settings. Experimental results show that Co2In achieves state-of-the-art performance with efficient memory consumption.

---


> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-278](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
