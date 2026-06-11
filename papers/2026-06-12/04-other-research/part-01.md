# 📦 其他研究 | 2026年06月12日

> 本类共 **248** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-248](./part-05.md)

---

### 1. [Restless bandits with imperfect binary feedback: PCL-indexability analysis and computation](https://arxiv.org/abs/2606.11192)

**<font color=#1a73e8>作者：</font>** José Niño-Mora  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study restless bandits with binary latent states and imperfect binary feedback, motivated by opportunistic spectrum access with sensing errors. For the associated belief-state model, we develop a partial conservation laws (PCL)-based analytical and computational framework for establishing indexability and evaluating the Whittle index, building on a verification theorem for real-state discounted restless bandits. The framework analyzes the stochastic dynamics via an associated deterministic skeleton, renewal decompositions, and combinatorics on words. It yields tractable expressions for discounted reward and resource metrics in several threshold regimes, enabling full verification of the PCL-indexability conditions there. For the remaining regime, where a complete analytic verification is not achieved in this paper, we derive efficient numerical schemes for computing the relevant marginal metrics and the marginal productivity (MP) index, which equals the Whittle index when those conditions hold. Extensive computational experiments provide strong evidence that these conditions also hold in that regime across broad parameter ranges and without the stringent parameter restrictions imposed in prior work. The experiments further show that theMP index policy typically outperforms standard benchmark policies, often by a substantial margin.

---


### 2. [LatticeBridge: Rare-Event Sequential Inference for Faithful Structured Sequence Synthesis](https://arxiv.org/abs/2606.11203)

**<font color=#1a73e8>作者：</font>** Faruk Alpay, Bugra Kilictas  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Structured sequence generation often requires a model to satisfy several input-derived constraints in a single output. Standard decoding methods may assign high probability to fluent continuations while placing low mass on continuations that realize all required anchors jointly. We study this regime as a rare-event sequential inference problem. LatticeBridge combines a compact prefix language model, instance-compiled surface automata, and a twisted sequential Monte Carlo (SMC) decoder with resampling, multilevel splitting, and a source-support proposal term derived from instance-provided phrases. The constraint representation is compiled from each input instance and does not rely on manually curated lexical classes. On 2,610 attainable validation tasks spanning CommonGen, E2E NLG, and WikiBio, the particle decoder improves exact anchor satisfaction and mean anchor coverage over greedy, beam-filtered, and best-of-k ancestral baselines under a shared proposal model. Since exact anchor satisfaction alone does not rule out unsupported attribute substitutions, the evaluation reports required-anchor coverage, source coverage, source-intrusion diagnostics, overlap, runtime, and particle statistics jointly. The benchmark characterizes the faithfulness-overlap-latency frontier under a fixed proposal model.

---


### 3. [Dual-Stance Evaluation of Sycophancy: The Structure of Agreement and the Limits of Intervention](https://arxiv.org/abs/2606.11205)

**<font color=#1a73e8>作者：</font>** Matthew James Buchan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation steering can shift LLM behaviour, but standard evaluations do not typically test whether a sycophancy-reduction direction also suppresses agreement with factually correct statements. We introduce dual-stance evaluation, which tests both stances of each topic, and apply it to centroid-difference steering on Llama-3-8B-Instruct. We find a dissociation: the model represents sycophantic and factual agreement in geometrically distinct subspaces, yet the steering direction projects equally onto both and cannot differentially target either. The direction accordingly reduces agreement with factually correct statements (e.g. that the Earth is round) as well as sycophantic ones. All other static properties of the two activation groups are matched, suggesting the behavioural dissociation arises from generation dynamics or from finer-grained structure that residual-stream analysis cannot resolve. The pattern illustrates a general gap: representations that are readable from activations may not be writable through them.

---


### 4. [From Explicit Elements to Implicit Intent: A Predefined Library for Auditable Behavioral Inference](https://arxiv.org/abs/2606.11207)

**<font color=#1a73e8>作者：</font>** Liu hung ming  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present SemantiClean, a modular framework for extracting structured semantic signals from e-commerce session data and driving pluggable inference targets including purchase intent, customer segmentation, and product affinity through a shared element library. Unlike conventional end-to-end predictors that optimise solely for accuracy, SemantiClean prioritises auditability, structural governance, and sigma=0 reproducibility, explicitly trading marginal predictive gains for element-level transparency and defensible decision trails. Built upon the Online Shoppers Purchasing Intention (OSPI) dataset, the framework organises twenty-four behavioural elements into a four-layer architecture (Functional, Interaction, Systemic, Contextual) and enforces signal quality through three anti-inflation mechanisms: RedundancyGroup contribution caps, TieredPenaltyCalculator bias penalties, and AdaptiveConstraintMode cold-start this http URL report introduces the LLM-Integrated Semantic Inference Engine, a fully implemented two-phase LLM-driven inference architecture that leverages complete element metadata at inference time. All quantitative results reported herein are produced by this engine. Deterministic engine outputs remain fully reproducible (sigma=0); LLM-dependent results (E8, E10) are subject to controlled output variability under fixed provider/model/temperature settings. The gender inference target remains non-functional in the current implementation and is excluded from all quantitative results.

---


### 5. [BioDivergence: A Benchmark and Evaluation Framework for Hidden Contextual Contradictions in Biomedical Abstracts](https://arxiv.org/abs/2606.11208)

**<font color=#1a73e8>作者：</font>** Elias Hossain, Sanjeda Sara Jennifer, Sabera Akter Bushra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Biomedical findings often seem to conflict across studies, but many of these differences are context-dependent rather than true contradictions. Variations in cohort, geography, assay protocol, disease subtype, and clinical setting can make both claims locally valid. Existing NLI and scientific claim-verification benchmarks reduce such cases to entailment, contradiction, or neutral, failing to capture the contextual structure behind divergence. To address this, we introduce BioDivergence, an evaluation framework with a six-class conflict taxonomy, a 13-axis divergence ontology, and four structured outputs per claim pair: conflict type, divergence axes, dominant confounder, and reconciliation explanation. We release BioDivergence-Silver-v1.0, an article-disjoint silver benchmark of 11,865 claim pairs across five biomedical domains, alongside a legacy deduplicated variant for comparison. Results show notable ranking differences between the two variants, with the fine-tuned reference model dropping about 12 points under the article-disjoint setting, while Mistral-7B-Instruct-v0.3 achieves 0.5523 accuracy and 0.3894 contextual-F1 on the 842-example primary test set. BioDivergence offers a more faithful way to distinguish contextual divergence from direct contradiction and to separate article-level memorization from genuine task learning.

---


### 6. [Beyond Compaction: Structured Context Eviction for Long-Horizon Agents](https://arxiv.org/abs/2606.11213)

**<font color=#1a73e8>作者：</font>** Andrew Semenov, Svyatoslav Dorofeev  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Context Window Lifecycle (CWL), a context-management scheme that gives long-horizon LLM agents an effectively unbounded working horizon. As a session accumulates history, CWL keeps the context within budget through graduated, semantically-aware eviction: the agent annotates its trajectory as typed, dependency-linked episodes as work proceeds, and a deterministic, LLM-free policy evicts content in priority order within that structure when a token budget is exceeded. CWL preserves user turns and the exploratory context the agent is actively reasoning over, while aggressively shedding action episodes whose effects are already persisted in the environment, keeping active context near a stable ceiling that also avoids the performance degradation associated with very large prompts.
Compared to summarization-based compaction, CWL avoids four well-known limitations: unpredictable lossiness, destruction of causal structure, blocking model cost, and compression-induced hallucination. Compared to recency truncation, CWL is semantically aware: it drops the oldest-and-most-recoverable content according to the dependency graph rather than oldest-in-time regardless of relevance. We describe the annotation protocol, the episode graph, the eviction policy, and the token-accounting loop, and evaluate CWL on long-horizon agentic benchmarks: a single agent session completing 89 sequential tasks across 80 million tokens with no measurable degradation in task accuracy relative to per-task isolated sessions

---


### 7. [A Geometric Profile of Semantic Information in Text: Frame-Conditional Uniqueness and a Trade-Off Triangle for Scalar Summaries](https://arxiv.org/abs/2606.11222)

