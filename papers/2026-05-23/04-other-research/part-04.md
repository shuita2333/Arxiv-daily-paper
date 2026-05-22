# 📦 其他研究 | 2026年05月23日

> 本类共 **347** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-347](./part-07.md)

---

### 151. [Zero-Shot Temporal Action Localization Through Textual Guidance](https://arxiv.org/abs/2605.22201)

**<font color=#1a73e8>作者：</font>** Benedetta Liberatori, Alessandro Conti, Lorenzo Vaquero 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot temporal action localization (ZS-TAL) consists of classifying and localizing actions in untrimmed videos, where action classes are unseen at training time. Existing work uses Vision and Language Models (VLMs), taking advantage of their strong zero-shot transfer capabilities. Yet, these models face evident challenges with fine-grained action classification, making it difficult to directly use them to distinguish between the presence and absence of an action. Most current methods for ZS-TAL address these challenges by training models on large-scale video datasets, which require annotated data and often result in limited generalization performance. Recently, approaches discarding the use of labeled data have emerged as an alternative. Following this direction, we propose a novel approach, ``Textual Guidance for finer localization of actions in videos'' (TEGU), that compensates for the lack of supervision from training data by exploiting rich textual information derived from large language models and structured text extracted from captions. This additional linguistic context can improve fine-grained discrimination by providing richer cues about fine-grained action differences within videos. We validate the effectiveness of the proposed method by conducting experiments on the THUMOS14 and the ActivityNet-v1.3 datasets. Our results show that, by exploiting rich textual information for improved action localization, TEGU outperforms state-of-the-art ZS-TAL approaches that do not involve training

---


### 152. [Structure Retention in Embedding Spaces as a Predictor of Benchmark Performance](https://arxiv.org/abs/2605.22202)

**<font color=#1a73e8>作者：</font>** Amanda Myntti, Jenna Kanerva, Veronika Laippala 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper, we show that high-performing embedding models organize their embedding spaces in a consistent way. We evaluate 25 contemporary embedding models on five MTEB tasks spanning four diverse task categories (retrieval, bitext mining, pair classification, and summarization) in both English and multilingual settings, and reveal that nearest-neighbor overlap and magnitude differences in independent component analysis (ICA) between paired text instances strongly correlate (even up to 0.97) with performance on the given task. Ultimately, we show that embedding tasks display varying degrees of linearity and reliance on retention of local information. Our results further the understanding of embeddings, their relation to model performance, and shed light on possible future training objectives and optimizing conditional embeddings.

---


### 153. [Evaluation of Chunking Strategies for Effective Text Embedding in Low-Resource Language on Agricultural Documents](https://arxiv.org/abs/2605.22203)

**<font color=#1a73e8>作者：</font>** Sovandara Chhoun, Pichdara Po, Sereiwathna Ros 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this study, we compare the performance of four text chunking approaches: Recursive, Khmer-Aware, Sentence-Based, and LLM-Based within a Retrieval-Augmented Generation (RAG) framework applied to Khmer agricultural documents. The document chunks are encoded using the BGE-M3 multilingual embedding model and retrieved using the FAISS library. Performance is evaluated using four metrics: Average Retrieval Score (L2 distance), Answer Relevance, Khmer Coverage, and Khmer Intersection over Union, all measured against ground-truth question-answer pairs. For evaluation, we perform 5-fold cross-validation over 18 question-answer pairs. We observe the best performance for the character-based Recursive chunking method with a chunk size of 300 characters, achieving the lowest L2 distance (0.4295 +- 0.0461), highest Answer Relevance (0.8663 +- 0.0199), and highest Khmer IoU (0.6441 +- 0.0347). A paired t-test shows a statistically significant improvement over the Sentence-Based chunking method in L2 distance (p = 0.0121). These results highlight the importance of segmentation granularity and structural preservation for optimizing dense retrieval in morphologically complex, low-resource languages such as Khmer.

---


### 154. [Audience Engagement with Arabic Women's Social Empowerment and Wellbeing: A Decadal Corpus](https://arxiv.org/abs/2605.22204)

**<font color=#1a73e8>作者：</font>** Wajdi Zaghouani, Mabrouka Bessghaier, MD. Rafiul Biswas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents the Arabic Women and Society Corpus, a ten year collection of 252,487 public Arabic Facebook posts related to women's empowerment and social wellbeing. The corpus was collected from 51,660 pages across 77 countries between 2013 and 2024, resulting in more than 267 million user interactions. Each post includes engagement metrics such as shares, comments, and emotional reactions, providing a unique view of audience sentiment and social attention. The data were processed using an automated pipeline with language identification, normalization, and metadata cleaning to ensure reliability and reproducibility. The corpus enables large scale analysis of gender discourse, social reform, and emotional engagement across Arabic dialects. It supports research in Arabic natural language processing, computational social science, and digital communication studies. The dataset and accompanying documentation will be released under request for research use.

---


### 155. [GALAR-TemporalNet v2: Anatomy-Guided Dual-Branch Temporal Classification with Bidirectional Mamba and Dual-Graph GCN for Video Capsule Endoscopy -- after competition results](https://arxiv.org/abs/2605.22209)

**<font color=#1a73e8>作者：</font>** Jiye Won, Seangmin Lee, Soon Ki Jung  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Capsule Endoscopy (VCE) poses a challenging multi-label temporal classification problem, requiring simultaneous localization of 8 anatomical regions and detection of 9 pathological findings across tens of thousands of frames. We present GALAR-TemporalNet v2, a hierarchical temporal model that addresses three core challenges: extreme class imbalance, long-range temporal dependencies, and pathology--anatomy entanglement. Our architecture combines windowed self-attention for local modeling, a Dual-Graph GCN for global frame relationships, and Bidirectional Mamba for selective boundary context encoding. A novel anatomy prototype residual pathway decouples pathological deviation signals from normal organ appearance, and a frame-level GCN skip connection stabilizes training of visually confusable rare classes. The competition version, GALAR-TemporalNet, achieved an overall mAP@0.5 of 0.2644 and mAP@0.95 of 0.2353 on the RARE-VISION test set. Following the competition, the redesigned GALAR-TemporalNet v2 -- incorporating a restructured pathology branch, refined loss functions, and extended post-processing -- improved these results to mAP@0.5 of 0.3409 and mAP@0.95 of 0.3333.

---


### 156. [Towards a compositional semantics for quantitative confidence assessment in assurance arguments](https://arxiv.org/abs/2605.22213)

**<font color=#1a73e8>作者：</font>** Benjamin Herd, Jessica Kelly, Jan Sabsch 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Assurance arguments provide a clear and structured way to explain why stakeholders should trust that a system satisfies certain properties, yet widely used notations, this http URL Structuring Notation (GSN), typically lack an operational semantics for deriving assurance confidence. Existing approaches address structure and soundness but largely reason over truth values, not over confidence in the justification of claims. Subjective Logic (SL) offers a calculus of belief, disbelief, and uncertainty with operators for combining opinions, enabling confidence propagation under incomplete, conflicting, or subjective evidence. However, existing SL-based approaches do not provide a uniform, compositional semantics that covers all argument elements and relations to enable overall confidence assessment. We propose a confidence semantics that represents argument elements as SL opinions and maps relations between elements to SL operators modelling how confidence flows, effectively turning the argument into an analyzable confidence network. The approach provides explicit warrants, principled handling of context, preserved provenance, and compatibility with GSN, along with practical guidance using an exemplary assurance confidence assessment.

---


### 157. [A Robust Semantic Segmentation Pipeline for the CVPR 2026 8th UG2+ Challenge Track 2](https://arxiv.org/abs/2605.22216)

**<font color=#1a73e8>作者：</font>** Jinming Chai, Libo Yan, Licheng Jiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This report presents our solution for the WeatherProof Dataset Challenge, namely CVPR 2026 8th UG2+ Challenge Track 2: Semantic Segmentation in Adverse Weather. For the semantic segmentation task under adverse weather conditions, we propose a semi-supervised segmentation pipeline. Our method is trained exclusively on the WeatherProof dataset, without using any additional external data. Specifically, we adopt UniMatch V2 as the baseline model and treat all degraded-weather images as unlabeled data for semi-supervised training, thereby fully exploiting the data distribution provided by the challenge. During inference, we further apply test-time augmentation to improve the robustness and segmentation accuracy of the final predictions. The code is publicly available at: this https URL.

---


### 158. [Survive or Collapse: The Asymmetric Roles of Data Gating and Reward Grounding in Self-Play RL](https://arxiv.org/abs/2605.22217)

