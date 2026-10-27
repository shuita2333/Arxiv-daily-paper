# 📦 其他研究 | 2026年10月28日

> 本类共 **446** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**401-446**（第 9/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-446**

---

### 401. [Balanced Sampling in Stochastic Multi-objective Bandits](https://arxiv.org/abs/2610.35551)

**<font color=#1a73e8>作者：</font>** Mengfan Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In stochastic multi-objective bandits, Pareto optimal arms may represent different trade-offs among objectives. Balanced sampling across them is important in practical settings such as online advertising. Yet, there seems to be little consensus on how to measure fairness, to our best knowledge. Achieving fairness is also tough as the set of Pareto optimal arms is unknown, and early sampling decisions may create imbalances that are difficult to erase afterwards. We measure unfairness by the KL divergence from the uniform distribution over the true Pareto set to the empirical measure induced by the sampling trajectory. Nicely, this measure admits an exact decomposition that separates the cost of sampling suboptimal arms from the imbalance among Pareto optimal arms. With a recursive form for unfairness, we develop \emph{adaptive top-two sampling}, which combines sampling counts and empirical evidence of Pareto membership to define a gain for each arm and guide sampling without committing to an estimated Pareto set. When the Pareto set is stable under small perturbations, we establish an $O(\log T/T)$ and $O(T^{-1})$ bound on expected unfairness and variance, respectively. Information-theoretic lower bounds show that the $\log T/T$ rate can be unavoidable for uniformly fair policies on stable instances, matching our upper bound. More surprisingly, stability is indeed crucial, as the expected unfairness can be $\omega(\log T/T)$ without it. Finally, we create a variant that encourages exploration of undersampled arms to reduce the risk of persistent underallocation. At sufficiently large horizons, it preserves the rate on the expected unfairness while admitting a sharper bound of $O(\log^2 T/T^2)$ on variance. Numerical studies support these findings and suggest practical insights.

---


### 402. [Metric Scale for Insta360 Structure-from-Motion from the Camera's Embedded IMU](https://arxiv.org/abs/2610.35554)

**<font color=#1a73e8>作者：</font>** Davide Cuttini, Diego Di Tommaso, Alessio Antoniacomi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Structure-from-motion (SfM) from the dual-fisheye video of a consumer 360-degree camera recovers geometry only up to a similarity transform; in the pipeline considered here, metric scale is obtained from smartphone ARKit or ARCore poses captured alongside the camera. This paper evaluates a self-contained alternative: the IMU embedded in the Insta360 X5 and X6, recorded at 1 kHz. The sensor is characterised (noise density, camera-IMU synchronisation, accelerometer scale factor, bias stability), the camera-IMU rotation and frame timing are estimated from the data, and the scale is recovered by a linear visual-inertial alignment over the SfM poses of a whole survey. The standard formulation, with gravity and accelerometer bias shared across the survey, overestimates the scale by 3.4% on average; estimating each contiguous segment independently and averaging removes the bias. On nine surveys with a co-mounted LiDAR scanner the inertial scale deviates from the LiDAR by 0.74% in mean absolute error, against 1.94% for the smartphone scale; on printed fiducial markers both agree within the 1% uncertainty of the target. On the reference trajectories of thirty sequences of a public benchmark, brought to scales of 1/40, 1 and 40, the estimator recovers the metric scale with a mean error of -0.07% and a standard deviation of 1.28%. On fifty production surveys where the smartphone is the only reference, the two scales agree to a standard deviation of 2.6%, the inertial scale being 0.9% lower on average; the difference does not depend on window construction, grows with the extent of the smartphone anchor, and cannot be attributed to either reference. An ablation over window construction and a comparison with monocular metric-depth networks complete the study.

---


### 403. [Multi-Fidelity Training Reshapes Uncertainty Decomposition in Atomistic Models](https://arxiv.org/abs/2610.35560)

**<font color=#1a73e8>作者：</font>** Matteo Tolloso, Davide Bacciu, Luigi Bonati  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-fidelity training, which combines abundant low-fidelity data with scarce high-fidelity labels, is increasingly common in atomistic modeling, but its effect on predictive uncertainty remains largely unexplored. We investigate this question using deep ensembles of mean-variance MACE models trained on ANI-1x, contrasting high-fidelity training from scratch with low-fidelity pretraining followed by fine-tuning. We characterize aleatoric, epistemic, and total uncertainty throughout training and under two distribution shifts: unseen molecular systems and higher-energy configurations. We find that pretraining reduces prediction error and improves uncertainty-based ranking across all test sets, but does not yield well-calibrated predictive variances; calibration deteriorates more severely under energy extrapolation. Training-dynamics analysis localizes most of this calibration degradation to high-fidelity optimization, during which the learned aleatoric variance becomes overconfident on held-out data. Moreover, multi-fidelity fine-tuning produces a more effective uncertainty-based acquisition function than high-fidelity training from scratch. These findings show that uncertainty ranking and calibration capture distinct properties and must be assessed separately in multi-fidelity atomistic models, especially under extrapolation.

---


### 404. [High-resolution tactile observation makes hidden racket-control mechanisms learnable](https://arxiv.org/abs/2610.35563)

**<font color=#1a73e8>作者：</font>** Haoyang Tian, Zhengwei Li, Houcheng Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Experts can master fine hand-object manipulation skills, yet limited conscious perception of rapid tactile interactions hinders their ability to articulate the underlying control mechanisms. Badminton racket control requires rapid, fine hand-force coordination, providing a demanding testbed for uncovering these mechanisms. An 864-node tactile-inertial glove with synchronized 100-Hz acquisition recorded over 14,000 strokes from more than 70 participants across five skills. Inspired by sensorimotor control, our mechanics-grounded two-layer framework inferred object-driving and grip-stabilizing control from tactile history, while resolving their spatiotemporal force realization. We found that higher proficiency was associated with selective rather than extensive control: greater skill specificity, anticipatory regulation, focal distal modulation and lower geometric torque cancellation, while spatiotemporal coordination showed a non-monotonic acquire-refine pattern. We translated these mechanisms into personalized guidance targeting force control and force-motion coordination. In a randomized cohort, mechanism-guided learners gained 0.72 expert-rated skill levels versus 0.05 with level-only feedback, making control mechanisms actionable.

---


### 405. [Copying As Defense: Protecting Images from Editing By Eliciting Model Copying](https://arxiv.org/abs/2610.35566)

**<font color=#1a73e8>作者：</font>** Salma Abdel Magid, Sanghyuk Chun, Eric Slyman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image editors built on diffusion transformers (DiTs), such as Flux Kontext, make it possible to turn a single photograph into a convincing manipulated image, including harmful and non-consensual edits. Proactive defenses aim to prevent such manipulations by adding an imperceptible perturbation before an image is shared. Existing defenses for DiT-based in-context editors make the output attend less to the protected reference image. But this leaves the model free to follow the edit instruction using the text and its own generated tokens, often producing a new, weakly grounded image rather than preventing the edit. We find that the opposite strategy is more effective: instead of leading the model to ignore the reference, we encourage it to copy it. Through controlled attention interventions, we show that concentrating target-token attention on the reference image in only a few early blocks is sufficient to collapse the editing behavior, causing the model to reproduce its input, often as a lossy copy, rather than execute the requested transformation. Based on this insight, we introduce Copying-as-Defense (CaD), which maximizes per-token target-to-reference attention mass in early transformer blocks. Since attention rows are normalized, increasing reference attention suppresses the attention allocated to the text and generated canvas. Restricting the objective to early blocks also lets us truncate the backpropagation path, keeping optimization cheap. Across editors and benchmarks, CaD reduces average edit success from 81.4% on unprotected images to 24.0%, a 70.6% relative reduction, and by a further 44.3% relative to DeContext, the strongest baseline (43.0%). CaD is also roughly 1.8-2.0x faster per optimization step than comparable methods.