**<font color=#1a73e8>作者：</font>** Dmitriy Kompaneets  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How much meaning does a text carry? Shannon's theory measures uncertainty over symbols and is intentionally indifferent to meaning, while pairwise metrics such as BERTScore compare two texts rather than characterizing one. We develop a geometric framework that measures semantic content from the structure of a text's sentence embeddings.
The framework has three parts. First, within a fixed embedding and baseline, six natural axioms uniquely determine a scalar measure up to scale, a frame-conditional uniqueness theorem. The resulting scalar is empirically too coarse, motivating a richer representation. Second, we propose a three-coordinate semantic profile capturing novelty (displacement from generic discourse), breadth (diversity of distinct ideas), and integration (connectedness among them), together with a discrete minimal unit (the semantic quantum) whose resolution is fixed by a clustering threshold $\tau$. Third, we prove a no-go theorem: no scalar summary of the profile can simultaneously satisfy analytic stability under paraphrase and concatenation, ordinal robustness across text scales, and cross-representation comparability. We exhibit two practical scalars, $S_{\mathrm{minmax}}$ and $S_{\mathrm{rank}}$, each occupying a distinct corner of this trade-off triangle.
Validation across 23 synthetic categories, 5 Project Gutenberg novels, and 3 embedding models confirms the trade-off. The recommended rank-normalized configuration passes 25 of 28 ordinal checks as point estimates (21 of 28 after Benjamini-Hochberg correction), outperforming seven baselines including unigram entropy and a BERTScore-based novelty signal. A separate variational result connects the breadth coordinate to the log-determinant of a determinantal point process (Spearman $\rho = 0.985$ over 507 Gutenberg chapters), giving an optimization-theoretic foundation for breadth.

---


### 8. [CFCamo: A Counterfactual Detect-or-Abstain Framework for Camouflaged Object Detection](https://arxiv.org/abs/2606.11231)

**<font color=#1a73e8>作者：</font>** Suhang Li, Osamu Yoshie, Yuya Ieiri  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language reinforcement learning has recently shown strong target-present localization for camouflaged object detection (COD). Yet localization is only one side of the decision: when the agent faces an ordinary image with no camouflaged target, will it still claim that a camouflaged object exists? Standard COD training and evaluation data are positive-only, so agents optimized under this setting can acquire an over-detect bias, a task-specific form of object hallucination that standard COD evaluation leaves unmeasured. To quantify this target-absent behavior, we construct Counterfactual COD (CF-COD), a paired benchmark that removes the camouflaged target from each held-out COD evaluation image while preserving a plausible background. CF-COD evaluates whether a model detects the target on the original image and abstains on the target-absent counterfactual, summarized by Pair Accuracy (PA). We further introduce CFCamo, a paired counterfactual framework for COD with abstention. For training, CFCamo optimizes a Qwen3-VL-4B-Instruct agent with Counterfactual Sequence Policy Optimization (CSPO), which samples paired original-counterfactual rollouts and uses a Counterfactual Paired Reward (CPR) to couple original-image detection with counterfactual abstention. On CAMO-test, CFCamo improves S_alpha by +3.7 pp over the prior RL-based COD baseline; across CF-COD, it reaches 80.0-90.8% PA. Ablations show that removing counterfactual coupling reduces PA to 1.4-5.2% despite strong target-present COD scores, showing that target-present evaluation alone does not characterize detect-or-abstain behavior. Overall, these results indicate that CFCamo improves COD agents by coupling target-present detection with target-absent abstention, rather than merely strengthening target-present localization. Code and data are available at this https URL.

---


### 9. [OSCS-SupCon: Orthogonal Sigmoid-based Common and Style Supervised Contrastive Learning for Robust Feature Disentanglement](https://arxiv.org/abs/2606.11233)

**<font color=#1a73e8>作者：</font>** Bin Wang, Fadi Dornaika  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Supervised Contrastive Learning (SupCon) has achieved strong performance by explicitly modeling pairwise relationships among samples. However, existing SupCon-based methods suffer from two key limitations: negative-sample dilution induced by the standard InfoNCE loss, and feature-space entanglement caused by the lack of explicit constraints separating category-relevant (common) and category-irrelevant (style) features. These limitations reduce feature discriminability and generalization ability. To address these issues, we propose OSCS-SupCon (Orthogonal Sigmoid-based Common and Style Supervised Contrastive Learning), a unified framework that combines a sigmoid-based pairwise contrastive objective with explicit orthogonality constraints. Specifically, we introduce a sigmoid-based contrastive loss with two learnable parameters, temperature and bias, which adaptively modulate pairwise decision boundaries and alleviate negative-sample dilution. Furthermore, we enforce orthogonality between common and style feature subspaces via a linear projection with ReLU nonlinearity, thereby reducing feature overlap and improving disentanglement of style-irrelevant representations. Extensive experiments on six benchmark datasets demonstrate that OSCS-SupCon consistently outperforms state-of-the-art supervised contrastive learning methods across multiple backbone architectures. In particular, on the fine-grained CUB200-2011 dataset with a ResNet-18 backbone, the proposed method achieves a 3.4% improvement in classification accuracy over CS-SupCon, highlighting its robustness and generalization capability. Ablation studies further confirm the effectiveness of each component.

---


### 10. [Few-Shot Resampling for Scalable Statistically-Sound Data Mining](https://arxiv.org/abs/2606.11235)

**<font color=#1a73e8>作者：</font>** Leonardo Pellegrina, Fabio Vandin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A key step in knowledge discovery is the evaluation of data mining results. In several applications, including pattern mining, graph analysis, and others, this step includes the evaluation of the statistical significance of the results, to avoid spurious discoveries due only to noise or random fluctuations in the data. While specialized procedures have been developed for some specific applications, resampling-based approaches are widely used, in particular for complex analyses where analytical results cannot be derived. However, current resampling-based approaches require the generation and analysis of thousands of resampled datasets, and are therefore impractical for large datasets or computationally intensive analyses.
In this paper, we introduce FewRS, a simple and effective resampling-based approach to assess the statistical significance of data mining results with rigorous guarantees on the probability of false discoveries. Our approach can be used in every situation where resampling-based approaches are applied. FewRS builds on our derivation of a novel bound to the supremum deviation of test statistics representing the quality of data mining results. We prove that FewRS needs to generate and analyze an extremely small number of resampled datasets, leading to a highly scalable approach with wide applicability. We test our approach on common tasks such as pattern mining and network analysis. In all cases, our approach results in a reduction of up to two orders of magnitude in running time compared to the state of the art, while preserving high statistical power, enabling the statistical validation of data mining results on large-scale real-world datasets.

---


### 11. [ProHiFlo: Hierarchical Flow Matching with Functional Guidance for De Novo Protein Generation](https://arxiv.org/abs/2606.11243)

**<font color=#1a73e8>作者：</font>** Chuanzhen Wang, Meade Cleti, Pete Jano  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> De novo protein generation has transformative potential in therapeutic design, enzyme engineering, and synthetic biology. While diffusion-based and flow matching approaches have achieved progress, they typically operate at single resolution and lack mechanisms for incorporating functional constraints. We introduce ProHiFlo, a hierarchical flow matching framework with three innovations: (1) coarse-to-fine generation that models backbone geometry before refining to all-atom coordinates, reducing computational cost while maintaining accuracy; (2) functional guidance leveraging pretrained predictors to steer generation toward desired properties without retraining; (3) adaptive SE(3)-equivariant architecture for efficient multi-scale processing. Experiments on unconditional generation, motif scaffolding, and functional design demonstrate state-ofthe-art performance while requiring 4 fewer sampling steps. On enzyme active site scaffolding, ProHiFlo achieves 58.9% success rate compared to 41.2% for RFDiffusion.

---


### 12. [Position: Hippocampal Explicit Memory Is the Cornerstone for AGI](https://arxiv.org/abs/2606.11245)

**<font color=#1a73e8>作者：</font>** Sangjun Park  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have demonstrated remarkable capabilities across various tasks, raising expectations for Artificial General Intelligence (AGI). This position paper argues that integrating explicit memory is the cornerstone for advancing LLMs toward AGI. The key reason is that the underlying learning mechanism of LLMs is highly analogous to human implicit memory. However, higher-order cognitive functions necessary for AGI, such as long-term strategic planning, metacognition, and symbolic reasoning, heavily rely on hippocampal explicit memory and cannot arise solely from implicit statistical learning. Drawing on findings from neuroscience, I advance this perspective and complement it with computational requirements for artificial explicit memory systems, hoping to foster further research and lay the groundwork for explicit memory integration.

---


### 13. [Physics-informed generative AI for semiconductor manufacturing: Enforcing hard physical constraints in generative models by construction](https://arxiv.org/abs/2606.11247)

**<font color=#1a73e8>作者：</font>** Yaser Mike Banad, Sarah Sharif  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models are increasingly used to propose designs, data, and control actions for physical systems, yet many such systems are governed by hard physical constraints rather than by perceptual plausibility. Semiconductor manufacturing provides a demanding test case: generated masks, layouts, synthetic defect data, and process recipes must obey lithography, transport, reaction, and device-physics constraints, because physically invalid samples are not merely low quality but unusable. This Perspective argues that semiconductor manufacturing exposes a broader computational-science challenge, namely that generative AI for constrained physical domains must be physics-informed by construction, not corrected only through post-hoc filtering. We survey the emerging architectural toolkit, including physics-informed diffusion, PDE-constrained variational models, neural-operator priors, and conservation-law-respecting generative networks, and show how it connects to differentiable lithography, TCAD, process simulation, and autonomous experimentation. We identify four integration patterns between generative models and physics-based simulators, and we propose a research agenda centered on physics-fidelity benchmarks, differentiable simulator infrastructure, and multimodal foundation models for physical design and manufacturing. The central claim is analytical rather than rhetorical: where physical validity is the binding criterion of success, architectures that enforce it by construction should be expected to outperform those that filter for it after the fact, and the fab is the setting where this distinction is sharpest.

