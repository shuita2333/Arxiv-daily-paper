# 📦 其他研究 | 2026年11月03日

> 本类共 **193** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-193**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-193**

---

### 151. [Exploring Bad Minima in Transfer Learning](https://arxiv.org/abs/2610.41807)

**<font color=#1a73e8>作者：</font>** Mina Remeli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transfer learning is a highly successful learning paradigm in deep learning which leverages knowledge from one task and applies it to another. Despite its success, the necessary conditions for knowledge transfer are unclear and require further research. In this dissertation, our aim is to understand transferability a little better by answering the following question: Does good generalization on a source task necessarily imply transferability to a related target task? We hypothesize the answer is negative, and attempt to find counterexamples via adversarial attacks on the transfer learning procedure. Over three types of adversarial attacks, our empirical results show a strong relationship between generalization on the source task and transferability. These results do not rule out generalization on the source task as a sufficient condition for successful transfer.

---


### 152. [Continual Reinforcement Learning Is an Integration Problem](https://arxiv.org/abs/2610.41809)

**<font color=#1a73e8>作者：</font>** Nis Meinert, Jakob Gawlikowski, Edward Grant 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents an opinionated set of ten desiderata intended to inform the design and evaluation of reinforcement-learning agents that learn continually throughout a continuing lifetime. We use these desiderata to examine a representative selection of existing approaches. Progress on individual desiderata is valuable, but the longer-term aim should be to integrate all ten within a single agent. To our knowledge, no published evaluation has yet provided evidence for such an integration. Likewise, the representative benchmarks we review probe different parts of this target, but separate evaluations do not establish that the corresponding properties coexist within one agent throughout a continuing lifetime. As a secondary contribution, we therefore present a compact persistent-world scenario as a playable companion to the desiderata and outline a proposed benchmark that examines a broad range of associated behavioral capabilities together within one such lifetime.

---


### 153. [A Patch is More Than a Token](https://arxiv.org/abs/2610.41814)

**<font color=#1a73e8>作者：</font>** Zixiong Wang, Haiping Ma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers represent each image patch through a canonical token produced under one observation condition. That token is a powerful interface, but it is still one realized state of the patch. We introduce PMTT, which establishes two foundations: a patch representation object can extend from one canonical state to a canonical-centered Representation State Family, and identity-preserving variation opens Patch-Level Local Feature Space. We develop four parts of this representation program. Patch Information Acquisition and Dense Orbital Views expose lawful same-patch states. Visible-to-Hidden prediction tests whether observed states reveal structure beyond themselves. Intrinsic analysis identifies low-dimensional, energy-concentrated, patch-specific, predictive geometry. Representation Organization separates acquiring more information from organizing that information, with an analytic Manifold as the central structured representation. We realize PMTT on frozen DINOv3 S/B/L/H+ backbones without neural post-training of the representation. Across two independent 4,096-anchor cohorts, Manifold explains 70.8-79.6% of Hidden variation, compared with 55.0-72.3% for directly Observed states, and wins on more than 95% of anchors at every scale. Effective rank falls from about 2.5 to 2.0 while dominant energy concentration rises with backbone scale. Across six visual capabilities and four scales, Observed exceeds the canonical Center in 21 of 24 conditions, Manifold exceeds Center in 23, and Manifold exceeds Observed in 16. The strongest current consequence appears in physical correspondence, where MegaDepth satisfies Center < Observed < Manifold at every scale. These results show that pretrained visual backbones contain richer patch information than the standard single-token interface directly exposes. Code and experimental assets are available at this https URL.

---


### 154. [DIFFNAS: Predictor-Free Neural Architecture Search via Diffusion Model and Zero-Cost Evaluation](https://arxiv.org/abs/2610.41818)

**<font color=#1a73e8>作者：</font>** Yize Sun, Hanzhang Ma, Zixin Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural Architecture Search (NAS) has advanced the automated design of deep networks, but remains computationally expensive due to reliance on model training or performance predictors. We introduce DIFFNAS, a predictor-free NAS framework that leverages a discrete graph diffusion model guided by zero-cost performance proxies. Unlike prior diffusion-based NAS methods that require learned performance predictors, DIFFNAS conditions the generative process on training-free metrics such as MeCo and SWAP, enabling efficient architecture search with minimal computational overhead. Experiments on NAS-Bench-201 show that DIFFNAS finds the optimal architectures for CIFAR-10 and CIFAR-100 (94.37% and 73.51%) without a pretrained predictor, while reducing search cost by up to 17.5x compared to DiffusionNAG. On the MobileNetV3 search space, its accuracy is lower than that of DiffusionNAG. These results highlight the promise of diffusion models combined with zero-cost proxies for scalable and effective architecture search.

---


### 155. [ElTab: Elastically Looped Tabular Transformers](https://arxiv.org/abs/2610.41819)

**<font color=#1a73e8>作者：</font>** Mieszko Komisarczyk, Saurabh Mathur, Maurice Kraus 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular transformer models such as TabPFN achieve strong predictive performance but incur substantial inference costs, making them difficult to deploy in resource-constrained settings. While looped transformers reduce parameter count through weight sharing, they can lose significant predictive power when stopped early. To address this challenge, we introduce the Elastically Looped Tabular Transformer (ElTab), a single model trained to operate across different computational budgets through supervision at randomly sampled early exits. Across 30 OpenML classification datasets, a single ElTab model matches six depth-specific looped models while cutting training cost by more than half, and matches a 12-layer TabPFN-style baseline with 25% fewer inference FLOPs. These results show that elastic-depth training yields a single model that adapts to the deployment budget at hand, offering a favorable trade-off among predictive performance, storage, and computational cost.

---


### 156. [PGGT-Loc: Primitive-Grounded Geometry Transformer for Feed-Forward Camera Localization](https://arxiv.org/abs/2610.41833)

**<font color=#1a73e8>作者：</font>** Hanqiao Ye, Yuzhou Liu, Mengqi Rong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera localization methods are mostly multi-stage pipelines relying on dedicated and complex maps that are costly to construct, store, and maintain over time. Alternatively, well-structured maps that organize scenes with compact yet expressive primitives are often readily available, providing rich structural and semantic cues that humans can interpret. However, their potential for direct camera localization remains largely unexplored due to the significant modality gap between map primitives and visual observations. This motivates a new concept for localization, which estimates camera poses by grounding query observations to map primitives. In this paper, we instantiate the concept in the context of planar primitives with PGGT, the Primitive-Grounded Geometry Transformer network. Given a single query image and a set of planar map primitives, the network is trained to predict multiple localization targets for feed-forward 6-DoF camera localization that generalizes to unseen environments. With this straightforward and scalable architecture, our method pushes the state-of-the-art localization performance on both dense surface maps and minimal layout models. The code and models are available at this https URL

---


### 157. [ObjectGuidedMap: An Object-Aware Model for Robust Bird's Eye View Map Prediction in High-Occlusion Scenarios](https://arxiv.org/abs/2610.41834)