---


### 406. [ExCal: Optimization-Free Multivariate Time Series Anomaly Detection via Excess Calibration](https://arxiv.org/abs/2610.35568)

**<font color=#1a73e8>作者：</font>** Kadir-Kaan Özer, René Ebeling, Markus Enzweiler  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce ExCal, a normal-only multivariate time series anomaly detector that combines raw state retrieval, a signal/derivative subspace, and robust statistics across temporal scales. Each expert map receives a high normality floor from the training prefix. During scoring, positive excess is retained, attenuated for broadly firing maps, and combined with a small rank term. The method fits reference memories and projections without gradient optimization or anomaly labels. Prevalence and ranks depend on the complete scored sequence, making inference batch and transductive rather than online. On 180 series from 17 TSB-AD-M families, ExCal obtains AUC-PR $0.421\pm0.37$ and VUS-PR $0.452\pm0.37$ over three seeds, ranking second among 24 methods. Holm-adjusted paired tests detect no significant difference from AxonAD or StreamVAE, which are the two leading non-pretrained methods on TSB-AD-M, on either primary metric, while finding significant positive differences against the other 21 baselines. A separate single-run probe over three series measures median model-wrapper time of $0.0662$ s. Ablations associate the largest primary-metric changes with raw retrieval and excess-magnitude preservation. The evaluated score is decomposable by expert, but its diagnostic utility and online suitability remain untested.

---


### 407. [GEAR: Feature-Based Configuration and Code Generation for Agentic Systems](https://arxiv.org/abs/2610.35592)

**<font color=#1a73e8>作者：</font>** Brell Sanwouo, Nada Zine, Paul Temple 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Engineering multi-agent systems (MAS) requires choosing agents, orchestration strategies, communication mechanisms, reasoning approaches, and memory configurations. These choices depend on framework-specific capabilities and abstractions, requiring developers to learn different APIs when exploring alternative implementations. We present GEAR, an open-source tool for configuring MAS and generating framework-specific implementations from a common specification. GEAR uses a feature-based representation to make configuration options and their constraints explicit, enabling users to validate specifications before code generation. Through connectors for ten agentic frameworks, users generate projects from the same specification and can then inspect reports describing framework-specific adaptations. A preliminary assessment of mapping feasibility identifies translation strategies for 271 of 320 evaluated feature-framework pairs (84.69%). GEAR supports developers prototyping agentic systems and researchers exploring MAS configurations across frameworks. GEAR is available as open-source software at this https URL and a video demo is available at this https URL.

---


### 408. [SAP-ViT: A Self-Attributing Patch Vision Transformer for Medical Image Classification](https://arxiv.org/abs/2610.35593)

**<font color=#1a73e8>作者：</font>** Wei Zhang, Wolfgang Nejdl, Ming Tang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision Transformer (ViT) classifiers commonly rely on a global classification (CLS) token for image-level prediction, which is poorly aligned with local interpretability requirements in medical imaging. We propose SAP-ViT, a Self-Attributing Patch Vision Transformer that replaces CLS-based classification with direct aggregation of last-layer patch embeddings. This design makes class predictions decomposable into patch-level contributions as part of the forward pass. To encourage concise and readable evidence, SAP-ViT applies sparsity regularization to the patch-weight distribution. Since self-attention mixes information across patch tokens, we further introduce an input-space back-mapping mechanism to estimate which input patches contribute to influential output patch embeddings. We evaluate SAP-ViT qualitatively and quantitatively on multiple medical image classification datasets spanning different imaging modalities. The results show that SAP-ViT maintains strong classification performance while providing consistent and interpretable patch-level explanations across datasets. Ablation results further show that both sparsity regularization and the alignment component of input-space back-mapping contribute to the final explanation quality. Overall, SAP-ViT provides a favorable trade-off between predictive accuracy and interpretability for ViT-based medical image classification.

---


### 409. [Beyond Distribution Matching: Self-Supervised Representation Forcing for Few-Step Video Generation](https://arxiv.org/abs/2610.35594)

**<font color=#1a73e8>作者：</font>** Junyi Chen, Haiyu Zhang, Zhoujie Fu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-step distillation is essential for deploying modern video diffusion models. Among existing approaches, Distribution Matching Distillation (DMD) has emerged as a highly promising paradigm by achieving strong output-space fidelity without adversarial training, while remaining flexible across various student architectures. We observe, however, that DMD fundamentally relies on an output-space objective, lacking explicit regularization on the model's internal representations. As the distillation step count aggressively shrinks, this output-only supervision becomes insufficient, causing the distilled student to degrade in both fine-grained spatial structures and coherent temporal dynamics. To address this limitation, we introduce Self Flow Forcing (SF$^2$), which incorporates a predictive representation loss into the DMD framework without altering its output objective. By providing the student and an Exponential Moving Average (EMA) teacher with heterogeneous noise levels, we establish an information asymmetry. This formulation forces the student to predict the teacher's internal representations from a more corrupted input, effectively integrating self-supervised representation alignment into distribution matching. Extensive experiments demonstrate that SF$^2$ effectively mitigates temporal flickering and consistently improves both spatial fidelity and motion quality. Furthermore, the proposed mechanism is architecture-agnostic - seamlessly supporting both bidirectional and causal models - and requires no external feature extractors, introducing minimal computational overhead.

---


### 410. [VaLoP: Value Gradient Lookahead and Pullback for Reward-Guided Diffusion](https://arxiv.org/abs/2610.35607)

**<font color=#1a73e8>作者：</font>** Kwanyoung Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reward guidance steers a pretrained diffusion or flow model toward images or actions that a reward model prefers, at sampling time and without retraining the model for each reward. It follows the gradient of a value function, the expected reward given the noisy state. The two common estimates of this gradient, gradients through a one-step denoised estimate and learned value models, are least accurate at high noise, where the coarse structure of the sample is decided. Interestingly, we find that both errors are posterior covariances, which grow with the uncertainty about the clean sample, and hence at higher noise. To reduce them, we evaluate the value at a less noisy state, one sampler step ahead, where this uncertainty is smaller, and pull its gradient back to the current state. This lookahead places both estimators at the two ends of one family and reveals that an intermediate lookahead requires one additional term, a correction through the generator. We therefore propose Value Gradient Lookahead and Pullback (VaLoP), which computes this correction with one vector-Jacobian product, and VaLoP-Fast, which amortizes it with a small head that, for text-to-image models, is trained with a single reward and reused for the others. Across various models, rewards, and benchmark datasets, both robustly outperform existing value-gradient guidance on the target reward, VaLoP-Fast at about the cost of learned-value guidance. Both extend to critic-guided robot policies, where VaLoP-Fast attains the highest success rates on LIBERO and RoboCasa.

---


### 411. [Making Reasoning Visible: Configuration-Aware Diagnostic Modeling for Adaptive Scaffolding in Structured Reasoning Tasks](https://arxiv.org/abs/2610.35609)

