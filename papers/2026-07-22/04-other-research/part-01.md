# 📦 其他研究 | 2026年07月22日

> 本类共 **386** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-386](./part-08.md)

---

### 1. [Reinforcement Learning-Guided NSGA-II Enhanced with Gray Relational Coefficient for Multi-Objective Optimization: Application to NASDAQ Portfolio Optimization](https://arxiv.org/abs/2607.16194)

**<font color=#1a73e8>作者：</font>** Zhiyuan Wang, Qinxu Ding, Ding Ding 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In modern financial markets, decision-makers increasingly rely on quantitative methods to navigate complex trade-offs among multiple, often conflicting objectives. This paper addresses constrained multi-objective optimization (MOO) with an application to portfolio optimization for minimizing risk and maximizing return. To address existing gaps, we propose a novel reinforcement learning (RL)-guided non-dominated sorting genetic algorithm II (NSGA-II) enhanced with gray relational coefficients (GRC), termed RL-NSGA-II-GRC, which combines an RL agent controller and GRC-based selection to improve convergence and diversity of Pareto fronts. The agent adapts evolutionary parameters online using metrics of hypervolume, feasibility, and diversity, while the GRC tournament operator ranks parents via a unified score considering dominance rank, crowding distance, and proximity to ideal reference. We evaluate the framework on the Kursawe and CONSTR benchmarks and a NASDAQ portfolio application. On the benchmarks, RL-NSGA-II-GRC achieves convergence improvements of about 5.8% and 4.4% over NSGA-II, while preserving well-distributed non-dominated solutions. In the portfolio application, it produces a smooth, densely populated efficient frontier supporting identification of the maximum Sharpe ratio portfolio (annualized Sharpe =1.92) and utility-optimal portfolios for different risk-aversion levels. The main contributions are three-fold: 1) we propose an RL-NSGA-II-GRC method integrating an RL agent into the evolutionary framework to adaptively control parameters via generational feedback; 2) we design a GRC-enhanced binary tournament operator providing a comprehensive indicator to guide the search toward the Pareto front; 3) we demonstrate, on benchmark MOO and a NASDAQ case study, that the method delivers improved convergence and well-populated frontiers supporting actionable insights.

---


### 2. [Design and Validation of a Lightweight 1D CNN for Affective Touch Classification in Soft Plush Companions](https://arxiv.org/abs/2607.16196)

**<font color=#1a73e8>作者：</font>** Aleksandrs Vališevskis, Aleksandrs Okss, Inese Tīģere 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Soft, sensorized companions offer a physically safe and emotionally intuitive interface for socially assistive technologies, yet their deformability and multichannel tactile sensing complicate the robust interpretation of human affect. This study presents a complete open-source MATLAB-based framework for the development and validation of compact deep learning models for affective touch recognition in soft interactive companions. As a primary contribution, a diverse FAIR-compliant dataset of 1326 labelled gesture sequences collected from 25 participants spanning children, teenagers, and adults is made publicly available, providing a reusable resource for future research in affective touch recognition. Through systematic architecture and hyperparameter exploration across 468 CNN models, the study identifies compact dilated one-dimensional convolutional neural networks (1D CNNs) as the most effective solution, with a 13.2k-parameter model achieving 75% test accuracy and 85% mean leave-one-subject-out cross-validation accuracy. Theoretical inference-time analysis shows that quantized deployment requires 3.2 MMAC per window, compatible with 20 Hz real-time operation on the target microcontroller. PC-based real-time simulation with the physical toy streaming sensor data demonstrates that the CNN resolves subtle social touches that the previous heuristic system failed to detect, whereas high-force negative interactions are captured more reliably by trivial threshold-based logic. The resulting hybrid inference pipeline - instantaneous heuristic filtering followed by CNN-based nuanced gesture classification - is proposed as the embedded deployment strategy. The study demonstrates that emotionally meaningful, privacy-preserving touch interpretation is computationally feasible for direct embedding within soft therapeutic companions, with hardware integration addressed in a forthcoming study.

---


### 3. [A Survey on GNN-based Link Prediction: Techniques, Applications, and Challenges](https://arxiv.org/abs/2607.16198)

**<font color=#1a73e8>作者：</font>** Chengcheng Sun, Yajie Song, Cheng Zhai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) have emerged as the leading paradigm for link prediction, enabling the inference of missing connections and the anticipation of potential future links. However, existing reviews lack systematic exploration specifically targeting underlying GNN architectures and diverse graph structures. To address this critical gap, this paper provides a comprehensive review of GNN-based link prediction from a novel and dedicated GNN perspective. We propose an innovative taxonomy that categorizes recent advancements based on techniques and applications. From a technique perspective, we focus on key GNN encoder architectures, including GCN-based, GAE-based, GAT-based, and GFormer-based methods, discussing their strengths and limitations. From an application perspective, we highlight prominent use cases of link prediction in knowledge graphs and recommendation systems, demonstrating their real-world impact. In addition, we examine the current challenges and discuss promising future directions.

---


### 4. [Deterministic Replay for AI Agent Systems](https://arxiv.org/abs/2607.16200)

**<font color=#1a73e8>作者：</font>** Rasheed Mudasiru  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agent systems that couple large language models (LLMs) with external tools and APIs are inherently non-deterministic: LLM sampling variance, external API state, CDN infrastructure headers, and execution-environment noise collectively prevent any prior agent run from being faithfully re-executed. Existing observability platforms capture execution logs but cannot reproduce a run in isolation. We present agrepl, a developer-first CLI framework for deterministic replay of agent executions. agrepl intercepts all external interactions at the transport layer via a man-in-the-middle (MITM) proxy, serialises them as structured execution traces, and replays them in a strictly isolated environment with zero outbound network access. We formalise the agent execution model, define the request-key matching function K(s), and prove the determinism invariant. We introduce a noise-aware diff algorithm classifying HTTP header divergence into signal and noise tiers. Empirical evaluation across five workloads (n = 250 replay instances) demonstrates replay fidelity F = 1.0 and a median per-step latency reduction of 98.3%. agrepl is implemented in Go, ships as a single static binary, and is released under the MIT licence.
Keywords: AI agents, deterministic replay, LLM debugging, reproducibility, MITM proxy, execution tracing, record/replay systems.

---


### 5. [It Takes 8 Tokens: Weak-to-Strong Off-Policy RL via Auxiliary Branches](https://arxiv.org/abs/2607.16205)

**<font color=#1a73e8>作者：</font>** Dayu Wang, Jiaye Yang, Weikang Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards has emerged as a standard approach for enhancing reasoning in large language models, which typically optimizes the policy by contrasting multiple self generated rollouts. However, we identify a critical support limited bottleneck in this paradigm: on challenging reasoning tasks, the target model's samples often exhibit semantic redundancy, converging into the same erroneous "reasoning basins" that offer negligible reward contrast for policy updates. In this paper, we propose to overcome this limitation through a weak to strong learning paradigm, where a policy's exploration is informed by a weaker but computationally efficient auxiliary model. We introduce W2SPO, an off policy RL method that injects short auxiliary segments often as brief as 8 tokens into intermediate target model trajectories and the target model then completes the reasoning path from these diverted states. Policy updates are restricted to these short inserted segments based on final verifiable rewards. Empirically, W2SPO achieves superior performance among evaluated 4B scale models on mathematical reasoning benchmarks, outperforming evaluated post trained baselines. Compared with vanilla GRPO under the same sampling budget, W2SPO improves Pass@1 from 62.3% to 64.2% while achieving a 3.55 times training speedup. These results suggest that weak auxiliary branches can induce stronger target reasoning policies by expanding local exploration support.

---


### 6. [Shapley Context Pruning: A Cooperative Game Perspective for Context Reranking and Pruning](https://arxiv.org/abs/2607.16209)

**<font color=#1a73e8>作者：</font>** Yanqiao Chen, Dongsheng Hou, Yuhan Rui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Context reranking and pruning have become essential for improving the efficiency of modern Retrieval-Augmented Generation (RAG) systems, yet an interpretable and unified framework remains underexplored. Previous work has primarily emphasized lexical retrieval, cross-encoder architectures, model distillation, and Low-Rank Adaptation (LoRA), mostly relying on heuristic loss functions and empirical attribution. This paper presents Shapley Context Pruning (SCP), a novel framework for context reranking that establishes a cooperative-game-theory perspective for importance attribution by modeling the context as a cooperative game. Balancing the trade-off between fine-grained and coarse-grained representations, we employ a Deep Sets architecture to approximate a permutation-invariant value function at the sentence level, utilizing pre-trained language models as sentence embedders and optimizing via a pairwise margin ranking loss. To ensure practical scalability without sacrificing mathematical rigor, we leverage Monte-Carlo sampling for efficient training and inference, providing formal theoretical error bounds and sample complexity guarantees for preserving Top-K subset rankings. Furthermore, we conduct comprehensive experiments-spanning supporting-sentence recall, Needle-in-the-Haystack (NIAH) evaluations, long-context QA, and multi-hop reasoning-alongside rigorous ablation studies on embedding quality and attribution strategies. The model achieves competitive downstream QA performance against robust baselines.