**<font color=#1a73e8>作者：</font>** Sophia Xiao Pu, Zhaotian Weng, Chengzhi Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-play reinforcement learning trains language models on their own generated tasks, co-evolving a proposer and solver without human labels. Recent systems report strong reasoning gains, but collapse and instability are widely observed and poorly understood. The dominant response treats this as a reward-design problem. We argue instead that self-play stability is governed by two distinct levers: a data-level gate that decides which proposer-generated tasks enter the training pool, and the reward signal that updates the policy on tasks already admitted. Through controlled experiments on a Python output-prediction task and a deterministic-DSL twin task that strips pretraining priors, output ambiguity, and executor noise, we find the two levers are asymmetric. A strict gate is sufficient for stability under every reward variant we test, including a self-consistency reward with no access to ground truth; while no reward variant is sufficient once the gate is removed. This asymmetry exposes a counter-intuitive coupling we call the Grounded Proposer Paradox: a proposer with ground-truth access accelerates collapse faster than an ungrounded one when paired with a self-consistency solver, by concentrating training on clean tasks that form the fastest path to a spurious self-consistent attractor. Replacing the binary gate with a continuous strictness parameter $\varepsilon$ further reveals a two-stage phase transition: training-side metrics decouple at low $\varepsilon$, while validation accuracy holds until $\varepsilon$ is much higher. Data-level gating, not reward calibration, is the binding constraint on self-play stability.

---


### 159. [Can Transformers Learn to Verify During Backtracking Search?](https://arxiv.org/abs/2605.22221)

**<font color=#1a73e8>作者：</font>** Yin Jun Phua, Tony Ribeiro, Tuan Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Backtracking search underlies classical constraint solvers, planners, and theorem provers. Recent transformer-based reasoning systems explore search trees over their own intermediate steps. A common training recipe fits an autoregressive next-token loss on offline solver traces. The model's input at each step is a cumulative trace of all prior decisions. The optimal continue-or-backtrack predictor depends only on the current search state, since two trajectories reaching the same state admit the same viable continuations. We show that decoder-only transformers trained on cumulative traces fail this requirement in two ways: the trace can scatter state features across many positions (scattered retrieval), and the predictor can condition on the trajectory rather than the state (history entanglement). We address scattered retrieval with localization, a trace-level fix that rewrites each decision block to expose state features locally. We address history entanglement with Selective State Attention (SSA), a fixed attention mask that enforces state-based decisions structurally without modifying training data, objective, or parameters. We focus on reactive verification, after propagation has exposed a contradiction. We test SSA on 3-SAT, graph coloring, Blocks World, and backtracking parsing. On same-state pairs that differ only in prior history, SSA emits identical decisions while a cumulative-trained causal baseline does not. Our contribution is a diagnostic of transformer behavior on serialized trajectory data, paired with a structural fix. Pretrained language models that search over their own reasoning steps may face the same failure. Our analysis opens up inference-time context clearing as a candidate way to apply the same isolation without retraining.

---


### 160. [How Many Different Outputs Can a Transformer Generate?](https://arxiv.org/abs/2605.22223)

**<font color=#1a73e8>作者：</font>** Maxime Meyer, Mario Michelessa, Caroline Chaux 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study how we can leverage only a handful of characteristics of a transformer's architecture to closely predict the number of different sequences it can output, both qualitatively and quantitatively. We provide an upper bound depending on the length of the prompt, which we show empirically to be tight up to a factor less than 10, across architectures and model sizes. Our analysis also provides a theoretical explanation for previously observed empirical failures of transformers on simple sequence tasks, such as copying and cramming. Formally, we prove that (i) the maximal length of accessible sequences (those that the transformer can output for some prompt) grows linearly with the prompt length, (ii) beyond a critical threshold, the proportion of accessible sequences decays exponentially with sequence length, and (iii) the linear coefficient relating prompt length to accessible sequence length admits a theoretical upper bound. Notably, these results hold even with unbounded context and computation time.

---


### 161. [GHI: Graphormer over Conditioned Hypergraph Incidence for Aspect-Based Sentiment Analysis](https://arxiv.org/abs/2605.22228)

**<font color=#1a73e8>作者：</font>** Yu Du, Wenlong Zhu, Xingze Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aspect-based sentiment analysis (ABSA) requires models to bind sentiment evidence to the correct aspect, making it a natural testbed for fine-grained structural reasoning. We introduce GHI, a Graphormer-over-Conditioned-Hypergraph-Incidence framework that is designed as an incidence-based structural reasoning layer built on a bipartite topology. GHI represents diverse linguistic and semantic evidence as token--hyperedge incidence relations, allowing different structural signals to be incorporated through a unified interface. Extensive experiments on six standard ABSA benchmarks show that GHI outperforms all baselines on the SemEval domains, and multi-seed evaluations show stable improvements over strong DeBERTa. Further experiments show that with only 247M parameters, GHI approaches the performance of 11B Flan-T5 based methods on the ISE benchmark. Moreover, it demonstrates strong robustness on the challenging ARTS datasets, maintaining highly competitive performance where traditional models degrade. These results demonstrate that compact structural reasoning remains a valuable alternative to scale-driven approaches for fine-grained tasks.

---


### 162. [REACH: Hand Pose Estimation from Room Corners](https://arxiv.org/abs/2605.22231)

**<font color=#1a73e8>作者：</font>** Shu Nakamura, Ryo Kawahara, Genki Kinoshita 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce a novel 3D hand pose estimator that can accurately recover the shape and pose of people's hands in a room from afar, typically from fixed cameras at room corners, in extremely low-resolution and frequently occluded views. Our key idea is to fully leverage hand-body coordination, its temporal progression, and multiview observations. We achieve this with a novel Transformer-based model, in which hand and body configurations are modeled through correlations between their visual features expressed as per-view tokens, and their temporal coordination is exploited in an autoregressive manner. We introduce a novel dataset, which we refer to as REACH, Room-Environment dataset Annotated with Chest cameras for Hand pose estimation, to train and test our method. REACH is a first-of-its-kind large-scale hand pose dataset that captures accurate hand movements of 50 participants across a wide variety of daily activities. In order to avoid interfering with natural movements while annotating the hands with accurate shape and pose, we leverage concealed chest cameras. Through extensive experiments, including comparative studies with existing methods, we show that our model, REACH-Net, achieves highly accurate 3D hand pose estimation from afar. These results broaden the horizon of 3D hand pose estimation, especially towards "in-the-wild" continuous human behavior analysis.

---


### 163. [Holomorphic Neural ODEs with Kolmogorov-Arnold Networks for Interpretable Discovery of Complex Dynamics](https://arxiv.org/abs/2605.22235)

**<font color=#1a73e8>作者：</font>** Bhaskar Ranjan Karn, Dinesh Kumar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Complex dynamical systems governed by holomorphic maps such as $z^2 + c$ exhibit fractal boundaries with extreme sensitivity to initial conditions. Accurately modelling these structures from data requires methods that respect the underlying complex-analytic geometry, yet Multi-Layer Perceptrons (MLPs) within Neural Ordinary Differential Equations (Neural ODEs) lack complex-analytic priors, violate the Cauchy--Riemann conditions, and function as opaque approximators incapable of yielding governing equations. We introduce Holomorphic KAN-ODE, a framework that replaces the MLP with a Kolmogorov-Arnold Network (KAN) whose learnable B-spline activations reside on network edges, and incorporates Cauchy--Riemann equations as a differentiable regularization to preserve holomorphic structure. We evaluate on six families of complex dynamical systems spanning polynomial and transcendental classes. With only 280 parameters ($16\times$ fewer than the MLP baseline), the network achieves velocity-field $R^2 > 0.95$ on all six systems, correctly identifies all six governing symbolic families through automatic spline-to-formula fitting, and reconstructs Julia set fractal boundaries with up to 98.0\% agreement. Crucially, the model exhibits only 4\% MSE degradation under 10\% observation noise versus $15.2\times$ for MLPs, and achieves 90.4\% improvement in transfer learning from quadratic to cubic dynamics. While the MLP attains lower pointwise reconstruction error due to its larger capacity, the KAN uniquely provides interpretable symbolic equations, enforced holomorphic structure, and superior noise resilience, capabilities that are entirely absent in black-box architectures. These results establish KANs as a parameter-efficient, interpretable alternative to MLPs for physics-informed discovery of holomorphic dynamics.

---


### 164. [Decision-Aware Quadratic ReLU Replacement for HE-Friendly Inference](https://arxiv.org/abs/2605.22237)