**<font color=#1a73e8>作者：</font>** Christian Bohn, Harsh Yadav, Klaus Friedrichs 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate BEV map prediction is a critical component of autonomous driving systems, enabling downstream planning and control. Recent approaches such as Mask2Map achieve strong performance by predicting vectorized, instance-level map elements directly from multi-view images. However, existing BEV map prediction models operate largely independently of object-level scene understanding, despite the fact that traffic participants frequently occlude or implicitly encode information about road geometry. In this work, we propose a multitask architecture that jointly predicts BEV maps and 3D objects, explicitly enabling information exchange between the two tasks. Building upon Mask2Map, we introduce an object detection branch and incorporate cross-task feature fusion at both the BEV feature level and the instance-query level via deformable attention and cross-attention mechanisms. This design allows map instances to leverage object context while remaining robust to occlusions caused by traffic participants. Experimental results on the nuScenes and Argoverse 2 datasets demonstrate that our approach consistently improves BEV map prediction accuracy, with particularly significant gains of 21% mAP in scenes containing heavy object occlusion.

---


### 158. [ReuScope: Auditing Data Reuse and Evaluation Sensitivity in Capsule Vision 2024](https://arxiv.org/abs/2610.41835)

**<font color=#1a73e8>作者：</font>** Eunseob Choi, Kyeonghun Kim, Hyuk-Jae Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We develop ReuScope, a protocol for auditing data reuse and evaluation sensitivity, using Capsule Vision 2024 as a case study. It combines measurements of data relationships with two comparisons: changing the evaluation population while holding predictions fixed, and changing training data while holding evaluation fixed. Byte-identical files cross the public training-validation boundary, and all 41 Kvasir-Capsule recordings that contribute frames occur in both partitions. Shared source recordings establish cross-split overlap; missing cross-recording patient identifiers prevent counting unique shared patients. Across ten paired seeds, removing all training rows attributed to Kvasir-Capsule, plus five rows from other sources flagged as near-matches to it, lowers public-validation balanced accuracy from 82.5% to 61.2%. Evaluating the same fitted models on the validation rows of the other sources reverses the comparison: removal improves balanced accuracy by 1.38 percentage points. The public-validation drop measures sensitivity to source removal, not an amount of leakage-induced inflation. Matched controls show that sample size and class counts alone do not explain the observed score differences. An exploratory experiment removes the training neighbors of validation frames that have close training matches, or equally many distant training rows, and yields a difference-in-differences estimate, relative to matched unflagged frames, of -0.355 percentage points in true-class probability; the paired-t interval for accuracy spans zero. The resulting procedure distinguishes observed reuse from conditional performance sensitivity and specifies the population, class support and uncertainty unit for each conclusion.

---


### 159. [Iterated Integrals as Lexical Fingerprints: Path Signature Embeddings for Lexical Similarity](https://arxiv.org/abs/2610.41855)

**<font color=#1a73e8>作者：</font>** Raj Shekhar Singh, Pratham Agarwal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While sentence embeddings are primarily designed for semantic generalization, their latent geometry implicitly encodes surface-level lexical properties, a relationship that remains poorly understood. Shallow pooling methods discard word order, while deep Transformer models obscure these lexical alignments behind computational complexity and uninterpretable spaces. We propose constructing sentence embeddings via the path signature of Word2Vec trajectories, leveraging the iterated integrals of rough path theory to create representations that explicitly capture sequential and lexical structure in a geometrically tractable manner. Through extensive ablations spanning Word2Vec dimensions, signature depths, and PCA compression, we correlate embedding distances against five lexical string metrics: Levenshtein, Jaro-Winkler, word Jaccard, phoneme Levenshtein, and character TF-IDF. We reveal that while average pooling almost entirely fails to capture character-level edit distances, path signatures strongly align with them, with depth 2 signatures optimally balancing character and word-level sensitivities. Furthermore, we demonstrate that the critical lexical variance is concentrated in a highly compact PCA subspace, and unlike pooling, signatures structurally preserve and quantify word order. These findings establish path signatures not as semantic generalizers, but as rigorous mathematical lenses that explicitly encode discrete lexical structures and word order, offering an interpretable alternative to opaque deep learning for lexical tracking.

---


### 160. [Learning to Interact and Direct: Co-Evolving Video Director Agents](https://arxiv.org/abs/2610.41865)

**<font color=#1a73e8>作者：</font>** Yingzhao Jian, Zhongan Wang, Yuxuan Hou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Video director agents orchestrate multistage production to realize users' creative visions. Emerging research on their self-evolution advances screenplay planning effectively. However, the mutual reinforcement between directing and user interaction remains largely overlooked. Improved interaction clarifies user intent and informs workflow refinement, while more reliable execution shifts collaboration from troubleshooting to creative decisions. To this end, we introduce LIT (Learning to Interact and DirecT), a framework comprises a director agent, a simulated user, and a meta engineer. Simulated user assigns creative tasks to probe the director's weaknesses, while the meta engineer uses the task traces to revise the director's interaction and production strategy. Although this approach can address discovered interaction and production issues, it still relies on passive attribution by the meta agent. This limits its ability to adapt to broader user interaction patterns and production techniques. To solve this problem, we equip LIT with a co-evolution paradigm. The meta agent proactively learns external knowledge, thereby improving its ability to discover problems and propose solutions. The meta agent, simulated user, and director together form an evolutionary closed loop, collaboratively enhances the system's directing and interaction capabilities. Across the Test and OOD Test splits, LIT improves production and Interaction scores by 19.1% and 32.0%, respectively, relative to the initial pipeline. Controlled ablations reveal the correlation between improvements in production and interaction, where the co-evolution mechanism further encourage directing skill and interaction mode exploration.

---


### 161. [Fuzzy selective state model for forecasting the dynamics of consumer preferences](https://arxiv.org/abs/2610.41879)

**<font color=#1a73e8>作者：</font>** P.A. Golovinski, A.A. Drobyshev, A.O. Shatalova  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We consider forecasting the dynamics of consumer preferences of retail chain customers. A customer's preference is described by a triangular fuzzy number. The evolution of the preference over time is governed by a Mamba-type selective state space model whose hidden state is a triangular number, with computations carried out in M.G.~Matveev's two-component algebra of fuzzy numbers. The recurrence parameters are computed from crisp features, while the fuzzy part of the model remains linear with non-negative coefficients. We show that the state then always remains a proper triangular number and is a convex combination of past observations, so that the fuzziness of the forecast does not accumulate over time and the algebraic computations coincide with Zadeh's extension principle. On a synthetic example with competitor promotions and customer switching, a lightweight 107-parameter model reaches a mean absolute error of the forecast centre of 0.154 versus 0.163 for the constant-inertia evolution operator and 0.179 for the naive forecast, matches a crisp model of the same architecture and additionally provides a linguistically interpretable estimate of forecast vagueness. We also show how the linguistic readout of the forecast can be used to detect a permanent switch of a customer to a competitor.

---


### 162. [Text as an Index for Zero-Shot Cross-Domain Knowledge Tracing](https://arxiv.org/abs/2610.41883)

**<font color=#1a73e8>作者：</font>** Yin Yi, Haiping Ma, Siyu Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge tracing (KT) predicts a student's next response from their history. New platforms often have question texts but no response logs for training, motivating zero-shot cross-domain KT. Existing transfer and cold-start methods use question semantics, but cross-platform semantic discrepancies limit transferability. We propose TIZSKT, which separates behavioral sequence modeling from domain-local historical evidence construction and uses text as an index rather than a directly transferable predictive representation. The Mastery-Dynamics Encoder learns correctness dynamics without question identifiers or text embeddings. Domain-Local Question Addressing builds fixed question addresses using a frozen text encoder and an unsupervised per-domain projection. The Text-Addressing Kernel uses these addresses to aggregate the current student's previous outcomes into a question-specific historical correctness summary. Cross-Segment Continuation retains access to earlier responses without extending the behavioral encoder's input sequence. Evidence-Volume Read-Out preserves the total kernel mass discarded by normalization and combines its log-compressed value with the behavioral state and historical correctness summary to predict the next response. All trainable parameters are learned from source domains; target inference uses public question texts and the current student's observed history without target-domain training. Leave-one-domain-out experiments on three public datasets show that TIZSKT achieves the highest mean AUC and accuracy among evaluated baselines on all target domains. Ablations confirm the contributions of text addressing and cross-segment continuation.

