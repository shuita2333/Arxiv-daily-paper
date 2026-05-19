# 📦 其他研究 | 2026年05月20日

> 本类共 **619** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**401-450**（第 9/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-619](./part-13.md)

---

### 401. [PlantPose: Universal Plant Skeleton Estimation via Tree-constrained Graph Generation](https://arxiv.org/abs/2605.17773)

**<font color=#1a73e8>作者：</font>** Xinpeng Liu, Hiroaki Santo, Yosuke Toda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate estimation of plant skeletal structures (e.g., branching structures) from images is essential for smart agriculture and plant science. Unlike human skeletons with fixed topology, plant skeleton estimation presents a unique challenge, i.e., estimating arbitrary tree graphs from images. To address this problem, we introduce PlantPose, a universal plant skeleton estimator via tree-constrained graph generation. PlantPose combines learning-based graph generation with traditional graph algorithms to enforce tree constraints during the training loop. To enhance the model's generalization capability, we curate a large and diverse dataset comprising real-world and synthetic plant images, along with simplified representations (e.g., sketches and abstract drawings). This dataset enables the generalized model to adapt to diverse input styles and categories of plant images while preserving topological consistency. Our approach demonstrates robust and accurate plant skeleton estimation across multiple domains, including previously unseen out-of-domain scenarios. Further analyses highlight the method's strengths and limitations in handling complex, heterogeneous data distributions. All implementations and datasets are available at this https URL.

---


### 402. [Efficient Sparse-to-Dense Visual Localization via Compact Gaussian Scene Representation and Accelerated Dense Pose Estimation](https://arxiv.org/abs/2605.17777)

**<font color=#1a73e8>作者：</font>** Zizhuo Li, Songchu Deng, Linfeng Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This letter presents LiteLoc, a novel and efficient localizer built on 3D Gaussian Splatting (3DGS). The previous state-of-the-art (SoTA) sparse-to-dense localizer, STDLoc, has shown remarkable localization capability but suffers from severe storage redundancy and computational latency. By revisiting its design decisions, we derive two simple yet highly effective improvements that cumulatively make LiteLoc much more efficient in both memory and computation, while also being easier to train. One key observation is that the color field, inherited directly from Feature 3DGS, is functionally useless for localization. Yet, its reconstruction of high-frequency photometric details necessitates excessive Gaussian primitives, resulting in a tightly coupled color-feature representation with significant memory overhead and sub-optimal feature field optimization. To resolve this, we propose a color-free decoupled feature field that constructs a compact Gaussian scene representation by retaining only task-essential feature attributes, thereby eliminating approximately 94% of redundant storage with no loss of localization-relevant information. We further find that the primary computational bottleneck lies in the dense Perspective-n-Point (PnP) solver, where most matches contribute saturated geometric constraints with diminishing accuracy gains. Accordingly, we propose a condensing strategy that distills dense matches into a subset of 5% representative matches, enabling a nearly 19-fold speedup in robust estimation with negligible performance drop. Extensive experiments show that LiteLoc surpasses STDLoc in multiple scenes with considerable efficiency benefits, opening up exciting prospects for latency-sensitive visual localization.

---


### 403. [Learning Variable-Length Tokenization for Generative Recommendation](https://arxiv.org/abs/2605.17779)

**<font color=#1a73e8>作者：</font>** Minhao Wang, Bowen Wu, Wei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative recommendation reformulates recommendation as next-token prediction over discrete semantic identifiers (IDs). A fundamental yet unexplored design choice is that existing methods employ fixed-length tokenization for all items, implicitly assuming uniform encoding capacity regardless of item characteristics. Through systematic experiments across four datasets, we discover the Popularity-Length Paradox: popular items achieve optimal performance with short IDs, while tail items require substantially longer codes to capture discriminative semantics. This reveals a critical mismatch where popular items benefit from abundant collaborative signals and require minimal semantic detail, whereas tail items must rely on fine-grained content features due to sparse interaction data.
To address this, we propose VarLenRec, a framework for learning variable-length tokenization. We develop Popularity-Weighted Information Budget Allocation (PIBA), an information-theoretic framework proving that optimal ID length should scale as a negative power of popularity. Directly implementing variable-length allocation faces two technical challenges: standard Euclidean residual quantization lacks geometric capacity to support diverse code lengths without distortion, and discrete length decisions are non-differentiable. We address these through Hyperbolic Residual Quantization, which leverages the exponential volume growth of the Poincaré ball to naturally stratify encoding capacity, and a Soft Length Controller, which enables differentiable length prediction via continuous layer retention probabilities regularized by PIBA-derived priors. Extensive experiments demonstrate that VarLenRec achieves significant improvements over state-of-the-art methods in recommendation accuracy and training/inference efficiency, revealing the importance of adaptive encoding capacity in generative recommendation.

---


### 404. [Network Knowledge Prior Guided Learning for Data-Efficient Surface Defect Detection](https://arxiv.org/abs/2605.17780)

**<font color=#1a73e8>作者：</font>** Hang-Cheng Dong, Guodong Liu, Dong Ye 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning-based methods have become the de facto standard for industrial defect detection. However, their data-hungry nature and inherent "black-box" characteristics often lead to performance bottlenecks and limited trustworthiness in real-world applications. To address these challenges, this paper proposes a novel knowledge-guided loss function that seamlessly integrates model interpretability into the training process without incurring any additional inference cost. Our method operates in two phases: first, a primary classification network is trained, and its explanations, in the form of saliency maps, are generated as prior knowledge. Second, a multi-task learning framework is established, where the main task performs classification, and an auxiliary task imposes consistency between the saliency maps of the final model and the primary model. This consistency is enforced by a dedicated knowledge-guided loss term, effectively acting as a powerful regularizer to steer the model towards robust feature representations. Extensive experiments on multiple public defect datasets demonstrate that our approach consistently enhances the performance of baseline models in terms of accuracy and AP. Moreover, visual analysis reveals that the proposed method yields more concentrated and human-intelligible saliency maps. This work presents a simple yet effective paradigm for bridging the gap between model performance and interpretability, paving the way for more reliable and high-performing vision systems in industrial quality inspection.

---


### 405. [SocialMemBench: Are AI Memory Systems Ready for Social Group Settings?](https://arxiv.org/abs/2605.17789)

**<font color=#1a73e8>作者：</font>** Olukunle Owolabi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Memory systems for AI assistants were built for single-user dialogue and fail characteristically when applied to multi-party social group settings. This gap matters for the social assistants being built today: group-acting agents embedded in chat platforms, and proactive personal-assistant agents whose holistic model of a user must include their social context. Existing memory benchmarks evaluate dyadic or workplace dialogue; none targets multi-party social groups, where memory must anchor facts in shared history rather than professional roles, separate group norms from individual exceptions, and correctly attribute even after member departure. We introduce SocialMemBench, a benchmark of human-verified synthetic social group networks across five archetypes (close friends, family, recreational, interest community, acquaintance network) and three group-size tiers (4-30 members), with 430 personas and 7,355 conversation turns, yielding 1,031 QA pairs across nine question categories. Each category isolates an architectural capability, and the five failure modes (single-stream conflation, temporal-state overwrite, entity merging at scale, missing cross-persona knowledge, norm-individual conflation) are testable hypotheses; our two research probes Subject-Mem and SMG provide evidence on two, three remain open. A full-context Gemini 2.5 Flash reference reaches only 0.721 against a blind-critic reasoning-model mean of 0.98 on small networks, indicating the benchmark is genuinely difficult even with complete access to the conversation. Across all 43 networks, the four open-source memory frameworks evaluated (Mem0, LangMem, Graphiti, Cognee) cluster in the 0.12-0.18 question-weighted range with overlapping 95% CIs, well below an uncompressed retrieval reference of 0.345 and a matched-answerer full-context reference of 0.369 (GPT-4o-mini). Current memory systems show a measurable gap.

---


### 406. [STRIDE: A Self-Reflective Agent Framework for Reliable Automatic Equation Discovery](https://arxiv.org/abs/2605.17790)

**<font color=#1a73e8>作者：</font>** Jiarui Su, Songjun Tu, Bei Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based equation discovery offers a promising route to recovering symbolic laws from data, but many systems still rely on generation-centered loops that propose candidates, fit parameters, score results, and reuse selected examples. Such loops can misjudge useful skeletons under unreliable fitting, discard near-correct equations that require repair, and accumulate redundant memories that provide limited guidance. We propose STRIDE, a self-reflective agent framework that improves reliability by coordinating data-aware generation, mixed-fitting evaluation, critic--executor repair, and diversity-preserving semantic memory. By turning fitted scores and candidate behavior into shared feedback, STRIDE enables equations to be proposed, assessed, refined, and reused within a closed-loop discovery process. Experiments on representative symbolic-regression benchmarks and LSR-Synth suites show that STRIDE improves accuracy, OOD robustness, and structural recovery across multiple LLM backbones, with ablations and analyses confirming the contribution of its core components.