**<font color=#1a73e8>作者：</font>** Rui Li, Wenyuan Wu, Weijie Miao  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fully homomorphic encryption (FHE) supports only additions and multiplications, so FHE-only neural-network inference typically replaces ReLU with polynomials fitted over empirical activation intervals. Such interval fitting often requires higher-degree polynomials to control activation error, incurring homomorphic evaluation costs, while classification is determined by the final logit decision. We revisit ReLU replacement from a decision-aware perspective: given a trained single-hidden-layer ReLU MLP and a specified calibration set, can an HE-friendly low-degree polynomial replace ReLU without retraining while preserving calibration-set decisions? We focus on quadratic replacement, the lowest-degree choice that retains a genuine per-unit nonlinearity. For calibration sets positive-margin separable in the lifted space, we formulate quadratic replacement as a linear separation problem, yielding necessary and sufficient conditions for calibration-lossless replacement and a constructive algorithm for the coefficients. When the positive-margin condition fails -- typically due to a few misclassified calibration samples -- we extend the same geometric framework via reduced convex hulls and Lagrangian-dual soft-margin relaxations, which bound the influence of any single sample, converting the problem into smaller convex quadratic programs that yield approximately feasible coefficients with high empirical agreement on calibration-set decisions. In particular, at the maximal weight cap $\mu=1$, the reduced-convex-hull relaxation reduces to the convex-hull separation of the strictly separable case; the relaxation thus continuously extends the exact theory. Under CKKS, the quadratic replacement matches plaintext top-1 accuracy on multiple benchmarks, running 3.7--4.1$\times$ faster than Remez-7 in the activation module and 1.18--1.68$\times$ faster end-to-end.

---


### 165. [Unlocking Proactivity in Task-Oriented Dialogue](https://arxiv.org/abs/2605.22240)

**<font color=#1a73e8>作者：</font>** Hongbin Zhang, Ning Gao, Yuqin Dai 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Proactive task-oriented dialogue (TOD), such as outbound sales, demands a persuasive agent that actively probes the user's concerns and steers the conversation toward acceptance within a bounded number of turns. Yet post-trained LLMs are inherently conservative, and reward-shaping RL (e.g., GRPO) struggles since it only re-weights what an already passive policy samples. We show that conditioning on the user's latent concerns unlocks proactive capability that no amount of sampling can undermine, establishing these concerns as a pivotal training-time signal. To operationalize this finding, we build the \textbf{Cognitive User Simulator}, which models each user as a stratified persona comprising observable external traits and hidden internal concerns. The simulator produces faithful and diverse interactions, while emitting per-turn state dynamics that track persuasion progress. We then introduce \textbf{Simulator-Induced Asymmetric-View Policy Optimization}, which converts the modeled concerns and the simulation state transition into complementary training objectives: (1) \emph{Asymmetric On-Policy Self-Distillation} that transfers concern-aware behavior from a privileged view of the same policy into its deployable, conversation-only view; and (2) \emph{State-Transition Policy Refinement} ...

---


### 166. [Decomposing Ensemble Spread in Lorenz '96 With Learned Stochastic Parameterizations](https://arxiv.org/abs/2605.22242)

**<font color=#1a73e8>作者：</font>** Birgit Kühbacher, Daan Crommelin, Niki Kilbertus  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weather and climate forecasts are inherently uncertain due to chaotic dynamics, imperfect initial conditions, and incomplete representation of the underlying physical processes. Operational ensemble forecasts aim to represent these uncertainties through forecast spread, yet many approaches yield underdispersive estimates, with spread that grows too slowly relative to forecast error. Using the two-scale Lorenz 1996 system as a widely used, controlled testbed, we design a systematic approach to disentangle intrinsic variability, initial-condition perturbations, and stochastic model uncertainty. We compare multiple ensemble configurations and parameterization strategies, including existing deterministic and autoregressive as well as novel Bayesian and flow-based approaches. Our results show that ensemble perturbations do not increase the system's long-term variance; rather, they regulate how rapidly trajectories decorrelate and explore the invariant measure. Stochastic parameterizations, particularly those with temporally persistent structure, enhance early spread growth and improve spread-error consistency. Overall, we bring clarity to how different sources of uncertainty interact in a chaotic system and provide guidance for the design and evaluation of stochastic parameterizations in weather and climate models.

---


### 167. [Explainable AI for Data-Driven Design of High-Dimensional Predictive Studies](https://arxiv.org/abs/2605.22243)

**<font color=#1a73e8>作者：</font>** Junyu Yan, Damian Machlanski, Kurt Butler 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive modelling is important for health data analysis and data-driven clinical decision-making. However, predictive studies are challenging to design optimally by hand when tens or even hundreds of features require selection, transformation, or interaction modelling. While complex machine learning models offer high performance, their "black-box" nature limits the clinical trust, transparency, and interpretability required for decision-making. We developed and evaluated an Exploratory AI Recommender that provides data-driven recommendations to improve predictive performance of existing interpretable statistical models. The developed framework uses flexible AI modelling to capture complex data patterns and explainable AI techniques to translate the patterns into three recommendation types: feature exclusion, non-linear terms, and feature interactions. We evaluated the framework by comparing predictive performance of a baseline (i.e., no interactions or non-linear terms) Cox Proportional Hazards (CPH) model against an augmented CPH incorporating recommendations suggested by our method. The primary analysis predicts the time to the first occurrence of a fall or related injury in 245,614 patients. Our method recommended excluding 23 features, including non-linear terms for two features, and including 221 suggested feature interactions. The C-index improved from 0.805 (95% CI 0.798-0.812) to 0.815 (95% CI 0.809-0.822), and so did calibration (intercept: -0.006 to 0.003; slope: 1.063 to 0.950). All recommendations were supported by existing literature. The method also proved effective on two additional public datasets, demonstrating wider applicability. The proposed Exploratory AI Recommender demonstrates the potential of explainable AI and data-driven study design to improve the process of developing, and the performance of high-dimensional transparent predictive models.

---


### 168. [IdioLink: Retrieving Meaning Beyond Words Across Idiomatic and Literal Expressions](https://arxiv.org/abs/2605.22247)

**<font color=#1a73e8>作者：</font>** Kai Golan Hashiloni, Daniel Fadlon, Lior Livyatan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Idioms pose a fundamental challenge for language models, as their meaning cannot be inferred from surface form alone. Understanding such expressions, therefore, requires semantic abstraction beyond lexical overlap. We introduce IdioLink, a retrieval benchmark designed to test whether models can link idiomatic expressions to conceptually equivalent meanings expressed in literal or paraphrased forms. IdioLink comprises 10,700 documents and 2,140 queries, spanning 107 idioms with both literal and figurative uses. Each document and query is annotated with spans that convey the core meaning. Evaluating strong embedding baselines (e.g., BGE, E5, Contriever, and Qwen), we show that current models struggle to retrieve equivalent meanings across divergent surface realizations, relying instead on topical and shallow semantic cues. IdioLink exposes key gaps in idiom-aware semantic retrieval and provides a challenging testbed for future models.

---


### 169. [No Epoch Like the Present: Robust Climate Emulation Requires Out-of-Distribution Generalisation](https://arxiv.org/abs/2605.22248)

**<font color=#1a73e8>作者：</font>** Bradley Stanley-Clamp, Anson Lei, Hannah M. Christensen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Climate emulation is an out-of-distribution (OOD) projection task. This is precisely the challenge where modern Machine Learning (ML) methods are most prone to failure. Consequently, while current ML emulators trained on present climate achieve high in-distribution performance, their future reliability under the inevitable distribution shifts of a changing climate remains a critical, poorly understood blind spot. Addressing this challenge requires a fundamental shift in how we understand, evaluate, and design climate emulators. In this work, we first confirm that climate change drives a statistically significant and progressively growing shift in atmospheric state distributions, rendering standard evaluation protocols insufficient. We empirically establish that seasonal variation serves as an effective proxy for these long-term climate shifts, providing access to $\textit{real-world}$ distribution shifts without recourse to heuristics like synthetic perturbations. Motivated by this link, we introduce a novel evaluation framework that leverages seasonal shifts as a rigorous, zero-overhead testbed for emulator robustness. Our systematic characterisation confirms that current state-of-the-art hybrid-ML emulators degrade significantly under these realistic shifts. Finally, we chart a path forward by identifying compositional generalisation, the ability to form novel combinations from observed elementary components, as a principled route towards robust climate emulation. We demonstrate that physically motivated decompositions substantially improve OOD performance with only modest trade-offs against in-distribution performance, providing an avenue towards ML-driven climate emulators robust to an unknown future.

