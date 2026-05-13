# 📦 其他研究 | 2026年05月14日

> 本类共 **396** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-396](./part-08.md)

---

### 1. [Interpretable EEG Microstate Discovery via Variational Deep Embedding: A Systematic Architecture Search with Multi-Quadrant Evaluation](https://arxiv.org/abs/2605.10947)

**<font color=#1a73e8>作者：</font>** Saheed Faremi, Andrea Visentin, Luca Longo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> EEG microstate analysis segments continuous brain electrical activity into brief, quasi-stable topographic configurations that reflect discrete functional brain states. Conventional approaches such as Modified K-Means operate directly in electrode space with hard assignment, offering no learned latent representation, no generative decoder, and no mechanism to decode latent configurations into verifiable scalp topographies, limiting both model transparency and interpretability. To address this, we present a Convolutional Variational Deep Embedding (Conv-VaDE) model that jointly learns topographic reconstruction and probabilistic soft clustering in a shared latent space. Conv-VaDE enables generative decoding of cluster prototypes into verifiable scalp topographies, replacing opaque hard partitioning with probabilistic soft assignment. A polarity invariance scheme and a four-dimensional grid search over cluster count (K from 3 to 20), latent dimensionality, network depth, and channel width are conducted to systematically reveal how each architectural design choice shapes the quality, stability, and interpretability of learned EEG microstate representations. The model is evaluated on the LEMON resting-state eyes-closed EEG dataset with ten participants using topographic template formation, clustering stability, and global explained variance (GEV). The architecture search reveals that depth L = 4 appears consistently across all 18 best-performing configurations, yielding a best-case GEV of 0.730 and a silhouette of 0.229 at K = 4 across the model sweeps, where moderately deep networks with compact channel widths and small latent dimensionality dominate across the full K range. These results establish that principled architecture search, rather than model scale, is the key to interpretable and stable EEG microstate discovery via variational deep embedding.

---


### 2. [QuIDE: Mastering the Quantized Intelligence Trade-off via Active Optimization](https://arxiv.org/abs/2605.10959)

**<font color=#1a73e8>作者：</font>** Xiantao Jiang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> There is currently no unified metric for evaluating the efficiency of quantized neural networks. We propose QuIDE, built around the Intelligence Index I = (C x P)/log_2(T+1), which collapses the compression-accuracy-latency trade-off into a single score. Experiments across six settings -- SimpleCNN (MNIST, CIFAR), ResNet-18 (ImageNet-1K), and Llama-3-8B -- show a task-dependent Pareto Knee. 4-bit quantization is optimal for MNIST and large LLMs, while 8-bit is the sweet spot for complex CNN tasks (ResNet-18 on ImageNet), where 4-bit PTQ collapses accuracy catastrophically. The accuracy-gated variant I' correctly flags these non-viable configurations that the raw I would reward. QuIDE provides a reproducible evaluation protocol and a ready-to-use fitness function for mixed-precision search.

---


### 3. [Vertex-Softmax: Tight Transformer Verification via Exact Softmax Optimization](https://arxiv.org/abs/2605.10974)

**<font color=#1a73e8>作者：</font>** Navid Rezazadeh, Arash Gholami Davoodi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Certified verification of transformer attention requires bounding the softmax function over interval constraints on the pre-softmax scores. Existing verifiers relax softmax ndependently of the downstream objective, leaving avoidable slack. We prove that the exact optimum of this score-box problem is attained at a vertex of the constraint box, and establish a threshold structure theorem showing that, after sorting the objective coefficients, the optimum lies among only linearly many candidates, yielding the Vertex-Softmax primitive with log-linear complexity in the sequence length. We further prove a formal optimality result showing that Vertex-Softmax is the tightest sound bound obtainable from score intervals alone, characterizing precisely what additional structure (score correlations, score-value coupling) is needed for further improvement. Integrated into a CROWN Convex Relaxation based Optimization for Worst-case Neurons)-style verifier with a formal soundness guarantee, Vertex-Softmax significantly improves certified rates and substantially tightens lower bounds across MNIST, Fashion-MNIST, and CIFAR-10 attention models, while consistently matching or outperforming alpha-CROWN and branch-and-bound baselines at a fraction of their cost.

---


### 4. [Hierarchical Multi-Scale Graph Neural Networks: Scalable Heterophilous Learning with Oversmoothing and Oversquashing Mitigation](https://arxiv.org/abs/2605.10975)

**<font color=#1a73e8>作者：</font>** Md Sazzad Hossen, Avimanyu Sahoo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graphs with heterophily, where adjacent nodes carry different labels, are prevalent in real-world applications, from social networks to molecular interactions. However, existing spectral Graph Neural Network (GNN) approaches tailored for heterophilous graph classification suffer from hub-dominated (node with large degree) aggregation and oversmoothing, as their suboptimal polynomial filters introduce approximation errors and blend distant signals. To address the degree-biased aggregation and suboptimal polynomial filtering, we introduce a Hierarchical Multi-view HAAR (HMH), a novel spectral graph-learning framework that scales in near-linear time . HMH first learns feature- and structure-aware signed affinities via a heterophily-aware encoder, then constructs a soft graph hierarchy guided by these embeddings. At each hierarchical level, HMH constructs a sparse, orthonormal, and locality-aware Haar basis to apply learnable spectral filters in the frequency domain. Finally, skip-connection unpooling layers combine outputs from all hierarchical levels back into the original graph, effectively preventing hub domination and long-range signal bottleneck (over-squashing). Experimentation shows that HMH outperforms state-of-the-art spectral baselines, achieving up to a 3% improvement on node classification and 7% points on graph classification datasets, all while maintaining linear scalability.

---


### 5. [$ξ$-DPO: Direct Preference Optimization via Ratio Reward Margin](https://arxiv.org/abs/2605.10981)

**<font color=#1a73e8>作者：</font>** Zhengyuan Fan, Zhonghua Wu, Yuxuan Du 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reference-free preference optimization has emerged as an efficient alternative to reinforcement learning from human feedback, with Simple Preference Optimization(SimPO) demonstrating strong performance by eliminating the explicit reference model through a simple objective. However, the joint tuning of the hyperparameters $\beta$ and $\gamma$ in SimPO remains a central challenge. We argue that this difficulty arises because the margin formulation in SimPO is not easily interpretable across datasets with different reward gap structures. To better understand this issue, we conduct a comprehensive analysis of SimPO and find that $\beta$ implicitly controls sample filtering, while the effect of $\gamma$ depends on the reward gap structure of the dataset. Motivated by these observations, we propose $\xi$-DPO: Direct preference optimization via ratio reward margin. We first reformulate the preference objective through an equivalent transformation, changing the optimization target from maximizing the likelihood of reward gaps to minimizing the distance between reward gaps and optimal margins. Then, we redefine the reward in a ratio form between the chosen and rejected, which effectively cancels the effect of $\beta$ and yields a bounded and interpretable margin. This margin is called the ratio reward margin and is denoted by $\xi$. Unlike the margin $\gamma$ in SimPO, $\xi$ explicitly represents the desired relative separation between chosen and rejected responses and can be determined from the initial reward gap distribution, avoiding repeated trial-and-error tuning. ....

---


### 6. [Principle-Guided Supervision for Interpretable Uncertainty in Medical Image Segmentation](https://arxiv.org/abs/2605.10984)

**<font color=#1a73e8>作者：</font>** An Sui, Yuzhu Li, Gunter Schumann 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Uncertainty quantification complements model predictions by characterizing their reliability, which is essential for high-stakes decision making such as medical image segmentation. However, most existing methods reduce uncertainty to a scalar confidence estimate, leaving its spatial distribution semantically underconstrained. In this work, we focus on uncertainty interpretability, namely, whether estimated uncertainty behaves in a human-understandable manner with respect to sources of ambiguity. We identify three perception-aligned principles requiring the spatial distribution of uncertainty to reflect: (1) image contrast between structures, (2) severity of image corruption, and (3) geometric complexity in anatomical structures. Accordingly, we develop a principle-guided uncertainty supervision framework (PriUS) based on evidential learning, in which the corresponding supervision objectives are explicitly enforced during training. We further introduce quantitative metrics to measure the consistency between predicted uncertainty and image attributes that induce ambiguity. Experiments on ACDC, ISIC, and WHS datasets showed that, compared with state-of-the-art methods, PriUS produced more consistent uncertainty estimates while maintaining competitive segmentation performance.

---


### 7. [AESOP: Adversarial Execution-path Selection to Overload Deep Learning Pipelines](https://arxiv.org/abs/2605.10987)