---


### 407. [When Accuracy Is Not Enough: Uncertainty Collapse between Noisy Label Learning and Out-of-Distribution Detection](https://arxiv.org/abs/2605.17795)

**<font color=#1a73e8>作者：</font>** Ningkang Peng, Jingyang Mao, Runhan Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning with noisy labels (LNL) is typically benchmarked by closed-set classification accuracy, yet deployment often requires classifiers to reject out-of-distribution (OOD) inputs. We present a learner-agnostic ACC-OOD benchmark that freezes LNL checkpoints and evaluates them with standardized near-/far-OOD routing and post-hoc scores across synthetic and real label noise. The benchmark reveals a recurring failure mode: high closed-set accuracy does not ensure OOD reliability, because low-confidence, misclassified in-distribution samples can overlap the score and feature regions occupied by OOD inputs under noisy training. We term this pathology uncertainty collapse. This structural overlap can make high-accuracy LNL methods lose separability at the ID-error/OOD interface under standard OOD scores. As an intervention, we study Virtual Margin Regularization (VMR), a lightweight repair probe demonstrated mainly with PSSCL that synthesizes boundary virtual outliers on trusted ID batches and widens the energy margin. VMR partially reduces the collapse-induced far-OOD failure without replacing the host objective or sacrificing closed-set accuracy in the tested settings. These results support LNL benchmarks that co-report closed-set generalization, open-world reliability, and structural overlap diagnostics.

---


### 408. [Is Complex Training Necessary for Long-Tailed OOD Detection? A Re-think from Feature Geometry](https://arxiv.org/abs/2605.17799)

**<font color=#1a73e8>作者：</font>** Ningkang Peng, Xuanming Chen, Yanhui Gu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-tailed out-of-distribution (LT-OOD) detection is often addressed with specialized training, including auxiliary out-of-distribution (OOD) data, abstention heads, contrastive objectives, energy losses, or gradient-conflict control. We show that these training mechanisms can obscure a simpler issue: frozen long-tailed representations may already contain useful OOD evidence, but raw Mahalanobis distance is distorted by frequency-coupled feature radius and poorly supported tail covariance. We propose Hyperspherical Pooled Mahalanobis (HPM), a post-hoc detector that normalizes features onto the unit sphere and replaces class-specific covariance with a pooled, ridge-regularized metric while keeping class means as semantic anchors. In CIFAR-LT experiments and an ImageNet-100-LT near-OOD boundary analysis, HPM improves raw Mahalanobis scoring; for Prior-Calibrated ERM (PC-ERM), it raises AUROC from 46.49 to 85.67 on CIFAR-10-LT and from 50.40 to 78.35 on CIFAR-100-LT. This simple PC-ERM+HPM pipeline also achieves the best Log Efficiency Score (LES; 3.08) on CIFAR-100-LT, retaining roughly 95% of the best CIFAR-100-LT AUROC observed among the compared post-hoc scores at substantially lower training-time cost. These results argue for evaluating representation quality, detector geometry, and training complexity as separate factors in LT-OOD detection.

---


### 409. [GenTS: A Comprehensive Benchmark Library for Generative Time Series Models](https://arxiv.org/abs/2605.17804)

**<font color=#1a73e8>作者：</font>** Chenxi Wang, Xiaorong Wang, Peiyang Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models have demonstrated remarkable potential in time series analysis tasks, like synthesis, forecasting, imputation, etc. However, offering limited coverage for generative models, existing time series libraries are mainly engineered for discriminative models, with standardized workflows for specific tasks, such as optimizing Mean Squared Errors for time series forecasting. This rigid structure is fundamentally incompatible with the distinct and often complex paradigms of generative models (e.g., adversarial training, diffusion processes), which learn the underlying data distribution rather than a direct input-output mapping. To this end, we proposed GenTS, a comprehensive and extensible benchmark library designed for systematic assessment on generative time series models. GenTS features a unified data preprocessing pipeline, a collection of versatile models, and panoramic evaluation metrics. Its modular design also enables the researchers to flexibly customize beyond our built-in datasets and models. Based on GenTS, we conducted benchmarking experiments under diverse tasks, accordingly offering suggestions for model selection and identifying potential directions for future research. Our codes are open-source at this https URL. The official tutorials and document are available at this https URL.

---


### 410. [Curriculum Group Policy Optimization: Adaptive Sampling for Unleashing the Potential of Text-to-Image Generation](https://arxiv.org/abs/2605.17807)

**<font color=#1a73e8>作者：</font>** Baoteng Li, Xianghao Zang, Xinran Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-Image (T2I) generation has achieved remarkable progress in recent years. Meanwhile, reinforcement learning methods, particularly those based on Group Relative Policy Optimization (GRPO), have attracted widespread attention and been successfully applied to T2I tasks. However, the uniform sampling strategy commonly used during training often ignores the match between sample difficulty and the model's current learning capability, leading to low training efficiency. We argue that improving training efficiency requires continuously prioritizing prompts that match the model's evolving capability and remain actively learnable. To this end, we propose Curriculum Group Policy Optimization (CGPO), an adaptive curriculum training framework. During training, each prompt produces a group of images scored by a reward model. We use the variance of group rewards as an online proxy for prompt inconsistency. A higher variance suggests that the model has partially captured the prompt requirements but has not yet achieved stable mastery. Such prompts are more likely to provide useful learning signals, so we increase their sampling probabilities accordingly. Additionally, to address data imbalance in multi-category datasets, we design a category calibration method based on proportional fairness optimization, which balances training difficulty across categories. Experiments on GenEval, T2I-CompBench++, and DPG Bench demonstrate that our framework effectively improves generation performance.

---


### 411. [A Unified Framework for Data-Free One-Step Sampling via Wasserstein Gradient Flows](https://arxiv.org/abs/2605.17808)

**<font color=#1a73e8>作者：</font>** Chenguang Wang, Tianshu Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop a unified theoretical framework for data-free one-step sampling from unnormalized target distributions based on Wasserstein gradient flows. For a broad class of standard f-divergence objectives, we show that the induced velocity field admits the universal form $\mathbf{V}(x)=w(r(x))\,\beta(x)$, where $\beta(x)=\nabla \log (p(x)/q(x))$ is shared across objectives and $w$ is determined solely by the choice of divergence. This decomposition shows that standard f-divergence drifts share the same asymptotic target distribution $p$ and differ primarily in how they redistribute transient repair effort across under-covered regions. To formalize this distinction, we derive a one-step regional-response theory for a soft under-coverage functional and obtain a compression--elasticity identity that links divergence choice to the geometry of mass transport into under-covered regions. We further extend the framework beyond the f-divergence family to the Log-Variance (LV) divergence, analyze how the reference distribution alters the resulting drift structure, and motivate a practical LV-inspired surrogate for data-free training. Based on this theory, we instantiate the framework with a KDE-based implementation and describe a complementary normalizing-flow route, enabling one-step inference after training. Experiments on multimodal Gaussian-mixture benchmarks are consistent with the theoretical predictions and demonstrate effective one-step sampling on these targets.

---


### 412. [One Model, Two Roles: Emergent Specialization in a Shared Recurrent Transformer](https://arxiv.org/abs/2605.17811)

**<font color=#1a73e8>作者：</font>** Jucheng Shen, Barbara Su, Anastasios Kyrillidis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can a shared-weight recurrent Transformer develop distinct internal roles without being partitioned into separate modules? We study this in Asymmetric Input Recurrence (AIR), a minimal two-state reasoning architecture in which the same Transformer model is reused for both updates (per literature, L and H) and the only built-in difference in the update rule is that the encoded input is injected during L-updates but not H-updates. Across Sudoku-Extreme and Maze, decoded rollouts reveal a consistent split: $\zH$ behaves like a fully committed proposal state, whereas $\zL$ retains local uncertainty and shifting intermediate structure. Freeze experiments show that this split is, in practice, related to the model's state dynamics: in Sudoku, freezing $\zH$ reduces $\zL$'s content changes whereas freezing $\zL$ increases $\zH$'s, while in Maze, freezing either state increases content changes in the other state. Ablations show that to induce specialization, the shared model needs to be able to tell the two update types apart, either from input injection asymmetry or from a separate level token. Mechanistically, attention analysis shows that L-updates are consistently more local than H-updates in both Sudoku and Maze. Together, these results show that, in a two-state recurrent setting, a clear state-identity signal can induce stable, related functional roles inside a shared-parameter recurrent Transformer. Code is available at \href{this https URL}{\textcolor{blue}{this https URL}}.

