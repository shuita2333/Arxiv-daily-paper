# 📦 其他研究 | 2026年05月18日

> 本类共 **337** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-337](./part-07.md)

---

### 101. [Dynamic Latent Routing](https://arxiv.org/abs/2605.14323)

**<font color=#1a73e8>作者：</font>** Fangyuan Yu, Xin Su, Amir Abdullah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate the temporal concatenation of sub-policies in Markov Decision Processes (MDP) with time-varying reward functions. We introduce General Dijkstra Search (GDS), and prove that globally optimal goal-reaching policies can be recovered through temporal composition of intermediate optimal sub-policies. Motivated by the "search, select, update" principle underlying GDS, we propose Dynamic Latent Routing (DLR), a language-model post-training method that jointly learns discrete latent codes, routing policies, and model parameters through dynamic search in a single training stage. In low-data fine-tuning settings, DLR matches or outperforms supervised fine-tuning across four datasets and six models, achieving a mean gain of +6.6 percentage points, while prior discrete-latent baselines consistently underperform SFT. Mechanistic analyses and targeted code ablations show that DLR learns structured routing behaviors with distinct causal roles.

---


### 102. [D2-CDIG: Controlled Diffusion Remote Sensing Image Generation with Dual Priors of DEM and Cloud-Fog](https://arxiv.org/abs/2605.14326)

**<font color=#1a73e8>作者：</font>** Zuopeng Zhao, Ying Liu, Kanyaphakphachsorn Pharksuwan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing image generation provides a reliable data foundation for remote sensing large models and downstream tasks. However, existing controllable remote sensing image generation methods typically rely on traditional techniques such as segmentation and edge detection, which do not fully leverage terrain or atmospheric conditions. As a result, the generated images often lack accuracy and naturalness when dealing with complex terrains and atmospheric phenomena. In this paper, we propose a novel remote sensing image generation framework, D2-CDIG, which integrates diffusion models with a dual-prior control mechanism. By incorporating both Digital Elevation Model (DEM) and cloud-fog information as dual prior knowledge, D2-CDIG precisely controls ground features and atmospheric phenomena within the generated images. Specifically, D2-CDIG decouples the terrain and atmospheric generation processes through independent control of ground and atmospheric branches. Additionally, a refined cloud-fog slider is introduced to flexibly adjust cloud thickness and distribution. During training, ground and atmospheric control signals are injected in layers to ensure a seamless transition within the images. Compared to traditional methods based on segmentation or edge detection, D2-CDIG shows significant improvements in image quality, detail richness, and realism. D2-CDIG offers a flexible and precise solution for remote sensing image generation, providing high-quality data for training large remote sensing models and downstream tasks.

---


### 103. [InsightTok: Improving Text and Face Fidelity in Discrete Tokenization for Autoregressive Image Generation](https://arxiv.org/abs/2605.14333)

**<font color=#1a73e8>作者：</font>** Yang Yue, Fangyun Wei, Tianyu He 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text and faces are among the most perceptually salient and practically important patterns in visual generation, yet they remain challenging for autoregressive generators built on discrete tokenization. A central bottleneck is the tokenizer: aggressive downsampling and quantization often discard the fine-grained structures needed to preserve readable glyphs and distinctive facial features. We attribute this gap to standard discrete-tokenizer objectives being weakly aligned with text legibility and facial fidelity, as these objectives typically optimize generic reconstruction while compressing diverse content uniformly. To address this, we propose InsightTok, a simple yet effective discrete visual tokenization framework that enhances text and face fidelity through localized, content-aware perceptual losses. With a compact 16k codebook and a 16x downsampling rate, InsightTok significantly outperforms prior tokenizers in text and face reconstruction without compromising general reconstruction quality. These gains consistently transfer to autoregressive image generation in InsightAR, producing images with clearer text and more faithful facial details. Overall, our results highlight the potential of specialized supervision in tokenizer training for advancing discrete image generation.

---


### 104. [IG-Diff: Complex Night Scene Restoration with Illumination-Guided Diffusion Model](https://arxiv.org/abs/2605.14337)

**<font color=#1a73e8>作者：</font>** Yifan Chen, Fei Yin, Chunle Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In nighttime circumstances, it is challenging for individuals and machines to perceive their surroundings. While prevailing image restoration methods adeptly handle singular forms of degradation, they falter when confronted with intricate nocturnal scenes, such as the concurrent presence of weather and low-light conditions. Compounding this challenge, the lack of paired data that encapsulates the coexistence of low-light situations and other forms of degradation hinders the development of a comprehensive end-to-end solution. In this work, we contribute complex nighttime scene datasets that simulate both illumination degradation and other forms of deterioration. To address the complexity of night degradation, we propose an integration of an illumination-guided module embedded in the diffusion model to guide the illumination restoration process. Our model can preserve texture fidelity while contending with the adversities posed by various degradation in low-light scenarios.

---


### 105. [AnyBand-Diff: A Unified Remote Sensing Image Generation and Band Repair Framework with Spectral Priors](https://arxiv.org/abs/2605.14341)

**<font color=#1a73e8>作者：</font>** Zuopeng Zhao, Ying Liu, Xiaoyu Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing diffusion models have made significant progress in generating realistic images. However, their direct adaptation to remote sensing imagery often disregards intrinsic physical laws. This oversight frequently leads to spectral distortion and radiometric inconsistency, severely limiting the scientific utility of generated data. To address this issue, this paper introduces AnyBand-Diff, a novel spectral-prior-guided diffusion framework tailored for robust spectral reconstruction. Specifically, we design a Masked Conditional Diffusion backbone integrated with a dual stochastic masking strategy, empowering the model to recover complete spectral information from arbitrary band subsets. Subsequently, to ensure radiometric fidelity, a Physics-Guided Sampling mechanism is proposed, leveraging gradients from a differentiable physical model to explicitly steer the denoising trajectory toward the manifold of physically plausible solutions. Furthermore, a Multi-Scale Physical Loss is formulated to enforce rigorous constraints across pixel, region, and global levels in a joint manner. Extensive experiments confirm the effectiveness of AnyBand-Diff in generating reliable imagery and achieving accurate spectral reconstruction, contributing to the advancement of physics-aware generative methods for Earth observation.

---


### 106. [Nearest-Neighbor Radii under Dependent Sampling](https://arxiv.org/abs/2605.14343)

**<font color=#1a73e8>作者：</font>** Yuanyuan Gao, Yilong Hou, Zhexiao Lin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Nearest-neighbor methods are fundamental to classical and modern machine learning, yet their geometric properties are typically analyzed under independent sampling. In this paper, we study the nearest-neighbor radii under dependent sampling. We consider strong mixing dependent observations and ask whether dependence changes the scale of nearest-neighbor neighborhoods. We establish distribution-free almost sure convergence under polynomial mixing and sharp non-asymptotic moment bounds under geometric mixing. The moment bounds depend on the local intrinsic dimension rather than the ambient dimension, making the results applicable to high-dimensional data concentrated near lower-dimensional manifolds. Synthetic experiments and real-world time-series benchmarks support the theory, showing that nearest-neighbor geometry remains informative under dependence sampling.

---


### 107. [CrystalReasoner: Reasoning and RL for Property-Conditioned Crystal Structure Generation](https://arxiv.org/abs/2605.14344)

**<font color=#1a73e8>作者：</font>** Yuyang Wu, Stefano Falletta, Delia McGrath 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative modeling has emerged as a promising approach for crystal structure discovery. However, existing LLM-based generative models struggle with low-level atomic precision, while diffusion-based methods fall short in integrating high-level scientific knowledge. As a result, generated structures are often invalid, unstable, or do not possess desirable properties. To address this gap, we propose CrystalReasoner (\method), an end-to-end LLM framework that generates crystal structures from natural language instructions through reasoning and alignment. \method introduces physical priors as thinking tokens, which include crystallographic symmetry, local coordination environments and predicted physical properties before generating atomic coordinates. This bridges the gap between natural language and 3D structures. \method then employs reinforcement learning (RL) with a multi-objective, dense reward function to align generation with physical validity, chemical consistency, and thermodynamic stability. For property-conditioned tasks, we design task-specific reward functions and train specialized models for discrete constraints (e.g., space group) and continuous properties (e.g., elasticity, thermal expansion). Empirical results demonstrate that compared to prior works and baselines without thinking traces or RL, \method obtains better performance on diverse metrics, triples S.U.N. ratio, and achieves better performance for property conditioned generation. \method also exhibits adaptive reasoning, increasing reasoning lengths as the number of atoms increases. Our work demonstrates the potential of leveraging thinking traces and RL for generating valid, stable, and property-conditioned crystal structures. Please see our work at this https URL .

