# 📦 其他研究 | 2026年06月27日

> 本类共 **245** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-245**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-245**

---

### 201. [Transformer-Based Classification of Bacterial Raman Spectra with LOOCV](https://arxiv.org/abs/2606.27096)

**<font color=#1a73e8>作者：</font>** Jamile Mohammad Jafari, Thomas Bocklitz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer-based models have recently attracted increasing attention for Raman spectral classification. In this study, a transformer-based approach was systematically evaluated using a nested leave-one-replicate-out cross-validation framework and compared with conventional machine-learning pipelines combining PCA or ICA with LDA, SVM, and Random Forest classifiers. A bacterial Raman dataset comprising 5,417 single-cell spectra from six bacterial species and nine independent measurement replicates was used. The transformer consistently achieved the highest classification performance across independent test replicates and significantly outperformed all conventional approaches. Analysis of the learned latent feature space revealed improved class separation compared with PCA- and ICA-based representations. Furthermore, the transformer maintained superior performance when applied directly to raw Raman spectra without preprocessing, demonstrating robust behavior across measurement replicates. These findings highlight the potential of transformer-based models for robust Raman spectral classification and emphasize the importance of replicate-aware validation for realistic model evaluation.

---


### 202. [PRISM: PE Relational Inter-Section Matrix. A 2D Section-Aware Dataset for Static PE Malware Detection](https://arxiv.org/abs/2606.27109)

**<font color=#1a73e8>作者：</font>** José M. Sacristán, Ana I. González-Tablas  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We introduce PRISM (PE Relational Inter-Section Matrix), an open dataset and feature representation for static Windows PE malware detection. Existing benchmarks such as EMBER, BODMAS, and SOREL-20M represent each PE file as a flat one-dimensional feature vector, discarding the ordering of sections and the relational context between them. PRISM instead encodes every binary as a two-dimensional matrix whose rows are individual PE sections in file order, with a global summary row that preserves compatibility with EMBER-style models. We build the corpus from four malware sources (BODMAS, MalwareBazaar, VirusShare, and CAPE) together with SOREL-20M benign software, yielding 83,633 deduplicated matrices and a family-filtered analysis corpus of 49,204 samples across 684 malware families.
A formal separability analysis (Fisher Discriminant Ratio, mutual information, and inter-section information gain) shows that the per-section positional structure carries discriminative information that flat representations cannot capture. Under a strictly controlled, sample-matched comparison, a gradient-boosted classifier on the compact PRISM representation recovers nearly all of the binary-detection performance of the same classifier on the much larger EMBER vector, at roughly one-sixth the dimensionality; EMBER retains only a small, consistent advantage confined to the extreme low-false-positive regime, the two being operationally indistinguishable at the decision threshold. We are explicit that this binary task is saturated, so the structural content PRISM preserves is reserved for tasks with greater metric headroom, such as family classification and architectures that exploit the 2D structure directly. The dataset, extraction library, trained models, and full analysis pipeline are released under CC BY-NC-SA and MIT licences.

---


### 203. [Behind the Mask: A Taxonomic Analysis of Activities in Online Social Networks](https://arxiv.org/abs/2606.27111)

**<font color=#1a73e8>作者：</font>** Debora F De Souza, Gabriela Beltrao, Berta Chulvi 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The broadcast of disinformation in online social networks (OSN) is a growing concern examined across several disciplines, including human-computer interaction (HCI). The pervasive issue has been prompting novel approaches to identify the malicious actors behind the dissemination of deceptive and fabricated content. Analyzing the characteristics and activities of these actors, we designed a taxonomy informed by collaboration with subject matter experts (SMEs) and a review of the academic literature. Our study explores how to distinguish the characteristics, activities, and strategies of malicious actors on OSN and examines how they contribute to the spread of disinformation. We describe the design process and the application of the taxonomy in a case study analyzing anti-migration discourse in social media channels, and reflect on its potential to aid researchers and practitioners in the responsible design of network systems.

---


### 204. [Heavy-Ball Q-Learning with Residual Weighting Correction](https://arxiv.org/abs/2606.27112)

**<font color=#1a73e8>作者：</font>** Donghwan Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes a corrected heavy-ball Q-learning method for reinforcement learning (RL) and establishes its convergence. It also identifies conditions under which the method is theoretically guaranteed to converge faster than standard Q-learning. The same construction is then extended to Q-learning with linear function approximation, where analogous convergence and acceleration statements are derived. The analysis is based on a switched linear system (SLS) representation of Q-learning algorithms and on the joint spectral radius (JSR) of the associated switching families. This SLS viewpoint is not commonly used in standard analyses of Q-learning, and it provides a complementary framework and new insight into how heavy-ball momentum can accelerate Q-learning.

---


### 205. [Cross-Head Attention Uplift Network with Inverse Propensity Score under Unobserved Confounding](https://arxiv.org/abs/2606.27114)

**<font color=#1a73e8>作者：</font>** Haoran Zhang, Chuanpu Li, Yuxin Fu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uplift modeling, crucial for estimating individual treatment effects (ITE), faces dual challenges: flexibly leveraging inter-group similarity to enhance discriminative power and debiasing under unobserved confounding scenarios. In this paper, we propose the Cross-Head Attention Uplift Network (CHAUN) and Robust Adversarial Inverse Propensity Score (RA-IPS) method to address these limitations. CHAUN employs shared feature embeddings and cross-head attention mechanisms to dynamically integrate treatment-specific and control-specific representations, enhancing inter-group correlation modeling. Theoretically, we prove that access to the true propensity scores ensures ITE identifiability even with unobserved confounders. For practical scenarios lacking true propensity scores, RA-IPS adversarially optimizes propensity weights within constrained uncertainty sets to mitigate bias from unobserved variables. Experiments on public datasets (CRITEO-UPLIFT, LAZADA) and a production e-commerce dataset demonstrate CHAUN's superiority over state-of-the-art uplift models, achieving relative improvements of up to 25.6% in QINI scores. RA-IPS further enhances robustness, outperforming standard IPS by 5.4% under unobserved confounding. The results validate the effectiveness of our proposed methods in real-world causal inference tasks.

---


### 206. [Kolmogorov Arnold networks (KAN) for aerodynamic prediction: a comparison with MLPs and GNNs](https://arxiv.org/abs/2606.27126)

**<font color=#1a73e8>作者：</font>** Miguel Jaraiz, Fermin Gutierrez, Pablo Yeste 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kolmogorov Arnold networks (KAN) have recently been introduced as a (deep) neural network architecture whose trainable parameters adapt the activation functions, instead of the coefficients of the affine transformations at the core of traditional architectures such as deep multilayer perceptrons (MLPs). This architecture builds on the Kolmogorov-Arnold theorem, which endows it with universal approximation properties. While the advent of KANs has been received with excitement, there is a current debate about the possible KAN supremacy over deep multilayer perceptrons (MLPs) for classic fields such as symbolic regression, generic-purpose machine learning, natural language processing or computer vision. Here we assess the performance of KANs --and its nuanced comparison against MLPs and graph neural networks (GNNs)-- in the realm of fluid dynamics surrogate modelling. To that aim, we consider the task of predicting the surface pressure distribution over subsonic and transonic airfoils, a canonical task in aerodynamics. Our results show that KAN models show good performance in predicting the whole pressure coefficients and is able to interpolate across Mach numbers and angles of attack, however its performance is comparable --marginally inferior-- to a suitably trained MLP, where best performance is achieved by a GNN at the expense or requiring lengthier training. While the optimal KAN model have typically much lower complexity than MLP and GNN --hence resulting in faster training--, we find that KANs suffer from training instabilities, and their performance is highly dependent on a proper hyperparameter optimisation.