---


### 413. [Going Headless? On the Boundaries of Vertical AI Firms](https://arxiv.org/abs/2605.17812)

**<font color=#1a73e8>作者：</font>** Muhammad Zia Hydari, Farooq Muzaffar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vertical AI firms in accounting, law, healthcare, procurement, and similar domains historically bundled workflow, domain logic, and accountability into a single application. General-purpose AI agents are now unbundling that package, prompting founders and investors to advocate "going headless": cede the workflow and interface to agents and expose domain expertise as callable services. This article argues that going headless is correct for some firms and destructive for others, and that the latter often cede their value capture inadvertently through architectural choices that look like interface decisions. This is a boundary question, and the answer turns on distinguishing the interface boundary, which can often move, from the accountability boundary, which often must not. Drawing on Coase's theory of the firm, Eisenmann, Parker, and Van Alstyne's platform envelopment framework, and Teece's analysis of complementary assets and appropriability, the article shows that orchestrators operating through open protocols acquire envelopment power even as technical interoperability improves, and that durable value capture concentrates in cospecialized accountability assets: professional signoff, regulated workflows, evidence trails, and trusted systems of record. The article proposes a three-position taxonomy (component, integrated software platform, dual-track) determined not by sector but by task-accountability regime, and formalizes the construct of rule debt: the future governance, maintenance, and accountability burden that accrues to customer organizations when business rules and professional standards migrate from governed systems into prompts and agent instructions. Four principles follow: decompose by accountability not interface, invert the edges while retaining the core, position rule debt as the customer cost the integrated platform prevents, and avoid single-orchestrator dependence.

---


### 414. [Evidence-Guided Unknown Rejection for High-Confidence Near-Known Unknowns](https://arxiv.org/abs/2605.17818)

**<font color=#1a73e8>作者：</font>** Xi Chen, Yingjun Xiao, Gang Fang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-set recognition systems face a neglected failure mode: high-confidence near-known unknowns, which lie outside the known label set but are close enough to known classes that a closed-set classifier accepts them with high confidence. We show that this failure is widespread across scalar-threshold methods, including recent post-hoc detectors, and that stronger encoders can amplify rather than remove the risk. We propose EGUR-A, which changes the decision from ``is this sample's score high enough?'' to ``does this predicted known class have sufficient evidence to accept this sample?'' EGUR-A combines class-conditional local acceptance evidence with global residual evidence, and selects their relative weight from known-sample statistics without unknown validation data. Across CUB, FGVC-Aircraft, and ImageNet-hard, EGUR-A substantially reduces high-confidence false known acceptance at matched known-rejection operating points. The result is not a stronger threshold; it is a different question: whether a known class is entitled to accept a sample.

---


### 415. [Unleashing the Representational Power of Fourier Shapes for Attacking Infrared Object Detection](https://arxiv.org/abs/2605.17822)

**<font color=#1a73e8>作者：</font>** Yixing Yong, Jian Wang, Ming Lei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared object detection is crucial for perception in autonomous driving and surveillance but remains vulnerable to physical adversarial attacks. Unlike in the RGB domain, where attacks rely on color texture, infrared attacks must manipulate thermal signatures, making the geometry shape of heat-blocking materials the primary adversarial information carrier. Current shape-based methods suffer from a fundamental trade-off between representational capability and optimization power, limiting their attack this http URL this work, we overcome this dilemma by introducing learnable Fourier shapes to the infrared domain. We utilize an end-to-end differentiable framework where a compact set of Fourier coefficients, defining the shape boundary, is analytically mapped to a pixel-space mask via the winding number theorem. This enables efficient gradient-based optimization to generate potent shapes that cause human targets to evade detection. Extensive digital and physical experiments provide a comprehensive evaluation and validate our superior performance. Our resulting physical patch achieves striking robustness, successfully evading detectors across diverse distances, angles, poses, and individuals, and achieves over 88% attack success rate at distances greater than 25m (conf.=0.5). Code is available at this https URL.

---


### 416. [Content-Style Identification via Differential Independence](https://arxiv.org/abs/2605.17827)

**<font color=#1a73e8>作者：</font>** Subash Timilsina, Hoang-Son Nguyen, Sagar Shrestha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative analysis often models multi-domain observations as nonlinear mixtures of domain-invariant content variables and domain-specific style variables. Identifying both factors from unpaired domains enables tasks such as domain transfer and counterfactual data generation. Prior work establishes identifiability under (block-wise) statistical independence between content and style, or via sparse Jacobian assumptions on the nonlinear mixing function, but such conditions can be restrictive in practice. In this work, we introduce content-style differential independence (CSDI), an alternative structural condition requiring that infinitesimal variations in content and style induce orthogonal directions on the data manifold, thereby enabling identifiability even when content and style are dependent and the Jacobian is dense. We operationalize this condition through a blockwise orthogonality constraint on the Jacobian subspaces associated with content and style. To support high-dimensional generative models, we design a stochastic regularizer based on numerical Jacobian approximation, enabling scalable training in settings such as high-resolution image generation. Experiments across multiple datasets corroborate the identifiability analysis and demonstrate practical benefits on counterfactual generation and domain translation.

---


### 417. [Efficient Bilevel Optimization for Meta Label Correction in Noisy Label Learning](https://arxiv.org/abs/2605.17833)

**<font color=#1a73e8>作者：</font>** Ba Hoang Anh Nguyen, Viet Cuong Ta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training a deep neural network with noisy labels could reduce data annotation cost but may introduce noise into the learned model. In meta label correction approaches, an additional meta model besides the main model is trained with a small, clean dataset to correct the large, noisy dataset. However, the update of the meta model requires the computation of hypergradients at the inner step of the main model which signif- icantly increases the computational cost. To improve the training efficiency, we first introduce the dynamic barrier gradient descent into standard meta label correction. While this naive extenstion is able to speed up the training process to approximately first- order complexity, it lacks mechanisms to prevent the leakage of noisy signals to the main model and to stabilize the learning of the meta model. Based on this observation, we propose the EBOMLC method, which is designed with three key improvements including one-step inner loop update, mixture upper loss and alignment- aware dynamic barrier. Empirical results on CIFAR-10 and CIFAR-100 demonstrate that EBOMLC consistently outperforms other baselines, especially under high noise rate settings, while reducing training time of the meta label correction approach.

---


### 418. [Stabilizing, Scaling & Enhancing MeanFlow for Large-scale Diffusion Distillation](https://arxiv.org/abs/2605.17834)

**<font color=#1a73e8>作者：</font>** Xiao He, Yang Li, Peizhen Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models exhibit remarkable generative capability, but their high latency limits practical deployment. Many studies have attempted to reduce sampling steps to accelerate inference. Among them, MeanFlow has attracted considerable attention due to its concise formulation and remarkable performance. Nevertheless, the instability of its optimization objective and the ''mean-seeking bias'' have limited its applicability to distill large-scale industrial models. To stabilize MeanFlow for distilling large-scale models, we first introduce a warm-up technique, in which the original differential solution of MeanFlow is replaced by a discrete solution. This design avoids training collapse caused by the MeanFlow target containing a stop-gradient term from an undertrained model. Once the model acquires a preliminary ability to fit the average velocity field, we switch the optimization objective back to the differential solution, enabling further refinement. Meanwhile, to alleviate the ''mean-seeking bias'' of MeanFlow under extremely few-step inference with complex target distributions, we incorporate trajectory distribution alignment as an auxiliary objective, encouraging the student model's trajectory distribution to align more closely with that of the teacher model. Our proposed distillation framework achieves superior performance compared to existing distillation approaches when applied to the text-to-image (T2I) model FLUX.1-dev (up to 12B parameters). Furthermore, when extended to the 80B-parameter state-of-the-art (SOTA) T2I model HunyuanImage 3.0, our method continues to demonstrate robust generalization and strong performance.

---


### 419. [Temporal Aware Pruning for Efficient Diffusion-based Video Generation](https://arxiv.org/abs/2605.17837)

