# 📦 其他研究 | 2026年08月25日

> 本类共 **158** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-158**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-158**

---

### 151. [Event-Time Confounding Under Bursty Human Dynamics](https://arxiv.org/abs/2608.21294)

**<font color=#1a73e8>作者：</font>** Michael Iannelli, Alan Ai  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Studies of digital behavior often align users at moments they choose, such as opening an AI assistant, clicking a recommendation, or visiting a product page, and interpret higher activity afterward as an event effect. We show how this creates an endogenous time zero: the event occurs during an ongoing task episode, so the aligned curve can trace episode continuation rather than a response to the event. In same-user, cross-surface web logs, AI, shopping, news, coding, and reference events are all preceded by broad activity increases that peak before time zero. Our strongest test uses known-null timestamps that cause nothing. Among the 5.8% of AI responses meeting strict pre-event activity and washout criteria, these timestamps show 3.42 times the post-event search activity of a within-user placebo, compared with 4.32 times for real events. The fraction of excess reproduced by the known null falls from 0.56 at detectably active moments to -0.04 at quiet moments, where the design detects none. We formalize this episode-selection bias, prove that a single-surface event window cannot separate it from a genuine effect without additional assumptions, and show in zero-effect simulations why user fixed effects and coarse activity matching can fail: the confound is within-user and time-varying. We provide a diagnostic protocol, public-data benchmarks, and burstcheck, a lightweight audit tool. User-timed events may have real effects, but post-event volume does not identify them by default; studies should compare similar episodes with and without the event.

---


### 152. [When Adaptation Hurts: Connecting Representational Drift to OOD Failures in MedSAM Fine-Tuning](https://arxiv.org/abs/2608.21300)

**<font color=#1a73e8>作者：</font>** Marko Haralović, Sounic Akkaraju, Carlo Baretta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models for medical image segmentation, like prompt-based MedSAM, generalize well across domains and modalities, often in zero or few-shot setups. However, their performance depends on the quality of prompts and the adaptation of the models to custom datasets. This work systematically examines how MedSAM generalizes across diverse medical imaging benchmarks, with six adaptation strategies: full-model and encoder-only LoRA, shallow and deep visual prompt tuning (VPT), and decoder-only and full fine-tuning. Models are trained on the International Skin Imaging Collaboration Challenge (ISIC 2018) dataset and evaluated under clean and increasingly noisy prompts on IN and Out-of-Distribution (OOD) datasets: close-OOD PH2 (dermoscopy), far-OOD BUSI (Breast Ultrasound Images Dataset) and CBIS-DDSM (Curated Breast Imaging Subset of the Digital Database for Screening Mammography). We show that adaptation improves performance on IN and close-OOD data but often reduces performance on far-OOD data. Full fine-tuning provides the best tradeoff, while encoder-only LoRA is the strongest parameter-efficient alternative, outperforming standard LoRA and VPT under far-OOD shifts. Using Centered Kernel Alignment (CKA), we show that far-OOD degradation is strongly associated with drift in decoder representations, whereas encoder similarity alone does not explain robustness. This suggests encoder-only LoRA provides stronger robustness than standard LoRA by adapting the encoder to distribution shift in visual features, while preserving the decoder pathway. We further show that random 0-100 pixel jitter on prompts produces more robust and better performing models. We thus conclude that robust MedSAM adaptation requires the combined consideration of prompt noise exposure, domain shift, and representation preservation. We release our code: this https URL

---


### 153. [SPARCL: Spectral Partitioned Analytic Continual Learning](https://arxiv.org/abs/2608.21307)