**<font color=#1a73e8>作者：</font>** Tingxi Li, Mingfang Ji, Ravishka Shemal Rathnasuriya 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern machine learning deployments increasingly compose specialized models into dynamic inference pipelines, where upstream components produce intermediate predictions that determine the workload and inputs of downstream components. The cost of processing an input is therefore not determined by any single model, but by two coupled factors: the per-inference cost of each invoked component and its workload volume. Because these pipelines run under hard real-time constraints, efficiency is a fundamental requirement for system availability. We show that this structure creates an efficiency-attack surface that existing methods targeting single models cannot exploit: on identical inputs and budgets, path-aware targeting inflates FLOPs by $2,407\times$ while the strongest single-model baseline achieves $117\times$ -- a $20\times$ gap attributable entirely to where the attack is directed. We formalize this as the adversarial path-selection problem and present AESOP, a framework combining vulnerability-guided path ranking with adaptive loss weighting. We evaluate AESOP on five pipelines plus a production-realistic deployment variant with batching, bounded buffering, and confidence-threshold defenses. AESOP achieves up to $2,407\times$ FLOPs and $419\times$ latency inflation in white-box setting and 58$\times$ FLOPs / 17$\times$ latency in gray-box settings. Under system-level defenses, the attack is not neutralized but redirected: pipelines are forced to choose between throughput collapse ($0.578 \to 0.006$ input/s) and $96.7\%$ data loss to sustain throughput.

---


### 8. [Seeing the Needle in the Haystack: Towards Weakly-Supervised Log Instance Anomaly Localization via Counterfactual Perturbation](https://arxiv.org/abs/2605.10988)

**<font color=#1a73e8>作者：</font>** Yutszyuk Wong, Wentai Wu, Yuen-Ying Yeung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Log anomaly detection is a critical task for system operations and security assurance. However, in networked systems at scale, log data are generated at massive scale while instance-level annotations are prohibitively expensive, posing great difficulties to fine-grained anomaly localization. To address this challenge, we propose LogMILP (Log anomaly localization based on Multi-Instance Learning enhanced by prototypes and Perturbation), a weakly supervised framework that enables both bag-level anomaly detection and instance-level anomaly localization using only bag-level labels. Our method guides the model to pinpoint the critical log entries using prototype-guided structural modeling with counterfactual perturbation consistency regularization, thereby improving localization reliability and interpretability under coarse-grained supervision. Experimental results on three public datasets demonstrate that LogMILP achieves competitive detection performance while yielding significantly more reliable instance-level localization. Our code is open-sourced at this https URL.

---


### 9. [SURGE: Surrogate Gradient Adaptation in Binary Neural Networks](https://arxiv.org/abs/2605.10989)

**<font color=#1a73e8>作者：</font>** Haoyu Huang, Boyu Liu, Linlin Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The training of Binary Neural Networks (BNNs) is fundamentally based on gradient approximation for non-differentiable binarization operations (e.g., sign function). However, prevailing methods including the Straight-Through Estimator (STE) and its improved variants, rely on hand-crafted designs that suffer from gradient mismatch problem and information loss induced by fixed-range gradient clipping. To address this, we propose SURrogate GradiEnt Adaptation (SURGE), a novel learnable gradient compensation framework with theoretical grounding. SURGE mitigates gradient mismatch through auxiliary backpropagation. Specifically, we design a Dual-Path Gradient Compensator (DPGC) that constructs a parallel full-precision auxiliary branch for each binarized layer, decoupling gradient flow via output decomposition during backpropagation. DPGC enables bias-reduced gradient estimation by leveraging the full-precision branch to estimate components beyond STE's first-order approximation. To further enhance training stability, we introduce an Adaptive Gradient Scaler (AGS) based on an optimal scale factor to dynamically balance inter-branch gradient contributions via norm-based scaling. Experiments on image classification, object detection, and language understanding tasks demonstrate that SURGE performs best over state-of-the-art methods.

---


### 10. [Test-Time Personalization: A Diagnostic Framework and Probabilistic Fix for Scaling Failures](https://arxiv.org/abs/2605.10991)

**<font color=#1a73e8>作者：</font>** Linhai Zhang, Yulan He  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing approaches to LLM personalization focus on constructing better personalized models or inputs, while treating inference as a single-shot process. In this work, we study Test-Time Personalization (TTP) along an unexplored axis: scaling inference-time computation by sampling N candidates from a personalized policy model and selecting the best with a personalized reward model. We prove that oracle selection yields expected utility growing logarithmically with the number of sampled candidates, establishing a theoretical ceiling for test-time scaling. However, standard reward models fail to realize this potential. To diagnose why, we derive a unified scaling law that decomposes any reward model's Best-of-N curve into four measurable quantities and reveals two failure modes, user-level collapse (near-constant prediction for some users) and query-level reward hacking (negative correlation with true quality for some queries). Guided by this law, we propose a probabilistic personalized reward model whose learned variance effectively mitigates both failure modes. Experiments confirm both elements of our framework: TTP delivers consistent scaling across multiple policy models and personalized text generation tasks, and our scaling law closely matches observed scaling curves across reward-model variants.

---


### 11. [SkillGen: Verified Inference-Time Agent Skill Synthesis](https://arxiv.org/abs/2605.10999)

**<font color=#1a73e8>作者：</font>** Yuchen Ma, Yue Huang, Han Bao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Skills are a promising way to improve LLM agent capabilities without retraining, while keeping the added procedure reusable and controllable. However, high-quality skills are still largely written by hand. We introduce SkillGen, a multi-agent framework that synthesizes a single auditable skill from trajectories generated by a base agent. The output is a human-readable artifact that can be inspected before use. Rather than merely summarizing trajectories, SkillGen leverages contrastive induction over both successful and failed trajectories to identify reusable success patterns, recurring failure modes, and behaviors that appear in nearby successes but are missing from failures. SkillGen then generates candidate skills and iteratively refines the skill. A key novelty in SkillGen is that we model agent skills as interventions to empirically verify the net effect of skills on the overall performance. Specifically, we compare outcomes on the same instances with and without the skill, so that we account for both repairs (cases where the skill fixes a baseline failure) and regressions (cases where the skill breaks a baseline success). Across a broad range of agents and datasets, SkillGen consistently improves held-out performance, outperforms existing skill-generation baselines, and produces skills that transfer across models.

---


### 12. [Finite Volume-Informed Neural Network Framework for 2D Shallow Water Equations: Rugged Loss Landscapes and the Importance of Data Guidance](https://arxiv.org/abs/2605.11001)

**<font color=#1a73e8>作者：</font>** Xiaofeng Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) are a simple surrogate-modelling paradigm for partial differential equations, but their standard strong-form residual formulation is ill suited to the shallow water equations (SWE). It cannot enforce local conservation, handle discontinuities, or leverage the boundary-conforming unstructured meshes used in real-world applications. We introduce ``Data-Guided FVM-PINN'', a framework that replaces the strong-form residual with a differentiable, well-balanced Roe Riemann-solver finite-volume (FVM) loss evaluated on unstructured meshes. The major finding is that physics-only FVM-PINN training often fails on realistic 2D problems: the network collapses to a trivial low-momentum state that nearly satisfies the FVM-PINN residual but bears no resemblance to the true flow. A loss-landscape diagnostic shows that the FVM-PINN loss at zero momentum is only about $7\times$ larger than at the trained solution, a shallow basin that an ordinary optimizer falls into; adding even sparse data turns this into a $310\times$ separation, breaking the degeneracy. On a 2D block-in-channel benchmark, just $200$ random velocity measurements drop the velocity-field $L_2$ error by $22\times$ versus physics-only; $50$ measurements still deliver a $7\times$ reduction. A controlled ablation isolates the contribution of the FVM-PINN loss: it reduces velocity-field $L_2$ by $\sim$$23\%$ in the sparse-data regime and is essentially neutral when dense reference data is available. On a real-world Savannah River reach ($1306$ cells, $3600$~s simulation, five Manning zones), the framework constructs an accurate surrogate from SRH-2D anchor data, with time-window decomposition reducing error monotonically via progressive initial-condition handoff.

---


### 13. [MT-JailBench: A Modular Benchmark for Understanding Multi-Turn Jailbreak Attacks](https://arxiv.org/abs/2605.11002)