---


### 207. [FlameVQA: A Physically-Grounded UAV Wildfire VQA Benchmark with Radiometric Thermal Supervision](https://arxiv.org/abs/2606.27128)

**<font color=#1a73e8>作者：</font>** Mobin Habibpour, John Spodnik, Niloufar Alipour Talemi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wildfire monitoring from UAVs requires reliable reasoning over complex aerial scenes, where smoke, scale variation, and occlusions often limit RGB-only interpretation. We introduce FlameVQA, a multiple-choice visual question answering benchmark for UAV-based wildfire intelligence built on FLAME 3, leveraging paired RGB imagery and radiometric thermal TIFFs for temperature-grounded, safety-critical reasoning. FlameVQA includes 34 multiple-choice questions per image spanning six operational capability groups, covering tasks such as detection, localization, distribution/coverage estimation, cross-modal reasoning, and flight planning. To ensure label reliability, we combine MLLM-assisted annotation with deterministic thermal rules and cross-question consistency checks, followed by human auditing. We also evaluate representative MLLMs on FlameVQA to provide baselines for future work. Results show strong performance when explicit cross-modal cues are available, but notable failures on presence detection under heavy smoke and on coverage estimation. These findings suggest that current MLLMs require domain-specific adaptation to better support disaster and wildfire monitoring. The dataset and benchmark code are open-source at this http URL

---


### 208. [The Observer World: A Cryptographic Extension of Impagliazzo's Five Worlds](https://arxiv.org/abs/2606.27139)

**<font color=#1a73e8>作者：</font>** Fabio F.G. Buono  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Impagliazzo's five worlds classify computational assumptions along a single axis, the existence of cryptographic primitives. All five worlds implicitly assume that every party, including the adversary, observes the full input, that the observer is always $O_{top}$. This assumption is so natural that it is never stated. This work makes it explicit and relaxes it by introducing a second, orthogonal axis, the observational axis, defined by the observer hierarchy introduced in previous work. Relaxing the assumption reveals structural phenomena, such as the collapse $P^{O_{prof}} = NP^{O_{prof}} \subset P$, that the five-world framework cannot express. We prove that this collapse holds unconditionally in all five worlds, showing that observational blindness and computational hardness are independent. We define the Observer World $W_O$, classify all world-observer pairs, identify the labeled cells (a)--(d), and introduce a parametric family $W_O^{\varepsilon}$ modelling partial violations of observational invariants. The framework also interfaces with physical information limits, including thermodynamic, quantum, and cosmological bounds.

---


### 209. [fTNN: a tensor neural network for fractional PDEs](https://arxiv.org/abs/2606.27140)

**<font color=#1a73e8>作者：</font>** Qingkui Ma, Hehu Xie, Xiaobo Yin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop the fTNN, a deterministic tensor neural network subspace method for problems involving the fractional Laplacian on bounded domains, taking the fractional Poisson equation and time-dependent fractional advection-diffusion equation as typical representatives. The work employs a geometry-adapted integration split featuring a spatially dependent near-field radius, which decomposes the fractional Laplacian into three contributions: a singular near field, a regular interior far field, and an analytical exterior far field. Then the singular radial integrals are treated by Gauss-Jacobi quadrature, the regular radial integrals by Gauss quadrature, and the angular variables by deterministic angular quadrature, yielding a fully deterministic integration framework of the fractional Laplacian operator. To accurately resolve low-regularity solutions and the associated loss functional, we construct boundary-singularity-aware trial functions enriched with explicit boundary features, and propose two strategies for automatically selecting the leading exponent and evaluating the loss function from the singularity structure induced by the fractional operator, or jointly by the fractional operator and the source term. For time-dependent fractional PDEs, we design a spatiotemporally separable neural network that factorizes the time-space residual into a sum of low-dimensional temporal and spatial integrals, and we integrate this representation with an alternating neural network subspace optimization strategy for efficient training. Numerical experiments show that the proposed framework attains high accuracy on the tested benchmarks and improves substantially over existing fPINN and Monte Carlo baselines, particularly for problems with strong boundary singularities and long-time simulations.

---


### 210. [Safe Autoregressive Image Generation with Iterative Self-Improving Codebooks](https://arxiv.org/abs/2606.27147)

**<font color=#1a73e8>作者：</font>** Yunqi Xue, Zhijiang Li, Philip Torr 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unlike diffusion-based models that operate in continuous latent spaces, autoregressive unified multimodal models produce images by sequentially predicting discretized visual tokens. These tokens are derived from a codebook that maps embeddings to quantized visual patterns. The language-like architecture enables unified multimodal models to effectively capture text conditional information for generation, making them promising for text-to-image tasks. This also raises an interesting question: how safe are the images generated in such an autoregressive way? In this work, we propose iterative self-improving codebooks for safe autoregressive generation. We leverage the understanding and judgment capabilities of the unified multimodal model itself to identify unsafe generated images without human annotation. Subsequently, the inherent representations in the codebook are fixed to eliminate harmful mappings. Our method comprises two steps: first, we use the unified model to identify unsafe generations and construct corresponding harmful and safe image-text pairs. These pairs are used to construct the Harmful Space and guide updates to the codebook, thereby eliminating harmful outputs. Second, we perform adaptive fine-tuning on the codebook within the harmless space using safe image-text pairs to ensure the quality of generated images. These two steps are repeated until no further improvement is observed, producing a safety-enhanced model codebook. Without additional external feedback, the safety of models is improved iteratively.

---


### 211. [Stochastic Gradient Optimization with Model-Assisted Sampling](https://arxiv.org/abs/2606.27171)

**<font color=#1a73e8>作者：</font>** Jonne Pohjankukka, Jukka Heikkonen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work addresses the problem of variance in stochastic gradient estimation for machine learning optimization. Deep learning relies on mini-batch methods such as stochastic gradient descent, which approximate full gradients but introduce noise, creating trade-offs between convergence stability, speed, and generalization. Existing methods, including variance reduction techniques (e.g., SVRG and SAG) and adaptive optimizers, aim to mitigate gradient noise but may introduce additional computational overhead. We propose a model-assisted sampling framework that interprets mini-batch gradients through survey sampling theory, treating the dataset as a fixed finite population and gradients as sample-based estimates. Our aim is to bridge machine learning optimization and survey sampling theory by combining their perspectives on sample-based estimation and variance reduction. By incorporating auxiliary gradient-prediction models, we construct more efficient gradient estimators, with uniform sampling arising as a special case when no auxiliary information is used. Our approach integrates easily with existing optimizers, improving efficiency without altering their dynamics. Empirical results on synthetic and six benchmark datasets show performance gains in 71-86% of the experiments, particularly for medium-sized input spaces in our benchmarks. Notably, with momentum-based optimizers such as AdamW, the proposed estimator achieves clearly better generalization in roughly half the training epochs compared to baseline estimator.

---


### 212. [RecallRisk-BERT: A Multi-Task Framework for Post-Report Medical Device Recall Triage](https://arxiv.org/abs/2606.27174)