---


### 7. [A Survey on the Verification of Reinforcement Learning Policies](https://arxiv.org/abs/2607.16210)

**<font color=#1a73e8>作者：</font>** Luca Marzari, Ezio Bartocci, Enrico Marchesini  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) is increasingly applied in complex, safety-critical domains, yet the lack of rigorous behavioral guarantees for neural network-based policies remains a major barrier to deployment. Recent advances in policy expressiveness and scale have intensified this challenge, leading to a rapidly growing but conceptually fragmented body of work on RL policy verification. This survey provides a unifying perspective on RL verification methods. We introduce a taxonomy that clarifies relationships among existing approaches along three axes: verification paradigm (formal versus probabilistic), temporal scope (step-wise versus multi-step), and guarantees strength. Beyond taxonomy, we unify underlying theoretical foundations, make implicit assumptions and limitations explicit, and identify emerging directions.

---


### 8. [Symbolic Augmentation Closes a Canonical-Equivalence Blind Spot in Neural Fact-Checkers](https://arxiv.org/abs/2607.16212)

**<font color=#1a73e8>作者：</font>** Genpei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models hallucinate numbers and units when summarizing scientific text, a failure mode that can silently invert a scientific claim. We recast the detection of such errors as typed verification: we introduce a five-class typed-quantity error taxonomy and a 1500-item benchmark, rewritten from PMC and arXiv sources and labeled by two independent LLM annotators with adjudication (Krippendorff's alpha = 0.882). A ModernBERT encoder fine-tuned on this benchmark reaches macro-F1 = 0.899, far above any off-the-shelf neural fact-checker, yet four probes expose a sharp structural blind spot: on canonical-equivalent rewrites of physically equivalent quantities (e.g., 95°C and 368.15 K) its accuracy collapses to 36.5%. We propose Symbolic Augmentation, a training-time framework that runs the modules of a symbolic verifier in reverse to generate label-preserving augmented training data. The augmentation lifts canonical-equivalence robustness to 98.2% while slightly improving in-distribution accuracy (macro-F1: 0.899 to 0.902); the augmented encoder matches a closed-frontier LLM at no inference cost and transfers to an external benchmark (SciFact-Open binary macro-F1: 0.791 to 0.828). Two negative results sharpen the claim: symbolic features as auxiliary encoder inputs add nothing, and symbolic silver labels scale negatively under teacher noise. Together these results identify training-time augmentation as the right integration point between symbolic and learned components.

---


### 9. [SelKV: Selective KV Cache Merging with Per-Token Merge-or-Drop and Attention Compensation](https://arxiv.org/abs/2607.16213)

**<font color=#1a73e8>作者：</font>** Soumia Bouyahiaoui, Manel Kara laouar, Aicha Boutorh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) generate text autoregressively, relying on a key-value (KV) cache whose memory footprint grows linearly with context length, creating a major bottleneck. Recent compression methods mitigate this cost via token merging; however, these approaches often rely on indiscriminate aggregation, which degrades representations and introduces attention sag, a mismatch where merged tokens receive the same softmax mass as individual tokens despite encoding multiple inputs. We propose a training-free, dual-component framework for KV cache compression that addresses these limitations. First, a soft cosine gate adaptively modulates merging decisions based on value-vector similarity, suppressing or discarding dissimilar tokens to preserve semantic fidelity. Second, we introduce an attention-ratio compensation mechanism that applies a decoding-time logit bias derived from prefill attention statistics, correcting the softmax imbalance induced by merging. Evaluated on LongBench (16 English datasets) while retaining only 25% of the KV cache, our framework achieves strong compressed performance against representative one-shot baselines. It is especially robust on the evaluated grouped-query attention (GQA) models, maintaining nearlossless generation quality. Furthermore, the method outperforms the full-cache baseline on complex multi-document QA tasks and delivers a 3.3x decoding speedup at 100k tokens.

---


### 10. [What Makes Linguistic Representations Good Models of High-Level Visual Perception in the Human Brain?](https://arxiv.org/abs/2607.16214)

**<font color=#1a73e8>作者：</font>** Anna Bavaresco, Ina Klarić, Raquel Fernández 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image descriptions represented with language models (LMs) predict human brain responses to naturalistic images in high-level visual regions, but the factors driving this predictivity remain unclear. To investigate this, we systematically studied how images are described and which language models are used to embed those descriptions. For a common set of images, we considered six caption types -- including human-annotated and multiple machine-generated captions -- differing along several dimensions. Each caption was represented with five LMs, spanning autoregressive LMs trained to predict upcoming words and text embedders, i.e., LMs fine-tuned on semantic tasks requiring sentence/document-level representations. Machine-generated captions yielded significant brain predictivity and alignment, often surpassing human-annotated captions used in previous work. Across caption types, text embedders consistently outperformed autoregressive LMs, a pattern replicated when measuring behavioural alignment with image-similarity judgments. Analyses of caption representations from different model layers further revealed that both brain predictivity and behavioural alignment peak at intermediate network depth, shortly after a point thought to mark the emergence of syntactic and semantic structure. Altogether, our results demonstrate that both the content of image captions and the LM used to represent them influence brain- and behaviour-modelling performance, establishing caption embeddings as a useful tool for studying high-level visual perception.

---


### 11. [Fully-sensorized smart-eyewear platform for on-device Machine Learning](https://arxiv.org/abs/2607.16222)

**<font color=#1a73e8>作者：</font>** Andrea Giudici, Christian Veronesi, Pietro Bartoli 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents ARGO, a smart eyewear platform designed to bridge ergonomic comfort, high computational throughput, and energy efficiency. Unlike cloud-dependent solutions, ARGO leverages the STM32N6 microcontroller and its integrated Neural Processing Unit (NPU) to enable on-device machine learning, minimizing latency and preserving user privacy through local data processing. The primary contribution lies in the holistic co-design of hardware, firmware, and artificial intelligence, centered on the deployment of an optimized YOLOv11 model for real-time urban obstacle recognition. To ensure compatibility with the target NPU, we introduce Head-wise Parallel Attention (HPA), an architectural refinement that enables efficient accelerator execution while preserving the original computational logic. The model is trained on the Walking On The Road (WOTR) dataset, and the final deployed configuration achieves an mAP50-95 of 24 under strict memory constraints, with a memory footprint of only 2.483 MB. The platform integrates a multimodal sensor suite, RGB cameras, Time-of-Flight sensors, microphones, and ambient sensors, and delivers 10 FPS at a continuous autonomy of ~113 minutes on a 200 mAh battery. These results demonstrate the feasibility of a high-performance, privacy-preserving, and socially acceptable assistive device, and highlight how competitive edge AI solutions increasingly demand tightly integrated, multidisciplinary co-design approaches.

---


### 12. [Operator-Aware Mixed-Precision Tolerance Calibration for Tensor Kernels](https://arxiv.org/abs/2607.16228)

**<font color=#1a73e8>作者：</font>** Dipankar Sarkar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most tensor-kernel correctness tests go through a fixed-shape all close-style check with hand-picked absolute and relative tolerances. The thresholds are copied across the corpus and rarely revisited. We mine the element-wise error distribution of every test case from accumulated cloud GPU runs across the 26-entry gpuemu corpus and 2 dtypes (8,076 result rows). We then ask one empirical question: what absolute tolerance would the kernel itself, observed under its correct implementation, justify?
The answer is much tighter than the current hand-picked atol. The largest tightening is attention_triton fp16 at $2{,}184\times$. Restricted to the seven LLM-style buggy variants for which the corpus ships a paired correct counterpart, calibrated per-(op, dtype) tolerances raise bug-detection recall from 73.2% (1,805 of 2,467) to 82.4% (2,034 of 2,467), an absolute gain of 9.3 percentage points (+229 new detections). The control false-positive count rises from 0 to 20 out of 1,882 correct-control cases (+1.1 percentage points).

---


### 13. [RouteCost: A Production-Inspired Multi-Stage Framework for Pre-Order Shipping Cost Estimation in E-Commerce](https://arxiv.org/abs/2607.16230)

**<font color=#1a73e8>作者：</font>** Xianling Zeng, Zihan Yu, Sichen Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate pre-order shipping cost estimation is important in e-commerce because it affects price presentation, margin planning, and conversion. In practice, shipping cost is shaped not only by distance but also by destination demand mix, billable weight, dimensional pricing, surcharge triggers, and latent operational effects such as shipment consolidation. Static lookup methods therefore miss important sources of variation, while monolithic regressors may exploit strong but non-causal correlations. We propose RouteCost, a production-inspired multi-stage framework that decomposes the problem into time-aware demand forecasting, fee-card-informed baseline pricing, Stage 2 residual correction, and proxy-based box-consolidation inference. Route-level cost estimates are aggregated through a route-weighted expectation formulation to produce product-level shipping cost predictions. Across over 250,000 orders, 260 products, and 18 months of order history, the framework improves predictive quality and aggregate calibration while preserving route-level interpretability.