**<font color=#1a73e8>作者：</font>** Sheng Li, Yang Sui, Junhao Ran 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video diffusion models have recently enabled high-quality video generation with ViT-based architectures, but remain computationally intensive because generation requires attention computation over long spatiotemporal sequences. Token pruning has proven effective for ViTs and VLMs. However, most prior pruning methods are attention-based and operate per frame, failing to ensure the vital temporal coherence across frames in video generation tasks. In practice, naively adopting attention-only pruning causes noticeable degradation due to worsened background consistency, flickering, and reduced image quality. To address this, we propose TAPE, a training-free Temporal Aware Pruning for Efficient diffusion-based video generation. TAPE (i) applies temporal smoothing to align token-importance across adjacent frames and suppress selection jitter; and (ii) performs token reselection in selected layers to align token pruning with layers' diverse semantic focus and avoid error accumulation in specific areas; it also (iii) adopt a timestep-level budget scheduling that prunes aggressively at early noisy steps and relaxes pruning during fidelity-critical refinement. The experimental results show that TAPE delivers significant speedups while preserving high visual fidelity, outperforming prior token reduction approaches.

---


### 420. [Balancing Knowledge Distillation for Imbalance Learning with Bilevel Optimization](https://arxiv.org/abs/2605.17839)

**<font color=#1a73e8>作者：</font>** Anh B.H. Nguyen, Ba Tho Phan, Viet Cuong Ta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation transfers knowledge from a high capacity teacher to a compact student using a mixture of hard and soft losses. On imbalanced data, a fixed weighting between hard and soft losses becomes brittle the learning process. Recent studies try to reweight these components in long-tailed settings. However, most of these meth- ods do not adapt weights at the sample-wise level and do not take into account the students behavior during training. To address this, we pro- pose BiKD - a bilevel framework that dynamically balances hard and soft losses for each sample. We employ a weight generation network that produces adaptive per-sample weights, guided by a small balanced vali- dation set. The student is now trained with an unconstrained combina- tion of weighted hard and soft losses, allowing the student to relax both terms. We further propose a multi-step SGD strategy to optimize the weight model more accurately and efficiently. Experiments on long-tailed CIFAR-10/100 show that our approach surpasses recent balanced distil- lation methods across imbalance factors.

---


### 421. [A Collaborative Rehabilitation-Exercise Serious Game for People with Stroke and their Caregivers: A Pilot Study](https://arxiv.org/abs/2605.17841)

**<font color=#1a73e8>作者：</font>** Elizabeth D. Vasquez, Jonathan Siskind, Marion S. Buckwalter 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Motivation to perform movement therapy and caregiver burnout are major challenges to post-stroke life. Serious games have been shown to support therapeutic tasks in people with stroke, but there are few activities that simultaneously support informal caregiver health, which is also impacted post-stroke. Here, we present a collaborative, mutually beneficial, serious game designed to support therapy for persons with stroke and also exercise for their informal caregivers. One player performs rehabilitative wrist movements - useful to people with stroke - and the other performs a seated march exercise - useful to informal caregivers - via pedals or a keyboard to control their avatar. We present a pilot study with 6 healthy dyads to evaluate how exercise-based input of one player, the Pseudo Caregiver (PCG), impacts motivation and emotional experience in both the PCG and Pseudo Person with Stroke (PPS). While not statistically significant, we find that PCGs Interest subscale scores trended higher when using a pedal (the exercised-based input) compared to a keyboard, regardless of game play mode. PPSs' positive affect scale scores and Competence subscale scores trended higher when their partner played collaboratively with a pedal compared to a keyboard. These trends encourage future work toward incorporating an exercise-based device, such as a pedal, to enhance the emotional and motivational experience of rehabilitative serious games for people with different movement ability levels.

---


### 422. [SNLP: Layer-Parallel Inference via Structured Newton Corrections](https://arxiv.org/abs/2605.17842)

**<font color=#1a73e8>作者：</font>** Ligong Han, Kai Xu, Hao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive language models execute Transformer layers sequentially, creating a latency bottleneck that is not removed by conventional tensor or pipeline parallelism. We study whether this layerwise dependency can be relaxed by treating the hidden-state trace across layers as the solution of a nonlinear residual equation and solving it with parallel Newton-style updates. While this view is principled, exact Newton corrections require expensive Jacobian-vector products and naive fixed-point iterations are unstable on trained Transformers. We introduce Structured Newton Layer Parallelism (SNLP), a training and inference framework that replaces exact layer Jacobians with cheap architecture-induced surrogate dynamics. In residual Transformers, this yields Identity Newton (IDN), where the correction reduces to a prefix-sum-like update; in mHC-style architectures, HC Newton (HCN) uses the model's residual mixing matrix. We further introduce SNLP-aware regularization, which trains models to make one or a few structured Newton iterations accurately approximate the sequential forward. Experiments on nanochat-scale Transformers show that SNLP regularization improves layer-parallel compatibility and can also improve standard sequential perplexity, reducing baseline PPL by 4.7%-23.4%. At inference time, SNLP combined with layer fusion and chunkwise decomposition achieves practical wall-clock speedups: on a 0.5B Nanochat model, it reaches 2.3x speedup while still improving PPL by 6.1%. These results suggest that layer-parallel inference is not merely a numerical approximation to sequential execution, but can act as a useful solver-induced inference bias. We also characterize limitations: off-the-shelf pretrained models are less amenable to this procedure, and exact convergence recovers the sequential computation rather than providing monotonic inference-time scaling.

---


### 423. [Generating Pretraining Tokens from Organic Data for Data-Bound Scaling](https://arxiv.org/abs/2605.17849)

**<font color=#1a73e8>作者：</font>** Zichun Yu, Chenyan Xiong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM pretraining is shifting from a compute-bound to a data-bound regime, where available human (organic) text falls far short of scaling demands. However, reaching the data-bound regime does not mean the model has fully utilized its organic corpus. In this paper, we introduce SynPro, a synthetic data generation framework that helps LLMs more thoroughly learn from limited organic data. SynPro applies two operations, rephrasing and reformat, that present the same organic source in diverse forms to facilitate deeper learning without introducing external information. Both generators are optimized via reinforcement learning with quality, faithfulness, and data influence rewards, and are continuously updated as pretraining plateaus to target content the model has yet to absorb. We pretrain 400M and 1.1B models with 10% of their Chinchilla-optimal tokens (0.8B and 2.2B) from DCLM-Baseline, reflecting a realistic data-bound regime in frontier pretraining. Our results reveal that organic data is significantly underutilized by standard repetition: SynPro unlocks 3.7-5.2x the effective tokens of repetition, even surpassing the non-data-bound oracle that trains on equivalent unique data at the 1.1B scale. Analyses confirm that faithful, model-aware synthesis sustains data-bound scaling without causing distribution collapse. We open-source our code at this https URL.

---


### 424. [Learning over Positive and Negative Edges with Contrastive Message Passing](https://arxiv.org/abs/2605.17854)

**<font color=#1a73e8>作者：</font>** Peter Pao-Huang, Charilaos I. Kanatsoulis, Michael Bereket 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conventional approaches to learning on graphs involve message passing along existing (i.e., positive) edges to update node features. However, these approaches often disregard the potentially valuable information contained in the absence (i.e., negative) of edges. Here, we theoretically analyze the value of negative edges in graph representations and prove that in settings of low label rates, high homophily, and high edge density, access to negative edges provides significant information gain over using only positive edges. Motivated by this insight, we introduce Contrastive Message Passing (CMP), a general message passing architecture that enable graph neural network layers to reason over positive and negative edges. By imposing soft positive semidefinite constraints on the learnable weights, our approach differentially applies similarity-preserving transformations to positively connected nodes and dissimilarity-inducing transformations to negatively connected nodes. Over simulated and real datasets in varying data regimes, CMP consistently outperforms baselines in low-label settings when negative edges are informative.

---


### 425. [Towards SocratiCode: Designing a Generative AI-Based Programming Tutor for K-12 Students through a 4-Week Participatory Design Study](https://arxiv.org/abs/2605.17857)

**<font color=#1a73e8>作者：</font>** Cassandra Lucas, Anshul Bihani, Rohini Kukka 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI creates new opportunities for programming education, but many existing systems remain overly directive, producing lengthy explanations and premature solutions that can overwhelm K-12 novices. In this paper, we present a participatory design study of how an adaptive tutorial system, SocratiCode, evolved toward a Socratic tutoring model for beginner programming instruction. Drawing on weekly learner feedback, we iteratively refined the system over a four-week study with two K-12 students learning Python. Across iterations, the system shifted from flexible tutorial generation toward a more dialogic form of support characterized by guided questioning, reflection prompts, misconception checks, incremental hints, and mandatory pauses for learner input. Our preliminary observations suggest that this Socratic shift improved explanation clarity, supported problem-solving engagement, and better aligned instruction with novice learners' needs, especially when combined with human guidance. We argue that generative AI in K-12 programming education may be most effective not as an answer engine, but as a Socratic, adaptive learning companion embedded within a human-guided instructional framework.