---


### 163. [On k-nearest-neighbor regression in metric spaces](https://arxiv.org/abs/2610.41896)

**<font color=#1a73e8>作者：</font>** László Györfi, Vladimir G. Pestov, Harro Walk 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study mean squared consistency of k-nearest-neighbor regression for metric space valued features. For a fixed feature distribution mu with atomless distance distributions, we describe how neighbor selection redistributes probability through the density of a uniformly chosen neighbor of an independent query. This gives separate conditions for the approximation error and the conditional response variance, and weakens Stone's domination condition when stronger response moments are available. In particular, when k_n tends to infinity and k_n/n tends to zero, a uniform L2(mu) bound on the selection densities suffices under a finite fourth response moment. We give a corresponding condition in terms of neighborhoods of fixed population mass and recover the Euclidean density bound. Finite global Nagata dimension gives Stone's domination. While sigma-finite Nagata dimensionality is known to ensure universal consistency of k-NN classification in complete separable spaces, we show that this is not the case for mean squared consistency with unbounded responses: we construct a space in this class on which one fixed noiseless response with all finite moments has diverging mean squared error.

---


### 164. [Using Machine Learning to Measure Self-Efficacy Belief Through Learners' Interaction Traces in Technology-Enhanced Learning](https://arxiv.org/abs/2610.41900)

**<font color=#1a73e8>作者：</font>** Maeva Somny, Linda Chouati, Marie Lefevre  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-efficacy beliefs play a critical role in learners' performance, academic choices, and, more broadly, in their future career trajectories. As Technology-Enhanced Learning (TEL) environments have demonstrated strong potential for supporting both performance and motivation, investigating self-efficacy within such environments is of particular interest, especially for implementing remedial practices as early as possible to support learners' self-efficacy beliefs. Our research aims to develop a system capable of detecting low self-efficacy based on learners' interaction traces while they solve exercises in a TEL system. In this paper, we present initial results and future perspectives on a detection approach based on data mining and machine learning techniques to identify features indicative of low self-efficacy beliefs. Because the detection of learners' self-efficacy beliefs through their use of TEL systems remains largely unexplored, this work is exploratory in nature. To this end, we conducted an experiment across two universities to collect interaction traces and self-reported measures of self-efficacy. We then developed a machine learning pipeline comprising multiple classification models, enabling us to highlight the importance of closely monitoring of learners' self-efficacy beliefs for improved prediction performance, given their highly dynamic nature during learning.

---


### 165. [Binary Sparse Codes: Where are we on Energy Efficient Representations?](https://arxiv.org/abs/2610.41933)

**<font color=#1a73e8>作者：</font>** Jose Miguel Ramos, Luis SaCouto, Andreas Wichert  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Biological neural systems achieve impressive computational capabilities under tight metabolic constraints, relying on sparse cortical representations that minimise total neural activity. This combination of efficiency and representational power has motivated growing interest in sparse coding as a computational strategy for artificial systems. Artificial models designed to produce binary sparse codes span three broad paradigms, theoretical methods grounded in efficient coding, deep learning methods trained via backpropagation, and biologically plausible methods that learn through local Hebbian rules, each yielding codes whose quality depends not only on achieving low activation density but also on preserving the informational structure of the input. The latter property, however, lacks an agreed-upon quantitative definition, leaving the field without a principled basis for comparing methods. We propose a set of metrics that formalise information preservation as similarity preservation, measuring how faithfully a binary sparse code reproduces the relational geometry of the input space, and apply this framework to compare four representative methods under matched conditions. The results reveal a consistent trade-off in which models that achieve high information preservation do so at the cost of sparsity, while models approaching the uniformity of an optimal random sparse code tend to sacrifice it. Competitive Sparse Codes, a biologically plausible approach, is the only architecture to occupy a region of near-maximal sparsity while retaining meaningful information preservation. These findings frame the simultaneous satisfaction of both factors as an open challenge for the field and provide a reusable evaluation framework for measuring progress toward it.

---


### 166. [Observable-Specific Validity Tests for Scientific AI: Controlled Approximations and Intervention Response](https://arxiv.org/abs/2610.41939)

**<font color=#1a73e8>作者：</font>** Xiaoshn Nee, Haobo Zhong, Xiaomin Ni  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An approximation can reproduce an energy while missing its response, or satisfy an error tolerance without being certified by a given bound. We formulate observable-specific validity records for scientific artificial intelligence (AI) that link a reduction to its reference model, error measure, tolerance, parameter domain, and transformations or interventions. Explicit displacement and velocity certificates for a singularly perturbed oscillator recover distinct convergence orders and provide sufficient validity guarantees. Exact Hubbard dimer relations resolve the different coupling domains accepted by energy and response criteria. Across 16 repeated neural fits, imposing dimensional homogeneity reduces energy scale transfer error from 52.3% to 0.0768% and raises the median fraction jointly satisfying gap and response tolerances from zero to 100%. Paired transformations verify the protected scaling relation, while a coupling crossover identifies the additional information needed for response transfer. A causal model recovers a positive intervention response beneath a strong negative observational association. For two mechanisms observed with Gaussian noise whose responses first differ at order $x^k$, we derive an exact fixed control query requirement scaling as $x^{-2k}$ and verify its full success curve numerically. Together with a 256-task evaluation interface, these results provide independently checkable tests of controlled approximation, physical transfer, and mechanism discrimination in scientific AI.

---


### 167. [Sensorium: An Open-Source Multimodal Data Collection and Curation Library for Embodied Surgical AI](https://arxiv.org/abs/2610.41946)

**<font color=#1a73e8>作者：</font>** Lorenzo Mazza, Ariel Rodriguez, Stefanie Speidel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Embodied surgical AI requires reliable multimodal data, yet surgical data collection remains costly, difficult to repeat, and strongly dependent on the hardware setup. We present Sensorium, an open-source Python library for recording, processing, annotating, and curating multimodal surgical data from configurable robot and sensor streams using the Robot Operating System (ROS) and ROS2 middleware. The library combines operator-facing data acquisition, configurable processing, semantic annotation, and episodic dataset generation. We evaluate Sensorium across 1516 recordings of phantom, ex vivo, and in vivo porcine experiments involving multiple surgical tasks and sensing configurations, and report preliminary usability feedback.

---


### 168. [Robust Learning of Multi-Index Models under Logconcave Distributions via Weak Partial Learners](https://arxiv.org/abs/2610.41961)

