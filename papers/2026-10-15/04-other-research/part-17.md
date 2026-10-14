# 📦 其他研究 | 2026年10月15日

> 本类共 **810** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**801-810**（第 17/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | **801-810**

---

### 801. [Depth Memory](https://arxiv.org/abs/2610.18809)

**<font color=#1a73e8>作者：</font>** David González-Martínez, Philipp Nazari, T. Konstantin Rusch 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Residual connections propagate information through a network by additively accumulating layer outputs. Recently proposed alternatives, such as Manifold-Constrained Hyper-Connections (mHC) and Attention Residuals (AttnRes), instead use more expressive depth aggregation mechanisms that improve language modeling performance at scale. In this work, we consider the mixing of representations over depth as a problem of storing and retrieving information across layers. Formalizing this perspective, we introduce Depth Memory (DM), a unified framework that describes the standard pre-layer-norm (PreLN) transformer, mHC, and AttnRes in terms of streams that carry representations through the network. One such stream, for example, could be an explicit memory stream that is queried to enrich the input to every layer, and whose output is subsequently written back into the memory for use by later layers. For AttnRes, this memory stream is a growing cache of explicit layer representations. For mHC, it is an expanded residual stream. Building on this view, we propose Linear Depth Memory (LDM), which formulates information retrieval across depth as a regression problem solved using recursive least squares. The resulting architecture propagates three streams across depth: the standard residual stream, a linear associative memory stream, and an inverse covariance stream. For high-throughput training and inference, we propose a hardware-aware implementation of LDM that reduces peak activation memory and memory traffic. LDM consistently achieves the lowest perplexities among PreLN, mHC and AttnRes baselines at the 400M and 1.5B parameter scales, alongside competitive zero-shot accuracy.

---


### 802. [Statistical Vignettes on the Grokking Phenomenon](https://arxiv.org/abs/2610.18811)

**<font color=#1a73e8>作者：</font>** Baye Malick Gning, Elvis Dohmatob  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we study grokking in a simple, analytically tractable setting whose rich phenomenology allows us to disentangle the effects of initialization, signal strength, weight decay, sample size, and input dimension. These factors can produce superficially similar learning curves through distinct mechanisms, complicating their interpretation. Our analysis distinguishes early fitting through nuisance features, core feature learning, and delayed generalization. We identify sharp conditions under which grokking provably occurs and derive analytic asymptotic expressions for the lengths of the generalization plateaus. Our results also characterize regimes of early generalization and failure to reach a prescribed test accuracy target. We show that the interpolation edge constitutes a distinct dynamical regime, where vanishing spectral gaps separate core learning from generalization, helping clarify the role of proximity to interpolation in existing accounts of grokking. The resulting picture is analogous to fast and slow phases in chemical kinetics and suggests that the lazy-to-rich transition discussed in the literature may reflect a similar separation of dynamical time scales. Our theoretical results are faithfully supported by extensive experiments.

---


### 803. [DuplexBridge: Coordinating Understanding and Generation for Unified Image Editing](https://arxiv.org/abs/2610.18819)

**<font color=#1a73e8>作者：</font>** Yidi Liu, Jie Xiao, Chaojie Mao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Complex image editing requires faithful task interpretation and accurate execution, but a failed edit does not reveal which responsibility failed. We present DuplexBridge, which uses a unified model's own understanding capability to enhance prompts for its own generation capability, without an external understanding module. A source-grounded bridge specifies targets, final-state changes, and preservation constraints. Understanding is supervised on fidelity to the original request without observing the generated image; generation is supervised on execution of the condition it actually receives. Reciprocal trust checks selectively admit global task feedback to each role while retaining independently valid local supervision. We introduce CE-Bench, a 1,200-task benchmark measuring joint satisfaction of task-derived change and preservation requirements. Across three model configurations, the full system improves complete compliance over direct editors by 21.75-25.75 percentage points, with gains also observed on KRIS-Bench, RISEBench, ImgEdit, and GEdit-Bench. From a common supervised Wan-Image initialization, gated joint training reaches 77.08% complete compliance, compared with 70.92% without gates and 75.00% when generation-local supervision instead checks the original task with both gates retained. These results support distinct local responsibilities and selective shared feedback for joint understanding-generation adaptation.

---


### 804. [AegisAsync: Symbolic Async-Event Simulation for Risks in Python Asynchronous Programs](https://arxiv.org/abs/2610.18831)

