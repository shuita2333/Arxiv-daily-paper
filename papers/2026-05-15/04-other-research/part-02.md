# 📦 其他研究 | 2026年05月15日

> 本类共 **328** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-328](./part-07.md)

---

### 51. [Constraint-Aware Flow Matching: Decision Aligned End-to-End Training for Constrained Sampling](https://arxiv.org/abs/2605.12754)

**<font color=#1a73e8>作者：</font>** Jacob K. Christopher, James E. Warner, Ferdinando Fioretto  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep generative models provide state-of-the-art performance across a wide array of applications, with recent studies showing increasing applicability for science and engineering. Despite a growing corpus of literature focused on the integration of physics-based constraints into the generation process, existing approaches fail to enforce strict constraint satisfaction while maintaining sample quality. In particular, training-free constrained sampling methods, while providing per-sample feasibility guarantees, introduce a fundamental mismatch between the training objective and the constrained sampling procedure, often leading to performance degradation. Identifying this training-sampling misalignment as a central limitation of current constrained generative modeling approaches, this paper proposes Constraint-Aware Flow Matching, a novel end-to-end framework that explicitly incorporates constraint projections into the training objective. By aligning the model's learned dynamics with the constrained sampling process, the proposed method mitigates distributional shift induced by projection-based corrections, enabling high-quality constrained generation. The proposed approach is evaluated on three challenging real-world benchmarks, illustrating the generality and efficacy of the method.

---


### 52. [State-Centric Decision Process](https://arxiv.org/abs/2605.12755)

**<font color=#1a73e8>作者：</font>** Sungheon Jeong, Ryozo Masukawa, Sanggeon Yun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language environments such as web browsers, code terminals, and interactive simulations emit raw text rather than states, and provide none of the runtime structure that MDP analysis requires. No explicit state space, no observation-to-state mapping, no certified transitions, and no termination criterion. We introduce the State-Centric Decision Process (SDP), a runtime framework that constructs these missing inputs by having the agent build them, predicate by predicate, as it acts. At each step the agent commits to a natural-language predicate describing how the world should look, takes an action to make it true, and checks the observation against it. Predicates that pass become certified states, and the resulting trajectory carries the four objects language environments do not provide, namely a task-induced state space, an observation-to-state mapping, certified transitions, and a termination criterion. We evaluate SDP on five benchmarks spanning planning, scientific exploration, web reasoning, and multi-hop question answering. SDP achieves the best training-free results on all five, with the advantage widening as the horizon grows. The certified trajectories additionally support analyses unavailable to reactive agents, including per-predicate credit assignment, failure localization, partial-progress measurement, and modular operator replacement.

---


### 53. [Predicting Channel Closures in the Lightning Network with Machine Learning](https://arxiv.org/abs/2605.12759)

**<font color=#1a73e8>作者：</font>** Simone Antonelli, Vincent Davis, Harrison Rush 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Lightning Network (LN) is a second-layer protocol for Bitcoin designed to enable fast and cost-efficient off-chain transactions. Channels in the LN can be closed either by mutual agreement or unilaterally through a forced closure, which locks the involved capital for an extended period and degrades network reliability. In this paper, we study the problem of predicting channel closure types from publicly available gossip data, framing it as a temporal link classification task over the evolving channel graph. We construct a dataset spanning over two years of LN activity and benchmark a range of machine learning approaches, from MLPs to temporal graph neural networks and spectral encodings. Our experiments reveal that the dominant predictive signals are temporal and behavioural, namely how recently each endpoint was active and the per-node history of past closures, while the surrounding network topology provides no additional benefit. We find that a simple MLP operating on edge-level features, node-level event counts, and temporal patterns outperforms all graph-based approaches, and discuss how the inherent privacy of the LN, where critical information such as channel balances and payment flows remains hidden, fundamentally limits the predictability of closures from gossip data alone. We publicly release the dataset and code at this https URL to encourage further research on this practically relevant task.

---


### 54. [Multi-Quantile Regression for Extreme Precipitation Downscaling](https://arxiv.org/abs/2605.12762)

**<font color=#1a73e8>作者：</font>** Hamed Najafi, Gareth Lagerwall, Jayantha Obeysekera 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep super-resolution networks for precipitation downscaling achieve strong bulk skill yet systematically under-predict the heavy-tail events that drive flood risk. We demonstrate that the primary obstacle is the loss function, not the data: under intensity-weighted MAE, real and synthetic labels at the same input are simply averaged, meaning data augmentation shifts the predicted mean rather than the conditional distribution. We resolve this with Q-SRDRN, a multi-quantile super-resolution network trained with pinball loss at tau in 0.50, 0.95, 0.99, 0.999. Two CNN-specific design choices make this practical: IncrementBound enforces monotonicity while preserving each quantile channel's gradient identity, and separate per-quantile output heads provide independent filter banks for bulk and tail detection. Under this design, data augmentation via cVAE becomes complementary: the median head absorbs synthetic patterns without contaminating upper quantiles. Empirically, on Florida (convective/tropical-cyclone dominated), the un-augmented Q-SRDRN P999 head detects 1,598 of 2,111 events at 200 mm/day versus 88 for the deterministic baseline--an 18x detection-rate gain (4.2% to 75.7%)--with 63% lower KL divergence and 3.9% lower RMSE. Adding cVAE-generated samples lifts the P50 channel from 14 to 1,038 hits at 200 mm/day. On California (atmospheric-river dominated), the architecture reaches near-perfect detection (P999 SEDI >= 0.996 through 300 mm/day). On Texas, the baseline catches only 2 of 10,720 events at 200 mm/day while the P999 head catches 8,776 (81.9%). While the cVAE does not transfer across regions, multi-quantile regression captures extremes wherever the large-scale signal is strong, while augmentation rescues the median where it is not.

---


### 55. [State-Space NTK Collapse Near Bifurcations](https://arxiv.org/abs/2605.12763)

**<font color=#1a73e8>作者：</font>** James Hazelden, Eric Shea-Brown  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rich feature learning in tasks that unfold over time often requires the model to pass through bifurcations, constituting qualitative changes in the underlying model dynamics. We develop a local theory of gradient descent near these transitions through the empirical state-space neural tangent kernel (sNTK). Our central finding is that bifurcations both dominate and simplify learning dynamics: near bifurcations, we can reduce sNTK to a rank-one operator corresponding to learning in a classical normal form system, providing an analytically tractable description of the local learning geometry, even for high-dimensional recurrent systems. Concretely, we give a procedure for decomposing sNTK into bifurcation-relevant and residual channels, showing that near commonly codimension-1 bifurcations the relevant channel is a rank-one operator that is highly amplified. This amplification causes the bifurcation channel to dominate the full sNTK. Thus, bifurcations locally warp the learning landscape, funneling gradient descent into a few critical dynamical directions and making the nearby kernel and loss geometry predictable from classical normal forms. We illustrate this in a student-teacher recurrent neural network: the first learned bifurcation coincides with a sharp collapse in sNTK effective rank and the emergence of a dominant parameter direction whose restricted sNTK closely matches the landscape predicted by the scalar pitchfork normal form. Finally, we show that low-rank natural gradient methods resolve the resulting learning instability near bifurcations with very little overhead over SGD.

---


### 56. [Inference-Time Machine Unlearning via Gated Activation Redirection](https://arxiv.org/abs/2605.12765)

**<font color=#1a73e8>作者：</font>** Vinícius Conte Turani, Otávio Parraga, João Vitor Boer Abitante 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models memorize vast amounts of training data, raising concerns regarding privacy, copyright infringement, and safety. Machine unlearning seeks to remove the influence of a targeted forget set while preserving model performance, ideally approximating a model retrained from scratch without the forget set. Existing approaches aim to achieve this by updating model parameters via gradient-based methods. However, these updates are computationally expensive, lead to irreversible weight changes, and degrade when the model is quantized for deployment. A recent alternative to changing model weights is activation engineering, where activations are changed during inference to steer model behavior. Despite circumventing weight editing, naive activation steering introduces its own failure modes, as a single global steering vector applies the same intervention to every input, leading to unintended changes in model behavior. We introduce Inference-Time Unlearning via Gated Activation Redirection (GUARD-IT), a training- and gradient-free method that unlearns via input-dependent activation steering at inference time. The resulting intervention is applied as a norm-preserving rotation in the residual stream, leaving model weights untouched. Experiments on TOFU and MUSE show that GUARD-IT matches or exceeds 12 gradient-based baselines across three model scales, while being the only method to simultaneously preserve utility, suppress memorization, and avoid catastrophic collapse across all settings. GUARD-IT further supports continual unlearning without retraining, and remains effective under quantization, a scenario in which parameter-editing methods degrade.

