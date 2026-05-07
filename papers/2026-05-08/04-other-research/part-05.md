# 📦 其他研究 | 2026年05月08日

> 本类共 **270** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-270](./part-06.md)

---

### 201. [A Comparative Analysis of Machine Learning and Deep Learning Models for Tweet Sentiment Classification: A Case Study on the Sentiment140 Dataset](https://arxiv.org/abs/2605.04888)

**<font color=#1a73e8>作者：</font>** Vita Anggraini, Cintya Bella, Bastian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The exponential growth of social media has created an urgent need for automated systems to analyze unstructured public sentiment in real time. This study compares a traditional Logistic Regression model using TF-IDF features with a deep learning Bidirectional Long Short-Term Memory (BiLSTM) architecture on a 10,000-tweet subset of the Sentiment140 dataset. Experimental results show that Logistic Regression outperformed BiLSTM, achieving an accuracy of 73.5% compared with 69.17%, while the deep learning model exhibited mild overfitting. These findings suggest that for medium-scale informal text data, classical machine learning with robust feature extraction can outperform more complex deep learning approaches. Finally, the trained models were integrated into an interactive web application using Streamlit and deployed on Hugging Face Spaces for public access.

---


### 202. [Self-Attention as Transport: Limits of Symmetric Spectral Diagnostics](https://arxiv.org/abs/2605.04893)

**<font color=#1a73e8>作者：</font>** Dominik Dahlem, Diego Maniloff, Mac Misiura  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models hallucinate in predictable ways: attention routing fails by over-concentrating on a narrow set of positions, or by spreading so diffusely that relevance is diluted, and the shape of the failure carries diagnostic signal. A widely used family of spectral methods analyzes the symmetric component of the degree-normalized attention operator, which governs transport capacity; we prove that every transpose-invariant spectral diagnostic of this operator is structurally orientation-blind (it cannot distinguish an operator from its transpose, and therefore cannot detect information-flow direction), with a quantitative converse establishing the asymmetry coefficient $G$ as the unique control parameter for direction.
Pairing this with a closed-form bipartite-Cheeger landscape for canonical causal architectures, we show that uniform causal attention satisfies an $n$-independent floor $\phi \ge 1/5$ with worst cut at $t^\ast/n \approx 0.32$, while window attention pierces the floor as $O(w/n)$; failure modes are shape-different, not just value-different. The resulting two-axis diagnostic ($\phi$ for capacity, $G$ for direction) yields a falsifiable polarity prediction: bottleneck- and diffuse-dominated benchmarks should exhibit opposite polarity. Under length-controlled evaluation, transport features retain interpretable signal (LC-AUROC from 0.62 to 0.84) on tested models up to 8B parameters, with polarity reversing as predicted between HaluEval and MedHallu.

---


### 203. [Regime-Conditioned Evaluation in Multi-Context Bayesian Optimization](https://arxiv.org/abs/2605.04895)

**<font color=#1a73e8>作者：</font>** Noel Thomas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Published transfer-BO comparisons often estimate an average treatment effect of acquisition choice over hidden regime variables, while practitioners need the conditional effect for their specific prior quality, budget ratio, and metric. An audit of 40 transfer-BO papers from NeurIPS, ICML, ICLR, AISTATS, UAI, TMLR, JMLR, and AutoML-Conf (2022-2025) finds that 98% never vary B/|A| as a controlled axis. On the same GDSC2 benchmark, changing only the budget reverses the ranking: at B=50, Greedy outperforms UCB by 0.050 Hit@1, while at B=100, UCB outperforms Greedy by 0.035. We capture this transition with the Portable Regime Score PRS=(B/|A|)(1-rho), where rho is the prior rank correlation and can be estimated from pilot contexts before the main comparison. Across 79 conditions spanning chemistry, drug-response biology, and HPO, a hierarchical model gives beta=0.50 (p=1.1e-9), and 19% of conditions fall in an equivalence zone where |advantage|<0.01 Hit@1. In five published reversal cases, PRS predicts the winner from pre-comparison observables. A No-Free-Leaderboard proposition explains why unconditional rankings are unstable: when CATE changes sign across regimes, the reported ATE becomes a function of benchmark mixture. RegimePlanner, which estimates rho online and switches acquisition accordingly, wins all 16 HPO-B search spaces at B=100 and exceeds the matched {Greedy,UCB} per-context oracle on GDSC2 by 18%. Pre-registered predictions achieve 27/40=67.5% overall accuracy and above 90% within EMA prior families. The practical protocol is simple: report B/|A|, rho, K, and metric alongside any claimed acquisition advantage.

---


### 204. [On the (In-)Security of the Shuffling Defense in the Transformer Secure Inference](https://arxiv.org/abs/2605.04901)

**<font color=#1a73e8>作者：</font>** Zhengyi Li, Yakai Wang, Kang Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> For Transformer models, cryptographically secure inference ensures that the client learns only the final output, while the server learns nothing about the client's input. However, securely computing nonlinear layers remains a major efficiency bottleneck due to the substantial communication rounds and data transmission required. To address this issue, prior works reveal intermediate activations to the client, allowing nonlinear operations to be computed in plaintext. Although this approach significantly improves efficiency, exposing activations enables adversaries to extract model weights. To mitigate this risk, existing works employ a shuffling defense that reveals only randomly permuted activations to the client. In this work, we show that the shuffling defense is not as robust as previously claimed. We propose an attack that aligns differently shuffled activations to a common permutation and subsequently exploits them to extract model weights. Experiments on Pythia-70m and GPT-2 demonstrate that the proposed attack can align shuffled activations with mean squared errors ranging from $10^{-9}$ to $10^{-6}$. With a query cost of approximately \$1, the adversary can recover model weights with L1-norm differences ranging from $10^{-4}$ to $10^{-2}$ compared to the oracle weights.

---


### 205. [Exploring Clustering Capability of Inpainting Model Embeddings for Pattern-based Individual Identification](https://arxiv.org/abs/2605.04904)

**<font color=#1a73e8>作者：</font>** Jens van Bijsterveld, Daniele Avitabile, Fons J. Verbeek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we explore deep learning techniques for individual identification of animals based on their skin patterns. Individual identification is crucial in biodiversity monitoring, since it enables analysis of decline or growth of populations, or intra-species interactions within populations. Models trained for the task of individual identification often do not focus on the skin pattern of animals, but on background details or body shape details. These characteristics are not individually specific, or can change drastically through time. We focus on techniques that will make machine learning models more responsive to skin pattern structure when extracting individual visual embeddings from images. For this, we explore image inpainting of task-specific masks as an auxiliary task to enhance ML-based individual identification from animal skin patterns. We propose a comparative analysis among four models as an encoder backbone for the individual identification task. We focus on the case study of zebrafish, which is a widely recognized biological model organism, and which exhibits individually identifying skin patterns. To evaluate encoder backbone performance, we present standard metrics for classification accuracy, embedding clustering metrics, and GradCAM visualizations.

---


### 206. [Cross-Model Consistency of Feature Importance in Electrospinning: Separating Robust from Model-Dependent Features](https://arxiv.org/abs/2605.04905)

**<font color=#1a73e8>作者：</font>** Mehrab Mahdian, Ferenc Ender, Tamas Pardy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electrospinning is a highly sensitive fabrication process in which small variations in operating parameters can significantly influence fiber morphology and material performance. Machine learning (ML) methods are increasingly employed to model these process-structure relationships and to identify the relative importance of processing variables. However, most existing studies rely on a single ML model, implicitly assuming that the resulting feature importance is robust and reproducible. In this study, the consistency of feature importance across multiple ML model families was systematically evaluated using a curated dataset of 96 polyvinyl alcohol (PVA) electrospinning experiments. Twenty-one ML models representing linear, tree-based, kernel-based, neural network, and instance-based approaches were trained and compared. To provide a unified interpretability framework, SHAP (SHapley Additive exPlanations) values were used to calculate feature importance consistently across all models. A rank-based statistical analysis was then performed to quantify inter-model agreement and assess the robustness of parameter rankings. The results demonstrate that predictive performance and interpretive reliability are fundamentally distinct properties. Although several models achieved comparable predictive accuracy, substantial differences were observed in their feature importance rankings. Solution concentration emerged as the most robust and consistently influential parameter (variability = 0), whereas flow rate and applied voltage exhibited high ranking variability (variability > 0.9), indicating strong model dependence. These findings suggest that feature importance derived from a single ML model may be unreliable, particularly for small experimental datasets, and highlight the importance of cross-model validation for achieving trustworthy interpretation in ML-assisted electrospinning research.

---


### 207. [Koopman Identification of Nonlinear Systems via Reservoir Liftings](https://arxiv.org/abs/2605.04917)