---


### 108. [Learning with Semantic Priors: Stabilizing Point-Supervised Infrared Small Target Detection via Hierarchical Knowledge Distillation](https://arxiv.org/abs/2605.14346)

**<font color=#1a73e8>作者：</font>** Yuanhang Yao, Ping Qian, Zhu Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-frame Infrared Small Target Detection (ISTD) aims to localize weak targets under heavy background clutter, yet dense pixel-wise annotations are expensive. Point supervision with online label evolution reduces annotation cost; however, lightweight CNN detectors often lack sufficient semantics, leading to noisy pseudo-masks and unstable optimization. To address this, we propose a hierarchical VFM-driven knowledge distillation framework that uses a frozen Vision Foundation Model (VFM) during training. We formulate point-supervised learning as a bilevel optimization process: the inner loop adapts a VFM-embedded teacher on reweighted training samples, while the outer loop transfers validation-guided knowledge to a lightweight student to mitigate pseudo-label noise and training-set bias. We further introduce Semantic-Conditioned Affine Modulation (SCAM) to inject VFM semantics into CNN features at multiple layers. In addition, a dynamic collaborative learning strategy with cluster-level sample reweighting enhances robustness to imperfect pseudo-masks. Experiments on diverse challenging cases across multiple ISTD backbones demonstrate consistent improvements in detection accuracy and training stability. Our code is available at this https URL.

---


### 109. [Exemplar Partitioning for Mechanistic Interpretability](https://arxiv.org/abs/2605.14347)

**<font color=#1a73e8>作者：</font>** Jessica Rumbelow  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Exemplar Partitioning (EP), an unsupervised method for constructing interpretable feature dictionaries from large language model activations with $\sim 10^{3}\times$ fewer tokens than comparable sparse autoencoders (SAEs). An EP dictionary is a Voronoi partition of activation space, built by leader-clustering streamed activations within a distance threshold. Each region is anchored by an observed exemplar that serves as both its membership criterion and intervention direction; dictionary size is not prespecified, but determined by the activation geometry at that threshold. Because exemplars are observed rather than learned, dictionaries built from the same data stream are directly comparable across layers, models, and training checkpoints.
We characterise EP as an interpretability object via targeted demonstrations of properties newly accessible through this construction, plus one head-to-head benchmark. In Gemma-2-2B, EP dictionary regions are interpretable and support causal interventions: refusal in instruction-tuned Gemma concentrates in a region whose exemplar ablation can collapse held-out refusal. Cross-checkpoint matching between base and instruction-tuned dictionaries separates the directions preserved through finetuning from those introduced by it. EP regions and Gemma Scope SAE features decompose activation space differently but agree on a shared core: $\sim 20\%$ of EP regions match an SAE feature at $F_{1} > 0.5$, and EP one-hot probes retain $\sim 97\%$ of raw-activation probe accuracy at $\ell_{0} = 1$. Nearest-exemplar distance provides a free out-of-distribution signal at inference. On AxBench latent concept detection at Gemma-2-2B-it L20, EP at $p_{1}$ reaches mean AUROC $0.881$, $+0.126$ over the canonical GemmaScope SAE leaderboard entry and within $0.030$ of SAE-A's $0.911$, at $\sim 10^{3}\times$ less build compute.

---


### 110. [Distributionally Robust Multi-Task Reinforcement Learning via Adaptive Task Sampling](https://arxiv.org/abs/2605.14350)

**<font color=#1a73e8>作者：</font>** Nicholas E. Corrado, Wenyuan Huang, Josiah P. Hanna  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-task reinforcement learning (MTRL) aims to train a single agent to efficiently optimize performance across multiple tasks simultaneously. However, jointly optimizing all tasks often yields imbalanced learning: agents quickly solve easy tasks but learn slowly on harder ones. While prior work primarily attributes this imbalance to conflicting task gradients and proposes gradient manipulation or specialized architectures to address it, we instead focus on a distinct and under-explored challenge: imbalanced data allocation. Standard MTRL allocates an equal number of environment interactions to each task, which over-allocates data to easy tasks that require relatively few interactions to solve and under-allocates data to hard tasks that require substantially more experience to solve. To address this challenge, we introduce Distributionally Robust Adaptive Task Sampling (DRATS), an algorithm that adaptively prioritizes sampling tasks furthest from being solved. We derive DRATS by formalizing MTRL as a feasibility problem from which we derive a minimax objective for minimizing the worst-case return gap, the difference between a desired target return and the agent's return on a task. In benchmarks like MetaWorld-MT10 and MT50, DRATS improves data efficiency and increases worst-task performance compared to existing task sampling algorithms.

---


### 111. [Ideology Prediction of German Political Texts](https://arxiv.org/abs/2605.14352)

**<font color=#1a73e8>作者：</font>** Sinclair Schneider, Florian Steuber, Joao A. G. Schneider 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Elections represent a crucial milestone in a nation's ongoing development. To better understand the political rhetoric from various movements, ranging from left to right, we propose a transformer-based model capable of projecting the political orientation of a text on a continuous left-to-right spectrum, represented by a normalized scalar d between -1 and 1. This approach enables analysts to focus on specific segments of the political landscape, such as conservatives, while excluding liberal and far-right movements. Such a task can only be achieved with multiclass classifiers, provided that the desired orientation is incorporated within one of their predefined classes. To determine the most suitable foundation model among 13 candidate transformers for this task, we constructed four distinct corpora. One corpus comprised annotated plenary notes from the German Bundestag, while another was based on an official online decision-making tool, Wahl-O-Mat. The third corpus consisted of articles from 33 newspapers, each identified by its political orientation, and the fourth included 535,200 tweets from 597 members of the 20th and 21st German Bundestag. To mitigate overfitting, we used two distinct corpora for training and two for testing, respectively. For in-domain performance, DeBERTa-large achieved the highest F1 score F1=0.844 as well as for the X (Twitter) out-of-domain test ACC=0.864. Regarding the newspaper out-of-domain test, Gemma2-2B excelled (MAE = 0.172). This study demonstrates that transformer models can recognize political framing in German news at the level of public opinion polls. Our findings suggest that both the model architecture and the availability of domain-specific training data can be as influential as model size for estimating political bias. We discuss methodological limitations and outline directions for improving the robustness of bias measurement.

---


### 112. [Uncovering the Representation Geometry of Minimal Cores in Overcomplete Reasoning Traces](https://arxiv.org/abs/2605.14358)

**<font color=#1a73e8>作者：</font>** Sanjoy Chowdhury, Dinesh Manocha  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models often generate long chain-of-thought traces, but it remains unclear how much of this reasoning is necessary for preserving the final prediction. We study this through the lens of overcomplete reasoning traces: generated traces that contain more intermediate steps than are needed to support the model's answer. We define the minimal core as the smallest subset of steps that preserves either the final answer or predictive distribution, and introduce metrics for compression ratio, redundancy mass, step necessity, and necessity concentration. Across six deliberative reasoning benchmarks spanning arithmetic, competition mathematics, expert scientific reasoning, and commonsense multi-hop QA, we find substantial overcompleteness: on average, 46% of steps are removable under greedy minimal-core extraction while preserving the original answer in 86% of cases. We also find that predictive support is concentrated: the top three steps account for 65% of measured necessity mass on average. Beyond compression, minimal cores expose a cleaner geometry of reasoning: compared with full traces, they improve correct-incorrect trace separation by 11 points, reduce estimated intrinsic dimensionality by 34%, and transfer across model families with 85% off-diagonal answer retention. Theoretically, we establish existence of minimal sufficient subsets, local irreducibility guarantees for greedy elimination, and certificates of overcompleteness and sparse necessity. Together, these results suggest that full reasoning traces are often verbose and overcomplete, while minimal cores isolate the effective support underlying language-model predictions.

---


### 113. [A Formative Study of Brief Affective Text as a Complement to Wearable Sensing for Longitudinal Student Health Monitoring](https://arxiv.org/abs/2605.14360)