---


### 14. [Orthogonal Gradient Constraints Shape Noisy-Label Memorization Dynamics](https://arxiv.org/abs/2607.16231)

**<font color=#1a73e8>作者：</font>** Richard Mai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern neural networks can fit corrupted training labels, making noisy-label learning a useful setting for studying memorization-driven overfitting. Most regularization methods modify the objective, architecture, or data distribution; here we instead study a geometric intervention on the optimizer update itself. We evaluate OrthoGrad, which removes the component of each weight gradient parallel to the current weight vector, in noisy-label image classification. On MNIST with small-data regimes, OrthoGrad improves test accuracy most clearly for CNNs while reducing corrupted-label fitting. Mechanism diagnostics based on weight norms and gradient-weight cosine similarity suggest that the projection has the strongest effect when the raw gradient contains a nontrivial radial component, and becomes weaker in larger-data regimes where gradients are already nearly orthogonal to weights. Additional CIFAR-10 ResNet-18 experiments show that the method can alter memorization trajectories but does not prevent eventual noisy-label memorization. These results support orthogonal update constraints as a useful diagnostic for studying learning dynamics, while showing that OrthoGrad is regime-dependent rather than universally regularizing.

---


### 15. [From Weights to Words: Expressing and Editing Preference Model Inferences in Natural Language](https://arxiv.org/abs/2607.16232)

**<font color=#1a73e8>作者：</font>** Zachary Wojtowicz, Ayush Nayak, Jacob Andreas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The growing use of statistical learning algorithms to infer human preferences from high-dimensional choice data runs up against a fundamental challenge: choice alternatives typically differ in many ways simultaneously, so it is generally unclear which factors actually drove an observed decision and should be credited as preferences. Compounding this problem, the opacity of these methods leaves human operators unable to inspect, contest, or correct models when they err. We introduce \emph{weights to words}, a method that takes a dataset of choice problems as input and automatically discovers a collection of domain-relevant preference dimensions, each described in natural language and paired with a vector in the model's representational space. These dimensions address both under-determination and opacity: they can be applied to concentrate attribution on a small set of meaningful factors, and they can externalize the model's inferences in natural language so that users can inspect and edit them in real time. We first qualitatively illustrate the method's versatility on four diverse domains: moral dilemmas, movies, wines, and free-form LLM responses. We then report two pre-registered human-subjects experiments, on moral dilemmas ($N=450$) and movie selection ($N=449$), that demonstrate its benefits for learning preference models: (1) regularizing a preference model toward the learned basis increases prediction accuracy on held-out choices, and (2) incorporating participants' structured edits further improves accuracy. In head-to-head comparisons, participants prefer the method's inferred preference profiles and endorse its predictions as more accurate.

---


### 16. [Token-Level Cross-Modal Transformer with Contrastive Multi-Task Learning for Breast Cancer Subtype Classification and Survival Prediction](https://arxiv.org/abs/2607.16233)

**<font color=#1a73e8>作者：</font>** Suxing Liu Byungwon Min  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Integrating heterogeneous genomic and clinical modalities for joint cancer subtype classification and survival prediction remains a key challenge in precision oncology. Existing approaches suffer from three limitations: (1) they treat each modality as a monolithic feature vector, precluding fine-grained token-level interactions across modalities; (2) cross-modal fusion is typically performed through linear weighting or late averaging rather than structured token exchange; and (3) survival and classification objectives are optimized independently, missing a joint regularization signal.

---


### 17. [HantaWatch: Federated Learning for Hantavirus Genomic Surveillance](https://arxiv.org/abs/2607.16234)

**<font color=#1a73e8>作者：</font>** Shanika Iroshi Nanayakkara, Shiva Raj Pokhrel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hantavirus genomic surveillance is limited by the distribution of sequence data, non-IID source heterogeneity, and constrained expert-review capacity. We propose HantaWatch, a federated learning framework that enables laboratories and surveillance sites to collaboratively train sequence-based models without sharing raw data. HantaWatch integrates k-mer feature extraction, source-aware federated client construction, adaptive DU-FedProx optimization, surveillance-specific model selection, and prediction-only triage. Experiments on binary and multi-class tasks show that HantaWatch supports high-risk screening, outbreak-associated prediction, clade classification, and clinical-syndrome categorization while balancing predictive performance, false-negative risk, and update stability. The framework converts model output into risk scores, confidence estimates, uncertainty flags, and ranked expert-review priorities. HantaWatch therefore provides a practical federated decision-support layer for decentralized Hantavirus surveillance, supporting expert prioritization without replacing laboratory or public-health interpretation.

---


### 18. [The Failures of Marginal Influence-Based Attribution Methods for Global Time Series Explanations](https://arxiv.org/abs/2607.16236)

**<font color=#1a73e8>作者：</font>** Amadeo Tunyi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Explainability methods for time series models predominantly produce flat attribution scores: they quantify the direct influence of a feature at a timestamp by a scalar. We prove that the dominant failure mode of such methods is not the scalar format itself but a fundamental computational mismatch: existing methods compute scores via marginal conditioning or off-manifold gradients, both of which conflate direct temporal dependencies with mediated ones under autocorrelation. We also define DAG-faithfulness: an explanation is DAG-faithful if the temporal dependency graph it encodes is Markov-equivalent to the temporal directed acyclic graph (DAG) implicitly learned by the model. Particularly, we observe that standard attribution methods, specifically SHAP, are not DAG-faithful in general, and that recent time-series-aware extensions inherit the same computational limitation.

---


### 19. [Diffusion-corrected Autoregressive Fourier Neural Operator for Droplet Evolution Prediction](https://arxiv.org/abs/2607.16238)

**<font color=#1a73e8>作者：</font>** Jinghao Cao, Minsung Kang, Hongyue Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting droplet evolution in material jetting, or Inkjet Printing (IJP), is essential for maintaining printing quality. However, long-horizon forecasts remain challenging due to error accumulation and the complex coupling of process variables. In this work, we introduce the Diffusion-corrected Auto-Regressive Fourier Neural Operator (DiffARFNO), a two-stage framework that combines an autoregressive Fourier-MIONet with a conditional Denoising Diffusion Implicit Model (DDIM) corrector. Fourier-MIONet is trained as a coarse predictor and deployed autoregressively for long-horizon forecasting. In the second stage, a DDIM-based conditional corrector refines the coarse prediction within each sliding window through efficient iterative denoising. By combining coarse predictions from Fourier-MIONet with a DDIM corrector that restores fine details, DiffARFNO aims to provide high-fidelity predictions for long-horizon forecasts. Extensive experiments on droplet datasets from ANSYS Fluent demonstrate that DiffARFNO significantly outperforms existing state-of-the-art models.

---


### 20. [BACON: Budgeted Human Calibration for Modeling and Evaluation with Multiple AI Judges](https://arxiv.org/abs/2607.16239)

**<font color=#1a73e8>作者：</font>** Lei Shi, Anlan Zhang, Rita Lyu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI judges offer a scalable, low-cost alternative to human evaluation, but their outputs can be biased relative to human preferences and highly item-dependent, varying across judges, tasks, and domains. When uncalibrated AI evaluations are used for model ranking, item scoring, or population-level quality reporting, these biases can directly distort downstream decisions. We propose BACON, a four-stage pipeline that combines budgeted human calibration with multiple AI-judge outputs to produce more accurate annotations. BACON constructs full-coverage auxiliary features for every item, including multi-judge scores, token-level uncertainty statistics, and contextual embeddings. It then collects human labels for a small sampled subset and trains a cross-fitted outcome model to generate calibrated item-level surrogate predictions. These predictions support two use cases: population-level estimation of summary metrics, such as means or quantiles, using an augmented estimating-equation estimator with valid confidence intervals; and individual-level surrogate scoring for item ranking and annotation. BACON treats AI judges as auxiliary measurements rather than ground truth: human labels provide the calibration anchor, while AI-derived signals improve efficiency. Across diverse tasks, domains, and labeling budgets, BACON improves predictive accuracy and ranking consistency, and reduces bias and variance relative to raw AI outputs and purely human-label-based methods. These results show that BACON offers a practical, statistically grounded framework for scalable evaluation with limited human annotation.

---


### 21. [Normalized Rewards for Preference Optimization](https://arxiv.org/abs/2607.16240)

