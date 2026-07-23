# 📦 其他研究 | 2026年07月24日

> 本类共 **192** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-192](./part-04.md)

---

### 1. [Hybrid LSTM-Graph Neural Framework for Robust Financial Fraud Detection and Adversarial Resilience](https://arxiv.org/abs/2607.19350)

**<font color=#1a73e8>作者：</font>** Mariam Zakaria Moussa Ali  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial institutions face significant challenges in detecting sophisticated money laundering patterns, such as smurfing and layering, due to extreme data imbalance (0.13% fraud rate) and evolving adversarial evasion tactics. This paper proposes FraudShield AI, a hybrid framework that integrates Long Short-Term Memory (LSTM) networks with hand-crafted Graph Topological Features to capture both temporal sequences and structural relational context. By engineering network-centric features including PageRank Centrality, In-Degree dynamics, and a custom Flow Ratio, the system shifts the detection paradigm from isolated transaction analysis to network-level forensics. A Focal Loss objective is used to address class imbalance, and a dynamic thresholding mechanism is introduced to improve resilience against low-value smurfing attacks. Experimental evaluation on the PaySim dataset shows that the proposed hybrid model substantially outperforms Logistic Regression and XGBoost baselines in Precision, Recall, and F1-Score, particularly on hard-to-detect micro-transaction fraud patterns. An ablation study confirms the complementary contribution of both the temporal and topological components.

---


### 2. [OpenEvoShield: Dual Non-Stationary Continual Defense for Open-World Multi-Agent System Attacks](https://arxiv.org/abs/2607.19351)

**<font color=#1a73e8>作者：</font>** Litian Zhang, Chaozhuo Li, Yuting Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based multi-agent systems (LLM-MAS) are increasingly deployed in safety-critical applications, where adversaries inject malicious instructions through inter-agent communication to propagate harmful behaviors. Unlike static threats, these attacks are doubly dynamic: adversaries refine injection strategies against deployed defenses while normal-agent behavior drifts with system expansion. Existing defenses treat deployment as a closed-world problem and degrade rapidly once either distribution shifts beyond training coverage. We propose OpenEvoShield, a co-evolutionary continual defense framework for LLM-MAS. An asymmetric rate controller (M1) decouples fast attack-side and slow normal-side learning rates from dual drift signals. A normal-boundary updater (M2) maintains a dynamic behavioral boundary at the slow rate, while an EWC-regularized policy ensemble (M3) fast-adapts without catastrophic forgetting. An energy-based multi-granularity detector (M4) fuses node-, subgraph-, and graph-level evidence to classify novel attacks as out-of-distribution. Experiments over 100 deployment rounds across five benchmarks and four MAS topologies show that OpenEvoShield outperforms static and continual baselines, detecting most previously unseen attacks while keeping false positive rates low.

---


### 3. [Validating the Single Item Kawaii Measure](https://arxiv.org/abs/2607.19352)

**<font color=#1a73e8>作者：</font>** Katie Seaborn, Yijia Wang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Kawaii is the Japanese instantiation of cuteness. As a multimodal percept theoretically derived from the notion of baby schema, kawaii can be a property of voice and sound, visual appearance and form factor, and movement and expression. However, measuring user perceptions of kawaii remains an open question. In the absence of a validated instrument, a one-item self-report measure has been used extensively, but has not been validated. Here, we report on three types of validity -- convergent, known groups, and cross-context -- and reliability for the single item measure across nine data sets featuring responses to video game character voices and visual appearances and computer-generated voice assistant voices from N=967 unique participants. Our results demonstrate initial evidence of the validity of the one-item measure for voice and visual kawaii perceptions. Further rigour can be pursued with novel stimuli, test-retest validation, and concurrent validity against the upcoming multi-item measure of kawaii.

---


### 4. [Stochastic Primal-Dual Decoding for Multiobjective Generative Recommender Systems](https://arxiv.org/abs/2607.19357)

**<font color=#1a73e8>作者：</font>** Dmitrii Moor, Ben Carterette, Senthilkumar Krishnamoorthy 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in recommender systems (RS) have shown substantial performance gains through generative modelling. In practice, recommendation often involves constructing slates -- ordered lists of items -- that must satisfy multiple objectives beyond relevance, such as constraints defined over item attributes or fairness constraints. Existing multiobjective approaches either rely on post-processing techniques designed for non-generative settings, or incorporate auxiliary objectives directly into model training. The former does not explicitly account for the sequential nature of generative RS, while the latter is often impractical in large-scale systems.
We propose a lightweight, inference-time decoding layer that augments autoregressive generative RS to support multiobjective slate generation without modifying or retraining the underlying model. We formulate decoding as an online constrained optimisation problem, where items are selected sequentially, and trade-offs between relevance and auxiliary objectives are adjusted dynamically based on the remaining constraint slack, i.e., how much of each objective remains to be satisfied. This is implemented via a stochastic primal-dual approximation scheme that balances relevance and auxiliary objectives during generation.
We provide theoretical guarantees on constraint violation and regret, and evaluate the proposed approach through extensive offline experiments and a large-scale online A/B experiment in a real-world recommender system. Our results show consistent improvements in multiobjective trade-offs, including a +1.8\% gain in the auxiliary objectives achieved at zero cost to user satisfaction.

---


### 5. [AdaRoPE: Not All Attention Heads Should Rotate and Scale Equally](https://arxiv.org/abs/2607.19363)

**<font color=#1a73e8>作者：</font>** Shaowen Wang, Yuke Zheng, Tansheng Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rotary Position Embedding (RoPE) is widely adopted in Transformers to encode positional information, yet standard implementations enforce a uniform frequency schedule and scaling across all attention heads. Using simplified retrieval tasks and length generalization scenarios, we show -- both empirically and theoretically -- that heads with different functional roles require distinct frequency ranges and attention scaling factors to operate effectively. Ignoring this structure leads to suboptimal utilization of embedding dimensions and degraded performance, particularly under long-context settings. To address these limitations, we propose AdaRoPE, which equips each attention head with learnable rotation frequencies and attention scaling factors. Pretrained LLMs with AdaRoPE consistently outperform existing RoPE variants, including partial RoPE and NoPE baselines. For context extension, we further show that uniform frequency and attention scaling, used in methods such as YaRN, are suboptimal. By applying head-specific scaling, AdaRoPE enables better context extension while better preserving short-context performance in both the extrapolation setting and the long-context continued pretraining setting. These results highlight the importance of optimizing rotary position embedding at the level of individual attention heads.

---


### 6. [Spectral-LSH: Sub-Quadratic Prompt Compression via Krylov-Projected Locality-Sensitive Hashing](https://arxiv.org/abs/2607.19368)

**<font color=#1a73e8>作者：</font>** Ali Mahdavi, Azaseh Zamanifar, Amirfarhad Farhadi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-prompt inference remains expensive because prefill attention scales quadratically with sequence length. We propose Spectral-LSH, a training-free prompt compression method that operates before the prompt enters the language model. Spectral-LSH approximates the dominant components of an implicit attention-kernel operator using a Krylov subspace method together with random features, avoiding explicit $O(N^2)$ attention-kernel materialization. It then applies SimHash in the resulting attention eigenspace to group similar tokens and aggregate them into macro-tokens with causal positional assignments.
We evaluate Mistral-7B-Instruct-v0.3, Qwen2.5-7B-Instruct, and Qwen2.5-14B-Instruct on C4. Our experiments reveal a compression-ratio phase transition. Below $\rho = 4 \times$, local token redundancy is low enough that lightweight chunking typically provides the best latency--quality trade-off. Above $\rho = 8 \times$, the spectral path preserves quality that chunking loses. At $\rho = 16 \times$, Qwen2.5-7B (adaptive) reduces the PPL ratio from 353.409 to 196.963, while Qwen2.5-14B (adaptive) reduces it from 9.533 to 3.427.
On a small long-context structured stress test containing JSON-like, code-like, and table-like inputs, local LSH also improves every metric over chunking at $8 \times$. The adaptive backend captures both regimes by using the chunk path at low compression and spectral clustering at high compression, although chunking remains the fastest backend in total latency.

---


### 7. [Beyond Tracking or Shortcut: Composition-Bounded Predictive States in Poker Autoregressive Models](https://arxiv.org/abs/2607.19369)

**<font color=#1a73e8>作者：</font>** Quanhao Li, Qianyu Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hidden-state probes often recover latent labels in imperfect-information sequence models, but this alone does not establish that a model maintains a posterior belief distribution over hidden states. This paper studies this ambiguity in a no-range Limit Hold'em autoregressive model trained only on action and value targets, not on an opponent's hand or range. Opponent-range probes are positive after action/value controls in two of three seeds, and the behavior head predicts held-out actions about five percentage points above a baseline using only observable public history. However, visible public betting composition explains more opponent-range signal than residual hidden states, suggesting that most recoverable information comes from betting summaries. Action/value+composition baselines reach 16.5-16.7% top-10 accuracy while composition-residual hidden probes fall to 11.4-12.2%, and matched-composition comparisons are negative in every seed. We call this evidence pattern composition-bounded predictive support: hidden states remain behavior-predictive and opponent-range correlated, but most recoverable range information is explained by visible betting composition rather than residual hidden-state structure. This is a case-study claim about opponent-range representational evidence, not exact Bayesian posterior tracking or a causal belief mechanism. Synthetic control and oracle validations show that the same diagnostics accept posterior-sensitive states and reject raw composition states under matched controls. Thus positive belief probes should be interpreted through targeted alternatives before being treated as evidence of belief tracking.