---


### 426. [Multi-site PPG: An In-the-Wild Physiological Dataset from Emerging Multi-site Wearables](https://arxiv.org/abs/2605.17859)

**<font color=#1a73e8>作者：</font>** Jiayi Shao, Jiaying Ye, Shengyao Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Wearables are widely used for mobile health monitoring, and photoplethysmography (PPG) is a key sensing modality for heart rate and related physiological measurements. However, public in-the-wild PPG datasets remain largely wrist-centric or limited to short, controlled studies, constraining research on emerging wearable form factors. We present Multi-site PPG, an in-the-wild physiological dataset collected from four custom-developed unobtrusive wearables: a smart earring, ring, watch, and necklace. Each device records green and infrared reflective PPG, 3-axis acceleration, and temperature with timestamps for cross-device alignment, while a Polar H10 chest strap provides reference electrocardiogram (ECG). Participants wore the devices for multiple days during daytime activities while continuing their normal routines. The dataset contains over 350 hours of raw data and 230-290 hours of modeling-ready 8-second windows per wearable. We benchmark heuristic, supervised, and self-supervised heart-rate estimation methods, showing substantial body-site differences: the best methods achieve mean absolute errors (MAEs) of 2.30 bpm on the earring, 5.13 bpm on the ring, 8.37 bpm on the watch, and 8.68 bpm on the necklace. We further analyze motion effects and evaluate multi-site and PPG-accelerometer fusion, demonstrating the dataset's value for robust physiological sensing across emerging wearable form factors.

---


### 427. [PAREDA: A Multi-Accent Speech Dataset of Natural Language Processing Research Discussions](https://arxiv.org/abs/2605.17860)

**<font color=#1a73e8>作者：</font>** Sicheng Jin, Dipankar Srirag, Aditya Joshi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While modern Automatic Speech Recognition (ASR) systems achieve high accuracy on benchmark corpora, their performance often degrades when there is real-world variability. This work focuses on variability arising due to accented, spontaneous, and domain-specific speech. In particular, we introduce PAper REading DAtaset (PAREDA), a first-of-its-kind multi-accent speech dataset consisting of discussions on academic Natural Language Processing (NLP) papers between speakers with Australian, Indian-English, and Chinese English accents. Each session elicits a spontaneous monologue (a summary of a paper's abstract) and a non-monologue (a question-and-answer session between participants), resulting in a corpus rich with technical jargon and conversational phenomena. We evaluate the performance of SOTA ASR models on PAREDA, analysing the impact of accent mixing and increased speech rate. Our results show that, in the zero-shot setting, models perform worse, confirming the dataset's challenging nature. However, fine-tuning on PAREDA significantly reduces the Word Error Rate (WER), demonstrating that our dataset captures linguistic characteristics often missing from existing corpora. PAREDA serves as a valuable new resource for building and evaluating more robust and inclusive ASR systems for specialised, real-world applications.

---


### 428. [Imaging Hidden Objects with Consumer LiDAR via Motion Induced Sampling](https://arxiv.org/abs/2605.17865)

**<font color=#1a73e8>作者：</font>** Siddharth Somasundaram, Aaron Young, Akshat Dave 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LiDARs are being increasingly deployed for consumer imaging in handheld, wearable, and robotic applications. These sensors can capture the time-of-flight of light at picosecond resolution, which in principle, enables them to capture information about objects hidden from their field of view. While such non-line-of-sight (NLOS) imaging capabilities have been shown on research-grade LiDARs, they are challenging to achieve on consumer devices due to poor signal quality resulting from low laser power, low spatial resolution, and object and camera motion. Inspired by burst photography and synthetic aperture radar, we propose a multi-frame fusion strategy to overcome these challenges and demonstrate NLOS imaging on consumer LiDAR. We first introduce the motion-induced aperture sampling model to unify the effects of object shape, object motion, and camera motion under a single measurement model. Using this model, we demonstrate several NLOS capabilities on a smartphone-grade LiDAR: (1) 3D reconstruction, (2) single and multi-object tracking, and (3) camera localization using hidden objects. Previously, NLOS imaging capabilities were largely restricted to bulky and expensive research-grade hardware that requires extensive setup and calibration. Our results represent a shift towards plug-and-play NLOS imaging, where anyone can image hidden objects with off-the-shelf hardware ($<100) and no additional setup. We believe that democratization of such capabilities will advance consumer applications of NLOS imaging.

---


### 429. [DAD4TS: Data-Augmentation-Oriented Diffusion Model for Time-Series Forecasting with Small-Scale Data](https://arxiv.org/abs/2605.17866)

**<font color=#1a73e8>作者：</font>** Masahiro Suzuki, Bohui Xia, Hiroto Yamamoto 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Small-scale data is a critical problem in time-series forecasting tasks. Data augmentation is an effective strategy for this task, but it has a limitation in generating meaningful data. To address this limitation, we propose DAD4TS, a diffusion-model-based data augmentation method with reinforcement learning, designed for time-series forecasting with small-scale data. In DAD4TS, a data generator is simultaneously trained with a time-series model and controlled by a reinforcement learning model to efficiently generate samples that improve the forecast accuracy of the time-series model. To support small-scale data, we use mathematical methods instead of conventional VAE methods to train the diffusion model by projecting the time-series data into the geometric space. We validated the effectiveness of DAD4TS with seven comparative methods through qualitative and quantitative experiments on six real-world datasets and eight time-series models. As a result, DAD4TS was validated on five datasets.

---


### 430. [PySIFT: GPU-Resident Deterministic SIFT for Deep Learning Vision Pipelines](https://arxiv.org/abs/2605.17869)

**<font color=#1a73e8>作者：</font>** Sivakumar K.S., Mohammad Daniyalur Rahman, Gopi Raju Matta  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A widespread assumption in local feature research holds that classical handcrafted descriptors are accuracy-limited relics best replaced by learned alternatives. We show this is wrong. Through an 8-configuration ablation spanning four benchmarks (HPatches, ROxford5K, IMC Phototourism, MegaDepth), we demonstrate that classical SIFT with DSP multi-scale pooling outperforms neural descriptor and orientation replacements (HardNet, OriNet) on every accuracy metric--while running 2--18$\times$ faster--and that learned matchers (LightGlue) complement rather than supersede classical features. The conclusion reframes a decade of work: not "replace SIFT" but "compose with SIFT," classical extraction paired with learned matching only where geometric context demands it. This finding was invisible because no prior GPU SIFT kept the complete pipeline in VRAM or offered modularity for controlled classical-vs-learned ablations. We present PySIFT, the first fully GPU-resident SIFT, implemented in CuPy/Numba CUDA kernels with DLPack zero-copy handoff to downstream DL frameworks--submillisecond O(1) metadata swap regardless of keypoint count. On a laptop-grade NVIDIA RTX 3050 (4 GB VRAM), PySIFT achieves: (i) higher Mean Matching Accuracy (MMA) than OpenCV SIFT on HPatches, (ii) 383 ms faster per pair on high-resolution MegaDepth, (iii) higher geometric accuracy on cross-dataset benchmarks (+5.6 pp AUC@10${}^\circ$ on MegaDepth, more inliers on IMC Phototourism), and (iv) bitwise deterministic output--identical keypoints and descriptors across runs, with detection reproducing identically even across GPU architectures: a guarantee that learned extractors cannot match without significant performance sacrifice, and cannot achieve at all across GPU architectures due to cuDNN's architecture-dependent algorithm selection. PySIFT is open-source, requiring no C++ compilation.

---


### 431. [HINT-SD: Targeted Hindsight Self-Distillation for Long-Horizon Agents](https://arxiv.org/abs/2605.17873)

**<font color=#1a73e8>作者：</font>** Woongyeng Yeo, Yumin Choi, Taekyung Ki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training long-horizon LLM agents with reinforcement learning is challenging because sparse outcome rewards reveal whether a task succeeds, but not which intermediate actions caused the outcome or how they should be corrected. Recent methods alleviate this issue by generating rewards or textual hints from turn-level action-output signals, or by using feedback-conditioned self-distillation. However, generating feedback at every turn is inefficient when many intermediate turns are already successful or neutral, and applying feedback at a fixed or misaligned turn often fails to supervise the actions that contributed to the failure. To bridge this gap, we propose HINT-SD, a targeted self-distillation framework that uses full-trajectory hindsight to select failure-relevant actions and applies feedback-conditioned distillation only on targeted action spans. Experiments on BFCL v3 and AppWorld show that our method improves over the dense per-turn feedback baseline by up to 18.80 percent while achieving 2.26$\times$ lower time per training step, suggesting that selecting where to distill is a key factor for both effective and efficient long-horizon agent training.