**<font color=#1a73e8>作者：</font>** Ilias Diakonikolas, Daniel M. Kane, Mingchen Ma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop a new algorithmic framework for learning Boolean concept classes under logconcave distributions. Our framework applies to broad families of multi-index models and yields significantly faster robust learners than were previously known in these settings. It extends to partial classification and testable learning. Consequently, we obtain improved learners for several fundamental concept classes, including functions of halfspaces and multiclass linear classifiers, under logconcave marginals.
Our starting point is a new boosting framework based on weak partial learners. Classical boosting approaches require often-intractable distribution-free weak learners or yield weak approximation guarantees. We show instead that weak learners for partial classification, where labels may be undefined on part of the domain, suffice for strong agnostic learning. The key challenge is that boosting requires a weak learner that succeeds under conditioned distributions that are not guaranteed to be logconcave. To address this, we develop a recursive moment-based partitioning procedure: given a logconcave distribution $X$ and a conditional version $X'$, we partition the space into polynomially many convex regions so that, on most regions, the low-degree moments of $X$ and $X'$ approximately agree. On each good region, a well-behaved multi-index model correlates with a low-degree polynomial, giving a weak hypothesis. Combining these hypotheses yields the required weak learner.
A key ingredient of our approach is an efficient method for detecting moment discrepancy. Specifically, we show how to find a low-dimensional subspace that captures any non-trivial discrepancy between $X$ and $X'$, if one exists. Our approach combines spectral analysis of moment tensors with recent progress on isoperimetry for logconcave measures. This discrepancy-finding procedure may be of independent interest.

---


### 169. [New Lower Bounds for Private PAC Learning](https://arxiv.org/abs/2610.41980)

**<font color=#1a73e8>作者：</font>** Prathamesh Dharangutte, Amartya Sanyal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study realizable PAC learning under approximate differential privacy, and give a framework for proving lower bounds on its sample complexity. We construct classes with identical VC and Littlestone dimensions but different private sample complexities at common privacy and accuracy parameters, showing that these dimensions do not determine the sample complexity, even for improper learners. To address this we introduce the Independent Class Packing (ICP) parameter, the largest total sample complexity of classes in $\mathcal{G}$ that can be packed independently into a class $\mathcal{H}$, and prove that every $(\varepsilon, \delta)$-DP, $(\alpha, \beta)$-PAC learner for $\mathcal{H}$, possibly improper, uses $\Omega\left(\mathrm{ICP}(\mathcal{H}, \mathcal{G})/(\alpha\varepsilon)\right)$ examples. Using this framework we prove tight lower bounds for axis-aligned rectangles, union of intervals and linear subspaces and improved lower bounds for halfspaces and convex polygons. Finally we also show that for product classes, and more generally when the same classes pack into $\mathcal{H}$ and cover its domain so that target labels can be used directly, ICP characterizes private PAC sample complexity up to logarithmic factors.

---


### 170. [FoAViS: Analyzing Learned Fixation Strategies in a Foveated Active Vision System](https://arxiv.org/abs/2610.41987)

**<font color=#1a73e8>作者：</font>** Valentin Hassler, Jonathan Henrich, Yohaï-Eliel Berreby 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human vision is foveated and active: resolution is highest at the fovea and falls off towards the periphery, and fixations are actively directed to locations of interest. Building a machine system that processes information in the same way lets us study gaze behavior in a controlled setting where the system's components and objectives are known. The emergence of gaze characteristics can therefore be examined systematically, which may in turn inform our understanding of biological vision. This requires a model that can sample like the fovea, handle various tasks from classification to dense prediction, and be trained concurrently with a fixation policy. In our study, we present such a system and study its capabilities and the fixation policies that emerge from it. Our system, FoAViS, samples visual input by adopting the established log-polar foveation and accumulates information in a 2D spatial memory. Due to its 2D structure, the same memory can be read out globally for classification or densely for semantic segmentation, without any architectural change. Fixations are drawn from a 2D map by a policy trained concurrently with the task. We find that learned fixation policies select more informative, task-specific locations than non-learned heuristics. These policies also shape the task representations in a beneficial way: for both classification and segmentation, models trained concurrently with a policy outperform models trained with random locations, even when the latter are provided with learned scanpaths. Moreover, these scanpaths exhibit similarities to human gaze behavior by capturing aspects of empirical scanpath characteristics. Our work marks an important step away from standard passive, single-pass architectures, towards biologically grounded models of vision. It opens a path for studying goal-directed gaze behavior and information representation in the visual system.

---


### 171. [AutoAnalysis: An automated, self-updating meta-analysis of human-AI collaboration](https://arxiv.org/abs/2610.42001)

**<font color=#1a73e8>作者：</font>** Michelle Vaccaro, Abdullah Almaatouq, Thomas W. Malone  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As generative artificial intelligence (AI) becomes more capable and widely used, understanding when and how humans should work with these systems is becoming increasingly important. However, the empirical evidence in this space offers conflicting recommendations, which leaves individuals and organizations without clear guidance on when to combine human and AI capabilities. Existing meta-analyses can help reconcile these findings, but they require substantial manual effort and cannot readily incorporate new evidence as it emerges. To address this challenge, we introduce AutoAnalysis: an automated, self-updating meta-analysis of when humans and AI work better together, and when they work better alone. AutoAnalysis' most recent run synthesizes 1,955 effect sizes from 420 papers. Across this body of work, we found that, on average, human-AI combinations performed significantly better than humans alone, but they performed significantly worse than the better of humans or AI alone. These findings highlight the important distinction between improving human performance and achieving human-AI synergy and underscore the need to evaluate collaboration against both human and AI performance alone. As new studies emerge, AutoAnalysis will integrate their findings into the meta-analysis, providing cumulative evidence about when humans and AI perform better together and how human-AI performance varies across AI agents, tasks, and processes.

---


### 172. [GeoFlip: Benchmarking Geometry-Sensitive Physics in Video Generation](https://arxiv.org/abs/2610.42002)

**<font color=#1a73e8>作者：</font>** Yuqi Li, Junming Liu, Bowen Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation models synthesize realistic motion, but can they respond correctly to changes in initial geometry? We introduce GeoFlip, a video generation benchmark centered on physical outcome flips induced by geometry. With shared physical settings and textual prompts held fixed, GeoFlip applies controlled interventions to support extent, object placement, and mechanism configuration, constructing paired scenes with contrasting reference events, such as remaining stable versus falling or tipping. These pairs test whether models translate geometric differences in the first frame into correct physical evolution. The benchmark comprises 482 scene pairs and 964 reference videos across six physical categories, with reference outcomes established through procedural scene construction, physics simulation, and numerical validation and verification of physical events. We evaluate 16 models for image to video generation along three dimensions: event correctness, structural integrity, and similarity to reference videos. We examine evaluation consistency with independent vision language judges. On the 442 conditions shared by all models, the highest event correctness averaged across tasks is 27.98%, revealing substantial limitations in physical generation conditioned on geometry. Model strengths vary across physical mechanisms, and the three evaluation dimensions capture distinct capabilities. Typical failures include ignoring geometric changes, generating incorrect object motion, bending rigid objects, and introducing additional components. Rank correlations between judges reach 0.906 for event correctness and 0.929 for structural integrity. By combining controlled geometric interventions, verifiable physical references, and multidimensional evaluation, GeoFlip assesses progress from visual realism toward physical consistency conditioned on geometry.

---


### 173. [When Does Jacobian Fine-Tuning Stabilize Neural PDE Emulators?](https://arxiv.org/abs/2610.42013)