**<font color=#1a73e8>作者：</font>** Tamunotonye Harry, Johanna Hidalgo, Matthew Price 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Wearable devices capture physiological and behavioral data with increasing fidelity, but the psychological context shaping these outcomes is difficult to recover from sensor data alone, limiting passive sensing utility for digital health. We examined whether ultra-brief naturalistic concern text could serve as a scalable complement to passive sensing. In a year-long study of 458 university students (3,610 person-waves) tracked with Oura rings, participants responded bimonthly to an open-ended prompt about what concerned them most; responses had a median length of three words. We compared dictionary-based, general pretrained, and domain-adapted NLP approaches using within-person mixed-effects models across nine sleep and physical activity outcomes. Weeks dominated by academic concern framing were associated with lower physical activity; weeks characterized by emotional exhaustion language were associated with poorer sleep quality and lower heart rate variability. General pretrained embeddings outperformed domain-adapted models for most outcomes, with domain adaptation showing relative advantage for autonomic outcomes. Zero-shot classification of concern topics produced no significant associations, while affective dimensions across all three methods were consistently associated with outcomes, indicating emotional register rather than topical content carries the signal. These findings offer design guidance: ultra-brief affective prompts enrich the psychological interpretability of passive physiological data at minimal burden.

---


### 114. [MoRe: Modular Representations for Principled Continual Representation Learning on Squantial Data](https://arxiv.org/abs/2605.14364)

**<font color=#1a73e8>作者：</font>** Jiaqi Sun, Boyang Sun, Mohamad Rasmy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning requires models to adapt to new data while preserving previously acquired knowledge. At its core, this challenge can be viewed as principled one-step adaptation: incorporating new information with minimal interference to existing representations. Most existing approaches address this challenge by modifying model parameters or architectures in a supervised, task-specific manner. However, the underlying issue is representational: tasks require distinct yet structured representations that can be selectively updated without disrupting representations, while structure should reflect intrinsic organization in the data rather than task boundaries. In sequential data, time-delayed dependencies provide a natural signal for uncovering this organization, revealing how fundamental representations give rise to more specific ones. Inspired by the modular organization of the human brain, we propose MoRe, a framework that identifies modularity in the representation itself rather than allocating it at the architectural level. MoRe decomposes knowledge into a hierarchy of fundamental and specific modules with identifiability guarantees, enabling principled module reuse, alignment, and expansion during adaptation while preserving old modules by construction. Experiments on synthetic benchmarks and real-world LLM activations demonstrate interpretable hierarchical structure, improved plasticity-stability trade-offs, suggesting MoRe as a principled foundation for continual adaptation

---


### 115. [LoMETab: Beyond Rank-1 Ensembles for Tabular Deep Learning](https://arxiv.org/abs/2605.14365)

**<font color=#1a73e8>作者：</font>** Changryeol Choi, Hyewon Park, Yujin Kwon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent tabular learning benchmarks increasingly show a tight performance cluster rather than a clear hierarchy among leading methods, spanning gradient boosted decision trees, attention-based architectures, and implicit ensembles such as TabM. As benchmark gains plateau, a complementary goal is to understand and control the mechanisms that make simple neural tabular models competitive. We propose LoMETab, a rank-$r$ generalization of multiplicative implicit ensembles. LoMETab lifts the rank-1 BatchEnsemble/TabM modulation to a rank-$r$ identity-residual Hadamard family by parameterizing each member weight as $W_k = W \odot (1 + A_kB_k^\top)$, where $W$ is shared and $(A_k, B_k)$ are member-specific low-rank factors. This exposes two practical diversity-control axes: the adapter rank $r$ and the initialization scale $\sigma_{\mathrm{init}}$, and we prove that for $r \ge 2$ this generalization strictly enlarges BatchEnsemble's hypothesis class. Empirically, we show that this added capacity manifests as measurable predictive diversity after training: on representative classification datasets, LoMETab sustains higher pairwise KL than an additive low-rank ablation, and $(r, \sigma_{\mathrm{init}})$ provides broad control over pairwise KL, varying by up to several orders of magnitude across configurations. The induced diversity is reflected in task-appropriate output-level measures: argmax disagreement for classification and ambiguity for regression, indicating that the control extends beyond pairwise KL to decision- and output-level member variation. Finally, experiments sweeping over adapter rank $r$ and initialization scale $\sigma_{\mathrm{init}}$ reveal that predictive performance is dataset-dependent over the $(r, \sigma_{\mathrm{init}})$ grid, supporting LoMETab as a controllable family of implicit ensembles rather than a fixed rank-1 construction.

---


### 116. [Turning Stale Gradients into Stable Gradients: Coherent Coordinate Descent with Implicit Landscape Smoothing for Lightweight Zeroth-Order Optimization](https://arxiv.org/abs/2605.14373)

**<font color=#1a73e8>作者：</font>** Chen Liang, Xiatao Sun, Qian Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zeroth-Order (ZO) optimization is pivotal for scenarios where backpropagation is unavailable, such as memory-constrained on-device learning and black-box optimization. However, existing methods face a stark trade-off: they are either sample-inefficient (e.g., standard finite differences) or suffer from high variance due to randomized estimation (e.g., random subspace methods). In this work, we propose Coherent Coordinate Descent (CoCD), a deterministic, sample-efficient, and budget-aware ZO optimizer. Theoretically, we formalize the notion of gradient coherence and demonstrate that CoCD is equivalent to Block Cyclic Coordinate Descent (BCCD) with ``warm starts,'' effectively converting historical (stale) gradients from a liability into a computational asset. This mechanism enables $O(1)$ query complexity per step while maintaining global descent directions. Furthermore, we derive error bounds revealing a counter-intuitive insight: larger finite-difference step sizes can induce an implicit smoothing effect on the optimization landscape by reducing the effective smoothness constant, thereby improving convergence stability. Experiments on MLP, CNN, and ResNet architectures (up to 270k parameters) demonstrate that CoCD significantly outperforms BCCD in terms of sample efficiency and convergence loss/accuracy, and exhibits superior stability over randomized ZO methods. Our results suggest that deterministic, structure-aware updates offer a superior alternative to randomization for lightweight ZO optimization.

---


### 117. [Optimal Pattern Detection Tree for Symbolic Rule-Based Classification](https://arxiv.org/abs/2605.14374)

**<font color=#1a73e8>作者：</font>** Young-Chae Hong, Yangho Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pattern discovery in data plays a crucial role across diverse domains, including healthcare, risk assessment, and machinery maintenance. In contrast to black-box deep learning models, symbolic rule discovery emerges as a key data mining task, generating human-interpretable rules that offer both transparency and intuitive explainability. This paper introduces the Optimal Pattern Detection Tree (OPDT), a rule-based machine learning model based on novel mixed-integer programming to discover a single optimal pattern in data through binary classification. To incorporate prior knowledge and compliance requirements, we further introduce the Branching Structure Constraints (BSC) framework, which enables decision makers to encode domain knowledge and constraints directly into the model. This optimization-based approach discovers a hidden underlying pattern in datasets, when it exists, by identifying an optimal rule that maximizes coverage while minimizing the false positive rate due to misclassification. Our computational experiments show that OPDT discovers a pattern with optimality guarantees on moderately sized datasets within reasonable runtime.

---


### 118. [Data-Augmented Game Starts for Accelerating Self-Play Exploration in Imperfect Information Games](https://arxiv.org/abs/2605.14379)

**<font color=#1a73e8>作者：</font>** JB Lanier, Nathan Monette, Pierre Baldi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Finding approximate equilibria for large-scale imperfect-information competitive games such as StarCraft, Dota, and CounterStrike remains computationally infeasible due to sparse rewards and challenging exploration over long horizons. In this paper, we propose a multi-agent starting-state sampling strategy designed to substantially accelerate online exploration in regularized policy-gradient game methods for two-player zero-sum (2p0s) games. Motivated by an assumption that offline demonstrations from skilled humans can provide good coverage of high-level strategies relevant to equilibrium play, we propose the initialization of reinforcement learning data collection at intermediate states sampled from offline data to facilitate exploration of strategically relevant subgames. Referring to this method as Data-Augmented Game Starts (DAGS), we perform experiments using synthetic datasets and analytically tractable, long-horizon control variants of two-player Kuhn Poker, Goofspiel, and a counterexample game designed to penalize biased beliefs over hidden information. Under fixed computational budgets, DAGS enables regularized policy gradient methods to achieve lower exploitability in games with significantly more challenging exploration. We show that augmenting starting state distributions when solving imperfect information games can lead to biased equilibria, and we provide a straightforward mitigation to this in the form of multi-task observation flags. Finally, we release a new set of benchmark environments that drastically increase exploration challenges and state counts in existing OpenSpiel games while keeping exploitability measurements analytically tractable.

---


### 119. [Mitigating Data Scarcity in Psychological Defense Classification with Context-Aware Synthetic Augmentation](https://arxiv.org/abs/2605.14380)