**<font color=#1a73e8>作者：</font>** Ali Semih Atalay, Sevgi Yigit-Sert  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Medical device recalls are a critical regulatory mechanism for protecting patient safety. The growing volume of FDA recall records presents challenges in post-report recall triage, severity assessment, and root-cause interpretation. Existing studies mostly address recall occurrence prediction or root-cause analysis separately, while joint modeling of recall severity and root-cause categories has received limited attention. We develop an automated recall triage framework using 54,165 FDA medical device recall records from openFDA, covering the period from 2002 to October 2025. We first evaluate classical machine learning and boosting-based models for recall severity and root-cause category prediction. We then develop RecallRisk-BERT, a multi-task model that combines PubMedBERT-based textual representations of recall narratives with embedding-based representations of structured categorical features, including product code, regulation number, and medical specialty. The model simultaneously predicts recall severity (Class I/II/III) and a consolidated root-cause category (9 classes). Performance was evaluated using accuracy, macro-averaged precision, recall, F1-score, and ROC-AUC. In single-task severity prediction, our LightGBM-based text--tabular configuration achieved the strongest performance, with an accuracy of 0.963, macro-F1 of 0.856, and ROC-AUC of 0.974. In the multi-task setting, RecallRisk-BERT substantially outperformed the single-task PubMedBERT baseline. Model-derived risk rankings were strongly consistent with observed root-cause severity patterns (rho = 0.983, p = 1.936e-6). These findings indicate that text--tabular learning can support scalable post-report recall triage, regulatory decision support, and model-based root-cause risk analysis.

---


### 213. [Explaining Temporal Graph Neural Networks via Feature-induced Information Flow](https://arxiv.org/abs/2606.27201)

**<font color=#1a73e8>作者：</font>** Ping Xiong, Thomas Schnake, Klaus-Robert Müller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Event-based Temporal Graph Neural Networks (ETGNNs) have demonstrated strong performance across a wide range of applications, including social network analysis, epidemic tracing, recommender systems, and political event forecasting. However, their increasing complexity poses significant challenges for explainability. Existing explanation methods focus only on a subset of the information flow within ETGNNs, typically tracing contributions from the event-related embeddings to the output. Consequently, they overlook the important pathways through event-induced variables, which mediate interactions between nodes and thereby play a central role in capturing long-range temporal dependencies. To overcome this limitation, we propose a novel attribution method that analyzes the \emph{entire} information flow through all event-associated variables. Our method is built upon the recent Normalized Relevance Measure (NRM) framework, which enables explicit quantification of information flow originating from event embeddings as well as information flow passing through event-induced variables. It also ensures comparability of latent variables across layers, and supports higher-order analysis of interactions between events. To handle the architectural complexity of ETGNNs, we extend the NRM framework with a modular decomposition procedure that facilitates the systematic construction of relevance structure for complex neural architectures. We evaluate our approach on two synthetic datasets for epidemic tracing and social dynamics, as well as a real-world dataset of political event networks. Our qualitative and quantitative experiments show that our method consistently outperforms existing explanation approaches while producing more human-interpretable explanations.

---


### 214. [Graph Neural Networks Applications Across Domains: All Insights You Need](https://arxiv.org/abs/2606.27202)

**<font color=#1a73e8>作者：</font>** Abderaouf Bahi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks have moved from a niche representation-learning technique to the default model class wherever data carry relational structure. The interesting question is no longer whether message passing helps on a given dataset, but where graph structure earns its computational cost and where it does not. This survey organises the field around a single design space, derives the spectral and spatial formulations from shared first principles, and connects expressive power to the Weisfeiler-Leman hierarchy with explicit statements of what current architectures can and cannot separate. Against that methodological backbone we examine twelve application domains, among them recommendation and social networks, knowledge graphs and language-model integration, drug discovery and molecular property learning, healthcare and neuroscience, computer vision, traffic and urban computing, power and renewable-energy systems, wireless and sixth-generation networks, fraud and cybersecurity, industrial prognostics, materials science, and climate modelling. For each domain we specify the graph-construction choices and their costs, identify which architecture families dominate and why, and separate reported gains from artefacts of weak baselines or favourable splits. A cross-domain comparison exposes recurring patterns: heterophily and scale undercut the same models almost everywhere, temporal graphs remain harder than their static counterparts, and the architectures that top public leaderboards are seldom the ones that reach deployment. We treat over-smoothing, over-squashing, robustness, distribution shift, fairness, and explainability not as a closing checklist but as the constraints that decide adoption.

---


### 215. [Syntactic Belief Update as the Driver of Garden Path Processing Difficulty](https://arxiv.org/abs/2606.27206)

**<font color=#1a73e8>作者：</font>** Alan Zhou, Miloš Stanojević, John T. Hale  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Garden path sentences present a processing difficulty for humans -- the sentence prefix leads the listener towards one interpretation, until the listener hears a critical word that shows that the initial interpretation was wrong. Lexical surprisal, a measure that usually predicts sentence processing difficulty quite well, fails to provide good predictions for garden path sentences.
We propose an alternative that actively predicts a probability distribution over syntactic trees (its syntactic belief) and updates that distribution after each new word. If a processor is led down a garden path, syntactic beliefs will be wrong and will require a large update at the critical word. The magnitude of the update is measured with a generalized Rényi divergence. Crucially, this metric is dependent on lexical items, but is fully independent of the probability of lexical items. This Syntactic Belief Update provides a better fit to the human reading time data on garden path sentences. This suggests a new research direction examining purely non-lexical alternatives to surprisal for psycholinguistics.

---


### 216. [Vulnerability of Natural Language Classifiers to Evolutionary Generated Adversarial Text](https://arxiv.org/abs/2606.27215)

**<font color=#1a73e8>作者：</font>** Manjinder Singh, Alexander E. I. Brownlee, Mohamed Elawady  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep learning models have achieved impressive performance across various fields but remain vulnerable to adversarial inputs, particularly in NLP, where such attacks can have significant real-world consequences. Adversarial attacks often involve small, semantically similar token replacements to fool NLP models, and recent methods have become more precise by targeting specific vulnerable words, often by exploiting some level of access to the model's internal structure. This paper proposes GAversary, a hybrid Genetic Algorithm (GA) to generate adversarial attacks on natural language models. The GA is able to treat the target model as a black box, requiring only the logit value output by the model to guide the search. GAversary differs from GAs previously proposed for this problem by using GloVe embeddings to propose word replacements (the mutation operator) to improve the semantic similarity of the adversarial examples. GAversary is applied to several benchmark data sets and well-known target models. GAversary is able to substantially reduce the target model's accuracy on test data compared to the BAE and A2T attacks compared against (in the best case, reducing a 76.8% accuracy to 5.8%, compared to BAE's 27.6%). The trade-off is that GAversary perturbs just under twice as many words as the other two methods, with a slightly lower semantic similarity to the original text and around a 5% increase in run-time.

---


### 217. [SatSplatDiff: Geometry-preserving generative refinement for high-fidelity satellite Gaussian Splatting](https://arxiv.org/abs/2606.27223)