**<font color=#1a73e8>作者：</font>** Xinkai Zhang, Zhipeng Wei, Huanli Gong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-turn jailbreaks exploit the ability of large language models to accumulate and act on conversational context. Instead of stating a harmful request directly, an attacker can gradually steer the conversation toward an unsafe answer. Recent methods demonstrate this risk, but they are usually evaluated as black-box pipelines with different budgets, judges, retry rules, and strategy generation procedures. As a result, it is often unclear whether reported gains reflect stronger attack mechanisms or different experimental conditions. We introduce MT-JailBench, a modular evaluation framework for benchmarking multi-turn jailbreaks under fixed conditions. MT-JailBench implements each attack as five interacting modules: evaluation function, attack strategy, prompt generation, prompt refinement, and flow control. This design enables fair comparison across attack methods and component-wise analysis of what drives attack success. Using MT-JailBench, we find that resource budgets and evaluation functions are major confounders: controlling turns, retries, interactions, sampled strategies, and judges substantially change the ranking of attacks. At the component level, prompt generation accounts for most performance variation, while refinement and flow control provide moderate gains. We also find that explicit dynamic strategy generation is not always necessary; stochastic sampling from a fixed strategy can rival more elaborate diversification mechanisms. Finally, recomposing the best components yields a strong attack configuration that outperforms its source attacks and generalizes across diverse target LLMs. MT-JailBench therefore provides a modular framework for comparing multi-turn jailbreaks, understanding the impact of components, and guiding stronger red-teaming evaluations.

---


### 14. [The Authorization-Execution Gap Is a Major Safety and Security Problem in Open-World Agents](https://arxiv.org/abs/2605.11003)

**<font color=#1a73e8>作者：</font>** Baoyuan Wu, Qingshan Liu, Adel Bibi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This position paper argues that the Authorization-Execution Gap (AEG) is a major safety and security problem in open-world agents. The AEG is the divergence between what a principal intends to authorize and what an open-world agent ultimately executes. Because such agents act autonomously across tools, persistent state, and multi-agent handoffs, even small instances of authorization divergence can cause harm that is difficult or impossible to undo. We argue that many observed agent failures can be traced to three structural sources of AEG: delegation-level incompleteness, channel-level corruption, and composition-level fragmentation. The same observed failure may arise from any of these sources. Without identifying the source, a defense targeting the symptom alone cannot address the underlying cause. Agent safety and security should therefore emphasize source-oriented diagnosis and defense. Because the structural sources of AEG arise dynamically during execution, this approach necessarily requires authorization integrity checks applied during execution, rather than relying solely on one-shot upfront filtering or post-hoc audit. For NeurIPS, the implication is that papers on open-world agents should report not only outcome-level metrics such as task success or attack resistance, but also process-level evidence showing where AEG was detected, constrained, and attributed to a structural source during execution.

---


### 15. [RT-Transformer: The Transformer Block as a Spherical State Estimator](https://arxiv.org/abs/2605.11007)

**<font color=#1a73e8>作者：</font>** Peter Racioppo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We show that the core components of the Transformer block -- attention, residual connections, and normalization -- arise naturally from a single geometric estimation problem. Modeling the latent state as a direction on the hypersphere, with noise defined in the tangent plane at the current estimate, yields a precision-weighted directional inference procedure in which attention aggregates evidence, residual connections implement incremental state updates, and normalization retracts the updated state back onto the hypersphere. Together, these components follow from the geometry of the estimation problem rather than being introduced as independent architectural choices.

---


### 16. [When and How to Canonize: A Generalization Perspective](https://arxiv.org/abs/2605.11008)

**<font color=#1a73e8>作者：</font>** Yonatan Sverdlov, Benjamin Friedman, Snir Hordan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While invariant architectures are standard for processing symmetric data, there is growing interest in achieving invariance by applying group averaging or canonization to non-invariant backbones. However, the theoretical generalization properties of these alternative strategies remain poorly understood. We introduce a theoretical framework to analyze the generalization error of these methods by bounding their covering numbers. We establish a rigorous generalization hierarchy: the error bounds of canonized models are at best equal to the error bounds of structurally invariant and group-averaged models, and at worst equal to the bounds of non-invariant baselines. Furthermore, we show that there exist optimal canonizations which attain the optimal error bounds, and poor canonizations which attain the non-invariant error bounds, and that this depends on the regularity of the canonization. Finally, applying this framework to permutation groups in point cloud processing, we rigorously prove that the covering number of lexicographical sorting grows exponentially with point cloud dimension, whereas Hilbert curve canonization guarantees polynomial growth. This provides the first formal theoretical justification for the empirical success of Hilbert curve serialization in state-of-the-art point cloud architectures. We conclude with experiments that support our theoretical claims.
Code is available at this https URL

---


### 17. [ACSAC: Adaptive Chunk Size Actor-Critic with Causal Transformer Q-Network](https://arxiv.org/abs/2605.11009)

**<font color=#1a73e8>作者：</font>** Qian Chen, Junqiao Zhao, Hongtu Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon, sparse-reward tasks pose a fundamental challenge for reinforcement learning, since single-step TD learning suffers from bootstrapping error accumulation across successive Bellman updates. Actor-critic methods with action chunking address this by operating over temporally extended actions, which reduce the effective horizon, enable fast value backups, and support temporally consistent exploration. However, existing methods rely on a fixed chunk size and therefore cannot adaptively balance reactivity against temporal consistency. A large fixed chunk size reduces responsiveness to new observations, while a small one produces incoherent motions, forcing task-specific tuning of the chunk size. To address this limitation, we propose Adaptive Chunk Size Actor-Critic (ACSAC). ACSAC leverages a causal Transformer critic to evaluate expected returns for action chunks of different sizes. At each chunk boundary, it adaptively selects the chunk size that maximizes the expected return, supporting flexible, state-dependent chunk sizes without task-specific tuning. We prove that the ACSAC Bellman operator is a contraction whose unique fixed point is the action-value function of the adaptive policy. Experiments on OGBench demonstrate that ACSAC achieves state-of-the-art performance on long-horizon, sparse-reward manipulation tasks across both offline RL and offline-to-online RL settings.

---


### 18. [A Comparative Study of Federated Learning Aggregation Strategies under Homogeneous and Heterogeneous Data Distributions](https://arxiv.org/abs/2605.11010)

**<font color=#1a73e8>作者：</font>** Antonios Makris, Christos Dousis, Emmanouil Kritharakis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning has emerged as a transformative paradigm for collaborative machine learning across distributed environments. However, its performance is strongly influenced by the aggregation strategy used to combine local model updates at the server, which directly affects learning performance, robustness, and system behavior. This work presents a comprehensive experimental comparison of widely used federated aggregation strategies under both homogeneous and heterogeneous data distributions. Using benchmark image classification datasets, we analyze how different aggregation mechanisms respond to varying degrees of data heterogeneity, examining their impact on centralized accuracy and loss, and system-level efficiency metrics, including aggregation, training, and communication time. The results demonstrate that aggregation strategies exhibit distinct trade-offs across datasets and data distributions, with their effectiveness varying according to dataset characteristics and operating conditions.

---


### 19. [Backbone-Equated Diffusion OOD via Sparse Internal Snapshots](https://arxiv.org/abs/2605.11014)

**<font color=#1a73e8>作者：</font>** Yadang Alexis Rouzoumka, Jean Pinsolle, Eugénie Terreaux 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fair comparison between diffusion-based OOD detectors is challenging, as conclusions can vary with backbone choice, corruption parameterization, and test-time budget. We address this issue through a Mutualized Backbone-Equated (MBE) protocol that aligns canonical corruption levels and logical test-time cost across diffusion backbones. Within this setting, we introduce Canonical Feature Snapshots (CFS), a family of detectors that probes a frozen diffusion backbone using only a tiny number of native internal activations at canonical low-noise levels. On a controlled CIFAR-scale benchmark, the strongest one-forward CFS variant is CFS(1x2), while an even smaller decoder-only variant remains highly competitive. This shows that much of the relative-OOD signal exposed by frozen diffusion backbones is concentrated in a small number of sparse internal states, rather than requiring full denoising trajectories or high-capacity downstream heads. We further provide a local diagnostic theory explaining these observations through conditional encoder-decoder complementarity, diagonal-score separation, and low-noise corruption stability. The official implementation is available at this https URL.

---


### 20. [DCVD: Dual-Channel Cross-Modal Fusion for Joint Vulnerability Detection and Localization](https://arxiv.org/abs/2605.11015)