---


### 8. [Euclean: Automated Geometry Problem Formalization with Unified Verification in Lean](https://arxiv.org/abs/2607.19374)

**<font color=#1a73e8>作者：</font>** Linbin Tang, Jingyan You, Zilin Kang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent formal reasoning systems have reached IMO-level performance, yet they leave a fragmented landscape: algebra and number theory are handled in Lean, while geometry still relies on domain-specific languages with limited formal guarantees. This split increases the trusted computing base and hinders unified model development. Existing geometry-in-Lean efforts (LeanEuclid, LeanGeo) introduce custom axiom systems incompatible with standard Mathlib, and their small scale ($<$ 1,100 problems) limits large-scale training. Native Mathlib autoformalization of geometry, however, poses distinct challenges: implicit diagrammatic assumptions (e.g., topological configuration and non-degeneracy) must be made explicit rather than deferred to external solvers, and models must adapt to Mathlib's small, rapidly evolving geometry infrastructure. We present Euclean, a four-stage framework - constraint explication, configuration anchoring, formalization mapping, and iterative repair - for automatically formalizing geometry in native Mathlib. We construct OMNI-Geometry (768 competition problems) and Numina-Geometry (177,597 problems), the largest geometry formalization dataset in Lean. Human evaluation shows 48.89% TOP1 and 73.33% TOP5 accuracy. Training Goedel v2 on our formalizations improves proof success from 13.6% to 15.1%, validating dataset quality for unified neural theorem proving. Code and datasets: this https URL.

---


### 9. [Native Multi-Dimensional Subquadratic Operators via Input Dependent Long Convolutions](https://arxiv.org/abs/2607.19378)

**<font color=#1a73e8>作者：</font>** David R. Wessels, Farhad Ramezanghorbani, David W. Romero 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Subquadratic alternatives to attention require compromises when applied to multi-dimensional data: standard convolutions lack global receptive fields and input dependency, while recurrent models require rasterizing data such as images, volumes, and partial differential equation (PDE) into an ad-hoc $1\rm D$ scan order that violates their spatial structure. We introduce \textit{HyenaND}, a subquadratic, global, input-dependent operator that acts directly on the native geometry of multidimensional data through convolutions with implicitly parametrized global, input-dependent multi-dimensional convolutional kernels. Our CUDA implementation, \texttt{nSubQ}, fuses the FFT-convolution path to turn HyenaND's $\mathcal{O}(L \log L)$ scaling into wall-clock speedups. Across long-context genomics, computer vision, medical imaging, and PDE modeling, pure HyenaND stacks match the accuracy of strong attention baselines, while hybrid configurations that interleave HyenaND and attention layers outperform both pure attention and strong recurrence-based hybrids.

---


### 10. [Bayesian Wind Tunnels for Model Selection](https://arxiv.org/abs/2607.19379)

**<font color=#1a73e8>作者：</font>** Siddhartha R Dalal, Vishal Misra, Abhay Parekh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prior work has shown that transformers can perform exact Bayesian filtering within a fixed
hypothesis class. Can they also perform Bayesian model selection -- identifying the correct
hypothesis class from data? We introduce model-selection Bayesian wind tunnels: controlled
environments where ground-truth posteriors over hypothesis classes are available in closed
form. Using fixed-point-free involutions -- whose defining property f(f(x))=x is purely
relational -- a 2.8M-parameter transformer achieves 0.01-bit entropy agreement with the
Bayesian optimum (3 seeds), with both integer tokens and opaque symbols whose meanings
change every episode. This extends to non-nested comparisons: involutions vs. 3-cycles
(where neither class is a subset of the other) achieve class-posterior MAE under 0.001,
demonstrating genuine model selection beyond simplicity/subset bias. We then identify a
sharp perceptual access condition: when the discriminative statistic requires arithmetic --
modular addition (rotations) or multiplication (f(x)=cx mod p) -- model selection succeeds
with integer tokens but fails completely with opaque symbols, and this boundary persists
under 112x scaling (2.8M to 316M parameters). A stationarity control confirms the operative
factor: opaque tokens with a fixed relabeling succeed (0.009-bit MAE), showing that stable
semantics, not integer identity, enable circuit compilation. Header subtask diagnostics
localize the failure to the composition of header inversion with arithmetic rather than
header parsing itself. Probing frontier LLMs on the same tasks shows qualitative Bayesian
behavior but a large calibration gap (~55x), measured through lossy probes and therefore
directional rather than exact.

---


### 11. [CruiseBench: A Real-Flight-Aligned N-CMAPSS Benchmark for Engine RUL Prediction](https://arxiv.org/abs/2607.19380)

**<font color=#1a73e8>作者：</font>** Pu Cheng, Qiang Miao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Remaining useful life (RUL) prediction estimates how long an engine can continue safe operation and is central to maintenance planning. N-CMAPSS extends C-MAPSS by simulating run-to-failure aero-engine trajectories using recorded real-flight profiles and retaining complete within-flight time series rather than cycle-level snapshots. However, this added realism reduces evaluation control because full-flight records increase data volume and entangle degradation cues with operating-regime variation, complicating preprocessing choices and direct comparisons of RUL modeling performance. To mitigate this issue, this paper proposes CruiseBench, a cruise-stage RUL benchmark derived from N-CMAPSS. It introduces CPM-N-CMAPSS (Cruising-Period Mask for N-CMAPSS), a mask artifact that stores cycle-local cruising intervals identified by the common-altitude method for the nine accessible subdatasets. CruiseBench applies a fixed protocol to the masked rows, using scenario descriptors and measured sensors as inputs while excluding virtual sensors, health parameters, and auxiliary metadata from the feature tensor, preserving native-resolution windows, and applying dataset-wise RUL caps. Experiments with LSTM, GRU, TCN, and TSMixer provide baseline results for this setting. Under CruiseBench-eta5-W256-S10, TSMixer obtains the lowest average RMSE, $3.4\pm1.71$, and Saxena score, $(2.50\pm2.99)\times 10^{4}$. Ablation studies show that flight-stage selection, temporal downscaling method, and RUL-cap threshold affect reported results. With its fixed cruise-stage protocol, CruiseBench provides a reproducible sub-benchmark for controlled RUL model comparison and CPM-N-CMAPSS provides a stage-specific data foundation for future transfer-learning and domain-adaptation studies.

---


### 12. [Challenges of Explainability in Continual Learning for Time Series Forecasting](https://arxiv.org/abs/2607.19382)

**<font color=#1a73e8>作者：</font>** Quentin Besnard, Emmanuel Doumard, Nicolas Labroche 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning models have shown strong potential for time series forecasting, yet their deployment in real-world environmental monitoring remains challenging due to non-stationary dynamics and limited explainability. In this work, we investigate explainability as a central tool for understanding continual learning in adaptive time series forecasting, with Experience Replay strategies. We study neural forecasting architectures such as PatchMixer, PatchTST and DLinear, augmented with attention-based sampling mechanisms to support model adaptation over time. Explainability is leveraged through attention rollout and gradient-based attribution methods (Grad-CAM) to analyze both predictive behavior and sampling strategies within a continual learning framework. Experiments conducted on real-world piezometric time series exhibiting heterogeneous patterns and regime shifts show that analyzing model and sampling behaviors provides valuable insights into the dynamics of the continual learning framework. Beyond predictive performance, our results highlight the challenges and opportunities of using explainability to understand continual learning behaviors, revealing how attribution patterns evolve over time and how they can inform data selection and adaptation strategies in non-stationary forecasting scenarios.

---


### 13. [SUM: Unified Geometric Surgery on Spatio-Temporal Adaptation Vectors for Federated Class Incremental Learning](https://arxiv.org/abs/2607.19384)

**<font color=#1a73e8>作者：</font>** Jaeik Kim, Jaeyoung Do  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world intelligent systems often require both distributed collaboration across data-isolated clients and continual adaptation to evolving tasks. This setting naturally gives rise to Federated Class Incremental Learning (FCIL), which combines Federated Learning (FL) and Continual Learning (CL). However, their combination introduces two coupled sources of interference: spatial interference from heterogeneous clients and temporal interference from sequential tasks, jointly leading to Spatial-Temporal Catastrophic Forgetting (ST-CF). Existing approaches typically address spatial and temporal interference with separate mechanisms, often incurring additional client-side computation or communication, while leaving directional interactions among updates during aggregation unregulated. In this paper, we reinterpret FCIL as a unified multi-task learning problem, where both client and task updates are represented as adaptation vectors in a shared parameter space. Based on this view, we propose Unified Geometric Surgery on Spatio-Temporal Adaptation Vectors (SUM), a purely server-side framework that performs geometric surgery on adaptation vectors during aggregation. Spatial SUM mitigates client-level interference within each round, while causal online temporal SUM removes cross-task interference over time without additional client-side computation, communication, or memory beyond standard federated training. Empirically, SUM achieves up to 22% improvement over prior FCIL methods across diverse vision and language benchmarks while remaining robust to unreliable clients and maintaining computational efficiency.