---


### 14. [Mechanical Field Networks: Structured Neural Dynamics for Multivariate Systems](https://arxiv.org/abs/2606.11251)

**<font color=#1a73e8>作者：</font>** Xingji Cui  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many multivariate dynamical systems are observed only through trajectories, leaving the mechanisms governing their joint dynamics hidden. Existing approaches can impose interpretable dynamics or learn flexible state transitions, yet the resulting interaction structure is typically either specified in advance or left implicit within the learned dynamics. We introduce MF-Net, a recurrent dynamical model that represents all variables in a shared field state and updates this state through a learned relation law. Each variable carries a field component, and these components evolve jointly through a learnable mechanical transition. Here, mechanical refers to the relation-to-motion organization of the transition, where learned relations shape state-dependent flows, field responses, and motion tendencies that move the field state forward. The resulting structure is part of the rollout itself: learned relations influence how the field moves, and the same internal quantities support both forecasting and structural readout. Across known-law interaction systems, chaotic benchmarks, real neural recordings, and ecological time series, MF-Net achieves competitive short- and medium-horizon forecasting while retaining inspectable structural readout. On the 40-dimensional Lorenz--96 testbed, MF-Net achieves an eight-step $R^2$ of $0.798\pm0.018$; across five seeds, its learned relation matrix recovers the local coupling support with a local/nonlocal strength ratio of $19.80\pm1.00$ and Precision@$K$ of $1.000\pm0.000$. MF-Net provides a structure-readable dynamical modeling framework in which learned relations are trained through forward evolution and, on real data, interpreted as functional predictive couplings under appropriate observational limits.

---


### 15. [Bernstein-Schur Kernels: Random Features by Sketched Modulation and Radial Randomization](https://arxiv.org/abs/2606.11255)

**<font color=#1a73e8>作者：</font>** Taha Bouhsine  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bernstein--Schur kernels are products of a finite-feature kernel (one with an explicit finite-dimensional feature map) and a completely monotone shift-invariant kernel: nonstationary kernels that fall between the shift-invariant and dot-product templates random features usually exploit, so in general neither Bochner sampling nor polynomial sketching applies to the full kernel directly. We give one random-feature construction for the whole class that \emph{randomizes both factors: it sketches the finite modulation and randomizes the completely monotone radial factor, sampling the latter's one-dimensional Bernstein--Widder scale and then applying Gaussian random Fourier features (whose frequency is still $d$-dimensional). The feature dimension is then $Dm$, set by the sketch size $m$ and the radial-draw count $D$, free of the $O(d^2)$ size of the exact modulation feature. Keeping the modulation \emph{exact} is the analyzable limit ($m\to\infty$): there we prove unbiasedness, an exact variance for the recommended flat estimator, an expected matrix-Bernstein operator-norm bound (with a matching high-probability tail) controlled by the top eigenvalues of the kernel and modulation Gram matrices together with an intrinsic dimension rather than the crude $N\max_{ij}$ entrywise route, and a deterministic relative-spectral kernel-ridge stability result. By conditioning on the sketch, the doubly-randomized estimator inherits the same intrinsic-dimension operator-norm guarantee plus a single additive sketch term, tunable by $m$ independently of $D$. The motivating instance is the biased $yat$-kernel $k_{yat,b}(w,x)=(w^\top x+b)^2/(\|w-x\|^2+\varepsilon)$, $b\ge0$, whose family span contains the inverse-multiquadric kernel by finite differences in $b$; for it the radial mixture is the IMQ spectral sampler, and one frequency per scale is variance-optimal at a fixed radial-feature budget.

---


### 16. [Loss Landscape Diagnosis for Gradient-Based Gray-Scott System Inversion: Disentangling the Roles of PINN Components](https://arxiv.org/abs/2606.11258)

**<font color=#1a73e8>作者：</font>** Yan Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gradient-based inversion of reaction-diffusion systems is typically approached via surrogate models or physics-informed neural networks (PINNs), while the most direct route, backpropagation through the PDE's structure itself, has largely been avoided. We pursue this direct route as a diagnostic probe, backpropagating a steady-state loss through unrolled Gray-Scott simulation to recover its parameters, with no surrogate or neural-network augmentation. Optimization fails to converge, and plotting the landscape directly locates the failure in its geometry -- flat plateaus with no gradient signal, bounded by sharp cliffs that align with bifurcation boundaries -- a structure that recurs across loss functions and is inherited however the gradients are routed to parameters. Reading this minimal setup as an ablation of PINN, we disentangle each component's role: with the neural network fixed, the residual loss is quadratic in the PDE parameters and yields a smooth landscape, so it alone already avoids the pathology, by implicitly encoding the full PDE dynamics across all initial conditions. The neural network, for its part, cannot repair an ill-posed parameter subspace, and so serves only to complete the observed data -- a division of labor not previously made explicit. These findings carry concrete design implications for PINN-type methods and a broader heuristic on when added dimensions actually help.

---


### 17. [When Poison Fails After Retrieval: Revisiting Corpus Poisoning under Chunking and Reranking Pipelines](https://arxiv.org/abs/2606.11265)

**<font color=#1a73e8>作者：</font>** Xi Nie, Hongwei Li, Shenghao Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) systems are vulnerable to corpus poisoning attacks that manipulate downstream model outputs through malicious knowledge injection. Existing studies mainly evaluate poisoning under simplified retrieval settings, overlooking practical RAG pipelines involving document chunking, dense retrieval, reranking, and grounded generation. In this paper, we revisit corpus poisoning under realistic multi-stage retrieval pipelines and show that many existing attacks substantially degrade after reranking despite achieving high retrieval-stage relevance. We identify retrieval granularity mismatch as a key reason for this failure: document-level adversarial signals are often fragmented during chunking, while rerankers favor locally coherent and answer-bearing passages rather than globally optimized semantic similarity. Based on this observation, we propose Chunk-aware and Rerank-Consistent Poisoning (CRCP), a poisoning framework that jointly optimizes retrieval relevance, reranker consistency, and chunk-boundary robustness. CRCP explicitly models chunking transformations during optimization to generate locally self-contained adversarial passages that remain effective under varying chunking configurations. Experiments on standard RAG benchmarks with multiple retrievers and rerankers show that existing poisoning methods are highly sensitive to chunk size and reranking strategies, whereas CRCP achieves substantially higher attack success rates and stronger robustness across realistic retrieval pipelines. Our findings highlight an important realism gap in current RAG security evaluation and suggest that poisoning in modern RAG systems should be studied as a multi-stage retrieval consistency problem rather than a retrieval-only problem.

---


### 18. [A prior-free blind detection of information leakage from model predictions](https://arxiv.org/abs/2606.11267)

**<font color=#1a73e8>作者：</font>** Laurence A. Jacobs  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data leakage -- contamination of a model with information unavailable at baseline -- is the dominant reproducibility failure in machine-learning-based science, yet detection tools require training code, external data, or domain expertise. None operates on the artifact an auditor most often holds: the model's output. We ask what can be decided about leakage from predictions and outcomes alone. We give a decision-theoretic framework in which leakage diagnostics are functionals of the predicted-risk/outcome law, parameterized by a threshold-weighting linked to proper scoring rules and decision-curve analysis. We prove a sharp impossibility: a recalibrated leak matching an honest model's calibration and discrimination is indistinguishable from honest performance by \emph{any} function of the predictions, so the broad class is detectable only against an externally supplied ceiling on achievable discrimination. We then prove what leakage cannot hide: a near-deterministic subgroup -- the signature of a near-label leak -- produces a sustained unit-purity head that no legitimate predictor of a non-deterministic outcome can manufacture, yielding a prior-free test. These results organize leakage into a trichotomy -- miscalibrated, broad-calibrated, and deterministic -- each with a matched detector and failure mode. We validate on UK Biobank using time-windowed comorbidity leakage with known, graded severity, measuring a detection floor of $\Delta\cstar \approx 0.007$ on this endpoint, below which residual leakage is undetectable from output and too small to alter conclusions. The numerical floor is cohort- and endpoint-specific; the structural lesson is general: output-only detection fails where residual leakage is indistinguishable from an honestly stronger predictor. The test returns a verdict on a prediction vector in under a second on commodity hardware.

---


### 19. [Traits Run Deeper: Trait-Specific Asymmetric Fusion for Personality Assessment](https://arxiv.org/abs/2606.11269)