---


### 57. [WriteSAE: Sparse Autoencoders for Recurrent State](https://arxiv.org/abs/2605.12770)

**<font color=#1a73e8>作者：</font>** Jack Young  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce WriteSAE, the first sparse autoencoder that decomposes and edits the matrix cache write of state-space and hybrid recurrent language models, where residual SAEs cannot reach. Existing SAEs read residual streams, but Gated DeltaNet, Mamba-2, and RWKV-7 write to a $d_k \times d_v$ cache through rank-1 updates $k_t v_t^\top$ that no vector atom can replace. WriteSAE factors each decoder atom into the native write shape, exposes a closed form for the per-token logit shift, and trains under matched Frobenius norm so atoms swap one cache slot at a time. Atom substitution beats matched-norm ablation on 92.4% of $n=4{,}851$ firings at Qwen3.5-0.8B L9 H4, the 87-atom population test holds at 89.8%, the closed form predicts measured effects at $R^2=0.98$, and Mamba-2-370M substitutes at 88.1% over 2,500 firings. Sustained three-position installs at $3\times$ lift midrank target-in-continuation from 33.3% to 100% under greedy decoding, the first behavioral install at the matrix-recurrent write site.

---


### 58. [WildPose: A Unified Framework for Robust Pose Estimation in the Wild](https://arxiv.org/abs/2605.12774)

**<font color=#1a73e8>作者：</font>** Jianhao Zheng, Liyuan Zhu, Zihan Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Estimating camera pose in dynamic environments is a critical challenge, as most visual SLAM and SfM methods assume static scenes. While recent dynamic-aware methods exist, they are often not unified: semantic-based approaches are brittle, per-sequence optimization methods fail on short sequences, and other learned models may degrade on static-only scenes. We present WildPose, a unified monocular pose estimation framework that is robust in dynamic environments while maintaining state-of-the-art performance on static and low-ego-motion datasets. Our key insight is to connect two powerful paradigms in modern 3D vision: the rich perceptual frontend of feedforward models and the end-to-end optimization of differentiable bundle adjustment (BA). We achieve this with a 3D-aware update operator built on a frozen, pre-trained MASt3R feature backbone, together with a high-capacity motion mask detector that uses multi-level 3D-aware features from the same backbone. Extensive experiments show WildPose consistently outperforms prior methods across dynamic (Wild-SLAM, Bonn), static (TUM, 7-Scenes), and low-ego-motion (Sintel) benchmarks.

---


### 59. [Graph-Based Financial Fraud Detection with Calibrated Risk Scoring and Structural Regularization](https://arxiv.org/abs/2605.12782)

**<font color=#1a73e8>作者：</font>** Yunfei Nie, Jiawei Wang, Ruobing Yan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial transaction fraud prevention faces challenges such as complex relationship structures, concealed behavioral patterns, and dynamically changing data distribution. Discrimination models relying solely on independent sample features are insufficient to fully characterize the risks of group collaboration and chain transfers within transaction networks. This paper proposes a graph neural network representation learning and risk discrimination framework for financial transaction fraud prevention. It integrates transaction records and identity information into node attributes and constructs a transaction graph based on shared attributes and interaction consistency to explicitly model inter-transaction relationships. In model design, a multi-layer message passing mechanism is employed to aggregate neighborhood information, learn node embedding representations containing structural context semantics, and output transaction-level fraud probability and risk scores through a lightweight risk discrimination head. A weighted supervision objective is introduced to mitigate training bias caused by class imbalance, and structural consistency regularization constraints are combined to suppress the impact of noisy edges on representation drift, thereby improving the stability and usability of risk characterization. Experiments are conducted on a publicly available financial transaction dataset, comparing various methods in the same direction and comprehensively evaluating them under a unified evaluation protocol. The results show that the proposed method outperforms other methods in risk ranking and probability calibration quality, validating the effectiveness of graph structure modeling and representation learning collaboration in financial transaction fraud prevention.

---


### 60. [Identifying the nonlinear string dynamics with port-Hamiltonian neural networks](https://arxiv.org/abs/2605.12785)

**<font color=#1a73e8>作者：</font>** Maximino Linares, Guillaume Doras, Thomas Hélie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid machine learning combines physical knowledge with data-driven models to enhance interpretability and performance. In this context, Port-Hamiltonian Systems (PHS), which generalize Hamiltonian mechanics to describe open, non-autonomous dynamical systems, have been successfully integrated with neural networks under the name Port-Hamiltonian Neural Networks (PHNNs). While the ability of PHNNs to identify Hamiltonian ordinary differential equation (ODE) systems has already been demonstrated, their application to learning Hamiltonian partial differential equation (PDE) systems remains largely unexplored. This limitation restricts their use in musical acoustics, where instruments are typically modeled as distributed parameter systems governed by PDEs. In this work, we demonstrate how to learn the nonlinear string dynamics from data in a physically-consistent framework through a PHNN extension to PDEs. By constructing structured neural network architectures based on PHS, we can recover both the Hamiltonian governing the string and the dissipation affecting it. This approach outperforms baseline, non-physics-informed methods in terms of both accuracy and interpretability. Numerical experiments using synthetic data demonstrate the ability of the proposed PHNN model to identify and emulate the nonlinear dynamics of the system.

---


### 61. [From Heuristics to Analytics: Forecasting Effort and Progress in Online Learning](https://arxiv.org/abs/2605.12788)

**<font color=#1a73e8>作者：</font>** Eric S. Qiu, Danielle R. Thomas, Boyuan Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sustained effort is essential for realizing the benefits of intelligent tutoring systems (ITS), yet many learners disengage or underuse available practice time. We introduce engagement forecasting as a supervised prediction task based on ITS logs, targeting two outcomes central to effort and learning progress: minutes practiced per week and new skills mastered per week. Using interaction log data from 425 middle-school students over a school year, we benchmark fifteen predictors including regressions, decision trees, and neural networks. We show that these feature-based models reduce mean absolute error (MAE) by 22-33% relative to heuristic baselines, including fixed-percentile rules adapted from prior work in other behavioral domains. We find that percentile heuristics systematically overpredict, whereas feature-based models better track student practice trajectories across weeks. To support explainability, we analyze feature importance and ablations, revealing target-specific patterns: effort forecasting is driven mainly by recent activity features, while progress forecasting depends more on learner-state and content difficulty signals. Finally, in a semi-structured user interview case study with eight college tutors, we examine how tutors reasoned about system-generated predictive features when setting goals with students. We find that tutors reasoned differently about effort versus progress goals in ways that mirror our pattern analysis. Together, these results establish a reproducible benchmark for forecasting weekly effort and learning progress in ITS. By making patterns of sustained effort and progress visible at a weekly timescale, engagement forecasting offers a foundation for supporting tutor-learner goal setting and timely instructional decisions.

---


### 62. [SoK: A Comprehensive Analysis of the Current Status of Neural Tangent Generalization Attacks with Research Directions](https://arxiv.org/abs/2605.12792)

**<font color=#1a73e8>作者：</font>** Thushari Hapuarachchi, Kaiqi Xiong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> There is recently a serious issue that Deep Neural Networks (DNNs) training uses more and more unauthorized data. A clean-label generalization attack, one type of data poisoning attacks, has been suggested to address this issue. The Neural Tangent Generalization Attack (NTGA) is considered as the first well-known clean-label generalization attack under the black-box settings, which provided an unprecedented step in data protection approaches. In this paper, we conduct a comprehensive analysis on the state-of-the-art of NTGA; to the best of our knowledge, this is the first thorough analysis regarding NTGA. First, we provide a classification of attacks against DNNs with their explanations and relations to NTGA. Then, this paper presents a taxonomy of black-box attacks and demonstrate that the NTGA is the first clean-label generalization attack under the black-box setting. We further analyze the existing studies of NTGA and give a comprehensive comparisons of their findings by conducting our own experiments to verify these findings. Moreover, our extensive experiments show that NTGA is vulnerable to adversarial training and image transformations, and applying linear separability to NTGA-generated images makes them more susceptible to such vulnerablities. We present the pros and cons of NTGA and suggest ways to improve NTGA robustness based on our analysis. Our further experiments indicate that several recently proposed clean-label generalization attacks outperform NTGA on data protection. Finally, we unveil the necessity of further research with future research insights on NTGA.

---


### 63. [Pitfalls of Unlabeled Disagreement-Based Drift Detection in Streaming Tree Ensembles](https://arxiv.org/abs/2605.12803)