---


### 14. [STN-TGAT: Top-K Portfolio Construction via Prior-Guided Graph Attention with Learnable Soft-Threshold Sparsification](https://arxiv.org/abs/2607.19385)

**<font color=#1a73e8>作者：</font>** Haoran Guo, Yutong Lu, Li Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper tackles the problem of stock ranking and portfolio construction under realistic investment settings by jointly modeling temporal dynamics and cross-sectional dependencies. We propose the Soft-Threshold NMI-prior Transformer Graph Attention Network (STN-TGAT), which integrates a temporal Transformer with a Graph Attention Network to capture long-horizon sequential patterns and dynamic inter-stock relationships. An NMI-based prior graph combined with a soft-threshold sparsification mechanism enhances structural robustness by mitigating noisy correlations while preserving informative connections. The portfolio formation process incorporates practical considerations, including Top-5 selection within the Top-50 $S\&P$ 500 constituents, explicit weight allocation, and transaction cost adjustment, thereby aligning the evaluation with real-world trading conditions. Empirical results on real-world data demonstrate that STN-TGAT consistently outperforms benchmark models from predictive accuracy and investment profitability measured by portfolio returns. These findings suggest that combining decision-aligned training with adaptive relational modeling provides a coherent and practically effective framework for data-driven portfolio construction.

---


### 15. [Building Fast, Evaluating Slow: Pipeline Choices Dominate Autointerpretability Score Variance](https://arxiv.org/abs/2607.19386)

**<font color=#1a73e8>作者：</font>** Sinie van der Ben, Neele Roch, Anna Hedström 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-paper comparison of sparse autoencoder (SAE) interpretability often relies on autointerpretability scores. In this evaluation pipeline, a language model (LM) explains each feature, and another LM scores the explanation. For these comparisons to be meaningful, scores must reflect stable properties of the features rather than confounding aspects of the evaluation pipeline. Through systematic experiments across four metrics (simulation, detection, fuzzing, purity), two models (Pythia-160M, Apertus-8B), and four axes of methodological variation, we show that this assumption does not hold. Specifically, we find that R1) methodological variance collectively exceeds architectural variance across all metrics and tested models; R2) each metric exhibits a distinct instability profile, with detection being the most stable and fuzzing unreliable across all conditions; R3) top-k feature rankings do not stay consistent across corpus and draw conditions, masking per-feature instability behind stable mean scores; a failure that cannot be detected by monitoring explanation similarity alone. These findings suggest that cross-paper comparisons based on autointerpretability scores may reflect pipeline differences rather than architectural differences, with implications for the ongoing debate on SAE utility. More broadly, unreliable evaluation slows progress in interpretability research at a time when reliable tools for understanding AI systems are needed. To support evaluation, we contribute a variance decomposition approach, a Stability Check, and a Minimum Reporting Checklist.

---


### 16. [Scale-Aware Learning of Chaotic Dynamics on Unstructured Meshes via Binned Spectral Losses](https://arxiv.org/abs/2607.19387)

**<font color=#1a73e8>作者：</font>** Kanad Sen, Romit Maulik  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Surrogate modeling for high-dimensional nonlinear dynamical systems that exhibit chaos requires mechanisms that preserve not only pointwise accuracy but also the scale-dependent structure of physical fields. Bandwise spectral power losses, such as the binned spectral loss function, provide such supervision on structured grids, where Fourier modes define a standard frequency decomposition. On irregular meshes, however, no canonical Fourier basis exists, and spectral representations must be constructed from graph operators induced by mesh connectivity and geometry. In this study, we extend the binned spectral power loss for application to unstructured-mesh surrogate modeling of nonlinear dynamical systems. This is obtained by replacing Fourier bands with graph-Laplacian frequency bands, and we provide scalable Chebyshev and multilevel approximations for improving long-horizon rollout fidelity. In its full-spectrum form, our approach uses graph Laplacian eigenspaces to provide a graph analogue of Fourier band-power matching, but incurs the high cost of spectral decomposition. As a scalable approximation, we replace exact band projectors with sparse Chebyshev polynomial graph filters, avoiding explicit eigendecomposition. When utilizing multilevel graph architectures, we introduce Graph Laplacian Energy Alignment for Meshes (GLEAM), which applies retained-subspace scale-aware supervision across graph hierarchies so that coarse and fine representations are regularized during autoregressive rollout. Our results show that the proposed spectral losses improve long-horizon rollout fidelity and preserve statistical invariants for the forecasting of turbulent flows on unstructured meshes, compared to deterministic baselines.

---


### 17. [Neural Operator Surrogates for Two-Dimensional Neutron Flux Estimation](https://arxiv.org/abs/2607.19388)

**<font color=#1a73e8>作者：</font>** Japan K. Patel, Barry D. Ganapol, Anthony Magliari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work extends our one-dimensional single-sweep neural-operator studies to two dimensions. We consider one-group transport with isotropic scattering. As in the one-dimensional work, we use Fourier neural operators (FNOs) to approximate the high-fidelity scalar flux. Additionally, we also investigate U-shaped neural operators (UNOs) in this study. We consider three surrogates. The first two map the material and source fields directly to the flux, one using an FNO and one using a UNO. The third is an FNO that additionally takes the scalar flux after one source iteration, the single-sweep approximation, as an input. Each case is solved to high fidelity with a verified discrete-ordinates solver, and an average relative L_2 error norm is used to characterize the quality of the inferred maps. We train every surrogate over three random seeds so that differences between them can be assessed against run-to-run variability. Two questions guide the study: whether the single-sweep input improves accuracy over the direct maps, and whether training on the logarithm of the flux improves accuracy in the strongly attenuated regions relevant to shielding.

---


### 18. [The Orthogonalized Read Is a Removable Training Scaffold for Recurrent Memory](https://arxiv.org/abs/2607.19390)

**<font color=#1a73e8>作者：</font>** Keston Aquino-Michaels  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A recent report finds that orthogonalizing the mLSTM memory matrix at read time (five Newton-Schulz iterations, trained through) substantially improves noisy associative recall. The effect replicates, but it is not a memory improvement. Training on this task is a long chance plateau followed by a sharp escape, and the orthogonalized read acts by re-conditioning the learning problem during the plateau. Three properties establish this. It must be self-consistent: an exact recursive least-squares read (the Mesa layer) reproduces it, while straight-through halves, delta-rule writes, frozen random keys, and plain normalization all fail. It is uniform: across a learning-rate x hardness grid it multiplies the escape hazard roughly six-fold with no detectable hardness dependence, widening the workable learning-rate corridor that narrows for the baseline. And it is removable: applied to failed models at inference it rescues none, and annealed away on an escape-triggered schedule it leaves numerically stock mLSTMs at full accuracy. Much of the published gain needs no architecture at all -- solved-rate at a fixed budget measures escape hazard, which follows a heat/noise law (learning-rate elasticity +3.0, gradient-noise elasticity -1.65) under which the original vocab-96 result is a large-batch noise condition rather than a capacity one. Decoding the memory state directly shows failed models carry roughly half their associations in linearly recoverable form: the plateau is a readout failure over half-written storage. Two conclusions travel beyond the intervention: recall benchmarks used for architecture selection partly measure trainability, and the system is a fully instrumented model organism of "emergence," in which a sharp behavioral threshold demonstrably arises from a censored metric over gradually accumulating structure.

---


### 19. [Predicting Groundwater Arsenic Concentrations Using Graph Neural Networks](https://arxiv.org/abs/2607.19392)

**<font color=#1a73e8>作者：</font>** William Xing, Stephanie Yang, Aarush Bandemegal 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Arsenic contamination in groundwater presents a longstanding public health crisis in the United States, especially for households depending on private wells. Accurate and spatially informed prediction of arsenic concentration is vital to identify high-risk areas and focus mitigation efforts. However, there is a lack of generalizable models for representing continuous variation in arsenic concentrations across regions. In this work, we pose arsenic prediction as a regression task and construct a spatially integrated dataset to aggregate over 74,000 arsenic samples from the Water Quality Portal (WQP), Mineral Resources Data System (MRDS), and Gridded National Soil Survey Geographic Database (gNATSGO). Specifically, we use a variety of techniques including kNearest Neighbors (k-NN) and Geographic Information Systems (GIS) to join arsenic measurement points from across the United States by location. Building on this dataset, we evaluate a diverse suite of machine learning models, including tree-based ensemble approaches, multilayer perceptrons, and spatially aware graph neural networks (GNN). Our findings show that while gradient-boosted trees are still considered state-of-the-art in the field of tabular data, GNNs are able to further account for spatial dependence to match or outperform the results of gradient-boosted trees. These results demonstrate that graph-based and spatially informed learning can enhance environmental prediction and provide a foundation for improved groundwater risk mapping and monitoring.