**<font color=#1a73e8>作者：</font>** Jia Li, Qian Chen, Wei Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Personality assessment aims to infer stable personality traits from dynamic behaviors across language, voice, and facial cues. Since different personality dimensions are revealed through distinct behavioral perspectives, modeling trait-specific evidence is challenging. However, most existing approaches adopt a uniform multimodal fusion strategy across all dimensions, assuming identical modality contributions. This overlooks trait-specific modality preferences and introduces cross-modal interference. To address this issue, we propose a novel personality assessment framework called Traits Run Deeper, which consists of three components. Specifically, the Multimodal Foundation Representation (MFR) module constructs personality-oriented multimodal inputs and leverages psychology-informed semantic templates as anchors, enabling foundation models to capture trait-relevant information. Building upon MFR, the Trait-Specific Modality Fusion (TSMF) module acts as an asymmetric fusion mechanism, allowing each dimension to selectively exploit different modality pathways from modality-specific modeling to complementary fusion. Thus, TSMF captures heterogeneous modality preferences while reducing cross-modal contamination. Furthermore, the Distribution-Calibrated Personality Regression (DCPR) module mitigates label imbalance and central tendency bias through target distribution calibration, improving robustness and stability. Experimental results on the AVI Challenge 2026 validation set demonstrate the effectiveness of the proposed framework, reducing mean squared error (MSE) by approximately 25% compared with the baseline. Consistent improvements are observed on the official test set, where our method achieves the best performance and ranks first in the Personality Assessment Track. The source code will be made available at this https URL.

---


### 20. [Federated continual learning: A comprehensive survey on lifelong and privacy-preserving learning over distributed and non-stationary data](https://arxiv.org/abs/2606.11272)

**<font color=#1a73e8>作者：</font>** Masoume Gholizade, Fabrizio Ruffini, Pietro Ducange 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) enables collaborative and privacy-preserving model training across distributed clients, but most existing FL systems implicitly assume data stationarity. In real-world settings-such as healthcare, industrial IoT (IIOT), cybersecurity, and smart cities-data streams are inherently non-stationary, leading classical FL methods to suffer from performance degradation, instability, and catastrophic forgetting.
Continual Learning (CL) addresses learning under evolving data distributions but has been largely studied in centralized settings, overlooking key constraints of federated systems, including privacy, limited communication, and client heterogeneity. Federated Continual Learning (FCL) emerges at the intersection of FL and CL, aiming to support lifelong, adaptive, and privacy-aware learning over distributed and non-stationary data.
This survey provides a comprehensive and systematic overview of FCL. We first present a formal definition of the FCL problem and clarify its distinctive characteristics. We then analyze the limitations of classical FL under non-stationary conditions, highlighting how CL principles support long-term adaptation. To organize the rapidly growing literature, we propose a multi-dimensional taxonomy of FCL approaches. Furthermore, we review representative application domains and data modalities, summarize commonly used evaluation metrics, and discuss experimental perspectives for assessing long-term performance and forgetting. Finally, we highlight key open challenges, including handling extreme heterogeneity under temporal drift, designing scalable and privacy-preserving memory mechanisms, and establishing standardized benchmarks. This survey aims to serve as a reference and a roadmap for advancing FCL toward robust and deployable real-world systems.

---


### 21. [Multi-agent rendezvous in fluid flows via reinforcement learning](https://arxiv.org/abs/2606.11274)

**<font color=#1a73e8>作者：</font>** Bocheng Li, Jingran Qiu, Lihao Zhao  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Rendezvous is a critical task for multi-agent systems, requiring agents to coordinate to meet at an unspecified location. However, achieving this in fluid environments presents a challenge, as it remains unclear how agents can exploit underlying fluid kinematics to facilitate convergence. In this study, we adopt a multi-agent reinforcement learning (MARL) approach to develop physics-informed rendezvous strategies in vortical flows. Compared to a naive strategy, where agents navigate toward their counterparts, MARL strategies significantly improve the rendezvous rate. MARL strategies also show transferability across varying vortex intensities, vortex scales, and swarm sizes. By breaking the symmetry of the state-action map, MARL strategy leverages a non-intuitive mechanism that prevents agents from becoming trapped in separate vortices, thereby enhancing rendezvous success. Additionally, a heuristic strategy is extracted from the learned strategy and also outperforms the naive strategy. Furthermore, a theoretical analysis demonstrates that fluid deformation impedes the rendezvous process. Large finite-time Lyapunov exponents identify where fluid effects separate adjacent agents, suggesting that targets should be planned in weak-deformation regions. Our findings reveal the important role that agent-fluid interactions play in multi-agent tasks and highlight the MARL capability to explore swarm intelligence in complex flow environments.

---


### 22. [RoVE: Rotary Value Embeddings Attention for Relative Position-dependent Value Pathways](https://arxiv.org/abs/2606.11275)

**<font color=#1a73e8>作者：</font>** Alejandro García-Castellanos, Maurice Weiler, Erik J Bekkers  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rotary Position Embeddings (RoPE) make attention scores position-relative but leave the value pathway position-blind: the message sent by a value token is the same regardless of its distance from the query. We propose RoVE, a parameter-free modification that makes values position-sensitive by rotating them simultaneously with keys, and show that it turns RoPE attention into attentive convolution. This new perspective unifies several independent formulations of the same operation across computer vision, robotics, and modern LLM architectures. Trained 124M and 354M GPT-2 models show consistent empirical gains over RoPE on few-shot in-context learning, out-of-distribution perplexity, and long-context retrieval, with the clearest improvements on tasks that require long-range aggregation.

---


### 23. [Least-Action-Guided Diffusion for Physical Extrapolation](https://arxiv.org/abs/2606.11277)

**<font color=#1a73e8>作者：</font>** Zhongxin Yang, Yuanwei Bin, Xiang I.A. Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable extrapolation remains a central challenge for generative models in computational physics, because models trained over finite ranges of time, parameters, or geometries may produce physically inconsistent predictions outside the training distribution. We introduce a least-action-principle-guided diffusion, LAPG, a framework that promotes physical consistency during inference rather than relying solely on constraints imposed during training. The method combines a conditional score-based diffusion model with an action-derived physical guidance score. In the first stage, the learned score model generates an in-distribution proposal; in the second, an action-based variational prior refines this proposal toward the target out-of-distribution condition. This formulation turns the principle of least action into a differentiable inference-time correction mechanism and provides an alternative to pointwise residual penalties that often require empirical loss balancing.
We evaluate LAPG on representative ordinary- and partial-differential-equation systems, including free fall, conservative and dissipative spring-mass dynamics, interacting point vortices, and potential flow over parameterized airfoils. In temporal, parameter, and geometric extrapolation tests, LAPG reduces phase drift, preserves dissipative decay, captures vortex motion, and improves the lift response of airfoil flows compared with training-time physics-informed baselines.

---


### 24. [Phi-Actor-Critic: Steering General-Sum Games to Pareto-Efficient Correlated Equilibria](https://arxiv.org/abs/2606.11284)

**<font color=#1a73e8>作者：</font>** Wongyu Lee, Francesco Lelli, Omran Ayoub 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Real-world multi-agent systems, from traffic coordination to resource allocation, are often modeled as general-sum games where individual incentives conflict with collective welfare. In these settings, the central challenge is not merely finding an equilibrium, but selecting socially desirable outcomes among many suboptimal Nash equilibria. Standard deep multi-agent reinforcement learning (MARL) methods struggle with this problem, as value-decomposition approaches are constrained by monotonicity assumptions and policy-gradient methods often converge to stable but socially inefficient equilibria. To address this limitation, we propose $\Phi$-Actor-Critic ($\Phi$-AC), a framework that leverages swap regret minimization to steer learning toward high-welfare correlated equilibria (CE). To make counterfactual regret estimation tractable in deep MARL, $\Phi$-AC employs a centralized attention critic that predicts vector-valued regrets in a single forward pass, avoiding computationally expensive counterfactual simulations. We further introduce a Lagrangian-based equilibrium selection mechanism that optimizes social welfare while enforcing stability through regret constraints. Experiments on matrix games, Multi-Agent Particle Environments (MPE), and the Melting Pot Harvest scenario demonstrate that $\Phi$-AC learns efficient and stable coordination strategies across diverse mixed-motive settings while maintaining high collective return and competitive fairness.

---


### 25. [EventRadar: Long-Range Visual UAV Discovery through Spatiotemporal Event Sensing](https://arxiv.org/abs/2606.11285)

**<font color=#1a73e8>作者：</font>** Zhiting Zhou, Xingchen Liu, Xinglin Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unauthorized unmanned aerial vehicle (UAV) activity around airports, public venues, and other sensitive sites has made protected-airspace monitoring increasingly important. A practical sensing system must search a wide angular region, find small long-range targets, and return both bearing support and UAV-specific evidence before a restricted perimeter is breached. Existing UAV detection paths often rely on spatially organized evidence, such as body extent, silhouette, or track continuity. At long range, however, these cues become difficult to preserve and verify as the target footprint weakens and its image-plane support shrinks. EventRadar follows a complementary cue: propeller-induced temporal periodicity, which recent event-camera sensing studies have shown can reveal UAV-specific motion after appearance becomes weak. We extend this cue to kilometer-scale active sensing with an event-camera prototype. Scene-Anchored Geometry Evidence (SAGE) fuses scanning events with IMU pose to maintain a bearing-indexed scene memory, separating transient candidate support from persistent background clutter. Comb-guided Harmonic-Group Learned Iterative Shrinkage and Thresholding Algorithm (CHG) then treats each candidate as a weak high-rate timing signal and recovers phase-insensitive harmonic evidence with fixed compute. Compared with related event-camera baselines on 700-1500 m UAV event recordings, EventRadar achieves 0.990 mAP$_{.3}$ and 0.949 F1$_{.3}$, reduces FN$_{.3}$ to 0.009, and shows real-time feasibility in prototype profiling.