**<font color=#1a73e8>作者：</font>** Shawn Im, Federico Danieli, Skyler Seto 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Direct Alignment Algorithms (DAAs) such as DPO have become a common way to post-train and align LLMs with human preferences. However, DAAs have been observed to over-optimize their implicit reward model and decrease the likelihood of preferred responses. This results in a decrease in the total likelihood assigned to responses seen in the preference dataset, potentially resulting in undesirable behavior. To counteract this undesired side-effect of DAAs, we examine the effect of using objectives that add a regularization term to maintain the total length-normalized probabilities of the chosen and rejected responses. To better understand over-optimization, we investigate how response likelihood changes are distributed over the tokens with and without regularization. We find that a significant portion of the likelihood changes are due to a small set of outlier tokens, which explains how DAAs improve generation quality despite decreasing the likelihoods of chosen responses. We apply the proposed regularization to reference-based (DPO) and reference-free (SimPO) methods and find (1) improved trade-offs between generation quality and general benchmark capability and (2) improvements in reward modeling across datasets. For example, on Llama-3.1-8B-Instruct, we see both a >20% relative increase in AlpacaEval2 scores and >9% relative performance gains on general benchmarks. Additionally, we find that the added regularization term effectively mitigates the amount of displacement within preferred responses overall, and for the outlier tokens specifically, by utilizing low-likelihood tokens.

---


### 22. [Learning Structural Manipulability in Gate-Level Netlists Using Graph Neural Networks](https://arxiv.org/abs/2607.16245)

**<font color=#1a73e8>作者：</font>** Rupesh Raj Karn, Ozgur Sinanoglu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gate-level netlists exhibit intrinsic structural properties that influence signal propagation independently of functional simulation. We define a topology-driven structural manipulability score that characterizes node-level structural flexibility using path participation, k-core embedding, symmetry, and centrality. Modeling netlists as directed graphs, we formulate node-level regression to learn this topology-derived score using graph neural networks (GNNs). Experiments on ISCAS85 and EPFL benchmarks evaluate how effectively different GNN architectures approximate this metric across held-out circuits, with hierarchical models yielding the most consistent rankings. Component-level and ablation analyses examine the contribution of individual factors. As an illustrative case study, analysis of Trojan-injected circuits using TrustHub templates reveals statistically distinguishable structural patterns, indicating that topology-based scoring provides complementary structural insight.

---


### 23. [Self-Evolving Just-In-Time Memory for Proactive Embodied Safety](https://arxiv.org/abs/2607.16247)

**<font color=#1a73e8>作者：</font>** Bingrui Sima, Lizhong Wang, Xiaoya Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While Vision-Language Models (VLMs) have empowered embodied agents to execute complex household tasks, they struggle to proactively handle dynamically emerging hazards during closed-loop interactions. Existing safety approaches often rely on runtime guardrails to block unsafe actions or induce excessive caution, which severely stalls task progress instead of actively resolving the underlying risks. To break this safety-progress trade-off, we introduce the Self-Evolving Just-In-Time Memory framework, which reframes embodied safety from progress-stalling guardrails to proactive hazard mitigation. The framework consists of a Risk-Sufficient Topological Belief Graph (RSG) for persistent safety-relevant state tracking under partial observability, an Agency-Grounded Factual Memory for precise hazard anticipation, and an Experience Memory that injects procedural Meta-Skills to guide executable, progress-preserving mitigation. Furthermore, we propose an automated Test-Verify-Write loop, allowing agents to continually refine their mitigation Meta-Skills from execution traces at test time. Experiments on IS-Bench demonstrate that our framework substantially boosts the Safe-Success rate across multiple VLM backbones (e.g., +30.3% on Qwen3-VL-8B), enabling agents to proactively mitigate hazards without stalling task progress. Code is available at this https URL.

---


### 24. [Benchmarking Machine Learning Models for Multi-Omics-Based Breast Cancer Prediction](https://arxiv.org/abs/2607.16250)

**<font color=#1a73e8>作者：</font>** Priyanka Paudel, Madan Baduwal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estrogen Receptor (ER) status is a critical biomarker in breast cancer diagnosis, prognosis, and treatment selection. Recent advances in high-throughput sequencing technologies have enabled the generation of multi-omics datasets that provide complementary molecular information for computational prediction tasks. This study presents a systematic benchmarking analysis of classical machine learning models for ER status prediction using transcriptomic (RNA expression), genomic (copy number variation; CNV), and proteomic (RPPA) data from the TCGA-BRCA cohort. A rigorous experimental framework incorporating stratified train-test splitting, stratified five-fold cross-validation, class imbalance handling, and fold-specific feature selection was employed to ensure reliable evaluation and prevent data leakage. Random Forest, XGBoost, LightGBM, CatBoost, Support Vector Machines (SVM), and Logistic Regression were evaluated across single-omic and multi-omic settings. Results demonstrated that RNA expression provided the strongest predictive signal, while multi-omic integration yielded modest but consistent improvements over individual modalities. Among all evaluated approaches, Random Forest achieved the best overall performance in the integrated multi-omic setting, obtaining a balanced accuracy of 90.3\% and an ROC-AUC of 97.1\%. Furthermore, recurrent selection of biologically relevant genes, including \textit{ESR1}, \textit{PGR}, \textit{FOXA1}, and \textit{GATA3}, supported the biological validity of the learned models. These findings indicate that carefully regularized classical machine learning methods remain highly effective for small, high-dimensional genomic datasets and that multi-omic integration provides complementary information for breast cancer ER status prediction.

---


### 25. [Comprehensive Evaluation of Machine Learning for Type 2 Diabetes Risk Prediction: Large-Scale External Validation and Fairness Analysis](https://arxiv.org/abs/2607.16253)

**<font color=#1a73e8>作者：</font>** Rajveer Singh Pall, Sameer Yadav, Siddharth Bhalerao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning-based Type 2 diabetes risk prediction models obtain good internal validation results but lose effectiveness in real-world applications due to deficient external testing and fairness assessment. We developed a multi-dimensional framework evaluating discrimination, calibration, interpretability, and algorithmic fairness on nationally representative populations. An XGBoost model was trained on NHANES 2015-2020 (n=15,685) using eight non-laboratory predictors: age, sex, race/ethnicity, BMI, smoking status, physical activity, history of heart attack, and history of stroke. External validation was performed on BRFSS 2020-2022 (n=1,285,783) under realistic distribution shift. Internal validation showed good discrimination (AUC=0.794, 95% CI 0.788-0.800), with performance loss on external validation (AUC=0.717, relative decrease: -9.7%, p<0.001). Fairness analysis revealed severe bias: elderly adults (>=60) showed AUC=0.607 vs 0.742 for young adults (difference=0.135, p<0.001); obese individuals showed AUC=0.698 vs 0.735 for normal weight (difference=0.037, p<0.001). Gender showed comparable performance (male=0.723 vs female=0.712, p=0.142). Calibration revealed risk overestimation (Brier score=0.123). SHAP analysis identified age, BMI, and physical activity as primary risk drivers. Populations with highest diabetes risk receive the worst algorithmic performance, underscoring the need for fairness-aware, age-stratified deployment strategies before clinical use.

---


### 26. [More Than Memory: Task-Conditioned Signed FFN Writes in Long-Context Retrieval](https://arxiv.org/abs/2607.16254)

**<font color=#1a73e8>作者：</font>** Zhibo Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> FFNs are often treated as parametric memories. In long-context retrieval, however, the sharper question is not only what they store, but whether their native residual writes push the current retrieval state toward or away from the correct answer. We test this by scaling the model's own FFN write one layer at a time, without editing weights or injecting external steering vectors.
Across controlled literal and semantic retrieval suites, native FFN response surfaces are signed, layer-specific, and task-conditioned: the final FFN is a suppressor in 7 of 8 model-suite cases, and 60% of layers switch role between retrieval modes (95% CI [50%, 69%]). A local directional derivative along the native write separates the two monotone roles: suppressors have negative derivative in 34/35 cases, and amplifiers have positive derivative in 18/18 cases, so the roles are not reducible to write size. On a safety-filtered LongBench retrieval-QA probe, the same diagnostic predicts attenuation damage with raw R^2=0.796 on Qwen2.5-7B and 0.791 on Qwen3.5-9B; a held-out suppressor-attenuation policy improves retrieval margins over random and norm-matched controls. These results show that native FFN scaling exposes a signed, task-conditioned residual-write structure in retrieval, and that write-gradient alignment is a compact diagnostic for the two monotone roles.

---


### 27. [Discovery by Dreaming: Cross-Domain Recombination in Artificial Memory](https://arxiv.org/abs/2607.16256)