**<font color=#1a73e8>作者：</font>** Wenxin Tang, Wenbin Li, Junliang Liu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Software vulnerability detection plays a critical role in ensuring system security, where real-world auditing requires not only determining whether a function is vulnerable but also pinpointing the specific lines responsible. However, existing approaches either rely on a single information source -- sequential, structural, or semantic -- failing to jointly exploit the complementary strengths across modalities, or treat statement-level localization merely as a byproduct of function-level detection without explicit line-level supervision. To address these limitations, we propose DCVD (Dual-Channel Cross-Modal Vulnerability Detection), a unified framework that performs joint function-level detection and statement-level localization. DCVD extracts control-dependency and semantic features through two parallel branches and integrates them via contrastive alignment coupled with bidirectional cross-attention, effectively bridging the cross-modal representation gap. It further introduces explicit supervision signals at both the function and statement levels, enabling collaborative optimization across the two granularities. Extensive experiments on a large-scale real-world vulnerability benchmark demonstrate that DCVD consistently outperforms state-of-the-art methods on both function-level detection and statement-level localization. Our code is available at this https URL.

---


### 21. [Simpson's Paradox in Behavioral Curves: How Aggregation Distorts Parametric Models of User Dynamics](https://arxiv.org/abs/2605.11017)

**<font color=#1a73e8>作者：</font>** Chao Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Behavioral curve modeling -- fitting parametric functions to engagement-versus-exposure data -- is standard practice in recommendation, advertising, and clinical dosing. We show that aggregation introduces a systematic distortion: Simpson's paradox in behavioral curves. On Goodreads (3.3M users, 9 genres), individual users peak at n* approximately 11 exposures while the aggregate peaks at n* approximately 34 -- a 3x gap driven by survival bias. Amazon Electronics (18M reviews) shows a 5.3x distortion. MovieLens-25M (D approximately 1) serves as a negative control, confirming that survival bias -- not aggregation per se -- is the operative mechanism. The distortion is robust to category granularity, engagement operationalization, and classifier calibration. We develop Synthetic Null Calibration to address a 32% false positive rate in per-user classification. Our findings apply wherever individual behavioral parameters are estimated from aggregate curves under differential attrition.

---


### 22. [Trust Region Inverse Reinforcement Learning: Explicit Dual Ascent using Local Policy Updates](https://arxiv.org/abs/2605.11020)

**<font color=#1a73e8>作者：</font>** Anish Diwan, Davide Tateo, Christopher E. Mower 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inverse reinforcement learning (IRL) is typically formulated as maximizing entropy subject to matching the distribution of expert trajectories. Classical (dual-ascent) IRL guarantees monotonic performance improvement but requires fully solving an RL problem each iteration to compute dual gradients. More recent adversarial methods avoid this cost at the expense of stability and monotonic dual improvement, by directly optimizing the primal problem and using a discriminator to provide rewards. In this work, we bridge the gap between these approaches by enabling monotonic improvement of the reward function and policy without having to fully solve an RL problem at every iteration. Our key theoretical insight is that a trust-region-optimal policy for a reward function update can be globally optimal for a smaller update in the same direction. This smaller update allows us to explicitly optimize the dual objective while only relying on a local search around the current policy. In doing so, our approach avoids the training instabilities of adversarial methods, offers monotonic performance improvement, and learns a reward function in the traditional sense of IRL--one that can be globally optimized to match expert demonstrations. Our proposed algorithm, Trust Region Inverse Reinforcement Learning (TRIRL), outperforms state-of-the-art imitation learning methods across multiple challenging tasks by a factor of 2.4x in terms of aggregate inter-quartile mean, while recovering reward functions that generalize to system dynamics shifts.

---


### 23. [A Switching System Theory of Q-Learning with Linear Function Approximation](https://arxiv.org/abs/2605.11021)

**<font color=#1a73e8>作者：</font>** Donghwan Lee, Han-Dong Lim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper develops a switching-system interpretation of Q-learning with linear function approximation (LFA) based on the joint spectral radius (JSR). We derive an exact linear switched model for the mean dynamics and relate convergence to stability of the corresponding switched system. The same construction is then used for stochastic linear Q-learning with independent and identically distributed (i.i.d.) observations and with Markovian observations. Although exact JSR computation is difficult in general, the certificate captures products of switching modes and can be less conservative than one-step norm bounds. The framework also yields a JSR-based view of regularized Q-learning with LFA. The resulting analysis connects projected Bellman equations, finite-difference stochastic-policy switching, and switched-system stability in a single parameter-space formulation.

---


### 24. [MambaNetBurst: Direct Byte-level Network Traffic Classification without Tokenization or Pretraining](https://arxiv.org/abs/2605.11034)

**<font color=#1a73e8>作者：</font>** Gayan K. Kulatilleke, Siamak Layeghy, Mahsa Baktashmotlagh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present MambaNetBurst, a compact tokenizer-free byte-level sequence classifier for network burst classification based on a Mamba-2 backbone. In contrast to most recent strong traffic-classification and intrusion-detection approaches, our method operates directly on raw packet bytes, avoids tokenization, patching, and heavy engineered multimodal representations, and does not require any self-supervised pre-training stage. Given a packet flow, we form a fixed-length burst from the first few packets, embed the resulting byte sequence appending a learnable CLS token, and process it with a stack of residual pre-normalized Mamba-2 blocks for end-to-end supervised classification. Across six public benchmarks spanning encrypted mobile app identification, VPN/Tor traffic classification, malware traffic classification, and IoT attack traffic, MambaNetBurst achieves consistently strong results and is competitive with, or outperforms, substantially heavier and often pre-trained baselines. Our ablation study shows that preserving byte-level temporal resolution is critical, that early downsampling through striding is consistently harmful, and that moderate state sizes are sufficient for robust generalization.
We further show that Mamba-2, despite its more constrained transition structure relative to Mamba-1, remains highly effective for packet-byte modeling while providing clear efficiency advantages, particularly in training speed. Overall, our results demonstrate that direct **undiluted** byte-to-classification learning with compact selective state space models is a practical, effective and novel direction for efficient, deployable traffic analysis that bypasses the complexity of pre-training pipelines even over highly optimized linear attention architectures.

---


### 25. [A Multi-Interface Firmware Acquisition and Validation Methodology for Low-Cost Consumer Drones: A Case Study on Three Holy Stone Platforms](https://arxiv.org/abs/2605.11040)

**<font color=#1a73e8>作者：</font>** Sandesh More, Sneha Sudhakaran, Marco Carvalho  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Consumer unmanned aerial vehicles (UAVs) have evolved into capable computing platforms, yet their embedded firmware remains largely inaccessible to the security community. Entry-level models, in particular those marketed to first-time and younger operators, commonly ship with limited protection mechanisms and no public documentation of their software internals. This paper presents a systematic study of firmware extraction and validation applied to three Holy Stone consumer drone models: the HS175D, HS720, and HS360S. Rather than pursuing reverse-engineering outcomes, the work focuses on obtaining reliable, ground-truth firmware images across heterogeneous hardware designs using only commercially available, low-cost tooling. Four acquisition methods are evaluated SPI flash in-circuit reading, SWD/JTAG debug-port access, UART boot-message capture, and a clip-based contact approach that avoids chip desoldering and each is assessed for success rate, image completeness, and operational practicality. Post-acquisition quality is evaluated through sliding-window Shannon entropy profiling and structural-signature analysis using binwalk, together forming a three-tier validation framework that distinguishes validated images from those that appear successful at the tool level but contain no meaningful firmware content. Static analysis via the EMBA framework confirms that validated images contain identifiable OS components, aging library stacks with known CVE exposure, and no binary-hardening mechanisms. The resulting corpus and methodology provide a reproducible baseline for firmware rehosting, vulnerability analysis, secure-boot assessment, and embedded-systems education within the consumer UAV domain.
Index Terms: consumer UAV, drone firmware, embedded systems security, entropy analysis, firmware extraction, IoT security, SPI flash, SWD/JTAG, UART.

---


### 26. [Red-Teaming Agent Execution Contexts: Open-World Security Evaluation on OpenClaw](https://arxiv.org/abs/2605.11047)

**<font color=#1a73e8>作者：</font>** Hongwei Yao, Yiming Liu, Yiling He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic language-model systems increasingly rely on mutable execution contexts, including files, memory, tools, skills, and auxiliary artifacts, creating security risks beyond explicit user prompts. This paper presents DeepTrap, an automated framework for discovering contextual vulnerabilities in OpenClaw. DeepTrap formulates adversarial context manipulation as a black-box trajectory-level optimization problem that balances risk realization, benign-task preservation, and stealth. It combines risk-conditioned evaluation, multi-objective trajectory scoring, reward-guided beam search, and reflection-based deep probing to identify high-value compromised contexts. We construct a 42-case benchmark spanning six vulnerability classes and seven operational scenarios, and evaluate nine target models using attack and utility grading scores. Results show that contextual compromise can induce substantial unsafe behavior while preserving user-facing task completion, demonstrating that final-response evaluation is insufficient. The findings highlight the need for execution-centric security evaluation of agentic AI systems. Our code is released at: this https URL