**<font color=#1a73e8>作者：</font>** Weibin Gu, Chen Yang, Lu Shi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning tractable linear representations of nonlinear dynamical systems via Koopman operator theory is often hindered by dictionary selection, temporal memory encoding, and numerical ill-conditioning. Inspired by Reservoir Computing (RC) paradigm, this paper introduces the RC-Koopman framework, which interprets reservoir as a stateful, finite-dimensional Koopman dictionary whose temporal depth is explicitly controlled by its spectral radius. We show that the Echo State Property (ESP) guarantees well-posedness and favorable numerical conditioning of the lifted Koopman approximation. A correlation-based spectral radius selection algorithm aligns reservoir memory with dominant system timescales. Analysis reveals how the finite memory of the reservoir determines which Koopman eigenfunctions remain observable from the lifted features. Evaluation on synthetic benchmarks demonstrates that RC-Koopman achieves a favorable balance between reconstruction accuracy of the underlying nonlinear dynamics and dynamical stability, compared to Extended Dynamic Mode Decomposition (EDMD) and Hankel-based lifting approaches. Code available at: this https URL

---


### 208. [Reinforcement Learning for Compositional Generalization with Outcome-Level Optimization](https://arxiv.org/abs/2605.04920)

**<font color=#1a73e8>作者：</font>** Xiyan Fu, Wei Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Compositional generalization refers to correctly interpret novel combinations of known primitives, which remains a major challenge. Existing approaches often rely on supervised fine-tuning, which encourages models to imitate target outputs. This token-level training paradigm fails to capture the global compositional structure required for generalizing to unseen combinations. In this work, we investigate whether compositional generalization can instead be improved through outcome-level reinforcement learning. We adopt Group Relative Policy Optimization to optimize models based on feedback on their final outputs. Within this framework, we explore both a simple binary outcome reward and a composite reward that provides additional composition feedback. Experiments on multiple compositional benchmarks show that reinforcement learning improves compositional generalization compared to supervised fine-tuning. Further analysis reveals that supervised models tend to overfit frequent training compositions, whereas reinforcement learning improves compositional generalization by reshaping the output distribution, particularly for more complex composition types.

---


### 209. [Evolving Idea Graphs with Learnable Edits-and-Commits for Multi-Agent Scientific Ideation](https://arxiv.org/abs/2605.04922)

**<font color=#1a73e8>作者：</font>** Jiangwen Dong, Bo Li, Wanyu Lin  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> LLM-empowered multi-agent systems offer new potential to accelerate scientific discovery by generating novel research ideas. However, existing methods typically coordinate agents through temporary texts, such as drafts or chat logs; it is difficult to pinpoint the weaknesses in the generated ideas and how the agents refine them. To this end, we introduce \textbf{Evolving Idea Graphs} (EIG), a graph-based multi-agent scientific ideation framework that can generate high-performance research ideas across various benchmark-native metrics, such as novelty, feasibility, and clarity. Instead of coordinating solely through texts, EIG represents a partially formed proposal as an evolving idea graph, where nodes capture scientific claims and edges encode relations (e.g., support and conflict), enabling unresolved weaknesses to remain identifiable throughout the idea evolving process. Specifically, a learned two-head controller operates over the evolving graph to guide the ideation: one head selects graph edits for agents to execute, while the other decides when the graph is ready for commit as final proposal synthesis. On AI Idea Bench 2025 and LiveIdeaBench, EIG outperforms all compared systems on both automatic benchmark scores and blind expert ratings. Ablations further show that explicit graph state provides the main performance gains, and learned edit-and-commit control adds consistent improvements.

---


### 210. [Unintended Negative Impacts of Promotional Language in Patent Evaluation](https://arxiv.org/abs/2605.04926)

**<font color=#1a73e8>作者：</font>** Bingkun Zhao, Chenwei Zhang, Hao Peng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Promotional language has been increasingly used to aid the communication of innovative ideas in science. Yet, less is known about its role in the context of technological innovation. Here, we use a validated and domain-diagnosed lexicon of 135 promotional words to study the association between promotional language and patent evaluation outcomes among 2.7 million USPTO patent applications. Our large-scale study reveals three unexpected findings. First, in contrast to scientific evaluation, we find that a higher frequency of promotional words is negatively associated with the probability of an application being (i) granted a patent, (ii) transferred ownership, and (iii) successfully appealed. This promotional penalty holds even after accounting for a range of confounding factors and is largely robust across different technological areas. Among matched samples, the difference in the success rate between the lowest and highest promotional density quintile is 5.5, 5.9, and 5.3 percentage points for patentability, transferability, and rejection reversal. Second, contrary to institutional skepticism, we show that promotional language is not a mask of weak technology, but objectively reflects the degree of combinatorial novelty and future citation impact. Third, digging into the mechanisms, we find that the tolerance to promotional framing is strongly moderated by human factors, with men and experienced examiners showing a higher acceptance of promotional narratives than women and novice examiners. By revealing an emerging paradox in the patent system, our study offers theoretical and practical implications for improving patent evaluation through more objective scrutiny of linguistic patterns in patent filings.

---


### 211. [When Does Gene Regulatory Network Inference Break? A Controlled Diagnostic Study of Causal and Correlational Methods on Single-Cell Data](https://arxiv.org/abs/2605.04930)

**<font color=#1a73e8>作者：</font>** Miguel Fernandez-de-Retana, Ruben Sanchez-Corcuera, Unai Zulaika 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite theoretical advantages, causal methods for Gene Regulatory Network (GRN) inference from single-cell RNA-seq data consistently fail to match or outperform correlation-based baselines in many realistic benchmarks, a persistent puzzle which casts doubt on the value of causality for this task. We argue that existing benchmarks are insufficiently controlled to answer this question because they evaluate on real or semi-real data where multiple pathologies co-occur, confounding failure modes, and obscuring the specific conditions under which different inference methods excel or fail. To address this gap, we introduce a controlled diagnostic framework that isolates seven biologically motivated pathologies (dropout, latent confounders, cell-type mixing, feedback loops, network density, sample size, and pseudotime drift) and measure how six representative methods spanning three inference paradigms degrade as each pathology intensifies. Across 6,120 controlled experiments, we find that causal methods genuinely dominate in clean and structurally favorable regimes, but specific pathologies (notably dropout and latent confounders) selectively neutralize their advantages. We further introduce an error-type decomposition that reveals methods with similar aggregate accuracy commit qualitatively different errors. To probe whether single-pathology effects persist when multiple stressors co-occur, we perform an interaction sweep over the three most impactful pathologies and find that their joint effects are sub-additive, while also exposing density-conditional cross-overs invisible to single-dial analysis. Our findings offer a nuanced understanding of when and why different methods succeed or fail for GRN inference, providing actionable insights for method development and practical guidance for practitioners.

---


### 212. [UFAL-CUNI at SemEval-2026 Task 11: An Efficient Modular Neuro-symbolic Method for Syllogistic Reasoning](https://arxiv.org/abs/2605.04941)

**<font color=#1a73e8>作者：</font>** Ivan Kartáč, Kristýna Onderková, Jan Bronec 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper describes our system submitted to SemEval-2026 Task 11: Disentangling Content and Formal Reasoning in Large Language Models. We present an efficient modular neuro-symbolic approach, combining a symbolic prover with small reasoning LLMs (4B parameters). The system consists of an LLM-based parser that translates natural language syllogisms to a first-order logic (FOL) representation, an automated theorem prover, and two optional modules: machine translation for multilingual inputs and a symbolic retrieval component for the identification of relevant premises. The system achieves competitive accuracy and relatively low content effect on most subtasks. Our ablations show that this approach outperforms LLM-based zero-shot baselines in this parameter size range, but also reveal limited multilingual capabilities of small LLMs. Finally, we include a discussion of the task's main ranking metric and analyze its limitations.

---


### 213. [Training-Time Batch Normalization Reshapes Local Partition Geometry in Piecewise-Affine Networks](https://arxiv.org/abs/2605.04946)

**<font color=#1a73e8>作者：</font>** Xuan Qi, Yi Wei, Fanqi Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Batch normalization (BN) is central to modern deep networks, but its effect on the realized function during training remains less understood than its optimization benefits. We study training-time BN in continuous piecewise-affine (CPA) networks through the geometry of switching hyperplanes and the induced affine-region partition. Conditioned on a mini-batch, we show that BN defines for each neuron a reference hyperplane through the batch centroid, and that breakpoint-switching hyperplanes are parallel translates whose offsets are expressed in batch-standardized coordinates and are independent of the raw bias. This yields an exact criterion for when a switching hyperplane intersects a local $\ell_\infty$ window and motivates a local region-density functional based on exact affine-region counts. Under explicit sufficient conditions, we show that BN increases expected local partition refinement in ReLU and more general piecewise-affine networks, and that this mechanism transfers locally through depth inside parent affine regions where the upstream representation map is an affine embedding. These results provide a function-level geometric account of training-time BN as a batch-conditional recentering mechanism near the data.