---


### 170. [D3Seg: Dependency-Aware Diffusion for Brain Tumor Segmentation with Missing Modalities](https://arxiv.org/abs/2605.22249)

**<font color=#1a73e8>作者：</font>** Danish Ali, Ajmal Mian, Naveed Akhtar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate brain tumor segmentation using multiparametric MRI is critical for effective treatment planning. However, in clinical settings, complete acquisition of all MRI sequences is not always possible. The absence of certain MRI modalities results in substantial performance degradation in existing segmentation methods, which typically rely on naive feature concatenation or direct fusion strategies. To address this limitation, we propose a novel segmentation model D3Seg which is designed to maintain stable performance under missing-modality settings. D3Seg introduces Multi-hop Modality Graph Fusion (MMGF) to model higher order inter-modality dependencies, a lightweight diffusion-based imputation mechanism to compensate for missing T1ce representations in latent space, and probability-space decision refinement to mitigate dominant class overconfidence and improve delineation of underrepresented tumor subregions. Extensive evaluation on BraTS 2023 dataset demonstrates that our D3Seg model consistently improves segmentation performance under missing modality configurations. The proposed model achieves approximately 1.5-2.0% Dice improvement on enhancing tumor (ET) and around 1.0% on tumor core (TC) across multiple missing modality configurations compared to the current state-of-the-art model, while maintaining computational efficiency.

---


### 171. [Direct content-based retrieval from music scores images](https://arxiv.org/abs/2605.22255)

**<font color=#1a73e8>作者：</font>** Noelia Luna-Barahona, Antonio Ríos-Vila, David Rizo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The digitization of musical scores plays a crucial role in their preservation and accessibility, yet information retrieval still depends mainly on metadata searches, such as by title or composer. Content based search in music score images remains underexplored compared to text documents, despite its potential value for musicians, musicologists, and educators. This work contributes to the field by first studying which characteristics of a score are most relevant for search and by defining a systematic method to build query datasets from any annotated corpus. We also consider diverse methods for content-based search on music score images, ranging from transcription-based approaches relying on Optical Music Recognition (OMR), to a transcription-free Transformer model trained to recognize queries directly from score images, and a text-prompted Large Language Model. Our experiments evaluate these models on four corpora exhibiting diverse characteristics in terms of dataset size, image quality, and typesetting mechanisms. Overall, each method excels under different conditions: OMR-based pipelines achieve higher in-domain retrieval, whereas transcription-free models handle domain variability more effectively.

---


### 172. [Emergence of agriculture in an artificial society of reinforcement learning agents](https://arxiv.org/abs/2605.22256)

**<font color=#1a73e8>作者：</font>** Gautier Hamon, Martí Sánchez-Fibla, Clément Moulin-Frier 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The origin of agriculture represents a major evolutionary transition and a paradigmatic example of how complex collective behaviors emerge from simple interactions. Here we introduce an artificial society of reinforcement learning agents embedded in a dynamic ecological environment to identify general principles underlying this transition. Within this system, agricultural practices emerge spontaneously - without explicit instruction - through the coupled dynamics of learning and environmental modification. We show that this transition is governed by four key ingredients: individual planning through the valuation of delayed rewards, social vulnerability to cheaters, stabilization via social learning, and an emergent lock-in effect that renders agriculture effectively irreversible once established. In particular, we demonstrate that social learning acts as a "firewall" that suppresses cheater invasion and enables the propagation of successful strategies, leading to sustained population growth and nonlinear amplification of domesticated resources. Together, these results reveal universal mechanisms linking individual decision-making, social interactions, and ecological feedbacks. More broadly, they highlight the potential of artificial societies as experimental platforms to study the emergence of cultural innovations and major evolutionary transitions.

---


### 173. [What are the Right Symmetries for Formal Theorem Proving?](https://arxiv.org/abs/2605.22257)

**<font color=#1a73e8>作者：</font>** Krzysztof Olejniczak, Radoslav Dimitrov, Xingyue Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Formal theorem provers based on large language models (LLMs) are highly sensitive to superficial variations in problem representation: semantically equivalent statements can exhibit drastically different proof success rates, revealing a failure to respect structural symmetries inherent in formal mathematics. This raises a central question: what are the right symmetries for formal theorem proving? We introduce rewriting categories, a category-theoretic framework capturing the compositional, generally non-invertible transformations induced by proof tactics, and use it to formalize two symmetry notions: proof equivariance, governing how proof distributions transform under rewrites, and success invariance (i.e., invariance of success probability), requiring equivalent statements to be solved with the same probability. We observe that state-based next-tactic provers naturally satisfy proof equivariance by operating on proof states. In contrast, state-of-the-art LLM-based provers satisfy neither property, exhibiting large performance variation across equivalent formulations. To mitigate this, we propose test-time methods that aggregate over equivalent rewritings of the input, showing theoretically that they recover success invariance in the sampling limit, and empirically, that they improve robustness and performance under fixed inference budgets. Our results highlight symmetry as a key missing inductive bias in LLM-based theorem proving and suggest test-time computation as a practical route to approximate it.

---


### 174. [An Evidence Hierarchy for Bayesian Object Classification via OSINT-Aided Heterogeneous Sensor Fusion](https://arxiv.org/abs/2605.22259)

**<font color=#1a73e8>作者：</font>** Jan Nausner, Michael Hubner  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Heterogeneous sensor fusion is vital for detecting, localizing, and classifying CBRNE threats. However, individual sensors are often only capable of detecting a subset of relevant threats with varying reliability or can even provide only indirect threat indications, making threat classification challenging. Furthermore, high clutter rates on the sensor side present a great challenge for fusion systems. Additionally, the limited availability of high quality datasets hinders the advancement of learning-based detection and classification models in smart sensors. To mitigate these sensor related shortcomings, a context-aware and domain knowledge-enhanced fusion process is proposed. First, a novel evidence hierarchy is established that enables modeling of direct, indicative, and contextual information. Second, contextual information about the environment is introduced into the fusion process, by collecting, processing, and exploiting OSINT inputs. Third, all levels of the evidence hierarchy are used to craft a Bayesian threat type classification mechanism with domain knowledge-informed priors. The proposed methodology is evaluated in simulated scenarios, and the results demonstrate the benefit of the proposed fusion approach in terms of robustness to clutter and prior mismatch, with an overall classification accuracy of up to 95%.

---


### 175. [Detecting Atypical Clients in Federated Learning via Representation-Level Divergence](https://arxiv.org/abs/2605.22266)

**<font color=#1a73e8>作者：</font>** Cristian Pérez-Corral, Jose I. Mestre, Alberto Fernández-Hernández 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning enables collaborative training across distributed clients with heterogeneous data, but such heterogeneity often leads to unstable updates and degraded global performance. Moreover, in practical deployments, client updates may deviate from the expected behavior not only due to benign not i.i.d. distributions, but also due to distributional shifts or anomalous inputs, raising concerns about the reliability of the aggregation process. In this work, we propose a lightweight geometric signal to quantify the functional deviation of a client with respect to the global model. Instead of comparing model parameters or gradients, our approach measures how the local training of each client alters the activation-induced partition of the input space, evaluated on a shared probe set. This yields a permutation-invariant, interpretable metric of client--global divergence that captures differences in how data is processed by the model. We show that this signal effectively identifies clients that induce atypical functional changes, distinguishing stable yet heterogeneous clients from those whose updates significantly diverge from the global regime. As a result, the proposed metric provides a simple tool for monitoring client behavior and enabling risk-aware aggregation strategies in federated learning systems.

---


### 176. [MuKV: Multi-Grained KV Cache Compression for Long Streaming Video Question-Answering](https://arxiv.org/abs/2605.22269)

**<font color=#1a73e8>作者：</font>** Junbin Xiao, Jiajun Chen, Tianxiang Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long streaming video QA remains challenging due to growing visual tokens and limited reasoning length of large language models (LLMs). KV-caching stores the Key-Value (KV) of the historical tokens via LLM prefill and enables more efficient streaming QA. However, existing methods cache every one or two frames, causing redundant memory usage and losing fine-grained spatial details within frame or temporal contexts across frames. This paper proposes MuKV, a method that features a multi-grained KV cache compression module and a semi-hierarchical retrieval approach to improve both efficiency and accuracy for long streaming VideoQA. For the offline KV cache, MuKV extracts visual representations at patch-, frame-, and segment-levels. The multiple levels of granularity preserve both local cues and global temporal context, while maintaining efficiency with a dual signal token compression mechanism guided by self-attention and frequency. For online QA, MuKV designs a semi-hierarchical retrieval method to retrieve relevant KV caches for answer generation. Experiments on long-streaming VideoQA benchmarks show that MuKV significantly improves answer accuracy, without sacrificing memory and online QA efficiency. Moreover, our compression mechanism alone brings consistent benefits across answer accuracy, memory, and QA efficiency over baselines, showcasing highly effective contribution.