**<font color=#1a73e8>作者：</font>** Hoang-Thuy-Duong Vu, Quoc-Cuong Pham, Huy-Hieu Pham  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Psychological defense mechanisms (PDMs) are unconscious cognitive processes that modulate how individuals perceive and respond to emotional distress. Automatically classifying PDMs from text is clinically valuable but severely hindered by data scarcity and class imbalance, challenges which generative augmentation alone cannot resolve without psychological grounding. In this work, we address these challenges in the PsyDefDetect shared task (BioNLP@ACL 2026) by proposing a context-aware synthetic augmentation framework combined with a hybrid classification model. Our hybrid model integrates contextual language representations with basic clinical features, along with 150 annotated defense items. Experiments demonstrate that definition quality in prompting directly governs generation fidelity and downstream performance. Our method surpasses DMRS Co-Pilot, reaching an accuracy of 58.26% (+40.25%) and a macro-F1 of 24.62% (+15.99%), thereby establishing a strong baseline for psychologically grounded defense mechanism classification in low-resource settings. Source code is available at: this https URL.

---


### 120. [Delta Forcing: Trust Region Steering for Interactive Autoregressive Video Generation](https://arxiv.org/abs/2605.14382)

**<font color=#1a73e8>作者：</font>** Yuheng Wu, Xiangbo Gao, Tianhao Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive real-time autoregressive video generation is essential for applications such as content creation and world modeling, where visual content must adapt to dynamically evolving event conditions. A fundamental challenge lies in balancing reactivity and stability: models must respond promptly to new events while maintaining temporal coherence over long horizons. Existing approaches distill bidirectional models into autoregressive generators and further adapt them via streaming long tuning, yet often exhibit persistent drift after condition changes. We identify the cause as conditional bias, where the teacher may provide condition-aligned but trajectory-agnostic guidance, biasing generation toward locally valid yet globally inconsistent modes. Inspired by Trust Region Policy Optimization, we propose Delta Forcing, a simple yet effective framework that constrains unreliable teacher supervision within an adaptive trust region. Specifically, Delta Forcing estimates transition consistency from the latent delta between teacher and generator trajectories, and uses it to balance teacher supervision with a monotonic continuity objective. This suppress unreliable teacher-induced shifts while preserving responsiveness to new events. Extensive experiments demonstrate that Delta Forcing significantly improves consistency while maintaining event reactivity.

---


### 121. [Model Forensics in AI-Native Wireless Networks: Taxonomy, Applications, and Case Study](https://arxiv.org/abs/2605.14387)

**<font color=#1a73e8>作者：</font>** Pengyu Chen, Weiyang Li, Jin Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As artificial intelligence (AI) is increasingly embedded in wireless networks, models are becoming core components that influence signal processing, resource scheduling and network control. However, model anomalies, tampering and malicious functions also introduce new security risks. In this article, we focus on model forensics in AI-native wireless networks. Specifically, we first discuss key problems including model authenticity verification, malicious function identification and accountability tracing, and summarize the main categories of model forensics. We then explain the role of model forensics in AI-native wireless networks and review representative application scenarios. In the case study, we use RF fingerprinting as an example and present two concrete workflows based on watermark authentication and backdoor detection, illustrating how provenance authentication and malicious behavior identification can be implemented in practice. The results show that model forensics can provide important support for anomaly assessment, provenance tracing and trustworthy operation in AI-native wireless networks. Finally, we outline several promising directions for future research in this emerging area.

---


### 122. [Dual-Latent Collaborative Decoding for Fidelity-Perception Balanced Image Compression](https://arxiv.org/abs/2605.14391)

**<font color=#1a73e8>作者：</font>** Qi Mao, Zijian Wang, Zhengxue Cheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learned image compression (LIC) increasingly requires reconstructions that balance distortion fidelity and perceptual realism across a wide range of bitrates. However, most existing methods still rely on a single compressed latent representation to simultaneously carry structural details, semantic cues, and perceptual priors, requiring the same latent representation to serve multiple, potentially conflicting roles. This tension becomes evident across different latent paradigms: scalar-quantized (SQ) continuous latents provide rate-scalable fidelity but tend to lose perceptual details at low rates, while vector-quantized (VQ) discrete tokens preserve compact semantic cues but suffer from limited structural fidelity and bitrate scalability. To address this issue, we propose Mixture of Decoder Experts (MoDE), a dual-latent collaborative decoding framework that decomposes reconstruction responsibilities across complementary latent paradigms. Specifically, MoDE treats the SQ branch as a fidelity-oriented expert and the VQ branch as a perception-oriented expert, and coordinates them through two decoder-side modules: Expert-Specific Enhancement (ESE), which preserves branch-specific expert references, and Cross-Expert Modulation (CEM), which enables selective complementary transfer during reconstruction. The resulting framework supports selective cross-latent collaboration under a shared dual-stream bitstream and enables both fidelity-anchored and perception-anchored decoding. Extensive experiments demonstrate that MoDE achieves a more favorable fidelity-perception balance than representative distortion-oriented, perception-oriented, generative, and dual-latent baselines across a wide bitrate range, highlighting decoder-side expert collaboration as an effective design for wide-range fidelity-perception balanced LIC.

---


### 123. [Learning to Build the Environment: Self-Evolving Reasoning RL via Verifiable Environment Synthesis](https://arxiv.org/abs/2605.14392)

**<font color=#1a73e8>作者：</font>** Yucheng Shi, Zhenwen Liang, Kishan Panaganti 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We pursue a vision for self-improving language models in which the model does not merely generate problems or traces to imitate, but constructs the environments that train it. In zero-data reasoning RL, this reframes self-improvement from a data-generation loop into an environment-construction loop, where each artifact is a reusable executable object that samples instances, computes references, and scores responses. Whether this vision sustains improvement hinges on a single property: the environments must exhibit stable solve--verify asymmetry, the model must be able to write an oracle once that it cannot reliably execute in natural language on fresh instances. This asymmetry takes two complementary forms. Some tasks are algorithmically hard to reason through but trivial as code: a dynamic program or graph traversal, compiled once, yields unboundedly many calibrated instances. Others are intrinsically hard to solve but easy to verify, like planted subset-sum or constraint satisfaction. Both create a durable gap between proposing and solving that the policy cannot close by gaming the verifier, and it is this gap that keeps reward informative as the learner improves. We instantiate this view in EvoEnv, a single-policy generator, solver method that synthesizes Python environments from ten seeds and admits them only after staged validation, semantic self-review, solver-relative difficulty calibration, and novelty checks. The strongest evidence comes from the already-strong regime: on Qwen3-4B-Thinking, fixed public-data RLVR and fixed hand-crafted environment RLVR reduce the average, while EvoEnv improves it from 72.4 to 74.8, a relative gain of 3.3%. Stable self-improvement, we suggest, depends not on producing more synthetic data, but on models learning to construct worlds whose difficulty stays structurally beyond their own reach.

---


### 124. [Analogical Trajectory Transfer](https://arxiv.org/abs/2605.14393)

**<font color=#1a73e8>作者：</font>** Junho Kim, Eun Sun Lee, Gwangtak Bae 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study analogical trajectory transfer, where the goal is to translate motion trajectories in one 3D environment to a semantically analogous location in another. Such a capacity would enable machines to perform analogical spatial reasoning, with applications in AR/VR co-presence, content creation, and robotics. However, even semantically similar scenes can still differ substantially in object placement, scale, and layout, so naively matching semantics leads to collisions or geometric distortions. Furthermore, finding where each trajectory point should transfer to has a large search space, as the mapping must preserve semantics and functionality without tearing the trajectory apart or causing collisions. Our key insight is to decompose the problem into spatially segregated subproblems and merge their solutions to produce semantically consistent and spatially coherent transfers. Specifically, we partition scenes into object-centric clusters and estimate cross-scene mappings via hierarchical smooth map prediction, using 3D foundation model features that encode contextual information from object and open-space arrangements. We then combinatorially assemble the per-cluster maps into an initial transfer and refine the result to remove collisions and distortions, yielding a spatially coherent trajectory. Our method does not require training, attains a fast runtime around 0.6 seconds, and outperforms baselines based on LLMs, VLMs, and scene graph matching. We further showcase applications in virtual co-presence, multi-trajectory transfer, camera transfer, and human-to-robot motion transfer, which indicates the broad applicability of our work to AR/VR and robotics.

---


### 125. [Systematic Discovery of Semantic Attacks in Online Map Construction through Conditional Diffusion](https://arxiv.org/abs/2605.14396)