---


### 214. [Adaptive Inverted-Index Routing for Granular Mixtures-of-Experts](https://arxiv.org/abs/2605.04952)

**<font color=#1a73e8>作者：</font>** Klaus-Rudolf Kladny, Maximilian Mordig, Bernhard Schölkopf 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-experts (MoE) models enable scalable transformer architectures by activating only a subset of experts per token. Recent evidence suggests that performance improves with increasingly granular experts, i.e., many small experts instead of a few large ones. However, this regime substantially increases routing cost, which can dominate computation. We introduce adaptive inverted-index routing for MoE (AIR-MoE), an inverted-index-inspired routing architecture based on vector quantization (VQ). In a first stage, AIR-MoE performs coarse shortlisting by assigning tokens to VQ codewords to construct a candidate set of experts. In a second stage, fine scoring computes exact routing scores restricted to this shortlist. This two-stage procedure approximates true top-k routing while avoiding full expert scoring and, in contrast to prior work, imposing no structural constraints on expert parameters. AIR-MoE serves as a drop-in replacement for standard routers and requires no modifications to the model architecture or loss function. We further provide a lower bound on the mass recall achieved by AIR-MoE that yields insights into its inner workings. Empirically, we demonstrate that AIR-MoE achieves improved performance compared to existing routing approaches in granular MoE settings.

---


### 215. [Order-based Rehearsal Learning](https://arxiv.org/abs/2605.04955)

**<font color=#1a73e8>作者：</font>** Yu-Xuan Tao, Tian-Zuo Wang, Zhi-Hua Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When a machine learning (ML) model forecasts an undesired event, one often seeks a decision to avoid it, known as the avoiding undesired future (AUF) problem. Many rehearsal learning methods have been proposed for AUF, but they rely on an underlying graph structure; learning such a graph from observational data is challenging and can incur substantial estimation error. In this work, we demonstrate that the order structure can be sufficient for AUF decision-making, and propose the first order-based rehearsal learning method. Although an order is less informative than a graph, it can be sufficient to identify the influence of decisions from observational data, suggesting that learning the entire graph is not always necessary. To learn the order, we develop an information-theoretic method that imposes no restrictions on the form of structural functions or the type of noise distributions. For AUF decision-making, we construct an order-based sampler to approximate the influence of decisions and, combined with a surrogate objective for maximizing the post-decision success probability, reduce the AUF task to a differentiable optimization problem. Experiments show that our order learning method outperforms existing methods, and that our AUF approach not only surpasses methods relying on learned graphs or learned orders, but also matches or even exceeds oracle baselines that are given the true graph.

---


### 216. [Delving into Non-Exchangeability for Conformal Prediction in Graph-Structured Multivariate Time Series](https://arxiv.org/abs/2605.04957)

**<font color=#1a73e8>作者：</font>** Ruichao Guo, Xingyao Han, Luo Wenshui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Point forecasting for graph-structured multivariate time series is a fundamental problem, but rigorous uncertainty quantification for such predictions is still underexplored. Conformal prediction (CP) offers uncertainty estimation with a solid coverage guarantee under the exchangeability assumption, which requires the joint data distribution to be unchanged under permutation. However, in graph-structured time series, inherent cross-node coupling can violate the exchangeability condition, making direct application of CP unreliable. Inspired by the spectral graph theory, such coupling resides in global trends and can be characterized by the low-frequency components, while high-frequency components are nearly exchangeable. Therefore, we propose a novel concept named Spectral Graph Conditional Exchangeability (SGCE), which conditions exchangeable high-frequency components on low-frequency ones to preserve global trends and enable effective CP in the spectral domain. Based on SGCE, we further propose Spectral Conformal prediction via wAveLEt transform (SCALE). SCALE uses graph wavelets to decompose low/high-frequency components and conformalizes high-frequency residuals via adaptive gating over a low-frequency embedding. Experimental results on real-world traffic datasets show that SCALE not only achieves valid coverage but also consistently improves the coverage-efficiency trade-off over the state-of-the-art CP methods.

---


### 217. [EP-GRPO: Entropy-Progress Aligned Group Relative Policy Optimization with Implicit Process Guidance](https://arxiv.org/abs/2605.04960)

**<font color=#1a73e8>作者：</font>** Song Yu, Li Li, Wenwen Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR), particularly Group Relative Policy Optimization (GRPO), has advanced LLM reasoning. However, GRPO suffers from three credit assignment failures: uniform token-level granularity that ignores heterogeneous informational value, uniform polarity that penalizes correct steps and rewards incorrect ones, and zero-variance collapse that erases outcome-driven gradients. We systematically quantify these failures, revealing highly non-uniform token informativeness, widespread step-level polarity misalignment, and substantial training waste.
To address these limitations, we propose Entropy-Progress Aligned GRPO (EP-GRPO), a framework that mines the model's intrinsic information flow for dense, self-supervised guidance. EP-GRPO integrates entropy-gated modulation to prioritize high entropy decision pivots, implicit process signals from policy divergence anchored to outcome advantages for directional token-level feedback without external reward models, and cumulative entropy mapping that enables progress-aligned advantage normalization, naturally maintaining gradient flow under zero reward variance.
Extensive experiments on mathematical reasoning benchmarks demonstrate that EP-GRPO achieves superior accuracy and efficiency compared to GRPO and its variants. The code will be available.

---


### 218. [TabEmbed: Benchmarking and Learning Generalist Embeddings for Tabular Understanding](https://arxiv.org/abs/2605.04962)

**<font color=#1a73e8>作者：</font>** Minjie Qiang, Mingming Zhang, Xiaoyi Bao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Foundation models have established unified representations for natural language processing, yet this paradigm remains largely unexplored for tabular data. Existing methods face fundamental limitations: LLM-based approaches lack retrieval-compatible vector outputs, whereas text embedding models often fail to capture tabular structure and numerical semantics. To bridge this gap, we first introduce the Tabular Embedding Benchmark (TabBench), a comprehensive suite designed to evaluate the tabular understanding capability of embedding models. We then propose TabEmbed, the first generalist embedding model that unifies tabular classification and retrieval within a shared embedding space. By reformulating diverse tabular tasks as semantic matching problems, TabEmbed leverages large-scale contrastive learning with positive-aware hard negative mining to discern fine-grained structural and numerical nuances. Experimental results on TabBench demonstrate that TabEmbed significantly outperforms state-of-the-art text embedding models, establishing a new baseline for universal tabular representation learning. Code and datasets are publicly available at this https URL and this https URL.

---


### 219. [Reliable Modeling of Distribution Shifts via Displacement-Reshaped Optimal Transport](https://arxiv.org/abs/2605.04965)

**<font color=#1a73e8>作者：</font>** Philip Naumann, Jacob Kauffmann, Klaus-Robert Müller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimal transport (OT) is a central framework for modeling distribution shifts. Because OT compares distributions directly in input space, a well-designed ground metric between observations is essential to ensure that the optimizer does not violate the true geometry of change. We propose Displacement-Reshaped Optimal Transport (ReshapeOT), a method that reshapes the ground metric by integrating observed sample displacements as an additional source of knowledge. Technically, ReshapeOT replaces the Euclidean metric with a Mahalanobis distance estimated from displacement second moments. This effectively carves expressways through the input space, inviting transport solutions that better align with observed displacements. Our method is computationally lightweight, integrates seamlessly into any OT solver that operates on a cost matrix, and can be kernelized for further flexibility. Experiments on synthetic and real-world data show that ReshapeOT achieves substantial gains in transport reliability. We further demonstrate our method's usefulness in two practical use cases.

---


### 220. [Skill Neologisms: Towards Skill-based Continual Learning](https://arxiv.org/abs/2605.04970)

**<font color=#1a73e8>作者：</font>** Antonin Berthon, Nicolas Astorga, Mihaela van der Schaar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern LLMs show mastery over an ever-growing range of skills, as well as the ability to compose them flexibly. However, extending model capabilities to new skills in a scalable manner is an open-problem: fine-tuning and parameter-efficient variants risk catastrophic forgetting, while context-based approaches have limited expressiveness and are constrained by the model's effective context. We explore skill neologisms--i.e., soft tokens integrated in the model's vocabulary and optimized to improve capabilities over a specific skill--as a way to selectively extend model capabilities to new skills without weight updates. We first observe that off-the-shelf pre-trained LLMs already demonstrate tokens associated with procedural knowledge. We then show that skill neologisms can be learned to improve model capabilities on specific skills while being composable with out-of-distribution skills, and that independently trained skill neologisms can be composed zero-shot. These results suggest that skill neologisms may provide a scalable path towards skill-based continual learning.