---


### 177. [Exposing Vulnerabilities in Visible-Infrared VLMs: A Unified Geometric Adversarial Framework with Cross-Task Transferability](https://arxiv.org/abs/2605.22273)

**<font color=#1a73e8>作者：</font>** Xiang Chen, Yuxian Dong, Chao Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have achieved strong performance across diverse multimodal tasks, but their adversarial robustness in visible-infrared (VIS-IR) scenarios remains underexplored. This gap is critical because VIS-IR sensing is widely used in real-world perception systems to support reliable understanding under challenging imaging conditions. To address this cross-modal threat setting, we propose CFGPatch, a curved-edge fractal geometric adversarial patch framework for attacking VIS-IR VLMs. CFGPatch builds on triangular fractal geometry and replaces rigid straight-edged primitives with Bezier-curved elements, preserving multi-scale fractal self-similarity while introducing smoother contours, richer directional variation, and more flexible shape deformation. In addition, we design a modality-specific Fraser-spiral rendering mechanism to inject fine-grained texture distortions and misleading perceptual cues into visible and infrared images. By coupling global curved-fractal geometry with local spiral-based appearance interference, CFGPatch disrupts both shape perception and texture interpretation. We further adopt expectation over transformation (EOT) to improve robustness against common image-level transformations. Extensive experiments show that CFGPatch effectively fools VIS-IR VLMs and consistently outperforms standard patch baselines in attack effectiveness and robustness. Moreover, adversarial samples optimized for zero-shot classification transfer well to image captioning and visual question answering, demonstrating strong cross-task transferability and generalizability across downstream tasks.

---


### 178. [Adaptive Measurement Allocation for Learning Kernelized SVMs Under Noisy Observations](https://arxiv.org/abs/2605.22275)

**<font color=#1a73e8>作者：</font>** Artur Miroszewski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kernel methods are typically formulated under the assumption of exact, noise-free access to the Gram matrix. However, in emerging settings such as quantum machine learning, each kernel entry must be inferred from noisy observations, and its accuracy depends on how a limited measurement budget is allocated. Despite this, existing approaches overwhelmingly rely on uniform allocation, which equalizes estimator variance but ignores the highly non-uniform dependence of kernelized classifiers on the Gram matrix. In this work, we introduce an adaptive measurement-allocation strategy for learning kernelized Support Vector Machines (SVMs) from noisy Bernoulli observations. Our approach combines two complementary principles: (i) geometric sensitivity, capturing how perturbations of individual kernel entries affect the classifier margin, and (ii) active-set instability, quantifying the probability of discrete changes in support-vector membership induced by measurement noise. These signals define a task-aware allocation scheme that concentrates measurements on the most decision-critical regions of the kernel matrix. We provide a theoretical analysis showing that the benefit of adaptive allocation is governed by the heterogeneity of the induced kernel importance structure, leading to distinct regimes in which adaptive or uniform strategies are preferable. Empirical evaluations on synthetic datasets demonstrate that adaptive allocation significantly improves support-vector recovery, margin estimation, and decision-function accuracy under fixed measurement budgets. A dual-coefficient stability criterion further enables early stopping, achieving near-optimal performance while using only a fraction of the measurement cost. Additional experiments on quantum kernels derived from real-world data reveal a regime-dependent behavior aligned with known phenomena such as kernel concentration. Together...

---


### 179. [EmoTrack: Robust Depression Tracking from Counseling Transcripts across Session Regimes](https://arxiv.org/abs/2605.22286)

**<font color=#1a73e8>作者：</font>** Zhaomin Wu, Jiayi Li, Bingsheng He  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Text-based counseling is an important interface for AI mental-health support, where transcripts may be used to monitor depression severity and flag sessions requiring timely human review. However, robust PHQ-8 prediction across session regimes remains challenging: fine-tuning-based methods can exploit richer supervision but may generalize poorly under data scarcity, while prompt-based LLM methods are data-efficient but usually treat each transcript holistically and provide limited support for longitudinal context. We study robust depression tracking from counseling transcripts across single-session and multi-session regimes. We introduce LongCounsel, a multi-session counseling dataset with session-level PHQ-8 supervision for evaluating repeated-session tracking under partial symptom disclosure and cross-session continuity. We further propose EmoTrack, a PHQ-8 prediction framework that combines LLM-extracted clinical signals with frozen turn-level semantic embeddings and trains symptom-specific predictors over the resulting transcript representation. When prior sessions are available, EmoTrack can further incorporate them through compact cross-session memory. Experiments on LongCounsel and DAIC-WOZ show that EmoTrack achieves a clear gain on the real single-session benchmark, including a 13.5% relative MAE reduction over the strongest DAIC-WOZ baseline, and remains competitive with the strongest longitudinal baseline on LongCounsel.

---


### 180. [Detection of Virus and Small Cell Patches in Foci Images Using Switchable Convolution and Feature Pyramid Networks](https://arxiv.org/abs/2605.22290)

**<font color=#1a73e8>作者：</font>** Amrita Singh, Snehasis Mukherjee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate detection and counting of virus patches in focus-forming unit (FFU) images, also known as foci images, are important for quantifying viral infection and analyzing cellular structures. This task is challenging because biomedical targets often vary substantially in size, density, contrast, and shape. In this paper, we propose an enhanced YOLOv2-based detector that integrates a Feature Pyramid Network (FPN) to improve multi-scale feature representation. We also incorporate a switchable atrous convolution mechanism to adapt the receptive field for fine-grained targets in dense microscopy images. The proposed method is evaluated on biomedical foci image datasets for virus patch and small cell patch detection. For small cell patch detection, the model achieves a mean average precision (mAP) of 40.5% at a 25% Intersection over Union (IoU) threshold. For FFU virus patch detection, the model achieves an mAP of 68%. These results indicate that combining FPN-based feature fusion with switchable convolution improves the suitability of YOLOv2 for specialized biomedical object detection tasks

---


### 181. [Long-term Fairness with Selective Labels](https://arxiv.org/abs/2605.22291)

**<font color=#1a73e8>作者：</font>** Giovani Valdrighi, Isabel Valera, Marcos Medeiros Raimundo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-term fairness algorithms aim to satisfy fairness beyond static and short-term notions by accounting for the dynamics between decision-making policies and population behavior. Most previous approaches evaluate performance and fairness measures from observable features and a label, which is assumed to be fully observed. However, in scenarios such as hiring or lending, the labels (e.g., ability to repay the loan) are selective labels as they are only revealed based on positive decisions (e.g., when a loan is granted). In this paper, we study long-term fairness in the selective labels setting and analytically show that naive solutions do not guarantee fairness. To address this gap, we then introduce a novel framework that leverages both the observed data and a label predictor model to estimate the true fairness measure value by decomposing it into the observed fairness and bias from label predictions. This allows us to derive sufficient conditions to satisfy true fairness from observable quantities by using the confidence in the predictor model. Finally, we rely on our theoretical results to propose a novel reinforcement learning algorithm for effective long-term fair decision-making with selective labels. In semisynthetic environments, the proposed algorithm reached comparable fairness and performance to an agent with oracle access to the true labels.

---


### 182. [Cross-domain benchmarks reveal when coordinated AI agents improve scientific inference from partial evidence](https://arxiv.org/abs/2605.22300)

**<font color=#1a73e8>作者：</font>** Fiona Y. Wong, Markus J. Buehler  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific evidence often spans instruments, databases, and disciplines, so no single source records the full phenomenon. This makes it difficult to determine when coordinated AI agents add value over simpler scientific workflows. We evaluate this question with a cross-domain benchmark spanning four scientific tasks: mapping molecular structure into musical representations, detecting historical paradigm shifts in science, identifying vector-borne disease emergence, and vetting transiting-exoplanet candidates. Each case uses a frozen evaluation panel, predefined scoring protocols, explicit baselines, ablations or null controls, and stated limitations. The results define three operating regimes. When different disciplines each capture only part of the phenomenon, cross-channel composites improve over single-channel baselines: climate-vector emergence reaches AUROC 0.944 and exoplanet vetting reaches AUROC 0.955. However, the exoplanet workflow is effectively tied with a strong combined-summary baseline, showing that decomposition does not always improve top-line performance. When one signal dominates, as in paradigm-shift detection, coordination mainly improves interpretation and traceability. For molecular sonification, the gain is representational rather than predictive. ScienceClaw x Infinite provides the auditable artifact and provenance layer for this evaluation. The benchmark therefore assigns value to coordination only when the corresponding performance, provenance, or representation claim is supported by explicit comparators.