**<font color=#1a73e8>作者：</font>** Baihong Chen, Wen Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security and robustness risks in Python async programs depend on event order, object identity, and execution after exceptions or cancellation. Detecting these risks requires connecting related operations across function calls and tracking their effects along execution paths. We present AegisAsync, a bytecode-based analysis of Python async risks for CPython 3.10-3.14. Its Async Event Transition Graph combines bytecode control flow, resolved calls, async events, and symbolic object relations. Bounded path-local simulation tracks event order and object states and explores cancellation at await suspensions. Six detector plugins evaluate the resulting traces and states to produce candidates with supporting witnesses. On AsyncBench, our benchmark of 180 labeled risks, AegisAsync detects all labeled risks with zero false positives on each of the five versions. Across five path budgets on 2,500 PyPI package versions, source review confirms 457 of 910 AegisAsync candidate records (50.2%), representing 457 unique bugs; across three flake8-async samples, 70 of 2,187 review judgments are confirmed (3.2%). By submission, 166 PoCs reproduce AegisAsync findings, and we have reported 157 bugs to developers, of which 16 have been confirmed and fixed.

---


### 805. [Scaling Online Optimal Transport Minibatches for Flow Matching](https://arxiv.org/abs/2610.18838)

**<font color=#1a73e8>作者：</font>** Peter Chen, Sergey Levine  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A central challenge in scaling flow models is maintaining stability in training and integration. In flow matching, this stability depends critically on how source samples are paired with data. Independent random pairing introduces substantial stochasticity, motivating minibatch optimal transport (OT) to construct online source-target couplings that reduce this randomness (Tong et al., 2024). However, as applications extend to larger and higher-dimensional datasets, small minibatches can limit these benefits, while scaling the coupling to substantially larger minibatches at every iteration is computationally prohibitive. Moreover, how OT coupling affects the full stochastic gradient and integration remains theoretically unresolved. In this work, we develop a scalable online entropic OT approximation that enables substantially larger source-target couplings while preserving the benefits of OT. We close the theoretical gap for both unregularized and entropic OT by proving strict reductions in full stochastic-gradient variance and integration error relative to independent pairing, and further characterize how these improvements strengthen as the online coupling minibatch grows. Experiments on single-cell gene interpolation-flow and image-flow training validate these predictions, showing that larger online couplings consistently improve training stability and final generation performance.

---


### 806. [Fast Rates for Offline Q-Learning with KL Regularization](https://arxiv.org/abs/2610.18839)

**<font color=#1a73e8>作者：</font>** Yize Hao, Guangxin Jiang, Shuang Qiu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper investigates offline Q-learning for finite-horizon Markov decision processes with Kullback-Leibler (KL) regularization. Recent studies have shown that KL regularization can yield fast rates in offline decision-making problems. However, it remains unclear whether Q-learning, which adopts incremental stochastic approximation updates, can achieve such fast rates in the offline setting. We first propose KL-regularized Q-Learning (KLQ), a simple variant of classical Q-learning. By exploiting KL regularization, we prove that KLQ achieves a sample complexity of $\widetilde{O}(1/\epsilon)$ without explicit pessimism. This guarantee, however, has an exponential dependence on the KL regularization parameter and the horizon. To address this limitation, we further propose KL-regularized Pessimistic Q-Learning (KLPQ), which incorporates pessimism into KLQ. We prove that KLPQ retains the same \(\widetilde O(1/\epsilon)\) rate while removing the explicit exponential dependence, thereby further improving the sample complexity. To the best of our knowledge, these results establish the first fast-rate guarantees for offline Q-learning in tabular finite-horizon KL-regularized MDPs.

---


### 807. [Who Improves the Robot? Toward Physical Recursive Self-Improvement](https://arxiv.org/abs/2610.18842)

**<font color=#1a73e8>作者：</font>** Hai Zhou, Fan Yang, Zeyi Chen 等 30 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Robots are increasingly autonomous in task execution, yet their improvement remains largely human-driven. This study investigates Physical Recursive Self-Improvement (Physical RSI), in which physical experience guides lasting updates to both a robot's capabilities and its improvement procedure, making subsequent improvement more effective across tasks. Physical RSI faces challenges from noisy observations, continuous dynamics, costly trials, and irreversible consequences. We present an L0-L5 framework that differentiates capability-level from meta-level updates and within-task from across-task gains, reserving L5 for independently verified recursive gain. We study existing methods around harness adaptation and model training, alongside safety and control mechanisms that govern execution and successive updates. Our analysis reveals that, despite substantial progress in self-improvement, the surveyed literature does not yet demonstrate Physical RSI as defined by our framework. We identify research priorities in reliable feedback, causal attribution, safety preservation, and benchmarking, outlining a path toward robots that autonomously improve how they learn while ensuring safety. The GitHub repository for Physical RSI is available at this https URL.