**<font color=#1a73e8>作者：</font>** Oliver Zahn, James Evans, David Eagleman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dreams splice together people, places, and times that never met. Neuroscience suggests this recombination is not noise, but a function driving insight and creative discovery. This reframes memory consolidation: rather than merely defending against forgetting, its measurable value lies in recombining knowledge across experiences that have not yet co-occurred. We test this directly by isolating the recombinatory-replay mechanism and implementing it in two architecturally unrelated systems: a LoRA fine-tuning pipeline (DREAMS) and a symbolic engine replaying structured knowledge objects (SAPIENCE). Both systems converge on the same finding: cross-domain consolidation creates value, while within-domain rehearsal does not. The symbolic arm surfaces novel cross-domain connections at 85.7%, a +21 percentage point (pp) gain over baseline. The neural arm improves overall by +5.64 pp, but on subtasks explicitly requiring cross-domain transfer (like unseen math reasoning on GSM8K), gains reach +14.5 pp. This effect is a genuine property of the weights--not a prompt artifact--as prepending the same material in-context to a 671B-parameter model actually reverses the gain. We validate this prediction against documented discoveries across 50,000 real papers and state a falsifiable hippocampal-recording prediction to distinguish recombination from rehearsal. Ultimately, this principle is substrate-general, tracking real discovery at scale. Reading the literature teaches a model to recall what it has seen, but producing discovery requires a separate offline phase that recombines knowledge across domains--the computational analog of dreaming. Consolidation is not for remembering, but for discovering.

---


### 28. [Neural Controlled Differential Equations for EMT-Level Surrogate Modeling of Grid-Forming Inverters](https://arxiv.org/abs/2607.16258)

**<font color=#1a73e8>作者：</font>** Jiagang Qu, Yong Tao, Dan Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The application of artificial intelligence methods in power electronic converter modeling is becoming increasingly widespread, but existing applications still face many challenges, such as difficulties in multi-time-scale hybrid analysis and the lack of physics-aware evaluation criteria and constraints, resulting in poor performance. This paper proposes a Neural Controlled Differential Equation (Neural CDE) framework for learning continuous-time surrogate models of grid-forming inverters for electromagnetic transient (EMT) simulation, which relaxes the constraint of fixed sampling rates and enables multi-time-scale control analysis. Then, an affine-control formulation with dual slow/fast pathways is proposed to capture the hierarchical and multiscale behavior of converter dynamics, and a physics-inspired regularization method is utilized to enhance stability and coherence. Evaluated on EMT-generated trajectories, the model accurately reproduces transient responses, preserves effective damping and the dominant oscillatory characteristics, and maintains bounded long-horizon rollouts. The results show that Neural CDE-based component modeling offers a physically consistent surrogate modeling approach for EMT-level simulation studies.

---


### 29. [Reducing Per-Sample Harm in Stochastic Optimization](https://arxiv.org/abs/2607.16261)

**<font color=#1a73e8>作者：</font>** Apostolos Avranas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern optimizers combine gradients from the current mini-batch with historical optimization state, such as momentum or adaptive moments. While highly effective, aggregating across the batch and incorporating this history can produce parameter updates that increase the loss of individual samples. We term this effect harm and formalize the parameter update as an optimization problem that explicitly minimizes the conflicting impact of both batch averaging and past optimization state on current data.
Because the exact formulation is intractable, we introduce a highly efficient proxy. We first reduce the problem's dimensionality to the batch size, and then drastically cut memory and speed bottlenecks by successfully restricting the optimization to the last linear layer. This hinges on the unexpected finding that this layer alone reliably captures the second-order statistics of the per-sample gradients. The resulting surrogate problem integrates readily into standard optimizers like SGD and AdamW, and can be solved using a small number of GPU-friendly iterations. Crucially, the method exhibits favorable scaling properties, as the relative computational overhead shrinks as the model size or input grows. Experiments on image classification benchmarks confirm reduced per-sample interference and improved generalization.

---


### 30. [Autonomous mechanistic discovery of colorectal cancer vulnerabilities via multi-scale AI swarms](https://arxiv.org/abs/2607.16262)

**<font color=#1a73e8>作者：</font>** Christopher Baker, Tianyu Ren, Karen Rafferty 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The acceleration of automated scientific discovery has been fundamentally bottlenecked by the epistemic gap between the semantic reasoning of large language models (LLMs) and the deterministic physics of mammalian biology. While recent multi-agent frameworks have achieved autonomous hypothesis generation and in vitro experimental analysis, they lack the mathematically grounded, causal constraints required for multi-scale clinical translation. Furthermore, while algorithmic clinical digital twins successfully forecast biological states, they rely on black-box latent spaces, sacrificing mechanistic interpretability for predictive accuracy. Here, we introduce the Multi-Scale Autonomous Discovery Engine (Octopus), a neuro-symbolic architecture that unites zero-leakage, local LLM swarms with strict algorithmic physics engines. Rather than stopping at isolated cellular assays, the system autonomously generated therapeutic hypotheses against in vitro CRISPR dependency data (CCLE), traced dynamic causal cascades using mechanistic interpretability (XGBoost SHAP vectors), and orthogonally translated the emergent vulnerabilities in silico to predict in vivo mammalian tumor trajectory (PDX) and human overall survival (Marisa). In a fully unsupervised sweep of colorectal cancer transcriptomes, the pipeline autonomously identified Insulin-like Growth Factor 2 (IGF2) as a strictly bounded vulnerability to 5-Fluorouracil resistance. The discovery maintained significance after rigorous Benjamini-Hochberg false discovery rate correction (q=0.0292, Log-Rank p=0.0007 ) and successfully predicted significant in vivo tumor volume shrinkage in an independent mouse cohort (Mann-Whitney p=0.0373). By bridging the chasm between multi-agent reasoning and mathematically bounded clinical survival, this framework establishes a verifiable, zero-leakage paradigm for automated, end-to-end biomedical discovery.

---


### 31. [Preference-based Antibody Expression Ranking: Scaling with Large-scale Weak Supervision](https://arxiv.org/abs/2607.16263)

**<font color=#1a73e8>作者：</font>** Josh Qixuan Sun, Morteza Babaie, Wenyang Hou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Antibody expression ranking is a critical task in antibody design, yet its modelling is severely hindered by the scarcity of labeled experimental data. To address this, we propose a unified preference-based learning framework that integrates scarce quantitative expression data with large-scale weak positive supervision from immunization data. We adapt Direct Preference Optimization (DPO) to protein language models by introducing a union-masked log-likelihood approximation and IMGT-based alignment, enabling efficient training on variable-length sequences. Evaluating on a diverse internal dataset of 1254 labeled sequences and 4 million unlabeled camelid-derived antibodies, we show that our method consistently outperforms baselines on most metrics. Our results demonstrate that preference learning can effectively learn from weak supervision, providing a scalable solution for antibody expressibility optimization in data-constrained settings. Project page: this https URL.

---


### 32. [PsiLogic: Chaos-Aware Active Cancellation for Adam with a Fair Cross-Domain Benchmark](https://arxiv.org/abs/2607.16268)

**<font color=#1a73e8>作者：</font>** Ali Sultonov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive optimizers such as Adam and AdamW apply the same update rule regardless of whether training is in a chaotic early phase or near convergence. We introduce PsiLogic, an optimizer that augments Adam with a dynamic Active Cancellation Term gated by a dual exponential moving average (EMA) of scale-normalized gradient norms. The resulting chaos detector strengthens damping when gradient statistics are unstable and fades to zero as training stabilizes, providing an implicit warmup without a hand-tuned schedule.
We evaluate PsiLogic against Adam, AdamW, and Lion using FairBench -- a reproducible benchmark protocol with per-optimizer learning-rate sweeps, identical initialization per seed, and Welch t-tests. On an NVIDIA H100 80GB reference run (4 arenas, 3 seeds, 2000 steps, bf16 AMP), PsiLogic achieves the best validation metric in three of four arenas: NLP perplexity 7.79 +/- 0.18 vs. 8.17 +/- 0.08 (AdamW, p = 0.049), ViT top-1 accuracy 0.244 +/- 0.006 vs. 0.223 +/- 0.002 (AdamW, p = 0.015), and ResNet top-1 accuracy 0.222 +/- 0.001 vs. 0.172 +/- 0.004 (Adam, p = 0.001). On diffusion, validation MSE is statistically tied with Adam/AdamW (p = 0.49). ResNet accuracy vs. AdamW is a numerical tie without significance at three seeds (p = 0.44). Peak GPU memory is comparable across optimizers; PsiLogic incurs 1.2--1.8x wall-clock overhead on transformer-heavy arenas (implementation-bound).
We release an open-source PyTorch implementation, the full FairBench harness, and all raw CSV outputs to support independent verification.

---


### 33. [ForensicNet: Lightweight Attention-Enhanced MobileNetV2 for Automated Face Identification](https://arxiv.org/abs/2607.16273)

**<font color=#1a73e8>作者：</font>** Savitha N J, Lata B T  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In forensic environments, automated identification of perpetrators is difficult due to pose changes, changes in light, occlusion, and lack of labeled data. This paper presents ForensicNet, a lightweight deep learning framework for forensic face recognition that enhances attention. The suggested model combines the MobileNetV2 backbone with Convolutional Block Attention Modules (CBAM) to improve the learning of discriminative features while maintaining computational speed. A two-phase transfer learning strategy with adaptive layer unfreezing is used to improve domain adaptation and reduce overfitting. This study used publicly available datasets such as LFW and SCFace, with 15,000 facial images spanning 68 identity classes. The proposed model outperforms baseline architectures such as AlexNet, ResNet-50, and MobileNetV2, with an accuracy of 92.4%, a precision of 90.8%, and a recall of 89.5%. Additionally, the framework requires only 2.1 GFLOPs per inference, and hence can be used in real-time forensic surveillance applications.