---


### 432. [HexagonalWarriorMamba: Superior Threshold-Dependent Multi-label Classification of 12-Lead ECG Cardiac Abnormalities](https://arxiv.org/abs/2605.17875)

**<font color=#1a73e8>作者：</font>** Huawei Jiang, Husna Mutahira, Shibo Wei 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The accurate automated diagnosis of cardiac abnormalities from 12-lead electrocardiograms (ECGs) is critical for managing cardiovascular disease. However, detecting concurrent conditions remains a challenge for traditional deep learning models, which often have limited ability to model the long-range dependencies inherent in ECG signals. This manuscript proposes HexagonalWarriorMamba (HWMamba), a framework built on the Mamba architecture that processes 12-lead ECGs as single-channel 2D images rather than conventional 1D time series. By integrating a hierarchical architecture with a 2D Selective Scan mechanism, HWMamba is designed to model global context and complex spatial relationships within the data. The model is evaluated on the PhysioNet/Computing in Cardiology Challenge 2021 dataset, which includes 26 diagnostic labels and comprises recordings collected from seven institutions across four countries and three continents. Results demonstrate that HWMamba outperforms current state-of-the-art (SOTA) methods across five key threshold-dependent metrics, including Challenge Score and Subset Accuracy. These improvements provide a balance between strong discriminative capability and effective threshold selection derived from the training data, while maintaining near-SOTA performance in Macro AUROC. This Hexagonal Warrior performance, reflecting consistent performance across multiple evaluation dimensions, positions HWMamba as a robust and versatile approach for multi-label ECG classification.

---


### 433. [PAIR: Prefix-Aware Internal Reward Model for Multi-Turn Agent Optimization](https://arxiv.org/abs/2605.17877)

**<font color=#1a73e8>作者：</font>** Wonjoong Kim, Yeonjun In, Sangwu Park 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A significant hurdle for current LLMs is the execution of complex, multi-stage tasks. Group Relative Policy Optimization (GRPO) has been emerging as a leading choice, but its reliance on sparse outcome rewards severely limits credit assignment across intermediate steps. Existing remedies such as running full rollouts to assign step-level advantages, calling external LLM judges at each step, or computing intrinsic rewards that require ground-truth answers at every evaluation introduce significant costs or practical constraints. We hypothesize that internal correctness probing over LLM hidden states can be repurposed as a step-level reward signal, potentially addressing all of these limitations at once. However, existing probing research assumes clean inputs, and we first show that this assumption breaks down in multi-step settings: hidden-state probes degrade severely under prefix contamination tracking coherence with the (possibly corrupted) prefix rather than grounded correctness, while attention-based features remain robust to contamination but underperform on clean prefixes. Building on this complementary relationship, we propose the Prefix-Aware Internal Reward (PAIR), a two-stage model with a frozen hidden-state probe estimating belief-consistency and a lightweight attention-based head correcting it toward grounded correctness. Experimental results show that PAIR achieves the highest AUROC on contaminated trajectories while operating at negligible inference cost, enabling dense step-level reward signals for GRPO training without external model calls, ground-truth dependencies, or full-trajectory rollouts.

---


### 434. [Multi-agent AI systems outperform human teams in creativity](https://arxiv.org/abs/2605.17885)

**<font color=#1a73e8>作者：</font>** Tiancheng Hu, Yixuan Jiang, Haotian Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although artificial intelligence (AI) now matches or exceeds human performance across numerous cognitive tasks, creativity remains a highly contested frontier. As AI systems based on large language models (LLMs) are increasingly adopted in research and innovation, it is essential to understand and augment their creativity. Here we demonstrate that multi-agent LLM teams not only surpass single agents, but also substantially outperform human teams in creativity (Cohen's d=1.50) across 4,541 multi-agent LLM ideas and 341 human-team ideas on six diverse problem-solving tasks. This advantage is driven by novelty while maintaining comparable usefulness. To investigate the generative processes in both groups, we represent conversations as paths through semantic space using neural language model representations. Both LLM and human teams produce more creative ideas when conversations range widely rather than staying centered on a single theme (low global coherence). However, the additional patterns that predict creativity differ: LLM teams benefit from efficient exploration (high semantic spread, shorter paths), while human teams benefit from maintaining smooth conversational flow (high local coherence, frequent pivots). Additionally, we identify model choice and discussion structure as orthogonal design levers that together explain 26.8% of variance in LLM conversational dynamics, paving the way for systematic approaches to developing multi-agent systems with augmented creative capabilities.

---


### 435. [Attention Sinks and Outliers in Attention Residuals](https://arxiv.org/abs/2605.17887)

**<font color=#1a73e8>作者：</font>** Haozheng Luo, Haoran Dai, Shaoyang Zhang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose OASIS, an outlier- and sink-aware technique built on inter-layer null signaling. As AttnResidual architectures introduce an additional depth-wise normalization channel, they improve inter-layer routing flexibility but also exacerbate attention sinks, activation outliers, and the resulting degradation in inference stability and quantization robustness. OASIS addresses this issue by introducing a Softmax1-based null space and coupling token-level null evidence to depth routing through an inter-layer null signal, thereby reducing sink-dominated routing and improving structural robustness. Theoretically, we show that the dual-normalization design of AttnResidual intensifies sink formation and quantization brittleness. Experimentally, we compare OASIS against five baselines on three real-world datasets and observe consistent improvements in both attention sink and post-quantization performance. Notably, OASIS achieves an average reduction of 9.26% in maximum infinity norm and 2.60% in average kurtosis across the evaluated settings, while lowering perplexity by 75.85% under W8A8 and improving GSM8K Pass@1 by 12.42% under W4A4.

---


### 436. [Explainable Machine Learning for Phishing Detection on Heterogeneous Datasets with MCP-Enabled Deployment](https://arxiv.org/abs/2605.17891)

**<font color=#1a73e8>作者：</font>** Nikhil Kumar Dora, Sumit Kumar Tetarave, Rishikesh Sahay 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the growth in digital transformation and Internet usage, the Social Engineering techniques such as Phishing have become a major concern for the users and the organizations. Phishing attacks involve deceptive techniques to trick users into revealing confidential information that causes financial loss and reputation damage to organizations. According to report of Verizon, 36% of all data breaches involved phishing, highlighting the need for intelligent, adaptive, and explainable security mechanisms. This paper examines the efficiency of different machine learning algorithms in phishing detection on heterogeneous phishing datasets that include a publicly available UCI dataset, our generated datasets using tools such as EvilGinx and Zphisher, and AI generated datasets. Moreover, this work incorporates explainable AI (XAI) techniques such as Information Gain, SHAP (SHapley Additive Explanations), and LIME (Local Interpretable Model-Agnostic Explanations) to examine the most influential features impacting classification outcomes. To support practical deployment, this work also incorporates an MCP-based phishing URL detection system that offers real-time URL analysis, feature extraction, confidence-based classification, and AI-assisted security interpretation. The experimental results demonstrate that among classical models the highest accuracy is obtained by Logistic Regression at 92.44%, among ensemble models CatBoost achieved the highest accuracy at 95.01%, among neural network CNN achieved an accuracy of 94.02%, and among transformer-based models, DistilBERT got the highest accuracy at 99.78%

---


### 437. [Lightweight Gaussian Process Inference in C++ on Metal and CUDA](https://arxiv.org/abs/2605.17898)

**<font color=#1a73e8>作者：</font>** Yu-Hsueh Fang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gaussian process (GP) inference in Python is dominated by libraries such as GPyTorch and GPflow, which are built on deep-learning frameworks and inherit their dispatch overhead and dependency footprint. We present LightGP, a dependency-free C++17 library for GP regression with Python bindings, supporting Apple Metal and NVIDIA CUDA backends alongside tuned CPU paths via Apple Accelerate and OpenBLAS. LightGP provides four inference paths -- exact Cholesky, matrix-free conjugate gradients, sparse variational free energy, and structured kernel interpolation with FFT -- covering problems from $N{=}100$ to $N{=}500{,}000$. On an Apple M4, LightGP CPU is 2.6--8.7$\times$ faster than GPyTorch CPU for exact GP and ${\sim}1.5\times$ faster for sparse GP at every scale tested. On an NVIDIA RTX~3060, LightGP CUDA is 2.3--6.7$\times$ faster than GPyTorch CUDA for exact GP up to $N{=}2{,}048$, with GPyTorch closing the gap at $N{=}4{,}096$. A fused matrix-free kernel-vector product on Metal achieves 32$\times$ over the explicit path at $N{=}20{,}000$ with $O(N)$ memory, and an FFT-accelerated SKI matvec via Accelerate vDSP runs in sub-millisecond time at $N{=}200{,}000$. LightGP compiles as a single static library with zero external dependencies and is installable via \texttt{pip install lightgp