---


### 26. [FreeBridge: Variational Schrödinger Bridges for Cellular Transition Dynamics](https://arxiv.org/abs/2606.11286)

**<font color=#1a73e8>作者：</font>** Xurui Wang, Qin Ren, Jun Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-content imaging assays quantify cellular responses to chemical and genetic perturbations, yet continuous trajectories of individual cells are unobservable because cells are chemically fixed at acquisition. Perturbation modeling therefore reduces to inferring stochastic transport between control and treated populations observed only as separate marginals. While recent generative models achieve strong end-point alignment, boundary consistency does not determine intermediate evolution: multiple stochastic processes may connect identical marginals while traversing regions unsupported by observed single-cell morphologies. We introduce \textbf{FreeBridge}, a Schrödinger Bridge formulation for single-cell transition modeling under endpoint-only supervision. FreeBridge defines atomic states as instance-segmented single-cell representations, establishing a fixed cellular manifold, and learns stochastic transport constrained within this geometry via empirical latent support regularization. Across BBBC021, RxRx1, and JUMP, FreeBridge maintains competitive or improved endpoint fidelity and mechanism-of-action retention under a unified evaluation protocol; on BBBC021, it further reduces intermediate support violations. These findings highlight the importance of geometric grounding for biologically interpretable perturbation dynamics. Project page: this https URL.

---


### 27. [i1: A Simple and Fully Open Recipe for Strong Text-to-Image Models](https://arxiv.org/abs/2606.11289)

**<font color=#1a73e8>作者：</font>** Boya Zeng, Tianze Luo, Shu Pu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have consistently driven progress in text-to-image generation. However, it is challenging to attribute recent progress to specific modeling and data choices: state-of-the-art open-weight models provide limited ablations, and do not disclose their training data and full training details. The research community needs fully open (weights, data, and code) models as a foundation for further research; yet existing fully open models still fall significantly short of leading models in performance. In this project, we conduct a systematic investigation of the modeling and data design choices in text-to-image diffusion training and inference with 300+ controlled experiments totaling 700K+ TPU v6e hours. Our experiments highlight several empirical findings (e.g., equal weighting is a strong default for mixing curated datasets) and simple design decisions (e.g., larger text encoder adapters improve performance with minimal added parameters) for training strong models. Guided by these insights, we train i1, a 3B-parameter text-to-image diffusion model using only publicly available datasets. i1 is competitive with leading models on five representative benchmarks (GenEval, DPG, PRISM, CVTG-2K, and LongText), and outperforms the best existing fully open model by 29.5 absolute percentage points on average. We provide the i1 checkpoints, training and inference code, and the data processing pipeline. Together, our findings and the i1 recipe establish a practical foundation for future open research in text-to-image diffusion models. Our code is available at this https URL.

---


### 28. [TRON: Tracing Rays to Orchestrate a Neural Renderer for 3D Gaussian Reconstructions](https://arxiv.org/abs/2606.11314)

**<font color=#1a73e8>作者：</font>** Or Perel, Hassan Abu Alhaija, Zian Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce TRON, a rendering framework that combines 3D Gaussian ray tracing with neural rendering to enable realistic and controllable rendering of real-world 3D scenes under novel lighting, dynamic object motion, object insertion, and material editing. Prior approaches that rely solely on physically based rendering (PBR) of Gaussian representations struggle to achieve realistic relighting due to imperfections in reconstructed geometry, material estimates, and light transport estimation. At the same time, neural rendering methods often lack an explicit scene representation, limiting their ability to support interactive editing with fine-grained manipulation. TRON bridges these two paradigms. We use intrinsic decomposition priors from a learned inverse rendering model to regularize the material properties of a Gaussian field, and repurpose a ray tracer to provide radiometric guidance rather than final pixels. By treating this output as a structured 3D scaffold, we empower a lightweight neural renderer to bridge the domain gap between shading-model constrained estimates and photorealistic output. Our key insight is that the combination of explicit 3D knowledge with robust material priors provides speed and controllability, while neural rendering enables the synthesis of photorealistic images. To support real-world scenarios, we train our neural renderer with a multi-stage strategy consisting of large-scale pretraining and targeted fine-tuning on a newly constructed dataset of 2.1M rendered synthetic and real-world frames from 3D reconstructions. TRON outperforms Gaussian-based relighting methods in realism, and prior neural renderers in editability and speed. To the best of our knowledge, TRON is the first method to enable practical interactive applications in captured 3D environments, offering realistic appearance under dynamic geometric, lighting and material conditions.

---


### 29. [Learning from almost nothing: How neural networks survive heavy input corruption](https://arxiv.org/abs/2606.11319)

**<font color=#1a73e8>作者：</font>** Justin Tahmassebpur, Asadullah Bhuiyan, Hyejin Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning from imperfect data is a central theme in machine learning, connecting practical questions of robustness to fundamental questions of learnability. Here we examine attribute noise: learning from corrupted inputs while keeping the labels intact, a setting that has received considerably less analytical attention than its label-noise counterpart. We consider two types of corruption models: additive noise and replacement noise. Through experiments with multi-layer perceptrons (MLPs) on corrupted classification datasets, we find that neural networks remain robust, maintaining well-above-chance accuracy even when inputs are >90% corrupted -- far beyond human recognition. To understand this robustness, we analyze infinite-width networks in the heavy-corruption regime using a mean-field-inspired approach and derive a leading-order decision rule for the classification outcome: the network implements a prototype rule, the nearest-class-mean, assigning each test point to the class whose training-set average it most closely resembles. This leading-order decision rule is universal across a broad range of MLP architectures, holding for any depth, as well as a wide class of activation functions and noise distributions. The same centroid mechanism closely matches finite-width network behavior in our experiments and provides an interpretable and analytically tractable account of why learning can succeed even when individual training examples carry almost no signal.

---


### 30. [Semantic Segmentation of Node and Edge Diagrams for Assistive Technology](https://arxiv.org/abs/2606.11320)

**<font color=#1a73e8>作者：</font>** Michael Cormier, Yichun Zhao, Laura Paul 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we present a novel set of related models for semantic segmentation of node-link diagrams. These diagrams are frequently used to represent mathematical graphs, relationships between concepts, and flowcharts. Such diagrams are difficult to access non-visually; while some assistive interfaces have been designed for node-link diagrams, they rely upon a machine-readable representation of the diagram, whereas such diagrams will generally be made available as bitmap images. Our compact deep learning models show excellent quantitative and qualitative performance on a large synthetic dataset of node-link diagrams, reaching per-pixel accuracy over 93\%.

---


### 31. [DarkVGGT: Seeing Through Darkness Using Thermal Geometry without Daylight Tax](https://arxiv.org/abs/2606.11326)

**<font color=#1a73e8>作者：</font>** Minseong Kweon, Wenyuan Zhao, Nuo Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent feed-forward 3D reconstruction methods have demonstrated strong performance and flexibility in efficient end-to-end scene geometry estimation from image streams. However, their reliance on visible-light appearance makes them vulnerable in dark and low-visibility environments, where RGB cues are severely degraded and geometric evidence becomes ambiguous. To address this challenge, we propose DarkVGGT, an RGB-T feed-forward geometry framework that uses physics-aware thermal modeling for robust 3D estimation in low-light scenes. DarkVGGT introduces two complementary modules. First, physics-inspired thermal factorization extracts emissive-dominant, geometry-consistent thermal cues while isolating sparse reflective residuals that may introduce geometric ambiguity. Second, geometry-shared thermal routing isolates modality-invariant geometric structures from thermal-specific patterns, selectively injecting reliability-aware structural guidance into the RGB stream. Together, these components enable accurate thermal-informed geometry estimation under degraded RGB conditions while largely preserving performance in well-lit environments. Experiments on low-visibility RGB-T benchmarks demonstrate consistent improvements in both depth and camera pose estimation over existing feed-forward geometry baselines.

---


### 32. [Towards a Joint Understanding of Remote Operation for Vehicles in Public Road Traffic](https://arxiv.org/abs/2606.11336)