**<font color=#1a73e8>作者：</font>** Chenyi Wang, Ruoyu Song, Raymond Muller 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous vehicles depend on online HD map construction to perceive lane boundaries, dividers, and pedestrian crossings -- safety-critical road elements that directly govern motion planning. While existing pixel perturbation attacks can disrupt the mapping, they can be neutralized by standard adversarial defenses. We present MIRAGE, a framework for systematic discovery of semantic attacks that bypass adversarial defenses and degrade mapping predictions by finding plausible environmental variation (e.g. shadows, wet roads). MIRAGE exploits the latent manifold of real-world data learned by diffusion models, and searches for semantically mutated scenes neighboring the ground truth with the same road topology yet mislead the mapping predictions. We evaluate MIRAGE on nuScenes and demonstrate two attacks: (1) boundary removal, suppressing 57.7% of detections and corrupting 96% of planned trajectories; and (2) boundary injection, the only method that successfully injects fictitious boundaries, while pixel PGD and AdvPatch fail entirely. Both attacks remain potent under various adversarial defenses. We use two independent VLM judges to quantify realism, where MIRAGE passes as realistic 80--84% of the time (vs. 97--99% for clean nuScenes), while AdvPatch only 0--9%. Our findings expose a categorical gap in current adversarial defenses: semantic-level perturbations that manifest as legitimate environmental variation are substantially harder to mitigate than pixel-level perturbations.

---


### 126. [Coding Agent Is Good As World Simulator](https://arxiv.org/abs/2605.14398)

**<font color=#1a73e8>作者：</font>** Hongyu Wang, Jingquan Wang, Bocheng Zou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models have emerged as a powerful paradigm for building interactive simulation environments, with recent video-based approaches demonstrating impressive progress in generating visually plausible dynamics. However, because these models typically infer dynamics from video and represent them in latent states, they do not explicitly enforce physical constraints. As a result, the generated video rollouts are not physically plausible, exhibiting unstable contacts, distorted shapes, or inconsistent motion. In this paper, we present an agentic framework constructing physics-based world models through executable simulation code. The framework coordinates planning, code generation, visual review, and physics analysis agents. The planning agent converts the natural language prompt into a structured scene plan, the code agent implements it as executable simulation code, and the visual review agent provide visual feedback while the physics analysis agent checks physical consistency. The code is iteratively revised based on the feedback until the simulation matches the prompt reqirements and physical constraints. Experimental results show that our framework outperforms advanced video-based models in physical accuracy, instruction fidelity and visual quality, which could be applied to various scenarios including driving simulation and embodied robot tasks.

---


### 127. [SceneForge: Structured World Supervision from 3D Interventions](https://arxiv.org/abs/2605.14399)

**<font color=#1a73e8>作者：</font>** Jizhizi Li, Jiayang Ao, Danny Wicks 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many multimodal learning tasks require supervision that remains consistent across edits, viewpoints, and scene-level interventions. However, such supervision is difficult to obtain from observation-level datasets, which do not expose the underlying scene state or how changes propagate through it. We present SceneForge, an intervention-driven framework that generates structured supervision from editable 3D world states. SceneForge represents each scene as a persistent world with semantic, geometric, and physical dependencies. By applying explicit interventions (e.g., object removal or camera variation) and propagating their effects through scene dependencies, SceneForge renders supervision that remains consistent with object structure and scene-level effects. This produces aligned outputs including counterfactual observations, multi-view observations, and effect-aware signals such as shadows and reflections, all derived from a shared world state rather than post hoc image-space processing. We instantiate SceneForge using Infinigen and Blender to construct a licensing-clean indoor supervision resource with a large number of counterfactual pairs and aligned annotations from over 2K scenes, covering both diverse single-view and registered multi-view settings. Under matched training budgets, incorporating SceneForge supervision improves both object removal and scene removal performance across multiple benchmarks in both quantitative and qualitative evaluation. These results indicate that modeling supervision as structured state transitions in editable worlds provides a practical and scalable foundation for intervention-consistent multimodal learning.

---


### 128. [Knowledge Beyond Language: Bridging the Gap in Multilingual Machine Unlearning Evaluation](https://arxiv.org/abs/2605.14404)

**<font color=#1a73e8>作者：</font>** Kyomin Hwang, Hyeonjin Kim, Sangyeon Cho 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While LLMs are increasingly used in commercial services, they pose privacy risks such as leakage of sensitive personally identifiable information (PII). For LLMs trained on multilingual corpora, Multilingual Machine Unlearning (MMU) aims to remove information across multiple languages. However, prior MMU evaluations fail to capture such cross-linguistic distribution of information, being largely limited to direct extensions of per-language evaluation protocols. To this end, we propose two metrics to evaluate the information spread across languages: the Knowledge Separability Score (KSS) and the Knowledge Persistence Score (KPS). KSS measures the overall unlearning quality across multiple languages, while KPS more specifically aims to assess consistent removal of information among different language pairs. We evaluated various unlearning methods in the multilingual setting with these metrics and conducted comprehensive analyses. Through our investigation, we provide insights into unique phenomena exclusive to MMU and offer a new perspective on MMU evaluation.

---


### 129. [Watch your neighbors: Training statistically accurate chaotic systems with local phase space information](https://arxiv.org/abs/2605.14405)

**<font color=#1a73e8>作者：</font>** Joon-Hyuk Ko, Andrus Giraldo, Deok-Sun Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chaotic systems pose fundamental challenges for data-driven dynamics discovery, as small modeling errors lead to exponentially growing trajectory discrepancies. Since exact long-term prediction is unattainable, it is natural to ask what a good surrogate model for chaotic dynamics is. Prior work has largely focused either on reproducing the Jacobian of the underlying dynamics, which governs local expansion and contraction rates, or on training surrogate models that reproduce the ground-truth dynamics' long-term statistical behavior. In this work, we propose a new framework that aims to bridge these two paradigms by training surrogate dynamics models with accurate Jacobians and long-term statistical properties. Our method constructs a local covering of a chaotic attractor in phase space and analyzes the expansion and contraction of these coverings under the dynamics. The surrogate model is trained by minimizing the maximum mean discrepancy between the pushforward distributions of the coverings under the surrogate and ground-truth dynamics. Experiments show that our method significantly improves Jacobian accuracy while remaining competitive with state-of-the-art statistically accurate dynamics learning methods. Our code is fully available at this https URL.

---


### 130. [Metis AI: The Overlooked Middle Zone Between AI-Native and World-Movers](https://arxiv.org/abs/2605.14407)

**<font color=#1a73e8>作者：</font>** Xiang Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The dominant discourse on AI limitations frames the boundary of AI capability as a divide between digital tasks (where AI excels) and physical tasks (where embodiment is required). We argue this framing misses the most consequential boundary: the one within digital tasks. We identify a class of tasks we call Metis AI, named for the Greek concept of metis (practical, contextual knowledge), that are performed entirely on computers yet resist reliable AI automation. These tasks are not computationally intractable; they are institutionally, socially, and normatively entangled in ways that defeat algorithmic approaches. We distinguish constitutive metis (knowledge destroyed by the act of formalization) from operational metis (system-specific familiarity that automation can progressively absorb), and propose five structural characteristics that define the Metis AI zone: consequential irreversibility, relational irreducibility, normative open texture, adversarial co-evolution, and accountability anchoring. We ground each in established theory from across the social sciences, philosophy, and humanitarian practice, argue that these characteristics are properties of the tasks themselves rather than limitations of current models, and show that the appropriate design response is not better automation but centaur architectures in which humans lead and AI supports.

---


### 131. [MahaVar: OOD Detection via Class-wise Mahalanobis Distance Variance under Neural Collapse](https://arxiv.org/abs/2605.14413)

**<font color=#1a73e8>作者：</font>** Donghwan Kim, Hyunsoo Yoon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Out-of-distribution (OOD) detection is a critical component for ensuring the reliability of deep neural networks in safety-critical applications. In this work, we present a key empirical observation: for in-distribution (ID) samples, class-wise Mahalanobis distances exhibit a pronounced sharp minimum structure, where the distance to the nearest class is small while distances to all other classes remain large, resulting in high variance across classes. In contrast, OOD samples tend to exhibit a less pronounced sharp minimum structure, producing comparatively lower variance across classes. We further provide a theoretical analysis grounding this observation in Neural Collapse geometry: under relaxed Neural Collapse assumptions on within-class compactness and inter-class separation, ID samples are shown to structurally exhibit high class-wise distance variance, offering a theoretical basis for its use as an OOD score. Motivated by this observation and its theoretical backing, we propose MahaVar, a simple and effective post-hoc OOD detector that augments the Mahalanobis distance with a class-wise distance variance term. Following the OpenOOD v1.5 benchmark protocol, MahaVar achieves state-of-the-art performance on CIFAR-100 and ImageNet, with consistent improvements in both AUROC and FPR@95 over existing Mahalanobis-based methods across all benchmarks.