---


### 20. [Decodable but Not Detectable: A Leakage Fingerprint for Near-OOD Benchmarks](https://arxiv.org/abs/2607.19393)

**<font color=#1a73e8>作者：</font>** Vishnu Bindu Balachandran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While auditing a perturbation-based OOD detector on a document benchmark, we recorded an AUROC of 0.326 -- well below the 0.5 chance level. The cause is a benchmark leak: the designated "OOD" class is one the model was trained on, so its examples sit inside the in-distribution fit set and the detector is penalized for correctly ranking them as familiar. Deleting the class and retraining 35 models across two domains raises the score to 0.911. We distill the contamination into a leak fingerprint -- near-perfect supervised decodability (AUROC approximately 1) coupled with unsupervised detection collapsed below 0.65 -- and validate it on a controlled battery of 52 settings (20 leaked, 32 clean) across ResNet-50 and ViT-B/16 on CIFAR-10/100, achieving sensitivity 18/20 and specificity 31/32 in embedding space; the matched fit-set-exclusion controls are perfect at 20/20. An in-the-wild audit of 24 standard near/far OOD benchmark pairs fires on exactly one (the intrinsically hard CIFAR-100 vs CIFAR-10 pair) and on no far-OOD pair, confirming specificity and that standard cross-dataset construction is clean. Under the corrected protocol, perturbation signals are decodable but not detectable: a supervised reader recovers the OOD signal (AUROC 0.87-1.00) while no unsupervised detector does, and the perturbation method does not improve on plain Mahalanobis distance. We provide a theoretical account of why and, for transparency, retract an earlier circular correlation. The contributions are a corrected protocol and a validated leak diagnostic, not a new OOD method.

---


### 21. [Cross-Subject Semantic Decoding with Shared-Space Alignment for Generalized Neural Representation Learning](https://arxiv.org/abs/2607.19394)

**<font color=#1a73e8>作者：</font>** Ji-Hoon Heo, Aleksandra Joanna Wisniewska, Seo-Hyun Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generalizing across subjects remains challenging in invasive neural recordings because electrode configurations, anatomical structures, and neural signal patterns vary substantially across individuals. To investigate such inter-subject variability, we propose a cross-subject semantic decoding framework that aligns neural responses to speech perception from multiple subjects into a shared latent space and learns a mapping from the aligned neural representations to contextual embeddings. More specifically, using electrocorticography data collected during natural language comprehension, we estimate the shared space using the shared response model and train a decoder to predict contextual semantic embeddings from projected neural responses. For a held-out subject, we estimate a subject-specific projection into the predefined shared space, and directly apply the pretrained decoder without any retraining. Experimental results demonstrate that the proposed framework consistently outperforms baseline methods across evaluation settings and exhibits a reduced performance drop from source subject to held-out subject testing, indicating improved cross-subject generalization. These results suggest that aligning neural activity into a shared latent space, while decoding in a semantic embedding space, provides an effective strategy for improving cross-subject generalization by reducing subject-specific differences in neural responses while effectively capturing shared stimulus-related representations.

---


### 22. [From Trajectories to Prefixes: Reusing Teacher Trajectories via Replayed Prefixes and Online Continuation](https://arxiv.org/abs/2607.19395)

**<font color=#1a73e8>作者：</font>** Yihan Wang, Zhong Guan, Haoran Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Small language models are attractive backbones for interactive agents, but direct distillation from strong teacher trajectories often turns rich multi-turn behavior into one-shot imitation targets. This is inefficient in long-horizon environments, where early decisions shape later states and rewards. We propose Prefix-GRPO, a reinforcement learning framework that decomposes teacher trajectories into replay-aligned prefix queries and online continuations. Each prefix is replayed in the environment to recover a valid intermediate state, after which the student continues online interaction and receives task reward. Unlike response-only GRPO, Prefix-GRPO also applies clipped policy updates to historical assistant tokens inside the replayed prefix, using a policy-distilled SFT checkpoint to estimate their old log-probabilities. This unifies prefix learning and continuation learning within the same policy-optimization form. Experiments on TextCraft, BabyAI, and ALFWorld show that Prefix-GRPO improves small-model agents over distillation and standard RL baselines, while ablations show that replay alone is insufficient without explicit prefix-token optimization. The implementation and reproduction scripts are available at this https URL.

---


### 23. [CrackedPDFs: A Controlled Benchmark for Hidden Prompt Injection in PDFs](https://arxiv.org/abs/2607.19396)

**<font color=#1a73e8>作者：</font>** Pukaphol Thienpreecha  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Document-based LLM systems often flatten a PDF before guardrails inspect it. That step can discard evidence that an instruction was never visible to the user. We introduce CrackedPDFs, a controlled benchmark for hidden prompt injection in PDFs. The benchmark contains 29,322 generated PDFs from 4,983 base docu ments. It includes 9,774 injected files and 19,548 benign or matched-confounder files. We evaluate PromptGuard and a rule baseline. We also evaluate structural only learned models and a sanitized hybrid detector. The evaluation uses held-out provenance splits and paired benign-confounder controls. It also uses label-shuffle checks and shortcut audits. On a 2,919-document held-out test set, the hybrid de tector reaches 0.960 F1. ROC-AUC is 0.998 and PR-AUC is 0.997. It also ranks injected files above matched benign confounders in 95.9% of 973 pairs. Prompt Guard has low recall when given extracted text only. Structural-only learned mod els are weak under paired controls. A text-only TF-IDF model reaches perfect held-out scores but fails shortcut audits. These results show that document-aware hybrid detection is useful under controlled paired evaluation. They do not show broad real-world robustness or reliable cross-family generalization.

---


### 24. [Memory Merge DQN: Sensitivity Weighted Target Updates for Stable Value Learning](https://arxiv.org/abs/2607.19397)

**<font color=#1a73e8>作者：</font>** Adrian Ly, Richard Dazeley, Peter Vamplew 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep Q-networks use target networks to stabilise bootstrapped value learning, but the standard hard copy update also introduces a tradeoff. Holding the target network fixed, improves short term stability, yet each hard update abruptly replaces the target parameters with the newest online network and discards recent parameter history. This can produce sudden changes in the bootstrap target and may remove value function structure that remains useful later in training. This paper introduces Memory Merge DQN, a target network update mechanism that maintains a short memory of recent historical online network copies and constructs the target network by merging network parameters based on the Q-value sensitivity rather than copying only the newest online network. Memory Merge gives greater influence to parameters that remain locally important for current Q-value behaviour, while using a recency prior to keep the merged target close to the latest online parameters. The method is inspired by Fisher Weight Model Merging, but uses Q-value sensitivity rather than Fisher information as the weighting signal. This paper evaluates Memory Merge DQN on Atari environments against DQN, Averaged DQN, DQN with layer normalisation, and PQN (with gradient clipping). The results show that Memory Merge DQN is highly competitive and it achieves the largest number of first place final performance results among the evaluated methods, beats DQN, Averaged DQN, and PQN (with gradient clipping), and produces substantial gains in several games where preserving useful value-function parameters appears beneficial. These findings suggest that selectively merging recent parameter weights and history can improve the stability and final performance of DQN agents, and that target network design is an important mechanism for preserving useful value function structure during long horizon value learning.

---


### 25. [HyGRL: Adaptive Hybrid Graph Reasoning for Multi-Entity Questions](https://arxiv.org/abs/2607.19398)

**<font color=#1a73e8>作者：</font>** Junyi Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-entity compositional questions pose significant challenges to existing retrieval-augmented language models. Conventional methods fall into a dilemma: standard RAG lacks dynamic reasoning, traditional Graph-RAG is limited by structural sparsity, and LLM-constructed Graph-RAG incurs prohibitive costs. We propose \textbf{\fwa}, a unified framework that embeds unstructured text into structured knowledge graphs, creating a heterogeneous network for flexible evidence retrieval. Reasoning is formulated as adaptive structure induction, learned via a robust two-stage process: (1) imitation learning distills heuristic expert signals, and (2) reinforcement learning refines the policy using LLM-driven preference rewards. Experiments demonstrate that {\fwa} effectively merges textual richness with structural knowledge, outperforming SOTA baselines in answer accuracy and reasoning fidelity while maintaining extremely low token costs and near real-time inference((code available at this https URL) .

---


### 26. [When Does Consensus Beat Voting? A Critical Analysis of Statistical Label Fusion in Medical Image Segmentation](https://arxiv.org/abs/2607.19402)