**<font color=#1a73e8>作者：</font>** Jiyong Kim, Shuang Song, Ronjgun Qin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaussian Splatting has been recently explored for satellite 3D reconstruction, demonstrating flexibility and efficiency in representing radiometrically diverse satellite scenes. However, the limited top viewpoint of satellite imagery results in insufficient supervision on building facades, leaving surface holes and degraded visual fidelity. Generative refinement, which leverages pretrained generative priors to iteratively refine and update the rendered images used as supervision targets, has recently been investigated to improve the visual fidelity of Gaussian-rendered images. However, since these models refine each view independently, the resulting images can generate hallucinations and break photo-consistency, leading to geometric degradation. To address these limitations, we propose SatSplatDiff, which aims to minimize geometric degradation prevalent in generative refinement. Building on photogrammetric DSM initialization and 2DGS-based shadow casting established in our prior work SatSplat, we first introduce monocular depth supervision and multi-scale geometric refinement to establish a geometrically accurate and well-regularized surface representation. We then apply shadow-guided generative refinement, where geometrically calculated shadow maps guide the Gaussians to maintain consistency with the underlying geometry, improving visual fidelity while reducing geometric degradation. Extensive evaluations on the IARPA2016 and DFC2019 datasets demonstrate state-of-the-art performance, reducing geometric MAE by up to 18% and improving visual fidelity (FID-CLIP) by 28-45% over existing baselines. Our method delivers up to 5x resolution enhancement with minimal hallucination and sensor-consistent appearance, demonstrating seamless cross-tile consistency and strong scalability for large-scale reconstruction. Source code is available at this https URL

---


### 218. [Compositionality and the lexicon in evolutionary semantics](https://arxiv.org/abs/2606.27228)

**<font color=#1a73e8>作者：</font>** Fausto Carcassi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Formal semantics has shown that sentence meanings arise by recursively composing lexical meanings, yet much of the literature on semantic universals models either lexicons with fixed signal structures or holistic composition without interpretable lexical parts. We introduce a framework that integrates this fundamental insight of formal semantics in evolutionary modeling, by allowing lexical meanings and a composition function to co-evolve under pressures for conceptual simplicity and communicative accuracy. We apply this framework to the evolution of quantificational meaning. Analyzing the Pareto frontier, we find that the most well-known semantic universal, conservativity, emerges as an efficient system-wide abstraction. The account is sensitive to syntactic structure and helps reconcile tensions between empirical evidence on quantifier learnability and prior evolutionary models. More broadly, the results demonstrate that the picture of sentential meaning developed in formal semantics can be productively combined with evolutionary modeling. The framework offers a template for studying universals that involve global compression within a grammatical category, semantic specialization of syntactic arguments, and the co-evolution of lexical and compositional meaning.

---


### 219. [CARVE: Content-Aware Recurrent with Value Efficiency for Chunk-Parallel Linear Attention](https://arxiv.org/abs/2606.27229)

**<font color=#1a73e8>作者：</font>** Sayak Dutta  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recurrent models must forget in order to remember, yet the state of the art decides what to erase without consulting what is stored -- the gate sees only the arriving token, not the memory it is about to modify. This memory-blind gating is one of three coupled defects in the leading delta-rule architecture (GDN-2): the value-axis erase mask wastes parameters at the scale of the value projection, and -- as we prove -- mathematically prevents the WY-form triangular chunk solver that makes recurrent training competitive with Transformers.
We introduce CARVE (Content-Aware Recurrent with Value Efficiency), which resolves all three problems through one principle: erase only on the key axis. This is provably necessary and sufficient for the WY-form solver to remain valid. Within it, CARVE reuses the recurrent output tensor -- already written to GPU memory -- as a free content signal for the erase gate, and replaces the per-value write-gate projection with a single scalar per head. At initialisation CARVE is bit-identical to GDN-2; any quality difference emerges from what the content gate learns.
At 1.3B parameters trained on 100B tokens, CARVE achieves WikiText perplexity 15.72 (minus 0.18 vs. GDN-2, a 4.5-sigma effect), leads every recurrent baseline on nine common-sense reasoning benchmarks, and sets state of the art on every RULER retrieval probe -- at 0.4% throughput overhead, 13% lower peak memory, and 19% fewer parameters. Six formal theorems cover memory capacity, Lyapunov stability, gradient flow, expressivity separation, Pareto-optimal chunk size, and hybrid optimality.

---


### 220. [Bridging Talk and Thought: Understanding Dialogue Dynamics Across Collaborative Problem-Solving Contexts](https://arxiv.org/abs/2606.27233)

**<font color=#1a73e8>作者：</font>** Zhengyuan Liu, Stella Xin Yin, Min-Yen Kan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a conceptual framework for analyzing dialogue in collaborative problem-solving contexts, with an emphasis on the emerging dynamics of human-AI and multi-agent collaboration. As intelligent systems become active agents capable of autonomous reasoning and strategic cooperation, understanding the dialogic interaction during collaborative problem solving is increasingly important for optimizing and evaluating such partnerships. Our framework addresses key limitations in current analytical approaches through a hierarchical two-layer coding scheme that integrates cognitive and non-cognitive problem solving with metacognitive regulatory mechanisms. We demonstrate its effectiveness and generalizability across nine datasets spanning multiple domains, and provide insights into how humans and agents coordinate their knowledge, skills, and efforts to solve complex problems, showing in particular that metacognitive regulation can be an essential discriminator of deeper collaboration.

---


### 221. [LMs as Task-Specific Knowledge Bases: An Interpretability Analysis](https://arxiv.org/abs/2606.27237)

**<font color=#1a73e8>作者：</font>** Amit Elhelo, Amir Globerson, Mor Geva  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models (LMs) capture large amounts of factual knowledge applicable to a wide range of tasks, motivating the view of their parameters as a knowledge base. An important property of knowledge bases is that different queries for the same fact return consistent results, drawing on a single source of truth. We investigate whether LMs satisfy this property through behavioral and mechanistic analyses. Our results suggest that they encode knowledge in a task-specific manner. Behaviorally, facts acquired on one task frequently fail to co-emerge on others during training. Parameter localization experiments suggest a mechanistic explanation, revealing distinct parameter subsets underlying different tasks for the same fact. Finally, we show that chain-of-thought reasoning draws part of its effectiveness from engaging task-specific parameters beyond those tied to the evaluation task. Our findings suggest that what the model knows and how it is asked are intertwined in parameter space, undermining the "knowledge base" analogy and carrying implications for the reliability and controllability of factual knowledge in LMs.

---


### 222. [Effective Covariance Dynamics in Solvable High-Dimensional GANs](https://arxiv.org/abs/2606.27246)

**<font color=#1a73e8>作者：</font>** Andrew Bond, Zafer Doğan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study a solvable high-dimensional model of generative adversarial network (GAN) training in which a linear generator learns a low-dimensional subspace from data with structured latent covariance. Prior solvable GAN analyses assume unconditional signals with diagonal latent covariance; we extend the multi-feature discriminator setting to class-dependent, correlated, and non-zero-mean latent structure. For the quadratic energy discriminator, all such heterogeneity enters the dynamics through a probability-weighted effective second moment. We prove that the stochastic microscopic training process converges, in the high-dimensional limit, to deterministic ordinary differential equations governed by this effective covariance. In the matched-covariance specialization, the stability analysis yields a mode-wise solvable interval determined by the learning rates and noise level: learning begins when the leading effective eigenvalue crosses the lower threshold, while full recovery requires all relevant effective modes to remain within the interval. This reveals a signal-boosting mechanism: low-rank correlations can lift weak directions above the learnability threshold, whereas overly strong correlations destabilize recovery. Numerical simulations validate the ODE, phase boundary, and boosting mechanism. Experiments on MNIST, FashionMNIST, and CIFAR-10 further show that informed generator covariance improves alignment with the data-driven reference subspace.

---


### 223. [Tilikum: Transaction Fair Ordering on a DAG without Weak Edges](https://arxiv.org/abs/2606.27250)