---


### 27. [The first global agricultural field boundary map at 10m resolution](https://arxiv.org/abs/2605.11055)

**<font color=#1a73e8>作者：</font>** Caleb Robinson, Gedeon Muhawenayo, Subash Khanal 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The agricultural field is the natural unit at which crops are planted, managed, regulated, and reported, yet most global remote-sensing products for agriculture are only available at the pixel level. While some high-quality field-level data products exist, they come from parcel registries covering only parts of Europe or from ML-derived products for individual countries. No openly available, globally consistent map of agricultural field boundaries exists to date. Here we present the first global field boundary dataset at 10\,m resolution for the years 2024 and 2025, comprising 3.17 billion remote-sensing field polygons (1.62 B in 2024 and 1.55 B in 2025) across 241 countries and territories, produced by applying a U-Net segmentation model trained on the Fields of The World dataset to cloud-free Sentinel-2 mosaics. Validated against ground-truth field boundaries in 24 countries, the map achieved a mean pixel-level recall of 0.85 with 14 countries exceeding 0.90. Evaluation against full-country ground-truth datasets in Austria, Latvia, and Finland yielded F1 scores of 0.89, 0.88, and 0.74, respectively. Because reference data for global validation is inherently incomplete, we accompanied the map with a 500 m confidence layer that identifies regions where predictions are reliable. We release the dataset openly as three global maps: the confidence-thresholded default field boundary dataset, the full unfiltered dataset, and the continuous-valued confidence raster. These maps provide the first globally consistent field-level unit of analysis for crop monitoring, food security, and downstream agricultural science.

---


### 28. [ExploitGym: Can AI Agents Turn Security Vulnerabilities into Real Attacks?](https://arxiv.org/abs/2605.11086)

**<font color=#1a73e8>作者：</font>** Zhun Wang, Nico Schiller, Hongwei Li 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents are rapidly gaining capabilities that could significantly reshape cybersecurity, making rigorous evaluation urgent. A critical capability is exploitation: turning a vulnerability, which is not yet an attack, into a concrete security impact, such as unauthorized file access or code execution. Exploitation is a particularly challenging task because it requires low-level program reasoning (e.g., about memory layout), runtime adaptation, and sustained progress over long horizons. Meanwhile, it is inherently dual-use, supporting defensive workflows while lowering the barrier for offense. Despite its importance and diagnostic value, exploitation remains under-evaluated. To address this gap, we introduce ExploitGym, a large-scale, diverse, realistic benchmark on the exploitation capabilities of AI agents. Given a program input that triggers a vulnerability, ExploitGym tasks agents with progressively extending it into a working exploit. The benchmark comprises 898 instances sourced from real-world vulnerabilities across three domains, including userspace programs, Google's V8 JavaScript engine, and the Linux kernel. We vary the security protections applied to each instance, isolating their impact on agent performance. All configurations are packaged in reproducible containerized environments. Our evaluation shows that while exploitation remains challenging, frontier models can successfully exploit a non-trivial fraction of vulnerabilities. For example, the strongest configurations are Anthropic's latest model Claude Mythos Preview and OpenAI's GPT-5.5, which produce working exploits for 157 and 120 instances, respectively. Notably, even with widely used defenses enabled, models retain non-trivial success rates. These results establish ExploitGym as an effective testbed for exploitation and highlight the growing cybersecurity risks posed by increasingly capable AI agents.

---


### 29. [ASD-Bench: A Four-Axis Comprehensive Benchmark of AI Models for Autism Spectrum Disorder](https://arxiv.org/abs/2605.11091)

**<font color=#1a73e8>作者：</font>** Shubhankit Singh, Hassan Shaikh, Kuldeep Raghuwanshi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated ASD screening tools remain limited by single-architecture evaluations, axis-restricted assessment, and near-exclusive focus on adult cohorts, obscuring age-specific diagnostic patterns critical for early intervention. We introduce ASD-Bench, a systematic tabular benchmark evaluating ML, deep learning, and foundation model configurations across three age cohorts (children 1-11 yr, adolescents 12-16 yr, adults 17-64 yr) on four axes: predictive performance, calibration, interpretability, and adversarial robustness. Applied to a curated v3 dataset of 4,068 AQ-10 records, our benchmark spans classical models (XGBoost, AdaBoost, Random Forest, Logistic Regression), neural networks (MLP), deep tabular transformers (TabNet, TabTransformer, FT-Transformer), and TabPFN v2. We introduce the Heuristic Aggregate Penalty (HAP): a cost-sensitive metric penalising false negatives more heavily and incorporating cross-validation variance for deployment stability. Adult classification yields high performance (10/17 models achieve perfect F1 and AUC), while adolescents present a harder task (F1 ceiling 0.837 vs. 0.915 for children). Feature hierarchies shift across cohorts: A9 (social motivation) dominates for children, A5 (pattern recognition) leads for adolescents, and adults exhibit a flatter importance profile consistent with developmental social masking. Accuracy and calibration are dissociated: AdaBoost achieves F1=1.000 on adults with ECE=0.302, confirming single-metric evaluation is insufficient for clinical AI. Cohort-specific deployment recommendations are provided. All findings should be interpreted as proof-of-concept evidence on questionnaire-derived labels rather than clinically validated diagnostic performance.

---


### 30. [Newton's Lantern: A Reinforcement Learning Framework for Finetuning AC Power Flow Warm Start Models](https://arxiv.org/abs/2605.11102)

**<font color=#1a73e8>作者：</font>** Shourya Bose, Helgi Hilmarsson, Dhruv Suri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural warm starts can sharply reduce the number of Newton-Raphson iterations required to solve the AC power flow problem, but existing supervised approaches generalize poorly on heavily loaded instances near voltage collapse. We prove a lower bound on the Newton-Raphson iteration count that depends on the direction of the warm start error rather than on its magnitude, and show as a corollary that the bound becomes vacuous as the smallest singular value of the power-flow Jacobian shrinks, identifying the failure mode of supervised regression near the saddle-node bifurcation. Motivated by this analysis, we introduce Newton's Lantern, a finetuning pipeline that combines group relative policy optimization with a learned reward model trained on perturbations of the base model's predictions, using the iteration count itself as the supervisory signal. Across IEEE 118-bus, GOC 500-bus, and GOC 2000-bus benchmarks, Newton's Lantern is the only method that converges on every test snapshot while attaining the smallest mean iteration count.

---


### 31. [LatentHDR: Decoupling Exposure from Diffusion via Conditional Latent-to-Latent Mapping for Text/Image-to-Panoramic HDR](https://arxiv.org/abs/2605.11115)

**<font color=#1a73e8>作者：</font>** Pedram Fekri, WenChen Li, William Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High Dynamic Range (HDR) generation remains challenging for generative models, which are largely limited to low dynamic range outputs. Recent diffusionbased approaches approximate HDR by generating multiple exposure-conditioned samples, incurring high computational cost and structural inconsistencies across exposures. We propose LatentHDR, a framework that decouples scene generation from exposure modeling in latent space. A pretrained diffusion backbone produces a single coherent scene representation, while a lightweight conditional latent to-latent head deterministically maps it to exposure-specific representations. This enables the generation of a dense, structurally consistent exposure stack in a single pass. This design eliminates multi-pass diffusion, ensures cross-exposure alignment, and enables scalable HDR synthesis. LatentHDR supports both textand image-conditioned HDR generation for perspective and panoramic scenes. Experiments on synthetic data and the SI-HDR benchmark show that LatentHDR achieves state-of-the-art dynamic range with competitive perceptual quality, while reducing computation by an order of magnitude. Our results demonstrate that high-quality HDR generation can be achieved through structured latent modeling, challenging the need for stochastic multi-exposure generation.

---


### 32. [A Cascaded Generative Approach for e-Commerce Recommendations](https://arxiv.org/abs/2605.11118)