**<font color=#1a73e8>作者：</font>** Renjie He  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper provides a rigorous, self-contained investigation of consensus segmentation. We derive the mathematical foundations from first principles -- the generative model, EM algorithm, Van Leemput's marginalization analysis, identifiability conditions, Spatial STAPLE, and deep variational formulations -- and validate each theoretical prediction through controlled experiments. The central finding is sobering: under common conditions, STAPLE reduces to thresholded majority voting, suffers 95% EM suboptimality, and collapses under class imbalance. These are not edge cases but typical scenarios in medical imaging. Majority voting -- simple, non-parametric, and robust -- is a surprisingly strong baseline that the field has perhaps too hastily dismissed in favor of more "sophisticated" methods. At the same time, the deep consensus model demonstrates that the consensus problem is not inherently difficult -- it becomes tractable when the image is used alongside the labels. And conformal prediction shows that formal uncertainty guarantees are achievable and practical. We hope this work encourages practitioners to critically evaluate their consensus methods rather than applying STAPLE by default, and provides the mathematical and empirical foundation for more principled approaches.

---


### 27. [Recovering Clinical Utility Under Differential Privacy: Empirical Validation of Adaptive Federated Aggregation on Heterogeneous Cardiovascular Datasets](https://arxiv.org/abs/2607.19403)

**<font color=#1a73e8>作者：</font>** Rodrigo Tertulino, Laercio Alencar, Ricardo Almeida  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Validating federated learning frameworks on real clinical data is an essential step between proof-of-concept demonstrations in controlled synthetic environments and deployment in real multicenter healthcare settings. A prior architectural study by the same authors (Tertulino and Alencar, 2026) demonstrated, on a synthetic six-feature benchmark, that server-side adaptive optimization acts as a temporal denoiser for Differential Privacy noise, answering an open challenge identified in the original pipeline work (Tertulino, 2025). That study used synthetically generated data and explicitly identified real-world validation as a priority future direction. The present work addresses this gap by validating the FedCVR framework on five publicly available real cardiovascular datasets (Framingham, Cleveland, Hungarian, Switzerland, and Long Beach VA), harmonized to the 13-attribute UCI Heart Disease schema and configured as a heterogeneous federated scenario with leave-one-institution-out cross-validation. Results demonstrate that FedCVR preserves its adaptive advantage on real data, achieving an F1-Score of 79.2% and AUC of 0.96 under the operational privacy budget (noise multiplier = 0.8, privacy budget epsilon approximately 4.2), while statistically outperforming standard FedAvg on all evaluated metrics (paired t-tests, all p <= 0.003, significant under the Bonferroni-corrected threshold). The measured privacy cost on real data confirms the graceful degradation pattern observed in the synthetic experiments, providing empirical evidence of the framework's clinical viability in genuine multicenter contexts.

---


### 28. [Structured Latent Space Modeling over Multi-Scale Temporal Patches for Multivariate Time Series Forecasting](https://arxiv.org/abs/2607.19404)

**<font color=#1a73e8>作者：</font>** Xingsheng Chen, Deyu Yi, Siu-Ming Yiu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multivariate time series encode structural patterns that unfold across multiple temporal scales, yet most forecasting backbones treat learned representations as transient byproducts of prediction, leaving the organizational geometry of these patterns underexploited. We introduce M2Patch, a CNN-based forecasting architecture that maps channel-independent multivariate observations into a structured latent space through two complementary differentiable constraints. Multi-scale patching decomposes the input into overlapping temporal granularities; depthwise separable convolutions with progressive dilation extract scale-specific features in linear time; and per-scale learned projections compress these features into a compact latent representation. The latent space is organized by an intra-scale smoothness constraint that enforces temporal continuity between adjacent patches, and an inter-scale alignment constraint, realized through learnable cross-scale mappings, that restores cross-granularity interaction within the channel-independent design, ensuring that all scales encode mutually consistent representations of the underlying dynamics. Experiments on ten real-world benchmarks show that M2Patch achieves 57 best and 34 second-best results across 40 forecasting settings, matching or exceeding representative baselines on most benchmarks while maintaining linear computational complexity and robustness to patch-level input corruption.

---


### 29. [Reproducing Recurrent Transformers: The CoTFormer](https://arxiv.org/abs/2607.19405)

**<font color=#1a73e8>作者：</font>** Aras Kavuncu, Bryan Vullo, Alberto Berni  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The CoTFormer architecture formalizes Chain-of-Thought as a form of recurrent latent computation, preserving intermediate states as attendable representations to mimic explicit reasoning traces. In this work, we evaluate CoTFormer and its structural variants across perplexity and compute efficiency metrics. Furthermore, we extend evaluation to controlled algorithmic settings to determine whether this recurrent framework improves out-of-distribution generalisation on inductive reasoning tasks.

---


### 30. [ITPEval: Benchmarking Formal Translation Across Interactive Theorem Provers](https://arxiv.org/abs/2607.19407)

**<font color=#1a73e8>作者：</font>** Jiayi Wu, Robert Joseph George, Anima Anandkumar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Formal theorem proving has emerged as a frontier challenge for machine learning, yet the ecosystem is fragmented: proofs remain siloed across incompatible systems, limiting both training data for learning-based provers and the portability of verified results. We present ITPEval, the first benchmark for evaluating automated formal proof translation across four major ITPs (Lean 4, Rocq, Isabelle, and HOL Light), spanning two distinct logical foundations. Our benchmark comprises 1,560 source files and 6,848 theorems organized into a controlled tier of axiomatized files that isolates foundational translation difficulty, and an ecosystem tier drawn from real libraries that exposes API and proof-style mismatches. We release itpeval, a unified multi-ITP verification infrastructure with state-isolated warm backends that preserve per-artifact native checking semantics. We evaluate both statement and proof translation across five frontier and open-weight LLMs on 12 directed translation pairs: statement translation peaks at 29.1% pass@1 and proof translation at 10.5%; controlled theorems reach 29.7% proof pass@1 versus 5.2% for ecosystem-level translations, confirming that library mismatch is the dominant bottleneck. In addition to pass@k evaluation, a deterministic Lean 4 BEq check establishes equivalence for 54.0% of verified source-to-Lean 4 miniF2F statement translations, showing that native type-checking alone can substantially overestimate semantic fidelity; in an autoformalization/auto-informalization round-trip study, Rocq and HOL Light are easier formalization targets than Lean 4 and Isabelle, while multi-ITP context improves pooled Lean 4 success from 4.8% to 10.6%. Our benchmark, verification infrastructure, and evaluation pipelines are publicly released.

---


### 31. [Adaptive Multi-Expert Graph Transformer for Interpretable EEG-Based Diagnostics](https://arxiv.org/abs/2607.19429)

**<font color=#1a73e8>作者：</font>** Maryam Rahimimovassagh, Md Elias Hossain, Ivan Garibay 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalographic (EEG) abnormalities arise from dynamic changes in neural synchrony across spatial and temporal scales, yet many computational approaches reduce these dynamics to static features. We present a Spatial Multi-Expert Graph Transformer that models each EEG recording as a sequence of dynamic functional connectivity graphs. Time-resolved connectivity is estimated using the weighted Phase Lag Index (wPLI), and hierarchical graph encoding aggregates information from electrode to regional and global levels. A multi-expert transformer architecture enables subtype-aware reasoning, with a gating mechanism adaptively fusing expert outputs for global abnormality prediction. Experiments on the TUAB dataset show competitive abnormal EEG detection performance and demonstrate the potential of dynamic graph modeling with adaptive expert fusion for interpretable, subtype-aware spatial--temporal analysis.

---


### 32. [ChainWatch: A Kill Chain-Aligned Sequential Detection Framework for Multi-Step Attacks in MCP-Based AI Agent Systems](https://arxiv.org/abs/2607.19432)

**<font color=#1a73e8>作者：</font>** Om Narayan, Rashmi Jyoti, Ramkinker Singh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Model Context Protocol (MCP) is an open-source standard that allows AI agents to connect to external tools, databases, and services. While this connectivity enables powerful agent capabilities, it also introduces multi-step attacks that existing per-call defenses cannot reliably detect. Attackers can compose individually benign tool invocations into malicious sequences that evade isolated inspection. This paper presents ChainWatch, a sequential detection framework for identifying multi-step attacks in MCP-based AI agent systems. ChainWatch models attack progression using a six-stage kill chain and applies a Hidden Markov Model (HMM) to classify tool-call sequences. Detection rules are triggered when a session exhibits suspicious progression across multiple stages. The framework is supported by a structured threat model covering direct sequential attacks, indirect prompt injection chains, and hybrid multi-stage attacks. A 20-dimensional feature extraction schema captures behavioral signals from tool interactions. We demonstrate the approach using five representative attack scenarios from the security literature, showing how ChainWatch detects attack chains that evade traditional per-call security mechanisms.

---


### 33. [Building Trust in Autonomous Commerce: A Verifiable Global Event Timeline and AI-Ready Fraud Intelligence Layer](https://arxiv.org/abs/2607.19436)