**<font color=#1a73e8>作者：</font>** Shreeyam Bangera, Manya Gupta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural emulators of chaotic PDEs are trained on one-step prediction but deployed autoregressively, where their errors compound. Jacobian-based regularisers aim to curb this growth, but in a chaotic system part of the growth is physical and cannot be trained away. We separate the two sources of this error with a first-order decomposition. We compare the emulator's error with a counterfactual that propagates the same one-step mistakes through the solver's Jacobian, giving an amplification ratio: the factor by which the model's own dynamics amplify its errors. We study 21 configurations across four PDEs, five architectures and two model sizes (8-10k and 33k parameters), with errors measured at one Lyapunov time. Jacobian fine-tuning reduced the error by more than 10% for 1 of 34 seeds whose amplification ratio was at most 1.25, and for all 20 seeds whose ratio was at least four; for the latter, the error fell by a factor of 8 (small models) and 55 (33k models) in geometric mean over seeds. The gain approximately equals the one-step accuracy cost of fine-tuning divided by the amplification ratio. Matching the solver's Jacobian along the model's own error direction (EDJM) outperformed random directions at the same cost on 28 of 35 seeds; input-noise injection performed comparably to EDJM.

---


### 174. [GhostPrefix: Synchronization-Free Universal Prefix Attacks for ASR Manipulation](https://arxiv.org/abs/2610.42026)

**<font color=#1a73e8>作者：</font>** Shengding Liu, Ashwin Innuganti, Qiben Yan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present GhostPrefix, the first synchronization-free universal adversarial prefix attack against automatic speech recognition (ASR) systems. Unlike prior audio attacks, which are typically crafted per utterance, require synchronization with the victim waveform, or target narrow objectives, GhostPrefix learns a short, reusable audio segment prepended to arbitrary live speech to exert real-time control over ASR outputs without knowledge of the future utterance or temporal alignment. A key challenge is maintaining stable adversarial effects across unknown, evolving speech contexts. GhostPrefix combines token-level losses with a novel representation-level objective for stable, input-agnostic effects. GhostPrefix supports three attack modes: (i) prompted prefix attacks for semantic steering, (ii) targeted prefix attacks for transcript hijacking, and (iii) untargeted prefix attacks for transcription degradation. To remain perceptually inconspicuous, we regularize prefixes toward benign environmental-sound distributions and improve robustness against over-the-air distortions. We evaluate GhostPrefix across 13 open-source ASR models from four families. In digital settings, it achieves average attack success rates of 97.6% for prompted steering and 93.4% for targeted hijacking, while driving word error rate to 1.18 under untargeted attacks. Over the air, it achieves success rates of 91.5% and 89.5% for prompted and targeted modes, respectively. These manipulations propagate into downstream AI-assisted pipelines, including voice assistants and AI note-taking tools, causing systematic semantic misinterpretations. GhostPrefix exposes synchronization-free universal prefixes as a practical, under-explored threat to real-world ASR and downstream applications. Artifacts and demos are available at this https URL.

---


### 175. [CausalXRL: Explainable Reinforcement Learning through Causal Graph Reasoning](https://arxiv.org/abs/2610.42028)

**<font color=#1a73e8>作者：</font>** Yanming Zhang, Eric Papenhausen, Klaus Mueller  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning is a powerful paradigm for training autonomous agents and has achieved impressive performance in complex environments. However, this success often comes at the cost of interpretability, diminishing trust and complicating efforts to debug and improve agent behavior. To address these challenges, we introduce CausalXRL, a novel framework for explainable reinforcement learning (XRL). A key feature of CausalXRL is its use of causal graph reasoning, which provides transparent, structured, multi-level explanations of agent decision-making. We validate CausalXRL through comprehensive case studies and a two-part evaluation: (1) a quantitative analysis of explanation fidelity and causal-structure learning efficiency in benchmark RL environments, and (2) a qualitative expert study assessing explainability in the real-time strategy (RTS) benchmark MicroRTS. The quantitative results show that CausalXRL can provide faithful explanations while efficiently learning causal structures, and the qualitative expert study suggests that participants found CausalXRL useful for inspecting high-level RTS strategies.

---


### 176. [Any Forcing: Any-Step Generality and One-Step Stability for Autoregressive Video Generation](https://arxiv.org/abs/2610.42031)

**<font color=#1a73e8>作者：</font>** Jiahua Xu, Yijie Fang, Nannan Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video generation enables efficient inference through streaming prediction. However, existing methods are typically restricted to fixed sampling steps, limiting the flexibility to balance generation quality and efficiency, while one-step generation suffers from degraded visual quality and error accumulation over long sequences, leading to content drift and generation collapse. To address these issues, we propose Any Forcing, a unified framework for achieving Any-Step Generality and One-Step Stability. Specifically, we introduce a unified adversarial discriminator that jointly performs real-distribution alignment, inter-step consistency alignment, and first-frame quality enhancement, enabling flexible sampling while preserving one-step generation quality. Furthermore, we propose a training-free adaptive long-term memory selection mechanism that selects historical states based on global semantic relevance and local value contribution, while remapping their temporal positions to preserve temporal relationships within the memory cache, thereby enabling stable one-step long-video generation. Experiments demonstrate that Any Forcing achieves high-quality and stable one-step autoregressive video generation, achieving 20.9 FPS and 24.7 FPS for short and long video generation on a single H100 GPU, respectively.

---


### 177. [Learning Clean Generative Processes from Noisy Measurements](https://arxiv.org/abs/2610.42036)

**<font color=#1a73e8>作者：</font>** Fabian Kruse, Lorenzo Baldassari, Ivan Dokmanić  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study how to learn a generative model of clean images using only noisy observations. Diffusion processes and their generalizations to non-Gaussian noise require posterior predictions at every noise level. We first show that it is possible to learn these predictions from independent noisy views using Noise2Noise regression, but only at or above the noise level of the training data. To learn the predictions below that level, needed to generate clean images, we impose consistency: a prediction should equal its expectation after continuing the sampling process. We derive conditions under which consistency uniquely determines the continuation to the clean image distribution and verify them for Poisson, binomial, Gamma, and negative-binomial measurements. Experiments on CIFAR-10, photon-counting microscopy, and synthetic aperture radar show that the required posterior predictions can be learned from noisy views alone and that the consistency relation repairs the continuation beyond the noise level of the data, which severely deteriorates without consistency.

---


### 178. [A richness-sensitive Acoustic Biodiversity Index from species-level detections: classifier benchmarking, false-positive control and validation against standard soundscape indices in an African savanna and an urban zoo](https://arxiv.org/abs/2610.42042)

**<font color=#1a73e8>作者：</font>** Muhammad Saeed, Dmitry Mikhaylov, Mohamed H. Alhosani 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Acoustic indices are widely used as rapid proxies for biodiversity, but they summarise the distribution of sound energy rather than the species producing it and often track richness poorly. We revise and test an Acoustic Biodiversity Index (ABI) built from species-level detections. Its primary form, ABI_E, is Shannon diversity of detections normalised by the regional species pool expected at the site and season (H / ln S_ref); temporal stability T is reported as a separate component. We first benchmarked four classifiers on a strongly labelled tropical dataset (1,216 calls, 24 classes) with recording-grouped cross-validation. BirdNET embeddings + logistic regression performed best (macro-F1 0.750 +/- 0.029), and random frame-level splits inflated accuracy from 0.41 to 0.70. We then applied BirdNET v2.4 with a location and season filter to recordings from a riverine savanna in the Zambezi Valley, Zimbabwe, and from three habitats at Emirates Park Zoo and Resort, Abu Dhabi, United Arab Emirates. A stricter post-hoc location filter removed 517 high-confidence detections of 9 implausible species, all at the zoo. After diel-matched rarefaction to equal effort (6 h), the savanna site held 21 species (Hill number 1D = 9.83; ABI_E = 0.38) against 1.3-13 species (ABI_E = 0.03-0.21) at the zoo sites. Across 149 recorded hours, ABI_E correlated strongly with richness (Spearman rho = 0.93), whereas six standard indices did not (best: ACI, rho = 0.48). The stability term was lower at the savanna site (0.39) than at the zoo (0.65-0.67), showing that it penalises the natural diel cycle of bird activity. Species-level indices with explicit false-positive control, a declared regional reference pool and effort standardisation provide a more interpretable biodiversity indicator than energy-based acoustic indices.