---


### 221. [Why Geometric Continuity Emerges in Deep Neural Networks: Residual Connections and Rotational Symmetry Breaking](https://arxiv.org/abs/2605.04971)

**<font color=#1a73e8>作者：</font>** Kyungwon Jeong, Won-Gi Paeng, Honggyo Suh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weight matrices in deep networks exhibit geometric continuity -- principal singular vectors of adjacent layers point in similar directions. While this property has been widely observed, its origin remains unexplained. Through experiments on toy MLPs and small transformers, we identify two mechanisms: residual connections create cross-layer gradient coherence that aligns weight updates across layers, and symmetry-breaking nonlinearities constrain all layers to a shared coordinate frame, preventing the rotation drift that would otherwise destabilize weight structure. Crucially, a nonlinear but rotation-preserving activation fails to retain continuity, isolating symmetry breaking -- not nonlinearity itself -- as the active ingredient. Activation and normalization play distinct roles: activation concentrates continuity in the leading singular direction, while normalization distributes it across multiple directions. In transformers, continuity is projection-specific: Q, K, Gate, and Up (which read from the residual stream) develop input-space ($\mathbf{v}_1$) continuity; O and Down (which write to it) develop output-space ($\mathbf{u}_1$) continuity; V alone, lacking an adjacent nonlinearity, develops only low continuity.

---


### 222. [Probabilistic Atomic Swaps for Bitcoin and Friends](https://arxiv.org/abs/2605.04975)

**<font color=#1a73e8>作者：</font>** Paul Gerhart, Jay Taylor, Sri Aravinda Krishnan Thyagarajan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Atomic swaps are a fundamental primitive for the trustless exchange of digital assets across blockchains: they guarantee that either both parties receive the agreed assets or neither party transfers. While this all-or-nothing guarantee is powerful, it also imposes an inherent determinism that rules out exchanges whose intended outcome is probabilistic. As a result, existing atomic swaps cannot realize trustless exchanges in which one party pays for a fixed chance of receiving a larger asset or reward, as in lotteries, randomized allocation mechanisms, and probabilistic cross-chain trades.
We introduce probabilistic swaps, a new cryptographic primitive that extends atomic swaps to the probabilistic setting. In a probabilistic swap, one party's transfer is executed with a fixed, publicly specified probability embedded in the protocol and cannot be biased by either party. This yields a trustless mechanism for randomized exchange with verifiable odds and no trusted intermediary.
Our construction combines adaptor signatures with oblivious pseudorandom functions (OPRFs) to realize the desired probabilistic outcome while ensuring that neither party can predict or bias it in advance. Along the way, we introduce a new mechanism for the atomic exchange of OPRF evaluations for payments, which may be of independent interest. A key feature of our approach is that it preserves the minimal on-chain footprint of modern atomic-swap protocols. The protocol relies only on standard Bitcoin scripts, such as digital signatures and timelocks, and is deployable on any blockchain that already supports atomic swaps. Consequently, probabilistic swaps are indistinguishable from ordinary on-chain transactions, which helps preserve privacy and fungibility. We provide formal security foundations and demonstrate practicality through a probabilistic swap in the Bitcoin testnet and in the Lightning Network.

---


### 223. [ICPR 2026 Competition on Privacy-Preserving Person Re-Identification from Top-View RGB-Depth Camera (TVRID)](https://arxiv.org/abs/2605.04977)

**<font color=#1a73e8>作者：</font>** Raphaël Delécluse, Hazem Wannous, Laurent Guimas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This companion paper reports the ICPR 2026 TVRID competition on privacy-aware top-view person re-identification. We present the competition setting, the released RGB-Depth dataset, and a summary of final results with descriptions of the top entries. TVRID contains 86 identities captured by four synchronized overhead Intel RealSense D455 cameras, with paired RGB/Depth streams and structured geometric variation across flat, ascent, descent, and oblique viewpoints. The evaluation protocol includes three tracks: RGB Re-ID, Depth Re-ID, and RGB$\leftrightarrow$Depth cross-modal retrieval. Submissions are ranked using mAP and CMC-1 under a unified server-side evaluation. The final results show a clear difficulty ordering (RGB $>$ Depth $>$ Cross-Modal), highlighting both the challenge of modality-constrained retrieval and the feasibility of strong performance with modality-invariant learning. By releasing the dataset at this https URL, the evaluation scripts at this https URL, and the accompanying documentation, TVRID establishes a reproducible benchmark for top-view, depth-based, and cross-modal person re-id.

---


### 224. [On-line Learning in Tree MDPs by Treating Policies as Bandit Arms](https://arxiv.org/abs/2605.04979)

**<font color=#1a73e8>作者：</font>** Anvay Shah, Ramsundar Anandanarayanan, Sharayu Moharir 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A Tree Markov Decision Problem (T-MDP) is a finite-horizon MDP with a starting state $s_{1}$, in which every state is reachable from $s_{1}$ through exactly one state-action trajectory. T-MDPs arise naturally as abstractions of decision making in sequential games with perfect recall, against stationary opponents. We consider the problem of on-line learning in T-MDPs, both in the PAC and the regret-minimisation regimes. We show that well-known bandit algorithms -- \textsc{Lucb} and \textsc{Ucb} -- can be applied on T-MDPs by treating each policy as an arm. The apparent technical challenge in this approach is that the number of policies is exponential in the number of states. Our main innovation is in the design of confidence bounds based on data shared by the policies, so that the bandit algorithms can yet be implemented with polynomial memory and per-step computation. We obtain instance-dependent upper bounds on sample complexity and regret that sum a ``gap term'' from every terminal state, rather than every policy. Empirically, our algorithms consistently outperform available alternatives on a suite of hidden-information games.

---


### 225. [Conceptors for Semantic Steering](https://arxiv.org/abs/2605.04980)

**<font color=#1a73e8>作者：</font>** Ilias Triantafyllopoulos, Young-Min Cho, Ren Tao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation-based steering provides control of LLM behavior at inference time, but the dominant paradigm reduces each concept to a single direction whose geometry is left largely unexamined. Rather than selecting a single steering direction, we use conceptors: soft projection matrices estimated from activations pooled across both poles of a bipolar concept, which preserve the concept's full multidimensional subspace. A geometric analysis shows the bipolar subspace strictly subsumes the single-vector baseline. We further show that the conceptor quota provides a parameter-free layer-selection diagnostic, predicting concept separability with Pearson correlations up to r=0.96 across three instruction-tuned models and three semantic dimensions. Beyond selection, conceptors admit a closed-form Boolean algebra (AND, OR, NOT): we evaluate conceptor compositionality on thematically related sub-concepts. Across a systematic five-axis design-space evaluation, conceptors match or outperform additive baselines at layers where concept subspaces are multi-dimensional while producing substantially fewer degenerate outputs. Conceptor steering is a geometrically principled, compositional, and practically safer alternative to single-direction steering from a limited number of contrastive pairs.

---


### 226. [Attention-Based Chaotic Self-Supervision for Medical Image Classification](https://arxiv.org/abs/2605.04985)

**<font color=#1a73e8>作者：</font>** Joao Batista Florindo, Amanda Pontes de Oliveira Ornelas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models for medical image classification usually achieve promising results but typically rely on large, annotated datasets or standard transfer learning from ImageNet. Self-Supervised Learning (SSL) has emerged as a powerful alternative, yet common methods like masked autoencoders (MAEs) may inadvertently destroy fine-grained diagnostic features by using random masking. In this paper, we propose a novel SSL pre-training strategy, the Chaotic Denoising Autoencoder (CDAE). Instead of masking, we apply a chaotic transformation to the input image, tasking an autoencoder to reconstruct the original. We hypothesize this forces the encoder to learn robust, domain-specific features by "inverting the chaos". Furthermore, we propose an attentive fusion mechanism that combines features from our CDAE-trained encoder with a standard encoder, leveraging the strengths of both general and domain-specific representations. Our method is evaluated on two public medical datasets: ISIC 2018 (skin lesions) and APTOS 2019 (diabetic retinopathy). The proposed model achieves high performance, with an accuracy of 0.9221 and an F1-macro of 0.8530 on ISIC 2018, and an accuracy of 0.8644 and F1-macro of 0.7433 on APTOS 2019, demonstrating the efficacy of our approach.

---


### 227. [Federated Learning for Early Prediction of EV Charging Demand](https://arxiv.org/abs/2605.04993)