**<font color=#1a73e8>作者：</font>** Elisabeth Shi, Maria-Magdalena Wolf, Nina Theobald 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Sustained driving automation systems are envisioned to be used as the foundation for driverless mobility services. However, both researchers and practitioners acknowledge that current driving automation systems are not yet able to handle all traffic situations that a human driver can handle. To bridge this gap and enable mobility services without an in-vehicle human driver or fallback, remote operation (or teleoperation) is increasingly discussed. Recently, first legal actions have been taken to enable some forms of remote operation on public roads. Remote operation encompasses a broad spectrum of methods to support a driving automation system, ranging from remote assistance, which includes providing information or releasing a maneuver, to remote driving, which includes driving the vehicle from a remote location. As such, safe implementation of remote operation in public road traffic challenges the collaboration of multiple academic disciplines (e.g. engineering, psychology, informatics, law, etc.) and stakeholders (e.g. remote operation service providers, remote operators, vehicle manufacturers, regulatory authorities, etc.). At the same time, the interdisciplinary discourse is often challenging due to differing expectations and language. To build a common ground, this article traces terminology back to the original differences in information processing both on human and vehicle side. This framework aims to help further discourse by directly specifying what is needed to engage a diverse audience including researchers and stakeholders of different backgrounds and interests. Recently discussed forms of teleoperation are integrated into this framework.

---


### 33. [Can AI Agents Synthesize Scientific Conclusions?](https://arxiv.org/abs/2606.11337)

**<font color=#1a73e8>作者：</font>** Hayoung Jung, Pedro Viana Diniz, José Reinaldo Corrêa Roveda 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific AI agents increasingly retrieve evidence, reason across sources, and synthesize conclusions used in consequential decisions. Yet, their ability to do so in high-stakes domains such as health remains unclear. We introduce SciConBench, a large-scale live benchmark of 9.11K questions and expert-written conclusions from systematic reviews to evaluate open-domain scientific conclusion synthesis. The benchmark draws on an expert-validated automated evaluation pipeline that decomposes conclusions into atomic facts and measures correctness and comprehensiveness via factual precision and recall. To mitigate data leakage, we further introduce SciConHarness, a clean-room evaluation harness that equips agents with controlled web interaction to ensure valid measurement. Evaluating 8 frontier models and deep research agents, we find that factual quality remains low: under clean-room settings, the best agent achieves only a factual F1 of 0.337. Our clean-room setting consistently reduces performance relative to unconstrained evaluation, suggesting that leakage inflates estimates of models' true synthesis capabilities. Finally, we audit consumer-facing agents (e.g., Google AI Overview, OpenEvidence) and find they frequently generate incomplete and sometimes contradictory conclusions, even when the ground-truth answer is available. Overall, our results show that reliable synthesis of scientific conclusions remains an open challenge, and that clean-room evaluation is essential for assessing open-domain AI agents.

---


### 34. [Energy-Conserved Neural Pipelines: Attenuating Error Propagation in Modular Neural Networks via Physical Conservation Constraints](https://arxiv.org/abs/2606.11341)

**<font color=#1a73e8>作者：</font>** David Young, Swan Yi Htet  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modular neural network pipelines suffer from error compounding: noise at any module boundary propagates and potentially amplifies through subsequent modules. We introduce energy conservation as a hard physical constraint on inter-module information flow. Activation energy (the squared L2 norm of feature vectors) is enforced to be exactly preserved at every module boundary. Unlike soft energy penalties, conservation is an inviolable law: the network may redistribute energy across neurons but cannot create or destroy it. Four experiments on CIFAR-10 demonstrate: (1) conservation retains 77.4% of clean accuracy at noise sigma=0.2, versus 35.1% for baselines and 30.9% for energy-penalized models (p<0.001, 5 seeds); (2) pipelines become depth-invariant, retaining 93.3% at depths 2 through 5 with noise at every boundary; (3) the advantage generalizes to systematic bias (+45.1%), Gaussian (+40.4%), and adversarial noise (+4.8%), with a principled non-effect on dropout (-0.3%); (4) on ResNet-18, the conservation advantage scales inversely with intrinsic normalization: +0.3 pp with BatchNorm, +26.2 pp without at sigma=0.2, reaching +58.0 pp at sigma=0.5. Experiment 5 validates the operator on a real modular robotic pipeline (MuJoCo physics, Franka Panda). Across three independent runs on separate machines (90 trials per cell), conservation provides +18.9 pp average advantage on monocular-depth-style noise. A formal bound proves conserved noise energy is strictly less than input noise energy.

---


### 35. [SwiftCTS: Fast Cross-Design Prediction and Pareto Optimization of Clock Tree Metrics via Few-Shot Calibration](https://arxiv.org/abs/2606.11348)

**<font color=#1a73e8>作者：</font>** Barsat Khadka, Kawsher Roxy, Md Rubel Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clock Tree Synthesis (CTS) is a computationally expensive stage in the physical design flow, requiring iterative EDA tool invocations to navigate a vast configuration space for optimal power, wirelength, and timing skew. Existing machine learning approaches require computationally expensive retraining or fine-tuning cycles to adapt to unseen macro architectures and are architecturally mismatched to the millions of evaluations demanded by exhaustive combinatorial search. We present SwiftCTS, a physics-informed surrogate framework that addresses both limitations simultaneously. By coupling lightweight, physics-grounded statistical features with gradient-boosted ensembles, SwiftCTS trains in under five seconds on a CPU and delivers sub-millisecond inference without GPU support. To handle out-of-distribution (OOD) designs without retraining or fine-tuning, we introduce a K-shot multiplicative calibration mechanism that anchors predictions to just one or two physical reference runs, reducing power prediction error from 24.5\% to 3.3\% and wirelength error from 56.6\% to under 1\% on unseen macros. Integrating this engine with an evolutionary optimizer, SwiftCTS evaluates 100,000 CTS configurations in under ten seconds, yielding Pareto-optimal frontiers that are physically validated within the OpenROAD flow. Closed-loop validation confirms prediction errors below 0.5\% for power and wirelength, and timing skew predictions within five picoseconds on an OOD benchmark, consistently outperforming default tool heuristics across all target metrics. Code publicly available at: \href{this https URL}{this https URL}

---


### 36. [Knowing When to Ask: Self-Gated Clarification for Hierarchical Language Agents](https://arxiv.org/abs/2606.11349)

**<font color=#1a73e8>作者：</font>** Aijing Gao, Yiming Kang, Mengdie Flora Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In hierarchical reasoning, failures often originate at intermediate decision points where the agent commits to a wrong branch without recognizing that it lacks critical information. Rather than treating clarification as an external uncertainty trigger, we propose ACTION-RATING, a formulation that places it inside the agent's action space on a shared ordinal scale with navigation, so that asking competes directly with acting at every decision point and help-seeking becomes observable at intermediate states. Two structurally distinct information-seeking modes emerge from the agent's own ratings: mandatory (no viable branch) and opportunistic (residual uncertainty despite a leading candidate). On Harmonized Tariff Schedule classification (30,000-node taxonomy, three benchmarks, 9~LLMs across 4 families), we observe a regime shift from mandatory to opportunistic clarification, with Information-Seeking Effectiveness (ISE), a local diagnostic defined as the fraction of help interactions followed by a correct next navigation step (not a final-task metric), rising from 50% to 74%. Three diagnostic contrasts fail to reproduce this structure. A separability test shows that the information-seeking pattern (mode split, ISE ranking) persists when answer quality is degraded (-18.8% accuracy), supporting an empirical separation between where an agent seeks help and the quality of the help it receives. Under the controlled answer channel, accuracy gains reach +16.2% at 10-digit; we read this as an upper bound on what better localization could unlock, not a deployment estimate.

---


### 37. [NSVQ: Mitigating Codebook Collapse by Stabilizing Encoder Drift in Vector Quantization](https://arxiv.org/abs/2606.11363)

**<font color=#1a73e8>作者：</font>** Hao Lu, Yongxin Guo, Onur Koyun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vector quantization is central to modern generative modeling pipelines, but large-codebook VQ models often suffer from codebook collapse. We identify encoder drift as a key driver of this failure: as the encoder moves the latent distribution, sparsely updated code vectors can lag behind, lose assignments, and increase quantization error, creating a feedback loop through the straight-through estimator. We propose NSVQ, a non-stationary-aware VQ training strategy that combines a dense non-stationary embedding loss, codebook replacement, and stage-wise encoder freezing. NSVQ first helps the codebook track encoder drift during early training, then freezes the encoder to consolidate the codebook under a fixed latent geometry, and finally reintroduces adversarial refinement. Experiments on ImageNet-1k show that NSVQ improves reconstruction quality while maintaining full codebook utilization. On ImageNet-1k at 128$\times$128 with 65,536 codes, NSVQ reduces rFID from 2.39 to 2.10 compared with SimVQ, while both methods maintain 100\% utilization. Additional latent diffusion experiments show that NSVQ also improves downstream ImageNet generation FID.

---


### 38. [The Dynamics of Human and AI-Generated Language: How Semantics Fluctuates across Different Timescales](https://arxiv.org/abs/2606.11371)