---


### 179. [The Knowledge Layer Model (KLM): Evidence-Visible AI Output, Routing Diagnostics, and Negative Results](https://arxiv.org/abs/2610.42066)

**<font color=#1a73e8>作者：</font>** Omer Asim Ozturk, Cihan Aydiner  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI answers require more than apparent correctness: reviewers need to inspect their recorded basis. We introduce the Knowledge Layer Model (KLM), an open, implementation-neutral specification for inference records with versioned epistemic assessments, evidence relations, and explicit unknowns. SEDIM, the knowledge and evidence architecture of Nage AI OS, is a reference implementation. We reference KLM v0.3 (repository tag v0.3.0). Empirical material consists of separate internal experiments, not end-to-end validation. A historical platform-domain routing benchmark reports 137/150 classifications across 15 classes (91.3%; nominal 95% Wilson interval 85.7-94.9%); the numerator is recovered from a rounded summary, and historical example membership is unverified. A native-model weight-path configuration yielded 0/15 successful answers in a corrected two-source test. A capacity-growth comparison could not establish a reliable effect because of a defective legacy scorer and missing original outputs. Lexical and scoped diagnostics each yielded AUC 0.008 for silent-versus-contradicted examples, below the registered minimum of 0.65. Legacy packing lost gold-containing text in 118/221 selected cases; repaired packing retained it in 221/221. These measure text presence, not answer quality. Python and TypeScript verifiers reportedly agreed on six checks per synthetic fixture; a separate production disclosure was not accepted. Restoration, re-derivation, human-rubric support, boundary isolation, and bounded-response evaluations remain proposed. Findings are internal and author-reported; historical observations are distinguished from later reproductions. Evidence visibility does not establish correctness, causal reliance, security, or regulatory compliance. Independent replication and a complete public audit package remain future work.

---


### 180. [Differentially Private Synthetic Data from Sliced Chebyshev Moments](https://arxiv.org/abs/2610.42081)

**<font color=#1a73e8>作者：</font>** Lucas Rosenblatt, R. Teal Witter, Christopher Musco  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Research on practical differentially private (DP) synthetic data has largely focused on methods that approximately preserve low-dimensional marginals of a target distribution, and can thus only hope to preserve higher-dimensional, global structure as a lucky by-product. At the same time, existing methods that target global accuracy guarantees pay a price exponential in the data dimension, $d$.
In this work, we address this ``curse of dimensionality'' by presenting a new DP synthetic data algorithm, SPLICE, that comes with a compelling global distributional guarantee, even in high-dimensions, and moreover, is practically state-of-the-art. Our algorithm is based on measuring noisy sliced Chebyshev polynomial moments of the target distribution and fitting a distribution to match, a twist on recent polynomial methods for 1-D synthetic data.
We prove that, given a dataset of $n$ examples, SPLICE returns a private distribution with Sliced Wasserstein-1 distance $\tilde{O}(1/\sqrt{n})$ from the target, for constant privacy parameters. Notably, this bound is independent of the data dimension, $d$. Along the way, we prove a moment matching result of independent interest: for a distribution on the unit ball, matching the first $O(1/\alpha)$ Chebyshev moments along $\tilde{O}(d/\alpha^2)$ random directions guarantees $\alpha$ Sliced Wasserstein error.
Finally, we provide a practical implementation of the algorithm that borrows tools from the tensor decomposition literature and achieves state-of-the-art performance compared to prior DP synthetic data methods on an extensive benchmark.

---


### 181. [Cost-Aware Stopping for Freeze-Thaw Bayesian Optimization: When Does One-Step Lookahead Suffice?](https://arxiv.org/abs/2610.42085)

**<font color=#1a73e8>作者：</font>** Long Vu, Jongseong Brad Choi, Binoy Ravindran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Freeze-thaw Bayesian optimization (BO) evaluates candidates in resumable increments but usually stops at a budget or convergence test. We maximize a budget-free utility, the best observed score minus a cost per increment, with a one-step lookahead: advance the candidate with the largest expected improvement (EI) under a fixed surrogate, and stop once no EI exceeds the cost. This rule, EI stopping, never falls below stopping immediately in expected utility, yet it can stop too early. We construct a certificate, a lower bound on the value of two-step lookahead, that proves such a stop premature, and repeating this correction never lowers expected utility under the surrogate. Under the surrogate, EI stops are premature on average at low costs and lose little at high costs. On three hyperparameter optimization benchmarks, a pre-registered test finds EI stopping noninferior to the correction in most high-cost settings, while the correction gains at low costs on two of the three; more information sharing in the surrogate raises EI stopping's utility. On the surrogates of two published methods, EI stopping trades lower scores for fewer training increments. EI stopping is a simple cost-aware reference whose utility depends on the surrogate.

---


### 182. [Rethinking Asymmetry in Self-Supervised 3D Geometry Learning](https://arxiv.org/abs/2610.42092)

**<font color=#1a73e8>作者：</font>** Gyeongjin Kang, Freeman Cheng, Botao Ye 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning relies on asymmetry between what a model observes and what it must explain. Recent methods learn 3D geometry from unposed images by predicting cameras and scene structure, then rendering held-out views. To avoid trivial solutions, they impose this asymmetry in the input space, restricting how views interact through separate branches or masked attention. We revisit this design with geometric accuracy, rather than rendering quality, as the main objective. When a held-out view lies between context views, the context already constrains the geometry it observes. We therefore impose the asymmetry in the 3D representation space, excluding held-out views only from the reconstructed scene while a shared backbone uses all views for correspondence. This improves depth and pose estimation over input-space designs. We further exploit view density: sparse and dense observations depict the same scene but provide different amounts of correspondence. Aligning sparse-context features with dense-context features supplies a geometric training signal alongside rendering, without a pretrained geometric teacher. We additionally align features with a frozen vision foundation model, which brings further gains. None of these signals requires geometric annotation, and the resulting model improves geometry estimation over prior self-supervised methods. Controlled experiments isolate the contribution of each component, and self-supervised pretraining also improves subsequent supervised training.

---


### 183. [CausalWAM: Learning the Causes of Actions in World Action Models](https://arxiv.org/abs/2610.42096)