---


### 438. [DCFold: Efficient Protein Structure Generation with Single Forward Pass](https://arxiv.org/abs/2605.17899)

**<font color=#1a73e8>作者：</font>** Zhe Zhang, Yuanning Feng, Yuxuan Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AlphaFold3 introduces a diffusion-based architecture that elevates protein structure prediction to all-atom resolution with improved accuracy. This state-of-the-art performance has established AlphaFold3 as a foundation model for diverse generation and design tasks. However, its iterative design substantially increases inference time, limiting practical deployment in downstream settings such as virtual screening and protein design. We propose DCFold, a single-step generative model that attains AlphaFold3-level accuracy. Our Dual Consistency training framework, which incorporates a novel Temporal Geodesic Matching (TGM) scheduler, enables DCFold to achieve a 15x acceleration in inference while maintaining predictive fidelity. We validate its effectiveness across both structure prediction and binder design benchmarks.

---


### 439. [Beyond Euclidean Prototypes: Spectral Disentanglement and Geodesic Matching for Few-Shot Medical Image Segmentation](https://arxiv.org/abs/2605.17904)

**<font color=#1a73e8>作者：</font>** Penghao Jia, Zhiyong Huang, Mingyang Hou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-Shot Medical Image Segmentation (FSMIS) aims to delineate novel anatomical targets from one or a few annotated support images, addressing the annotation scarcity in medical imaging. Notwithstanding recent advancements, current prototype-based methods are bottlenecked by two coupled limitations: 1) cue entanglement, where a single spatial-domain prototype is forced to summarise organ silhouette, parenchymal texture and boundary appearance simultaneously, so any support-query mismatch on one cue propagates indiscriminately to the others; and 2) topology-blind matching, where cosine similarity measures distance in the ambient Euclidean space and ignores the connectivity of the underlying feature manifold, causing fragmented activations inside low-contrast organs and leakage into neighbouring tissues. To this end, we propose Spectral-Geodesic Prototype Network (SGP-Net), built around a Spectral-Geodesic Prototype Module with two coupled components. A Spectral Prototype Bank (SPB) decomposes support and query features into low-, mid- and high-frequency bands via learnable radial Fourier filters, yielding three disentangled prototypes per class that separately encode shape, texture and boundary cues. A Geodesic Matcher (GM) then replaces cosine similarity with a differentiable heat-diffusion approximation of geodesic distance, propagating matching signals along a feature affinity graph so that on-manifold pixels accumulate consistent responses while off-manifold look-alikes are suppressed. Experiments on three public FSMIS benchmarks demonstrate that SGP-Net achieves competitive performance against recent state-of-the-art methods.

---


### 440. [One Model to Translate Them All: Universal Any-to-Any Translation for Heterogeneous Collaborative Perception](https://arxiv.org/abs/2605.17907)

**<font color=#1a73e8>作者：</font>** Yang Li, Weize Li, Quan Yuan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> By sharing intermediate features, collaborative perception extends each agent's sensing beyond standalone limits, but real-world feature modality heterogeneity remains a key barrier to effective fusion. Most existing methods, including direct adaption and protocol-based transformation, typically rely on training adapters for newly emerging feature modalities and often require additional retraining or fine-tuning. Such repeated training is costly and is often infeasible across manufacturers due to model and data privacy constraints, limiting real-world scalability. To address this issue, we propose UniTrans, a universal any-to-any feature modality translation model that instantiates translators on the fly for arbitrary modalities.
UniTrans pretrains a bank of translator expert parameters and learns their combination coefficients as a function of source-to-target modality mapping. The mapping is measured in a modality-intrinsic latent space, where an intrinsic encoder extracts modality-specific yet scene-invariant codes from single-frame intermediate features, enabling UniTrans to instantiate translators in a zero-shot manner.
Experiments on OPV2V-H and DAIR-V2X demonstrate that UniTrans consistently outperforms state-of-the-art methods in both simulated and real-world settings, enabling efficient any-to-any translation through a universal model. The code is available at this https URL.

---


### 441. [A Pilot Benchmark for NL-to-FOL Translation in Planetary Exploration](https://arxiv.org/abs/2605.17911)

**<font color=#1a73e8>作者：</font>** Hayden Moore, Suman Saha, Mahfuza Farooque  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Future planetary exploration envisions autonomous robotic agents operating under severe communication constraints, without global positioning, and with minimal human intervention. In such environments, agents must not only perceive and act, but also reason over mission objectives, operational constraints, and evolving environmental conditions. While prior work has largely focused on perception and control, the translation of high-level mission knowledge into structured, machine-interpretable representations remains underexplored.
We introduce a pilot benchmark for translating natural language (NL) into First-Order Logic (FOL) within the domain of planetary exploration. The dataset is constructed from real mission documentation sourced from NASA's Planetary Data System (PDS), spanning missions from 2003 to 2013. These documents describe mission phases such as launch, boost, coast, cruise, and orbital operations in rich natural language. We manually annotate these documents with corresponding FOL representations that capture temporal structure, agent roles, and operational dependencies. In addition, we provide structured predicate vocabularies and typed constants to enable controlled experimentation with varying levels of prior knowledge. This pilot benchmark provides a foundation for research at the intersection of language understanding and formal reasoning, grounded in real-world, safety-critical mission data. The dataset is provided at: this https URL

---


### 442. [SurgLQA: Scalable Long-Horizon Surgical Video Question Answering](https://arxiv.org/abs/2605.17915)

**<font color=#1a73e8>作者：</font>** Diandian Guo, Xikai Yang, Ruiyang Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surgical Video Question Answering (VideoQA) provides a promising paradigm for dynamic intraoperative interpretation, enabling real-time decision support and context-aware retrieval in clinical environments. Nevertheless, existing approaches are predominantly restricted to images or short clips, limiting their ability to model long-range procedural dynamics and causal dependencies across extended surgical workflows. To address this challenge, we propose SurgLQA, a unified long-horizon VideoQA framework for scalable surgical reasoning. This framework incorporates Faithful Temporal Consolidation (FTC), which leverages intrinsic temporal cues to construct compact long-range representations while preserving fine-grained temporal fidelity. Further, we develop Temporally-Grounded Multi-Policy Scaling (TMS), an adaptive test-time inference paradigm that strategically adjusts policy-level reasoning capacity within temporally grounded contexts. To facilitate systematic evaluation, we restructured a long-duration colonoscopy VideoQA benchmark, Colon-LQA, and conducted extensive experiments on Colon-LQA and REAL-Colon-VQA. Experimental results demonstrate that our approach achieves consistent performance gains in long-range reasoning with temporally grounded inference. Code link: this https URL.

---


### 443. [Domain Transfer Becomes Identifiable via a Single Alignment](https://arxiv.org/abs/2605.17918)

**<font color=#1a73e8>作者：</font>** Sagar Shrestha, Subash Timilsina, Hoang-Son Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Domain transfer (DT) maps source to target distributions and supports tasks such as unsupervised image-to-image translation, single-cell analysis, and cross-platform medical imaging. However, DT is fundamentally ill-posed: push-forward mappings are generally non-identifiable, as measure-preserving automorphisms (MPAs) preserve marginals while altering cross-domain correspondences, leading to content-misaligned translation. Recent work shows that MPAs can be eliminated by jointly transferring multiple corresponding source/target conditional distributions, but supervision signals labeling such conditionals are not always available in practice. We develop an alternative route to DT identifiability. Under a structural sparsity condition on the Jacobian support pattern, we show that distribution matching together with a single paired anchor sample suffices to identify the ground-truth transfer -- requiring substantially less supervision than prior approaches. To enable practical high-dimensional learning, we further propose an efficient Jacobian sparsity regularizer based on randomized masked finite differences, yielding a scalable surrogate without explicit Jacobian evaluation. Empirical results on synthetic and real-world DT tasks validate the theory.

---


### 444. [GREEN GRID: A Web-Based E-Waste Recycling Platform](https://arxiv.org/abs/2605.17924)