**<font color=#1a73e8>作者：</font>** Lara Sá Neves, Afonso Lourenço, Lizy K. John 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Detecting concept drift in high-speed data streams remains challenging, particularly when models must operate on unlabeled data and avoid false alarms caused by benign shifts. While disagreement-based uncertainty has shown promise in neural networks, its adaptation to ensembles of incremental decision trees (IDTs) remains largely unexplored. We investigate this approach by constructing batch-specific disagreement measures via label flipping in ensemble members and evaluating their effectiveness for drift detection in tabular data streams. Our experiments show that, although this method performs well in ensembles of multi-layer perceptrons (MLPs), it consistently underperforms loss-based detectors when applied to IDTs. We attribute this behavior to the intrinsic rigidity of IDTs: learning primarily through structural expansion, with limited parameter adaptation, restricts model plasticity and prevents disagreement from reliably reflecting learning potential. Recent work on restructuring IDTs using their intrinsic decomposition into non-overlapping rules offers a promising direction for improving adaptability.

---


### 64. [Discrete MeanFlow: One-Step Generation via Conditional Transition Kernels](https://arxiv.org/abs/2605.12805)

**<font color=#1a73e8>作者：</font>** Fairoz Nower Khan, Nabuat Zaman Nahim, Md Sajid Ahmed 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> MeanFlow enables one-step generation in continuous spaces by learning an average velocity over a time interval rather than the instantaneous velocity field of flow matching. However, discrete state spaces do not have smooth trajectories or spatial derivatives, so the continuous formulation does not directly apply. We introduce Discrete MeanFlow, which replaces the motion of a point with the transport of probability mass over finite states. Our key object is the conditional transition kernel of a continuous-time Markov chain (CTMC), from which we define a mean discrete rate that measures the average change in transition probability over a time interval. We prove a Discrete MeanFlow identity that relates this finite-interval rate to the instantaneous CTMC generator at the endpoint, with the Kolmogorov forward equation replacing the spatial chain rule of continuous MeanFlow. Based on this identity, we parameterize the transition kernel directly using a boundary-by-construction design that guarantees valid probability outputs and exact boundary conditions without auxiliary losses. Since the learned kernel is itself a probability distribution, generation reduces to a single forward pass followed by one categorical draw meaning no iterative denoising, ODE integration, or multi-step refinement is required. We validate the framework on exact finite-state Markov chains, where the learned kernel recovers the analytical ground truth to high precision, and on factorized synthetic sequence generation tasks with varying alphabet sizes and sequence lengths.

---


### 65. [AGOP as Explanation: From Feature Learning to Per-Sample Attribution in Image Classifiers](https://arxiv.org/abs/2605.12816)

**<font color=#1a73e8>作者：</font>** Raj Kiran Gupta Katakam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Average Gradient Outer Product (AGOP) governs feature learning in neural networks: the Neural Feature Ansatz states that weight Gram matrices at each layer align with the corresponding AGOP matrices computed over the training distribution. We ask a complementary question: can this same quantity serve as a post-hoc attribution method for explaining individual predictions? We introduce AGOP-Weighted: a novel attribution method that multiplies the per-sample gradient by sqrt(diag(M) / max diag(M)), a training-distribution prior that suppresses gradient noise and amplifies consistently important pixels -- a combination not present in any prior attribution method. We formalise two companion variants -- AGOP-Local (per-sample gradient, equivalent to VanillaGrad) and AGOP-Global (diag(M) directly as a zero-cost saliency map) -- and implement an efficient training-time accumulation hook; AGOP-Global then requires zero inference cost (disk lookup) while AGOP-Weighted requires only a single gradient pass. We conduct the first rigorous comparison of AGOP attribution against Integrated Gradients (IG), SmoothGrad, GradCAM, and VanillaGrad across two benchmarks with pixel-level ground truth: (i) the synthetic XAI-TRIS benchmark (four classification scenarios, 8x8 images, CNN8by8) and (ii) the photorealistic CLEVR-XAI benchmark (ResNet-18 fine-tuned from ImageNet). AGOP-Weighted achieves 44% higher mIoU than IG on linear tasks; AGOP-Global achieves 7x higher mIoU than IG on multiplicative tasks (where IG falls below random) at zero inference cost. Both findings generalise to ResNet-18 on CLEVR-XAI (+18% and +37% respectively). We further show that GradCAM fails on small-resolution images due to spatial resolution collapse, and that diag(M) quality improves monotonically throughout training even after classification accuracy has plateaued.

---


### 66. [Hessian Matching for Machine-Learned Coarse-Grained Molecular Dynamics](https://arxiv.org/abs/2605.12823)

**<font color=#1a73e8>作者：</font>** Sanya Murdeshwar, Sanjit Shashi, Kevin Bachelor 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Coarse-grained (CG) molecular dynamics enables simulations of atomic systems such as biomolecules at timescales inaccessible to all-atom (AA) methods, but existing CG neural potentials trained via force matching capture only the gradient of the free-energy surface, leaving its curvature unconstrained. We introduce a framework that augments force matching with stochastic Hessian-vector product (HVP) matching, instilling second-order curvature information into CG potentials without constructing the full Hessian. We derive a decomposition of the target CG Hessian into a model-independent projected AA Hessian, precomputed once before training, and a model-dependent covariance correction computed online at negligible cost. We construct an unbiased stochastic estimator of the Hessian-matching objective by using random probe vectors. We evaluate our method by comparing against force matching on a benchmark of nine fast-folding proteins unseen during training. HVP matching outperforms plain force matching on 8 of 9 proteins on slow-mode metrics, with reductions of up to 85% in the Kullback--Leibler divergence between the CG and reference distributions along the slowest collective mode of the largest protein. Our results demonstrate that higher-order physical supervision is a practical path to more accurate and transferable CG potentials for biomolecular simulation.

---


### 67. [Mechanism Plausibility in Generative Agent-Based Modeling](https://arxiv.org/abs/2605.12824)