---


### 132. [A Unified Knowledge Embedded Reinforcement Learning-based Framework for Generalized Capacitated Vehicle Routing Problems](https://arxiv.org/abs/2605.14416)

**<font color=#1a73e8>作者：</font>** Wen Wang, Xiangchen Wu, Liang Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Capacitated Vehicle Routing Problem (CVRP) is a fundamental NP-hard problem with broad applications in logistics and transportation. Real-world CVRPs often involve diverse objectives and complex constraints, such as time windows or backhaul requirements, motivating the development of a unified solution framework. Recent reinforcement learning (RL) approaches have shown promise in combinatorial optimization, yet they rely on end-to-end learning and lack explicit problem-solving knowledge, limiting solution quality. In this paper, we propose a knowledge-embedded framework inspired by the Route-First Cluster-Second heuristics. It incorporates knowledge at two levels: (1) decomposing CVRPs into the route-first and cluster-second subproblems, and (2) leveraging dynamic programming to solve the second subproblem, whose results guide the RL-based constructive solver to solve the first problem. To mitigate partial observability caused by problem decomposition, we introduce a unified history-enhanced context processing module. Extensive experiments show that this framework achieves superior solution quality compared with state-of-the-art learning-based methods, with a smaller gap to classical heuristics, demonstrating strong generalization across diverse CVRP variants.

---


### 133. [What if Tomorrow is the World Cup Final? Counterfactual Time Series Forecasting with Textual Conditions](https://arxiv.org/abs/2605.14422)

**<font color=#1a73e8>作者：</font>** Shuqi Gu, Yongxiang Zhao, Baoyu Jing 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series forecasting has become increasingly critical in real-world scenarios, where future sequences are influenced not only by historical patterns but also by forthcoming events. In this context, forecasting must dynamically adapt to complex and stochastic future conditions, which introduces fundamental challenges in both forecasting and evaluation. Traditional methods typically rely on historical data or factual future conditions, while overlooking counterfactual scenarios. Furthermore, many existing approaches are restricted to simple structured conditions, limiting their ability to generalize to the real-world complexities. To address these gaps, we introduce the task of counterfactual time series forecasting with textual conditions, enabling more flexible and condition-aware forecasting. We propose a comprehensive evaluation framework that encompasses both factual and counterfactual settings, even in the absence of ground truth time series. Additionally, we present a novel text-attribution mechanism that distinguishes mutable from immutable factors, thereby improving forecast accuracy under sophisticated and stochastic textual conditions. The project page is at this https URL

---


### 134. [Collaborative Yet Personalized Policy Training: Single-Timescale Federated Actor-Critic](https://arxiv.org/abs/2605.14423)

**<font color=#1a73e8>作者：</font>** Leo Muxing Wang, Pengkun Yang, Lili Su  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the popularity of the actor-critic method and the practical needs of collaborative policy training, existing works typically either overlook environmental heterogeneity or give up personalization altogether by training a single shared policy across all agents. We consider a federated actor-critic framework in which agents share a common linear subspace representation while maintaining personalized local policy components, and agents iteratively estimate the common subspace, local critic heads, and local policies (i.e., actors). Under canonical single-timescale updates with Markovian sampling, we establish finite-time convergence via a novel joint linear approximation framework. Specifically, we show that the critic error converges to zero at the rate of $\tilde{\mathcal{O}}(1/((1-\gamma)^4\sqrt{TK}))$, and the policy gradient norm converges to zero at the rate of $\tilde{\mathcal{O}}(1/((1-\gamma)^6\sqrt{TK}))$, where $T$ is the number of rounds, $K$ is the number of agents, and $\gamma\in (0,1)$ is the discount factor. These results demonstrate linear speedup with respect to the number of agents $K$, despite heterogeneous Markovian trajectories under distinct transition kernels and coupled learning dynamics. To address these challenges, we develop a new perturbation analysis for the projected subspace updates and QR decomposition steps, together with conditional mixing arguments for heterogeneous Markovian noise. Furthermore, to handle the additional complications induced by policy updates and temporal dependence, we establish fine-grained characterizations of the discrepancies between function evaluations under Markovian sampling and under temporally frozen policies. Experiments instantiate the framework within PPO on federated \texttt{Hopper-v5} action-map heterogeneity, showing gains over Single PPO and FedAvg PPO and downstream transfer from the learned shared trunk.

---


### 135. [A Calculus-Based Framework for Determining Vocabulary Size in End-to-End ASR](https://arxiv.org/abs/2605.14427)

**<font color=#1a73e8>作者：</font>** Sunil Kumar Kopparapu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In hybrid automatic speech recognition (ASR) systems, the vocabulary size is unambiguous, typically determined by the number of phones, bi-phones, or tri-phones present in the language. In contrast, end-to-end ASR systems derive their vocabulary, often referred to as tokens from the text corpus used for training. The choice and, more importantly, the size of this vocabulary is a critical hyper-parameter in training end-to-end ASR systems. Tokenization algorithms such as Byte Pair Encoding (BPE), WordPiece, and Unigram Language Model (ULM) use the vocabulary size as an input hyper-parameter to generate the sub-words employed during ASR training. Popular toolkits like ESPNet provide a fixed vocabulary size in their training recipes, but there is little documentation or discussion in the literature regarding how these values are determined. Recent work [1] has formalized an approach to identify the vocabulary size best suited for end-to-end ASR, introducing a cost function framework that treats the tokenization process as a black box. In this paper, we build upon that foundation by curve fitting the training data and using the principle of first and second derivative tests in calculus to formally estimate the vocabulary size hyper-parameter. We demonstrate the utility and usefulness of our approach by applying it on a standard Librispeech corpus and show that the optimal choice of vocabulary size hyper-parameter improves the performance of the ASR. The main contribution of this paper in formalizing an approach to identify the vocabulary size best suited for training an end-to-end ASR system.

---


### 136. [Synthesizing POMDP Policies: Sampling Meets Model-checking via Learning](https://arxiv.org/abs/2605.14440)

**<font color=#1a73e8>作者：</font>** Debraj Chakraborty, Anirban Majumdar, Prince Mathew 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Partially Observable Markov Decision Processes (POMDPs) are the standard framework for decision-making under uncertainty. While sampling-based methods scale well, they lack formal correctness guarantees, making them unsuitable for safety-critical applications. Conversely, formal synthesis techniques provide correctness-by-construction but often struggle with scalability, as general POMDP synthesis is undecidable. To bridge this gap, we propose a synthesis framework that integrates sampling, automata learning, and model-checking. Inspired by Angluin's $L^*$ algorithm, our approach utilizes sampling as a membership oracle and model-checking as an equivalence oracle. This enables the synthesis of finite-state controllers with formal guarantees, provided the sampling-induced policy is regular. We establish a relative completeness result for this framework. Experimental results from our prototypical implementation demonstrate that this method successfully solves threshold-safety problems that remain challenging for existing formal synthesis tools. We believe our algorithm serves as a valuable component in a portfolio approach to tackling the inherent difficulty of POMDP synthesis problems.

---


### 137. [FrontierSmith: Synthesizing Open-Ended Coding Problems at Scale](https://arxiv.org/abs/2605.14445)

**<font color=#1a73e8>作者：</font>** Runyuan He, Qiuyang Mang, Shang Zhou 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many real-world coding challenges are open-ended and admit no known optimal solution. Yet, recent progress in LLM coding has focused on well-defined tasks such as feature implementation, bug fixing, and competitive programming. Open-ended coding remains a weak spot for LLMs, largely because open-ended training problems are scarce and expensive to construct. Our goal is to synthesize open-ended coding problems at scale to train stronger LLM coders. We introduce FrontierSmith, an automated system for iteratively evolving open-ended problems from existing closed-ended coding tasks. Starting from competitive programming problems, FrontierSmith generates candidate open-ended variants by changing the problems'goals, restricting outputs, and generalizing inputs. It then uses a quantitative idea divergence metric to select problems that elicit genuinely diverse approaches from different solvers. Agents then generate test cases and verifiers for the surviving candidates. On two open-ended coding benchmarks, training on our synthesized data yields substantial gains over the base models: Qwen3.5-9B improves by +8.82 score on FrontierCS and +306.36 (Elo-rating-based performance) on ALE-bench; Qwen3.5-27B improves by +12.12 and +309.12, respectively. The synthesized problems also make agents take more turns and use more tokens, similar to human-curated ones, suggesting that closed-ended seeds can be a practical starting point for long-horizon coding data.