**<font color=#1a73e8>作者：</font>** Giulio Segalini, Yigit Çolakoğlu, Marko Putnik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Decentralized Finance (DeFi) applications rely heavily on the order in which transactions are executed, making them susceptible to reordering attacks that enable adversaries to extract Blockchain Extractable Value (BEV). While linear blockchain systems such as Ethereum have inspired extensive research into fair ordering mechanisms, DAG-based consensus protocols have remained largely unprotected despite their growing adoption for scalability and performance. In this paper, we introduce Tilikum, a DAG-based ledger protocol that ensures fair transaction ordering without relying on weak edges. Tilikum achieves ordering linearizability by leveraging median-based timestamp aggregation, or batch order fairness, while maintaining low data redundancy and robust garbage collection. We implemented Tilikum in Rust and evaluated it against representative baselines, namely Narwhal/Tusk, Pompē, Themis and FairDAG. Our results show that Tilikum achieves up to $39\times$ higher throughput than other fair-ordering baselines, while fully blocking state-of-the-art DAG-specific reordering attacks.

---


### 224. [BetXplain: An Explanation-Annotated Dataset for Detecting Manipulative Betting Advertisements on Social Media](https://arxiv.org/abs/2606.27274)

**<font color=#1a73e8>作者：</font>** MSVPJ Sathvik, Parmitha Vangapadu, Nishit Rane 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The promotion of betting applications on social media platforms has increased significantly in recent years. Many of these advertisements use persuasive techniques that may mislead users, encourage risky behavior, and potentially influence users' mental well-being. However, research on the automated detection of manipulative and deceptive betting advertisements remains limited due to the lack of publicly available annotated datasets. In this work, we introduce a new dataset of betting-related advertisements collected from two widely used social media platforms, Instagram and Reddit. The advertisements were manually annotated for manipulative and deceptive advertising practices. In addition to classification labels, the dataset includes human-provided explanations that describe the reasoning behind each annotation, enabling research into explainable approaches to detecting manipulative advertising. Furthermore, we analyze the strategies commonly used in betting advertisements and examine how these persuasive tactics may impact users' mental health. The proposed framework can also enable practical applications such as browser plugins that warn users about manipulative betting advertisements and automated web crawlers that help regulatory authorities monitor and detect such promotions online.

---


### 225. [Exact and Deterministic Patch Descriptor Retrieval via Hierarchical Normalization](https://arxiv.org/abs/2606.27280)

**<font color=#1a73e8>作者：</font>** Koichi Sato  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a patch descriptor retrieval method that returns the exact nearest neighbour -- provably identical to exhaustive full-vector search -- while evaluating only a small fraction of the database, and does so deterministically: the same (database, query) pair always produces the same result, independent of run order, thread count, or hardware. This contrasts with approximate nearest-neighbour (ANN) approaches such as HNSW and IVF-PQ, which trade exactness for speed and may return different results across runs. The enabling mechanism is Hierarchical Normalization (HN): a normalisation scheme that splits the pre-normalisation feature vector into a K-dim major component (norm sqrt(1-alpha)) and a (128-K)-dim minor component (norm sqrt(alpha)). Since the minor inner product is bounded by alpha (Cauchy-Schwarz on the prescribed norms), the major similarity plus alpha is an admissible upper bound on the full similarity: the search scans the K-dim major component for all entries, then applies full 128-dim evaluation only to entries that cannot be pruned -- a provably exact branch-and-bound scan. We train HN-modified HardNet on the notredame split of the UBC patch dataset and evaluate on trevi and halfdome. With a cache-optimised Structure-of-Arrays layout and K=8, alpha=1/32, the search achieves 13.7x (trevi) / 12.7x (halfdome) speed-up over brute-force 128-dim search, with only 0.4% of entries requiring full evaluation. At K=16, alpha=1/8, FPR@95 rises from 0.0062 to 0.0064 on trevi at 7.2x speed-up, with 98.8% of entries bypassing full evaluation.

---


### 226. [How Good Can Linear Models Be for Time-Series Forecasting?](https://arxiv.org/abs/2606.27282)

**<font color=#1a73e8>作者：</font>** Lang Huang, Jinglue Xu, Luke Darlow  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series forecasting research has been moving steadily toward larger architectures, from specialized transformers to general-purpose foundation models, on the assumption that capacity is what unlocks accuracy. We take the opposite position: most of the gap can be closed at far lower cost by tuning preprocessing rather than scaling models. We use Ridge regression as the testbed, since it has a closed-form solution and interpretable weights, which let the optimal hyperparameters be read off the search directly. We search over context length, local normalization, regularization, and augmentation on eight standard benchmarks and find three patterns. (1) Optimal lookback is strongly series-specific and often non-monotonic in forecast horizon, with fitted power-law exponents ranging from $+0.46$ on ETTm2 to $-0.19$ on Exchange and Traffic, challenging the convention that longer horizons need longer history. (2) Normalizing over a learned trailing fraction of the context, rather than its entirety, is almost universally preferred. (3) Series within the same dataset often disagree on hyperparameters; the optimal degree of cross-series sharing varies from fully shared to fully per-series. The resulting models beat prior linear forecasters on most dataset-horizon entries and exceed Transformer, MLP, and CNN baselines on six of eight benchmarks. The optimized hyperparameters also serve as a diagnostic on the data itself, revealing structures that larger models absorb silently into their learned parameters.

---


### 227. ["Everyone Says Them": Deception Typologies, Probabilistic Trust, and Grassroots Safety Knowledge Among Gay Dating App Users in China](https://arxiv.org/abs/2606.27284)

**<font color=#1a73e8>作者：</font>** Yibo Meng, Lyumanshan Ye, Yingfangzhong Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Gay dating applications have become critical platforms for sexual minority men to seek relationships and community, yet they also expose users to deceptive interactions that remain underexplored in HCI and CSCW research. This study examines how gay male users in China experience, identify, and respond to deception on dating applications. Through semi-structured interviews with 22 participants across platforms including Blued, Aloha, Fanka, and Soul, we make three contributions. First, we identify a typology of deceptive practices extending beyond profile misrepresentation to encompass relational, emotional, financial, and commercial forms of deception. Second, we document the layered, probabilistic verification strategies users develop through long-term platform use, showing that trust assessment operates as a multi-signal, provisional process rather than a binary judgment. Third, we demonstrate that risk recognition is a collaborative practice shaped by the circulation of experience, the abstraction of recurrent tactics, and the codification of shared rules within the community.

---


### 228. [Recovering Governing Equations from Solution Data: Identifiability Bounds for Linear and Nonlinear ODEs](https://arxiv.org/abs/2606.27285)

**<font color=#1a73e8>作者：</font>** Yang Pan, Helmut Bölcskei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning governing equations from observed solution data is a fundamental challenge in scientific machine learning \cite{bruntonDiscoveringGoverningEquations2016,kovachkiNeuralOperatorLearning2023,longPDENetLearningPDEs2018,rudyDatadrivenDiscoveryPartial2017,raonicConvolutionalNeuralOperators2023}, yet the theoretical conditions under which a ground-truth ODE can be uniquely and stably identified from multiple solution observations remain largely undeveloped, and no quantitative analysis of the sample complexity of such learning tasks exists in the literature. To address this gap, we introduce the Hausdorff distance on solution sets as the natural metric for comparing differential equations, since it captures the worst-case separation between two equations over all admissible initial conditions and thus encodes the minimax structure of the identification problem. We establish identifiability bounds for governing ODEs across a wide class of structure equations--ranging from linear ODEs to nonlinear classes with Lipschitz (Hölder)-continuous vector fields--characterizing precisely when two distinct equations can be distinguished from solution data. Using this metric, we derive metric entropy estimates for the relevant ODE classes and analyze sample complexity bounds, quantifying how many solution observations are needed to reliably recover the governing equation.