**<font color=#1a73e8>作者：</font>** Trystan Geoffre, Zheng Yuan, Thierry Geoffre  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modeling the latent, multi-step reasoning processes of learners is a core challenge for adaptive tutoring systems, which often rely on simple right/wrong answers rather than understanding how students think. Instantiated here for grammatical reasoning, this study introduces a diagnostic framework that makes students' step-by-step problem-solving visible by analyzing their action sequences in an interactive learning game. The framework computes five interpretable strategy dimensions (e.g., systematic error correction, random guessing), estimates coordination demand from task structure and behavioral patterns, and classifies reasoning into four distinct states. Analyzing 36,234 interactions from 234 students working on 42 morphosyntactic exercises, we found that reasoning strategies vary primarily by context rather than stable traits (intraclass correlation = 0.14), and students show high persistence in unproductive states; specifically, 74.6% of failures driven by high coordination demand (rather than simple knowledge gaps) are followed by another failure without intervention. Our early warning model predicts validation success with strong accuracy (AUC = 0.826 using strategy patterns alone; 0.902 with additional sequential context) while avoiding circular reliance on current error counts. These findings demonstrate that making latent reasoning processes visible enables earlier, more targeted scaffolding that responds to how students are thinking rather than simply whether they succeed. While demonstrated in language learning, the framework provides a generalizable, interpretable architecture for diagnosing complex, structured reasoning in any domain.

---


### 412. [Distilling neural networks into equations to predict planetary instability](https://arxiv.org/abs/2610.35617)

**<font color=#1a73e8>作者：</font>** Simon Alford, Edward Gu, Omar Costilla-Reyes 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The problem of predicting when a multi-planet system will become dynamically unstable has defied analytical progress over the past three hundred years. Recent machine learning advances achieve high predictive performance of instability dynamics, but as black-box systems cannot be interpreted to connect to existing scientific understanding. Here we show analytic equations that predict when a multi-planet system will undergo instability. We discover these equations by first training a neural network on a dataset of N-body simulations, and then distilling its latent knowledge into closed-form algebraic expressions. Our two-stage pipeline first learns an interpretable variable basis, then searches for equations using symbolic regression. The resulting equations outperform existing analytic estimates of instability and apply across wide ranges of mass ratios, spacing, and orbital eccentricities. They capture structure in the prediction landscape with a small number of variables amenable to dynamical interpretation. These results demonstrate how symbolic learning can be combined with neural networks to extract scientific insight from complex dynamical systems.

---


### 413. [Synthetic Deformable Tubular Benchmark: A mechanically annotated dataset for evaluating deformable 3D reconstruction](https://arxiv.org/abs/2610.35621)

**<font color=#1a73e8>作者：</font>** Íñigo Cirauqui-Viloria  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Evaluating deformable 3D reconstruction requires ground truth linking camera motion, surface deformation, material correspondence and image appearance. We introduce the Synthetic Deformable Tubular Benchmark, generated with LumenMorph, an open-source toolkit for creating, annotating and evaluating tubular scenes. The release contains 5,580 RGB images. Its baseline crosses three surface-motion conditions with moving and stationary cameras in six scene families; matched appearance variants cover only moving-camera finite-element actions in four families. Documented public and evaluation interfaces expose camera poses, geometry, depth, deformation fields, persistent material correspondences and discrete finite-element records. Persistent triangle identities and material weights let users track the same surface location across frames and query its three-dimensional trajectory. Separately implemented geometric and mechanical checks assess annotation consistency with the generating models. Structure-from-motion, optical-flow and supplied-geometry displacement-interpolation studies demonstrate how the resource distinguishes registration coverage from geometric accuracy, exposes camera- and surface-motion effects, and tests the benefits and mismatch of mechanical priors. Public readers, evaluation contracts and the configurable generator support reuse and extension. Data integrity, fixed-environment repeatability and retained-prediction score replay have distinct verification scopes. The benchmark provides a controlled synthetic reference without claiming anatomical or clinical realism.

---


### 414. [Adapt for Planning, Not just Prediction: Optimistic Test-Time World Model Adaptation](https://arxiv.org/abs/2610.35636)

**<font color=#1a73e8>作者：</font>** Akshay Mete, Dileep Kalathil, P. R. Kumar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent world models are typically pre-trained offline and kept frozen at test time, so planning with them can degrade under distribution shift. Test-time adaptation (TTA) can mitigate this degradation by updating the model during deployment. Unlike pre-training on fixed data, TTA for planning is closed-loop: the planner uses model rollouts to select actions, and the resulting transitions drive the next update. This raises the question: which objective should guide TTA for planning? Under a prediction-only objective, the model is fit only to the outcomes of its own actions, so it can remain wrong about the actions that would reach the goal, and low prediction error need not translate into better planning. Inspired by reward-biased maximum likelihood from adaptive control, we introduce Optimistic Test-Time Adaptation (OpTTA). Its objective has two terms, the prediction loss on observed transitions and the planner's goal-reaching cost on its candidate rollouts, both minimized over the model parameters. The planning term biases adaptation toward models that are optimistic about reaching the goal, without any additional environment interaction. Across visual and environment shifts on manipulation, reaching and navigation tasks, OpTTA raises final planning success over the frozen model by 13.5 percentage points on average, compared with 6.9 for the prediction-only objective (AdaJEPA), when only the predictor is adapted. When the encoder is adapted as well, the gains are 13.5 and 7.5 points. These experiments span three JEPA world models with different encoders and training objectives and, for temporal straightening, both CEM and gradient-based planners. Our results suggest that test-time adaptation of world models for planning benefits from an optimistic, task-aware term in addition to the prediction loss.

---


### 415. [SeeRF: Learning to See Beyond Fields of View via Generative Image Registration and Fusion](https://arxiv.org/abs/2610.35637)

**<font color=#1a73e8>作者：</font>** Xunpeng Yi, Yibing Zhang, Qinglong Yan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Due to the inherent discrepancies in imaging viewpoints and field-of-view mismatches among multi-modal sensors, existing fusion methods have long struggled to achieve complete scene-level information integration beyond the limitation in sensor fields of view. Consequently, the generated fusion results often contain modality-specific regions and fusion artifacts, limiting the comprehensive representation of scene structures and semantic information. To address this challenge, we propose a generative registration-fusion framework, termed SeeRF. Specifically, it first introduces a deformation generation strategy based on the diffeomorphic stationary velocity field, combined with visual foundation model-guided feature extraction and a coarse-to-fine progressive multi-modal image registration module, to achieve accurate cross-modal flow estimation and generate valid field-of-view masks. Subsequently, the registration module is tightly coupled with the generative diffusion module for multi-modal completion and fusion, where the cross-modal control encoding module and the control residual feature encoder-decoder mechanism provide effective guidance. By leveraging the powerful prior modeling capability of generative diffusion models, the proposed framework overcomes the limitations imposed by shared fields of view and enables effective completion and natural fusion of non-overlapping field-of-view regions. Extensive experiments on multiple public datasets and real-world scenarios demonstrate that the proposed method achieves superior performance, validating its effectiveness, superiority, and robustness. The code will be available at this https URL.

---


### 416. [Proofs of strong forms of the Bovdi--Geche universality conjecture and a complex analogue](https://arxiv.org/abs/2610.35645)

**<font color=#1a73e8>作者：</font>** Victor Bovdi, Ambrus Pal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We prove two universality theorems for neural networks consisting of a single neuron. First we prove a strong form of the Bovdi--Geche universality conjecture on neurons over finite fields, where the activation function is a certain modification of the discrete logarithm, using the Weil bound on multiplicative character sums over finite fields. Then we show a generalisation of Aizenberg's universality theorem for complex binary neurons with a weight vector independent of the target function, positively answering another question in the literature. The proof of the latter uses an equidistribution theorem for the dilates of certain maps into tori.

---


### 417. [Active Learning of Conditional Generative Models via the Transport Neural Tangent Kernel](https://arxiv.org/abs/2610.35652)