**<font color=#1a73e8>作者：</font>** Moein Hasani, Hamidreza Shahidi, Trace Levinson 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personalized storefronts in large e-commerce marketplaces are often assembled from many independent components: static themes per page section ("placement"), retrieval systems to fetch eligible products per placement, and pointwise rankers to order content. While effective in optimizing for aggregate preferences, this paradigm is rigid and can limit personalization and semantic cohesion across the page. This makes it poorly suited to support dynamic objectives and merchandising requirements over time. To address this, we introduce a cascaded merchandising framework that decomposes storefront construction into two generative tasks: (i) placement-level theme generation and (ii) constrained keyword generation per placement to power product retrieval. Teacher-student fine-tuning is leveraged to improve scalability of this framework under production latency and cost constraints. Fine-tuned model ablations are shown to approach closed-weight LLM performance. We further contribute frameworks for AI-driven content evaluation and quality filtering, enabling safe and automated deployment of dynamic content at scale. Generative output is fused with traditional ranking models to preserve hybrid infrastructure. In online experiments, this framework yields an estimated +2.7% lift in cart adds per page view over a strong baseline.

---


### 33. [FedSurrogate: Backdoor Defense in Federated Learning via Layer Criticality and Surrogate Replacement](https://arxiv.org/abs/2605.11122)

**<font color=#1a73e8>作者：</font>** Fatima Z. Abacha, Sin G. Teo, Yuanxiang Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated Learning remains highly susceptible to backdoor attacks--malicious clients inject targeted behaviours into the global model. Existing defenses suffer from substantial false-positive rates under realistic non-independent and identically distributed (non-IID) data, incorrectly flagging benign clients and degrading model accuracy even when adversaries are correctly identified. We present FedSurrogate, a novel backdoor defense that addresses this limitation by combining bidirectional gradient alignment filtering with layer-adaptive anomaly detection. FedSurrogate performs selective clustering on security-critical layers identified via directional divergence analysis, concentrating the detection signal on a low-dimensional subspace. A bidirectional soft-filtering stage screens trusted clients for residual contamination while rescuing false positives from suspects, substantially reducing misclassifications under heterogeneous conditions. Rather than removing confirmed malicious updates, FedSurrogate replaces them with downscaled surrogate updates from structurally similar benign clients, preserving gradient diversity while neutralising adversarial influence. Extensive evaluations demonstrate that FedSurrogate maintains false-positive rates below 10% across all datasets and attack types, compared to 31-32% for the nearest comparably effective baseline, while achieving superior main-task accuracy and maintaining attack success rates below 2.1% across all tested datasets and attack types under challenging non-IID settings.

---


### 34. [HEPA: A Self-Supervised Horizon-Conditioned Event Predictive Architecture for Time Series](https://arxiv.org/abs/2605.11130)

**<font color=#1a73e8>作者：</font>** Jonas Petersen, Gian-Alessandro Lombardi, Riccardo Maggioni 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Critical events in multivariate time series, from turbine failures to cardiac arrhythmias, demand accurate prediction, yet labeled data is scarce because such events are rare and costly to annotate. We introduce HEPA (Horizon-conditioned Event Predictive Architecture), built on two key principles. First, a causal Transformer encoder is pretrained via a Joint-Embedding Predictive Architecture (JEPA): a horizon-conditioned predictor learns to forecast future representations rather than future values, forcing the encoder to capture predictable temporal dynamics from unlabeled data alone. Second, we freeze the encoder and finetune only the predictor toward the target event, producing a monotonic survival cumulative distribution function (CDF) over horizons. With fixed architecture and optimiser hyperparameters across all benchmarks, HEPA handles water contamination, cyberattack detection, volatility regimes, and eight further event types across 11 domains, exceeding leading time-series architectures including PatchTST, iTransformer, MAE, and Chronos-2 on at least 10 of 14 benchmarks, with an order of magnitude fewer tuned parameters and, on lifecycle datasets, an order of magnitude less labeled data.

---


### 35. [USEMA: a Scalable Efficient Mamba Like Attention for Medical Image Segmentation](https://arxiv.org/abs/2605.11131)

**<font color=#1a73e8>作者：</font>** Elisha Dayag, Nhat Thanh Tran, Jack Xin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate medical image segmentation is an integral part of the medical image analysis pipeline that requires the ability to merge local and global information. While vision transformers are able to capture global interactions using vanilla self-attention, their quadratic computational complexity in the input size remains a struggle for medical image segmentation tasks. Motivated by the dispersion property of vanilla self-attention and recent development of Mamba form of attention, Scalable and Efficient Mamba like Attention (SEMA) utilizes token localization via local window attention to avoid dispersion and maintain focusing, complemented by theoretically consistent arithmetic averaging to capture global aspect of attention. In this work, we present USEMA, a hybrid UNet architecture that merges the local feature extraction ability of convolutional neural networks (CNNs) with SEMA attention. We conduct experiments with USEMA across a variety of modalities and image sizes, demonstrating improved computational efficiency compared to transformer based models using full self-attention, and superior segmentation performance relative to purely convolution and Mamba-based models.

---


### 36. [Steerable Neural ODEs on Homogeneous Spaces](https://arxiv.org/abs/2605.11133)

**<font color=#1a73e8>作者：</font>** Emma Andersdotter, Daniel Persson, Fredrik Ohlsson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce steerable neural ordinary differential equations on homogeneous spaces $M=G/H$. These models constitute a novel geometric extension of manifold neural ordinary differential equations (NODEs) that transport associated feature vectors transforming under the local symmetry group $H$. We interpret features as sections of associated vector bundles over $M$, and describe their evolution as parallel transport. This results in a coupled system of ODEs consisting of a flow equation on $M$ and a steering equation acting on features. We show that steerable NODEs are $G$-equivariant whenever the vector field generating the flow and the connection governing parallel transport are both $G$-invariant. Furthermore, we demonstrate how steerable NODEs incorporate existing NODE models and continuous normalizing flows on Lie groups. Our framework provides the geometric foundation for learning continuous-time equivariant dynamics of general vector-valued features on homogeneous spaces.

---


### 37. [Spurious Correlation Learning in Preference Optimization: Mechanisms, Consequences, and Mitigation via Tie Training](https://arxiv.org/abs/2605.11134)

**<font color=#1a73e8>作者：</font>** Christian Moya, Alex Semendinger, Guang Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Preference learning methods such as Direct Preference Optimization (DPO) are known to induce reliance on spurious correlations, leading to sycophancy and length bias in today's language models and potentially severe goal misgeneralization in future systems. In this work, we provide a unified theoretical analysis of this phenomenon, characterizing the mechanisms of spurious learning, its consequences on deployment, and a provable mitigation strategy. Focusing on log-linear policies, we show that standard preference-learning objectives induce reliance on spurious features at the population level through two channels: mean spurious bias and causal--spurious correlation leakage. We then show that this reliance creates an irreducible vulnerability to distribution shift: more data from the same training distribution fails to reduce the model's dependence on spurious features. To address this, we propose tie training, a data augmentation strategy using ties (equal-utility preference pairs) to introduce data-driven regularization. We demonstrate that this approach selectively reduces spurious learning without degrading causal learning. Finally, we validate our theory on log-linear models and provide empirical evidence that both the spurious learning mechanisms and the benefits of tie training persist for neural networks and large language models.

---


### 38. [Control Charts for Multi-agent Systems](https://arxiv.org/abs/2605.11135)

**<font color=#1a73e8>作者：</font>** Hayden Helm, Carey Priebe, Brandon Duderstadt  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Generative agents have proven to be powerful assistants in a wide variety of contexts. Given this success, users are now deploying agents with minimal restrictions in open ended, multi-agent environments. Current methods for monitoring the dynamics of open-ended multi-agent systems are limited to qualitative inspection. In this paper, we extend the process-theoretic notion of adaptive control charts to multi-agent systems to enable automated monitoring. Using simulation, we demonstrate that adaptive control charts are necessary for monitoring multi-agent systems that can learn from their environment. We further demonstrate, both empirically and theoretically, that adaptive control charts are susceptible to adversarial agents that defect sufficiently slowly. These results illustrate a fundamental tradeoff in multi-agent system control: either agents in a system cannot learn or the system is susceptible to adversaries.

---


### 39. [EVOCHAMBER: Test-Time Co-evolution of Multi-Agent System at Individual, Team, and Population Scales](https://arxiv.org/abs/2605.11136)