**<font color=#1a73e8>作者：</font>** Patrick Zhao, David Huu Pham, Nicholas Vincent  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can generate high-level diverse phenomena without explicitly programmed rules. This capability has led to their adoption within different agent-based models (ABMs) and social simulations. Recently, research has aim to test whether they are capable of generating different phenomena of interest, for example, human behavior on social media platforms or performance in game-theoretic scenarios.
However, capability, prediction, and explanation are different -- drawing from the philosophy of science and mechanisms literature, \textit{explanation} requires showing, to some degree, how a phenomenon is produced by related organized entities and activities. For modelers, describing the characteristics of an experiment or whether a simulation provides progress in capability (or explanation), can be difficult without being grounded in potentially distant research areas.
We integrate recent work on LLM-ABMs with contemporary philosophy of science literature and use it to operationalize a definition of `plausibility' in a four-level scale. Our scale separates the evaluation of a model's generative sufficiency (ability to reproduce a phenomenon) from its mechanistic plausibility (how the phenomenon could be produced), and clarifies the distinct roles of different models, such as predictive and explanatory ones. We introduce this as the Mechanism Plausibility Scale.

---


### 68. [Orthrus: Memory-Efficient Parallel Token Generation via Dual-View Diffusion](https://arxiv.org/abs/2605.12825)

**<font color=#1a73e8>作者：</font>** Chien Van Nguyen, Chaitra Hegde, Van Cuong Pham 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Orthrus, a simple and efficient dual-architecture framework that unifies the exact generation fidelity of autoregressive Large Language Models (LLMs) with the high-speed parallel token generation of diffusion models. The sequential nature of standard autoregressive decoding represents a fundamental bottleneck for high-throughput inference. While diffusion language models attempt to break this barrier via parallel generation, they suffer from significant performance degradation, high training costs, and a lack of rigorous convergence guarantees. Orthrus resolves this dichotomy natively. Designed to seamlessly integrate into existing Transformers, the framework augments a frozen LLM with a lightweight, trainable module to create a parallel diffusion view alongside the standard autoregressive view. In this unified system, both views attend to the exact same high-fidelity Key-Value (KV) cache; the autoregressive head executes context pre-filling to construct accurate KV representations, while the diffusion head executes parallel generation. By employing an exact consensus mechanism between the two views, Orthrus guarantees lossless inference, delivering up to a 7.8x speedup with only an O(1) memory cache overhead and minimal parameter additions.

---


### 69. [FRAME: Forensic Routing and Adaptive Multi-path Evidence Fusion for Image Manipulation Detection](https://arxiv.org/abs/2605.12826)

**<font color=#1a73e8>作者：</font>** Kaixiang Zhao, Tianrun Yu, Aoxu Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The proliferation of sophisticated image editing tools and generative artificial intelligence models has made verifying the authenticity of digital images increasingly challenging, with important implications for journalism, forensic analysis, and public trust. Although numerous forensic algorithms, ranging from handcrafted methods to deep learning-based detectors, have been developed for manipulation detection, individual methods often suffer from limited robustness, fragmented evidence, or weak generalization across manipulation types and image conditions. To address these limitations, we present \textbf{FRAME}, a method for \textbf{F}orensic \textbf{R}outing and \textbf{A}daptive \textbf{M}ulti-path \textbf{E}vidence fusion for image manipulation detection. FRAME organizes diverse forensic algorithms into a multi-path analysis space, adaptively selects informative forensic paths for each input image, and fuses complementary evidence to improve detection and localization performance. By moving beyond single-method analysis and fixed fusion strategies, FRAME provides a more robust and flexible approach to image forensic reasoning while preserving interpretable forensic cues from multiple evidence sources. Experimental results demonstrate the effectiveness of FRAME across diverse manipulation scenarios. Code is available at \href{this https URL}{this https URL}.

---


### 70. [GraphIP-Bench: How Hard Is It to Steal a Graph Neural Network, and Can We Stop It?](https://arxiv.org/abs/2605.12827)

**<font color=#1a73e8>作者：</font>** Kaixiang Zhao, Bolin Shen, Yuyang Dai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Graph neural networks (GNNs) deployed as cloud services can be \emph{stolen} through \emph{model-extraction attacks}, which train a surrogate from query responses to reproduce the target's behaviour, and a growing line of ownership defenses tries to prevent or trace such theft. The title of this paper asks two questions: \emph{how hard is it to steal a GNN?}, and \emph{can we stop it?} Prior work cannot answer either, because experiments use inconsistent datasets, threat models, and metrics. We introduce \emph{GraphIP-Bench}, a unified benchmark which evaluates both sides under a single black-box protocol. It integrates twelve extraction attacks, twelve defenses spanning watermarking, output-perturbation, and query-pattern-detection families, ten public graphs covering homophilic, heterophilic, and large-scale regimes, three GNN backbones, and three graph-learning tasks, and it reports fidelity, task utility, ownership verification, and computational cost on shared splits, queries, and budgets. We further add a joint attack-and-defense track which runs every attack on every defended target and measures watermark verification on the resulting surrogate, which exposes the protection that a defense retains after extraction. The empirical picture is short: stealing a GNN is easy at medium query budgets and most defenses do not change this; several watermarks verify reliably on the protected model but lose most of their verification signal on the extracted surrogate, which exposes a gap that single-model evaluations miss; and heterophilic graphs are systematically harder to steal, while a cross-architecture mismatch between target and surrogate reduces but does not prevent extraction. Code: \href{this https URL}{LabRAI/GraphIP-Bench}.

---


### 71. [Quantifying Potential Observation Missingness in Inverse Reinforcement Learning](https://arxiv.org/abs/2605.12831)

**<font color=#1a73e8>作者：</font>** Leo Benac, Abhishek Sharma, Alihan Huyuk 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inverse reinforcement learning (IRL), which infers reward functions from demonstrations, is a valuable tool for modeling and understanding decision-making behavior. Many variants of IRL have been developed to capture complexities of human decision-making, such as subjective beliefs, imperfect planning, and dynamic goals. However, an often-overlooked issue in real-world behavioral datasets is that the recorded data may be missing observations that were available to the original decision-maker. In use-inspired settings such as healthcare, this can make expert actions appear suboptimal, even when they were near-optimal given the information available at the time. As a result, the rewards learned by standard IRL may be misleading. In this paper, we identify the minimal perturbations to the recorded observations needed for the expert's actions to appear optimal. We develop a practical algorithm for this problem and demonstrate its utility for quantifying the possible extent of missing observations in behavioral datasets through extensive experiments on synthetic navigation tasks, a cancer treatment simulator, and ICU treatment data.

---


### 72. [PROMETHEUS: Automating Deep Causal Research Integrating Text, Data and Models](https://arxiv.org/abs/2605.12835)

**<font color=#1a73e8>作者：</font>** Sridhar Mahadevan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can extract local causal claims from text, but those claims become more useful when organized as persistent, navigable world models rather than as flat summaries. We introduce PROMETHEUS, a framework that turns retrieved literature, filings, reviews, reports, agent traces, source data, code, simulations, and scientific models into causal atlases: sheaf-like families of local causal predictive-state models over an explicit cover of a research substrate. Each local region contains causal episodes, structured claim tables, predictive tests, support statistics, and provenance; restriction maps compare overlapping regions; gluing diagnostics expose agreement, drift, contradiction, and underdetermination. The resulting Topos World Model is not a single universal graph. It is a research instrument for navigating what a corpus says, where it says it, how strongly it is supported, and where local claims fail to assemble into a coherent global view. Three literature-atlas case studies -- ocean-temperature impacts on marine populations, GLP-1 weight-loss evidence, and resveratrol/red-wine health-benefit claims -- illustrate deep causal research from text with explicit locality, evidence, persistent state, and gluing tension. Four grounded-counterfactual case studies -- a Nature Climate Change microplastics forcing paper, an Indus Valley hydrology paper with VIC-derived figure data and model code, the canonical Sachs protein-signaling study with single-cell perturbation data, and a Nature singing-mouse study with MAPseq projection matrices -- show a stronger mode: when a paper ships source data, simulation outputs, or code, PROMETHEUS can evaluate a counterfactual against that scientific substrate and then rebuild the sheaf world model around the

---


### 73. [Discrete Stochastic Localization for Non-autoregressive Generation](https://arxiv.org/abs/2605.12836)

**<font color=#1a73e8>作者：</font>** Yunshu Wu, Jiayi Cheng, Longxuan Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous diffusion is a natural framework for non-autoregressive generation but has generally lagged behind masked discrete diffusion models (MDMs) on discrete sequence generation. We argue that the bottleneck is not continuity itself, but a representation in which denoising depends on timestep-indexed noise regimes. We introduce \emph{Discrete Stochastic Localization} (DSL), a continuous-state framework with unit-sphere token embeddings whose Bayes-optimal denoiser is invariant to the nominal signal-to-noise ratio (SNR) under the localization channel. One trained network then supports an entire family of per-token SNR paths, with endpoint masked-diffusion paths as a special case. Fine-tuning a pretrained MDLM checkpoint with DSL substantially improves distributional faithfulness (MAUVE) on OpenWebText across all step budgets from $T{=}128$ to $T{=}1024$, and the same checkpoint supports random-order autoregressive sampling, as well as a hybrid continuous-then-discrete sampler using as few as T=48 total steps -- without distillation or retraining.

---


### 74. [HE-PIM: Demystifying Homomorphic Operations on a Real-world Processing-in-Memory System](https://arxiv.org/abs/2605.12841)

**<font color=#1a73e8>作者：</font>** Harshita Gupta, Mayank Kabra, Jaewoo Park 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Homomorphic encryption (HE) enables computation over encrypted data, offering strong privacy guarantees for untrusted computing environments. Practical adoption remains limited by high computational complexity, large ciphertext sizes, and substantial data movement. Processor-centric architectures (CPUs, GPUs, ASICs) hit fundamental bottlenecks on HE workloads because ciphertexts are large, data locality is low, and primitives such as relinearization and bootstrapping repeatedly access large auxiliary metadata. Processing-In-Memory (PIM) is a promising mitigation by computing near or inside memory. Prior PIM proposals for HE either do not target real-world PIM systems or cover only a narrow set of operations.
We comprehensively characterize HE operations on a real-world, general-purpose PIM system. We implement a complete set of HE kernels used by emerging applications (databases, machine learning) on the UPMEM PIM system, evaluate performance and scalability, compare against CPU and GPU baselines, and discuss implications for future PIM hardware. Our results demonstrate four major findings. (1) HE-based applications expose distinct bottlenecks across execution stages: some kernels are compute-bound due to modular arithmetic, while others are memory-bound due to large ciphertexts and intermediate data. These bottlenecks are exacerbated by limited per-core compute and per-bank capacity, which force frequent data movement. (2) The dominant compute bottleneck is the lack of native 64-bit modular integer multiplication, a key HE primitive. (3) Limited per-bank memory capacity is the second major bottleneck, since HE ciphertexts and auxiliary metadata do not fit and require inter-bank movement. (4) Despite these limits, PIM can be a viable alternative to state-of-the-art CPU and GPU systems for HE when equipped with native modular multiplication and efficient inter-PIM data movement.

---


### 75. [Bayesian Model Merging](https://arxiv.org/abs/2605.12843)

**<font color=#1a73e8>作者：</font>** Kaiyang Li, Shaobo Han, Qing Su 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model merging aims to combine multiple task-specific expert models into a single model without joint retraining, offering a practical alternative to multi-task learning when data access or computational budget is limited. Existing methods, however, face two key limitations: (1) they overlook the valuable inductive bias of strong anchor models and estimate the merged weights from scratch, and (2) they rely on a shared hyperparameter setting across different modules of the network, lacking a global optimization strategy. This paper introduces Bayesian Model Merging (BMM), a plug-and-play bi-level optimization framework, where the inner level formulates the model merging as an activation-based Bayesian regression under a strong prior induced by an anchor model, yielding an efficient closed-form solution; and the outer level leverages a Bayesian optimization procedure to search module-specific hyperparameters globally based on a small validation set. Furthermore, we reveal a key alignment between activation statistics and task vectors, enabling us to derive a data-free variant of BMM that estimates the Gram matrix for regression without any auxiliary data. Across extensive benchmarks, including up to 20-task merging in vision and 5-task merging in language, BMM consistently outperforms all plug-and-play anchor baselines (e.g., TA, WUDI-Merging, and TSV). In particular, on the ViT-L/14 benchmark for 8-task merging, a single merged model reaches 95.1, closely matching the average performance of eight task-specific experts (95.8).

---


### 76. [AssemblyBench: Physics-Aware Assembly of Complex Industrial Objects](https://arxiv.org/abs/2605.12845)

**<font color=#1a73e8>作者：</font>** Danrui Li, Jiahao Zhang, Bernhard Egger 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Assembling objects from parts requires understanding multimodal instructions, linking them to 3D components, and predicting physically plausible 6-DoF motions for each assembly step. Existing datasets focus on simplified scenarios, overlooking shape complexities and assembly trajectories in industrial assemblies. We introduce AssemblyBench, a synthetic dataset of 2,789 industrial objects with multimodal instruction manuals, corresponding 3D part models, and part assembly trajectories. We also propose a transformer-based model, AssemblyDyno, which uses the instructional manual and the 3D shape of each part to jointly predict assembly order and part assembly trajectories. AssemblyDyno outperforms prior works in both assembly pose estimation and trajectory feasibility, where the latter is evaluated by our physics-based simulations.

---


### 77. [PRISM: Perinuclear Ring-based Image Segmentation Method for Acute Lymphoblastic Leukemia Classification](https://arxiv.org/abs/2605.12851)

**<font color=#1a73e8>作者：</font>** Larissa Ferreira Rodrigues Moreira, Leonardo Gabriel Ferreira Rodrigues, Rodrigo Moreira 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated analysis of peripheral blood smears for Acute Lymphoblastic Leukemia (ALL) is hindered by low contrast and substantial variability in cytoplasmic appearance, which complicate conventional membrane-based segmentation. We found that many recent approaches rely on heavy neural architectures and extensive training, but still struggle to generalize across staining and acquisition variability. To address these limitations, we propose the Perinuclear Ring-based Image Segmentation Method (PRISM), which replaces explicit cytoplasmic delineation with adaptive concentric zones constructed around the nucleus. These perinuclear regions enable the extraction of robust cytoplasmic descriptors by integrating color information with texture statistics derived from grey-level co-occurrence patterns, without requiring accurate cell-boundary detection. A calibrated stacking ensemble of traditional classifiers leverages these descriptors to achieve a high performance, with an accuracy of 98.46% and a precision-recall AUC of 0.9937.

---


### 78. [Prediction of Rectal Cancer Regrowth from Longitudinal Endoscopy](https://arxiv.org/abs/2605.12855)

**<font color=#1a73e8>作者：</font>** Jorge Tapias Gomez, Despoina Kanata, Aneesh Rangnekar 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Clinical trial studies indicate benefit of watch-and-wait (WW) surveillance for patients with rectal cancer showing a complete or near clinical response (CR) directly after treatment (restaging). However, there are no objectively accurate methods to early detect local tumor regrowth (LR) in patients undergoing WW from follow-up exams. Hence, we developed Temporal Rectal Endoscopy Cross-attention (TREX), a longitudinal deep learning approach that combines pairs of images acquired at restaging and follow-up to distinguish CR from LR. TREX uses pretrained Swin Transformers in a siamese setting to extract features from longitudinal images and dual cross-attention to combine the features without spatial co-registration between image pairs. TREX and Swin-based baselines were trained under two settings: (a) detecting LR or CR at the last available follow-up and (b) early detection of LR at 3--6, 6--12, and 12--24 months before clinical confirmation. TREX achieved the highest accuracy in detecting LR with a high sensitivity of 97% $\pm$ 6% and a balanced accuracy of 90% $\pm$ 3%, and outperformed all baselines in early detection at both 3--6 (74% $\pm$ 1%) and 6--12 months (62% $\pm$ 4%) prior to clinical detection. Clinical validation via a surgeon survey showed that TREX matched attending-level overall accuracy (TREX: 86.21% vs.\ Clinicians: 87.84% $\pm$ 1.28%). Finally, we explored TREX's ability to predict treatment response by combining pre-treatment (pre-TNT) and restaging endoscopies, achieving a balanced accuracy of 73% $\pm$ 12%. These results show that longitudinal deep learning analysis of endoscopy may improve surveillance and enable earlier identification of rectal cancer regrowth.

---


### 79. [Moltbook Moderation: Uncovering Hidden Intent Through Multi-Turn Dialogue](https://arxiv.org/abs/2605.12856)

**<font color=#1a73e8>作者：</font>** Ali Al-Lawati, Nafis Tripto, Abolfazl Ansari 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The emergence of multi-agent systems introduces novel moderation challenges that extend beyond content filtering. Agents with {\em malicious intent} may contribute harmful content that appears benign to evade content-based moderation, while compromising the system through exploitative and malicious behavior manifested across their overall interaction patterns within the community. To address this, we introduce \textsc{\textbf{Bot-Mod}} (\textsc{\textbf{Bot-Mod}}eration), a moderation framework that grounds detection in agent intent rather than traditional content level signals. \method{} identifies the underlying intent by engaging with the target agent in a multi-turn exchange guided by Gibbs-based sampling over candidate intent hypotheses. This progressively narrows the space of plausible agent objectives to identify the underlying behavior. To evaluate our approach, we construct a dataset derived from Moltbook that encompasses diverse benign and malicious behaviors based on actual community structures, posts, and comments. Results demonstrate that \textsc{\textbf{Bot-Mod}} reliably identifies agent intent across a range of adversarial configurations, while maintaining a low false positive rate on benign behaviors. This work advances the foundation for scalable, intent-aware moderation of agents in open multi-agent environments.

---


### 80. [ChipMATE: Multi-Agent Training via Reinforcement Learning for Enhanced RTL Generation](https://arxiv.org/abs/2605.12857)

**<font color=#1a73e8>作者：</font>** Zhongkai Yu, Yichen Lin, Chenyang Zhou 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Existing API-based agentic systems for RTL code generation are fundamentally misaligned with industrial practice: they assume a golden testbench is available at generation time, rely on closed-source APIs incompatible with chip vendors' air-gapped security requirements, and cannot be trained on vendors' proprietary RTL codebases, leaving valuable internal data unused. Recent self-trained models address the deployment constraint but remain single-turn generators that overlook the critical role of verification in real industrial flows.
To bridge these gaps, we present ChipMATE, the first self-trained multi-agent framework for RTL generation. Inspired by industrial practice where correctness emerges from cross-comparison between independently written RTL modules and reference models, ChipMATE pairs a Verilog agent with a Python reference-model agent that mutually verify each other's outputs without any golden oracle. We design a backtrack-based inference workflow to prevent error propagation across turns, and a two-stage training pipeline that first trains each agent individually to saturate its code-generation capability, then trains the team jointly to collaborate effectively. To support the training, we further build a hybrid data-generation framework that produces 64.4K high-quality reference model training samples. ChipMATE achieves 75.0\% and 80.1\% pass@1 on VerilogEval V2 with 4B and 9B base models, outperforming all existing self-trained models and even DeepSeek V4 with 1600B parameters. Our code and model weights are publicly available in this https URL.

---


### 81. [Descriptive Collision in Sparse Autoencoder Auto-Interpretability: When One Explanation Describes Many Features](https://arxiv.org/abs/2605.12874)

**<font color=#1a73e8>作者：</font>** Jordan F. McCann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) are now standard tools for decomposing language model activations into interpretable features, and automated interpretability pipelines routinely assign each feature a short natural-language explanation. Existing critiques of this practice focus on polysemanticity -- one feature with many meanings -- or on whether explanations predict activations. We identify a complementary, structurally distinct problem we call descriptive collision: many distinct SAE features admit the same explanation. Reanalyzing the largest publicly-available dataset of human-annotated SAE features (Marks et al., 2025), comprising 722 annotated features across Gemma 2 2B and Pythia 70M, we find that the mean annotation string is reused across 3.07 features; 82.1% of features share their annotation with at least one other feature; and the single most common annotation string ("plural nouns") labels 101 distinct features spanning 18 layers and four model components. Information-theoretically, the average annotation resolves only 70% of feature identity. We formalize a property called discrimination, prove that current detection-style auto-interpretability scoring is invariant to collision, and propose two complementary corrective metrics -- collision-adjusted detection and discrimination scoring -- that explicitly penalize explanations that fail to distinguish a feature from its neighbors. The collision problem is independent of, and additive with, previously identified failure modes of auto-interpretability; ignoring it inflates reported feature interpretability by a quantity equal to roughly one-third of the bits required to identify a feature.

---


### 82. [Certified Robustness under Heterogeneous Perturbations via Hybrid Randomized Smoothing](https://arxiv.org/abs/2605.12876)

**<font color=#1a73e8>作者：</font>** Blaise Delattre, Hengyu Wu, Paul Caillon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Randomized smoothing provides strong, model-agnostic robustness certificates, but existing guarantees are limited to single modalities, treating continuous and discrete inputs in isolation. This limitation becomes critical in multimodal models, where decisions depend on cross-modal semantics and adversaries can jointly perturb heterogeneous inputs, rendering unimodal certificates insufficient. We introduce a unified randomized smoothing framework for mixed discrete--continuous inputs based on an analytically tractable Neyman--Pearson formulation of the joint worst-case problem. By analyzing the joint likelihood ordering induced by factorized discrete and continuous noise, our approach yields a closed-form, one-dimensional certificate that strictly generalizes both Gaussian (image-only) and discrete (text-only) randomized smoothing. We validate the framework on multimodal safety filtering, providing, to our knowledge, the first model-agnostic Neyman--Pearson certificate for joint discrete-token and continuous-image perturbations in interaction-dependent text--image safety filtering.

---


### 83. [ASAP: Amortized Doubly-Stochastic Attention via Sliced Dual Projection](https://arxiv.org/abs/2605.12879)

**<font color=#1a73e8>作者：</font>** Huy Tran, Max Milkert, David Hyde  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Doubly-stochastic attention has emerged as a transport-based alternative to row-softmax attention, with recent Transformer variants using it to reduce attention sinks and rank collapse while improving performance. In this family, the standard approach is Sinkhorn scaling, which trains more efficiently but still repeats matrix scaling in every inference forward pass. Sliced-transport attention removes the online iteration, but its soft sorting approximation materializes dense tensors for each slice, requiring substantially more training resources than Sinkhorn attention. We introduce ASAP: Amortized Doubly-Stochastic Attention via Sliced Dual Projection, a train-then-compile method that trains the doubly-stochastic layer with Sinkhorn, then replaces the iterative scaling loop at inference with a fixed sliced-dual operator. It learns a lightweight parametric map from exact one-dimensional Kantorovich potentials to the Sinkhorn query-side dual, then reconstructs the attention plan with a two-sided entropic c-transform. Across language and vision benchmarks, ASAP keeps the cheaper training setup and remains highly competitive with recent baselines. In the main frozen-layer benchmark, ASAP is 5.3 faster than the trained Sinkhorn teacher while matching its accuracy; in downstream replacements, ASAP recovers most of the teacher performance without any retraining.

---


### 84. [RISED: A Pre-Deployment Safety Evaluation Framework for Clinical AI Decision-Support Systems](https://arxiv.org/abs/2605.12895)

**<font color=#1a73e8>作者：</font>** Rohith Reddy Bellibatlu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Aggregate accuracy metrics dominate the evaluation of clinical AI decision-support systems but do not detect deployment-phase failures of input reliability, subgroup equity, threshold sensitivity, or operational feasibility. We propose the RISED Framework: a five-dimension pre-deployment evaluation covering Reliability, Inclusivity, Sensitivity, Equity, and Deployability, in which each dimension is operationalized through formal sub-criteria, pre-specified pass/fail thresholds, and bias-corrected accelerated (BCa) bootstrap 95% confidence intervals combined under a Holm-Bonferroni family-wise error correction. A central demonstration is that a classifier satisfying conventional high-discrimination benchmarks can simultaneously fail input-encoding stability and threshold-shift sensitivity checks, while subgroup AUC parity remains statistically inconclusive, pointing to deployment risks that aggregate evaluation alone cannot detect. We validate this differential pass/fail pattern on a synthetic cohort and three publicly available real-world cohorts spanning 35 years of clinical data vintage, from a 1980s cardiology dataset to a 2024 nationally representative health survey, where failing dimensions differ across cohorts, providing preliminary evidence of construct validity. The Equity dimension is reframed as a proxy-dependence diagnostic rather than a stand-alone gate: any need-based fairness verdict computed against a utilization-derived proxy carries a construct-validity problem the framework surfaces explicitly, triggering a procurement requirement for an outcome-independent need measure before the gate is binding. RISED is released as an open-source Python package that supplies the quantitative verdicts existing clinical AI reporting standards require, providing a principled gateway between in-silico model validation and silent-trial clinical evaluation.

---


### 85. [Magical Touch: Transforming Raw Capacitive Streams into Expressive Hand-Touchscreen Interaction](https://arxiv.org/abs/2605.12902)

**<font color=#1a73e8>作者：</font>** Yuanlei Guo, Xizi Gong, Yizhong Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Modern touchscreens utilize capacitive sensing technology to enable precise and robust multi-touch interaction. However, the broader expressive potential of the human hand remains underutilized, since most existing methods directly filter out larger-area hand-screen contact. This paper introduces Magical Touch, an interaction method based on raw capacitive sensing data. By directly integrating raw touchscreen sensor data into the interaction loop, our method allows users to interact with the screen naturally and efficiently using arbitrary hand gestures on existing touchscreen devices. To demonstrate the feasibility and expressive capacity of this approach, we implement a physics-based interactive game featuring single-player, multiplayer collaborative, and pressure-sensitive modes. These scenarios showcase how digital objects can respond in real-time to both the geometry and contact intensity of the user's hand. Our results indicate that leveraging raw capacitive data can expand the design space of touchscreen interaction, offering an embodied and continuous interaction paradigm beyond existing fingertip-based approaches.

---


### 86. [SHM-Agents: A Generalist-Specialist Integrated Agent System for Structural Health Monitoring](https://arxiv.org/abs/2605.12916)

**<font color=#1a73e8>作者：</font>** Yuequan Bao, Xing Li, Huabin Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence is increasingly used to simplify complex tasks. In engineering applications of structural health monitoring (SHM), existing specialized algorithms, while effective, often face high implementation barriers, limited interoperability and complex training procedures. To overcome these challenges, this paper proposes SHM-Agents, a generalist-specialist agent system that integrates the reasoning and planning abilities of large language models with the problem-solving strengths of specialized algorithms. SHM-Agents enables end-to-end execution of single and combined SHM tasks via natural language, supports deep learning pre-training to simplify deployment and allows flexible expansion through a modular design. Experiments on a long-span cable-stayed bridge show that SHM-Agents can accurately and efficiently perform diverse SHM tasks, including data anomaly diagnosis and recovery, signal processing, statistical analysis, modal identification, damage identification, finite element model updating, vehicle load modeling, response calculation, reliability assessment, fatigue estimation and bridge knowledge Q\&A.

---


### 87. [Adaptive Conformal Prediction for Reliable and Explainable Medical Image Classification](https://arxiv.org/abs/2605.12917)

**<font color=#1a73e8>作者：</font>** One Octadion, Novanto Yudistira, Lailil Muflikhah  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models for medical imaging often exhibit overconfidence, creating safety risks in ambiguous diagnostic scenarios. While Conformal Prediction (CP) provides distribution-free statistical guarantees, standard methods such as Regularized Adaptive Prediction Sets (RAPS) optimize for average efficiency and can mask severe failures on difficult inputs.
We propose an Adaptive Lambda Criterion for RAPS that minimizes the worst-case coverage violation across prediction set size strata. On OrganAMNIST (58,850 abdominal CT images, 11 classes), standard size-optimized RAPS converges to near-deterministic behavior with stratified undercoverage on uncertain samples, while our method achieves 95.72 percent global coverage with average set size 1.09 and at least 90 percent coverage across all strata. Cross-domain validation on PathMNIST (107,180 pathology images, 9 classes) confirms generalizability.
Quantitative Grad-CAM analysis (rho = -0.30, p < 1e-22) shows that multi-label predictions correspond to focused attention on anatomically ambiguous regions. These results demonstrate that the proposed method improves reliability while maintaining efficiency, making it suitable for safety-critical medical AI applications.

---


### 88. [GuardMarkGS: Unified Ownership Tracing and Edit Deterrence for 3D Gaussian Splatting](https://arxiv.org/abs/2605.12919)

**<font color=#1a73e8>作者：</font>** Utae Jeong, Jaewan Choi, Junseok Lee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) is becoming a practical representation for novel view synthesis, but its growing adoption, together with rapid advances in instruction-driven 3DGS editing, also exposes a dual copyright risk: once a 3DGS-based asset is released, it can be used without permission and manipulated through 3D editing. Existing protection methods address only one side of this problem. Watermarking can trace ownership after unauthorized use, but it cannot prevent malicious editing. Adversarial edit-deterrence methods can disrupt editing, but they do not provide evidence of ownership. To the best of our knowledge, we present the first unified protection framework for 3DGS that jointly optimizes ownership tracing and unauthorized editing deterrence. Our framework combines a scene-wide watermarking objective over all Gaussians with an adversarial objective for edit deterrence. The adversarial branch combines latent-anchor separation, denoising-trajectory diversion, and cross-attention diversion to divert the editing trajectory, while an update-saliency-motivated Gaussian selection strategy assigns stronger adversarial updates to mask-selected Gaussians, improving the balance among watermark recovery, edit deterrence, and rendering fidelity. Experiments on scenes from Mip-NeRF 360 and Instruct-NeRF2NeRF demonstrate that the proposed framework achieves a favorable balance among bit accuracy, edit deterrence, and rendering quality. These results suggest that practical copyright protection of 3DGS-based assets can be more effectively addressed by integrating ownership tracing and unauthorized editing deterrence into a single optimization framework.

---


### 89. [ThermalTap: Passive Application Fingerprinting in VR Headsets via Thermal Side Channels](https://arxiv.org/abs/2605.12927)

**<font color=#1a73e8>作者：</font>** Mahsin Bin Akram, A H M Nazmus Sakib, OFM Riaz Rahman Aranya 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Standalone virtual reality (VR) headsets process highly sensitive personal, professional, and health-related data, yet their susceptibility to non-contact physical side channels remains largely unexplored. Existing side-channel attacks typically require malicious software execution or physical access to peripherals, making them conspicuous and potentially patchable. This paper introduces ThermalTap, the first passive, non-contact side-channel attack that fingerprints VR applications solely from the long-wave infrared (LWIR) radiation emitted by the headset chassis. By treating a headset's thermal signature as a high-fidelity proxy for internal computational workloads, ThermalTap enables remote application inference at meter-scale distances without any device interaction. To achieve robust performance in real-world settings, the system combines a commodity thermal camera with a multi-modal sensor suite (capturing ambient temperature, humidity, and airflow) to normalize environmental noise. We evaluate ThermalTap using six applications across three commercial standalone headsets. In indoor settings, ThermalTap identifies applications with over 90% accuracy using only 10 seconds of thermal camera data. Under outdoor conditions, with longer session-level observations, several applications remain identifiable despite environmental variability, with the strongest outdoor application reaching 81% accuracy. Our findings establish thermal radiation as a fundamental and unavoidable privacy risk for immersive systems, exposing a critical security gap that bypasses current software-level protections and physical access controls.

---


### 90. [The Efficiency Gap in Byte Modeling](https://arxiv.org/abs/2605.12928)

**<font color=#1a73e8>作者：</font>** Celine Lee, Jing Nathan Yan, Chen Liang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern language models have historically relied on two dominant design choices: subword tokenization and autoregressive (AR) ordering. These design decisions bake in priors that dictate a model's learning. Recently, two alternative paradigms have challenged this: byte-level modeling, which bypasses static statistically-derived token vocabularies, and masked diffusion modeling (MDM), which conducts parallel, non-sequential generation. Their intersection represents a fully end-to-end modality-agnostic generative prototype; however, removing these structural priors incurs a significant computational cost. In this work, we investigate this cost through a compute-matched scaling study. Our results reveal that the performance penalty of byte modeling is not uniform; across scale, the scaling overhead of byte modeling is worse for MDM than for AR. We hypothesize that this disparity stems from context fragility: while AR's stable causal history allows models to naturally rediscover subword patterns, the MDM objective destroys the local contiguity required to efficiently resolve semantics from raw bytes. Our findings from controlled permutation experiments suggest that future modality-agnostic designs must incorporate alternative structural biases to maintain viable scaling trajectories in the byte regime.

---


### 91. [Anatomy-Slot: Unsupervised Anatomical Factorization for Homologous Bilateral Reasoning in Retinal Diagnosis](https://arxiv.org/abs/2605.12929)

**<font color=#1a73e8>作者：</font>** Yingzhe Ma, Xiao Yang, Yuguo Yin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retinal diagnosis is inherently bilateral: clinicians compare homologous structures across eyes (e.g., optic disc asymmetry), yet most deep models operate on monocular representations. We investigate whether explicit structural correspondence improves diagnosis, and propose Anatomy-Slot to operationalize this hypothesis. Anatomy-Slot introduces an unsupervised anatomical bottleneck by decomposing patch tokens into slots and aligning slots across eyes via bidirectional cross-attention. On ODIR-5K with $n=10$ seeds, the method improves AUC by 4.2% over a matched ViT-L baseline (95% CIs; Wilcoxon signed-rank test, $W=0$, $p=0.002$). Pairing disruption and stress testing under Gaussian noise provide controlled tests of correspondence dependence and robustness under corruption. We further report quantitative optic disc grounding on REFUGE and cross-attention localization analysis.

---


### 92. [ATD-Trans: A Geographically Grounded Japanese-English Travelogue Translation Dataset](https://arxiv.org/abs/2605.12933)

**<font color=#1a73e8>作者：</font>** Shohei Higashiyama, Hiroki Ouchi, Atsushi Fujita 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Geographic text, or textual data rich in geographic (geo-) information is a valuable source for various geographic applications, e.g., tourism management. Making such information accessible to speakers of other languages further enhances its utility; thus, accurate machine translation (MT) is essential for equity in multilingual geo-information access. To facilitate in-depth analysis for geographic text, we introduce ATD-Trans, a geographically grounded Japanese--English travelogue translation dataset, which enables evaluation of MT quality at both the overall and geo-entity levels across domestic (within Japan) and overseas regions. Our experiments on existing language models examine two factors: model language focus and geographic regions. The results highlight advantages of Japanese-enhanced models and greater difficulty in translating domestic-region geo-entities mentioned in travel blogs.

---


### 93. [AuraMask: An Extensible Pipeline for Developing Aesthetic Anti-Facial Recognition Image Filters](https://arxiv.org/abs/2605.12937)

**<font color=#1a73e8>作者：</font>** Jacob Lagogiannis, William Agnew, Rosa I. Arriaga 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Anti-facial recognition (AFR) image filters alter images in ways that are subtle to people but blinding to computer vision. Yet, despite widespread interest in these technologies to subvert surveillance, users rarely use them in practice -- because the ``subtle'' alterations are visible enough to conflict with users' self-presentation goals. To address this challenge, we propose AuraMask: a novel approach to creating AFR filters that are both adversarially effective and aesthetically acceptable. Using AuraMask, we produce 40 ``aesthetic'' filters that emulate popular ``one-click'' Instagram image filters. We show that AuraMask filters meet or exceed the adversarial effectiveness of prior methods against open-source facial recognition models. Moreover, in a controlled online user study ($N=630$) we confirm these filters achieve significantly higher user acceptance than prior methods. Lastly, we provide our AFR pipeline to the community for accelerated research in adversarially effective and aesthetically acceptable protections.

---


### 94. [CRePE: Curved Ray Expectation Positional Encoding for Unified-Camera-Controlled Video Generation](https://arxiv.org/abs/2605.12938)

**<font color=#1a73e8>作者：</font>** Seonghyun Jin, Youngmin Kim, Sunwoo Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-conditioned video generation requires positional encoding that remains reliable under changes in camera motion, lens configuration, and scene structure. However, existing attention-level camera encodings either provide ray-only camera signals or rely on pinhole camera geometry, limiting their applicability to general camera control under the Unified Camera Model, including wide-angle and fisheye lenses. To address this limitation, we propose Curved Ray Expectation Positional Encoding (CRePE). CRePE represents each image token as a depth-aware positional distribution along its source ray, providing a Unified Camera Model-compatible positional encoding that captures the projected-path geometry induced by wide-angle and fisheye cameras. CRePE is implemented through a Geometric Attention Adapter added to frozen video DiTs, injecting token-wise scene-distance information into selected attention layers and stabilizing it with pseudo supervision from a monocular geometry foundation model. This design leads to more stable camera control and improves several geometry-aware and perceptual-quality metrics, while remaining competitive on video-quality metrics. Controlled positional-encoding ablations show a better overall average rank than a RayRoPE-style endpoint PE baseline, demonstrating the effectiveness of UCM-aware projected-path integration across diverse camera models. Furthermore, by extending the same positional-encoding pathway to external geometry control through Radial MixForcing, CRePE supports external radial-map control for scene-geometry-conditioned generation and source-video motion transfer beyond camera control.

---


### 95. [DirectTryOn: One-Step Virtual Try-On via Straightened Conditional Transport](https://arxiv.org/abs/2605.12939)

**<font color=#1a73e8>作者：</font>** Xianbing Sun, Jiahui Zhan, Liqing Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent diffusion- and flow-based VTON methods achieve strong results with pretrained generative models, but their reliance on multi-step sampling incurs high inference cost, while existing acceleration methods largely overlook the intrinsic structure of the try-on task. In this paper, we highlight a key observation: VTON outputs are highly constrained by the conditional inputs, suggesting that the conditional sampling trajectory can be much straighter than that in general image generation, making one-step generation a natural solution. However, limited task-specific data makes training from scratch impractical, forcing existing methods to fine-tune pretrained models whose objectives do not encourage such straight conditional trajectories. Thus, the deviation from an ideal straight path mainly comes from the mismatch between pretrained base models and the conditional nature of try-on generation, rather than from the task itself. Motivated by this insight, we encourage straighter VTON sampling trajectories through three targeted modifications: pure conditional transport, a garment preservation loss, and a self consistency loss. We further introduce a one-step distillation stage. Extensive experiments show that our method achieves state-of-the-art performance with one-step sampling, establishing a new standard for efficient and high-quality VTON.

---


### 96. [From Compression to Accountability: Harmless Copyright Protection for Dataset Distillation](https://arxiv.org/abs/2605.12942)

**<font color=#1a73e8>作者：</font>** Yan Liang, Ziyuan Yang, Mengyu Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large-scale datasets have been a key driving force behind the rapid progress of deep learning, but their storage, computational, and energy costs have become increasingly prohibitive. Dataset distillation (DD) mitigates this problem by synthesizing compact yet informative datasets, thereby enabling efficient model training and storage. However, the ease of copying and distributing distilled datasets introduces serious risks of copyright infringement and data leakage. Existing protection methods are primarily designed for raw datasets rather than distilled datasets, and typically rely on backdoor-triggered malicious behaviors, which may raise security concerns. In this paper, we observe that deep neural networks tend to memorize subpopulation distributions during training, resulting in a systematic prediction bias, where models perform better on samples aligned with memorized subpopulations. Motivated by this observation, we propose SubPopMark, a harmless subpopulation-driven protection framework for distilled datasets. SubPopMark consists of two stages. First, the Copyright Verification Marker(CVM) optimization stage injects a class-consistent subpopulation bias while preserving the original optimization trajectory. Second, the User-Specific Tracing Marker (USTM) optimization stage further introduces user-distinguishable perturbations into the CVM-augmented data. To enable black-box verification and tracing, we construct a reference behavior bank by collecting model outputs over carefully designed test sets that cover both standard and subpopulation-shifted data distributions. The provenance of a suspicious model is then inferred by comparing its output behavior signature with the bank and identifying the most consistent reference behavior pattern.

---


### 97. [Reinforced Collaboration in Multi-Agent Flow Networks](https://arxiv.org/abs/2605.12943)

**<font color=#1a73e8>作者：</font>** Zheng Wang, Yuang Liu, Yangkai Ding  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems provide a powerful way to extend large language models (LLMs) by decomposing a complex task into specialized subtasks handled by different agents. However, their performance is often hindered by error propagation, arising from suboptimal workflow design or inaccurate agent outputs, which can propagate through the agent collaboration process and degrade final results. To address the challenges, we present MANGO (Multi-Agent Network Gradient Optimization), a data-driven framework that organizes and refines agent collaboration via a flow network constructed from past successful workflows. MANGO integrates reinforcement learning and textual gradients to jointly optimize workflow paths and agent behaviors, while a skipping mechanism prevents redundant updates to well-optimized agents for improving efficiency. Extensive experiments on seven benchmarks show that MANGO achieves up to 12.8% performance improvement over state-of-the-art baselines, enhances efficiency by 47.4%, and generalizes effectively to unseen domains. Our code and datasets are publicly available at this https URL.

---


### 98. [Separating Shortcut Transition from Cross-Family OOD Failure in a Minimal Model](https://arxiv.org/abs/2605.12945)

**<font color=#1a73e8>作者：</font>** Hongmin Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Shortcut features are often invoked to explain out-of-distribution (OOD) failure, but training correlation, learned shortcut use, and test-time failure need not coincide. We study a minimal binary model with one invariant coordinate and one family-dependent shortcut coordinate. In the deterministic regime, positive average shortcut correlation pulls logistic ERM toward positive shortcut weight, but ridge regularization keeps the classifier invariant-dominated and prevents deterministic OOD failure. When the invariant coordinate is noisy, ridge-logistic ERM switches to the shortcut rule once the training shortcut signal exceeds the invariant signal. Whether that transition causes failure depends on the held-out family: weaker shortcut correlation yields positive excess risk, and sign-flipped families yield above-chance error. Synthetic checks match these analytic regimes and show that the same training-side transition can have different held-out consequences. The model separates shortcut attraction, shortcut-rule transition, and cross-family OOD failure.

---


### 99. [Debunking Grad-ECLIP: A Comprehensive Study on Its Incorrectness and Fundamental Principles for Model Interpretation](https://arxiv.org/abs/2605.12952)

**<font color=#1a73e8>作者：</font>** Yongjin Cui, Xiaohui Fan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Grad-ECLIP is published at ICML 2024 and represents a new Transformer interpretation technical route (intermediate features-based). First, this paper demonstrates that the intermediate features-based technical route is not a novel one. Based on the existing attention-based route, we have developed Attention-ECLIP, which is completely equivalent to Grad-ECLIP but with simpler computation. Both through formal derivation and experimental validation, we prove that the intermediate feature-based route represented by Grad-ECLIP is actually an equivalent variant of the attention-based route. Next, this paper demonstrates that the Grad-ECLIP method is flawed. The model interpretation results obtained by Grad-ECLIP are not those of the original model, and the interpretation results are misaligned with the model's performance. We analyze the causes of Grad-ECLIP's flaws and propose, or rather, explicitly emphasize two fundamental principles that model interpretation should adhere to in order to avoid similar errors.

---


### 100. [AdaFocus: Adaptive Relevance-Diversity Sampling with Zero-Cache Look-back for Efficient Long Video Understanding](https://arxiv.org/abs/2605.12954)

**<font color=#1a73e8>作者：</font>** Xiao Yang, Yingzhe Ma, Haoxuan Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long video understanding is heavily bottlenecked by a rigid one-shot paradigm: existing methods either densely encode videos at prohibitive memory and latency costs, or aggressively compress them into sparse frame sets that irreversibly discard fine-grained evidence needed for downstream reasoning. Consequently, current models struggle to simultaneously balance temporal coverage, visual details, and computational efficiency.
We propose AdaFocus, an efficient framework that rethinks long-video understanding as progressive evidence acquisition rather than one-pass encoding. AdaFocus relies on two tightly coupled components. First, a Query-Aware Adaptive Relevance-Diversity sampler (AdaRD) produces a compact yet informative video preview, adaptively switching to global clustering when the query lacks reliable local grounding. Second, instead of caching exhaustive frame sequences in memory, AdaFocus introduces an uncertainty-triggered refinement mechanism. It performs targeted look-back only when the model is not confident, retrieving high-resolution evidence directly from disk via a zero-cache I/O design. This turns discarded visual details from an irreversible loss into on-demand recoverable evidence without paying the cost of exhaustive preloading.
Experiments on seven standard long-video benchmarks show that AdaFocus delivers a substantially better efficiency-accuracy trade-off than strong baselines. Compared with conventional dense encoding, AdaFocus achieves improved task performance (e.g., +2.59 accuracy on VideoMME, +8.39 mIoU on Charades-STA over single-pass inference) while reducing visual token consumption by ~33x and eliminating the need for in-memory frame pre-caching through its zero-cache disk retrieval design. These findings suggest that progressive preview combined with zero-cache evidence refinement is a highly effective paradigm for scalable multimedia reasoning.

---


> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-328](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