**<font color=#1a73e8>作者：</font>** Vasilis Perifanis, Foteini Nikolaidou, Nikolaos Pavlidis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate forecasting of electric vehicle (EV) charging demand is critical for grid stability, infrastructure planning, and real-time charging optimization. In this work, we study the problem of early prediction of charging demand, where the total energy of a session is estimated using only information available at plug-in time and during the first minutes of charging. This enables actionable decisions while the session is still in progress, which is of direct importance for EV network operators. We construct a session-level dataset from the Adaptive Charging Network (ACN), combining session metadata with early-window charging measurements, and derive tabular features capturing user intent, temporal patterns, and initial charging behavior. We focus on a single operational depot, Caltech, and model intra-depot heterogeneity through station-level client partitions while evaluating multiple model families in a federated learning (FL) setting. Our results show that federated models can approach centralized predictive performance while keeping data in-depot, enabling privacy-enhanced training across distributed charging infrastructures. Overall, we demonstrate that reliable demand estimates can be obtained early in the session with minimal data, and that FL provides a practical pathway toward scalable and privacy-aware analytics for EV charging networks. Code is available at this https URL.

---


### 228. [DualTCN: A Physics-Constrained Temporal Convolutional Network for 2 Time-Domain Marine CSEM Inversion](https://arxiv.org/abs/2605.04997)

**<font color=#1a73e8>作者：</font>** Khaled Ahmed, Ghada Omar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> DualTCN is the first deep-learning framework for inverting time-domain marine controlled-source electromagnetic (MCSEM) transient data. Moving away from traditional subsurface discretization, the framework regresses four earth-model parameters -- $\sigma_1$, $\sigma_2$, $d_1$, $d_2$ -- and reconstructs conductivity-depth profiles using a differentiable soft-step decoder. The optimized architecture (379K parameters) features a Temporal Convolutional Network (TCN) encoder paired with a late-time branch and an auxiliary seafloor-depth head. This design achieves a 25.3\% loss reduction over baseline models, with high predictive accuracy ($R^2 = 0.898$ for $\sigma_2$) and an inversion speed of 3.5~ms per sample on an A100 GPU.
The framework demonstrates high robustness to noise through curriculum-based amplitude augmentation, maintaining a mean $\bar{R}^2$ of 0.858 at $\pm2\%$ random amplitude error, compared to $0.363$ without augmentation. DualTCN generalizes effectively to three-layer extensions (seawater/resistive layer/basement), accurately resolving basement conductivity ($R^2 \approx 0.88$), though thin-layer resolution remains a physical limitation ($R^2 \approx 0.23$).
In comparative benchmarks, DualTCN significantly outperforms traditional local optimization methods like Levenberg-Marquardt and L-BFGS-B, yielding a mean $\bar{R}^2 = 0.877$ versus 0.129-0.439 for multi-start baselines, while operating at up to 21,000$\times$ lower computational cost. Finally, the framework incorporates uncertainty quantification via Monte Carlo (MC) Dropout. While well-calibrated for $\sigma_1$ (PICP90 = 0.944), inherent signal limitations at short offsets (200m) lead to under-coverage for $d_2$ (PICP90 = 0.572), which can be mitigated through post-hoc temperature scaling or split conformal prediction.

---


### 229. [Learned Neighbor Trust for Collaborative Deployment in Model-Agnostic Decentralized Learning](https://arxiv.org/abs/2605.05009)

**<font color=#1a73e8>作者：</font>** Michael Lanier, Luise Ge, Sastry Kompella 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many decentralized distillation methods are designed around training-time coordination, yet deploy each node in isolation even when more capable neighbors remain available at inference time. This is an incomplete objective for settings such as IoT, where devices are heterogeneous, data is scarce and skewed, and a node's strongest neighbors may far exceed its own local capacity. We study how nodes should train so that their predictions compose well at deployment, and how each node should learn whom to trust. Under a server-free, model-agnostic protocol where nodes exchange only queries and soft predictions, we propose Learned Neighbor Trust (LNTrust) wherein each node learns a compact trust function over its neighborhood from local validation evidence. This trust function gates auxiliary distillation during training and defines a deployment ensemble at inference, so that collaboration learned during training transfers directly to deployment. Across datasets and topologies, LNTrust improves deployed accuracy over the strongest output-only baseline by large margins while using significantly less communication than previous methods.

---


### 230. [Chaotic Contrastive Learning for Robust Texture Classification](https://arxiv.org/abs/2605.05012)

**<font color=#1a73e8>作者：</font>** Joao B Florindo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Texture classification is a pivotal task in computer vision, presenting unique challenges due to high inter-class similarity and the sensitivity of structural patterns to scale and illumination changes. While Convolutional Neural Networks (CNNs) and recent Vision Transformers have set performance benchmarks, they often require extensive labeled datasets or struggle to generalize across domains due to an over-reliance on color and shape features. This paper introduces a novel framework that synergizes Self-Supervised Learning (SSL) with deterministic chaotic dynamics. We propose a chaotic contrastive pre-training strategy, where pixel-wise chaotic maps, specifically Logistic, Tent, and Sine maps, act as non-linear data augmentation techniques. These chaotic perturbations, grounded in ergodic theory, force the network to learn topologically robust features by mimicking complex environmental noise and reflectance variations. Furthermore, we introduce an attention-based feature ensemble that fuses high-level semantic representations from a supervised large backbone with low-frequency structural features from a chaos-pretrained tiny encoder. Experimental results on six texture benchmarks (FMD, UMD, KTH-TIPS2-b, DTD, GTOS, and 1200Tex) demonstrate the superiority of the proposed method, outperforming state-of-the-art approaches and achieving promising accuracies on all the analyzed datasets.

---


### 231. [CARD: A Multi-Modal Automotive Dataset for Dense 3D Reconstruction in Challenging Road Topography](https://arxiv.org/abs/2605.05014)

**<font color=#1a73e8>作者：</font>** Gasser Elazab, Frank Neuhaus, Tilman Koß 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous driving must operate across diverse surfaces to enable safe mobility. However, most driving datasets are captured on well-paved flat roads. Moreover, recent driving datasets primarily provide sparse LiDAR ground truth for images, which is insufficient for assessing fine-grained geometry in depth estimation and completion. To address these gaps, we introduce CARD, a multi-modal driving dataset that delivers quasi-dense 3D ground truth across continuous sequences rich in speed bumps, potholes, irregular surfaces and off-road segments. Our sensor suite includes synchronized global-shutter stereo cameras, front and rear LiDARs, 6-DoF poses from LiDAR-inertial odometry, per-wheel motion traces, and full calibration. Notably, our multi-LiDAR fusion yields ~500K valid depth pixels per frame, about 6.5x more than KITTI Depth Completion and 10x more on average than other public driving datasets. The dataset spans ~110 km and 4.7 hours across Germany and Italy. In addition, CARD provides 2D bounding boxes targeting road-topography irregularities, enabling accurate benchmarking for both geometry and perception tasks. Furthermore, we establish a standardized evaluation protocol for road surface irregularities on CARD and benchmark state-of-the-art depth estimation models to provide strong baselines. The CARD dataset is hosted on this https URL.

---


### 232. [Position: Embodied AI Requires a Privacy-Utility Trade-off](https://arxiv.org/abs/2605.05017)

**<font color=#1a73e8>作者：</font>** Xiaoliang Fan, Jiarui Chen, Zhuodong Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Embodied AI (EAI) systems are rapidly transitioning from simulations into real-world domestic and other sensitive environments. However, recent EAI solutions have largely demonstrated advancements within isolated stages such as instruction, perception, planning and interaction, without considering their coupled privacy implications in high-frequency deployments where privacy leakage is often irreversible. This position paper argues that optimizing these components independently creates a systemic privacy crisis when deployed in sensitive settings, thereby advancing the position that privacy in EAI is a life cycle-level architectural constraint rather than a stage-local feature. To address these challenges, we propose Secure Privacy Integration in Next-generation Embodied AI (SPINE), a unified privacy-aware framework that treats privacy as a dynamic control signal governing cross-stage coupling throughout the entire EAI life cycle. SPINE decomposes the EAI pipeline into various stages and establishes a multi-criterion privacy classification matrix to orchestrate contextual sensitivity across stage boundaries. We conduct preliminary simulation and real-world case studies to conceptually validate how privacy constraints propagate downstream to reshape system behavior, illustrating the insufficiency of fragmented privacy patches and motivating future research directions into secure yet functional embodied AI systems. We detail the SPINE framework and case studies at this https URL.

---


### 233. [Graph-SND: Sparse Aggregation for Behavioral Diversity in Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2605.05020)