**<font color=#1a73e8>作者：</font>** Jayoung Ryu, Kyunghyun Cho, Romain Lopez  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many high-throughput scientific experiments produce distributional outputs, requiring conditional generative models to interpret the data, and to predict outcomes at new inputs. Acquiring experimental data at new conditions (e.g., for a new antigen or a new cell type) is often expensive, motivating the need for automated experimental design methods. However, existing active learning frameworks are limited as they assume scalar or vector-valued outputs. We first show that the Wasserstein test risk of a conditional generative task decomposes into a mean term and a shape term, demonstrating why mean-based active learning is blind to distributional shape. To capture both, we propose the transport Neural Tangent Kernel (tNTK), a tractable kernel that measures how sensitive a generative model's predicted distribution is with respect to its parameters. The tNTK recovers the standard NTK in the deterministic limit and upper-bounds the posterior Fréchet variance of the prediction under small parameter perturbations. It admits a closed-form expression for affine Gaussian transport and tractable Monte Carlo estimators otherwise. Treating the tNTK as the covariance function of a Gaussian process, we greedily select inputs that minimize the total GP posterior variance across the pool, yielding a distribution-aware active learning strategy. We evaluate this strategy across four classes of conditional generative models, including conditional flow matching and conditional Monge gap, on synthetic distributions, intent-labeled sentences, and single-cell perturbation responses. In these experiments, the tNTK outperforms the baseline NTK computed from the conditional mean, demonstrating the value of distribution-aware active learning for generative-modeling tasks.

---


### 418. [SCAFFOLD under Hessian Similarity: Sharp Convergence Rates](https://arxiv.org/abs/2610.35663)

**<font color=#1a73e8>作者：</font>** Zhirayr Tovmasyan, Slavomír Hanzely, Egor Shulgin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> One of the main challenges of federated learning is heterogeneous data split among the clients, leading to biased local updates called client drift. The SCAFFOLD algorithm (Karimireddy et al., 2020) corrects client drift with control variates, but its relation to the similarity of client data is not yet fully understood: the original similarity-based guarantees cover only quadratics with a stronger second-order similarity assumption, and a follow-up weakly convex analysis (Luo et al., 2025) obtains a $\sqrt{L\delta}$ dependence for $L$-smooth losses with averaged Hessian similarity $\delta$. We analyze SCAFFOLD with minibatch-based control variates and establish linear dependence on Hessian similarity beyond quadratics, for both convex and nonconvex objectives. In particular, for convex objectives with exact gradients, $R$ SCAFFOLD rounds with $K$ local steps lead to an objective gap of order $(L/K+\delta)D_0^2/R$, where $D_0$ is the initial distance to a minimizer. When $K=\Theta(L/\delta)$, it improves the minibatch SGD rate by a factor $\Theta(L/\delta)$. For nonconvex objectives, we prove an analogous stationarity guarantee under uniform Hessian similarity for a client-selection variant. In both settings, we extend these guarantees to stochastic gradients and prove matching lower bounds for the analyzed methods with constant local stepsizes. We also show that, under partial participation, even identical clients need not obtain the full communication benefit of additional local steps.

---


### 419. [CounterFlow: Target-Conditioned Flow Matching for Visual Counterfactuals](https://arxiv.org/abs/2610.35679)

**<font color=#1a73e8>作者：</font>** Paul Sevellec, Elisa Fromont, Romaric Gaudel 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In eXplainable AI, counterfactual explanations have gained significant traction by offering users direct, intuitive, and actionable insights into model decisions. We introduce CounterFlow, a novel framework based on Conditional Flow Matching that generates visual counterfactual explanations by directly steering a source image toward a user-specified target class. By leveraging target-conditioned vector fields, CounterFlow identifies highly realistic semantic modifications while requiring substantially lower computational overhead than traditional GAN- or diffusion-based architectures. Empirical evaluations on standard benchmarks demonstrate that CounterFlow achieves state-of-the-art performance in both visual realism and target class switching. By working directly in the raw pixel space, CounterFlow offers a more practical solution for real-world deployment.

---


### 420. [Printed and Scanned: Exposing the Fragility of Single-Image Morphing Attack Detectors under Print-Scan Degradation](https://arxiv.org/abs/2610.35682)

**<font color=#1a73e8>作者：</font>** Diogo J. Paulo, Hugo Proença, João C. Neves  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face morphing attacks, in which the biometric traits of two or more identities are blended into a single face image, pose a severe threat to identity document issuance and automated border control. Consequently, a large body of work has proposed Single-image Morphing Attack Detection (S-MAD) algorithms and benchmarked them on datasets such as SYN-MAD22. However, the majority of these benchmarks operate exclusively in the digital domain, which contrasts with the real-world passport issuance pipeline in some countries, which still requires an applicant-supplied photograph to be printed and subsequently re-scanned before it is embedded in the identity document or fed into an automated verification system. This print-scan step introduces halftoning, resampling, color-space, and sensor noise that are absent from digital pipelines, and may mask the high-frequency artifacts that S-MAD models rely on. In this work, we introduce a print-scan version of the SYN-MAD22 dataset, obtained by printing and re-scanning all bona fide and morphed images at 300 and 600 DPI, and we use it to evaluate eight state-of-the-art S-MAD models trained exclusively on digital data. We additionally repeat the acquisition with a second scanner to assess cross-device robustness. Our results show that detectors that achieve near state-of-the-art performance in the digital domain suffer a more than threefold increase in average equal error rate, with the same qualitative degradation observed across both scanning devices, exposing a critical, previously under-reported gap between digital-benchmark performance and robustness to print-scan degradation.

---


### 421. [OmniShowcase: Omnidirectional Subject-Consistent Video Generation from Multi-View Images](https://arxiv.org/abs/2610.35684)

**<font color=#1a73e8>作者：</font>** Junyeong Ahn, Geonwoo Kim, Kinam Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating videos of a specific subject from a few reference images remains challenging when the camera reveals surfaces that are not visible in the input. Early subject-to-video (S2V) methods condition on a single reference image and must therefore infer the subject's unseen appearance and geometry as the viewpoint changes. To address this limitation, recent methods extend S2V to multiple reference views, providing more information about the subject from different viewpoints. However, they do not explicitly specify the 3D structure that connects these observations. In addition, existing training data do not guarantee that viewpoint changes preserve the same underlying 3D subject. We present OmniShowcase, built on two components: (i) a fully automated data synthesis pipeline that produces training videos along diverse camera trajectories, with viewpoint variation driven by underlying subject geometry, even spanning full 360-degree orbits; and (ii) a geometry-conditioning method that provides the video model with a turntable of surface-normal maps reconstructed from the reference views without requiring temporal alignment with the generated frames. We construct Showcase-4K, a corpus of 3D-asset-based videos covering twelve camera motions across 88 trajectory configurations with reconstruction-derived surface-normal conditioning, and ShowcaseBench, a held-out evaluation set with the source meshes and camera parameters used to render each video. Experiments show state-of-the-art subject identity and 3D consistency while maintaining competitive video quality and motion. Project page: this http URL

---


### 422. [GNN-VIEW: Visual Inspection and Explanation of Graph-based Earth-System Models](https://arxiv.org/abs/2610.35693)

**<font color=#1a73e8>作者：</font>** Alessandro Lucatelli, Ferdinand Unterhuber, Katharina Krenzer 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning Earth-system models are becoming increasingly important, and so is their development. Graph-based models, one of the most prominent approaches, allow developers to constrain the learning process before training via graph connectivity. Yet, developing these models remains challenging: the graph is built algorithmically with little intuition about the final result beyond static plotting, which requires extra work and is often not detailed enough. Even after successful training, how the model arrives at forecasts remains obscure. We present GNN-VIEW, an interactive browser-based tool that supports the development of such systems. GNN-VIEW exposes the graph's information pathways, allowing model developers to debug the graph structure before training. After training, GNN-VIEW uses attribution-based explainability to reveal which input features are used by the trained model for a given forecast. This helps developers understand why a model fails. We showcase the usefulness of GNN-VIEW in the construction stage of a graph for an ocean forecasting model, and in explaining poorly predicted precipitation of a trained weather forecasting model during Hurricane Laura.