---


### 138. [When Answers Stray from Questions: Hallucination Detection via Question-Answer Orthogonal Decomposition](https://arxiv.org/abs/2605.14449)

**<font color=#1a73e8>作者：</font>** Siyang Yao, Erhu Feng, Yubin Xia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hallucination detection in large language models (LLMs) requires balancing accu racy, efficiency, and robustness to distribution shift. Black-box consistency methods are effective but demand repeated inference; single-pass white-box probes are effi cient yet treat answer representations in isolation, often degrading sharply under domain shift. We propose QAOD (Question-Answer Orthogonal Decomposition), a single-pass framework that projects away the question-aligned direction from the answer representation to obtain a question-orthogonal component that suppresses domain-conditioned variation. To identify informative signals, QAOD further selects layers via diversity-penalized Fisher scoring and discriminative neurons via Fisher importance. To address both in-domain detection and cross-domain generalization, we design two complementary probing strategies: pairing the or thogonal component with question context yields a joint probe that maximizes in-domain discriminability, while using the orthogonal component alone preserves domain-agnostic factuality signals for robust transfer. QAOD's joint probe achieves the best in-domain AUROC across all evaluated model-dataset pairs, while the orthogonal-only probe delivers the strongest OOD transfer, surpassing the best white-box baseline by up to 21% on BioASQ at under 25% of generation cost.

---


### 139. [LiSA: Lifelong Safety Adaptation via Conservative Policy Induction](https://arxiv.org/abs/2605.14454)

**<font color=#1a73e8>作者：</font>** Minbeom Kim, Lesly Miculicich, Bhavana Dalvi Mishra 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As AI agents move from chat interfaces to systems that read private data, call tools, and execute multi-step workflows, guardrails become a last line of defense against concrete deployment harms. In these settings, guardrail failures are no longer merely answer-quality errors: they can leak secrets, authorize unsafe actions, or block legitimate work. The hardest failures are often contextual: whether an action is acceptable depends on local privacy norms, organizational policies, and user expectations that resist pre-deployment specification. This creates a practical gap: guardrails must adapt to their own operating environments, yet deployment feedback is typically limited to sparse, noisy user-reported failures, and repeated fine-tuning is often impractical. To address this gap, we propose LiSA (Lifelong Safety Adaptation), a conservative policy induction framework that improves a fixed base guardrail through structured memory. LiSA converts occasional failures into reusable policy abstractions so that sparse reports can generalize beyond individual cases, adds conflict-aware local rules to prevent overgeneralization in mixed-label contexts, and applies evidence-aware confidence gating via a posterior lower bound, so that memory reuse scales with accumulated evidence rather than empirical accuracy alone. Across PrivacyLens+, ConFaide+, and AgentHarm, LiSA consistently outperforms strong memory-based baselines under sparse feedback, remains robust under noisy user feedback even at 20% label-flip rates, and pushes the latency--performance frontier beyond backbone model scaling. Ultimately, LiSA offers a practical path to secure AI agents against the unpredictable long tail of real-world edge risks.

---


### 140. [Intelligence Impact Quotient (IIQ): A Framework for Measuring Organizational AI Impact](https://arxiv.org/abs/2605.14455)

**<font color=#1a73e8>作者：</font>** Chandan Rajah, Neha Sengupta, Federico Castanedo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Intelligence Impact Quotient (IIQ) is a composite metric intended to quantify the depth to which AI systems are integrated into organizational work and their impact. Rather than treating access counts or aggregate token volume as sufficient evidence of impact, IIQ combines a novelty-weighted, time-decayed token stock with usage frequency, a grace-period recency gate, organizational leverage, task complexity, and autonomy. The formulation produces a raw Intelligence Adoption Index (IAI) and a normalized 0-1000 IIQ index for comparison between heterogeneous users and units. We also derive sub-daily update rules and a bounded interpretation layer for estimated efficiency and financial impact. The paper positions IIQ as a deployment-oriented measurement framework: a formal proposal for tracking AI embedding in workflows, not a direct measure of model capability or a substitute for causal productivity evaluation. Synthetic scenarios illustrate how the revised metric distinguishes between frequent low-leverage use, semantically repetitive prompting, and more autonomous, higher-consequence AI-assisted work.

---


### 141. [ClickRemoval: An Interactive Open-Source Tool for Object Removal in Diffusion Models](https://arxiv.org/abs/2605.14461)

**<font color=#1a73e8>作者：</font>** Ledun Zhang, Yatu Ji, Xufei Zhuang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing object removal tools often rely on manual masks or text prompts, making precise removal difficult for non-expert users in complex scenes and often leading to incomplete removal or unnatural background completion. To address this issue, we present ClickRemoval, an open-source interactive object removal tool built on pretrained Stable Diffusion models and driven solely by user clicks. Without additional training, hand-drawn masks, or text descriptions, ClickRemoval localizes target objects and restores the background through self-attention modulation during denoising. Experiments show that ClickRemoval achieves competitive results across quantitative metrics and user studies. We release a complete software package at this https URL under the Apache-2.0 license.

---


### 142. [Real2Sim in HOI: Toward Physically Plausible HOI Reconstruction from Monocular Videos](https://arxiv.org/abs/2605.14462)

**<font color=#1a73e8>作者：</font>** Yubo Zhao, Yujin Chai, Yunao Dong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering 4D human-object interaction (HOI) from monocular video is a key step toward scalable 3D content creation, embodied AI, and simulation-based learning. Recent methods can reconstruct temporally coherent human and object trajectories, but these trajectories often remain visual artifacts while failing to preserve stable contact, functional manipulation, or physical plausibility when used as reference motions for humanoid-object simulation. This reveals a fundamental interaction gap: HOI reconstruction should not stop at tracking a human and an object, but should recover the relation that makes their motion a coherent interaction. We introduce $\textbf{HA-HOI}$, a framework for reconstructing physically plausible 4D HOI animation from in-the-wild monocular videos. Instead of treating the human and object as independent entities in an ambiguous monocular 3D space, we propose a $\textit{human-first, object-follow}$ formulation. The human motion is recovered as the interaction anchor, and the object is reconstructed, aligned, and refined relative to the human action. The resulting kinematic trajectory is then projected into a physics-based humanoid-object simulation, where it acts as a teacher trajectory for stable physical rollout. Across benchmark and in-the-wild videos, $\textbf{HA-HOI}$ improves human-object alignment, contact consistency, temporal stability, and simulation readiness over prior monocular HOI reconstruction methods. By moving beyond visually plausible trajectory recovery toward physically grounded interaction animation, our work takes a step toward turning general monocular HOI videos into scalable demonstrations for humanoid-object behavior. Project page: this https URL

---


### 143. [From Table to Cell: Attention for Better Reasoning with TABALIGN](https://arxiv.org/abs/2605.14465)

**<font color=#1a73e8>作者：</font>** Tung Sum Thomas Kwok, Zeyong Zhang, Xinyu Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-step LLM reasoning over structured tables fails because planning and execution share no explicit cell-grounding contract. Existing methods constrain the planner to a left-to-right factorization at odds with table permutation invariance, and score intermediate states by generated content alone, overlooking cell grounding. We conduct a pilot study showing that diffusion language models (DLMs) produce more human-aligned and permutation-stable cell attention on tables than autoregressive models, with a 40.2% median reduction in attention-AUROC variability under row reordering. Motivated by this, we propose TABALIGN, a planned table reasoning framework that operationalizes the contract. TABALIGN pairs a masked DLM planner, whose bidirectional denoising emits plan steps as binary cell masks, with TABATTN, a lightweight verifier trained on 1,600 human-verified attention standards to score each step by its attention overlap with the plan-designated mask. Across eight benchmarks covering table question answering and fact verification, TABALIGN improves average accuracy by 15.76 percentage points over the strongest open-source baseline at comparable 8B-class scale, with a matched-backbone ablation attributing 2.87 percentage points of this gain to the DLM planner over an AR planner on a fixed reasoner. Cleaner DLM plans also accelerate downstream reasoning execution by 44.64%.

---


### 144. [Focused PU learning from imbalanced data](https://arxiv.org/abs/2605.14467)