**<font color=#1a73e8>作者：</font>** Juntao Cheng, Jinzhou Tang, Fan Feng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World action models (WAMs) learn latent variables from observations and use these to both predict the evolution of the scene and to generate actions. The prediction has to be of the whole scene, whereas only a portion of the scene causes actions. WAMs fitted to demonstrations do not, in general, guarantee that they will generate actions solely from the latent causes of the demonstrated actions (the action-relevant latent variables), as the model could just as well learn to imitate in this way whilst entangling the action-relevant latent variables with the nuisance variables. We therefore separate out what causes action from what prediction depends on. We prove that under a sparsity constraint the latent variables used to generate actions are an invertible function of the action-relevant latent variables alone and the true structure is identified up to a permutation of the latent variables. This requires neither sufficient temporal dependence nor any assumptions on how the unobserved regimes evolve and holds even when the action-relevant latent variables are statistically dependent on the rest. We therefore propose CWAM (Causal WAM), which incorporates the constraint into a pretrained WAM by adding a sparse routing path to its action head, with the world modeling objective remaining unchanged. Experiments on both synthetic data and real-world robots validate the theory as well as showcase the improved efficiency in closed-loop success.

---


### 184. [Towards Understanding the Impact of Plasticity Loss on Reinforcement Learning in Stochastic Environments](https://arxiv.org/abs/2610.42100)

**<font color=#1a73e8>作者：</font>** Philipp Bordne, André Biedenkapp  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep reinforcement learning (RL) is a powerful framework for sequential decision-making. Despite many high-profile successes in recent years, deep RL is known to be brittle. An emerging line of research attributes this brittleness to a loss of plasticity in neural networks. However, plasticity loss has so far been understudied in stochastic environments. We study this interplay systematically, training SAC agents on three DeepMind Control tasks augmented with controlled levels of observation and action noise. We find that plasticity-preserving methods increase learning robustness on the two harder tasks, with their advantage growing as observation noise increases, while combining resets with layer normalization underperforms resets alone at every observation noise level tested. Further, stochasticity can accelerate the loss of plasticity in harder environments, whereas in easier settings noise can act as a regularizer that sustains plasticity. Lastly, plasticity loss is most pronounced in the early stages of training. In the most challenging stochastic settings, TD instability rather than gradual plasticity loss becomes the dominant failure mode.

---


### 185. [Hyperbolic Inverse Reinforcement Learning](https://arxiv.org/abs/2610.42104)

**<font color=#1a73e8>作者：</font>** Iulia Rusu, Anoop Praturu, Sergei Gepshtein 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inverse reinforcement learning (IRL) seeks to infer the reward function underlying observed behavior, but its predictive accuracy and interpretability depend on how that reward is computed from the underlying features. While prior IRL reward functions have been implemented through a variety of techniques including linear weights, neural networks, or other function approximators, none make assumptions about the geometry of the underlying feature space. Inspired by geometric organization observed in neural circuits, we introduce Hyperbolic inverse reinforcement learning (Hyperbolic IRL), which parameterizes reward as a function of Hyperbolic distance between the feature vector and a learned parameter vector, as well as its Euclidean distance variant. We tested our methods against a range of linear and nonlinear IRL baselines under both deterministic and stochastic policies. Our Hyperbolic approach achieved comparable performance to state-of-the-art models on established benchmarks and excelled in the low data limit and across dense environments. Applied to human navigation among multiple exhibits in a museum room, Hyperbolic IRL reveals reward structure that depends not only on individual exhibit-distance features, but also on non-separable conjunctions between them. Together, these results demonstrate that a Hyperbolic reward parameterization can improve both the predictive accuracy and interpretability of IRL, providing a framework for studying how non-separable, conjunctive structure can begin to explain behavior.

---


### 186. [Fast Privacy Loss Accounting for Random Allocation via Multiscale FFT](https://arxiv.org/abs/2610.42117)

**<font color=#1a73e8>作者：</font>** Vitaly Feldman, Moshe Shenfeld  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the random allocation sampling scheme each user's data is used in $k$ steps chosen randomly and uniformly from a sequence of $t$ steps. This scheme is known to improve on Poisson sampling in private optimization and in communication-efficient aggregation. The existing privacy loss distribution (PLD) accountant for this scheme runs in time quadratic in the inverse of the accuracy parameter $\alpha$ (Feldman and Shenfeld, 2026). We give an algorithm, \emph{multiscale FFT}, that represents likelihood ratios on a grid that is uniform within each dyadic interval and computes the exact rounding of every pairwise sum using FFTs within each interval. It keeps the guarantees of the accountant and improves the dependence of its running time on $\alpha$ from $O(\alpha^{-2})$ to $O(\alpha^{-1}\log(1/\alpha))$. In addition, we demonstrate that rounding can be performed via the mean-preserving connect-the-dots projection of (Doroshenko et al., 2026). This reduces the errors that rounding introduces in the mean of the privacy loss and in the $\chi^2$ divergence of the computed pair from the order of $\alpha$ to $O(\alpha^2/\log(t))$. In our experiments, our algorithm achieves speedups of several orders of magnitude at high accuracy and gives improved privacy bounds for DP-SGD with PREAMBLE.

---


### 187. [Gradient Descent on Two ReLU Neurons: Global Landscape and Bifurcation Dynamics](https://arxiv.org/abs/2610.42118)

**<font color=#1a73e8>作者：</font>** Binghua Li, Mengzhe Li, Denny Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding how gradient descent learns features remains a central challenge in neural network theory. We study this question in a minimal multi-index setting that already exhibits rich multi-phase gradient dynamics: a well-specified two-neuron ReLU teacher-student model under isotropic Gaussian inputs, trained by population gradient flow from small initialization. We show that the dynamics are organized by two directions: the "easy" bisector direction, which carries the leading signal, and the "hard" splitting direction, which governs specialization. To characterize the loss structure and learning behavior, we analyze the population squared-loss landscape and show that every critical point with both student weights nonzero is either a global minimum or a saddle. We then track the gradient-flow trajectory, showing that student neurons first collapse toward a bisector saddle before escaping and specializing to teacher neurons. Our results provide both a landscape and dynamics account of the multi-phase symmetry-breaking behavior that arises in a simple multi-index model and under standard algorithmic and architectural choices.

---


### 188. [Physiological Trajectories and Observation Patterns in ICU Mortality Prediction: Transportability Under Changing Measurement Conditions](https://arxiv.org/abs/2610.42126)

**<font color=#1a73e8>作者：</font>** Benjamin T. Pike  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Objective: To distinguish the transferable predictive value of physiological trajectories from that of observation patterns in ICU mortality prediction, and to assess whether measurement timing affects performance independently of observation quantity.
Materials and Methods: In-hospital mortality was predicted at 48 hours using MIMIC-III, MIMIC-IV, and eICU. Nested representations progressively integrated latest-value snapshots (R1), longitudinal physiological summaries (R2), and measurement frequency and timing features (R3). Models fitted on 7,762 MetaVision patients were evaluated on 21,682 MIMIC-IV patients and 43,878 eICU patients across 204 hospitals. The effect of measurement timing was assessed while holding the number of retained observations constant.
Results: Physiological trajectories improved external prediction in eICU (R2-R1 log-loss difference -0.00922, 95% CI -0.01148 to -0.00704). Observation-pattern features improved locally developed eICU models (R3-R2 -0.00257, 95% CI -0.00370 to -0.00146), but not clearly after transfer from MetaVision (-0.00012, 95% CI -0.00206 to +0.00208). R3 was favoured in 10 of 30 source bootstrap refits. At matched observation counts, retaining measurements spread throughout the window reduced log loss relative to random retention by 0.03280 for R3 versus 0.00703 for R2. Removing the final 12 hours increased log loss relative to count-matched random removal by 0.01947 for R3 versus 0.00822 for R2. Under reduced availability, the local R3 increment changed from beneficial to harmful.
Discussion: Physiological trajectories transferred more consistently, while observation-pattern features were particularly sensitive to the timing and availability of measurements.
Conclusion: Clinical prediction models should be evaluated not only in new patient populations but also under the measurement conditions that supply their inputs.