**<font color=#1a73e8>作者：</font>** Shawn Ray  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> System Neural Diversity (SND) measures behavioral heterogeneity in multi-agent reinforcement learning by averaging pairwise distances over all $\binom{n}{2}$ agent pairs, making each call quadratic in team size. We introduce Graph-SND, which replaces this complete-graph average with a weighted average over the edges of an arbitrary graph $G$. Three regimes follow: $G=K_n$ recovers SND exactly; a fixed sparse $G$ defines a localized diversity measure at $O(|E|)$ cost; and random edge samples yield an unbiased Horvitz-Thompson estimator and a normalized sample mean with $O(1/\sqrt{m})$ concentration in the sampled edge count $m$. For fixed sparse graphs we prove forwarding-index distortion bounds for expanders and a spectral refinement under low-rank distance structure; for random $d$-regular graphs we prove an unconditional probabilistic $\widetilde{\mathcal{O}}(D_{\max}/\sqrt{n})$ bound. On VMAS we verify recovery, unbiasedness, concentration, and wall-clock scaling, with a PettingZoo TVD panel checking non-Gaussian transfer. In a 500-iteration $n=100$ PPO run, Bernoulli-$0.1$ Graph-SND tracks full SND while reducing per-call metric time by about $10\times$, and frozen-policy GPU timing up to $n=500$ follows the predicted $\binom{n}{2}/|E|$ speedup. Random $d$-regular expanders empirically achieve $\mathrm{SND}_{G}^{\mathrm{u}}/\mathrm{SND} \in [0.9987, 1.0013]$ at $\Theta(n \log n)$ edges. In DiCo diversity control at $n=50$, Bernoulli-$0.1$ Graph-SND preserves set-point tracking with paired reward differences indistinguishable from zero across nine matched cells while cutting per-call metric cost by ${\sim}9.5\times$. Together, these results show that the SND aggregation bottleneck can be removed without changing the metric's semantics, yielding a drop-in sparse alternative that scales beyond complete-graph SND and supports both passive measurement and closed-loop diversity control.

---


### 234. [Local Intrinsic Dimension Unveils Hallucinations in Diffusion Models](https://arxiv.org/abs/2605.05026)

**<font color=#1a73e8>作者：</font>** Bartlomiej Sobieski, Matthew Tivnan, Dawid Płudowski 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models are prone to generating structural hallucinations - samples that match the statistical properties of the training data yet defy underlying structural rules, resulting in anomalies like hands with more than five fingers. Recent research studied this failure mode from several viewpoints, offering partial explanations to their occurrence, such as mode interpolation. In this work, we propose a complementary perspective that treats hallucinations as instabilities on the model-induced manifold. We begin by showing that a hallucination filter based on such instabilities matches or exceeds the performance of the recently proposed temporal one. By tracing the source of these instabilities, we identify local intrinsic dimension (LID) as their primary driver and propose Intrinsic Quenching (IQ), a direct corrective mechanism that deflates it to alleviate hallucinations. IQ consistently outperforms standard hallucination reduction baselines across a wide array of benchmarks and offers a highly promising solution for enforcing anatomical consistency in downstream medical imaging tasks.

---


### 235. [Prompt-Anchored Vision-Text Distillation for Lifelong Person Re-identification](https://arxiv.org/abs/2605.05027)

**<font color=#1a73e8>作者：</font>** Wen Wen, Hao Chen, Shiliang Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lifelong person re-identification (LReID) aims to train a generalizable model with sequentially collected data. However, such models often suffer from semantic drift, limited adaptability, and catastrophic forgetting as new domains emerge. Existing exemplar-free approaches largely rely on visual-only distillation or parameter regularization, while overlooking the potential of auxiliary modalities, such as text, to preserve semantic stability and enable incremental plasticity. We observe that the frozen text encoder in pretrained vision-language models can serve as a stable semantic anchor across domains. To decouple the roles of vision and text, we propose Prompt-Anchored vision-text Distillation (PAD), an asymmetric vision-text framework for semantic alignment and cross-domain generalization. On the textual side, we distill prompts to preserve vision-text alignment under a fixed semantic space, acting as a global semantic reference rather than a dominant learning signal. On the visual side, an EMA-based teacher with an adaptive prompt pool enables domain-wise adaptation by allocating new slots while freezing past ones. Extensive experiments show that PAD substantially outperforms state-of-the-art methods across seen and unseen domains, achieving a strong balance between stability and plasticity. Project page is available at this https URL.

---


### 236. [The Predictive-Causal Gap: An Impossibility Theorem and Large-Scale Neural Evidence](https://arxiv.org/abs/2605.05029)

**<font color=#1a73e8>作者：</font>** Kejun Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We report a systematic failure mode in predictive representation learning. Across 2695 neural network configurations trained to predict linear-Gaussian dynamics, the optimal encoder tracks the environment rather than the system it is meant to model. The mean causal fidelity -- the fraction of encoder sensitivity allocated to system degrees of freedom -- is 0.49, and only 2.5% of configurations exceed 0.70. The failure intensifies with dimension: at N=100, the optimal encoder becomes causally blind (fidelity ~10^{-8}) while achieving 92% lower prediction error than the causal representation. We prove this is not an optimization artifact but a structural property of the predictive objective: when environment modes are slower or less noisy than system modes, every minimizer of the population risk encodes the former. The set of dynamics exhibiting this predictive-causal gap is open and of positive measure in parameter space. In a nonlinear Duffing-GRU sweep, unconstrained predictors learn environment-dominant representations in 55% of tasks (95% CI 41--68%) versus 24% under operational grounding (p=2.3e-3); the median out-of-distribution MSE inflation under environment shift is 1.82x versus 1.00x. Operational grounding -- restricting the loss to system observables -- partially suppresses the gap, but causal fidelity is never recovered without an explicit system-environment boundary. The results identify the predictive-causal gap as a structural limit of learning, with implications for self-supervised representation learning, world models, and the scaling paradigm.

---


### 237. [Computer-Aided Design Generation by Cascaded Discrete Diffusion Model](https://arxiv.org/abs/2605.05031)

**<font color=#1a73e8>作者：</font>** Honghu Pan, Xiaoling Luo, Yongyong Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent deep learning approaches seek to automate CAD creation by representing a model as a sequence of discrete commands and parameters, and then generating them using autoregressive models or continuous diffusion operating in Euclidean embedding space. However, continuous diffusion perturbs representations in a continuous Euclidean domain that does not reflect the inherently discrete and heterogeneous nature of CAD tokens, often producing perturbed representations that map to semantically invalid symbols. To overcome this limitation, we propose a cascaded discrete diffusion framework for CAD generation, which consists of a command diffusion for generating CAD commands and a parameter diffusion conditioned on CAD commands. Unlike isotropic Gaussian perturbation, the forward process of our approach operates directly over categorical token distributions using delicate transition matrices. For commands, we adopt an absorbing-state transition matrix that progressively corrupts tokens to a designated symbol; for parameters, we introduce specific transition matrices tailored to heterogeneous attributes: a Gaussian kernel for coordinate continuity, a scale-invariant kernel for dimensional values, and a prior-preserving kernel for boolean attributes. The reverse process is achieved by two denoising networks: a Transformer-based encoder for command recovery, and a parameter network with extra local self-attention for command-level interaction and cross-attention for conditional injection. Experiments on the DeepCAD dataset show that the proposed approach surpasses existing autoregressive and continuous diffusion models on unconditional generation metrics, while qualitative results validate effective controllability in conditional generation tasks. Source codes will be released.

---


### 238. [Few-Shot Learning Pipeline for Monkeypox Skin Disease Classification Using CNN Feature Extractors](https://arxiv.org/abs/2605.05034)

**<font color=#1a73e8>作者：</font>** Md. Safirur Rashid, Sabbir Ahmed, Muhammad Usama Islam 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the strong performance of Convolutional Neural Networks (CNNs) in disease classification, their effectiveness often depends on access to large annotated datasets, which is an impractical requirement for emerging or rare conditions such as Monkeypox. To overcome this limitation, we propose a few-shot learning (FSL) framework that employs SimpleShot, a lightweight, non-parametric, inductive classifier, for Monkeypox and pox-like skin disease recognition from limited labeled examples. The proposed pipeline passes the skin lesion images through a frozen, pretrained CNN backbone to obtain feature embeddings, which are then classified via SimpleShot using nearest-centroid comparisons in a normalized embedding space. We systematically benchmark six widely used CNN backbones as feature extractors under consistent experimental settings, enabling fair comparison. Experiments on three publicly available datasets (MSLD v1.0, MSID, and MSLD v2.0) are conducted across 2-way, 4-way, and 6-way tasks with 1-shot, 5-shot, and 10-shot configurations. Among all models, MobileNetV2_100 consistently achieves the highest accuracy. In addition, we present a cross-dataset evaluation for Monkeypox classification, revealing that binary Mpox-vs-Others transfer remains comparatively stable while multi-class performance degrades significantly under domain shift. Together, these results demonstrate the practical utility of combining inductive FSL methods with lightweight CNN backbones and highlight the importance of domain robustness for reliable real-world clinical deployment.