---


### 183. [Evaluation of Pipelines for Data Integration into Knowledge Graphs](https://arxiv.org/abs/2605.22304)

**<font color=#1a73e8>作者：</font>** Marvin Hofer, Erhard Rahm  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Integrating new data into knowledge graphs (KG) typically involves different tasks that are executed within workflows or pipelines There are many possible pipelines for a specific integration problem but there is not yet a general approach to evaluate the overall quality and performance of such pipelines to be able to determine the best choices. We therefore propose a new benchmark KGI-Bench to evaluate integration pipelines that ingest different kinds of input data into an existing KG. We evaluate pipelines by analyzing their output, i.e., the updated KG, with the three complementary quality metrics coverage, correctness and consistency. We also provide benchmark datasets (seed KG, overlapping input data of three formats, reference KG as a ground truth) for the movie domain. To demonstrate the applicability and usefulness of the proposed benchmark, we comparatively evaluate 12 pipelines and analyze their behavior across different input data formats and design choices.

---


### 184. [Chebyshev Policies and the Mountain Car Problem: Reinforcement Learning for Low-Dimensional Control Tasks](https://arxiv.org/abs/2605.22305)

**<font color=#1a73e8>作者：</font>** Stefan Huber, Hannes Unger, Georg Schäfer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We analytically solve the Mountain Car problem, a canonical benchmark in RL, and derive an optimal control solution, closing a gap after 36 years. This enables us to reveal two surprising insights: The optimal control is quite simple, yet modern RL agents display a large gap to optimality. Motivated by the analysis of the optimal control, we introduce Chebyshev policies as a universal (i.e. dense) class of RL policies from first principles. They can be trained as drop-in replacements of neural nets, reducing the regret by a factor of 4.18, while requiring 277 times fewer parameters, fostering sample efficiency, explainability and realtime capability. Chebyshev policies are evaluated on further RL tasks, including a real-world nonlinear motion control testbed. They consistently improve performance over neural nets with PPO, ARS and REINFORCE. Our results demonstrate how Chebyshev policies offer a compelling and lightweight alternative or addition to neural nets for low-dimensional control tasks.

---


### 185. [ACCoRD: Actor-Critic Conflict Resolution with Deep learning for O-RAN xApps](https://arxiv.org/abs/2605.22306)

**<font color=#1a73e8>作者：</font>** Cezary Adamczyk, Adrian Kliks  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Conflict Mitigation (ConMit) is a crucial part of intelligent network control in Open Radio Access Networks (O-RAN). In this paper, we propose a method named ACCoRD to resolve detected control conflicts in Near-Real Time RAN Intelligent Controller using a Conflict Resolution (CR) Agent with an Artificial Neural Network (ANN) trained with a reinforcement learning algorithm PPO-Clip. The implemented ANN analyzes data about the network and conflicting control decisions to infer optimal CR actions. The CR Agent gathers feedback from the network after each resolved conflict to assess its efficiency and adjust the ANN's weights during batch training. The evaluation of the proposed approach is based on simulation data. A new methodology for evaluating CR solutions is proposed. Results show that the proposed ANN-based method improves on the efficiency of rule-based approaches by significantly reducing negative network events caused by conflicting control decisions in medium and high traffic scenarios.

---


### 186. [Pattern-and-root inflectional morphology: the Arabic broken plural](https://arxiv.org/abs/2605.22310)

**<font color=#1a73e8>作者：</font>** Alexis Amid Neme, Eric Laporte  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a substantially implemented model of description of the inflectional morphology of Arabic nouns, with special attention to the management of dictionaries and other language resources by Arabic-speaking linguists. The breakthrough lies in the reversal of the traditional root-and-pattern Semitic model into pattern-and-root, giving precedence to patterns over roots. Our model includes broken plurals (BPs), i.e. plurals formed by modifying the stem. It is based on the traditional notions of root and pattern of Semitic morphology. However, as compared to traditional Arabic morphology, it keeps the formal description of inflection separate from that of derivation and semantics. As traditional Arabic dictionaries, the updatable dictionary is structured in lexical entries for lemmas, and the reference spelling is fully diacritized. In our model, morphological analysis of Arabic text is performed directly with a dictionary of words and without morphophonological rules. Our taxonomy for noun inflection is simple, orderly and detailed. We simplify the taxonomy of singular patterns by specifying vowel quantity as v or vv, and ignoring vowel quality. Root alternations and orthographical variations are encoded independently from patterns and in a factual way, without deep roots or morphophonological or orthographical rules. Nouns with a triliteral BP are classified according to 22 patterns subdivided into 90 classes, and nouns with a quadriliteral BP according to 3 patterns subdivided into 70 classes. These 160 classes become 300 inflectional classes when we take into account inflectional variations that affect only the singular. We provide a straightforward encoding scheme that we applied to 3 200 entries of BP nouns.

---


### 187. [PIU: Proximity-guided Identity Unlearning in ID-Conditioned Diffusion Models](https://arxiv.org/abs/2605.22311)

**<font color=#1a73e8>作者：</font>** Jose Edgar Hernandez Cancino Estrada, Mauro Díaz Lupone, Žiga Emeršič 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Identity-conditioned diffusion models enable high-quality and identity-consistent face generation, but they also raise severe privacy concerns, as models may continue to synthesize individuals despite their right to be forgotten. While machine unlearning has been extensively studied for concept and data removal, identity unlearning remains largely unexplored, particularly in models conditioned directly on identity embeddings rather than text prompts. In this work, we study identity unlearning in Arc2Face, a state-of-the-art identity-conditioned latent diffusion model for face generation, and introduce Proximity-guided Identity Unlearning (PIU), an anchor-guided framework for identity unlearning. Specifically, we formulate identity removal as an identity replacement objective that reassigns the source identity to a selected anchor identity in the learned identity space, and we complement it with a proximity-based anchor selection strategy motivated by the geometry of ArcFace representations. We further show that effective unlearning can be achieved through localized fine-tuning of a small subset of identity-sensitive cross-attention layers. Experiments across many target identities show that our framework effectively suppresses generation of the target identity while preserving realism and identity consistency for retained identities, as validated by improved performance on unlearning and image-quality metrics, together with qualitative evaluation. The source code for the PIU framework is publicly available at this https URL .

---


### 188. [Benchmarking Autonomous Agents against Temporal, Spatial, and Semantic Evasions](https://arxiv.org/abs/2605.22321)

**<font color=#1a73e8>作者：</font>** Jianan Ma, Xiaohu Du, Ruixiao Lin 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As autonomous agents (e.g., OpenClaw) increasingly operate with deep system-level privileges to execute complex tasks, they introduce severe, unmitigated security risks. Current vulnerability analyses overwhelmingly focus on single-turn, stateless behaviors, overlooking the expanded attack surface inherent in stateful, multi-turn interactions and dynamic tool invocations. In this paper, we propose a novel, multi-dimensional evasion framework targeting LLM-based agent systems. We introduce three stealthy attack vectors: (1) Temporal evasion, which fragments malicious payloads across sequential interaction turns; (2) Spatial evasion, which conceals payloads within complex external artifacts that evade standard LLM parsing mechanisms; and (3) Semantic evasion, which obscures malicious intents beneath benign contextual noise. To systematically quantify these threats, we construct A3S-Bench, a comprehensive benchmark comprising 2,254 real-world agent execution trajectories. Evaluating a standard agent framework separately integrated with 10 mainstream LLM backbones against 20 practical threat scenarios, we demonstrate that our evasion framework elevates the average risk trigger rate from a 28.3\% baseline to 52.6\%. These findings reveal systemic, architecture-level vulnerabilities in current autonomous agent systems that existing defenses fail to address, highlighting an urgent need for defense mechanisms tailored to the unique threats.

---


### 189. [PACT: Reducing Alert Fatigue in Low-Prevalence SOC Streams with Triggered Active Learning](https://arxiv.org/abs/2605.22324)