**<font color=#1a73e8>作者：</font>** Yaolun Zhang, Tianyi Xu, Shengyu Dai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We argue that multi-agent test-time evolution is not single-agent evolution replicated N times. A single-agent learner can only evolve its own context and memory. A multi-agent system additionally evolves who collaborates, how they collaborate, and how knowledge flows across the population. These components have no single-agent counterpart and can produce phenomena such as emergent specialization. Yet prior test-time methods either confine experiences to individual agents, forfeiting cross-agent learning, or broadcast symmetrically to all agents, erasing the specialization that makes collaboration valuable. We present EVOCHAMBER, a training-free framework that instantiates test-time evolution at three levels over a coevolving agent pool. At its core is CODREAM (Collaborative Dreaming), a post-task protocol triggered on team failure or disagreement, in which agents collaboratively reflect, distill insights, and route them asymmetrically from strong to weak agents on the failed niche, preserving specialization while filling knowledge gaps. Team-level operators assemble niche-conditioned teams and select collaboration structures online. Population-level lifecycle operators fork, merge, prune, and seed agents under performance pressure. On three heterogeneous task streams with Qwen3-8B, EVOCHAMBER reaches 63.9% on competition math, 75.7% on code, and 87.1% on multi-domain reasoning, outperforming the best baseline by 32% relative on math and confirming asymmetric cross-agent transfer as the primary driver in ablation. Starting from several identically initialized agents, four to five stable niche specialists spontaneously emerge, a structural signature of multi-agent evolution that no single-agent learner can express. See our code at: this https URL

---


### 40. [Rank Is Not Capacity: Spectral Occupancy for Latent Graph Models](https://arxiv.org/abs/2605.11142)

**<font color=#1a73e8>作者：</font>** Nikolaos Nakis, Panagiotis Promponas, Konstantinos Tsirkas 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph representation learning has become a standard approach for analyzing networked data, with latent embeddings widely used for link prediction, community detection, and related tasks. Yet a basic design choice, the latent dimension, is still treated as a brittle hyperparameter, fixed before training and tuned by held-out performance. Learned factors are also identifiable only up to rotation and rescaling, so the nominal rank rarely coincides with the quantity that governs model behavior. We propose Spectral Prefix Extraction and Capacity-Targeted Representation Analysis (Spectra), which replaces rank as the unit of analysis with the spectrum of a learned positive semidefinite kernel, trace-normalized so that spectra are comparable across fits. The normalized eigenvalues form a distribution on the simplex, and their Shannon effective rank acts both as a summary of learned capacity and as a controllable training-time coordinate: a single scalar shapes this realized dimension during training, and bisection targets any desired value within the rank cap. To theoretically support that, we show local regularity and monotonicity of the realized-dimension profile. Across collaboration, social, biological, and infrastructure networks, Spectra traces performance--capacity frontiers that make the trade-off between predictive accuracy and realized dimension visible. It performs competitively with strong link-prediction baselines, yields aligned lower-capacity views of the same fitted model through spectral prefixes, and provides a principled handle on capacity in the overparameterized regime. Capacity thus becomes a property of the fitted model rather than a hyperparameter of the training.

---


### 41. [Conversational Customization of Productivity Systems: A Design Probe of Malleable AI Interfaces](https://arxiv.org/abs/2605.11149)

**<font color=#1a73e8>作者：</font>** Karthik Sreedhar, Aryan Kaul, Lydia B. Chilton  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Customization has long been a central goal in interactive systems, yet prior work shows that end-user tailoring occurs infrequently and is often confined to initial setup or moments of breakdown. Recent advances in generative AI suggest that highly malleable systems-where users can modify system behavior through natural language-are now technically feasible. However, it remains unclear how such malleability is used in practice: What kinds of customizations do users create, when do they choose to customize, and how do these modifications shape their experience of everyday tools? We present a design probe that uses a conversationally customizable email system as an instrument to study how users create and refine functionality within everyday tools. The system allows users to iteratively modify their inbox by restructuring categories, introducing interface elements, and authoring new workflow behaviors directly through natural language interaction. We study how participants create, refine, and use these features over several days within their own email workflows. We find that users' customizations are often grounded in existing patterns, which they adapt and specialize to fit their needs, rather than generating entirely novel functionality. Malleability changes how users engage with their inbox, shifting it from a fixed interface to a flexible data layer shaped through user-authored features. At the same time, customization introduces new forms of risk, including mis-specified behavior, unintended filtering, and uncertainty around outcomes, which users manage through ongoing oversight and refinement. These findings highlight how conversational customization becomes embedded within everyday interaction, and point toward the need for systems that support iterative refinement, visibility into behavior, and safe experimentation as users shape their own tools.

---


### 42. [RankQ: Offline-to-Online Reinforcement Learning via Self-Supervised Action Ranking](https://arxiv.org/abs/2605.11151)

**<font color=#1a73e8>作者：</font>** Andrew Choi, Wei Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Offline-to-online reinforcement learning (RL) improves sample efficiency by leveraging pre-collected datasets prior to online interaction. A key challenge, however, is learning an accurate critic in large state--action spaces with limited dataset coverage. To mitigate harmful updates from value overestimation, prior methods impose pessimism by down-weighting out-of-distribution (OOD) actions relative to dataset actions. While effective, this essentially acts as a behavior cloning anchor and can hinder downstream online policy improvement when dataset actions are suboptimal. We propose RankQ, an offline-to-online Q-learning objective that augments temporal-difference learning with a self-supervised multi-term ranking loss to enforce structured action ordering. By learning relative action preferences rather than uniformly penalizing unseen actions, RankQ shapes the Q-function such that action gradients are directed toward higher-quality behaviors. Across sparse reward D4RL benchmarks, RankQ achieves performance competitive with or superior to seven prior methods. In vision-based robot learning, RankQ enables effective offline-to-online fine-tuning of a pretrained vision-language-action (VLA) model in a low-data regime, achieving on average a 42.7% higher simulation success rate than the next best method. In a high-data setting, RankQ improves simulation performance by 13.7% over the next best method and achieves strong sim-to-real transfer, increasing real-world cube stacking success from 43.1% to 84.7% relative to the VLA's initial performance.

---


### 43. [Decomposing Evolutionary Mixture-of-LoRA Architectures: The Routing Lever, the Lifecycle Penalty, and a Substrate-Conditional Boundary](https://arxiv.org/abs/2605.11153)

**<font color=#1a73e8>作者：</font>** Ramchand Kumaresan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We decompose an evolutionary mixture-of-LoRA system on a from-scratch ~150M-parameter widened-D substrate (D=1536, V=32000; D/V approx 0.048; the "widened-1536" substrate) into three factors -- a router rewrite (parallel sigmoid gate with learnable per-adapter floor and bounded temperature anneal, fed post-stack hidden states rather than token-embedding means), a per-domain leave-one-out evaluation scope, and a lifecycle of death plus alpha-blend inheritance plus SVD mutation plus slot reallocation -- and report a 5-of-8 partial 2^3 factorial run at n=3 seeds and 25000 adaptation steps per cell. The attribution chain is sharp on this substrate: the router rewrite carries the entire +0.0426 nat balanced log-PPL improvement (Delta = log PPL_ref - log PPL_test, positive = improvement; t=12.86, p=0.006) attributed to "the full evolutionary system vs the static B3 baseline"; the headline full-system-vs-B3 balanced contrast itself is +0.015 nats, t=1.94, p=0.19 at n=3 and does not clear alpha=0.05. The per-domain evaluation scope is null at seed-resolution, and the lifecycle is a net drag of approx -0.028 nats (t=-4.46,p=0.047 in the primary chain). An auxiliary alpha=0 inheritance counterfactual at n=3 seeds is sign-inconsistent at the headline metric and underpowered for either an equivalence or load-bearing conclusion (corrected from an earlier arithmetic-mean aggregator that erroneously cleared inheritance; see Appendix B.11). A base-perturbation probe directionally refutes a "genomic-context" reframe of the lifecycle role. A controllable synthetic sandbox locates a substrate-conditional regime boundary: evolutionary search on the routing channel is load-bearing only when adapters are pre-aligned to the task; in every other regime tested it underperforms, ties, or actively degrades the gradient solution.

---


### 44. [CORE: Cyclic Orthotope Relation Embedding for Knowledge Graph Completion](https://arxiv.org/abs/2605.11159)

**<font color=#1a73e8>作者：</font>** Yingqi Zeng, Luying Wang, Huiling Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge graph completion (KGC) aims to automatically infer missing facts in multi-relational data by mapping entities and relations into continuous representation spaces. Recent region-based embedding models have shown great promise in capturing complex logical patterns by representing relations as geometric regions. However, these models inevitably suffer from absolute boundary constraints during optimization. Conversely, without such constraints, relation regions expand indefinitely. To address the limitation, we propose \textbf{CORE} (Cyclic Orthotope Relation Embedding), a novel KGC model that embeds entities and relations onto a boundary-less torus this http URL represents relations as cyclic orthotopes on the torus manifold, allowing regions to seamlessly wrap around spatial boundaries to ensure smooth gradient conduction. Furthermore, an adaptive width regularization is introduced to prevent unconditional region expansion. Theoretical analysis proves that CORE can capture various complex relation patterns such as subsumption and intersection. Extensive experiments on four benchmark datasets demonstrate that CORE achieves highly competitive performance, significantly improving link prediction accuracy in dense semantic environments.