---


### 423. [Triage: Skip, Skim, or Refine Attention Tiles in Video Diffusion Transformers](https://arxiv.org/abs/2610.35706)

**<font color=#1a73e8>作者：</font>** Yeonjae Kim, Omin Kwon, Seong Hoon Seo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attention over tens of thousands of visual tokens dominates the inference of video diffusion transformers (DiTs). Existing methods reduce this cost through sparsity, low precision, or both, but use a single precision for all kept tiles. We observe that the output error introduced by approximation varies widely across tiles. Many tiles can be skipped with little error, others must be computed but gain little beyond low precision, and a few retain substantial error even at low precision. We present Triage, a training-free attention method that assigns each tile one of three approximation tiers: skipping it by replacing it with its block means, skimming it in NVFP4, or refining it with NVFP4 residual correction. A lightweight router predicts each tile's error under each tier from block statistics and moves a tile to a more accurate tier only when the predicted error reduction justifies the extra compute, with a single price setting this trade-off. A fused kernel executes all three tiers in a single pass on the FP4 tensor cores of RTX Blackwell GPUs. Across Wan2.2, HunyuanVideo, and LTX-2.5, Triage accelerates end-to-end generation by up to 2.32x over dense FlashAttention, and in each of five settings it runs faster than every baseline while reaching 0.3-3.0 dB higher PSNR than the highest-PSNR baseline.

---


### 424. [Detecting bus delays and service anomalies in Niterói with autoencoder latent feature representations](https://arxiv.org/abs/2610.35710)

**<font color=#1a73e8>作者：</font>** Matheus Germano, Claudio E. C. Campelo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bus riders judge service by two failures: single trips that run late, and days on which the whole system misbehaves. We ask whether one unsupervised representation of raw GPS telemetry can serve both diagnoses on the NetMob 2026 Niterói bus dataset. An autoencoder compresses each trip into a 64-dimensional latent vector; the frozen encoder feeds supervised delay classifiers, and the reconstruction error serves as an anomaly score. Two findings are negative. First, the latent representation does not improve delay detection: gradient boosting on per-trip summary features reaches $0.846 \pm 0.013$ ROC-AUC against $0.838 \pm 0.016$ for the best latent setup, and the gap becomes significant once the preprocessing filters are relaxed. Second, two of the three external checks of the anomaly score were circular. Retraining without rainfall removes the rain association ($5.4\%$ against $5.0\%$ flagged, $p = 0.84$) and an apparent citywide disruption on 23 March. What survives is a day-level signal stable across three autoencoders (Spearman $\rho \geq 0.96$), driven mostly by day type, with degraded-telemetry days still separable within weekday and weekend strata. The alarm threshold limits detection more than the score does: a pooled percentile cut flags $5.7\%$ of trips on the worst degraded day, while re-scaling within each bus line flags $29.3\%$. The delay model rests almost entirely on one feature, no latent dimension is individually interpretable, and 22 chronic line-directions carry half of all delayed trips.

---


### 425. [Quantifying the failure of symmetry learning in linear diffusion models due to initialization and finite-sample effects](https://arxiv.org/abs/2610.35720)

**<font color=#1a73e8>作者：</font>** John J. Vastola, Kanaka Rajan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data distributions often possess one or more symmetries: for example, all orientations of any specific dog are included in the distribution of all possible dog pictures. Despite the omnipresence of such symmetries, modern generative modeling approaches may fail to incorporate or learn them, which can lead to lower sample efficiency and poorer generalization. To what extent do diffusion models fail to learn data distribution symmetries, and what sources of symmetry breaking are most responsible? Here, we answer this question in the theoretically tractable setting of linear diffusion models. We show that of three potential sources of symmetry breaking---a non-symmetric initial weight matrix, a noisy learning target, and finite-sample noise---target noise produces the most robust symmetry breaking, since it persists even in the sample-rich regime. Using local laws from random matrix theory, we derive formulas for average symmetry error in fairly general cases involving symmetry within a subspace and show that smaller symmetries are harder to learn.

---


### 426. [MatAnyone-E: Sparse Memory Propagation for Efficient High-Resolution Video Matting](https://arxiv.org/abs/2610.35724)

**<font color=#1a73e8>作者：</font>** Shuyun Wang, Shangchen Zhou, Peiqing Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution video matting requires preserving fine details, such as hair strands and soft transparency, while maintaining consistency across frames. Memory-based methods achieve strong matting quality by matching current-frame features with information stored from earlier frames, but this process becomes increasingly costly as resolution grows. We present MatAnyone-E, an efficient extension of MatAnyone 2 that focuses computation where it is most needed. Our approach first performs low-resolution propagation to identify uncertain regions that require closer inspection and the memory candidates most relevant to them. It then performs high-resolution matching only for these regions using the selected memory, while reusing low-resolution matching results elsewhere. This strategy reduces both the number of locations requiring detailed matching and the amount of memory searched, while preserving the information needed to produce a complete matte. We further reduce the cost of generating high-resolution mattes with a lightweight decoder designed around measured runtime bottlenecks and trained to reproduce the original decoder's representations. Experiments show that MatAnyone-E maintains matting quality comparable to MatAnyone 2 while achieving an estimated 7.4x inference speedup and reducing peak GPU memory usage to 7.6% of the usage of MatAnyone 2 at 4K. With compilation-enabled inference on a single NVIDIA H200 GPU, it reaches 73.07 FPS at 1080p and 28.62 FPS at 4K.

---


### 427. [TRACE: Memory-Efficient Time Series Class-Incremental Learning via Temporal-Spectral Reconstruction](https://arxiv.org/abs/2610.35727)

**<font color=#1a73e8>作者：</font>** Junhui Mao, Junru Zhang, Liming Ye 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Web-connected sensing applications continuously generate multivariate time series with evolving behavioral categories, making Time Series Class-Incremental Learning (TSCIL) essential for adapting to new classes without forgetting previously acquired knowledge. However, preserving diverse and evolving class distributions under strict privacy and memory constraints remains a fundamental challenge. Existing approaches often face a trade-off between retaining sufficient historical knowledge for accurate recognition and minimizing the memory required for continual adaptation. To address these limitations, we propose TRACE, a memory-efficient, replay-free framework that preserves class-specific knowledge through generative modeling rather than sample rehearsal. TRACE employs a compact, frozen temporal-spectral representation and lightweight class-specific autoencoders to capture complex intra-class variations. By independently preserving each class model, TRACE avoids recursive generation and catastrophic forgetting, while enabling direct classification through reconstruction-based scoring without retaining historical samples or large statistical matrices. Extensive experiments across five TSCIL benchmarks demonstrate that TRACE achieves competitive classification accuracy while reducing mean retained memory by approximately 98.26% compared with TS-ACL, the strongest evaluated analytical baseline, and achieving an approximately 33.43% relative improvement in accuracy on GrabMyo.

---


### 428. [A Category-Selective Encryption Framework for Privacy Protection of UAV Images](https://arxiv.org/abs/2610.35729)

**<font color=#1a73e8>作者：</font>** Ting Yan, Minghui Shang, Haolang Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Imagery captured by unmanned aerial vehicle (UAV) systems increasingly raises privacy concerns, as UAV aerial surveillance routinely captures sensitive objects such as pedestrians and vehicles alongside ordinary scene content. Existing privacy-preserving approaches typically employ class-agnostic saliency detection to indiscriminately obfuscate all visually salient regions, leading to unnecessary information loss and hindering downstream scene analysis. This paper proposes a category-selective encryption framework for privacy-preserving UAV surveillance. The core advance over prior class-agnostic approaches is semantic-level selectivity: the system first recognizes what is present in the scene via an 80-class detector, then encrypts only user-specified sensitive categories while leaving non-sensitive objects and background intact for downstream analytics. The framework supports two complementary encryption schemes: Thumbnail-Preserving Encryption (TPE), which applies adaptive pixelation with a learnable blend parameter and recovers content through a jointly trained Enhanced U-Net, and XOR stream cipher encryption, which offers parameter-free, mathematically exact reversibility. The architectural design, composite loss formulation, and joint training methodology are presented in detail, establishing a foundation for practical privacy-preserving UAV surveillance that balances protection strength and scene utility.