**<font color=#1a73e8>作者：</font>** Yashodip Jagtap, Aaditya Bagul, Om Kothawal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Electronic waste (e-waste) is one of the fastest-growing waste streams worldwide due to rapid technological advancements and shorter device lifespans. Improper disposal releases hazardous substances that harm the environment and human health, while valuable materials such as gold, copper, and aluminum are lost if not recycled. In 2022, approximately 62 million metric tonnes of e-waste were generated globally, but only about 22% was formally recycled. India generated around 1.751 million metric tonnes in 2023-24, with only 43% processed through authorized channels. Green Grid is a full-stack web-based platform designed to simplify and encourage e-waste recycling through an E-Dumper Locator, Green Rewards System, Insights and Awareness Hub, Scheduled Pickup Service, Recycling Impact Calculator, Eco AI Assistant, and Eco-Marketplace. Developed using this http URL, this http URL, this http URL, SQL, Google Maps API, and JWT authentication, the platform transforms e-waste recycling into a transparent, educational, and rewarding process. By combining technology, awareness, and incentives, Green Grid promotes responsible disposal and supports circular economy practices for a more sustainable future.

---


### 445. [InfoFlow: A Framework for Multi-Layer Transformer Analysis](https://arxiv.org/abs/2605.17930)

**<font color=#1a73e8>作者：</font>** Penghao Yu, Haotian Jiang, Zeyu Bao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While the approximation properties of single-layer Transformer architectures have been studied in recent works, a rigorous theoretical understanding of the multi-layer setting remains limited. In this work, we establish that multi-layer Transformers possess fundamentally different approximation capabilities from single-layer ones: for certain retrieval tasks, any single-layer Transformer requires least $\Omega (\varepsilon^{-k})$ parameters to achieve precision $\varepsilon$, where $k$ grows linearly with sequence length $T$, whereas a two-layer Transformer with a single head per layer achieves the same approximation precision with at most $O (\varepsilon^{-1})$ parameters. To understand this separation, we identify two structural mechanisms underlying multi-layer approximation. Specifically, softmax attention can only efficiently retrieve the token attaining the maximum attention score, incurring exponential-in-length parameter cost for $k$-th largest retrieval with $k \geq 2$. Moreover, the parameter cost of decoding coupled information scales with the size of the retrieved token set. Motivated by these findings, we propose InfoFlow, a framework for multi-layer Transformers. The framework tracks an information set of accessible input positions at each token and layer, assigning an explicit approximation rate to each mode of information propagation. This abstraction recovers known approximation bounds, remains consistent with experimental observations on trained networks, and yields concrete predictions in settings where direct theoretical analysis is currently intractable. Our results provide a principled framework for reasoning about the approximation efficiency of multi-layer Transformers.

---


### 446. [AtlasVA: Self-Evolving Visual Skill Memory for Teacher-Free VLM Agents](https://arxiv.org/abs/2605.17933)

**<font color=#1a73e8>作者：</font>** Pan Wang, Yihao Hu, Xiujin Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language model (VLM) agents increasingly rely on memory-augmented reinforcement learning to reuse experience across long-horizon tasks, yet most existing frameworks store memory as text and depend on proprietary teacher models to summarize or refine it. This design is poorly matched to spatial decision making: geometric priors are compressed into lossy language, and sparse interaction is often supervised through delayed textual feedback rather than dense visually grounded signals. We argue that reusable experience for VLM agents should remain visually grounded. Based on this insight, we propose \textbf{AtlasVA}, a teacher-free visual skill memory framework that organizes memory into three complementary layers: spatial heatmaps, visual exemplars, and symbolic text skills. AtlasVA further evolves danger and affinity atlases directly from trajectory statistics and lightweight grid heuristics, and reuses these self-evolving atlases as potential-based shaping rewards for reinforcement learning. This unifies perception, memory, and optimization without external LLM supervision. Experiments on \textsc{Sokoban}, \textsc{FrozenLake}, 3D embodied navigation, and 3D robotic manipulation benchmarks show that AtlasVA consistently outperforms text-centric memory baselines and competitive VLM agents, with especially strong gains on spatially intensive tasks. Homepage: this https URL

---


### 447. [Universal Adversarial Triggers](https://arxiv.org/abs/2605.17936)

**<font color=#1a73e8>作者：</font>** Benedict Florance Arockiaraj, Alexander Feng, Jianxiong Cai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent works have illustrated that modern NLP models trained for diverse tasks ranging from sentiment analysis to language generation succumb to universal adversarial attacks, a class of input-agnostic attacks where a common trigger sequence is used to attack the model. Although these attacks are successful, the triggers generated by such attacks are ungrammatical and unnatural. Our work proposes a novel technique combining parts-of-speech filtering and perplexity based loss function to generate sensible triggers that are closer to natural phrases. For the task of sentiment analysis on the SST dataset, the method produces sensible triggers that achieve accuracies as low as 0.04 and 0.12 for flipping positive to negative predictions and vice-versa. To build robust models, we also perform adversarial training using the generated triggers that increases the accuracy of the model from 0.12 to 0.48. We aim to illustrate that adversarial attacks can be made difficult to detect by generating sensible triggers, and to facilitate robust model development through relevant defenses.

---


### 448. [Training data attribution in diffusion models via mirrored unlearning and noise-consistent skew](https://arxiv.org/abs/2605.17938)

**<font color=#1a73e8>作者：</font>** Joan Serrà, Dipam Goswami, Fabio Morreale 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training data attribution (TDA) should enable generative model interpretability and foster a variety of related downstream tasks. Nonetheless, current TDA approaches lack reliability and robustness, preventing their adoption in real-world setups. In this paper, we take a decisive step towards more reliable and robust TDA for diffusion models. We propose to perform TDA with mirrored unlearning and noise-consistent skew (MUCS). The idea is to fine-tune a second model with bounded mirrored gradient ascent, and to measure the normalized skew of this model with respect to the original one using consistent noise samples. We show that, while being conceptually simple and generic, MUCS systematically outperforms existing methods on three different datasets by a large margin. We additionally study the effect that core design choices have on final performance, and analyze novel aspects regarding the overlap of influential instances across generated items and the potential of ensembling TDA approaches. We believe that our findings may have broader implications for more general unlearning setups, as well as for tasks requiring the comparison of diffusion losses.

---


### 449. [UAVFF3D: A Geometry-Aware Benchmark for Feed-Forward UAV 3D Reconstruction](https://arxiv.org/abs/2605.17942)

**<font color=#1a73e8>作者：</font>** Xiang Yang, Yongli Wang, HaiFeng Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D reconstruction has recently demonstrated strong generalization across diverse scenes, yet its performance in UAV imagery remains underexplored due to distinctive acquisition geometries, large viewpoint variations, and ambiguity between horizontal field of view and flight height. We present UAVFF3D, a geometry-aware benchmark for feed-forward UAV 3D reconstruction, comprising over 170K real UAV images and more than 370K high-quality synthetic images. The benchmark also includes a challenging diagnostic test subset designed to analyze model behavior under UAV-specific geometric this http URL on UAVFF3D, we propose an evaluation protocol that jointly assesses camera-geometry estimation and reconstruction accuracy, addressing limitations of existing evaluations that rely on separate alignments. Experiments on four representative feed-forward reconstruction models show that UAV-domain adaptation substantially improves performance, reducing Ray Error by up to 84.2%, Pose ATE by up to 76.0%, and Chamfer Distance by up to 41.1%. Further analysis reveals that domain adaptation mitigates rotation-estimation degradation in oblique-view scenes and improves robustness under horizontal-field-of-view/height ambiguity. Incorporating camera priors further enhances reconstruction performance under UAV-specific acquisition geometries.

---


### 450. [Counting Machine Parts](https://arxiv.org/abs/2605.17952)

**<font color=#1a73e8>作者：</font>** Benedict Florance Arockiaraj, Elizabeth Dinella, Ankit Billa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Counting objects in an image is a task applicable across many domains. For instance, crowd counting, inventory counting, and cell counting have been the focus of recent research. The major challenges in estimating the count of objects include overlapping objects, object scale issues, occlusions, and varying lighting conditions. In this report, we explore the problem of counting machine washer parts. Our technique is an extension of FamNet with an additional loss component, trained on the given dataset. We compare to three baseline methods: a traditional image processing pipeline, instance segmentation, and density map estimation. We evaluate the performance of these algorithms by computing the Mean Absolute Error (MAE) and the Root Mean Squared Error (RMSE) between the true object counts and the model outputs. Our approach achieves a performance of 1.96 MAE.

---


> [!TIP]
> 当前位于：**401-450**（第 9/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-619](./part-13.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