**<font color=#1a73e8>作者：</font>** Rajat Srivastava  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic commerce protocols such as AP2 and ACP define mechanisms for secure agent-initiated transactions but do not provide interoperable, tamper-evident auditability or verifiable temporal ordering of events across heterogeneous domains. This paper addresses these gaps by proposing a verifiable global event timeline for agentic commerce, constructed from four core components: canonical event schemas that enforce deterministic serialization, deterministic batch formation ensuring reproducible ordering without reliance on synchronized clocks, Merkle-based append-only commitments providing logarithmic-cost inclusion proofs, and blockchain anchoring establishing a tamper-evident temporal backbone. Building on this infrastructure, we introduce a cryptographically signed fraud marker that binds risk labels to anchored evidence through an unforgeable provenance chain, and a dataset lineage model enabling reproducible, tamper-evident AI training pipelines. Empirical results from a prototype implementation demonstrate: Merkle tree construction processes 50,000 events in 47 milliseconds; end-to-end verification completes in under 0.013 milliseconds regardless of batch size; inclusion proof sizes grow logarithmically from 320 bytes at 1,000 events to 512 bytes at 50,000 events; and Merkle-based verification outperforms linear scan by 14.4x at 50,000 events.

---


### 34. [How Far Can Wearable-Compatible Signals Go? A Controlled Decomposition of Non-EEG Sleep Staging](https://arxiv.org/abs/2607.19441)

**<font color=#1a73e8>作者：</font>** Yi Wang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Consumer wearables increasingly infer sleep stages from signals including heart rate, accelerometry, and photoplethysmography. However, existing studies often report end-to-end performance under a fixed signal setting, making it difficult to determine whether the observed performance comes from genuine physiological decoding, temporal priors, or dataset-specific confounds. To address this limitation, we introduce a four-layer controlled decomposition framework for non-EEG sleep staging, covering signal source, physiological representation, temporal prior, and decision layers. The framework is evaluated across a signal-quality ladder spanning Apple Watch Sleep-Accel ($N=31$), the Sleep Heart Health Study ($N=195$, laboratory ECG, respiratory, and SpO$_2$ signals), and Sleep-EDF-20 as an EEG+EOG reference, using the same compact Mamba2 model throughout. Laboratory cardiorespiratory signals reach $\kappa=0.492$, while EEG+EOG reaches $\kappa=0.796$, leaving a residual gap of $\Delta\kappa=+0.304$ that reflects missing cortical information rather than temporal modeling alone. Consumer HR/ACC reaches only $\kappa=0.255$, quantifying the additional penalty of derived wearable signals and real-world sensing constraints. Confidence-based abstention provides a calibrated operating mode: removing the 20% lowest-confidence epochs increases $\kappa$ from $0.452$ to $0.512$, while a label-shuffled control collapses to $\kappa=-0.003$. These results support non-EEG sleep staging as coarse, confidence-aware sleep-structure monitoring rather than EEG-equivalent five-class clinical staging.

---


### 35. [Unlearning as Distribution Restoration: A Controlled Counterfactual Study, a Validated Selective Screen, and the Limits of Oracle-Free Certification](https://arxiv.org/abs/2607.19442)

**<font color=#1a73e8>作者：</font>** Sen Yang, Yuen-Hei Yeung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine unlearning is commonly evaluated by matching a retrained oracle on trained probes. In a controlled nonce-fact testbed with a matched retraining reference, we find this criterion can favor methods that retain held-out knowledge: candidates it rates adequate score held-out forget facts $-2.82$ nats below the never-learned level (cluster CI $[-3.16,-2.48]$). We recast unlearning as restoration to the matched reference and audit oracle-free screens and certificate-style criteria across 45 model-seed cells spanning five open architecture families. The reference itself falsifies an absolute retain/round-trip certificate: the injected model, which retains the retain set by construction, fails the fixed retain threshold in 41/45 cells and its own round trip in 31/45, and the reference fully certifies in only 1/45. A base-anchored held-out screen remains strong as a selective necessary test: on a sealed challenge suite it rejects the injected model in 45/45 cells, accepts the reference in 44/45, and partially detects entity-routing suppression (35/45); it is a necessary test with measured sensitivity, not a sufficiency certificate. A damage-relative recalibration anchored to the reference's own operating point certifies a small subset in 15/45 cells; where it does not abstain, its picks lie within retraining noise (0.80 nats) on the axes it optimizes, while the common trained-probe criterion sits 5.17 nats away (a supporting comparison, not a head-to-head benchmark). A fixed-magnitude logit-suppression attack defeats the full forward battery in 12/45 cells, so forward-only certification is not sound; our method is an empirical selective test for methods-as-produced. An identifiability theorem delimits which facts admit an oracle-free forget threshold at all, with TOFU as the predicted boundary case.

---


### 36. [Marine Engine Fault Dataset: Open-Access Data under Controlled Reference and Fault Scenario Conditions](https://arxiv.org/abs/2607.19444)

**<font color=#1a73e8>作者：</font>** Ahmad BahooToroody, Oleksiy Bondarenko, Mohammad Mahdi Abaei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Open-access datasets for marine-engine predictive maintenance remain scarce, particularly those from controlled fault experiments with documented operating conditions, subsystem-level interventions and system-level measurements. This work presents the Marine Engine Fault Dataset, an openly available dataset from a turbocharged, intercooled three-cylinder marine diesel engine operated on a testbed under both reference and fault-scenario conditions. The experimental campaign combined a reference-performance program across the 30-90% load range with scenario-based tests in which abnormal conditions were introduced after stabilized fault-free operation, enabling controlled comparison between baseline and fault-affected behaviour. Five anomaly classes were implemented through physical interventions affecting major engine subsystems: cooling-water pump cavitation, compressor air-filter clogging, air-cooler fouling, injection-valve nozzle clogging and turbine degradation induced through increased exhaust-side restriction. The released data comprise multi-sensor time-series of operating, thermal, pressure, flow and combustion-related variables, with a separate reference-performance record and metadata for structured reuse. Technical validation shows that the reference measurements remain physically coherent across the operating range and that the imposed anomalies produce interpretable response patterns consistent with the affected subsystems, including progressively distinguishable behaviour where different severities were implemented. By combining controlled fault realization, multi-load operation and system-level measurements within a real marine-engine platform, the dataset provides a well-documented benchmark for anomaly detection, fault diagnosis, degradation modelling and related condition-monitoring studies in maritime machinery.

---


### 37. [Intelligent Disruption: Undetectable Attacks on Wireless Autoencoders](https://arxiv.org/abs/2607.19448)

**<font color=#1a73e8>作者：</font>** Han Jiang, Jifa Zhang, Hu Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Adversarial attacks can degrade the legitimate decision performance in wireless autoencoder communications. However, in complex scenarios with multiple adversaries, the cumulative leakage interference (CLI) caused by the multiple parallel attacks increases the chance of detecting the attacks, while dynamical environments also make the fixed attack strategies difficult to have stable effectiveness. To jointly enhance the undetectability, aggressivity and adaptability of adversarial attacks, we propose a deep learning based intelligent attack framework. Specifically, considering the CLI caused by the multiple parallel attacks, a deep neural network based transmit power control is established to reduce the interference leakage by regulating the transmit power of these adversaries, thereby improving the undetectability. Furthermore, to enhance the attack effectiveness and stability in the dynamic environment, the conditional generative adversarial attack is further developed. The generator takes the attack channel information as the conditional input to produce the perturbating signals to mislead the discriminator by making the attacked received signals resemble the clean received signals, while the discriminator distinguishes between the two under the same condition. Through the adversarial training, the generator can learn to create adaptive perturbating signals with enhanced attack performance. Simulation results demonstrate that the proposed framework outperforms benchmarks in terms of attack undetectability, aggressivity and adaptability.

---


### 38. [Predictive Extrema, Unprofitable Policies: An AI-Assisted Audit of Candle-Based Binance Spot Timing Models](https://arxiv.org/abs/2607.19453)

**<font color=#1a73e8>作者：</font>** Ayoub Jadouli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We audit whether candle-based machine-learning models can turn predictions of cryptocurrency extrema or short-horizon outcomes into positive Binance Spot paper policies after assumed costs. Numerical results come from scripted fixed-seed model runs and deterministic simulators; human-supervised AI agents supported the July 20 evidence-integrity revision through literature retrieval, separately tasked critique, artifact reconciliation, documentation, and source packaging, not trading decisions. The strongest later-period evidence, conditional on extensive predecessor search, is negative: an unchanged ten-pair mandatory-daily selector lost 6.72\% over 19 July cycles at an assumed 31-bps completed-cycle cost, with 3 wins and 16 losses. In short model-specific July evaluations, the validation-selected local-minimum policy returned -1.79\%, while the local-maximum sell-to-cash/re-entry policy underperformed continuous holding by 2.80\%; their gross mean advantages of 11.11 and 12.21 bps were below even the 21-bps stress. A Gurgul-inspired, OHLCV-only daily adaptation attained minimum/maximum ROC AUC of 0.874/0.896 but average precision of only 0.134/0.116 and lost 44.30\% over seven cycles, versus -41.20\% for buy-and-hold. A forensic audit also downgraded an earlier One4All "30-day holdout": its dates had influenced prior architecture work, its four-hour outcome horizon was not purged at split boundaries, it used same-close entry, and its raw result directories were absent. Across the tested, mostly exploratory protocols, event-ranking performance did not establish positive executable policy value. Every operational decision remains NO\_TRADE.

---


### 39. [Generating Bearing Vibration Signals at User-Specified Fault Probabilities Using PR-GAN and Counterfactual Methods](https://arxiv.org/abs/2607.19455)