---


### 429. [Preference-Guided Cooperation in Multi-Objective Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2610.35736)

**<font color=#1a73e8>作者：</font>** Qiyue Xia, J. Michael Herrmann  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-objective multi-agent reinforcement learning (MOMARL) addresses agent coordination and objective trade-offs simultaneously while optimising overall system performance. Existing work tends to treat multi-agent cooperation and multi-objective optimisation as largely independent components of a learning problem, which amounts to an exorbitant complexity except in trivial cases. We study here whether the structure provided by multiple objectives can itself be exploited to facilitate cooperation, rather than being treated as an additional optimisation challenge. We formulate MOMARL at both the team and individual levels and introduce objective-wise counterfactual credit assignment to evaluate each agent's contribution across the team objectives. We propose Meta-Gradient Informed Multi-Objective Multi-Agent Reinforcement Learning (MIRL), with static (MIRL-S) and dynamic (MIRL-D) variants. By incorporating meta-gradient information, MIRL enables agents to learn how to prioritise objectives individually while collectively optimising the system-level objective, allowing the multi-objective structure to directly guide cooperation. Experiments on a multi-objective multiple particle environment show that our methods improve Pareto-front quality over baselines, with the dynamic variant achieving the strongest performance.

---


### 430. [LUCID: Local Understanding of Covariate Importance with Conditional Density Estimation](https://arxiv.org/abs/2610.35740)

**<font color=#1a73e8>作者：</font>** Yixiao Wang, Srikar Katta, Jon Donnelly 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Computing local-level variable importance (VI) is critical for understanding machine learning models. Local permutation-based VI metrics offer a simple yet powerful approach, measuring how much a model's output changes when perturbing its inputs. However, existing perturbation strategies often ignore feature dependence or account for it only through restricted approximations. Perturbing a feature without fully respecting this dependence can generate unrealistic counterfactuals, thereby evaluating the model in regions unsupported by the observed data distribution. We address this gap by introducing a new model-agnostic local VI metric and estimator, Local Understanding of Covariate Importance with conditional Density estimation (LUCID). LUCID perturbs features of interest using plausible values drawn from the full conditional distribution given the remaining observed features. We establish theoretical connections between LUCID and existing VI measures, and provide an estimator with convergence guarantees and uncertainty quantification. Finally, we demonstrate LUCID's stable performance and practical utility across simulated and real-world examples.

---


### 431. [CLOSURE: Cross-Channel Closure for Multivariate Time Series Anomaly Detection](https://arxiv.org/abs/2610.35753)

**<font color=#1a73e8>作者：</font>** Fan Xu, Hao Wu, Zhi Song 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multivariate time series produced by industrial installations and server clusters are under continuous monitoring, and anomaly detection is the first line of defense before a local fault escalates into a system-wide failure. In the absence of labels, the dominant paradigm trains a reconstruction model on normal data and scores the residual to reach a verdict. Recent work has steadily enriched the expressiveness of the recovery map through Transformers, diffusion models, and cross-scale associations. A residual, however, only certifies that an observation can be recovered; it does not certify that the variables still explain one another as they do under normal operation. A coordinated yet unfamiliar operating transition inflates the residual without breaking any relationship, whereas a sensor drifting away from its peers may leave the residual silent. Methods that fold inter-variable dependencies into the reconstruction objective inherit this ambiguity, because their relational evidence is ultimately supervised by the same recovery loss. We therefore propose CLOSURE, which evaluates recoverability and cross-channel consistency as two normal-data prediction tasks learned in separation. The recoverability task is solved by a diffusion reconstructor conditioned on a discrete memory of normal temporal bases. The consistency task is solved by a relation-closure operator that predicts every channel exclusively from the others, where the target's own trajectory is withheld and sparse signed gates decide which peers are actually used. The two scores are reconciled only through calibration on normal data. Extensive experiments show that CLOSURE consistently outperforms recent reconstruction-, frequency-, and topology-based detectors on public benchmark streams, confirming the value of examining consistency alongside recoverability.

---


### 432. [VidEdit3D: Flexible 3D Gaussian Editing with Video Diffusion](https://arxiv.org/abs/2610.35756)

**<font color=#1a73e8>作者：</font>** Yanming Yang, Chenxi Song, Tong Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements in text-guided 3D editing, particularly with 3D Gaussian Splatting (3DGS), have shown promise but still lag behind the flexibility of 2D editing tools. Existing methods face a critical trade-off between preserving multi-view consistency and allowing structural modifications. Image-based editors can also struggle to apply the intended edit to objects viewed from unusual angles. To address these limitations, we introduce VidEdit3D, a framework that reformulates 3D scene editing as a trajectory-based video editing task. By drawing a parallel between camera movement in static 3D scenes and temporal dynamics in video, we leverage the robust spatiotemporal priors of pre-trained Video Diffusion Models (VDMs) to encourage semantic and structural coherence across views. Specifically, we propose Trajectory-Guided Rendering (TGR) to select informative keyframes and construct smooth video clips aligned with VDM input requirements. To propagate edits from an anchor view to these clips, we develop Flow-Aligned Video Editing (FAVE), a training-free framework incorporating an Editing Consistency Guidance (ECG) mechanism. ECG contrasts source and edited image conditions at a shared latent state, using scheduled source-image amplification to strengthen adherence to the edited reference while maintaining original scene context. Finally, we introduce Region-Selective 3DGS Refinement (RS-GS) to strictly confine geometric and appearance updates to target primitives, reducing background attribute leakage. Experiments demonstrate stronger instruction alignment and better multi-view consistency than the baselines.

---


### 433. [EEGaze: Multimodal Attention Prediction in Visual Search via EEG-Based Saliency Refinement](https://arxiv.org/abs/2610.35757)

**<font color=#1a73e8>作者：</font>** Mansi Sharma, Dinar Orazgaliyev, Antonio Krüger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Visual search is ubiquitous in daily life, from locating keys in a messy apartment to finding a tool in a cluttered workshop or an application icon on a desktop screen. While visual attention is to a large extent driven by image content, research in psychology indicates that user cognitive states have a significant influence on attention allocation. A promising way to access information about cognitive states is via Electroencephalography (EEG) recordings. Despite this potential, previous works in computational attention modeling have largely disregarded EEG, and related studies in psychology operate with abstract, simplistic stimuli, or even artificially guided search procedures. We bridge this gap with two contributions. First, we present EEGaze 140, the largest publicly available multimodal dataset of free visual search with realistic stimuli. The dataset contains synchronized EEG and eye tracking recordings from 36 participants across 140 naturalistic scenes, covering two scenarios: searching for desktop icons and finding tools in cluttered workshop scenes. Second, we introduce EEGazeNet, the first method for human attention prediction in visual search that integrates EEG signals. Our approach consists of a EEG guided refinement stage that adapts the output of a state of the art saliency prediction method to the user current cognitive state. In comprehensive evaluations on EEGaze 140, we show that EEGazeNet consistently outperforms all baselines and ablation conditions.

---


### 434. [Beyond Physical Illness: Can Clinical Narratives Reveal Emerging Mental Health Risks in Chronically Ill Patients?](https://arxiv.org/abs/2610.35761)