---


### 808. [WorldRecon: Generative Multi-View Mesh Reconstruction for Large-Scale 3D World](https://arxiv.org/abs/2610.18846)

**<font color=#1a73e8>作者：</font>** Mengchen Zhang, Yang Li, Chunshi Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing complete, high-quality meshes of large-scale scenes from unposed multi-view images requires faithful geometric grounding while plausibly completing surfaces that are unobserved or only sparsely captured. We present WorldRecon, a generative multi-view reconstruction framework for recovering complete, large-scale 3D scene meshes from unposed RGB images. WorldRecon uses a coarse, noisy global point cloud and camera poses estimated from the input images by a reconstruction model as a global scaffold for whole-scene generation and partitions it into overlapping spatial blocks. To robustly leverage these imperfect geometric priors, we equip the native 3D generative model TRELLIS.2 with a dedicated reconstruction-based conditioning architecture that generates each block from its local point-cloud crop and block-relevant image observations, producing sparse structure, detailed geometry, and PBR materials. To maintain scene-level coherence, we introduce neighbour-aware latent inpainting and a causal world-generation procedure that propagates structural, geometric, and material context across overlapping blocks. Together, these designs scale multi-view generative reconstruction to large-scale scenes, yielding coherent, unified meshes. Extensive experiments demonstrate that WorldRecon achieves state-of-the-art reconstruction performance, reducing Chamfer distance by 14.9% and 43.1% while improving F-score by 17.3% and 12.0% over the strongest baselines on synthetic and real-world indoor scenes, respectively, thereby demonstrating faithful and complete generative reconstruction as well as strong sim-to-real generalization. Project page: this https URL.

---


### 809. [Exact Topological Compliance: Generating Persistence-Equivalent Graphs](https://arxiv.org/abs/2610.18856)

**<font color=#1a73e8>作者：</font>** Mattie Ji, Indradyumna Roy, Vikas Garg  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Persistent homology summarizes the topological evolution of a graph as persistence diagrams (PDs). Generating graphs whose topology matches a target descriptor is increasingly important, yet existing topology-aware generative models rely on soft regularization, producing graphs whose PDs may only be approximately similar. We initiate a principled investigation of the generation problem: produce graphs that realize a target PD exactly. We propose two approaches guided by the implicit local and global constraints a target PD imposes. The local approach builds degree-based PD-equivalent graphs iteratively, and we prove that every output realizes the target PD and that every degree-based PD-equivalent graph is reachable. However, as shown thereafter, local generation necessarily trades off between sample diversity and reaching infeasible states. We therefore recast generation as a global constraint satisfaction problem with a complete encoding solvable by modern constraint programming solvers. This is applicable to any vertex-based permutation equivariant filtration scheme and is minimal under the degree filtration. Experiments on four standard graph generation benchmarks confirm that both methods realize the target PD exactly. Together, our methods provide a principled treatment of strict topology-compliant graph generation. Code is available at this https URL.

---


### 810. [Cepheid: Decoupling Scale from Structure for Cross-Family Motion Completion](https://arxiv.org/abs/2610.18871)

**<font color=#1a73e8>作者：</font>** Chih-Hai Su, Tsung-Wei Ke, Yu-Lun Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse-to-dense motion completion recovers dense mesh motion from sparse vertex displacements. Residual priors trained on one geometry family frequently fail to beat parameter-free harmonic extension off-family. Moreover, cross-family training meets a scaling barrier: residual amplitude varies by more than an order of magnitude across geometry families and collapses as observations become denser. Since this scale depends on unknown target motion, it cannot be measured directly at test time. We decouple residual structure from physical scale by learning a dimensionless prior, estimating amplitude from observables and a lightweight correction fitted only on training sources. Our unified model surpasses harmonic extension across all evaluated families, including unseen cloth and legged bodies, without skeletons, registration, or cross-mesh correspondence. The same prior applies without retraining to point-tracked animal video and a robot grasping a soft body. Project page: this https URL

---


> [!TIP]
> 当前位于：**801-810**（第 17/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | **801-810**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