---


### 229. [Simulation-based inference for rapid Bayesian parameter estimation in epidemiological models: a comparison with MCMC](https://arxiv.org/abs/2606.27286)

**<font color=#1a73e8>作者：</font>** Alina Bazarova, Johann Fredrik Jadebeck, Henrik Zunker 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mechanistic epidemiological models are widely used to support infectious disease forecasting and public-health decision making. Bayesian calibration of such models is commonly performed using Markov chain Monte Carlo (MCMC), which can become computationally expensive for high-dimensional nonlinear systems and repeated near-real-time analyses. Here, we investigate simulation-based inference (SBI) using neural posterior estimation as a scalable alternative for Bayesian calibration of a mechanistic SECIR epidemiological model using COVID-19 intensive care unit (ICU) occupancy data from Germany during 2020. We compared SBI and MCMC across multiple epidemic phases using both 31-day inference windows and a substantially more challenging 201-day reconstruction problem involving multiple transmission change points. Posterior agreement was evaluated quantitatively using Wasserstein distances and Kullback-Leibler divergences together with posterior predictive checks. Across the 31-day windows, SBI recovered posterior distributions in strong agreement with MCMC while accurately reproducing observed ICU trajectories. In the 201-day setting, SBI preserved the dominant posterior structure despite increased uncertainty. SBI, by combining CPU and GPU resources, substantially reduced computational runtime compared with MCMC, which was restricted to running on CPUs. Whereas MCMC required approximately 1000 seconds for the 31-day inference problems, SBI achieved comparable posterior and predictive performance in approximately 60-70 seconds on a single GPU. For the 201-day inference problem, SBI required an average of 157 seconds, while the MCMC runs took over 19,000 seconds. Our results demonstrate that SBI provides a rapid and computationally efficient framework for Bayesian calibration of mechanistic epidemiological models, supporting repeated near-real-time inference and rapid outbreak analysis.

---


### 230. [Designing Reward Signals for Portable Query Generation: A Case Study in Industrial Semantic Job Search](https://arxiv.org/abs/2606.27291)

**<font color=#1a73e8>作者：</font>** Ping Liu, Qianqi Shen, Jianqiang Shen 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Job-search platforms rely on low-bandwidth query interfaces that often fail to capture the high-dimensional complexity of candidate profiles. We present an end-to-end RLAIF (Reinforcement Learning from AI Feedback) framework to generate \emph{portable} job search queries, terms that abstract away seeker-specific identifiers while preserving generalizable qualifications. This task introduces a highly adversarial reward surface where policy optimization frequently exploits flaws in LLM-as-judge rubrics, resulting in degenerate verbatim-copying behaviors.
We conducted comprehensive empirical experiments to isolate the impact of optimization mechanics against structured reward engineering. Our results demonstrate that for critic-free optimizers, performance is overwhelmingly dictated by robust reward shaping, rendering the specific choice of algorithm largely immaterial. While critic-free per-rollout baseline methods (RLOO and REINFORCE++) natively resist reward-hacking, the group-relative advantage normalization in GRPO appears uniquely sensitive to spurious reward signals, making it disproportionately susceptible to exploitation. We show that introducing a deterministic, rule-based reward floor to correct for rewards assigned to verbatim copying mitigates this failure mode, resulting in a substantial $+0.147$ quality improvement on a cross-family evaluation judge. Ultimately, we show that the training-time reward model inflates performance gains by $2.4\times$, confirming that the training success is fundamentally dependent on enforcing reward-shaping disciplines rather than selecting alternative optimizers.

---


### 231. [Reading the Same Data Differently: Interpretive Labor Across System Boundaries in Electronic Monitoring](https://arxiv.org/abs/2606.27301)

**<font color=#1a73e8>作者：</font>** Yibo Meng, Bingyi Liu, Zhiqi Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Electronic monitoring (EM) systems are increasingly used in community corrections to enforce spatial, temporal, and behavioral rules through continuous sensing. While prior work has examined EM as a criminal justice tool or as a mechanism for compliance, less is known about how sensed data become meaningful in everyday practice. This poster examines EM as a dual-sided sensing system in which supervised individuals and authorities reason about the same data stream from different positions. Based on semi-structured interviews with 26 supervised individuals and 12 authorities in China's community corrections system, we show that supervised individuals infer system logic from outcomes with limited visibility into how data are interpreted, while authorities reconstruct behavior from ambiguous traces using contextual knowledge, professional experience, and institutional procedures. We call this structural divergence interpretive misalignment. It emerges from asymmetric access to data, context, and reasoning processes, and it shapes behavior through probing, strategic adaptation, over-compliance, disengagement, and contestation. We contribute a CSCW account of continuous sensing as distributed interpretive work and identify design opportunities for making data-to-decision processes more legible, contestable, and accountable across system sides.

---


### 232. [AI Healthcare Chatbots as Information Infrastructure: A Large-Scale Study of User-Reported Breakdowns](https://arxiv.org/abs/2606.27302)

**<font color=#1a73e8>作者：</font>** Muhammad Hassan, Ramazan Yener, Ece Gumusel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI healthcare chatbots are increasingly used to support health information seeking and self-management, yet their performance and impact on users remains to be studied. This study examines over 15,000 user reviews from 59 AI healthcare chatbot apps to explore how these systems function in everyday informational and emotional contexts. Topic modeling and interpretive analysis identify three recurring breakdowns: access barriers and service unreliability, user experience and interaction quality, and billing and customer support issues. Privacy and security concerns are associated with the most negative experiences. By framing AI healthcare chatbots as information infrastructures, our findings highlight how failures in access, usability, and trust affect users, offering actionable insights for designers, policymakers, and information professionals aiming to improve digital health systems.

---


### 233. [A Multi-Fidelity Convolutional Autoencoder-Transfer Learning Framework for Guided-Wave-Based Damage Diagnosis Using Large Simulated and Limited Experimental Datasets](https://arxiv.org/abs/2606.27304)

**<font color=#1a73e8>作者：</font>** Santosh Kapuria, Abhishek  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Guided wave-based structural health monitoring (GWSHM) with onboard transducers offers significant potential for the early diagnosis of damage in engineering structures. However, the practical deployment of deep learning models is often hindered by the limited availability of labelled experimental data and the high computational cost of generating large-scale high-fidelity simulation datasets. This study presents a multifidelity transfer learning framework that integrates lightweight physics-based simulations, convolutional autoencoder (CAE)-based deep feature learning, a feed-forward neural network, and limited experimental measurements for accurate damage localisation and sizing in plate-like structures instrumented with piezoelectric transducers. A computationally efficient one-dimensional time-domain spectral element model is employed to generate a large synthetic dataset for pretraining, while transfer learning adapts the model to experimental domains using only a small amount of labelled data. The CAE-based transfer learning framework significantly outperforms its CNN-based counterpart in damage localisation accuracy. The model achieves excellent predictive performance with $R^2$ scores exceeding 0.93 for damage localisation and 0.99 for damage sizing. Its generalisation capability is demonstrated on previously unseen data, showing high prediction accuracy for damage scenarios not represented during pretraining or fine-tuning. The results establish the proposed framework as an accurate, computationally efficient, and practically viable solution for real-world GWSHM applications.

---


### 234. [Multilingual Reasoning Cascades Need More Context](https://arxiv.org/abs/2606.27306)