**<font color=#1a73e8>作者：</font>** Han-Jen Chang, Yasir Çatal, Angelika Wolman 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Spoken language, whether produced by humans or large language models (LLM), unfolds over time with varying semantic content. However, we still lack simple, interpretable time-series features that capture how generic versus specific content is distributed over time, and that can be used to compare human and AI-generated speech. We introduce a semantic-timescale analysis pipeline that turns word-level transcripts with timestamps into semantic time-series. For each spoken narrative, we compute (i) semantic specificity using WordNet-based word depth and (ii) contextual similarity using SBERT embeddings and quantify their temporal dependence using autocorrelation-window measures (ACW-0 and related metrics). We then compare original speech to multiple shuffled controls that selectively disrupt lexical identity, temporal order, and word duration. Across human-read autobiographical narratives, TTS readings, and LLM-generated texts rendered with TTS, we find that segments with longer ACW-0 in the semantic time-series tend to contain more generic vocabulary, whereas segments with shorter ACW-0 are enriched in more specific words. These associations are strongly attenuated or abolished when word order and timing are randomized, indicating that ACW-based measures capture non-trivial temporal organization of semantic content beyond static lexical distributions. Our results suggest that ACW-based semantic timescales are a useful family of features for analyzing and comparing the temporal structure of human and AI-generated speech.

---


### 39. [From Simulation to Real-World: An In-Field 6D Pose Dataset and Baseline for Robotic Strawberry Harvesting](https://arxiv.org/abs/2606.11381)

**<font color=#1a73e8>作者：</font>** Woojung Son, Won Suk Lee, Zijing Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robotic strawberry harvesting requires precise 6D pose estimation; however, collecting 6D pose ground truth in real agricultural fields is inherently challenging. Existing 6D pose estimation methods have therefore relied solely on synthetic data that lacks scene-level realism, leaving their performance under real agricultural field conditions unquantified. In this work, we present, to the best of our knowledge, the first real-world 6D pose ground truth dataset of strawberries collected in actual agricultural fields (12,040 images). We also introduce a synthetic dataset rendered in NVIDIA Isaac Sim, featuring scene-level realism and domain randomization. Nevertheless, our experiments reveal that a significant sim-to-real gap persists, underscoring the necessity of real agricultural field data for reliable evaluation. We further quantify the sim-to-real gap through baseline 6D pose estimation results across backbone encoders, serving as a reference for future work. The real-world dataset will be made available upon acceptance.

---


### 40. [Small Experiments, Cheaper Decisions: A Case Study in Staged Promotion for Micro-Pretraining](https://arxiv.org/abs/2606.11387)

**<font color=#1a73e8>作者：</font>** Felipe Chavarro Polania  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Short pretraining runs can reduce experimental cost, but they can also over-promote configurations that only look strong at tiny budgets. We study an auditable staged-promotion protocol for a fixed micro-pretraining runner on two heterogeneous host blocks: Windows A100 and Linux L40S. Starting from twelve prior-screened configurations, we use staged budgets of 2 minutes, 5 minutes, 10 minutes, 60 minutes, and 12 hours, with frozen promotion rules before expensive continuations.
The early screens are intentionally treated as unstable: the 5- and 10-minute rankings are host-sensitive, and the eventual 12-hour top-ranked condition is not the mean-best condition at the replicated 10-minute gate. Because seed ranges differ across stages, these changes are operational promotion evidence, not within-seed curves. A replicated 60-minute gate keeps the Staged Factorial Screening bridge reference in the promoted set, where it ranks first in all four 60-minute host-seed cells. In the final 12-hour confirmation package, the bridge condition ranks first in all four host-seed cells across two seeds; the greedy comparator does not meet the frozen 0.010 val_bpb near-equivalence rule; and the cheaper d8/ar48 (depth-8, aspect-48) sentinel does not meet the frozen 0.020 mean-gap rule.
The executed 12-hour branch spends 144 GPU-hours, and the full staged protocol records 169.2 training GPU-hours including screening stages. Continuing all four 60-minute candidates would spend 192 GPU-hours, while continuing all nine replicated 10-minute candidates would spend 432 GPU-hours. The latter numbers are accounting counterfactuals for unrun continuations, not evidence that skipped candidates could not have overtaken the reference. The result is a bounded cost-allocation finding, not a claim of global optimality, capacity-normalized superiority, or superiority over adaptive hyperparameter optimization methods.

---


### 41. [A Scalable PyTorch Abstraction for Multi-GPU Gaussian Splatting](https://arxiv.org/abs/2606.11390)

**<font color=#1a73e8>作者：</font>** Matthew Cong, Francis Williams, Jonathan Swartz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaussian splatting methods have become increasingly popular for neural reconstruction of the real world. However, they are often limited in scale and resolution due to compute and memory constraints. We present a multi-GPU Gaussian splatting approach that scales reconstruction to higher resolutions and larger scenes while abstracting away the code complexity typically associated with distributing a model. To accomplish this, we propose a PyTorch backend that distributes the Gaussian parameters and splatting operators across GPUs via CUDA unified memory and NVLink. Because distribution occurs at the operator level, the model code requires no explicit cross-device communication. More broadly, the backend exposes multiple GPUs as an aggregate PyTorch device and supports other PyTorch operators. We demonstrate city-scale reconstructions with street-level detail consisting of over 1 billion Gaussian splats, more than 25 times as many as the current state of the art.

---


### 42. [Recursive Binding on a Budget: Subspace Carving in Order-p Tensor Memories](https://arxiv.org/abs/2606.11391)

**<font color=#1a73e8>作者：</font>** Travis Pence, Daisuke Yamada, Vikas Singh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tensor Product Representations provide the structural fidelity required for symbolic reasoning in models but suffer from exponential dimensionality growth when encoding deep recursive structures. Conversely, Vector Symbolic Architectures maintain constant dimensionality but sacrifice capacity and fidelity due to noisy compression via superposition. In this work, we propose Orthogonal Subspace Carving (OSC), a memory architecture that binds fillers to roles by projecting onto the null space of the role basis before aggregating into a fixed order-p tensor. OSC uses projections to enforce geometric orthogonality between bound structures within a static memory trace. We show that this mechanism decouples the tensor order from the structural depth, enabling deep recursive binding within a constant memory footprint. By performing retrieval via recognition, this construction allows for component vectors that are orders of magnitude smaller than the memory tensor, giving superior memory efficiency in settings involving high superposition. We also show that TPR is a special case of binding in Clifford algebra, and give a Clifford formulation of OSC.

---


### 43. [Signed Compression Progress on a Sealed Audit is Goodhart-Resistant](https://arxiv.org/abs/2606.11417)

**<font color=#1a73e8>作者：</font>** Ayush Mittal, Dhruv Gupta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Compression progress is a long-standing proposal for intrinsic motivation: reward an agent when its world model becomes better at predicting or compressing experience. The folk claim is that this reward is "credible" because it is paid only for learning. We make this precise and prove it. If intrinsic reward is the signed decrease of a fixed sealed-audit loss, r_t = E(theta_{t-1}) - E(theta_t), then cumulative reward telescopes exactly to endpoint audit improvement, so no policy can push reward up indefinitely while true audit performance stagnates or degrades. For finite audit panels the same result holds with a sharp false-positive budget: cumulative empirical reward is at most true audit improvement plus 2 Delta_n(F, delta), the uniform audit deviation of the model class. This is horizon-free: adaptivity over time costs nothing once the sealed panel uniformly controls the class.
The theorem also identifies the failure modes: the guarantee disappears if progress is clipped, scored on the agent's own stream, exposed to a high-capacity model on a reusable panel, or applied to a neural class that makes Delta_n vacuous. We give a Lean 4 mechanization of the structural core (telescoping, the finite-audit bound, finite Gibbs, and the entropy floor) and an experiment suite on ARC-TGI grid-transformation generators with adaptive holdout attacks. Experiments confirm the theory: finite-audit deviation scales as n^{-0.527}; signed progress resists clip-farming, stream leakage, and noisy-TV curiosity; naive reusable audits are exploitable by black-box scalar feedback, while standard release defenses keep the attack below the 2 Delta_n threshold. Signed compression progress on a sealed audit is an accounting signal of genuine improvement.

---


### 44. [SOMA-SQL: Resolving Multi-Source Ambiguity in NL-to-SQL via Synthetic Log and Execution Probing](https://arxiv.org/abs/2606.11424)

**<font color=#1a73e8>作者：</font>** Sai Ashish Somayajula, Marianne Menglin Liu, Chuan Lei 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural language interfaces to databases aim to translate user questions into executable SQL, yet remain brittle in real-world settings where questions are underspecified and schemas are large and ambiguous. Ambiguity across user questions, database schemas, and model interpretations are central failure modes in NL2SQL, leading to misaligned intent, incorrect schema grounding, and erroneous SQL generation. Existing approaches rely on human clarification or treat ambiguity as a schema representation problem, but these do not scale nor resolve ambiguity autonomously. We propose SOMA-SQL to automatically resolve ambiguity via targeted synthetic query log and ambiguity-driven probing. SOMA-SQL constructs synthetic query log to ground schema interpretation and guide candidate SQL generation; it then executes targeted probing queries, driven by a structured ambiguity taxonomy and candidate disagreements, to produce disambiguation evidence for final SQL selection and repair. This active approach to ambiguity discovery and resolution generalizes across unseen schemas and query distributions without human-in-the-loop. Experiments on six public benchmarks demonstrate that SOMA-SQL improves execution accuracy by 13.0% on average over state-of-the-art baselines, with gains of up to 16.7% on ambiguous questions.