**<font color=#1a73e8>作者：</font>** Samuel Ndichu, Tao Ban, Seiichi Ozawa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security operations centers face persistent alert fatigue: in low-prevalence streams, even low false-positive rates generate substantial investigation load, while aggregate F1 scores obscure analyst burden. We introduce PACT, a Pareto-aware controller for triggered active learning, which wraps an already-deployed frozen XGBoost-Focal screener with an adaptive windowing score-shift trigger and a hybrid acquisition rule combining threshold-relative uncertainty with high-score sampling. On two public low-prevalence benchmarks, AIT-ADS (AIT Alert Data Set), and BOTSv1 (Boss of the SOC version 1), PACT attains the lowest benign-normalized false-positive (FP) burden among the adaptive methods tested. It reduces burden by 43% and 21%, respectively, relative to a frozen baseline, while using 3.8x and 5.2x fewer analyst queries than periodic uniform-random updating. A matched-trigger ablation controls trigger timing and shows that acquisition contributes beyond timing alone, at the cost of approximately ten percentage points of positive-window recall under free-running triggers. A frozen threshold-only baseline pushes FP lower still but collapses BOTSv1 recall by 55 percentage points. Under the evaluated workload assumptions, pure FP minimization trades unacceptable recall for that lower burden.

---


### 190. [Robustness of breast lesion segmentation under MRI undersampling improves with k-space-aware deep learning](https://arxiv.org/abs/2605.22327)

**<font color=#1a73e8>作者：</font>** Lukas T. Rotkopf, Marco Schlimbach, Julius C. Holzschuh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purpose: To assess whether breast lesion segmentation can be learned directly from acquired MRI k-space, and whether doing so improves robustness when data are accelerated or noisy.
Materials and Methods: This retrospective study used public breast dynamic contrast-enhanced MRI (DCE-MRI) datasets with acquired and synthetic k-space, together with a within-dataset synthetic control. We compared four 3D U-Net variants: a hybrid k-space-to-image model, a native k-space model, and magnitude and complex image-space baselines. Models were evaluated under increasing undersampling and added complex Gaussian k-space noise. The primary outcome was patient-level Dice similarity coefficient under cross-validation, with the hybrid model prespecified as the main comparison against the magnitude image-space baseline.
Results: At full sampling, the hybrid and image-space models performed similarly. As acceleration increased, the hybrid model retained substantially more segmentation accuracy and significantly outperformed the magnitude image-space baseline across moderate to high undersampling levels. The same pattern was observed when noise was added directly to k-space: the hybrid model degraded more slowly, whereas the image-space baseline failed under heavier noise. This advantage was reproduced in the within-dataset synthetic control. Feature analysis suggested that the k-space stage and image-space stage played complementary roles, with frequency-domain filtering concentrated before image-domain lesion localization.
Conclusion: K-space-aware deep learning improves the robustness of breast lesion segmentation under MRI undersampling and k-space noise, while matching image-space methods at full sampling.

---


### 191. [3D LULC classification using multispectral LiDAR and deep learning: current and prospective schemes](https://arxiv.org/abs/2605.22328)

**<font color=#1a73e8>作者：</font>** Narges Takhtkeshha, Aldino Rizaldy, Markus Hollaus 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Land Use Land Cover (LULC) classification is essential for national 3D mapping, geospatial analysis, and sustainable planning. Multispectral (MS) LiDAR provides synchronized spatial-spectral information, and deep learning (DL) enables 3D point cloud semantic segmentation; however, adoption is limited by the lack of publicly available urban and suburban MS LiDAR datasets aligned with National Mapping and Cadastral Agencies (NMCAs) classification schemes. This study addresses these gaps by introducing L1 and L2 NMCA-aligned LULC classification schemes and a new benchmark MS LiDAR dataset. We evaluate seven state-of-the-art DL models and perform spectral ablation studies at both levels of detail. Results show that Point Transformer V3 achieves the best performance, with mIoU of 79.4% (L1, 8 classes) and 58.9% (L2, 20 classes) using a dual-wavelength LiDAR system (532 nm and 1064 nm). Ablation results show that multispectral information improves performance over geometry-only inputs, with gains of 1.1 percentage points at L1 and 7.8 points at L2. These results highlight the value of LiDAR reflectance for fine-grained material discrimination and support the evolution of NMCA LULC schemes toward higher semantic detail. The Loosdorf-MSL dataset contributes a new benchmark for consistent national and international LULC mapping.

---


### 192. [SepsisAI Orchestrator: A Containerized and Scalable Platform for Deploying AI Models and Real-Time Monitoring in Early Sepsis Detection](https://arxiv.org/abs/2605.22331)

**<font color=#1a73e8>作者：</font>** Santiago Ospitia, John Sanabria, John Garcia-Henao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite strong predictive results in the clinical machine learning literature, the translation of these models into bedside use remains limited by systems-level barriers: heterogeneous data representations, the absence of standardized deployment workflows, and a mismatch between research prototypes and the concurrency and latency requirements of hospital environments. We present the SepsisAI-Orchestrator, an open-source modular platform that addresses this deployment gap for early sepsis detection. The platform integrates HL7 FHIR-inspired Clinical Document Architecture (CDA) preprocessing, NoSQL storage, a containerized LightGBM classifier served via REST APIs, and a Streamlit clinical dashboard, orchestrated with Docker and Kubernetes. A previously validated LightGBM model (F1 0.87-0.94 on PhysioNet 2019) is reused without modification; the contribution lies in the surrounding infrastructure and its empirical characterization under load. Using k6 with 50-1000 concurrent virtual users, we find that replica count must be matched to the physical CPU thread count of the host: scaling from 3 to 12 replicas on a 12-thread CPU reduces p95 latency from 3.3s to 1.41s (57.3% reduction) and eliminates all request failures, while over-provisioning to 24 or 48 replicas degrades performance due to scheduler contention. To our knowledge this U-shaped scaling behavior has not been quantified previously for clinical AI inference workloads. We do not claim prospective clinical validation. Source code and deployment manifests are available at this https URL.

---


### 193. [Building Europe's Quantum Shield: The Strategic view for a Continent-Wide Quantum Key Ditribution (QKD) Infrastructure](https://arxiv.org/abs/2605.22332)

**<font color=#1a73e8>作者：</font>** Leandros Maglaras, Ilias Papastamatiou, Alexios Aivaliotis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The fast growth of quantum computing can lead to amazing scientific breakthroughs while on the same time can be used to break today's security systems, raising new risks for existing digital systems. Facing this challenge, the European's Union's deployement of the European Communication Infrastructure (EuroQCI) is crucial. The SEEWQCI project combines fiber cables, satellite communications and enhanced security rules to build a strong digital shield. Its focus is to protect vital services like power grids and hospitals keeping Europeans' data safe.

---


### 194. [A First Measurement Study on Authentication Security in Real-World Remote MCP Servers](https://arxiv.org/abs/2605.22333)

**<font color=#1a73e8>作者：</font>** Huijun Zhou, Xiaohan Zhang, Haozhe Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Model Context Protocol (MCP) is emerging as a common interface connecting large language models (LLMs) with external services. Remote deployments are becoming increasingly important as agents connect to user-linked online services, such as social, productivity, and financial services. In such deployments, the authentication boundary between MCP clients and remote servers becomes security-critical, yet remains underexplored.
We present the first measurement study of authentication security in real-world remote MCP servers. We identify 7,973 live remote MCP servers, finding that 40.55% expose tools without authentication. Among authenticated servers, OAuth is the dominant authorization mechanism for reaching remote services, and OAuth deployments in the MCP ecosystem commonly exhibit three characteristics: open client environments, dynamic client registration, and delegated authorization. These characteristics distinguish MCP deployments from traditional OAuth and introduce new attack surfaces. Guided by this observation, we derive a taxonomy of authentication flaws comprising three MCP-specific categories and conventional OAuth misconfigurations, for a total of four categories and nine concrete flaw types. To evaluate these flaws at scale, we implement a semi-automated detection framework that combines passive traffic inspection with active dynamic probing. Applying it to 119 testable real-world OAuth-enabled MCP servers, we find that each server exhibits at least one flaw, with a total of 325 flaws identified, among which dynamic client registration flaws affect 96.6% of tested servers. Many of these flaws can lead to sensitive information leakage and account takeover. Through responsible disclosure, we obtained 9 CVE IDs. Our findings expose pervasive authentication weaknesses in the MCP ecosystem and underscore the urgent need for hardened OAuth-based remote deployments.

---


### 195. [Riemannian geometry meets fMRI: the advantages of modeling correlation manifolds and eigenvector subspaces](https://arxiv.org/abs/2605.22334)