---


### 239. [Preference-Based Self-Distillation: Beyond KL Matching via Reward Regularization](https://arxiv.org/abs/2605.05040)

**<font color=#1a73e8>作者：</font>** Xin Yu, Liuchen Liao, Yiwen Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation is an efficient alternative to reinforcement learning, offering dense token-level training signals. However, its reliance on a stronger external teacher has driven recent work on on-policy self-distillation, where the same model serves as both teacher and student under different prompt contexts. Yet, existing self-distillation methods largely reduce learning to KL matching toward the context-augmented teacher model. This approach often suffers from training instability and can degrade reasoning performance over time. Moreover, self-distillation from the same model with prompt augmentation lacks the exploratory diversity provided by a genuine external teacher. To address these limitations, we move beyond fixed-teacher KL matching and propose \textbf{P}reference-\textbf{B}ased \textbf{S}elf-\textbf{D}istillation (\textbf{PBSD}), which revisits on-policy self-distillation through a reward-regularized perspective. Instead of directly matching the teacher distribution, we derive a reward-regularized objective whose analytic optimum is a reward-reweighted teacher distribution, yielding a target policy provably superior to the original teacher under this objective. Practically, PBSD optimizes preference gaps between teacher and student samples while maintaining on-policy student sampling. We support this framework with a statistical analysis of the induced preference-learning problem, formally establishing when on policy self-distillation is preferable to learning from an external teacher in our setting. Experiments on mathematical reasoning and tool-use benchmarks across multiple model scales demonstrate that PBSD consistently achieves the strongest average performance among comparable baselines, showing improved training stability over prior self-distillation baselines while preserving token efficiency.

---


### 240. [Direct Product Flow Matching: Decoupling Radial and Angular Dynamics for Few-Shot Adaptation](https://arxiv.org/abs/2605.05054)

**<font color=#1a73e8>作者：</font>** Hongxu Chen, Yanghao Wang, Bowei Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent flow matching (FM) methods improve the few-shot adaptation of vision-language models, by modeling cross-modal alignment as a continuous multi-step flow. In this paper, we argue that existing FM methods are inherently constrained by incompatible geometric priors on pre-trained cross-modal features, resulting in suboptimal adaptation performance. We first analyze these methods from a polar decomposition perspective (i.e., radial and angular sub-manifolds). Under this new geometric view, we identify three overlooked limitations in them: 1) Angular dynamics distortion: The radial-angular coupling induces non-uniform speed on the angular sub-manifold, leading to regression training difficulty and extra truncation errors. 2) Radial dynamics neglect: Feature normalization discards modality confidence, failing to distinguish out-of-distribution and in-distribution data, and abandoning crucial radial dynamics. 3) Context-agnostic unconditional flow: Dataset-specific information loss during pre-trained cross-modal feature extraction remains unrecovered. To resolve these issues, we propose warped product flow matching (WP-FM), a unified Riemannian framework that reformulates alignment on a warped product manifold. Within this framework, we derive direct product flow matching (DP-FM) by introducing a constant-warping metric, which yields a decoupled cylindrical manifold (i.e., direct product manifold). DP-FM enables independent radial evolution and constant-speed angular geodesic transport, effectively eliminating angular dynamics distortion while preserving radial consistency. Meanwhile, we incorporate classifier-free guidance by conditioning the flow on the pre-trained VLMs' hidden states to inject missing dataset-specific information. Extensive results across 11 benchmarks have demonstrated that DP-FM achieves a new state-of-the-art for multi-step few-shot adaptation.

---


### 241. [Adaptive Learning Strategies for AoA-Based Outdoor Localization: A Comprehensive Framework](https://arxiv.org/abs/2605.05055)

**<font color=#1a73e8>作者：</font>** Bac Trinh-Nguyen, Sara Berri, Sin G. Teo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Localization in 5G and 6G networks is essential for important use cases such as intelligent transportation, smart factories, and smart cities. Although deep learning has enabled improving localization accuracy, depending on the deployment scenario and the effort required for dataset collection campaigns on a given infrastructure, the training process for localization models can vary significantly. Furthermore, with respect to feature selection, recent works have demonstrated the robustness of angle-of-arrival (AoA) based localization. In view of these two points, we propose an adaptive framework for AoA-based localization that consists of two alternative learning strategies, each suited either for large or small training datasets. The proposed framework is evaluated on a real, massive multiple input multiple output (mMIMO) orthogonal frequency division multiplexing (OFDM) outdoor channel state information (CSI) dataset. First, we investigate offline learning when large training datasets are available; we propose a hierarchical framework that first distinguishes between line of sight (LoS) and non line of sight (NLoS) regions and then moves to more fine grained localization in the respective region. This approach provides high-performance localization through accumulated batch retraining and an integrated hyperparameter optimization mechanism. Second, when only a small training dataset is available, an online learning framework is proposed, using incremental tree-based and ensemble-based models for handling streaming data and continuously updating mode, as well as an online few-shot learning model for rapidly initializing new classes from a limited labeled support set. These results showcase that highly accurate robust localization can be achieved incrementally during network operation by exploiting online learning, alleviating the need for large dataset collection campaigns.

---


### 242. [ScriptHOI: Learning Scripted State Transitions for Open-Vocabulary Human-Object Interaction Detection](https://arxiv.org/abs/2605.05057)

**<font color=#1a73e8>作者：</font>** Minh Anh Nguyen, Quang Huy Tran, Bao Ngoc Le 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary human-object interaction (HOI) detection requires recognizing interaction phrases that may not appear as annotated categories during training. Recent vision-language HOI detectors improve semantic transfer by matching human-object features with text embeddings, but their predictions are often dominated by object affordance and phrase-level co-occurrence. As a result, a model may predict \textit{cut cake} from the presence of a knife and a cake without verifying whether the hand, tool, target, contact pattern, and object state jointly support the action. We propose \textbf{ScriptHOI}, a structured framework that represents each interaction phrase as a soft scripted state transition. Rather than treating a phrase as a single class token, ScriptHOI decomposes it into body-role, contact, geometry, affordance, motion, and object-state slots. A visual state tokenizer parses each detected human-object pair into corresponding state tokens, and a slot-wise matcher estimates both script coverage and script conflict. These two quantities calibrate HOI logits, expose missing visual evidence, and provide training constraints for incomplete annotations. To avoid suppressing valid but unannotated interactions, we further introduce interval partial-label learning, which constrains unannotated candidates with script-derived lower and upper probability bounds instead of assigning closed-world negatives. A counterfactual script contrast loss swaps individual script slots to discourage object-only shortcuts. Experiments on HICO-DET, V-COCO, and open-vocabulary HOI splits show that ScriptHOI improves rare and unseen interaction recognition while substantially reducing affordance-conflict false positives.

---


### 243. [The Impossibility Triangle of Long-Context Modeling](https://arxiv.org/abs/2605.05066)

**<font color=#1a73e8>作者：</font>** Yan Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We identify and prove a fundamental trade-off governing long-sequence models: no model can simultaneously achieve (i) per-step computation independent of sequence length (Efficiency), (ii) state size independent of sequence length (Compactness), and (iii) the ability to recall a number of historical facts proportional to sequence length (Recall). We formalize this trade-off within an Online Sequence Processor abstraction that unifies Transformers, state space models, linear recurrent networks, and their hybrids. Using the Data Processing Inequality and Fano's Inequality, we prove that any model satisfying Efficiency and Compactness can recall at most O(poly(d)/log V) key-value pairs from a sequence of arbitrary length, where d is the model dimension and V is the vocabulary size. We classify 52 architectures published before March 2026 into the triangle, showing that each achieves at most two of the three properties and that hybrid architectures trace continuous trajectories in the interior. Experiments on synthetic associative recall tasks with five representative architectures validate the theoretical bound: empirical recall capacity lies strictly below the information-theoretic limit, and no architecture escapes the triangle.

---


### 244. [Height-Guided Projection Reparameterization for Camera-LiDAR Occupancy](https://arxiv.org/abs/2605.05072)