**<font color=#1a73e8>作者：</font>** Seyed Mohammadreza Alavi, Ardeshir Shojaeinasab, Reza Jalayer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In bearing vibration datasets, most samples receive predicted fault probabilities close to 0 or 1, while samples with intermediate (gray-zone) probabilities are rare. Such borderline samples are important because they reflect conditions in which maintenance decisions may require additional inspection or a conservative response and are useful for studying decision boundaries. To address this scarcity, this paper proposes and compares two approaches that generate vibration signals whose predicted fault probability matches a target probability of 0.25, 0.50, or 0.75. We use the average output of a heterogeneous ensemble classifier with different architectures and random initializations as a fixed, gradient-accessible probability oracle. The first, training-based approach, Probability-Regularized Generative Adversarial Network (PR-GAN), extends Wasserstein Generative Adversarial Network with Gradient Penalty (WGAN-GP) and edits a real signal through a residual generator while pushing the classifier output toward the target probability. The second is a training-free, per-sample Wachter-style counterfactual (CF) procedure that directly optimizes each input signal to reach the target probability while remaining close to the source signal. We evaluate both methods on the Case Western Reserve University (CWRU) and Paderborn bearing datasets using mean absolute target-probability error, time-domain total variation, and frequency-domain log power spectral density (log-PSD) differences. Across all settings, CF reaches the target with a mean absolute probability error of 0.005-0.008 and a within-tolerance success rate of 1.000 on retained samples, whereas PR-GAN's mean error is 0.046-0.059 with success rates between 0.501 and 0.680. CF therefore steers the probability more reliably and requires smaller average L1 changes, whereas PR-GAN has a lower reported runtime in most settings.

---


### 40. [MoA-Structured Decode Attention DNF Derivation, KV-Cache Accumulation, GQA/MQA, and OpenACC Kernel](https://arxiv.org/abs/2607.19456)

**<font color=#1a73e8>作者：</font>** Lenore Mulin, Gaetan Hains  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We derive four memory-optimal inference artifacts for transformer attention using the Mathematics of Arrays (MoA), each following directly from the forward-pass Denotational Normal Form (DNF) of with the query-row index fixed to the current decode step. The artifacts are: (1)~a single-query decode DNF in which the $\psi$-reduction eliminates the $K^\top$ buffer algebraically, achieving $(d_k + nd_k+ nd_v+ d_v)\times4\,{B}$ Dynamic Random Access Memory (DRAM) traffic result numerically verified to $\|{err}\|_\leq2\times10^{-7}$; (2)~a C/OpenACC Graphics Processing Unit (GPU) kernel with Operational Normal Form (ONF) stride arithmetic and hardware-coalesced memory access, verified to $\|\mathrm{err}\|_\infty=0$ (exact IEEE-754 floating-point arithmetic); (3)~a multi-step KV-cache with $O(d_k+d_v)$ per-step append via MoA concatenation $\#$; and (4)~Grouped-Query Attention (GQA) and Multi-Query Attention (MQA) derived via $\psi$-selection, achieving a proven $\frac {h_q} { h_{kv} }$ reduction in KV traffic. All programs are verified against PyTorch scaled_dot_product_attention.

---


### 41. [Detect Early, Escalate Rarely: Anytime Detection of AI-Generated Video from the Compressed Bitstream](https://arxiv.org/abs/2607.19476)

**<font color=#1a73e8>作者：</font>** Mert Onur Cakiroglu, Mehmet Dalkilic, Hasan Kurban  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detectors for AI-generated video are evaluated offline. A clip is decoded to pixels and scored once, increasingly by a large vision-language model. Detection, however, is deployed online. We recast the task as streaming perception and score the motion field the codec already wrote into the bitstream. Reading that field is a parse, not a pixel-domain forward pass. Because the running aggregate is monotone, one end-calibrated threshold is anytime-valid at the data-dependent decision time. Recalibrating at each prefix is not. Escalation is priced in closed form. A compute budget maps to a deferral window, on a frontier monotone exactly where the deferral condition holds. On matched GenVidBench the codec stage reaches full-length AUC 0.64 at five orders of magnitude less compute than a pixel CNN, on CPU. Its gate holds the stopping-time false-positive rate at target while the real data match its calibration, and drifts above it under distribution shift. Deferring 15% of clips lifts accuracy from 0.75 to 0.78 at $7\times$ less compute (paired: McNemar $p<10^{-6}$). The stage-1 ordering replicates on AIGVDBench. We introduce no new detector. The contribution is the reframing, two guarantees, and the measured frontiers. Code, configurations, and evaluation splits: this https URL.

---


### 42. [Total Variation Distance Estimation in Autoregressive Models](https://arxiv.org/abs/2607.19510)

**<font color=#1a73e8>作者：</font>** Eric Price, Kevin Tian, Zhiyang Xun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern LLM deployments use a number of implementation choices and inference optimizations (e.g., batching, custom kernels, and quantization) on top of fixed weights, so two engines serving "the same model" can produce meaningfully different distributions. We study the problem of estimating the total variation (TV) distance between two length-$n$ autoregressive distributions to additive error $\varepsilon$, under three access models. (1) Under sample access, we use $\widetilde{O}(n^2 K/\varepsilon^2)$ queries, where $K$ is the maximum support of the next-token distribution. This improves upon the $\widetilde{O}(n^3 m/\varepsilon^5)$-query estimator of Meel et al. (2025), where $m \geq K$ is the total size of the token alphabet. (2) Under logit access, we use $O(n/\varepsilon^2)$ queries, and this is tight. (3) Under noisy logit access, we smoothly interpolate between the above two guarantees: if probability values are given to relative error $\sigma$, we use $\widetilde{O}((n+n^2\sigma^2)/\varepsilon^2)$ queries. We complement our theoretical results with an empirical evaluation of our algorithms, for example measuring the distance between SGLang and vLLM serving identical weights. Our experiments highlight the robustness and practicality of estimating the total variation distance, which remains estimable where the KL divergence is infinite. Our code is available at this https URL.

---


### 43. [Do Sheaf Neural Networks Use Holonomy? A Measure--Intervene--Control Study](https://arxiv.org/abs/2607.19514)

**<font color=#1a73e8>作者：</font>** Ankit Grover, Rémi Bourgerie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Geometric architectures are often justified by internal mechanisms such as rotations, yet task performance alone cannot show whether those mechanisms drive predictions. Using sheaf neural networks (SNNs) as a testbed, we introduce the first basis-independent measurement of trained triangle-loop products, separating rotation, stalk-space area, and orientation. In a custom high-homophily GraphUniverse regime, Neural Sheaf Propagation (NSP) increases the triangle-weighted mean two-dimensional SO(2) loop rotation from 0.010 to 0.388 radians for triangle counting, while the community-detection comparison ends at 0.029 radians. Across the training-set-size experiment, replacing all learned SO(2) transports with identities sharply increases test error, establishing post-training sensitivity to the complete learned connection. However, a graph-summary ridge predictor is more accurate, diagonal maps also improve, and fixed-degree graphs develop increasing rotation without outperforming the training-mean predictor. This measure-intervene-control study separates geometric change, connection sensitivity, and evidence for triangle-specific computation.

---


### 44. [Crowd4D: Scene-Aware Monocular 4D Crowd Reconstruction](https://arxiv.org/abs/2607.19517)

**<font color=#1a73e8>作者：</font>** Hongbo Kang, Tianyi Zhou, Qingyang Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering scene-consistent 4D crowd motion from monocular video in large-scale scenes remains challenging due to severe depth ambiguity and complex scene geometry. Existing monocular crowd reconstruction methods typically rely on single-plane assumptions, leading to unreliable metric scale and spatial drift under complex terrain. We propose Crowd4D, the first scene-aware 4D crowd reconstruction framework that jointly optimizes the crowd and scene from a monocular RGB video in large-scale scenes. Crowd4D explicitly incorporates scene geometry and ensures consistency across image and scene spaces via a multi-stage optimization strategy. A key bottleneck of this task lies in accurate human-scene alignment, particularly in scale and position. However, human and scene reconstructions are typically decoupled. To address this, we introduce the Human-Scene Interaction Proxy, abbreviated as HSIP, as an intermediate representation derived from Scene Interaction Point Clouds and a Scene Interaction Surface, abbreviated as SIPC and SIS. These representations encode explicit scene-aware geometric priors and redefine the optimization space for large-scale monocular 4D crowd reconstruction. To further improve temporal stability under occlusions, we introduce Crowd Structural Coherence Regularization, abbreviated as CSCR, which leverages HSIP-based spatial priors to impose soft temporal consistency on pairwise relative displacements and directions within local crowd neighborhoods. Extensive experiments demonstrate that Crowd4D consistently outperforms existing state-of-the-art methods and enables robust monocular 4D crowd reconstruction in complex, large-scale real-world scenes.

---


### 45. [Sophisticated Policies from Epistemic Priors](https://arxiv.org/abs/2607.19518)