**<font color=#1a73e8>作者：</font>** James Hartley, Zeropy Surio, Daniel Whitmore 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Analytic continual learning has emerged as a strong exemplar-free alternative to gradient-based class-incremental learning because it replaces iterative optimization with closed-form ridge updates. Yet the usual forgetting narrative, centered on stochastic gradient overwriting, does not explain why analytic methods still drift on old classes despite exact recursive solvers. We identify the culprit as spectral interference: the joint ridge classifier for all tasks shares the inverse autocorrelation operator $(R+\lambda I)^{-1}$, so incoming task samples that load onto old dominant eigendirections dilute the spectrum and perturb old-class logits even when old labels are never revisited. Based on this view, we propose SPARCL, a spectral partitioned analytic continual learner that decomposes the running autocorrelation into a high-energy core and a residual complement, freezes old-class classifier components in the core subspace, and updates only the residual block through recursive least squares with an optional residual random-projection expansion. This yields a simple closed-form update with a provable invariance guarantee for the core contribution of old logits. Across CIFAR-100, CUB-200, ImageNet-R, and ImageNet-A under a frozen ViT-B/16 protocol, SPARCL closes most of the gap from classical analytic learners to strong representation matchers, while remaining complementary to sparse feature-decorrelation approaches such as Fly-CL.

---


### 154. [Rethinking Expressivity and Efficiency in Test-Time Training](https://arxiv.org/abs/2608.21308)

**<font color=#1a73e8>作者：</font>** Zeyun Zhong, Joya Chen, Manuel Martin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-Time Training (TTT) enables long-context processing via continuous weight updates during inference, but current methods struggle to balance the expressivity of per-token update dynamics with the hardware efficiency of chunk-wise approximations. We propose E$^2$-TTT (Expressive and Efficient TTT) to bridge this gap. Under the standard approximation of taking gradients at the chunk-start weights, we derive a closed-form state transition that exactly reproduces the chunk-end fast-weight and momentum states of the per-token recurrence. This enables fully parallelized chunk-level training while preserving the temporal structure of the update rule that prior chunk-wise methods discard. We validate E$^2$-TTT by training models up to 1.3B parameters from scratch. It performs on par with previous TTT and hybrid attention baselines in language modeling while outperforming them on in-context retrieval. Its advantage is most pronounced in length extrapolation: on the standard ``Needle in a Haystack'' passkey test, it retains over 90% accuracy at $8\times$ the training context length. Meanwhile, E$^2$-TTT can match the training throughput of efficient chunk-wise methods, demonstrating that it effectively reconciles expressivity with efficiency. The code is available at this https URL.

---


### 155. [Unified Branch-and-Bound Search for the Steiner Traveling Salesman Problem on Graphs of Convex Sets](https://arxiv.org/abs/2608.21319)

**<font color=#1a73e8>作者：</font>** Jingtao Tang, Hang Ma  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We formalize the Steiner Traveling Salesman Problem (Steiner-TSP) on Graphs of Convex Sets (GCS), which seeks a minimum-cost closed trajectory through required convex sets while allowing optional transit vertices and revisits. To explore the resulting infinite solution space, we propose a unified branch-and-bound search over rooted walk prefixes. Additive lower-bound-graph costs bound committed prefixes, while a cut-separated connected-flow relaxation lower-bounds the residual cost of visiting every remaining target and returning to the root. Under a uniform positive-cost assumption, best-first traversal terminates after finitely many expansions on every feasible instance without an initial incumbent, whereas depth-first traversal does so once a finite incumbent is available. For a user-specified factor $\epsilon\geq1$, a global lower bound certifies that either strategy's incumbent cost is at most $\epsilon$ times the global optimum. We further demonstrate joint sensing-mode, visitation-order, and continuous-trajectory selection for a mobile-manipulator inspection task, including action precedences expressed in linear temporal logic over finite traces (LTL$_f$). Both traversal strategies find feasible solutions on all benchmark instances within 30s with mean certified optimality gaps of 28.1% and 29.7%, respectively, whereas two recent baselines succeed on only about half of the instances

---


### 156. [Time-Aware Tranformer-Based Prediction Model for AECOPD](https://arxiv.org/abs/2608.21324)