---


### 34. [The JEPA Predictor: A Transferable Operator for Occluded Feature Completion](https://arxiv.org/abs/2607.16274)

**<font color=#1a73e8>作者：</font>** William Nguyen, Christopher Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Joint-Embedding Predictive Architectures (JEPAs) train a predictor jointly with their encoder, but downstream deployment discards the predictor and reads features from the encoder alone. The predictor is, by construction, a learned operator from visible-context features to features at masked positions, the structure a partial-view classifier needs. We show that this operator is portable across encoder families. We first establish that, at heavy mask, retaining the frozen predictor on a JEPA encoder substantially closes the accuracy gap against the strongest non-JEPA discriminative baselines. We then bolt the frozen predictors of I-JEPA and V-JEPA 2 onto four non-JEPA hosts (CLIP, DINOv3, DINOv2, MAE) through a single linear projection between feature spaces, fit in closed form on 500 ImageNet-1k images. Across both ImageNet-9 and Stanford Dogs and across three mask fractions, the lift over each host's masked-encoder baseline grows monotonically with the mask fraction K in every host-donor pair. CLIP paired with the I-JEPA predictor recovers most of the accuracy that masking removed on ImageNet-9 at heavy occlusion, and lifts fine-grained Stanford Dogs from 15.9% to 52.1% (+36 pp). The mechanism is identifiable: the projection pays a fixed cost on visible patches and the predictor provides a growing benefit on masked patches; the benefit dominates the heavy-occlusion regime. At low K on fine-grained classification the projection cost exceeds the benefit, defining the boundary where the linear bridge breaks down. The frozen JEPA predictor functions as a portable operator for occluded feature completion across encoder families, requiring no retraining of either model while fitting matched linear probes per mask fraction.

---


### 35. [A Step Forward Towards Trustworthy Risk-Aware Facial Retrieval (RA-FR)](https://arxiv.org/abs/2607.16279)

**<font color=#1a73e8>作者：</font>** Muhammad Emmad Siddiqui, Muhammad Rafi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facial image retrieval in unconstrained surveillance environments is a high-stakes challenge where missing a subject of interest -- a single false negative -- is simply not an option. Despite near-perfect performance on curated benchmarks, current recognition systems falter under real-world domain shifts such as low resolution, motion blur, and uncontrolled illumination (e.g., SCFace). Addressing this reliability gap, we propose Risk-Aware Facial Retrieval (RA-FR), a framework that moves beyond fixed Top-$k$ retrieval to adaptive set generation, guaranteeing ground truth inclusion within a user-specified risk level ($\alpha$) and confidence level ($1 - \delta$). Our approach integrates three core contributions: (1) reducing aleatoric uncertainty via a hybrid blind face restoration technique coupling Latent Consistency Models (InterLCM) and DiffBIR; (2) extracting discriminative, restoration-robust features via self-supervised DINOv1 ViT-B with GGeM pooling; and (3) employing conformal prediction with Hoeffding's inequality to dynamically calibrate retrieval set sizes based on query uncertainty. On the IMFDB benchmark, it consistently satisfies a 5% risk target with an average retrieval set size of approximately 10 images. By unifying domain-specific restoration, robust representation learning, and provable decision rules, RA-FR offers a pipeline that makes facial retrieval in surveillance both reliable and auditable. The code is available at: this https URL.

---


### 36. [Moving Like a Human: Ego-Motion-Normalized Temporal Signatures for Real-Time Aerial Person Tracking on Milliwatt-Class Hardware](https://arxiv.org/abs/2607.16282)

**<font color=#1a73e8>作者：</font>** Akbar Anbar Jafari, Cagri Ozcinar, Gholamreza Anbarjafari  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Follow-me person tracking must run on the drone itself, where affordable companion computers offer only a few effective int8 GFLOP/s. At typical follow distances a person spans 10-60 pixels, indistinguishable from clutter and beyond the reach of single-frame appearance detectors. The missing evidence is temporal and belongs in the input representation, computed analytically, rather than in learned temporal machinery. EMTS-Det is a five-stage system that estimates ego-motion, converts each frame into ego-motion-normalized residual-motion channels, detects person centers with a 22k-parameter, 7.6-MFLOP network, tracks a locked target with a Kalman filter in stabilized coordinates, and verifies tracks with a 1-D convolutional classifier of human motion (ROC AUC 0.941). Training uses a synthetic-motion curriculum with motion channels generated by the deployed ego-motion code. Multi-seed ablations locate the value in generalization: on held-out VisDrone-DET a luminance-only variant collapses to 0.051 AP25 versus 0.415, as does YOLOv8n fine-tuned identically despite 1,100 times the compute, while the deployed int8 detector reaches 0.694 AP25 in-domain and 0.444 on this split. Temporal-shift modules lower accuracy, so the deployed detector is stateless. Silent int8 calibration failures are documented; min-max calibration with propagated caches matches float within 0.008 AP. On a Raspberry Pi Zero 2W the pipeline runs at 31.85 FPS with 0.462 AP25 and 0.714 recall over 1,000 real-world UAV videos, versus 1.95 FPS and 0.172 AP25 for YOLOv8n. A 57-second field sequence shows auto-lock at 1.3 s, 97.9% lock recall, and recovery from all nine occlusions with zero false re-locks.

---


### 37. [A Shared Latent for Partially-Labeled Multi-Task Facial Affect Recognition](https://arxiv.org/abs/2607.16285)

**<font color=#1a73e8>作者：</font>** Hong Hai Nguyen, Sy Phan Van, Soo-Hyung Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facial affect in the wild is naturally multi-task: valence-arousal, discrete expressions, and facial action units describe the same face. Yet real corpora annotate these tasks only partially and unevenly, so most systems mask the missing labels or impute pseudo-labels and forgo the cross-task signal. We instead cast partially-labeled multi-task learning as marginalization over a shared affect latent: one variational bottleneck mediates all three task decoders, so a frame annotated for one task shapes the representation the others use, and the masked objective reappears as the reconstruction term of an evidence lower bound. On s-Aff-Wild2, where only 37% of frames carry all three labels, the classes are severely imbalanced, and pretraining on the source data is disallowed, we isolate where this coupling acts. On a single backbone it lifts expression macro-F1 from 0.403 for a dedicated specialist to 0.446, which the masked-loss model does not reach; a second, near-peer backbone with decorrelated errors then breaks an action-unit ceiling that external action-unit data could not, while valence-arousal stays within noise. Every gain is disciplined by a matched-control negative; together these controls indicate that the rare-class failure is representational, not a matter of loss shaping. As each task's source is chosen on the evaluation split, we report the assembled result, a combined multi-task score of 1.679 on validation, as an in-sample endpoint and rest our conclusions on the controlled comparisons; a small, regime-dependent transfer of the expression advantage to AffectNet and RAF-DB is presented as exploratory rather than conclusive.

---


### 38. [Depth Estimators Are Implicit Neural Fields for 3D Scene Geometry Inpainting and Reconstruction](https://arxiv.org/abs/2607.16286)

**<font color=#1a73e8>作者：</font>** Yingzhao Jian, Zihao Lin, Hehe Fan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The 3D geometry of real-world scene data is often incomplete. Mainstream methods use depth estimators to inpaint missing structure. However, their prediction results can be inconsistent with observed geometry, or unreliable on out-of-distribution data. To solve these problems, we propose Neural Depth Field (NDF). Our key insight is that a depth estimator can also be a scene-level implicit field. As an estimator, it adapts to the target domain by learning observed depth data. As an implicit field, it fits the existing geometry to maintain consistency. Under this view, NDF addresses both problems through a single test-time optimization. Experiments show that NDF produces high-fidelity and globally consistent geometry across diverse scene data, ranging from indoor scans to satellite imagery. It reduces cross-view inconsistency by 63.3\% and improves inpainting accuracy by 23.1\%, achieving state-of-the-art performance in 3D scene geometry inpainting. The code is available at: this https URL.

---


### 39. [Identity-Consistent Expression Fields: A Disentangled Neural Radiance Field Framework for Few-Shot Facial Expression Synthesis](https://arxiv.org/abs/2607.16287)