**<font color=#1a73e8>作者：</font>** Elias Zavitsanos, Georgios Paliouras  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a new method of learning from positive and unlabeled (PU) examples in highly imbalanced datasets. Many real-world problems, such as disease gene identification, targeted marketing, fraud detection, and recommender systems, are hard to address with machine learning methods, due to limited labeled data. Often, training data comprises positive and unlabeled instances, the latter typically being dominated by negative, but including also several positive instances. While PU learning is well-studied, few methods address imbalanced settings or hard-to-detect positive examples that resemble negative ones. Our approach uses a focused empirical risk estimator, incorporating both positive and unlabeled examples to train binary classifiers. Empirical evaluations demonstrate state-of-the-art performance on imbalanced datasets under two labeling mechanisms - selecting positives completely at random (SCAR) and selecting at random (SAR). Beyond these controlled experiments, we demonstrate the value of the proposed method in the real-world application of financial misstatement detection.

---


### 145. [GeoVista: Visually Grounded Active Perception for Ultra-High-Resolution Remote Sensing Understanding](https://arxiv.org/abs/2605.14475)

**<font color=#1a73e8>作者：</font>** Jiashun Zhu, Ronghao Fu, Jiasen Hu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interpreting ultra-high-resolution (UHR) remote sensing images requires models to search for sparse and tiny visual evidence across large-scale scenes. Existing remote sensing vision-language models can inspect local regions with zooming and cropping tools, but most exploration strategies follow either a one-shot focus or a single sequential trajectory. Such single-path exploration can lose global context, leave scattered regions unvisited, and revisit or count the same evidence multiple times. To this end, we propose GeoVista, a planning-driven active perception framework for UHR remote sensing interpretation. Instead of committing to one zooming path, GeoVista first builds a global exploration plan, then verifies multiple candidate regions through branch-wise local inspection, while maintaining an explicit evidence state for cross-region aggregation and de-duplication. To enable this behavior, we introduce APEX-GRO, a cold-start supervised trajectory corpus that reformulates diverse UHR tasks as Global-Region-Object interactive reasoning processes with a unified, scale-invariant spatial representation. We further design an Observe-Plan-Track mechanism for global observation, adaptive region inspection, and evidence tracking, and align the model with a GRPO-based strategy using step-wise rewards for planning, localization, and final answer correctness. Experiments on RSHR-Bench, XLRS-Bench, and LRS-VQA show that GeoVista achieves state-of-the-art performance. Code and dataset are available at this https URL

---


### 146. [Test-Time Learning with an Evolving Library](https://arxiv.org/abs/2605.14477)

**<font color=#1a73e8>作者：</font>** Weijia Xu, Alessandro Sordoni, Chandan Singh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce EvoLib, a test-time learning framework that enables large language models to accumulate, reuse, and evolve knowledge across problem instances without parameter updates or external supervision. Instead of adapting model parameters, our approach maintains a shared library of knowledge abstractions, including modular skills and reflective insights, automatically extracted from the model's own inference trajectories. To support continual improvement, we introduce a principled weighting and consolidation mechanism that jointly optimizes for immediate utility and long-term value. This allows simple, instance-specific abstractions to evolve into more general and reusable ones over time. Across challenging benchmarks in mathematical reasoning, code generation, and multi-turn agentic environments, EvoLib improves substantially over the top test-time scaling and learning methods without ground-truth feedback.

---


### 147. [Cross-Linguistic Transcription and Phonological Representation in the Huìtóngguǎnxì Huáyíyìyǔ](https://arxiv.org/abs/2605.14480)

**<font color=#1a73e8>作者：</font>** Ji-eun Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Purpose: This study investigates the transcription principles underlying Huìtóngguǎnxì Huáyíyìyǔ (HHY), a series of multilingual glossaries compiled by the Ming government between the fifteenth and sixteenth centuries for interpreter training. The study treats HHY not as a collection of isolated language materials, but as a coherent multilingual transcription system representing spoken forms of non-Chinese languages through Chinese characters.
Methods: A substantial portion of HHY was digitized and aligned with Chinese phonological categories. Previous reconstructions of individual language sections were critically reviewed and integrated into a unified comparative database. The analysis focuses on cross-linguistic regularities in Main Transcription (MT) and Supplementary Transcription (ST) across eight language sections.
Results: MT generally represents sounds compatible with the Chinese syllable structure of the period, whereas ST mainly encodes phonetic features less compatible with Chinese phonology. The analysis further shows that Chinese phonological categories were used more flexibly in foreign-language transcription than previously assumed. HHY therefore functioned as a relatively systematic method of phonetic approximation rather than a direct projection of Chinese phonology onto non-Chinese languages.
Conclusion: HHY can be analyzed as an internally structured transcription system rather than merely as a collection of glossaries. More broadly, the study demonstrates that historical transcription systems can provide valuable evidence for historical phonology, particularly for under-documented Asian languages with limited historical records.

---


### 148. [LEMON: Learning Executable Multi-Agent Orchestration via Counterfactual Reinforcement Learning](https://arxiv.org/abs/2605.14483)

**<font color=#1a73e8>作者：</font>** Xudong Chen, Yixin Liu, Hua Wei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have become a strong foundation for multi-agent systems, but their effectiveness depends heavily on orchestration design. Across different tasks, role design, capacity assignment, and dependency construction jointly affect both solution quality and execution efficiency. Existing approaches automate parts of this design process, yet they often optimize these decisions partially or sequentially, and rely on execution-level feedback that provides limited credit assignment for local orchestration decisions. We propose LEMON (\textbf{L}earning \textbf{E}xecutable \textbf{M}ulti-agent \textbf{O}rchestratio\textbf{N} via Counterfactual Reinforcement Learning), an LLM-based orchestrator that generates an executable orchestration specification. The specification integrates task-specific roles, customized duties, capacity levels, and dependency structure into a single deployable system. To train the orchestrator, we augment the orchestration-level GRPO objective with a localized counterfactual signal that edits role, capacity, or dependency fields and applies the resulting reward contrast only to the edited spans. Experiments on six reasoning and coding benchmarks, including MMLU, GSM8K, AQuA, MultiArith, SVAMP, and HumanEval, show that LEMON achieves state-of-the-art performance among the evaluated multi-agent orchestration methods. Our code is available at this https URL.

---


### 149. [Reduce the Artifacts Bias for More Generalizable AI-Generated Image Detection](https://arxiv.org/abs/2605.14486)

**<font color=#1a73e8>作者：</font>** Yiheng Li, Yang Yang, Zichang Tan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As the misuse of AI-generated images grows, generalizable image detection techniques are urgently needed. Recent state-of-the-art (SOTA) methods adopt aligned training datasets to reduce content, size, and format biases, empowering models to capture robust forgery cues. A common strategy is to employ reconstruction techniques, e.g., VAE and DDIM, which show remarkable results in diffusion-based methods. However, such reconstruction-based approaches typically introduce limited and homogeneous artifacts, which cannot fully capture diverse generative patterns, such as GAN-based methods. To complement reconstruction-based fake images with aligned yet diverse artifact patterns, we propose a GAN-based upsampling approach that mimics GAN-generated fake patterns while preserving content, size, and format alignment. This naturally results in two aligned but distinct types of fake images. However, due to the domain shift between reconstruction-based and upsampling-based fake images, direct mixed training causes suboptimal results, where one domain disrupts feature learning of the other. Accordingly, we propose a Separate Expert Fusion (SEF) framework to extract complementary artifact information and reduce inter-domain interference. We first train domain-specific experts via LoRA adaptation on a frozen foundational model, then conduct decoupled fusion with a gating network to adaptively combine expert features while retaining their specialized knowledge. Rather than merely benefiting GAN-generated image detection, this design introduces diverse and complementary artifact patterns that enable SEF to learn a more robust decision boundary and improve generalization across broader generative methods. Extensive experiments demonstrate that our method yields strong results across 13 diverse benchmarks. Codes are released at: this https URL.

---


### 150. [Head Forcing: Long Autoregressive Video Generation via Head Heterogeneity](https://arxiv.org/abs/2605.14487)

**<font color=#1a73e8>作者：</font>** Jiahao Tian, Yiwei Wang, Gang Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video diffusion models support real-time synthesis but suffer from error accumulation and context loss over long horizons. We discover that attention heads in AR video diffusion transformers serve functionally distinct roles as local heads for detail refinement, anchor heads for structural stabilization, and memory heads for long-range context aggregation, yet existing methods treat them uniformly, leading to suboptimal KV cache allocation. We propose Head Forcing, a training-free framework that assigns each head type a tailored KV cache strategy: local and anchor heads retain only essential tokens, while memory heads employ a hierarchical memory system with dynamic episodic updates for long-range consistency. A head-wise RoPE re-encoding scheme further ensures positional encodings remain within the pretrained range. Without additional training, Head Forcing extends generation from 5 seconds to minute-level duration, supports multi-prompt interactive synthesis, and consistently outperforms existing baselines. Project Page: this https URL.

---


> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-337](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