**<font color=#1a73e8>作者：</font>** Mario Severino, Manuela Moretto, Robert A. McCutcheon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Correlation matrices are fundamental summaries of functional brain networks, yet standard analyses often treat entries independently, ignoring the curved geometry of correlation space. Existing geometric methods frequently lack closed-form operations or depend on arbitrary region ordering, limiting scalability. We introduce a scalable geometric framework with two components: (i) the Off-log metric, a smooth transformation mapping correlation matrices to symmetric zero-diagonal matrices. This enables closed-form expressions for distances, Frechet means, and linear models, allowing standard statistical modeling without complex manifold optimization. (ii) Grassmannian subspace discrimination, which compares subjects via principal-angle distances between eigenvector subspaces, resolving inherent sign and basis ambiguities. Both components integrate into standard machine-learning workflows for inference, regression, and classification. Validated across two clinical cohorts (Parkinson's and psychosis) and three ageing fMRI datasets, the Off-log metric increased sensitivity in permutation tests and matched or exceeded Riemannian and Euclidean baselines in classification. Brain-age prediction performance was comparable, with Riemannian metrics excelling in two of three cohorts. The Grassmannian method consistently outperformed Euclidean baselines, highlighting disease-relevant networks. Overall, geometry-aware representations improve sensitivity and predictive performance while remaining straightforward to deploy at scale.

---


### 196. [Learning Causal Orderings for In-Context Tabular Prediction](https://arxiv.org/abs/2605.22335)

**<font color=#1a73e8>作者：</font>** Sascha Xu, Sarah Mameche, Jilles Vreeken  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In-context learning for tabular data sets strong predictive standards in observational settings; it however primarily relies on correlational structure, which becomes unreliable under distribution shift or intervention. While established methods to discover causal structure exist, they are often focused on structure identifiability and decoupled from the predictive architectures that could benefit from them.
To bridge these perspectives, we study how to simultaneously infer and enforce causal structure in the form of topological variable orderings into tabular prediction. Unlike standard architectures, our model TabOrder uses causal order-constrained attention, basing predictions only on features that precede a target under a learned causal order. Similar to causal discovery methods, TabOrder learns the optimal variable ordering in an unsupervised manner through a likelihood-based objective. We justify this choice under standard functional model classes and also study how sample missingness, a common challenge in tabular data, interacts with causal direction identification. Empirically, we confirm that TabOrder recovers accurate variable orderings while addressing prediction and imputation tasks, as well as gives insight into real-world biological data under intervention.

---


### 197. [Physics-Informed Generative Solver: Bridging Data-Driven Priors and Conservation Laws for Stable Spatiotemporal Field Reconstruction](https://arxiv.org/abs/2605.22338)

**<font color=#1a73e8>作者：</font>** Ziyuan Zhu, Keyu Hu, Zhifei Chen 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reconstructing continuous physical fields from sparse measurements is a central inverse problem, but data-driven generative models can produce states that violate governing dynamics. We introduce a physics-informed generative solver that separates stable prior learning from inference-time enforcement of conservation laws. Martingale-Regularized Score Matching regularizes score pretraining with a Score Fokker-Planck constraint, yielding a dynamically stable prior. Physics-Informed Implicit Score Sampling then guides denoising trajectories by gradients of physical residuals, projecting samples toward admissible manifolds without retraining. In acoustics, the method co-generates pressure and particle velocity from sparse sensors, enabling dense virtual arrays that suppress spatial aliasing. The same framework generalizes to real-world ERA5 meteorological fields under extreme sparsity. Together, this work establishes a rigorous and generalizable paradigm for solving high-dimensional inverse problems, bridging the gap between generative artificial intelligence and first-principles science.

---


### 198. [From Snapshots to Trajectories: Learning Single-Cell Gene Expression Dynamics via Conditional Flow Matching](https://arxiv.org/abs/2605.22340)

**<font color=#1a73e8>作者：</font>** Siyu Pu, Qingqing Long, Xiaohan Huang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Single-cell RNA sequencing (scRNA-seq) provides high-dimensional profiles of cellular states, enabling data-driven modeling of cellular dynamics over time. In practice, time-resolved scRNA-seq is collected at only a few discrete time points as unpaired snapshot populations, leaving substantial temporal gaps. This motivates trajectory inference at unmeasured time points. Existing methods mainly follow two directions, optimal-transport (OT) alignment provides distribution-level matching between observed snapshots, while continuous-time generative models support forecasting via learned dynamics. However, two challenges remain: (i) unpaired snapshots render local transitions between adjacent time points ambiguous, leading to unstable supervision; and (ii) long-horizon prediction relies on repeated integration, where small modeling errors compound and cause distribution drift. To address these challenges, we propose single-cell Flow Matching (scFM), a latent generative framework based on coupling-conditioned flow matching. First, we compute entropically regularized OT couplings between adjacent snapshots and use them to construct soft, weighted flow-matching targets for learning time-dependent velocity fields. Second, we learn bidirectional velocity fields and leverage their consistency to refine couplings and improve temporal coherence under sparse supervision. Third, we introduce distribution-level alignment and latent dynamic regularization to anchor long rollouts and mitigate drift. Experiments on real-world time-series scRNA-seq datasets show that scFM consistently improves distributional prediction performance for both temporal interpolation and extrapolation. Moreover, scFM yields more accurate trajectory reconstruction and temporally coherent visualizations where intermediate time points are absent, indicating a more faithful recovery of underlying temporal gene expression dynamics.

---


### 199. [A Boundary-Layer Mechanism for One-Third Scaling in Online Softmax Classification](https://arxiv.org/abs/2605.22341)

**<font color=#1a73e8>作者：</font>** Marcel Kühn, Yoon Thelge, Bernd Rosenow  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hard-label classification is usually trained with smooth surrogate losses, most prominently softmax cross-entropy. We isolate an asymptotic mechanism by which this mismatch between smooth surrogate and discrete labels produces power-law learning curves in an online teacher-student model. After subtracting the mean logit, the thermodynamic-limit dynamics close in centered variables: a growing centered student-teacher alignment $D$ and the residual student variance $\Delta$. At late times, examples away from teacher decision boundaries are already classified confidently and contribute exponentially little. Only boundary layers of width $O(D^{-1})$ remain active, while the noise of fixed-learning-rate online gradient descent maintains a nonzero $\Delta$. As a function of the training time $\alpha$ the late-time solution yields a $\alpha^{-1/3}$ power law not only for the test loss but also for the generalization error $\epsilon_g$, i.e., one minus test accuracy. This is much slower than the $\alpha^{-1}$ Bayes-optimal reference for the same model. We further show that learning-rate schedules can improve the generalization error towards a $\epsilon_g \sim \alpha^{-1/2}$ power law. Simulations support the predicted order parameter dynamics and learning curves. Controlled experiments with correlated Gaussian inputs and whitened pretrained features show that data structure can dominate transients. Therefore, our result is an asymptotic, complementary mechanism rather than an alternative to spectral explanations of neural scaling laws.

---


### 200. [4D-GSW: Kinematic-Aware Spatio-Temporal Consistent Watermarking for 4D Gaussian Splatting](https://arxiv.org/abs/2605.22342)

**<font color=#1a73e8>作者：</font>** Sifan Zhou, Hang Zhang, Yuhang Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While 4D Gaussian Splatting (4DGS) has revolutionized high-fidelity dynamic reconstruction, safeguarding the intellectual property of these assets remains an open challenge. Conventional steganographic techniques often neglect the underlying kinematic manifolds, triggering non-physical artifacts such as severe temporal flickering and "FVD collapse". To address this, we propose \textbf{4D-GSW}, a kinematic-aware watermarking framework designed to embed robust copyright information while preserving high spatio-temporal consistency. Unlike prior 4D steganography that primarily focuses on opacity-guided invisibility, our approach explicitly addresses the physical coherence of motion trajectories. We introduce a \textbf{Spatio-Temporal Curvature (STC)} metric to identify "Dynamic Instants," adaptively gating watermark gradient injection to shield critical motion manifolds from non-physical perturbations. To ensure global coherence across complex deformations, we formulate a joint \textbf{HMM-MRF energy minimization} model that synchronizes watermark phases within both temporal trajectories and spatial neighborhoods. Furthermore, an \textbf{anisotropic gradient routing} mechanism ensures that watermark embedding remains strictly decoupled from photometric reconstruction fidelity. Extensive experiments have demonstrated the superior performance of our method in robustly hiding watermarks while resisting various attacks and maintaining high rendering quality and spatiotemporal consistency.

---


> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-347](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