---


### 189. [Instance-dependent sequential limits as an exact information ledger](https://arxiv.org/abs/2610.42133)

**<font color=#1a73e8>作者：</font>** Akshay Balsubramani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Instance-dependent limits for bandit regret, sequential tests, best-arm identification and Markov decision processes are proved by one chain. It runs from a divergence decomposition through data processing to a statistic, a testing step that turns a class guarantee into a requirement on the history, and optimization over alternatives and allocations. Only the first step is an identity. This work writes the chain as an exact ledger. By the chain rule, data processing loses exactly a conditional divergence, which vanishes for arms in natural exponential families at the per-arm counts and reward sums. A one-parameter family of martingale identities extends the decomposition to every tilt between two instances. The classical limits follow by relaxations with named defects. All defects but the asymptotic step's can be computed from an algorithm's own runs, the uniform quantification's only when the class guarantee is a number. On seven published sources, from movie ratings to engine replacement, the ledger locates the difference between standard algorithms and the classical limits. For identification among trained models and for Wald's test the largest term is usually the uniform quantification's.

---


### 190. [A Better Critic Matters for Distribution Matching Distillation](https://arxiv.org/abs/2610.42135)

**<font color=#1a73e8>作者：</font>** Zongze Wu, Xianbang Wang, Zhengyang Geng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Distribution Matching Distillation (DMD) trains a few-step student using the difference between a teacher's score and an online critic's estimate of the student distribution's score. We investigate what the critic needs, in capacity and in information, to provide a reliable training signal. On the capacity side, controlled experiments across seven SiT model sizes on ImageNet show that increasing teacher size while keeping a small critic fixed can degrade student quality and cause training collapse. Scaling the critic alongside the teacher, a strategy we call joint scaling, prevents collapse in our experiments and allows the student to benefit from larger teachers. On the information side, rather than forcing the critic to model a step-agnostic mixture of student outputs, we introduce a step-aware critic (STAC) that conditions on the student's generation step to estimate step-specific scores. Together, joint scaling and STAC consistently improve few-step distillation across class-conditional ImageNet generation, text-to-image generation with SDXL and FLUX.2, and text-to-video generation with Wan2.1.

---


### 191. [ReLift: Dense 3D Tracking as Lifted Trajectory Repair](https://arxiv.org/abs/2610.42136)

**<font color=#1a73e8>作者：</font>** Assaf Singer, Maroun Khriesh, Noam Rotstein 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dense 3D tracking from monocular video requires establishing point correspondences over time, estimating their depth, and inferring their trajectories during occlusion. Existing methods typically learn these tasks jointly, a demanding objective given the scarcity of 4D supervision. We show that strong pretrained 2D trackers and 3D geometry models provide an effective foundation: lifted trajectories, with occluded segments simply interpolated, already rival dedicated 3D trackers using the same geometry. However, lifted trajectories inherit correspondence and depth errors, and under occlusion, their depth comes from the occluder rather than the tracked point. We introduce ReLift, an efficient feed-forward framework that recasts dense 3D tracking as geometric trajectory repair and completion. At its core, a trajectory corrector alternates attention along and across trajectories to preserve reliable observations, repair corrupted positions, and complete missing motion. Using only geometric inputs allows us to train directly on 3D trajectories with simulated lifting errors, decoupling training from images and from any specific tracker or geometry model. Concentrating 4D supervision on trajectory refinement yields a reusable model that consistently improves lifted trajectories across trackers and geometry providers without retraining, so it benefits directly from future advances in either component. On WorldTrack, ReLift achieves state-of-the-art mean accuracy, improving on the strongest baselines by 2.1 APD on all points and 3.0 on dynamic points, with faster configurations remaining competitive with leading 3D trackers while running faster than 4RC. Visit our supplementry page for more examples and code.

---


### 192. [Counting on Dummies: Privacy Amplification with Observable Counts and Truncated Batches](https://arxiv.org/abs/2610.42139)

**<font color=#1a73e8>作者：</font>** Vitaly Feldman, Audra McMillan, Kunal Talwar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many practical deployments of Differentially Private Stochastic Gradient Descent (DP-SGD), the server processes data in batches. Randomly sampling these batches allows for better privacy bounds via privacy amplification results. Most sampling schemes with provable privacy amplification, including Poisson sampling and random allocation, result in variable batch sizes. The privacy guarantee of these schemes requires that the batch sizes are not revealed. In distributed settings, the server performing the aggregation or any party observing the communication traffic may learn these batch sizes. Furthermore, in both centralized and distributed settings, memory and computation constraints may require each batch to be of some maximum size $s$, necessitating truncation of the batch when it exceeds this limit. It is known that this truncation can result in a significant increase in privacy loss. In this work, we address both of these challenges via a simple mechanism that uses a random number of \emph{dummy points} to privatize the batch size and maintain the privacy guarantee even under truncation. We demonstrate that our mechanism is easy to implement in a distributed setting, and provide a general analysis of this mechanism for both Poisson sampling and random allocation. Our analysis is designed to support efficient and relatively tight privacy accounting. It also effectively amplifies the privacy of the count releases by subsampling, making the expected number of dummy points asymptotically smaller than what is needed to directly privatize the (sensitivity-one) batch sizes with non-negative noise. For Poisson sampling with truncated batches, we demonstrate empirically that our mechanism achieves better privacy--efficiency tradeoffs than the direct accounting for truncation recently given by (Ganesh, 2025).

---


### 193. [GazeRIB: Systematic Evaluation of Multi-Reader Gaze-Guided Chest X-ray Learning](https://arxiv.org/abs/2610.42152)

**<font color=#1a73e8>作者：</font>** Nattakorn Kittisut, Roy M. Gabriel, Marly van Assen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiologists' visual attention can supervise medical image learning, but how reader panel composition affects its value remains untested. We evaluated GazeRIB (Gaze-guided Radiologist-Informed Blackout), which masks unviewed regions during training and uses unmasked images at inference. Eight experts repeatedly read the same 80 chest X-rays (CXRs). We compared individual readers with three-, five- and eight-reader panels across seven architectures and 10 seeds, evaluating 910 models on a separate 2,897-CXR cohort for four-class severity prediction. Every panel improved macro F1 over the no-gaze baseline by 5.33-7.47 percentage points (pp; Bonferroni-adjusted p < 0.007); no individual reader reached significance on this endpoint. Three readers captured 73-80% of the eight-reader gain in macro F1, the area under the receiver-operating-characteristic curve (ROC-AUC) and the area under the precision-recall curve (AU-PRC). On external validation without retraining, all four panels improved ROC-AUC on SIIM-FISABIO-RSNA by +1.93 to +4.24 pp (p <= 0.004); on MIMIC-Eye no panel differed significantly from baseline, whereas the single-reader average declined (-1.40 pp, p = 0.008). Reader composition therefore influenced performance, although transfer depended on the cohort.

---


> [!TIP]
> 当前位于：**151-193**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-193**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