---


### 45. [Interpretability Can Be Actionable](https://arxiv.org/abs/2605.11161)

**<font color=#1a73e8>作者：</font>** Hadas Orgad, Fazl Barez, Tal Haklay 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interpretability aims to explain the behavior of deep neural networks. Despite rapid growth, there is mounting concern that much of this work has not translated into practical impact, raising questions about its relevance and utility. This position paper argues that the central missing ingredient is not new methods, but evaluation criteria: interpretability should be evaluated by actionability--the extent to which insights enable concrete decisions and interventions beyond interpretability research itself. We define actionable interpretability along two dimensions--concreteness and validation--and analyze the barriers currently preventing real-world impact. To address these barriers, we identify five domains where interpretability offers unique leverage and present a framework for actionable interpretability with evaluation criteria aligned with practical outcomes. Our goal is not to downplay exploratory research, but to establish actionability as a core objective of interpretability research.

---


### 46. [COSMOS: Model-Agnostic Personalized Federated Learning with Clustered Server Models and Pseudo-Label-Only Communication](https://arxiv.org/abs/2605.11165)

**<font color=#1a73e8>作者：</font>** Ben Rachmut, Luise Ge, William Yeoh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) in heterogeneous environments remains challenging because client models often differ in both architecture and data distribution. While recent approaches attempt to address this challenge through client clustering and knowledge distillation, simultaneously handling architectural and statistical heterogeneity remains difficult. We introduce COSMOS, a model-agnostic framework that enables server-side personalization using only pseudo-label communication. Clients train local models and predict on the public data; the server clusters clients by prediction similarity, trains a cluster-specific model for each group using its own compute, and distills the resulting models back to clients. We provide the first theoretical analysis showing that distillation from the learned cluster models can yield exponential personalization risk contraction, going beyond the convergence-to-stationarity guarantees typically provided in model-agnostic FL. Experiments across benchmarks demonstrate that COSMOS consistently outperforms all model-agnostic FL baselines while remaining competitive with state-of-the-art personalized FL methods. More broadly, our results highlight personalized server-side learning with pseudo-labels as a promising paradigm for scalable and model-agnostic federated learning in highly heterogeneous environments.

---


### 47. [Unpacking the Eye of the Beholder: Social Location, Identity, and the Moving Target of Political Perspectives](https://arxiv.org/abs/2605.11166)

**<font color=#1a73e8>作者：</font>** Elena Sirotkina  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Political and social identities structure how people evaluate political information, a finding decades deep in political science and routinely discarded by computational tools that often produce single scores that treat a piece of text, an image, or a video as if it means the same thing to everyone. This paper shows that it does not, and that the difference is consequential. To address this problem, I develop the Perspectivist Visual Political Sentiment (PVPS) classifier, which learns from approximately 82,000 evaluations by 5,575 U.S. adults to predict how audiences defined by political and social identities will evaluate the same image. Unlike standard tools that average systematic disagreement away, PVPS preserves it, returning an evaluative profile that records who agrees, who diverges, and along which identity lines. Applied to several influential studies of visual sentiment, PVPS shows that perceived violence in protest imagery and the emotional mechanisms behind protest image engagement both change substantively once audience identity is taken into account. It follows that what a political image conveys is a moving target, and measuring it requires knowing whom it is moving.

---


### 48. [Unlearning with Asymmetric Sources: Improved Unlearning-Utility Trade-off with Public Data](https://arxiv.org/abs/2605.11170)

**<font color=#1a73e8>作者：</font>** Ahmed Mehdi Inane, Vincent Quirion, Gintare Karolina Dzugaite 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Noise-based certified machine unlearning currently faces a hard ceiling: the noise magnitude required to certify unlearning typically destroys model utility, particularly for large-scale deletion requests.
While leveraging public data is a standard technique in differential privacy to relax this tension, its role in unlearning remains unexplored. We address this gap by introducing Asymmetric Langevin Unlearning (ALU), a framework that uses public data to mitigate privacy costs. We prove that public data injection suppresses the unlearning cost by a factor of $O(1/n_{\mathrm{pub}}^2)$, guaranteeing a strict computational advantage over retraining. This establishes a new control mechanism: practitioners can mitigate the need for high noise-and the associated utility loss-by increasing the volume of public data. Crucially, we analyze the realistic setting of distribution mismatch, explicitly characterizing how shifts between public and private sources impact utility.
We show that ALU enables mass unlearning of constant dataset fractions -- a regime where standard symmetric methods become impractical -- while maintaining high utility. Empirical evaluations using variational Rényi divergence and membership inference attacks confirm that ALU effectively thwarts privacy attacks while preserving utility under reasonable distribution shifts.

---


### 49. [Oversmoothing as Representation Degeneracy in Neural Sheaf Diffusion](https://arxiv.org/abs/2605.11178)

**<font color=#1a73e8>作者：</font>** Arif Dönmez, Axel Mosig, Ellen Fritsche 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural Sheaf Diffusion (NSD) generalizes diffusion-based Graph Neural Networks by replacing scalar graph Laplacians with sheaf Laplacians whose learned restriction maps define a task-adapted geometry. While the diffusion limit of NSD is known to be the space of global sections, the representation-theoretic structure of this harmonic space remains largely implicit. We develop a quiver-theoretic interpretation of NSD by identifying cellular sheaves on graphs with representations of the associated incidence quiver. Under this correspondence, learned sheaf geometries become points in a finite-dimensional representation space. We show that direct-sum decompositions of the underlying incidence-quiver representation induce decompositions of the harmonic space reached in the diffusion limit. This gives an algebraic interpretation of oversmoothing as representation degeneration: learned sheaves may collapse toward low-complexity summands whose global sections fail to preserve discriminative information. Building on this viewpoint, we connect sheaf diffusion to stability and moment-map principles from Geometric Invariant Theory. We introduce moment-map-inspired regularizers that bias restriction maps toward balanced representation geometries, and identify a structural obstruction in equal-stalk architectures: when $d_v = d_e$, admissibility for learnable stability parameters forces the trivial all-object summand onto a stability wall. Non-uniform stalk dimensions remove this obstruction, making adaptive stability meaningful. Experiments on heterophilic benchmarks are consistent with this mechanism: breaking stalk symmetry can reduce variance or improve validation behavior, and adaptive stability becomes more effective in selected rectangular settings. Overall, our framework reframes oversmoothing as a degeneration phenomenon in the representation geometry underlying learned sheaf diffusion.

---


### 50. [Muon is Not That Special: Random or Inverted Spectra Work Just as Well](https://arxiv.org/abs/2605.11181)

**<font color=#1a73e8>作者：</font>** Zakhar Shumaylov, Nathaël Da Costa, Peter Zaika 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The recent empirical success of the Muon optimizer has renewed interest in non-Euclidean optimization, typically justified by similarities with second-order methods, and linear minimization oracle (LMO) theory. In this paper, we challenge this geometric narrative through three contributions, demonstrating that precise geometric structure is not the key factor affecting optimization performance. First, we introduce Freon, a family of optimizers based on Schatten (quasi-)norms, powered by a novel, provably optimal QDWH-based iterative approximation. Freon naturally interpolates between SGD and Muon, while smoothly extrapolating into the quasi-norm regime. Empirically, the best-performing Schatten parameters for GPT-2 lie strictly within the quasi-norm regime, and thus cannot be represented by any unitarily invariant LMO. Second, noting that Freon performs well across a wide range of exponents, we introduce Kaon, an absurd optimizer that replaces singular values with random noise. Despite lacking any coherent geometric structure, Kaon matches Muon's performance and retains classical convergence guarantees, proving that strict adherence to a precise geometry is practically irrelevant. Third, having shown that geometry is not the primary driver of performance, we demonstrate it is instead controlled by two local quantities: alignment and descent potential. Ultimately, each optimizer must tune its step size around these two quantities. While their dynamics are difficult to predict a-priori, evaluating them within a stochastic random feature model yields a precise insight: Muon succeeds not by tracking an ideal global geometry, but by guaranteeing step-size optimality.

---


> [!TIP]
> 当前位于：**1-50**（第 1/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-396](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