**<font color=#1a73e8>作者：</font>** Arnav Mazumder, Dengjia Zhang, Shuyue Stella Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Translation cascades for reasoning translate the query from another language to English, reason in English, and translate the answer back to the original language. This is a competitive approach to multilingual reasoning, but structurally lossy, since each stage discards information later stages may need, including cues for cultural grounding, register, and disambiguation. We examine the benefits of a simple and training-free intervention: a context-aware translation cascade, which additionally provides the original question, the English translated question, and the reasoning trace to the context of the final translation module. We evaluate gains across nine multilingual benchmarks including various task types, three backbone models, and 285 high-, mid-, and low-resource languages, and demonstrate strong gains for open-ended generation across models and resource regimes. We show that the original language question carries most of the beneficial context. Our study emphasizes the need to better design information flow in machine translation cascades for mitigating error propagation, and provides a simple and actionable default strategy: preserve the original user question until the end of the pipeline.

---


### 235. [See & Sniff: Learning Visuo-Olfactory Representations](https://arxiv.org/abs/2606.27307)

**<font color=#1a73e8>作者：</font>** Seongyu Kim, Seungwoo Lee, Hyeonggon Ryu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While modern multimodal models integrate vision with language, audio, or touch, olfaction remains largely unexplored due to the lack of paired visuo-olfactory data. We introduce SmellNet-V, a scalable visuo-olfactory dataset built on the insight that odor identity is largely invariant to visual transformations within a semantic category. This allows us to synthetically pair smell-only samples with semantically aligned in-the-wild web images, converting a unimodal olfactory dataset into a cross-modal benchmark without costly co-collection. Building on this dataset, we propose See & Sniff, a self-supervised framework that learns joint visuo-olfactory representations via dense local alignment and naturally produces smell saliency maps for spatial grounding of odor sources. We further introduce pixel-level smell localization task and a benchmark for evaluation. Our method surpasses smell-only baselines by 7% in smell classification from smell alone and generalizes to cross-modal retrieval and smell localization, establishing visuo-olfactory learning as a new direction in multimodal perception.

---


### 236. [Blackwell Approachability and Gradient Equilibrium are Equivalent](https://arxiv.org/abs/2606.27315)

**<font color=#1a73e8>作者：</font>** Brian W. Lee, Nika Haghtalab, Michael I. Jordan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gradient equilibrium (GEQ) is a recently introduced online optimization framework that generalizes first-order stationarity from offline optimization and abstracts problems like online conformal prediction. While GEQ has curious similarities with known online learning frameworks, namely regret minimization, prior work has shown that GEQ error and regret are incomparable objectives, leaving open a precise understanding of how GEQ fits into the broader online learning landscape. In this work, we show that GEQ is equivalent to Blackwell approachability in the algorithmic sense. That is, a Blackwell approachability problem can always be solved using queries to a black-box GEQ oracle, with no asymptotic loss in the oracle's error rate, and vice versa. Taken together with known equivalences between approachability, regret minimization, and calibration, these results imply that GEQ is equivalent to these frameworks, as well. Our reductions are efficient and can be used to transfer refined guarantees, such as optimism and strong adaptivity, from regret minimization to GEQ. Along the way, we also identify necessary and sufficient conditions for GEQ, and establish reductions between different notions of GEQ with unconstrained and constrained decision sets.

---


### 237. [Beyond the Hard Budget: Sparsity Regularizers for More Interpretable Top-k Sparse Autoencoders](https://arxiv.org/abs/2606.27321)

**<font color=#1a73e8>作者：</font>** Nathanaël Jacquier, Maria Vakalopoulou, Mahdi S. Hosseini  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) have become a leading tool for interpreting the representations of vision foundation models, decomposing their polysemantic activations into a larger set of sparse, more monosemantic features. The Top-$k$ SAE, a now-standard variant, enforces sparsity architecturally through its activation function, retaining only the $k$ most active latents per input. Because it was designed precisely to avoid the $\ell_1$ penalty used by earlier SAEs and its known drawbacks, it has not been combined with an explicit sparsity regularizer, despite retaining limitations of its own, such as a budget $k$ that is fixed regardless of input complexity and a tendency to overfit to the training value of $k$. We introduce two sparsity regularizers compatible with the Top-$k$ architecture, both acting on the activations before the Top-$k$ selection: an $\ell_1$ penalty on the unselected (off-support) units, and a scale-invariant $\ell_1/\ell_2$-ratio penalty that concentrates the code onto fewer effective units. Both penalties are applied only to the batch-active units, those selected by the Top-$k$ operator at least once within the batch. Across two datasets, three vision foundation models, and a range of $k$, both regularizers consistently improve monosemanticity at no cost to reconstruction quality. The $\ell_1/\ell_2$ penalty further concentrates information into fewer latents, making reconstruction more robust to the inference-time choice of $k$ and improving small-budget linear probing. Our central finding is that hard architectural sparsity and soft sparsity regularization are complementary rather than mutually exclusive.

---


### 238. [RoPEMover: Depth-Aware Object Relocation via Positional Embeddings](https://arxiv.org/abs/2606.27332)

**<font color=#1a73e8>作者：</font>** Ipek Oztas, Duygu Ceylan, Aybars Bugra Aksoy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Moving an object in a single image requires geometry-consistent spatial rearrangement, including handling occlusions, revealing previously unseen regions, and maintaining coherent shadows and reflections. Existing approaches are not well suited to this setting and often fail to preserve such scene-level consistency. We address this problem by introducing a geometry-aware object motion method that operates directly on the positional representations of diffusion transformers. Our key insight is that rotary positional embeddings (RoPE) define a structured spatial field that can be explicitly manipulated to induce controlled motion. We extend 2D RoPE into a depth-aware formulation that encodes 3D spatial structure, enabling consistent object displacement and scene-aware updates. Our model is trained using synthetic data combined with a small set of real images via parameter-efficient fine-tuning. Despite minimal real supervision, it preserves object identity under large spatial displacements, generates plausible content in newly revealed regions, and consistently updates scene-dependent effects such as shadows and illumination. Experimental results on standard object motion benchmarks demonstrate state-of-the-art performance across all evaluation metrics.

---


### 239. [SAM2Matting: Generalized Image and Video Matting](https://arxiv.org/abs/2606.27339)

**<font color=#1a73e8>作者：</font>** Ruiqi Shen, Guangquan Jie, Chang Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite impressive advances in image matting, video matting remains challenging due to the inherent gap between high-level tracking, which requires frame-wise understanding, and low-level matting, which focuses on extremely fine-grained details. Existing methods attempt this with expensive and narrowly-scoped video matting datasets, which may limit out-of-domain generalization and compromise tracking robustness. We rethink the paradigm with SAM2Matting, a tracker-to-matting framework that advances VOS trackers to high-fidelity video matting. Specifically, it decouples the task by enhancing a foundational tracker (e.g., SAM2, SAM3) with a region-proposal bridge and dedicated matting heads, enabling the uncompromised tracker to handle temporal consistency while the matting components resolve fine-grained details. Notably, despite being trained only on images, SAM2Matting establishes new state-of-the-art performance on video matting, supports diverse prompt types, maintains strong temporal consistency, and demonstrates robust generalization across both human-centric and in-the-wild scenarios.

---


### 240. [RayPE: Ray-Space Positional Encoding for 3D-Aware Video Generation](https://arxiv.org/abs/2606.27345)