---


### 45. [JailbreakOPT: Tool-Assisted Iterative Jailbreak Prompt Optimization](https://arxiv.org/abs/2606.11425)

**<font color=#1a73e8>作者：</font>** Ge Shi, Jun Yin, Donglin Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Jailbreak attacks expose persistent safety weaknesses in large language models (LLMs), but existing stateless single-turn methods face a trade-off: hand-crafted prompts are expressive but static, while iterative prompt optimization can adapt but often relies on low-level mutations that require many target queries. We propose JailbreakOPT, a tool-assisted framework for improving iterative single-turn jailbreak prompt optimization. JailbreakOPT organizes diverse atomic jailbreak prompts into an attack tool library and composes them through a unified intra-episode optimization abstraction to generate stronger standalone attack prompts. To reuse experience across attack episodes, JailbreakOPT further frames tool selection as a contextual bandit problem and applies contextual Thompson sampling to guide exploration and exploitation based on past outcomes. Experiments across multiple target LLMs and attack goals show that JailbreakOPT improves attack success rate (ASR) while reducing the number of attacks until success (No.A) compared with atomic single-turn attacks and existing iterative optimization baselines. This paper may contain offensive or harmful content.

---


### 46. [Mirror Descent Beyond Euclidean Stability: An Exponential Separation in Initialization Sensitivity](https://arxiv.org/abs/2606.11431)

**<font color=#1a73e8>作者：</font>** Shira Vansover-Hager, Matan Schliserman, Ofir Schlisselberg 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mirror Descent (MD) extends Gradient Descent (GD) beyond Euclidean geometry and has recently reappeared as a lens for KL-regularized policy optimization in reinforcement learning and LLM post-training. This raises a basic robustness question, crucial to reproducibility and reliability: how sensitive are MD dynamics to their inputs? We focus on initialization, often itself a pretrained or previously aligned model. Quadratic-regularized MD, including GD and Mahalanobis geometries, is well-known to be stable for convex smooth objectives. We show a sharp contrast: once the regularizer is non-quadratic, MD can be exponentially more sensitive to initialization than GD, even with a well-conditioned regularizer in Euclidean norm. We give a three-dimensional construction with a convex, smooth objective and a strongly convex, smooth, well-conditioned regularizer where an initial $\varepsilon$ perturbation is quickly amplified to $\min\{\text{polylog}^{-1}(1/\varepsilon), \varepsilon e^{\Omega(\eta T)}\}$ after $T$ iterations of MD with step size $\eta$. For canonical KL-regularized MD on the simplex, we show that even linear objectives can amplify an initial $\varepsilon$ perturbation exponentially fast in high-dimensional or near-boundary regimes. Finally, we show that adding a Bregman regularization term toward an anchor point can stabilize the dynamics while largely preserving the optimization guarantees, and that the choice of anchor is crucial: anchoring at the initialization only partially mitigates the instability, whereas anchoring at a fixed point yields a more stable mechanism.

---


### 47. [Agent Skill Evaluation and Evolution: Frameworks and Benchmarks](https://arxiv.org/abs/2606.11435)

**<font color=#1a73e8>作者：</font>** Kexin Ding, Yang Zhou, Can Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The growth of agent skills has transformed how agentic systems are built, evaluated, and deployed. As skill libraries continue to scale, rigorous evaluation becomes critical to ensuring their utility, quality, and safety in real-world applications. Consequently, the field is undergoing an emerging paradigm shift from isolated skill creation to automated, evaluation-driven skill evolution. In this survey, we systematically examine the landscape of skill evolution and evaluation beyond foundational skill creation. We categorize evolution into four distinct paradigms, spanning execution feedback, trajectory distillation, compression, and reinforcement learning, showing how each element contributes to improving skill utility and reliability. We also provide an analysis of six skill-centric benchmark categories, identifying structural gaps in benchmark coverage, trade-offs, and metric richness to advance skill research. Finally, we identify open directions for building skill ecosystems that are generalizable, efficient, and verifiably safe. The project URL is this https URL

---


### 48. [INFRAMIND: Infrastructure-Aware Multi-Agent Orchestration](https://arxiv.org/abs/2606.11440)

**<font color=#1a73e8>作者：</font>** Ahasan Kabir, Jiaqi Xue, Mengxin Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing multi-agent LLM orchestration methods, ranging from brute-force ensembles to learned routers, select models and topologies based on task and model features. However, these methods do not consider the runtime state of the serving infrastructure. On shared GPU clusters under concurrent load, this infrastructure blindness causes systematic resource underutilization: preferred models accumulate deep request queues while equally capable alternatives sit idle. In multi-agent pipelines, where each query triggers multiple sequential model calls, these delays then compound across every downstream step. Closing this gap is challenging because the relevant infrastructure signals (queue depths, KV-cache pressure, latencies) are dynamic and noisy, and they must drive three different decisions: planning, per-step routing, and scheduling. We introduce INFRAMIND, a framework that makes the entire multi-agent stack infrastructure-aware. An infra-aware planner conditions topology and role selection on real-time system load and remaining budget, biasing toward simpler graphs under congestion and richer ones at low load. An infra-aware executor then observes per-model queue depths, cache utilization, and response latencies at each agent step to decide which model to call and how deeply to reason; a budget-aware scheduler further reorders each model's queue so that urgent requests are served first. Cast as a hierarchical constrained MDP and solved end-to-end via reinforcement learning, the system learns to balance quality against latency automatically. Across five benchmarks, INFRAMIND delivers up to +7.6 pp accuracy over the prior baseline at low load with up to 7x lower latency, and sustains up to 99.9% SLO compliance under high load where every baseline drops below 50%.

---


### 49. [3D-CBM: A Framework for Concept-Based Interpretability in Generative 3D Modeling](https://arxiv.org/abs/2606.11446)

**<font color=#1a73e8>作者：</font>** Ahmad Al-Kabbany  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This research introduces a framework for incorporating Concept Bottleneck Models (CBMs) into 3D generative architectures to address the inherent 'semantic gap' in deep geometric learning. As deep models become central to 3D content creation, explainability shifts from a peripheral feature to a fundamental requirement for trust and accountability in safety-critical domains such as healthcare and manufacturing. CBMs provide an intrinsic interpretability solution by constraining latent representations to align with human-defined concepts, yet their application to unstructured 3D data remains largely unexplored.
We design, implement, and validate a formal 3D-CBM architecture that maps raw geometric inputs, including point clouds and meshes, into a multi-tiered taxonomy of interpretable primitives and functional attributes. The framework further identifies strategic datasets, such as PartNet and ShapeNet, specialized for concept-based supervision. Experimental results from a 3D part-manipulation proof-of-concept experiment demonstrate the framework's efficacy, achieving a concept prediction accuracy of 88.8\% and a Chamfer Distance of 0.0115. Critically, the model enables precise test-time intervention, allowing for the interactive correction of structural errors. This work establishes a foundation for semantically-steerable 3D generation and invites further exploration into collaborative human-in-the-loop design systems.

---


### 50. [AI Coding Agents Can Reproduce Social Science Findings](https://arxiv.org/abs/2606.11447)

**<font color=#1a73e8>作者：</font>** Meysam Alizadeh, Mohsen Mosleh, Fabrizio Gilardi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent anecdotal evidence suggests that AI coding agents can reproduce published findings when provided with original data and code; yet systematic evaluation across social sciences remains limited. Existing evaluation benchmarks are insufficient, either small or conflate agent performance with problems in the reproduction materials themselves, such as code that fails to execute correctly. Here we introduce SocSci-Repro-Bench, a benchmark of 221 tasks spanning four disciplines and 13 substantive domains, constructed from studies whose results are either fully reproducible with available materials or demonstrably non-reproducible due to missing data, allowing us to isolate agents' reproduction capacity. Evaluating two frontier coding agents, Claude Code and Codex, we find that both can reproduce a large share of social science findings, with Claude Code substantially outperforming Codex. These reproduction rates considerably exceed those previously reported for general-purpose LLM-based agents on comparable reproducibility benchmarks. Both agents also perform strongly on a reasoning task requiring identification of underlying research questions, and additional analyses suggest that results are not primarily driven by memorization. Providing the original paper PDF alongside replication materials modestly improves performance but introduces bias on tasks where reproduction is impossible. We also show that agents can be nudged toward confirmatory specification search through subtle prompt framing. Together, these findings suggest that at least some frontier coding agents can serve as reliable executors of computational workflows while underscoring the need for careful benchmarking and prompt design as AI systems assume larger roles in scientific production.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-248](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