**<font color=#1a73e8>作者：</font>** Yuan Wu, Zhiqiang Yan, Jiawei Lian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D occupancy prediction aims to infer dense, voxel-wise scene semantics from sensor observations, where the 2D-to-3D view transformation serves as a crucial step in bridging image features and volumetric representations. Most previous methods rely on a fixed projection space, where 3D reference points are uniformly sampled along pillars. However, such sampling struggles to capture the sparsity and height variations of real-world scenes, leading to ambiguous correspondences and unreliable feature aggregation. To address these challenges, we propose HiPR, a camera-LiDAR occupancy framework with Height-Guided Projection Reparameterization. HiPR first encodes LiDAR into a BEV height map to capture the maximum height of the point cloud. HiPR then adjusts the sampling range of each pillar using the height prior, enabling adaptive reparameterization of the projection space. As a result, the projected points are redistributed into geometrically meaningful regions rather than fixed ranges. Meanwhile, we mask out the invalid parts of the height map to avoid misleading the feature aggregation. In addition, to alleviate the training instability caused by noisy LiDAR-derived heights, we introduce a training-time Progressive Height Conditioning strategy, which gradually transitions the conditioning signal from ground-truth heights to LiDAR heights. Extensive experiments demonstrate that HiPR consistently outperforms existing state-of-the-art methods while maintaining real-time inference. The code and pretrained models can be found at this https URL.

---


### 245. [FlowDIS: Language-Guided Dichotomous Image Segmentation with Flow Matching](https://arxiv.org/abs/2605.05077)

**<font color=#1a73e8>作者：</font>** Andranik Sargsyan, Shant Navasardyan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate image segmentation is essential for modern computer vision applications such as image editing, autonomous driving, and medical image analysis. In recent years, Dichotomous Image Segmentation (DIS) has become a standard task for training and evaluating highly accurate segmentation models. Existing DIS approaches often fail to preserve fine-grained details or fully capture the semantic structure of the foreground. To address these challenges, we present FlowDIS, a novel dichotomous image segmentation method built on the flow matching framework, which learns a time-dependent vector field to transport the image distribution to the corresponding mask distribution, optionally conditioned on a text prompt. Moreover, with our Position-Aware Instance Pairing (PAIP) training strategy, FlowDIS offers strong controllability through text prompts, enabling precise, pixel-level object segmentation. Extensive experiments demonstrate that our method significantly outperforms state-of-the-art approaches both with and without language guidance. Compared with the best prior DIS method, FlowDIS achieves a 5.5% higher $F_{\beta}^{\omega}$ measure and 43% lower MAE ($\mathcal{M}$) on the DIS-TE test set. The code is available at: this https URL

---


### 246. [A unified Benchmark for Multi-Frame Image Restoration under Severe Refractive Warping](https://arxiv.org/abs/2605.05079)

**<font color=#1a73e8>作者：</font>** Maxim V. Shugaev, Md Reshad Ul Hoque, Bridget Kennedy 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video sequence capturing through refractive dynamic media, such as a turbulent air or water surface, often suffer from severe geometric distortions and temporal instability. While recent advances address mild atmospheric turbulence, no existing benchmarks systematically evaluate restoration methods under strong and highly nonuniform refractive conditions. We present a comprehensive benchmark for geometric distortion removal in video, covering a range from turbulence-like mild warping to strong discontinuous refractive deformations. The benchmark includes both laboratory-captured real data and synthetic sequences generated for static scenes via physics-based light refraction modeling across four distortion levels and multiple surface wave types. We evaluate a spectrum of methods from simple baselines and classical registration algorithms to advanced learning-based approaches including DATUM and our proposed diffusion based V-cache for high and extreme distortions regimes. Evaluation uses both pixel-level (PSNR, SSIM), and perceptual (LPIPS, DINO, CLIP) metrics providing the first large scale analysis of geometric distortion removal. Our benchmark establishes a new foundation for developing and evaluating algorithms capable of reconstructing video from highly distorted optical environments. Our code and datasets are available at this https URL.

---


### 247. [Provable imitation learning for control of instability in partially-observed Vlasov--Poisson equations](https://arxiv.org/abs/2605.05081)

**<font color=#1a73e8>作者：</font>** Xiaofan Xia, Qin Li, Wenlong Mou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider the stabilization of Vlasov--Poisson plasma dynamics, a central control problem in nuclear fusion. Our focus is the gap between what an ideal controller would use and what experiments can actually observe: while optimal policy may rely on the full phase-space state, practical feedback is typically limited to sparse macroscopic diagnostics. We therefore study imitation learning methods that distill a fully observed expert policy into controllers operating only on macroscopic measurements. We show the stability guarantees of the learned policy, where the error floor depends on the minimal behavior cloning loss achievable under the observation constraints. We further characterize this minimal loss in terms of a notion of entropy that quantifies the complexity of the initial distribution. Our results demonstrates the theoretical feasibility of learning stabilizing feedback policies for kinetic plasma dynamics from macroscopic observations, and exhibits the adaptivity of the learning approach to low-complexity structures. Through extensive numerical experiments, we validate our theory and show that the learned policies can stabilize the system using only macroscopic observations, within a significantly longer time horizon than non-adaptive baseline controllers.

---


### 248. [Order Matters: Improving Domain Adaptation by Reordering Data](https://arxiv.org/abs/2605.05084)

**<font color=#1a73e8>作者：</font>** Andrea Napoli, Paul White  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Domain shift remains a key challenge in deploying machine learning models to the real world. Unsupervised domain adaptation (UDA) aims to address this by minimising domain discrepancy during training, but the discrepancy estimates suffer from high variance in stochastic settings, which can stifle the theoretical benefits of the method. This paper proposes Optimal Reordering of Data for Error-Reduced Estimation of Discrepancy (ORDERED), a novel unbiased stochastic variance reduction technique which reduces the discrepancy estimation error by optimising the order in which the training data are sampled. We consider two specific domain discrepancy losses (correlation alignment and the maximum mean discrepancy), formulate their stochastic estimation error as a function of the data sampling order, and propose a practical optimisation algorithm. Our simulations demonstrate reduced variance compared to related methods, and experiments on two domain shift image classification benchmarks show improved target domain accuracy.

---


### 249. [Unified Framework of Distributional Regret in Multi-Armed Bandits and Reinforcement Learning](https://arxiv.org/abs/2605.05102)

**<font color=#1a73e8>作者：</font>** Harin Lee, Min-hwan Oh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the distribution of regret in stochastic multi-armed bandits and episodic reinforcement learning through a unified framework. We formalize a distributional regret bound as a probabilistic guarantee that holds uniformly over all confidence levels $\delta \in (0,1]$, thereby characterizing the regret distribution across the full range of $\delta$. We present a simple UCBVI-style algorithm with exploration bonus $\min\{c_{1,k}/N, c_{2,k}/\sqrt{N}\}$, where $N$ denotes the visit count and $(c_{1,k},c_{2,k})$ are user-specified parameters. For arbitrary parameter sequences, we derive general gap-independent and gap-dependent distributional regret bounds, yielding a principled characterization of how the parameters control the trade-off between expected performance, tail risk, and instance-dependent behavior. In particular, our bounds achieve optimal trade-offs between expected and distributional regret in both minimax and instance-dependent regimes. As a special case, for multi-armed bandits with $A$ arms and horizon $T$, we obtain a distributional regret bound of order $\mathcal{O}(\sqrt{AT}\log(1/\delta))$, confirming the conjecture of Lattimore & Szepesvári (2020, Section 17.1) for the first time.

---


### 250. [Text Corpora as Concept Fields: Black-Box Hallucination and Novelty Measurement](https://arxiv.org/abs/2605.05103)

**<font color=#1a73e8>作者：</font>** Nicholas S. Kersting, Vittorio Castelli, Chieh Ting Yeh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce the **Concept Field** of a text corpus: a local drift field with pointwise uncertainty, estimated in sentence-embedding space from the deltas between consecutive sentences. Given a candidate sentence transition, we score its agreement with the field by $\zeta$, the mean absolute z-distance between the observed delta and the field's local Gaussian estimate. The score is black-box (no model internals), corpus-attributable (every score traces to nearby corpus sentences), and admits a direct probabilistic reading. We support the computation with the introduction of a **Vector Sequence Database (VSDB)** that stores embeddings together with sequence-position and next-delta metadata. We evaluate this approach on two large-scale settings: hallucination-style groundedness detection over the U.S. Code of Federal Regulations, and novelty detection over Project Gutenberg. Using controlled LLM-generated rewrites, Concept Fields achieve strong selective classification performance under a grounded / ungrounded / unsure triage policy, which unlike retrieval-centric baselines have similar coverage-risk behavior across both domains, supporting a probability-based interpretation that transfers across domains. We also sketch how divergence and curl of the Concept Field, computed on dense clusters, surface qualitatively meaningful semantic patterns (logic sources, sinks, and implicit topics), which we offer as hypothesis-generating rather than as a quantitative result. Concept Fields provide a fast, lightweight, and interpretable signal for groundedness and novelty, complementary to LLM-as-judge and white-box detectors.

---


> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-270](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