**<font color=#1a73e8>作者：</font>** Minghao Yin, Jiahao Lu, Wenbo Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern video diffusion transformers position their tokens through RoPE on the (u,v,t) axes -- a description of the camera's sampling grid that says nothing about the 3D structure of the scene. We observe that the geometric relation between two camera rays is captured by the Plucker reciprocal product, which is bilinear in the two rays -- the same algebraic form as the dot product in Transformer attention. Building on this analogy, we propose RayPE, a positional-encoding extension that injects per-token 6D Plucker coordinates additively into the queries and keys of self-attention, with a query/key flip arrangement under which the symmetric identity configuration coincides exactly with the reciprocal product. The injection is additive, the resulting attention score decomposes into a content term, a geometry term, and two content and geometry cross-terms -- all of which our experiments find individually necessary. To make the encoding stable across video data with heterogeneous camera-translation scales (SfM, deep SLAM, metric), we further decouple ray direction from moment magnitude, gate the encoding by a learned function of the log-magnitude, and apply RMSNorm to align it with the QKNorm-normalized content branch. The full module adds less than 0.1% parameters to a pretrained video DiT, is zero-initialized to start from the pretrained weights, and improves camera controllability, cross-frame 3D consistency, and overall video quality on a four-dataset training mixture.

---


### 241. [Error-Conditioned Neural Solvers](https://arxiv.org/abs/2606.27354)

**<font color=#1a73e8>作者：</font>** Haina Jiang, Liam Wang, Peng-Chen Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural surrogate models offer fast approximate mappings from PDE parameters to solutions, but they typically treat solving as a purely statistical task: once trained, they struggle to correct their own constraint violations and extrapolate beyond the training distribution. Recent hybrid methods promote physical correctness by targeting the PDE residual via gradient descent or Gauss--Newton steps, but inherit the compute cost and instability of the underlying classical optimizers. We show, theoretically and empirically, that numerically minimizing the PDE residual can be an unreliable proxy for reconstruction accuracy in ill-conditioned systems, explaining why these methods often do not make accurate predictions despite achieving low residuals. We propose error-conditioned Neural Solvers (ENS), built on a different principle: rather than an optimization target, the PDE residual field is passed as a direct input to the network at each iteration, enabling it to read the spatial structure of its own errors and learn an update policy to iteratively correct its predictions. Across four PDE families, ENS attains the highest prediction accuracy in the large majority of settings, with gains reaching $10\times$ on turbulent Kolmogorov flow, while avoiding the expensive compute cost of hybrid methods. ENS's learned correction policy generalizes under distribution shift, including zero-shot parameter changes and cross-equation transfer, where its relative advantage is largest in the ill-conditioned regimes where residual minimization is least reliable. Project website: this https URL.

---


### 242. [PhysiFormer: Learning to Simulate Mechanics in World Space](https://arxiv.org/abs/2606.27364)

**<font color=#1a73e8>作者：</font>** Yiming Chen, Yushi Lan, Andrea Vedaldi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present PhysiFormer, a diffusion transformer for physically-plausible 3D object motion. Unlike video world models that operate in view-dependent pixel space, PhysiFormer represents objects as 3D meshes expressed in world coordinates. Given the initial vertex positions and velocities, as well as object material type, rigid or elastic, the model samples future vertex trajectories. While related neural physics approaches build on ad-hoc latent spaces or explicitly enforce rigidity and causality, PhysiFormer shows that excellent results can be obtained without any such inductive biases, by casting vertex trajectory prediction as a single denoising diffusion process directly in world coordinates. The probabilistic formulation captures uncertainty in the learned dynamics, enabling diverse plausible futures from initial conditions, making this framework potentially useful for applications with unobserved uncertainty. The model features attention factorised over time, space, and objects for efficiency, enabling permutation-invariant multi-object reasoning without needing explicit object encoding. Trained on over 100k simulated trajectories, PhysiFormer generates rigid and elastic mechanics, and generalises to mixed-material settings, unseen real-world geometries, and larger object counts. It substantially outperforms autoregressive baselines in trajectory accuracy, rigidity preservation, and momentum-based physical consistency. Our results position coordinate-space diffusion as a promising step toward view-invariant, geometry-aware world modelling for robotics, graphics, and physical design. Visualisations, code, and models are available at this https URL.

---


### 243. [Don't Settle at the Mode! Mitigating Diversity Collapse in Pretrained Flow Models via Feature Self-Guidance](https://arxiv.org/abs/2606.27371)

**<font color=#1a73e8>作者：</font>** Pradhaan S Bhat, Rishubh Parihar, Abhijnya Bhat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> State-of-the-art flow models generate stunning images from text or image prompts. However, they suffer from diversity collapse when generating multiple samples under the same conditioning. Existing methods address this issue via either latent guidance, which has limited effectiveness, or sample selection, which relies on external reward models that incur significant inference-time overhead. In this work, we introduce an efficient, training-free self-guidance mechanism to mitigate diversity collapse without requiring additional reward models. Specifically, we disperse the internal features of the flow model during batch generation with feature self-guidance. Further, to keep the features close to the manifold, we introduce a manifold regularization step that projects these dispersed features back onto the data manifold, ensuring diverse generation without sacrificing alignment with the input conditions. Our method integrates seamlessly as a plug-and-play module into pretrained flow models, adding only a marginal inference cost. Experiments demonstrate significant improvements in diversity while preserving fidelity across several conditional flow models, including multi-step and few-step text-to-image, depth-to-image, and reference image generation.

---


### 244. [DnA: Denoising Attention for Visual Tasks](https://arxiv.org/abs/2606.27372)

**<font color=#1a73e8>作者：</font>** Ron Campos, Subhajit Maity, Xin Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The softmax activation in multihead attention (MHA) is the de facto standard for attention-based models in visual perception tasks. However, standard softmax can produce noisy attention patterns that dilute relevant features and degrade its performance. In this paper, we propose Denoising Attention or DnA, in which, first, a positive query identifies which image features belong to the correct class, and a negative query identifies closely associated but irrelevant image features. DnA then projects these interactions into two distinct subspaces with larger principal angles, promoting subspace separation and improved discriminability. Using a ViT-B backbone, our proposed DnA achieves an absolute gain of 0.8% on ImageNet-1K compared to the baseline. We further show improvements across multiple visual understanding tasks, including video understanding with video transformers (1.8%) and video LLMs (0.5%). Our extensive empirical analyses justify the design choices involving two interacting subspaces and the denoising effect of DnA.

---


### 245. [DanceOPD: On-Policy Generative Field Distillation](https://arxiv.org/abs/2606.27377)

**<font color=#1a73e8>作者：</font>** Wei Zhou, Xiongwei Zhu, Zelin Xu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern image generation demands a single model that unifies diverse capabilities, including text-to-image (T2I), local editing, and global editing. However, these capabilities are rarely naturally aligned and often conflict. For instance, editing tends to degrade T2I performance, while global and local editing interfere with each other. Consequently, effectively composing these capabilities has become a central challenge for image generation model training. To tackle this, we introduce DanceOPD, an on-policy generative field distillation framework for flow-matching models that routes each sample to one capability field, queries one low-noise student-induced state, and trains with a simple velocity MSE objective. With each capability source defined as a velocity field over the shared flow state space, the student learns from fields queried on its own rollout states to compose expert capabilities. This formulation also absorbs operator-defined fields such as classifier-free guidance. Comprehensive experiments on T2I, editing, realism-field absorption, and CFG absorption show that our approach improves multi-capability composition, strengthening target capabilities while preserving anchor generation quality. We believe this work establishes a practical route for generative field distillation in flow-matching models.

---


> [!TIP]
> 当前位于：**201-245**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-245**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