**<font color=#1a73e8>作者：</font>** Weihao Qu, Ling Zheng, Dongyang Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid symptom change of Acute exacerbation of chronic obstructive pulmonary disease (AECOPD) makes it critical to have time-sensitive prediction models. However, most current machine learning models studying AECOPD use clinical and laboratory data, which will inevitably cause latency. To ensure timely detection of AECOPD and minimize latency, this paper focuses on home monitoring scenarios where only respiratory data from daily-use ventilators is available. We introduce a Time-Aware transformer-based AECOPD prediction model, which generates meaningful patient representations using the Time-Aware transformer to capture the symptoms and their temporal progression in ventilator data. Our experimental results demonstrate that our Time-Aware transformer-based approach outperforms traditional methods in multiple classification tasks, highlighting its potential to enhance AECOPD prediction accuracy.

---


### 157. [Anatomy-Informed Neural Networks: Encoding Anatomic Priors in Loss and Architecture, with an SE(3) Formulation of Guidewire-Induced Aortoiliac Deformation](https://arxiv.org/abs/2608.21332)

**<font color=#1a73e8>作者：</font>** David P. Stonko  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep-learning models of anatomy can be numerically plausible yet anatomically impossible, and they generalize poorly when data are scarce. We introduce Anatomy-Informed Neural Networks (AINN), in which soft anatomic priors enter as penalty terms in the loss (e.g., a branching penalty that treats a renal transplant artery off the iliac instead of the aorta as unexpected rather than impossible), in direct analogy to a physics-informed neural network, and hard anatomic priors (e.g., continuity of the vessel) are built into the architecture and state representation, making such invalid predictions impossible by construction wherever the prior admits architectural enforcement.
We develop it on a clinical test case with limited data: how the aortoiliac tree deforms when a stiff wire is introduced endoluminally. This is important to contemporary aortic surgery and will matter to autonomous endovascular navigation. We lift the vessel centerline and the wire path from R^3 to curves of frames in the Lie group SE(3), and couple a Cosserat-rod wire to a tortuosity-modulated, anatomically anchored vessel through a unilateral lumen-contact inequality. The prediction is a constrained minimizer of the coupled elastic energy, with contact forces as its Lagrange multipliers. Supervision is a Wasserstein-2 optimal-transport loss between the predicted projection through the C-arm geometry and the observed angiogram, so a 2D angiogram can train a 3D prediction. The kinematics, loss and projection are verified against known ground truth; the mechanics solver only against its own optimality conditions, and predicted displacement is not yet mesh-converged. Here, no network is trained. Future work will transfer this in silico model to real CT scans and test whether it improves predictive accuracy and reduces the training data required.

---


### 158. [Across-Design Uncertainty in Short Pricing Panels: Evidence from Simulated Price Trajectories](https://arxiv.org/abs/2608.21334)

**<font color=#1a73e8>作者：</font>** Pedro Cadahia Delgado  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Short observational pricing panels can contain many observations while offering only a small number of distinct price movements. This paper studies the inferential consequences of that distinction in a synthetic data-generating process calibrated to a sparse pricing regime. We separate uncertainty conditional on a realised price trajectory from variation in estimation error across alternative trajectories generated by the same pricing process. In the baseline simulations, the latter component accounts for 97.6% of the variance of estimation error for the gradient-boosted specification. Within-panel resampling procedures use the information of one realised trajectory and do not identify this across-design component.
Three results organise the analysis. First, across-design dispersion is well described by the empirical relation sigma_hat approx 0.182 V^(-0.271), where V equals moves times magnitude squared. Second, adding regions sharing a common price path reduces outcome noise but does not create independent price trajectories; conversely, averaging across units with independent design-specific errors reduces dispersion at the standard square root rate. Third, a Paule-Mandel variance component estimated across independently priced units substantially increases empirical coverage in homogeneous simulations, from 0.469 to 0.931. The broader implication is a shift toward designing data-generating processes that create independent identifying variation rather than relying solely on fixed passive panels.

---


> [!TIP]
> 当前位于：**151-158**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-158**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