**<font color=#1a73e8>作者：</font>** Sudeshna Jana, Siddhartha Laha, Manjira Sinha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mental-health risks such as depression, dementia, and suicidal ideation can emerge during hospitalization among chronically ill patients and may worsen without timely recognition and intervention. However, most existing mental health studies focus on patients with established psychiatric conditions rather than patients hospitalized primarily for physical illness. In this work, we investigate whether latent mental-health risk in chronically ill patients can be inferred from longitudinal clinical narratives. We construct a weakly supervised cohort around 4,000 patients from MIMIC-III using mental-health evidence extracted from discharge summaries. A hierarchical state-space framework derives mental-health representations from day-wise clinical narratives and models their temporal evolution for risk estimation throughout hospitalization. Preliminary results demonstrate improved binary risk prediction using the proposed representations and show distinct model derived risk trajectories between risk and no-risk cohorts, providing a foundation for studying emerging mental-health risks in chronically ill patients.

---


### 435. [The Evolution and 'Chineseness' of Urban Screens in China: From Propaganda Posters to Smart City Interfaces](https://arxiv.org/abs/2610.35762)

**<font color=#1a73e8>作者：</font>** Wuwu Ran  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Urban screens have become a global feature of the media city, yet their developmental paths are not universal. This paper argues that the evolution of urban screens in China constitutes a distinct paradigm of media urbanism, termed Chineseness, understood here not as cultural essence but as a relational, historically situated configuration of three linked elements: deep-rooted lineages of public communication; state-steered technological leapfrogging driven by industrial policy and mega-events; and a regulatory paradox that enables spectacular scale while tightening operational control. Drawing on a five-stage genealogy (1990-present), a chronology of representative screens, and five paradigmatic cases, the study shows how this configuration produces temporal-spatial compression, the coexistence of multiple technological generations, and privileges collective witnessing over device-centric interactivity. The paper contributes a documented genealogy of Chinese urban screens, develops temporal-spatial compression and collective witnessing as analytical tools for non-Western media ecologies, and positions Chineseness as a globally relevant alternative to market-led models of media architecture.

---


### 436. [Improving Signals, Declining Encoder: A Known-Answer Test of Label-Free Monitoring in Self-Supervised Learning](https://arxiv.org/abs/2610.35766)

**<font color=#1a73e8>作者：</font>** Nilotpal Kakati  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-supervised training is monitored without labels, through the loss and statistics of the learned features. We report a case where we know the encoders lost part of what they had learned, so we can check whether these signals noticed. We trained LeJEPA encoders on synthetic images with known generating factors. In nine of ten seeds, the readability of those factors fell abruptly and stayed down, nearly always along the same direction in factor space. Meanwhile the loss kept falling, and most of the eleven label-free signals we tracked kept improving and rated the declining runs better than runs that did not decline. Standard change-point detection rarely flagged the decline near its onset, and selecting checkpoints by these signals mostly chose ones after it.

---


### 437. [Atomic Security Concerns: Towards a Foundational Language for Security Knowledge Representation](https://arxiv.org/abs/2610.35782)

**<font color=#1a73e8>作者：</font>** Hanane Houmani  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cybersecurity governance, risk management, compliance, and security architecture rely on numerous concepts, including security properties, domains, controls, risks, implementation measures, capabilities, and compliance requirements. Although these concepts are widely used, they are often represented through heterogeneous abstractions and vocabularies, making relationships among them difficult to express consistently and leaving much of the associated reasoning dependent on expert knowledge. This paper introduces the concepts of Security Concerns and Atomic Security Concerns (ASCs) and explores the hypothesis that cybersecurity knowledge may be represented through a finite set of foundational concerns. Inspired by the role of atoms in chemistry, the proposed approach views cybersecurity concepts as compositions of more fundamental concerns rather than as independent abstractions. Hence, Atomic Security Concerns could be viewed as a common abstraction layer for the representation of cybersecurity concepts, independently of their domain, nature, or level of granularity. Building upon this perspective, the paper explores how Atomic Security Concerns may provide the vocabulary of a cybersecurity language and how cybersecurity concepts may be represented as concern sets supporting explicit relationships among concepts. The contribution of this work is intentionally conceptual: it introduces a framework and research hypothesis for investigating the foundations of a common language for cybersecurity knowledge representation, reasoning, and future formalization.

---


### 438. [A theory of noisy linear recurrent neural network learning dynamics](https://arxiv.org/abs/2610.35785)

**<font color=#1a73e8>作者：</font>** John J. Vastola, Kanaka Rajan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Biological neural networks are noisy: their dynamics involve difficult-to-predict fluctuations which are likely due not just to chaos, but also to a variety of low-level biophysical processes. Despite the omnipresence of intrinsic noise, its theoretical consequences are incompletely understood, especially in the context of learning. For example, does noise meaningfully shape representation learning, or is it better viewed as a nuisance factor whose presence or absence changes little about what solution is found and when? Here, we argue that intrinsic noise can significantly modulate representation learning in recurrent neural networks (RNNs), since it can strongly break solution-space degeneracies and in some cases control whether a non-degenerate solution exists at all. We show that this is true for an analytically tractable model of noisy RNN learning with a linear activation function and white noise inputs. We find that, in the so-called rich regime (where weights are initialized with small values), noise strongly modulates the directions in which the read-in, readout, and recurrent weights align. Moreover, we find that noise produces a kind of phase transition: for sufficiently high noise, a non-degenerate solution is not even optimal if parameter scales are limited (e.g., via regularization). These results extend recent analytic work on RNN representation learning and show that noise can act as a fundamental determinant of representations.

---


### 439. [Game theory of academic effort and hiring in the age of AI](https://arxiv.org/abs/2610.35802)

**<font color=#1a73e8>作者：</font>** Saptarshi Pal, Peter S. Park  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many academic disciplines (in particular, mathematics and the theoretical sciences) face difficult questions about how to adapt their practices to the rise of highly capable artificial intelligence (AI). Before AI, a well-written research paper with a strong theoretical result acted as a reliable signal that its authors understood their field in depth. Now that AI is widely accessible, such signals have become cheaper to produce. As a result, they no longer reliably sort academics by their level of understanding. This has direct consequences for academic hiring. The age of AI raises a question for each side of the academic job market. Should an early-career researcher invest in a deep understanding of their field, or instead use AI to build a longer resume with many papers? Should a recruiter favor applicants with fewer papers who pass an interview aimed at probing understanding, or insist on both publication volume and a pass? In this paper, we develop a game-theoretic model of this two-sided dilemma. We classify all pure-strategy equilibria that can arise in this game and use learning simulations to identify the behaviors that populations of applicants and recruiters may learn to adopt. Our analysis provides a framework for reasoning about how academic hiring can adapt to AI and for evaluating practices that preserve the value of deep understanding.

---


### 440. [Does VGGT Know What It Does Not Know?](https://arxiv.org/abs/2610.35806)

**<font color=#1a73e8>作者：</font>** Adityan Thirumani Srinivasan, David Nordström  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D reconstruction models such as VGGT regress cameras and geometry in a single forward pass, but they report no uncertainty for the camera poses they predict: an incorrect relative pose looks no different from a correct one. We ask whether the frozen model nonetheless knows when its pose is wrong. On HardMatch, a benchmark of 1,000 deliberately difficult image pairs on which VGGT fails on 35% of pairs, a linear probe on VGGT's frozen features predicts pose failure on held-out categories with ROC-AUC 93.5%, compared with 79.7% for VGGT's own point-map confidence and 77.7% for a classifier trained on all of VGGT's outputs. The probe catches failures VGGT is confident about, lets a downstream system abstain on the pairs it distrusts, and transfers without retraining to rotation failures on PhotoTourism and ScanNet-1500, beyond what co-visibility explains. This knowledge is absent from the per-image encoder: it is computed partway through the layers that fuse the two views, and the same holds for a second model, $\pi^3$. In essence, we find that VGGT knows more about its own failures than it reports.