**<font color=#1a73e8>作者：</font>** Minh Tran  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neural Radiance Fields (NeRF) have enabled photorealistic novel-view synthesis of 3D scenes and, in the facial domain, have been extended to reconstruct and animate 3D face models from a small number of images. However, existing few-shot dynamic NeRF methods for facial expression editing typically warp a single learned feature volume conditioned on target expression parameters, which can cause identity-specific appearance details (skin texture, fine geometric structure) to drift when the model is driven toward expressions far from those seen in the few-shot input set. We propose Identity-Consistent Expression Fields (ICEF), a framework that explicitly disentangles a static, identity-specific radiance component from a dynamic, expression-conditioned deformation component, and introduces an identity preservation regularizer that constrains the deformation network to modify only expression-relevant regions while leaving identity-specific canonical appearance untouched. ICEF further incorporates a confidence-weighted conditional feature warping step that down-weights unreliable warps for target expressions that are far, in parameter space, from the observed few-shot inputs, mitigating artifacts observed in prior few-shot dynamic NeRF methods when extrapolating to novel expressions. We relate ICEF to prior few-shot dynamic NeRF, static 3D-aware face generation, and disentangled face-editing radiance field methods, and describe an evaluation protocol measuring both novel-expression rendering quality and, specifically, identity-consistency metrics across a range of expression-parameter extrapolation distances.

---


### 40. [A Synthetic 3D Gear Dataset for Manufacturing Quality Inspection (MFGNet-Gear)](https://arxiv.org/abs/2607.16288)

**<font color=#1a73e8>作者：</font>** Ruo-Syuan Mei, Chenhui Shao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Quality control in smart manufacturing increasingly relies on data-driven methods, particularly deep learning, to automate the inspection of manufactured parts. Recent advances in three-dimensional (3D) metrology have enabled fine-scale assessment of dimensional accuracy, surface quality, and shape conformity. However, deep learning methods for point-cloud-based inspection require large volumes of labeled data covering part designs and defect types, which are costly and time-consuming to obtain. Moreover, defective parts are intrinsically rare in mass production, and the resulting class imbalance can degrade model performance and make rare defect types difficult to detect. Synthetic data generation (SDG) offers a promising approach to address these challenges by producing large, balanced, and fully annotated datasets. Yet, applying SDG to precision components requires representing part geometry and defect morphology parametrically, so that design and quality can be co-varied. This article describes MFGNet-Gear, a publicly available synthetic 3D dataset comprising 24,000 paired polygon meshes and point clouds across 12 gear designs and 4 quality classes, with 500 instances per design-quality combination. Gear geometries are generated with parametric computer-aided design software, with dimensional parameters perturbed by $\pm$0.0254 mm and defect parameters sampled from distributions representing defect morphologies. For each mesh, 100,000 points are uniformly sampled using Open3D and stored as N $\times$ 3 coordinate text files. Metadata labels identify the gear design and quality class, supporting part design classification, geometric defect detection, representation learning, and dataset benchmarking. MFGNet-Gear provides an open-source dataset for deep learning-based 3D metrology, with a reproducible generation pipeline extensible to additional part designs.

---


### 41. [Strength-Parity Ensembling with Parameter-Isolated Experts for Multi-Task Affect Recognition](https://arxiv.org/abs/2607.16290)

**<font color=#1a73e8>作者：</font>** Hong Hai Nguyen, Van Thong Huynh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Leading entries on the multi-task track of the 11th ABAW challenge rely on heavy ensembling, yet which member is worth adding to an already strong ensemble is rarely made explicit. We study this question for joint valence-arousal estimation, 8-way expression recognition, and 12-way action-unit detection from a single unconstrained face, under partial, long-tailed labels and a rule that forbids pretraining on Aff-Wild2. Building on a shared affect-latent that marginalizes the missing labels across two affect-supervised backbones, we propose a strength-parity rule: an added member lowers the ensemble error only when it is both decorrelated from the current members and a near-peer of them in individual accuracy. The rule exposes a concrete obstacle, as on a single backbone re-seeding and even distinct fine-tuning curricula re-converge to a prediction correlation of 0.98 and add no diversity. Parameter-isolation removes it: confining each adaptation to a disjoint low-rank subspace of a shared backbone yields experts that stay decorrelated at 0.91 while remaining near-peers, the strongest of them an AffectNet-adapted expert. The resulting system raises the overall validation score to 1.6949, against the organizers ConvNeXt-with-MixAugment baseline of 0.45; with per-AU calibration and by pooling the shared-latent heads valence-arousal byproduct as a further near-peer, the strongest configuration reaches 1.7259.

---


### 42. [Beyond Target Scores: Measuring Off-Target Drift in Diffusion-Based Medical Image Editing](https://arxiv.org/abs/2607.16291)

**<font color=#1a73e8>作者：</font>** Todd Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models can now edit medical images in visually plausible ways, but the standard evaluation question is too narrow: did the target score increase? In clinical imaging, target findings are entangled with co-morbidities, acquisition effects, and selection bias, so a model can appear successful by changing correlated non-target findings rather than isolating the intended pathology. We introduce CIB-Med-1, a trajectory-level benchmark for controlled biomarker editing in chest radiography. CIB-Med-1 evaluates directional pleural effusion editing through calibrated target progression, inversion rate, and off-target semantic drift over 14 clinically motivated nuisance axes. The benchmark exposes a reward-hacking failure mode in which diffusion editors increase effusion scores while simultaneously altering parenchymal, cardiomediastinal, pleural, chronic, or artifact-related findings. We further present a constrained diffusion guidance baseline that optimizes target progression subject to bounded off-target change. Across held-out radiographs, the constrained editor preserves target progression ($\rho_{\mathrm{trend}}=0.88$ vs. $0.90$ for unconstrained guidance) while reducing median off-target drift from $0.46$ to $0.20$ and 90th-percentile drift from $0.98$ to $0.33$. Drift magnitude tracks empirical target--off-target association, supporting the view that semantic instability is structured rather than incidental. A blinded human validation probe with radiology trainees further shows stronger agreement with intended progression orderings ($\tau=0.61$ vs.\ $0.29$ for Pix2Pix). These results argue that medical image editing should be evaluated as trajectory-level semantic control, not as endpoint score maximization.

---


### 43. [It Depends on the Dataset: When a Brain-Encoding Model's Predicted Responses Beat Their Visual Backbone for Video Memorability](https://arxiv.org/abs/2607.16292)

**<font color=#1a73e8>作者：</font>** Carson Rodrigues  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Brain-encoding foundation models predict fMRI responses to video, audio, and text well enough to win the Algonauts 2025 challenge. We ask whether their predicted responses, obtained with no scanner, are a useful feature lens for a downstream human-behavior task: forecasting the memorability of short videos. We project each clip into TRIBE v2's predicted cortical space and forecast short-term memorability with ridge regression, against a matched control: the model's own V-JEPA2 visual backbone taken before the brain projection. The answer is dataset-dependent, and cleanly so. Within Memento10k the backbone wins (Spearman 0.594 vs 0.544 for the brain projection); within VideoMem the brain projection wins (0.415 vs 0.368, delta +0.047, 95% CI [+0.009, +0.088]). Both within-dataset gaps have bootstrap intervals excluding zero, in opposite directions. Cross-dataset transfer inherits the split: trained on Memento10k and tested on VideoMem the brain projection beats the backbone (+0.076), while the reverse loses heavily (-0.311). Each representation transfers best onto the dataset it already fits better. The VideoMem advantage is not a sample-size artifact (it survives matched training size and a PCA-then-ridge pipeline) and not mere compression of the backbone (a compressed or heavily regularized backbone tops out below the brain projection, which also beats a transfer-tuned backbone, +0.053). So predicted-brain features carry a small but real memorability signal the backbone misses on one dataset and not the other: not a domain-general prior, but a dataset-specific representation. A vision-orthogonal component (partial Spearman 0.19, permutation p=2.5e-4) localizes to ventral occipito-temporal cortex. Code and predicted-response arrays are released; source videos and scores are not redistributed.

---


### 44. [SLT: Robust Quantum Neural Networks for Noisy-Label Medical Image Classification via Supermartingale-based Label Transition](https://arxiv.org/abs/2607.16293)

**<font color=#1a73e8>作者：</font>** Jun Zhuang, Mohammad Al Hasan, Yiyu Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Noisy-label learning in small-scale medical image classification is challenging and hinders the superiority of deep neural networks. Recent studies suggest that quantum neural networks (QNNs) have shown potential in limited-data regimes, yet their use for noisy-label learning remains under-explored. A key obstacle is QNNs' intrinsic "natural smoothness", which may regularize training but also obscure high-confidence samples needed for noise-transition estimation. We propose Supermartingale-based Label Transition (SLT), an anchor-free loss correction framework for robust QNN-based medical image classification under noisy labels. SLT models entropy reduction in predictive distributions as a supermartingale and uses its monotonic behavior to identify stable transition-matrix refinement steps. This enables dynamic transition updates while reducing noise-driven oscillations during QNN training. We further provide a convergence analysis showing that the proposed transition-refinement process reaches a steady state. Experiments on multiple public small-scale medical image datasets demonstrate that SLT consistently improves QNN-based classification and stably outperforms classic noise-label learning baselines under synthetic and real-world label noise.