**<font color=#1a73e8>作者：</font>** Wouter W. L. Nuijten, Bert de Vries  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sophisticated Inference is a variant of active inference often associated with recursive belief modeling and tree search. We argue that its central computational role is simpler: within a planning horizon, it makes active inference closed-loop by allowing future actions to depend on future states and observations. This closed-loop structure can be represented in the epistemic-prior variational free energy framework. Epistemic priors supply the active-inference objective, while a joint posterior over future states and actions supplies the state-contingent control structure. We evaluate this decomposition in the Reactivity Maze, a stochastic benchmark designed to separate epistemic incentive from inner-horizon closed-loop control. The comparison includes three variational objectives with the same state-action posterior family, an action-state factorized active inference objective, Sophisticated Inference, and standard Expected Free Energy planning. The results show that neither ingredient is sufficient on its own. Methods without an epistemic component do not seek information, while methods that prevent future actions from depending on future states cannot turn information into reliable goal-reaching. By contrast, both Sophisticated Inference and full-joint epistemic-prior active inference solve the environment by combining epistemic drive with closed-loop inference. These results show that the advantage associated with Sophisticated Inference need not be specific to tree search itself. It arises from the closed-loop form of active inference, and this form can be represented in epistemic-prior variational inference when the posterior keeps future actions dependent on future states.

---


### 46. [Geospatial Diffusion-based Evolution Synthesis (GeoDES) for Storm-Centered Weather Augmentation](https://arxiv.org/abs/2607.19522)

**<font color=#1a73e8>作者：</font>** Sonia Cromp, Satya Sai Srinath Namburi GNVV, Youran Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While machine learning-based weather models hold significant promise, they struggle to predict the detailed structure of large-scale weather systems such as cyclonic storms. Regional models are constrained by limited historical records within fixed geographic boundaries, while global models are computationally expensive and often operate at resolutions too coarse to capture fine-grained storm dynamics. To bridge this gap, we introduce the Geospatial Diffusion-based Evolution Synthesis (GeoDES) model, a custom image-to-video diffusion model. By focusing generation strictly on the evolving storm structure, GeoDES synthesizes physically consistent, high-fidelity weather events suitable for stress-testing forecast models and expanding meteorological datasets. Evaluations demonstrate that GeoDES outperforms prior methods on key metrics, achieving $52\%$ lower Peak Vorticity Error and $8\%$ higher Anomaly Correlation Coefficient than the next strongest methods on the North Atlantic test set.

---


### 47. [SynPre-FL: Synthetic data-driven pretraining integrated Federated Learning training framework](https://arxiv.org/abs/2607.19524)

**<font color=#1a73e8>作者：</font>** Akarsh K Nair, Muhammad Arifur Rahman, Nicholas Shopland 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) offers a promising approach to privacy-preserving clinical risk prediction, but its deployment remains limited by restricted data sharing, client heterogeneity, class imbalance, and the lack of realistic tabular electronic health record (EHR) benchmarks. Synthetic data generation may alleviate data scarcity, yet its integration with federated optimisation has received limited systematic study. We propose SynPre-FL, a unified framework combining high-fidelity synthetic EHR generation with synthetic-pretrained FL for robust prediction under non-IID conditions. A latent autoencoder-diffusion model generates privacy-preserving synthetic cohorts, which are used to warm-start federated training. This pretraining is followed by heterogeneity-aware optimisation using class-balanced local objectives, proximal regularisation, and adaptive server aggregation. Post-hoc calibration and federated-safe explainability support reliable and interpretable risk estimates. Experiments show that the synthetic generator preserves univariate, bivariate, and multivariate structure while protecting against membership-inference and reconstruction attacks. The generated data achieve strong downstream utility under TSTR, TRTS, and model-based evaluations. Across federated settings with 5, 10, and 15 heterogeneous clients, SynPre-FL consistently improves robustness and scalability over baseline methods, especially under severe non-IID fragmentation. Calibration improves probability reliability, while SHAP analysis produces stable and clinically coherent feature attributions across federation sizes. SynPre-FL therefore provides a practical and reproducible framework for combining synthetic data with FL to enable privacy-aware, interpretable, and robust clinical prediction from distributed tabular EHR data.

---


### 48. [The C-index illusion: discrimination without calibration in published survival models](https://arxiv.org/abs/2607.19526)

**<font color=#1a73e8>作者：</font>** Rafael da Silva, Danilo Alvares  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> "Stop Chasing the C-index when Evaluating Survival Analysis Models" (ICML 2026, Spotlight) argued normatively, on synthetic data, that evaluating survival models by discrimination alone, i.e. the concordance index, produces systematically misleading model comparisons, because the metric ignores calibration and time-dependent accuracy. Whether this matters for real, published, non-clinical models has not been tested. We reproduce three published survival-ML models across three structurally distinct domains (hard-drive failure, peer-to-peer credit default, and user disengagement on digital platforms), validate our evaluation instrument against the anchor paper's own synthetic experiment, and test five pre-registered hypotheses under a Holm-corrected family-wise error rate. Three of five reject. A model that reproduces the published discrimination almost exactly (C = 0.9595 vs. 0.958 reported) fails a formal calibration test at p = 2.6e-136; a broad feature-ablation search finds no single attribute responsible for this discrimination, so the calibration failure is not an artifact of a trivial shortcut. A lender's estimated default risk is biased upward by roughly two percentage points, growing to nearly four points in the riskiest segment, when loan prepayment is treated as non-informative censoring rather than as a competing risk. A platform's churn model shows probability estimates that degrade with the prediction horizon even as its global discrimination stays within the pre-registered C-index band. A direct test of whether metric choice inverts which model is preferred does not reject, though with limited power given only two to three models per domain; the failure mode we document is better characterized as misplaced confidence in a chosen model than as choice of the wrong one. We release a reusable, pre-registered evaluation harness with full code and a single annotated notebook.

---


### 49. [Synthetic and Derived Training Images for Campus Waste Detection: A Multi-Seed Evaluation with YOLOv8n](https://arxiv.org/abs/2607.19535)

**<font color=#1a73e8>作者：</font>** Ali Behbahani, Newsha Javanmardi, Shahriar Ahmed 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Incorrect disposal can contaminate campus recycling streams, and a bin-mounted camera could provide feedback as an item is discarded. We evaluated whether synthetic and derived images improve a YOLOv8n detector for this view. The real dataset contained 148 campus photographs: 86 for training, 31 for validation, and 31 for testing. Twelve joint-training configurations varied the amount and source of added images. We repeated seven principal settings with four matched seeds and computed bootstrap percentile intervals over those seeds. The real-only model reached a mean mAP@0.5 of 0.691 [0.665, 0.722]. Background replacement reduced the mean to 0.560 [0.499, 0.619], isolated-object images gave 0.680 [0.644, 0.724], and the full augmentation pool gave 0.487 [0.438, 0.537]. We also tested hand-and-forearm composites because every real photo showed a held object. Two cutouts in the initial composite set came from test photographs, so we discarded that experiment, rebuilt the set with training-split cutouts, and reran all four seeds. The corrected paired difference was +0.034 [-0.063, 0.199], which does not support a reliable hand-composite effect. Single-seed transfer experiments produced source-dependent rankings between joint mixing and sequential pretraining. None of the evaluated configurations exceeded the real-only baseline. The reported intervals quantify seed variation; the 31-photo test set remains too small for strong class-specific conclusions.

---


### 50. [When HTTP 402 Meets the Blockchain: Risks on Emerging x402 Payments](https://arxiv.org/abs/2607.19545)

**<font color=#1a73e8>作者：</font>** Qinying Wang, Yong Yang, Yuan Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> x402 is an emerging payment protocol for Web APIs and autonomous AI agents. x402 extends HTTP 402 with a payment negotiation flow and delegates payment proof verification and on-chain settlement to third-party facilitators. As a result, facilitators serve as a shared payment infrastructure for many independent merchants. This centralizes trust and validation in one component, so a single flaw can affect many services. Despite rapid adoption by major vendors and economically meaningful mainnet activity, the security posture of real-world x402 deployments remains poorly characterized.
We present the first systematic study of authorization correctness and execution safety in current facilitator-mediated x402 deployments in the wild, identifying eight security rules for facilitators as critical payment infrastructure. Based on our analysis of rule violations, we derive four new attack vectors, including Free Shopping, Asset Theft, Service Denial, and Gas Abuse. These attacks exploit weaknesses in the real-world facilitator and server implementations and cause severe harm, including direct financial loss to merchants, theft of facilitator-held assets, unbounded sponsor-paid gas/fees, and disruption of payment services. To assess the security of x402 deployments at scale, we propose a semi-automated black-box tool and apply it to 15 major x402 facilitators collectively used by over 60K sellers and 360K buyers. Alarmingly, we find violations in all evaluated facilitators. We responsibly disclosed our findings to the affected parties, who acknowledged the issues and adopted mitigations, including changes by Coinbase. Finally, we complement our controlled testing with an empirical measurement of over 119 million recent Base and Solana transactions, quantifying x402 adoption, facilitator centralization, and ecosystem-level risk indicators.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-192](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