---


### 441. [Seeing Through Distractions: Context-Stable Attribution via the Least Core](https://arxiv.org/abs/2610.35827)

**<font color=#1a73e8>作者：</font>** Sai Ganesh Nagarajan, Toshinori Yamauchi, Hiroshi Kera  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Shapley-value-based explanations are widely used for feature attribution in machine learning. However, in computer vision, a feature may reduce the target-class score when added to the complete genuine image, even when the predicted label remains unchanged. We formalize such features as contextual distractors and investigate their attributions under semivalues and the least core. Under a weak average marginal monotonicity assumption, we derive quantitative semivalue--least-core gap bounds and sufficient conditions based on the probability of sampling smaller contexts. We further show that shifting semivalue weights toward larger contexts decreases the signed gap. Finally, controlled image-classification experiments and evaluations on Salient ImageNet provide strong empirical support for our theoretical findings.

---


### 442. [I-HITL: Inalienable Human-in-the-Loop](https://arxiv.org/abs/2610.35835)

**<font color=#1a73e8>作者：</font>** Samuel Breckenridge, Dani Vilardell, Wenhao Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Human oversight is a pillar of AI safety. It is often exercised by a human in the loop (HITL) who approves critical actions taken by an AI agent. AI agents' increasing ability to bypass guardrails, though, raises the question of how to enforce HITL robustly.
We introduce the concept of inalienable human-in-the-loop (I-HITL). An I-HITL protocol ensures that an agent can initiate an action only with explicit human approval, even when the human interacts with a system (e.g., a local agentic harness) compromised by the agent. A strong I-HITL protocol additionally ensures such approval even when an adversarial human attempts to delegate approvals to an agent.
To motivate I-HITL, we report on experiments with a popular agentic wallet platform in which raising an agent's spending cap requires HITL approval via emailed one-time passcodes (OTPs). Given access to the user's email and a task blocked by the cap, we find that ten different frontier models will often autonomously raise the cap, harvesting OTPs to bypass a HITL guardrail and surfacing other vulnerabilities.
We formally define I-HITL using the concept of communication topologies and prove necessary and sufficient conditions for its realization. We show that an I-HITL protocol requires a trusted entity - a trusted computing device (or equivalent) - and characterize which such devices can and cannot realize an I-HITL protocol. We present a prototype I-HITL system called Countersign that can plug into and strengthen existing HITL systems using off-the-shelf consumer mobile devices.

---


### 443. [Work Agents: Systems, Capabilities, and Optimization](https://arxiv.org/abs/2610.35845)

**<font color=#1a73e8>作者：</font>** Zishan Xu, Enjun Du, Mingqi Gao 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As foundation models evolve from information generation to digital work execution, agents are increasingly capable of completing complex tasks across tools, applications, and workflows. However, existing research lacks a unified perspective on how agents reliably accomplish delegated work. To address this gap, we present a work-centric, system-level perspective that views work agents as systems combining foundation models and runtime harnesses to execute tasks in stateful workspaces and deliver verifiable outcomes. We introduce two complementary dimensions, work persistence and work openness, to characterize working conditions, and classify digital work into five forms according to task scope and organization. Building on this framework, we identify five core capability families required for reliable work execution and examine approaches to model optimization, harness optimization, and their joint optimization. We further analyze existing evaluation methods and metrics from the perspective of work outcomes. Finally, we discuss future research directions, including sustained work delegation, adaptation to open environments, and the interaction between work execution and capability improvement. This paper provides a unified framework for understanding, optimizing, and evaluating work agents, supporting the development of systems capable of delivering reliable, verifiable, and practically valuable work outcomes.

---


### 444. [OSWAM: An Effective World Action Model with One-Step Action Generation](https://arxiv.org/abs/2610.35850)

**<font color=#1a73e8>作者：</font>** Guowen Zhang, Liyi Chen, Xu Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Direct-policy World Action Models (WAM) have demonstrated the benefits of decoupling action generation from explicit future visual prediction for efficient inference in autonomous driving and embodied control. However, they still require tens of denoising steps to achieve competitive action quality, incurring substantial latency and hindering real-time deployment. Simply reducing the number of denoising steps will collapse the nonlinear multi-step denoising trajectory into coarse updates, substantially degrading action quality. To reduce the denoising steps while enabling real-time action generation, we present an effective world action model with one-step action generation, namely OSWAM, for autonomous driving and embodied control. We argue that it is the absence of structured action priors in random noise initialization that forces direct-policy WAMs to recover coherent action sequences through iterative denoising. Hence, we construct imagination tokens to initialize the diffusion process, providing physical priors and action-conditioned representations. We further introduce privileged information distillation with future conditioning to enhance future-aware action generation. As a result, OSWAM can efficiently and effectively generate high quality actions in just one diffusion step. Our experiments demonstrate that OSWAM achieves comparable or even better results in both autonomous driving and embodied control than direct-policy WAM and Joint-WAM that require tens of steps. It obtains approximately $3\times$ speedup over direct-policy WAM baselines and supports real-time compiled inference with latency as low as 40ms on an NVIDIA RTX 5090 GPU. The project page is available at this https URL

---


### 445. [FL4N: Feed-forward Latent Model for 4D Novel View Synthesis](https://arxiv.org/abs/2610.35854)

**<font color=#1a73e8>作者：</font>** Eunbeen Hong, Hyeonseo Yu, Honggyu An 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 4D novel view synthesis (NVS) aims to render dynamic scenes across viewpoints and timestamps, which requires jointly inferring 3D structure and temporal dynamics. Existing monocular feed-forward methods often rely on explicit 4D Gaussian representations, which are prone to temporal inconsistency and severe rendering artifacts. We present FL4N, the first feed-forward latent 4D NVS model. Instead of relying on explicit 4D primitives, FL4N encodes a 4D scene prior into a unified latent representation across space and time. Our core insight is that learning temporal dynamics as residuals on top of a pretrained static latent prior enables effective 4D modeling with limited dynamic training data. To this end, we introduce a lightweight dynamic encoder that leverages static scene features to disentangle object motion from camera-induced parallax. Trained solely with an image synthesis objective, FL4N achieves state-of-the-art 4D NVS quality while rendering in real time. Its learned latent representation generalizes to real-world videos and disentangles viewpoint from time.

---


### 446. [Center-of-Mass Interpretation of Evolution Strategies](https://arxiv.org/abs/2610.35865)

**<font color=#1a73e8>作者：</font>** Akshat Gupta  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evolution strategies (ES) update a model by sampling a population of perturbed copies, scoring each one, and moving in the reward-weighted direction of the perturbations. This update is usually presented as an estimate of a smoothed gradient. We present a geometrical interpretation of this update instead. Treat each perturbed model as a particle and its reward as the particle's mass. Before scoring, every particle has the same mass and the population balances at its centroid. Once rewards are assigned, it balances at its reward-weighted center of mass instead. We show that the mean-subtracted ES update is exactly this displacement, scaled by a scalar factor that depends on the mean reward, for any finite population. The physical reading needs nonnegative rewards, which can always be arranged by adding a constant to every reward without changing the update. In the limit of a large population or under antithetic sampling, the centroid sits on the model itself, so ES has an even simpler geometric interpretation: from its current location, the model moves towards the reward-weighted center of mass of its own population. The same picture explains what subtracting the mean reward does: it changes the point from which the displacement is measured, from the model to the sampled centroid. Our contribution is an intuitive, geometric way to visualize an ES update, exact for any finite population.

---


> [!TIP]
> 当前位于：**401-446**（第 9/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-446**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