---


### 45. [Emergent Hierarchical Monosemantic Neurons from the Group-Contrastive Forward-Forward Algorithm](https://arxiv.org/abs/2607.16295)

**<font color=#1a73e8>作者：</font>** Yiming Tang, Qinglin Qi, Zhaoqian Yao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability has made significant strides in understanding neural network representations, with sparse dictionary learning (SDL) methods, most prominently sparse autoencoders, as a central paradigm. However, recent work has reported several limitations of this paradigm: SDL objectives are non-identifiable; SDL methods rely heavily on the Linear Representation Hypothesis; and a growing body of evidence points to concepts that are encoded non-linearly and are therefore not expressible as any single direction. We hypothesise that a different route to monosemanticity is available. Biological visual systems exhibit highly selective neurons organised into hierarchies of increasing abstraction, and this organisation emerges from local, layer-wise learning rules rather than from a global error signal; we therefore ask whether a biologically plausible learning algorithm will likewise yield monosemantic neurons. To test this, we propose Group-Contrastive Forward-Forward (GCFF), a forward-forward training algorithm that combines class-specific routing with within-class contrastive objectives, reaching monosemanticity through architectural constraints rather than sparsity. Because GCFF attaches multiple non-linear layers to the representation under study, its neurons can therefore capture the non-linear concepts. On CLIP representations, a single trained GCFF module recovers monosemantic neurons whose abstraction increases progressively with depth, reaching environmental properties that hold independently of an image's foreground, without any sparsity constraint or supervision of abstraction level. We further demonstrate that GCFF can train networks from scratch, achieving state-of-the-art performance among forward-forward algorithms on various image classification benchmarks.

---


### 46. [Rethinking Feature Reliance Evaluation with Semantically Matched Suppression](https://arxiv.org/abs/2607.16298)

**<font color=#1a73e8>作者：</font>** Ning Jiang, Tianyi Luo, Zhengyong Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding whether visual recognition models rely on shape, texture, or color is central to interpreting their behavior. Prior cue-conflict studies have strongly influenced the view that CNNs are texture-biased, yet such tests measure cue preference under artificial conflicts rather than feature reliance during natural recognition. We revisit this question through controlled feature suppression and show that performance drops are difficult to interpret unless different suppression operations impose comparable category-level damage. We introduce a semantically matched evaluation framework that compares shape and texture suppression at matched levels of category separability loss. Under this framework, ImageNet-trained CNNs show stronger degradation under texture suppression than under shape suppression, revealing greater texture reliance than suggested by unmatched suppression analyses. Extending the comparison across architectures, we find that Vision Transformers retain higher accuracy than CNNs under both shape and texture suppression. Brain encoding further shows that ViT representations exhibit smaller suppression-induced decreases in neural prediction performance under the tested suppression settings. These findings indicate that semantic comparability is essential for interpreting feature reliance from suppression experiments, and suggest that the robustness advantage of ViTs may be related to representations more compatible with human visual cortex.

---


### 47. [Algorithmic Accuracy as a Motivational Driver in Robot-Mediated Learning: A Comparative Study of Cross-Correlation and CNN-Based Sound Detection in an Interactive Quiz Game](https://arxiv.org/abs/2607.16299)

**<font color=#1a73e8>作者：</font>** Rezaul Tutul, Ilona Buchem, Niels Pinkwart  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In competitive learning activities, inaccurate robot decisions may reduce students' perceptions of fairness and competence, ultimately affecting their motivation. This paper investigates whether the accuracy of sound detection algorithms influences student motivation during a robot-mediated quiz game. A Pepper humanoid robot hosted an interactive buzzer-based quiz in which two sound detection approaches, a Convolutional Neural Network (CNN) and a Cross-Correlation algorithm, were evaluated using a controlled between-subjects experiment involving 40 university students. Participants were equally assigned to a CNN group (n = 20) and a Cross-Correlation group (n = 20). Both groups completed the same quiz under identical conditions, differing only in the sound detection algorithm used for first-responder identification. Student motivation was assessed using the Intrinsic Motivation Inventory (IMI), while algorithm performance was evaluated through real-time detection accuracy. The results indicate that the Cross-Correlation approach achieved more reliable sound detection under classroom conditions and produced significantly higher scores across all IMI subscales, demonstrating greater student interest, perceived competence, effort, perceived choice, and lower perceived pressure (after reverse coding). These findings provide empirical support for the proposed Algorithmic Precision-Motivation Relationship (APMR) model, demonstrating that algorithmic accuracy is not merely an engineering performance metric but an important factor influencing learner motivation in robot-assisted educational environments.

---


### 48. [FedDP-PALD: A Privacy-Preserving Federated Latent Diffusion Framework with Prototype Aggregation for Medical Data Synthesis](https://arxiv.org/abs/2607.16300)

**<font color=#1a73e8>作者：</font>** Md. Sajeebul Islam Sk., Khan Enaet Hossain, Md. Mehedi Hasan Shawon  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical images and physiological signals provide valuable information for accurate diagnosis. Developing diagnostic models often requires patient data from multiple institutions, although strict privacy regulations limit the sharing of sensitive clinical records. Federated learning enables multiple hospitals to train a shared model without exchanging raw data. However, existing methods face two problems: the information exchanged during training can reveal whether a patient's data were used, and synthetic data meant to replace real records often fail to preserve their predictive structure, which limits clinical use. To address this issue, we propose FedDP-PALD, a privacy-preserving federated latent diffusion framework for multimodal medical data synthesis under formal privacy guarantees. It jointly processes chest X-ray images and electrocardiogram (ECG) signals through gated multi-head attention with modality-availability masks, remaining effective even when a modality is missing. We also introduce Differentially Private Prototype Mixture Aggregation (DP-PMA), which clips class-level latent prototypes and adds calibrated Gaussian noise before combining them on the server to maintain $(\epsilon, \delta)$ differential privacy. We evaluate FedDP-PALD on PneumoniaMNIST, ChestMNIST, and MIT-BIH datasets, where differential privacy reduced summary-level attack AUROC from 0.6229 $\pm$ 0.0026 to between 0.5016 and 0.5093 for privacy budgets from $\epsilon = 1$ to $\epsilon = 8$. On the test data, synthetic-latent training achieved an F1 score of 0.8993 $\pm$ 0.0006 and an AUROC of 0.9057 $\pm$ 0.0503, close to the 0.9747 $\pm$ 0.0132 real-latent training. These results show that FedDP-PALD generates private synthetic representations that preserve useful decision performance while strongly resisting membership inference.

---


### 49. [Dual-Domain Self-Supervised Artifact Removal Framework for Photoacoustic Computed Tomography](https://arxiv.org/abs/2607.16304)

**<font color=#1a73e8>作者：</font>** Yucheng Zhou, Shuang Li, Yu Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Photoacoustic Computed Tomography (PACT) often faces severe challenges from reconstruction artifacts due to sparse detection conditions. In this work, based on the distinct differences in artifact patterns between back-projection-based and Fourier-based reconstruction algorithms, we propose a self-supervised artifact removal framework that employs a lightweight Siamese Neural Network and a composite loss function integrating cross-domain fidelity and uncertainty-weighted consistency, effectively decoupling dual-domain features and filtering artifacts. Comprehensive validations using simulations, phantoms, in vivo rat and human experimental data demonstrate that the proposed method can significantly suppress image artifacts. Furthermore, enabled by the acceleration of the spatial-domain and frequency-domain inverse operator, this end-to-end approach also achieves exceptional computational efficiency.

---


### 50. [CoBind: Stage-Aware Compositional Binding for Training-Free Text-to-Image Generation](https://arxiv.org/abs/2607.16307)

**<font color=#1a73e8>作者：</font>** Kaijie Chen, Ethan Caldwell, Mira Vossen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based text-to-image models often fail on complex prompts involving multiple entities, attributes, and relations, producing object omissions, incorrect attribute assignments, or reversed spatial layouts. Existing training-free methods mainly strengthen token-level attention, but do not explicitly model which attributes belong to which entities or when different constraints should be enforced during denoising.
We introduce \textbf{CoBind}, a training-free framework for stage-aware compositional binding. CoBind parses a prompt into a composition graph of entities, attributes, and relations. It first establishes the global layout using entity-completeness and relation constraints, then binds attributes to their target entities through contrastive cross-entity optimization. Structural guidance is gradually relaxed in later denoising steps to preserve textures and visual details. CoBind also adapts the guidance strength according to the current satisfaction of each constraint, reducing unnecessary latent updates.
CoBind requires no retraining or additional annotations. Experiments on T2I-CompBench++, GenEval, and multiple diffusion backbones show consistent improvements in attribute binding, spatial relations, and complex compositional generation while maintaining competitive visual quality.

---


> [!TIP]
> 当前位于：**1-50**（第 1/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-386](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
