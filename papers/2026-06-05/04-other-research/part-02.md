# 📦 其他研究 | 2026年06月05日

> 本类共 **265** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-265](./part-06.md)

---

### 51. [StandardE2E: A Unified Framework for End-to-End Autonomous Driving Datasets](https://arxiv.org/abs/2606.04271)

**<font color=#1a73e8>作者：</font>** Stepan Konev  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous driving has shifted from modular perception-prediction-planning stacks toward end-to-end (E2E) models that map sensor inputs directly to vehicle control, often regularized by auxiliary tasks such as 3D detection, motion forecasting, and HD-map perception. Progress is driven by a fast-growing ecosystem of sensor-rich driving datasets, yet each ships its own file formats, APIs, coordinate conventions, and modality coverage, leaving cross-dataset experimentation and even basic per-dataset preprocessing to be re-implemented per project. We present StandardE2E, a framework that provides a single unified interface over E2E driving datasets. StandardE2E (i) standardizes per-dataset preprocessing under one shared data schema; (ii) combines multiple datasets in a single PyTorch DataLoader for cross-dataset pretraining, auxiliary-task supervision, and scenario-level filtering; and (iii) reduces adding a new dataset to a single per-dataset mapping from raw frames to the canonical schema, leaving the entire downstream pipeline unchanged. The framework supports six datasets out of the box: Waymo End-to-End, Waymo Perception, Argoverse 2 Sensor, Argoverse 2 LiDAR, NAVSIM (OpenScene-v1.1), and WayveScenes101, and is released as the open-source standard-e2e Python package, available at this https URL.

---


### 52. [Characterizing initial human-AI proof formalization workflows](https://arxiv.org/abs/2606.04273)

**<font color=#1a73e8>作者：</font>** Katherine M. Collins, Simon Frieder, Jonas Bayer 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> For centuries, human mathematicians have written proofs to substantiate their mathematical arguments; yet, the ability to automatically verify the validity of proofs has long been a challenge. Advances in AI systems' ability to generate code and engage in increasingly high-level mathematical reasoning promise to transform people's ability to formalize and thereby verify proofs. While many works focus on benchmarking the current frontier, we instead study how people use these tools. We conduct a mixed-methods analysis into the initial impact of AI on people's formalization workflows: what people claim they want, what they see as the barriers to those visions, and how they actually use and adapt AI in practice. A qualitative survey shows that people's preferences are diverse, but with a general desire for AI assistance in formalization that preserves high-level human control over the proof discovery process. To assess how people actually engage with AI for formalization under such limitations, we conduct a controlled user study in which participants formalize informal math problems and their proofs, with and without AI, across a range of mathematical problems at varying levels of difficulty and domains. Despite limitations of the tools at the time for autoformalization, participants tend to attain higher formalization accuracy when allowed access to AI tools than when formalizing on their own, with most participants flexibly choosing to use multiple different AI tools. Taken together, our work sheds light on the early stages of AI integration into formalization workflows, involving an intimate interplay of human and AI engagement.

---


### 53. [From Ticks to Flows: Dynamics of Neural Reinforcement Learning in Continuous Environments](https://arxiv.org/abs/2606.04275)

**<font color=#1a73e8>作者：</font>** Saket Tiwari, Tejas Kotwal, George Konidaris  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a novel theoretical framework for deep reinforcement learning (RL) in continuous environments by modeling the problem as a continuous-time stochastic process, drawing on insights from stochastic control. Building on previous work, we introduce a viable model of actor-critic algorithm that incorporates both exploration and stochastic transitions. For single-hidden-layer neural networks, we show that the state of the environment can be formulated as a two time scale process: the environment time and the gradient time. Within this formulation, we characterize how the time-dependent random variables that represent the environment's state and estimate of the cumulative discounted return evolve over gradient steps in the infinite width limit of two-layer networks. Using the theory of stochastic differential equations, we derive, for the first time in continuous RL, an equation describing the infinitesimal change in the state distribution at each gradient step, under a vanishingly small learning rate. Overall, our work provides a novel nonparametric formulation for studying overparametrized neural actor-critic algorithms. We empirically corroborate our theoretical result using a toy continuous control task.

---


### 54. [Derivative Informed Learning of Exchange-Correlation Functionals](https://arxiv.org/abs/2606.04279)

**<font color=#1a73e8>作者：</font>** Eike S. Eberhard, Luca A. Thiede, Abdul Aldossary 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine-learned (ML) exchange-correlation (XC) functionals aim to replace human-designed density functional approximations by learning directly from reference data, but they still do not consistently outperform traditional $\mathcal{O}(N^4)$-scaling hybrid functionals. We study a hybrid-distillation setting in which $\mathcal{O}(N^3)$-scaling ML-XC functionals are trained to reproduce B3LYP/def2-SVP targets. We introduce Derivative Informed XC-Loss (DI-Loss), a loss that incorporates additional information from the reference hybrid functional by supervising first and second derivatives of the energy on the Grassmannian of admissible density matrices. Rather than only matching the self-consistent fixed point, DI-Loss aligns the local first- and second-order response of the learned functional with that of the target functional. Across four evaluated architectures, DI-Loss consistently improves the main energy metrics. Averaged uniformly across architectures, the total-energy MAE decreases by 66% relative to energy and density supervision alone. The density-sensitive mean-field energy metric $E_\rho$ improves from $1.2$ to $0.8$ mEh on average, while dipole and $\mathcal{L}_2$ density errors do not improve uniformly. We further show that densities from the distilled functionals reduce hybrid-functional SCF iterations by up to 50%. In downstream TDDFT calculations, Hessian supervision improves excited-state predictions, with XCdiff reducing the mean excitation-energy MAE by 19 - 35%.

---


### 55. [The Loss Is Not Enough: Sampling Conditions and Inductive Bias in Contrastive Representation Learning](https://arxiv.org/abs/2606.04280)

**<font color=#1a73e8>作者：</font>** Justinas Zaliaduonis, Patrick Putzky, Till Richter 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contrastive learning has become a leading paradigm for self-supervised representation learning, yet the conditions under which it recovers meaningful latent geometry remain incompletely understood. We develop a measure-theoretic framework formalizing the diversity condition, a support requirement on positive-pair sampling that is necessary for isometric latent recovery. We show that the standard full-support von Mises-Fisher setting implies the satisfaction of the diversity condition and as a consequence global contrastive loss minimizers recover latent geometry up to orthogonal transformation, while restricted conditionals can make non-orthogonal maps attain strictly lower asymptotic contrastive loss. We introduce a support-corrected Information Noise Contrastive Estimation (InfoNCE) variant as a theoretical fix: this correction makes orthogonal latent space recovery achievable but does not uniquely select it. Experiments on synthetic benchmarks validate the identifiability predictions, and CIFAR-10 experiments are consistent with the qualitative prediction that architectural inductive bias becomes more important when sampling diversity is limited. Together, our results clarify how sampling mechanisms and encoder inductive bias interact in contrastive representation learning.

---


### 56. [Using Text-Based Causal Inference to Disentangle Factors Influencing Online Review Ratings](https://arxiv.org/abs/2606.04286)

**<font color=#1a73e8>作者：</font>** Linsen Li, Aron Culotta, Nicholas Mattei  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Online reviews provide valuable insights into the perceived quality of facets of a product or service. While aspect-based sentiment analysis has focused on extracting these facets from reviews, there is less work understanding the impact of each aspect on overall perception. This is particularly challenging given correlations among aspects, making it difficult to isolate the effects of each. This paper introduces a methodology based on recent advances in text-based causal analysis, specifically CausalBERT, to disentangle the effect of each factor on overall review ratings. We enhance CausalBERT with three key improvements: temperature scaling for better calibrated treatment assignment estimates; hyperparameter optimization to reduce confound overadjustment; and interpretability methods to characterize discovered confounds. In this work, we treat the textual mentions in reviews as proxies for real-world attributes. We validate our approach on real and semi-synthetic data from over 600K reviews of U.S. K-12 schools. We find that the proposed enhancements result in more reliable estimates, and that perception of school administration and performance on benchmarks are significant drivers of overall school ratings.

---


### 57. [Scaling Novel Graph Generation via Lightweight Structure-Guided Autoregressive Models](https://arxiv.org/abs/2606.04287)

**<font color=#1a73e8>作者：</font>** Alessio Barboni, Massimiliano Lupo Pasini, Bishal Lakha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generating realistic and diverse graphs is a key problem in machine learning, with applications in molecular discovery, circuit design, cybersecurity, and beyond. However, current graph generative models remain limited by scalability and novelty. Diffusion-based methods often require costly full-adjacency operations and long denoising chains, while many autoregressive and hybrid models have at least quadratic complexity. In addition, these models often imitate training graphs rather than generalize beyond them.
We propose a lightweight autoregressive framework to address these issues. It uses a structure-guided topological ordering to serialize graphs into regular edge sequences, enabling near log-linear generation, and a two-phase training strategy that combines exploration-oriented augmentation with iterative refinement to reduce overfitting and promote controlled novelty.
Experiments on molecular and non-molecular benchmarks show that our approach improves novelty while preserving high validity and uniqueness. The framework also supports both LSTM and Mamba-style causal sequence backbones, with large-memory accelerators enabling longer graph-sequence experiments beyond typical GPU limits.

---


### 58. [PE-MHL: Physics-Encoded Modular Hybrid Layers for Scalable Learning of Complex Systems](https://arxiv.org/abs/2606.04290)

**<font color=#1a73e8>作者：</font>** Ismail Hassaballa, Mircea Lazar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid models that combine physics-based and data-driven components have shown strong potential for achieving accuracy and interpretability in control applications. While recent methods have made progress in incorporating physical consistency, challenges remain in scalability, robustness to noise, and control of model complexity. This paper proposes a Physics-Encoded Modular Hybrid Layer (PE-MHL) framework, in which a baseline physics-based model is incrementally refined through the addition of new sub-models, where each new component adds complexity while preserving what previous components have already learned. We establish a theoretical guarantee for this construction: with a least-squares initialization of each new sub-model, the training error is monotonically non-increasing in the number of sub-models and provably converges. Empirical evaluations on a nonlinear NARX benchmark and the Quanser Aero 2 platform demonstrate that PE-MHL outperforms equivalently sized monolithic networks in both accuracy and generalization, while also providing more stable training dynamics and better preservation of underlying data structures.

---


### 59. [A Cookbook of 3D Vision: Data, Learning Paradigms, and Application](https://arxiv.org/abs/2606.04291)

**<font color=#1a73e8>作者：</font>** Hongyang Du, Zongxia Li, Dawei Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D vision has rapidly evolved, driven by increasingly diverse data representations, learning paradigms, and modeling strategies. Yet the field remains fragmented across representations and benchmarks, making it difficult to develop unified perspectives on efficiency, fidelity, and scalability. This work provides a data-centric taxonomy of 3D vision that connects geometric representations, datasets, learning frameworks, and applications within a single conceptual map. We begin by analysing the principal structural representations of 3D data--point clouds, meshes, voxels, and 3D Gaussians--along with their acquisition pipelines. We then examine how dataset design, benchmark construction, and supervision regimes shape recent advances, spanning 2D-supervised 3D learning, implicit neural representations, and 4D world modeling. Through this integrative lens, we clarify the relationships among representations, learning paradigms, and downstream tasks in reconstruction, generation, and video modeling, offering a consolidated view of emerging trends toward balancing efficiency and fidelity and toward multimodal geometric grounding.

---


### 60. [Efficient and Training-Free Single-Image Diffusion Models](https://arxiv.org/abs/2606.04299)

**<font color=#1a73e8>作者：</font>** Haojun Qiu, Kiriakos N. Kutulakos, David B. Lindell  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We consider the problem of generating images whose internal structure -- defined by the distribution of patches across multiple scales -- matches that of a single reference image. Recent approaches address this problem by training a diffusion model on a single image. But even in this setting, training is computationally expensive and requires hours of optimization. Instead, we model the image using a dataset of its patches at different scales. As this dataset is finite and the dimensionality of its patches is small, the score function for a noisy patch can be computed tractably using an optimal, closed-form denoiser, eliminating the need for neural network training. We integrate this patch-based denoiser into an efficient, training-free image diffusion model, and we describe how our method connects to classical patch-based image restoration techniques. Our approach achieves state-of-the-art generation quality and diversity compared to trained single-image diffusion models, and we demonstrate applications, including unconditional image generation, text-guided stylization, image symmetrization, and retargeting. Further, we show that our approach is compatible with latent space diffusion, and we show multiple additional acceleration techniques to achieve megapixel single-image generation in one second, and gigapixel generation in minutes.

---


### 61. [XSSR: Cross-Domain Self-Supervised Representative Selection for Efficient Annotation in Medical Image Segmentation](https://arxiv.org/abs/2606.04301)

**<font color=#1a73e8>作者：</font>** Byunghyun Ko, Aleksei Anisimov, Kobe Ke 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Acquiring labeled medical image data is resource-intensive and a challenge further exacerbated in cross-domain scenarios where source and target datasets differ in imaging equipment, population, or clinical site. This study introduces XSSR (Cross-Domain Self-Supervised Representative Selection), a framework designed to minimize annotation effort in the target domain while maintaining robust segmentation performance. XSSR comprises three stages: first, a Masked Autoencoder (MAE) is trained on unlabeled source data to establish a shared embedding space without requiring target labels; second, a greedy selection algorithm scores unlabeled target samples based on a composite density, novelty, and diversity criterion; and third, a U-Net segmentation model is trained exclusively on the selected subset. The novelty-diversity trade-off parameter, alpha, is automatically calibrated by minimizing embedding-space coverage, eliminating manual tuning. We evaluate XSSR on three public benchmarks: Chest X-ray, RIGA+ retinal fundus imaging, and multi-site Prostate MRI, each under a fixed 5% annotation budget. XSSR achieves 99.3% of full-data performance on Chest X-ray using only 22 labeled samples, surpasses random selection by up to 2.5 Dice points on Prostate MRI, and consistently outperforms the CoreSet baseline by 0.4 to 1.2 Dice points across all datasets. Ablation studies indicate that diversity is the most influential scoring component, and per-site analysis shows that performance correlates with scanner similarity to the source domain.

---


### 62. [Offline-to-Online Learning in Linear Bandits](https://arxiv.org/abs/2606.04305)

**<font color=#1a73e8>作者：</font>** Kushagra Chandak, Toshinori Kitamura, Xiaoqi Tan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study online learning with an additional offline dataset in the stochastic linear bandit setting. Although this problem arises frequently in practice, the offline-to-online tradeoff remains poorly understood in structured environments. We propose a linear bandit algorithm that balances this tradeoff: it relies on offline data during early rounds, and increasingly favors exploration as the horizon grows. We establish regret bounds showing that our method is simultaneously competitive with both purely online and purely offline solutions. In particular, it achieves sublinear regret relative to the optimal action in the number of online interactions, while its regret relative to an offline reference decreases as the number of offline samples grows. Empirical results further demonstrate its effectiveness across various problem parameters.

---


### 63. [Folded Transport MCMC: Certifiable Quotient Posterior Computation for Symmetric Bayesian Models](https://arxiv.org/abs/2606.04307)

**<font color=#1a73e8>作者：</font>** Jun Hu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian models with finite symmetry - mixture models with exchangeable components, structural identification with closely-spaced modes - define posteriors that are invariant under a group of label permutations, creating redundant multimodality that degrades MCMC convergence diagnostics. We introduce Folded Transport MCMC (FolT-MCMC), which performs inference directly on the quotient posterior by constructing an independence sampler on the fundamental domain of the symmetry group. The quotient proposal is formed by symmetrising a learned normalising flow over the group orbits. We prove that the LCNF oscillation-based certification framework transfers to the quotient metric with a stabiliser-corrected ball-mass bound and improved covering radius, and that the quantile-core certified lower bound improves whenever the unfolded flow exhibits cross-mode proposal deficiency. On Gaussian mixtures (d = 2 - 20), label-switching targets (up to 24 equivalent modes), and a standard Bayesian three-component mixture posterior, the quantile-core certified improvement ratio ranges from 2x to 145x, with the folded certificate empirically nearly dimension-free. On real accelerometer data from a supertall building during Typhoon Mangkhut, FolT-MCMC yields a non-vacuous quantile-core certificate where the unfolded certificate is vacuous.

---


### 64. [Creative Reading: Scaffolding Reading for Transformation](https://arxiv.org/abs/2606.04308)

**<font color=#1a73e8>作者：</font>** Sophia Liu, Sarah Abowitz, Yijun Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Reading augmentation systems increasingly help readers process text at scale. While these tools address real constraints of time and cognitive load, they often implicitly frame reading as information transmission, or "reading to discard," delegating interpretation and effort to the machine. Yet this delegation changes the outcome of reading. For example, in scholarly reading, deciding what a research text implies and why it matters is central to the work of scholarly production. We propose creative reading as an alternative goal: reading augmentation that supports readers in creating both readings and themselves as readers. By putting literary and narrative theories into conversation with scholarly sensemaking and creativity support, we present a provocation-oriented design space for valuing the process of reading as a way of preserving a plurality of readings and transforming readers over time.

---


### 65. [Latent Anchor-Driven Test Generation for Deep Neural Networks](https://arxiv.org/abs/2606.04310)

**<font color=#1a73e8>作者：</font>** Bin Duan, Matthew B. Dwyer, Guowei Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep Neural Networks (DNNs) are increasingly being deployed in security-critical and safety-sensitive applications, which makes rigorous testing essential to identify and mitigate model weaknesses. Existing DNN testing approaches explore either the input space or a learned latent space. While latent-space generation can better maintain plausibility than direct input-space mutation, current methods still face a trade-off among exploration controllability, failure diversity, and seed-relative semantic drift. To overcome these limitations, we propose Latte, a black-box testing framework that generates semantically proximate, diverse, and fault-revealing test cases by leveraging the latent space. Specifically, Latte encodes each input seed with a pre-trained VQ-VAE and performs a seed-centered, one-step latent mutation along directions defined by anchors sampled from alternative classes, followed by quantization and decoding back to the input space. This explores local neighborhoods around each seed within the learned latent manifold, resulting in a larger number and broader diversity of oracle-triggering prediction discrepancies under the same budget. We evaluated Latte on 5 datasets and 10 DNN models in single-model and multi-model testing scenarios. Across the evaluated datasets and models, Latte improves fault exposure and behavioral diversity under matched testing budgets. Under the single-model setting, it also maintains low seed-relative semantic drift with respect to the source seeds.

---


### 66. [Formal verification of the S-two AIR](https://arxiv.org/abs/2606.04311)

**<font color=#1a73e8>作者：</font>** Jeremy Avigad, Anat Ganor, Lior Goldberg 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> StarkWare's S-two prover provides an efficient means for establishing, on blockchain, that a program written in the Cairo virtual machine language runs to completion. The latter claim is encoded by an algebraic intermediate representation (AIR) that captures the semantics of the Cairo language. The AIR asserts the existence of tables of values from a finite field satisfying certain algebraic constraints. A cryptographic interactive proof system, circle STARK, provides an efficiently-checked certificate that the AIR is satisfied. We describe our verification, using the Lean 4 proof assistant, that the AIR encoding is sound, which is to say, the satisfiability of the AIR implies the computational claim.

---


### 67. [Testing Neural Networks via Bayesian-Guided Exploration of Decision Landscapes](https://arxiv.org/abs/2606.04314)

**<font color=#1a73e8>作者：</font>** Bin Duan, Meiru Che, Guowei Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As neural networks are increasingly deployed in safety-critical domains, testing is essential to evaluate and improve their reliability. Existing testing methods, whether black-box or white-box, primarily use global mutation or coverage-guided strategies, both of which struggle to efficiently uncover diverse model failures while remaining proximate to the original data distribution and semantics. We propose BayesWarp, a testing framework that addresses this limitation by mutating decision-critical input regions identified via interpretable saliency techniques and adaptively guiding the testing process using an uncertainty-aware Bayesian Optimization strategy, enabling the discovery of diverse failures while preserving distributional and semantic proximity to the original data. Evaluation on MNIST, CIFAR-10, and ImageNet across six neural network models shows that BayesWarp improves failure discovery, failure diversity, test case quality, and critical neuron coverage under a fixed mutation budget. These results demonstrate that BayesWarp improves testing effectiveness. Moreover, fine-tuning with the generated failure cases leads to improvements in model performance.

---


### 68. [Toward a Generalized Defense Across Sparse, Continuous, and Structured Parameter Attacks](https://arxiv.org/abs/2606.04317)

**<font color=#1a73e8>作者：</font>** Bin Duan, Zeyu Bai, Guowei Yang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deep neural networks are increasingly deployed across heterogeneous and partially untrusted environments, where models are distributed through cloud storage, CI/CD pipelines, containerized services, and edge execution platforms. This broad deployment landscape exposes model parameters to various integrity risks. Unlike input-space adversarial attacks, parameter attacks directly tamper with the model's internal parameters and persist across all subsequent inferences. Existing defenses either require retraining, incur significant accuracy degradation, or are limited to specific attack classes. However, in real-world deployment scenarios, the forms of parameter attacks are often unpredictable. To address this challenge, we present ParDef, a generalized defense for deep neural networks against diverse types of parameter attacks. ParDef integrates keyed channel reparameterization, which obscures sensitive parameter directions, QC-LDPC quantization, which embeds redundancy and supports error correction, and adaptive robust inference, which stabilizes predictions under uncertainty. Our evaluation on CIFAR-10, CIFAR-100, and Tiny-ImageNet using ResNet and VGG models demonstrates that ParDef consistently reduces attack success rates across different parameter attacks while maintaining high model performance and incurring only moderate deployment overhead. These results highlight that ParDef is a practical and generalized defense for DNN deployments.

---


### 69. [Neural Galerkin Normalizing Flows for Bayesian Inference of Diffusions with Inaccessible Boundaries](https://arxiv.org/abs/2606.04324)

**<font color=#1a73e8>作者：</font>** Riccardo Saporiti, Fabio Nobile  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> One of the primary challenges in Bayesian inference on the parameters of a diffusion model from discrete observations is the unavailability of an analytical expression for the transition density function between consecutive observation times, which is needed to derive the likelihood function.
Extending previous studies that solve Fokker-Planck (FP) type partial differential equations with Normalizing Flows, we propose a new Normalizing Flow architecture to learn the transition density function of the diffusion process between two observation times. We do so by solving in a Neural Galerkin framework the associated FP equation with a Dirac mass as initial condition, over a specified training distribution of the initial datum and the coefficients of the diffusion. We specifically focus on processes whose diffusion matrix vanishes in certain inaccessible boundary regions, such as Stochastic Volatility models that satisfy a Feller condition.
The product of the obtained transition densities evaluated along the observed trajectory approximates the likelihood function, thereby enabling cheap posterior sampling via Markov chain Monte Carlo (MCMC). After the offline training phase, inference becomes significantly more efficient, as it avoids the need to solve the FP equation in real time for each parameter proposed by the MCMC sampler or to rely on other likelihood-free methods for Bayesian inference that involve repeated simulation of diffusion bridges.

---


### 70. [Measuring What Matters: Synthetic Benchmarks for Concept Bottleneck Models](https://arxiv.org/abs/2606.04326)

**<font color=#1a73e8>作者：</font>** Julian Skirzynski, Harry Cheon, Shreyas Kadekodi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Concept bottleneck models predict outcomes from high-level concepts detected in inputs. Although concepts provide a simple way to reap benefits from interpretability, very few datasets include concept labels. This limits researchers' ability to determine which problems are suitable for these models, isolate the factors that drive their performance or lead to failures, or uncover which algorithms perform well. In this paper, we develop synthetic benchmarks for concept-bottleneck models, focusing on their two main use cases: decision support, in which models assist humans in making better decisions, and automation, in which models handle routine tasks without supervision. Our benchmarks can generate labeled datasets while controlling for properties that affect performance, including data modality, concept choice, annotation quality, and completeness. We demonstrate how the benchmarks can be used to evaluate representative classes of concept bottleneck models. Our demonstrations show how the benchmarks can diagnose failure modes and guide follow-up testing.

---


### 71. [A Geometric Characterization of the Stationary Plateau for Two-Layer Neural Networks](https://arxiv.org/abs/2606.04327)

**<font color=#1a73e8>作者：</font>** Tian Ding, Dawei Li, Ruoyu Sun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate the geometric structure of stationary plateaus that arise in the loss landscape of two-layer neural networks with smooth activation functions. We focus on the phenomenon of "neuron splitting" where duplicating a hidden neuron yields an affine set of stationary points in a wider network. We provide a comprehensive classification of all stationary points on these plateaus, determining under what conditions they constitute local minima or saddle points. Our characterization hinges on a per-neuron curvature object we term the "inner Hessian" matrix. Our analysis reveals that the definiteness of the inner Hessian and the choice of splitting coefficients jointly dictate the local geometry of the plateau. We show that "splitting" a local minimum can yield either a mixture of local minima and saddles or an all-saddle plateau, with a concrete sure-saddle region identified under mild assumptions. In contrast, splitting a saddle point always produces a plateau of saddle points. Our results unify and extend prior landscape analyses, elucidating when and how model expansion preserves or alters the nature of stationary points. These findings offer new geometric insights into the effects of width expansion and reparameterization in neural networks.

---


### 72. [Policy Gradient for Continuous-Time Robust Markov Decision Processes](https://arxiv.org/abs/2606.04335)

**<font color=#1a73e8>作者：</font>** Tanya Veeravalli, David M. Bossens, Atsushi Nitanda  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The framework of robust Markov decision processes (RMDPs) allows the design of reinforcement learning agents that satisfy performance guarantees under worst-case transition dynamics. Traditional RMDPs consider discrete-time dynamics and recently, sample-efficient policy gradient algorithms have been considered in this context. This paper investigates policy gradient algorithms within a continuous-time RMDP framework. Policy gradients and adversarial gradients are derived using pathwise and adjoint-based formulas for stochastic and ordinary differential equations. We propose double-loop optimisers to obtain linear convergence in the oracle-based setting and an $\tilde{\mathcal{O}}(\frac{1}{\epsilon^2})$ sample complexity in the sample-based setting in an analysis which also derives novel tools for the framework of undiscounted total cost MDPs. Additionally, we propose mean-field optimisers as distributional optimisers with an $\tilde{\mathcal{O}}(\frac{1}{K})$ oracle-based convergence rate and an $\tilde{\mathcal{O}}(\frac{N^2}{\epsilon})$ sample complexity under $N$-particle approximation. The effectiveness of continuous-time policy gradient algorithms is confirmed for both optimisers on continuous-time RMDPs with neural ordinary differential equation dynamics.

---


### 73. [Federated Learning for Multi-Center Sepsis Early Prediction with Privacy-Preserving](https://arxiv.org/abs/2606.04338)

**<font color=#1a73e8>作者：</font>** Xixi Tian, Di Wu, Xiang Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Privacy-sensitive and distributed characteristics of multi-center medical data bring severe obstacles to centralized modeling for accurate early prediction of sepsis. Federated learning (FL) has attracted growing attention as a promising framework for collaborative model development, as it allows multiple institutions to jointly train predictive models without directly sharing or centralizing raw data. Nevertheless, its practical performance, robustness, and privacy-preserving benefits remain insufficiently evaluated using real-world clinical datasets. To bridge this gap, this study systematically examines the application of federated learning to multi-center sepsis prediction. The experimental dataset consists of 648 clinically screened samples collected from three tertiary hospitals in China, with rigorous inclusion and exclusion criteria. We establish a centralized training paradigm as the performance baseline, and then implement a horizontal federated learning framework for distributed collaborative modeling. Extensive experimental results demonstrate that the federated learning-based model achieves highly comparable prediction accuracy to the centralized counterpart, while fundamentally avoiding privacy leakage. Further privacy security analysis verifies that malicious attackers cannot reconstruct the original patient data from the transmitted model parameters, indicating strong resistance against data reconstruction attacks. This work not only validates the practicality and security of federated learning in clinical sepsis prediction, but also provides a reliable and feasible solution for privacy-preserving multi-center medical collaboration.

---


### 74. [Literature-Guided Minimax Optimization of Virtual Epilepsy Neurostimulation](https://arxiv.org/abs/2606.04339)

**<font color=#1a73e8>作者：</font>** Cathy Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Computational models of epilepsy promise patient-specific treatment design, but most optimization workflows still search for parameters that perform well on average. In neuromodulation, this is a weak target: a protocol that improves the mean response can still fail in the patient whose network is least tolerant to stimulation. We present a literature-guided minimax pipeline that couples PubMed-scale hypothesis extraction, The Virtual Brain (TVB) Epileptor simulations, and large-language-model-guided black-box optimization. The optimizer proposes either intrinsic model-control parameters or clinically interpretable external-stimulation protocols; TVB evaluates each proposal across sampled virtual patients; and the objective maximizes worst-case reward, defined as the negative variance of simulated seizure activity. In the intrinsic model-control experiment, the best archived parameter set improved worst-case reward from -0.5285 to -0.3182, a 39.8% gain over baseline. The clinical-style external-stimulation search produced a much smaller worst-case improvement (1.7%), and a 20-patient virtual cohort showed no aggregate benefit (p=0.9019), despite a 55% responder rate and a positive temporal-lobe subgroup signal. The study should be read as an in silico proof of concept for robust, literature-aware neurostimulation design, not as clinical evidence.

---


### 75. [Noisy memory encoding explains negative polarity illusions](https://arxiv.org/abs/2606.04340)

**<font color=#1a73e8>作者：</font>** Yuhan Zhang, Edward Gibson  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A sentence like "The authors that no critics recommended have ever received acknowledgment for a best-selling novel" is sometimes rated as acceptable even though, strictly speaking, it is ungrammatical because the negative polarity word "ever" is not licensed where it is. This behavioral effect is sometimes called a "negative polarity illusion". Here we propose that the lossy context surprisal theory of Hahn et al. (2022) -- whereby people have an imperfect encoding of complex sentences -- might explain this effect. We hypothesize that people have poor memory representation of the determiners in the main-clause and embedded-clause subjects and could entertain a determiner exchange that licenses ever. We propose that more similar determiners in those positions would trigger stronger illusion effects. Acceptability judgment tasks with six novel determiner pairs (e.g., "few" and "many", "few" and "most") support our proposal, showing, specifically, that a novel sentence, "Many authors that few critics recommended have ever received acknowledgment for a best-selling novel", triggered a much stronger illusion than the canonical one even without time pressure. These results offer further support for the suggestion that human language processing is imperfect and resource-rational: in face of working memory limitations, humans rationally reconstruct what is most likely from noisy linguistic input to facilitate downstream processing.

---


### 76. [Expectations vs. Realities: The Cost of MSE-Optimal Forecasting Under Conditional Uncertainty](https://arxiv.org/abs/2606.04342)

**<font color=#1a73e8>作者：</font>** Riku Green, Zahraa S. Abdallah, Telmo M Silva Filho  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-step time series forecasting (MSF) is commonly evaluated using point-wise error metrics such as mean squared error (MSE), implicitly treating the conditional mean as a sufficient target. We show that this can be misleading under conditional uncertainty, where the conditional expectation becomes unrepresentative of typical realized values at longer horizons. We formalize this effect through a conditional uncertainty gap and prove that whenever this gap is nonzero, no deterministic predictor can simultaneously minimize MSE and match the marginal distribution of realized futures. This establishes a fundamental, model-agnostic trade-off between point accuracy and marginal realism in MSF evaluation. Using controlled stochastic dynamical systems and nine real-world forecasting benchmarks, we empirically characterize the resulting accuracy--realism frontier and \textbf{quantify the practical cost of MSE-only model selection}. As conditional uncertainty increases with forecast horizon, the attainable set expands into a pronounced Pareto front, separating MSE-optimal but under-dispersed predictors from methods that trade accuracy for realistic marginal variability. \textbf{Across benchmarks, we find that small relaxations in MSE ($\boldsymbol{\le 5\%}$) frequently unlock disproportionate gains in marginal realism, with median improvements of $\mathbf{17.3\%}$ and gains exceeding $\mathbf{30\%}$ in some datasets.} We further show that common forecasting strategies systematically occupy different regions of this frontier: direct multi-output predictors concentrate near the accuracy-optimal extreme, while recursive strategies and sample-based inference favors marginal realism. Together, these results expose a structural failure mode of MSE-based evaluation in long-horizon forecasting and recast strategy and inference selection as navigation of an unavoidable accuracy--realism trade-off.

---


### 77. [Robust Multi-view Clustering against Imperfect Information](https://arxiv.org/abs/2606.04343)

**<font color=#1a73e8>作者：</font>** Zhichao Huang, Haochen Zhou, Hao Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world multi-view data always suffer from imperfect information problem, where the view-specific observations are absent (i.e., Incomplete Views, IV) and cross-view correspondences are mismatched (i.e., Noisy Correspondences, NC) for certain instances. As a remedy, numerous IV- and NC-oriented multi-view clustering (MvC) methods have been proposed, which however require either reliable correspondences or sufficiently complete instances, thus stopping short of addressing the imperfect information problem. In contrast, we observe that both IV and NC challenges originate from the same issue of imperfect cross-view counterpart information, where the counterpart of an anchor instance in another view might be either unavailable or unreliable. Based on the observation, we propose a novel robust MvC framework, termed Posterior-guided Latent Counterpart Inference (PLCI), which could handle both IV and NC in a unified manner. Specifically, PLCI formulates the desired cross-view counterpart of each anchor instance as a latent variable, and integrates both instance-level reliability and prototype-level semantic transport to infer the posterior distribution of the latent counterpart. Extensive experiments on six widely-used multi-view datasets against 10 state-of-the-art MvC methods demonstrate the effectiveness of PLCI for tackling the imperfect information problem. The code will be released upon acceptance.

---


### 78. [HYolo: An Intelligent IoT-Based Object Detection System Using Hypergraph Learning](https://arxiv.org/abs/2606.04345)

**<font color=#1a73e8>作者：</font>** Isha Abid, Fawad Khan, Muhammad Khuram Shahzad  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents HYolo, an intelligent IoT-based object detection framework that integrates hypergraph learning into the YOLO architecture. Traditional YOLO-based object detection models primarily capture pairwise feature interactions and may fail to model complex high-order relationships among objects and contextual features. To address this limitation, HYolo incorporates hypergraph learning to capture richer contextual dependencies and improve object representation. Experimental evaluation on the COCO dataset demonstrates significant performance improvements over baseline YOLO models. The proposed approach achieves approximately 12% improvement in mAP@50 while enhancing overall detection accuracy and robustness. By modeling high-order feature relationships, HYolo provides improved contextual understanding and more reliable object detection performance in IoT-based environments. The results indicate that integrating hypergraph learning into object detection pipelines offers a promising direction for intelligent and context-aware IoT vision systems.

---


### 79. [Spatially Grounded Concept Bottleneck Models via Part-Factorized Attention](https://arxiv.org/abs/2606.04364)

**<font color=#1a73e8>作者：</font>** Dhanesh Ramachandram  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept bottleneck models (CBMs) predict a layer of human-named attributes before predicting a class, which makes their decisions auditable. On fine-grained recognition tasks the concept heads are usually free to attend anywhere in the image, so a head named for one body region can be satisfied by evidence on another. This work studies a part-factorized CBM that removes that freedom by construction. The method has three components built on a frozen DINOv3 vision transformer. A learned foreground gate, trained on DINOv3 patch features, suppresses background patches inside the part attention. A set of part queries cross-attends to patch features and each of the 312 CUB attributes is routed, through a fixed concept-to-part map, to read only from the part token its name implies. A learnable two-dimensional Gaussian prior, injected additively in log space into the attention logits, breaks the permutation symmetry among part queries; its means are initialized from the dataset-average keypoint location of each part, which requires no per-image keypoint supervision at training or test time. On CUB-200-2011 the spatial-prior model matches a fully supervised baseline (88.85% versus 88.95% top-1) while raising pointing accuracy by 16 points (52.6% versus 36.4%). Replacing bounding-box supervision with a PCA foreground target and combining it with the Gaussian prior removes all per-image supervision and reaches 88.6% top-1 at about 70% pointing accuracy. A keypoint-fraction sweep shows that 0.5% of the training set (about 27 images) suffices to initialize the prior with no measurable loss. Removing part identity entirely is the harder case: without any spatial prior, pointing accuracy collapses to $2.9\%$.

---


### 80. [Multi-Granularity 3D Kidney Lesion Characterization from CT Volumes](https://arxiv.org/abs/2606.04365)

**<font color=#1a73e8>作者：</font>** Renjie Liang, Zhengkang Fan, Jinqian Pan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiology reports describe kidney lesions by type, size, enhancement, and attenuation, yet existing 3D methods predict only at the patient or organ level. We reformulate kidney CT characterization as a per-lesion set-prediction task: one model emits a variable number of lesions per kidney, each with four clinical attributes. We curated 2,619 CT volumes from 788 patients at one academic medical center, with multi-granularity side- and per-lesion labels, and used KiTS23 (489 cases) for zero-shot external validation. We propose \textbf{LesionDETR}, a DETR-style architecture with size-distance Hungarian matching and a hierarchical loss that aggregates per-slot outputs to side-level objectives. Across four input representations and six encoder initializations, two design choices dominate: a segmentation mask as an input channel, and same-domain abdominal pretraining (SuPreM); generic large-corpus pretraining is no better than random initialization. LesionDETR reaches bilateral side-level abnormality AUC $0.799 \pm 0.009$ on UF-Health and $0.817 \pm 0.072$ on KiTS23. A count-conditioned variant reaches per-lesion mAP $0.190 \pm 0.083$ on cystic lesions; rare solid-lesion AP stays at the noise floor, pointing to targeted data collection, not architecture, as the next bottleneck. The framework yields verified per-lesion predictions for downstream structured report generation.

---


### 81. [MeshTok: Efficient Multi-Scale Tokenization for Scalable PDE Transformers](https://arxiv.org/abs/2606.04366)

**<font color=#1a73e8>作者：</font>** Yanshun Zhao, Xiaoyu Peng, Jiamin Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conventional patchified Transformers operate on uniform spatial partitions, distributing computational effort evenly across the domain irrespective of local features. This inflexible tokenization scheme is inherently limited in its ability to efficiently represent and process solutions to complex PDEs. To address this, we propose MeshTok, an adaptive mesh refinement (AMR)-inspired tokenization and sequence modeling framework. This method selectively refines spatial regions exhibiting sharp gradients, transient features, or multiscale structures, generating a heterogeneous set of multiscale tokens defined on a fixed simulation grid. These tokens are processed within a unified Transformer sequence, enabling the model to simultaneously capture coarse-grained global context and fine-grained local details without requiring specialized architectural components. Although adaptive refinement moderately increases token count, it promotes a more targeted allocation of computational resources to physically informative regions, which we view as a practical inductive bias rather than a formal optimality guarantee. Experimental evaluations across multiple PDE families and benchmark datasets demonstrate that MeshTok consistently improves the efficiency-accuracy trade-off compared to uniform-grid baselines. This suggests adaptive multiscale tokenization as a scalable and generalizable design principle for neural PDE modeling. Code is available at this https URL.

---


### 82. [GlossAssist -- A Tool to Simplify Corpus Creation and Study the Effect of NLP Models in Low-Resource Documentation Settings](https://arxiv.org/abs/2606.04367)

**<font color=#1a73e8>作者：</font>** Bhargav Shandilya, Matt Buchholz, Alexis Palmer  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Interlinear glossed text (IGT) is the standard format for linguistic annotation in language documentation. Producing it manually, however, is often slow and costly. Automated glossing systems have improved substantially in recent years, but adoption among field linguists remains limited. Existing tools are designed to be evaluated rather than used, offering no interpretable path for correction or the incorporation of linguistic expertise back into model behavior. We present GlossAssist, a glossing tool built around the retrieval-based architecture of CWoMP (Contrastive Word-Morpheme Pre-training), which grounds predictions in a mutable lexicon of learned morpheme representations. In conjunction with CWoMP, our system treats each correction by an annotator as part of an active learning setting, which expands the lexicon and improves future predictions without having to retrain the model. In this paper, we present our interface and argue that this feedback loop should be treated as a design requirement for NLP tools aimed at documentary linguists.

---


### 83. [When Do Fewer Coordinates Suffice in DP-SGD?](https://arxiv.org/abs/2606.04375)

**<font color=#1a73e8>作者：</font>** Huiqi Zhang, Fang Xie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differentially private stochastic gradient descent (DP-SGD) injects noise into every updated coordinate, making the injected noise energy scale with the ambient parameter dimension \(d\). We ask when private training can update fewer coordinates without losing the signal needed for optimization. We propose \textsc{TP-TopK} (Two-Phase TopK DP-SGD), a two-phase method for coordinate-sparse private training without public data, in which a private warm-up phase identifies a coordinate support used to guide the main training phase. We give a criterion characterizing when coordinate restriction can be beneficial, show via a nonconvex stationarity bound that under this condition the relevant noise term scales with the active dimension \(k\) rather than the full parameter dimension \(d\), and provide a lower bound on the reliability of warm-up-based coordinate ranking. Experiments on MNIST, FMNIST, and CIFAR-10 show that learned coordinate supports can retain more gradient energy than size-matched random supports, with the largest gains when the active dimension is small and warm-up scores are informative.

---


### 84. [Revisiting Privacy Amplification by Subsampling in Selective Release DPSGD](https://arxiv.org/abs/2606.04384)

**<font color=#1a73e8>作者：</font>** Xiaobo Huang, Fang Xie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning's reliance on sensitive data necessitates privacy-preserving techniques like Differentially Private Stochastic Gradient Descent (DPSGD). However, DPSGD suffers from substantial utility degradation and slow convergence due to gradient clipping and noise injection. Prior works have attempted to improve DPSGD from various perspectives; notably, the Differentially Private Selective Update and Release (DPSUR) algorithm has achieved remarkable model utility. However, the privacy accounting in DPSUR overlooks the variation in sampling probability introduced by the selective release mechanism, which compromises the rigor of its privacy guarantees. To address these limitations, we re-evaluate the privacy analysis of the selective release mechanism and propose a novel algorithm: Differentially Private Selective Release based on Clipped Gradients (DPSR-CG). Through a rigorous, newly derived privacy analysis and extensive experiments on multiple datasets (MNIST, CIFAR-10, IMDB, and FMNIST), we demonstrate that our DPSR-CG mechanism maintains strict privacy guarantees while achieving exceptional model performance.

---


### 85. [TITAN-FedAnil+: Trust-Based Adaptive Blockchain Federated Learning for Resource-Constrained Intelligent Enterprises](https://arxiv.org/abs/2606.04388)

**<font color=#1a73e8>作者：</font>** Muhammad Hadi, Muhammad Jahangir, Talha Shafique 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) has emerged as an effective paradigm for collaborative intelligence while preserving data privacy. However, data heterogeneity arising from non-IID distributions and decentralized security threats remain significant challenges, particularly in resource-constrained enterprise environments. This paper presents TITAN-FedAnil+, a Trust-Based Adaptive Network for blockchain-enabled federated learning in intelligent enterprises. The proposed framework introduces affinity propagation-based adaptive clustered aggregation to identify and filter malicious updates without requiring prior knowledge of the number of attackers. In addition, GPU-accelerated vectorization is employed to improve computational efficiency, while a signed state jump mechanism enables lightweight blockchain resynchronization. Experimental results demonstrate substantial reductions in memory overhead, achieving up to 81% savings across 50 communication rounds on constrained 8 GB edge devices compared with the baseline framework. The results indicate that TITAN-FedAnil+ effectively improves robustness, scalability, and resource efficiency for secure federated learning deployments in intelligent enterprise environments.

---


### 86. [When Clients Stop Following: A Cognitive Conceptualization Diagram-driven Framework for Strategic Counseling](https://arxiv.org/abs/2606.04389)

**<font color=#1a73e8>作者：</font>** Yihao Qin, Junyi Zhao, Changsheng Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) show promise in psychological counseling, yet existing benchmarks rely heavily on highly cooperative simulated clients. We observe a critical counselor-following phenomenon: these clients often rapidly shift from resistance to compliance after only a few turns, creating an illusion of therapeutic progress and inflating scores under current evaluation protocols through superficial empathy. To address this evaluation mismatch, we propose a Cognitive Behavioral Therapy (CBT)-grounded resistance-aware framework. We introduce CARS, a client simulator that explicitly models dynamic resistance via Cognitive Conceptualization Diagrams (CCDs). We present STREAMS, a dual-module framework that decouples strategic reasoning (Thinker) from response generation (Presenter) and optimizes it via reinforcement learning. We further propose EWTS-MI, an entropy-weighted metric for evaluating responsiveness under high-friction interactions. Experiments across resistant and non-resistant counseling settings validate our findings on evaluation mismatch and demonstrate the effectiveness of resistance-aware training for improving strategic robustness under challenging counseling interactions.

---


### 87. [Shortcomings and capacities of real-constrained neural networks in complex spaces](https://arxiv.org/abs/2606.04390)

**<font color=#1a73e8>作者：</font>** Andrew Gracyk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We find the asymptotic ratio between the storage capacities when enforcing real pre-activations in a complex hypothesis class as opposed to complex ones in the same class. Our methods depend on Gardner volume comparisons at critical capacity. Our proof relies on an application of the Harish-Chandra-Itzykson-Zuber (HCIZ) formula, nonstandard in literature. With the HCIZ formula, we may obtain a more robust approximation for the final asymptotic ratio. This strategy is applicable to our work specifically since we integrate over the unitary and orthogonal compact manifolds, facilitated via the Weyl integration formula and the Haar measure.

---


### 88. [Online Skill Learning for Web Agents via State-Grounded Dynamic Retrieval](https://arxiv.org/abs/2606.04391)

**<font color=#1a73e8>作者：</font>** Jiaxi Li, Ke Deng, Yun Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language agents increasingly rely on reusable skills to improve multi-step web automation across related tasks. A growing line of work studies online skill learning, where agents continually induce skills from previous task trajectories and reuse them in future tasks on the fly. However, existing methods mainly reuse skills at the task-level: a fixed set of skills is retrieved based on the initial task instruction and then held fixed throughout execution. This static strategy is misaligned with web execution, where the appropriate next action depends not only on the task goal but also on the current webpage state, which often transitions into situations that the initial skills fail to cover. To address this gap, we propose State-Grounded Dynamic Retrieval (SGDR), an online skill learning method that enables stepwise skill reuse for web agents. SGDR consists of three components: a sliding-window extraction process that turns completed trajectories into reusable sub-procedures invokable at intermediate execution states, a dual text-code representation that connects skill retrieval with executable action, and a state-grounded dynamic retrieval mechanism that matches skills to both the task goal and the current webpage state. Experiments on WebArena across five domains show that SGDR consistently outperforms strong baselines, achieving average success rates of 37.5% with GPT-4.1 and 24.3% with Qwen3-4B, corresponding to relative gains of 10.6% and 10.0% over the strongest baseline, respectively. The code is available at this https URL.

---


### 89. [Physics-Informed Neural Network Modeling of Biodegradable Contaminant Transport through GCL/SL Composite Liners](https://arxiv.org/abs/2606.04392)

**<font color=#1a73e8>作者：</font>** Dong Li, Yapeng Cao, Haiping Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study develops a two-domain physics-informed neural network framework for contaminant transport through a GCL/SL composite liner system, in which the thin GCL layer is treated using a steady-state advection-dispersion-biodegradation formulation and the underlying soil liner is modeled as a transient transport domain. Two formulations are evaluated against analytical and finite-element reference solutions under different leachate-head conditions: a standard PINN with soft constraint enforcement (Std-PINN) and a hard-constrained PINN (H-PINN), in which selected boundary and initial conditions are embedded directly into the trial solutions. The Std-PINN captures the overall breakthrough behavior but shows larger errors during the early transport stage, particularly under higher leachate heads where advective transport becomes more pronounced. The H-PINN reduces the optimization burden associated with penalty-based constraint enforcement and provides more accurate and stable concentration predictions, lowering the MAE from approximately 0.058-0.067 for the Std-PINN to about 0.011-0.023 for the H-PINN, while reducing the MRE from approximately 9.10%-19.16% to about 2.08%-3.14%. Parametric analyses confirm that the H-PINN with the tanh activation function and an optimized network structure provides the best predictive accuracy. The H-PINN is further extended to inverse modeling for identifying the SL degradation half-life from limited concentration observations, showing reliable convergence toward prescribed values and acceptable robustness under low-to-moderate observation noise.

---


### 90. [DPDL: Towards Differential Privacy Preservation in Decentralized Stochastic Learning on Non-IID Data](https://arxiv.org/abs/2606.04399)

**<font color=#1a73e8>作者：</font>** Yunsheng Yuan, Xue Xiao, Lina Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the paradigm of decentralized learning, a group of agents collaborate to train a global model using distributed datasets without a central server. Although the power of collaboration has been verified by many state-of-the-art studies, it entails extensive gradient information exchanging among the agents and thus induces high risk of privacy leakage for the individual agents. Moreover, in real-world applications, the training data are usually non-identically and independently distributed across the agents, inducing more challenges to enable privacy-preserved decentralized learning. To address these issues, we propose a privacy-preserved decentralized learning algorithm with non-IID data, DPDL, which leverages the notion of Differential Privacy (DP) in cross-gradient aggregation through a similarity-based calibration technique. Specifically, in each round, each agent perturbs the cross-gradients (i.e., the derivatives of its neighbors' local model in its private local data) by Gaussian noise mechanism before sharing them with its neighbors; it then adopt cosine similarity to calibrate the received perturbed cross-gradients such that the aggregation of the calibrated cross-gradients can be utilized to effectively update local model in a momentum-like manner. Our rigorous theoretical analysis not only reveals the minimum noise level required to achieve a specific level of privacy preservation, but also illustrates that our algorithm still achieves a linear speedup in training with non-IID data. We finally conduct extensive experiments on real-world dataset to validate the effectiveness of our algorithm in defending privacy attacks and in training accurate models.

---


### 91. [Not All Errors Are Equal: Consequence-Aware Reasoning Compute Allocation](https://arxiv.org/abs/2606.04402)

**<font color=#1a73e8>作者：</font>** Jingbo Wen, Liang He, Ziqi He  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern reasoning models can allocate different amounts of test-time computation, such as thinking tokens, model calls, or compute budget, to different tasks. Existing methods generally drive this allocation by predicted difficulty and spend more compute where it is expected to raise accuracy. This implicitly assumes that all failures cost the same, since an accuracy objective weights every task equally. However, such an assumption does not hold in deployment: A typo in a log message and a migration that corrupts a production database both count as one benchmark failure, but their real-world costs are fundamentally different. To fill this gap, we propose consequence-aware test-time compute allocation. Instead of routing compute only by predicted difficulty, we use a lightweight predictor to estimate from the issue text how costly a task would be if solved incorrectly. The scheduler then routes higher-consequence tasks to larger compute tiers or higher thinking budgets under the same total budget. We conduct main experiments on SWE-bench Lite and evaluate cross-dataset behavior on Multi-SWE-bench mini, covering 700 software-engineering tasks in total. Our results reveal that consequence and difficulty are approximately orthogonal under various annotations, and that current thinking models do not allocate compute sufficiently according to consequence. Moreover, our issue-only predictor never misclassifies a high-consequence task as low-consequence across the 300 SWE-bench tasks. Under matched compute budgets, our consequence-aware scheduler reduces cost-weighted loss by 22% to 33% relative to difficulty-aware routing; in particular, the priority-aware variant, which routes by per-task cost scaled by the marginal-utility signal, crosses 30%, and its deployable predictor-driven version retains over 90% of the oracle gain.

---


### 92. [Low-Rank Decay for Grokking in Scale-Invariant Transformers: A Spectral-Geometric View](https://arxiv.org/abs/2606.04405)

**<font color=#1a73e8>作者：</font>** Mingyu Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern Transformer architectures frequently employ normalization mechanisms such as RMSNorm and Query-Key Normalization, making parts of the model approximately scale-invariant with respect to weight magnitudes. In this regime, standard Frobenius-norm weight decay acts purely along the radial direction of the weight space and cannot directly simplify the function represented by the normalized layer. We study grokking in small algorithmic tasks through this lens and propose \emph{Low-Rank Decay} (LRD), a nuclear-norm-like spectral regularizer whose subgradient -- the polar factor $UV^\top$ -- retains a tangential component even in the scale-invariant setting. This distinction has a concrete dynamical consequence: after the model memorizes the training set and task gradients vanish, L2 decay can no longer reshape the weight spectrum, whereas LRD continues to compress singular values in an $\ell_1$-like fashion. On modular arithmetic tasks, we find that LRD induces rapid effective-rank collapse in Query/Key matrices and expands the data-fraction boundary at which delayed generalization (grokking) occurs. We further provide a spectral-geometric interpretation through the ``needle-to-fan'' expansion of the nuclear-norm subdifferential near low-rank strata.

---


### 93. [An Ensembled Latent Factor Model via Differential Evolution and Gradient Descent Optimization](https://arxiv.org/abs/2606.04408)

**<font color=#1a73e8>作者：</font>** Rui Zhang, Jinhang Liu, Wenbo Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-dimensional and incomplete (HDI) data are prevalent in many real-world big data scenarios. Latent factor models serve as a common representation learning approach, capable of uncovering informative latent factors from such data. Nevertheless, most existing latent factor models rely solely on gradient descent for optimization, which may lead to insufficient and biased representations, particularly when dealing with heterogeneous HDI data. Thus, this study proposes an Ensembled Latent Factor Model via Differential Evolution and Gradient Descent Optimization (ELFM-DEGDO) with two-fold designed: 1) two diverse latent factor models are independently modeled via differential evolution and gradient descent optimization, respectively, and 2) the two diverse latent factor models are combined via a customized self-adaptive weighting mechanism to effectively fuse their strengths. By leveraging the complementary advantages of both optimization paradigms, ELFM-DEGDO is able to produce more comprehensive and less biased representations for HDI data. Three HDI datasets are tested to show that ELFM-DEGDO consistently performs better than related several latent factor models.

---


### 94. [An Empirical Study of Data Scale, Model Complexity, and Input Modalities in Visual Generalization](https://arxiv.org/abs/2606.04409)

**<font color=#1a73e8>作者：</font>** Luoyidi Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern deep neural networks usually have large parameter scales and nonlinear hierarchical structures, and they have achieved strong performance in computer vision. However, the source of their generalization performance remains difficult to explain using traditional statistical learning theory. Among the factors that may affect visual generalization, data scale, model complexity, and input modalities are fundamental and controllable variables. This study empirically analyzes how these three factors influence model generalization performance. Specifically, in a preliminary experiment, we construct a one-dimensional nonlinear function and vary the number of training samples and the polynomial degree to observe the effects of data scale and model complexity on model performance. In the main experiments, we compare model performance on CIFAR-10 and CIFAR-100 under different training data scales, model architectures, and input modalities. The experimental results show that increasing the training data scale consistently improves generalization performance, whereas changes in model complexity do not provide stable gains. In addition, removing color information degrades model performance, while explicit prior features such as gradients, edges, and wavelets have inconsistent effects across different model architectures. Overall, this study provides an empirical analysis of the relationships among data scale, model complexity, input modalities, and visual generalization performance. Code and experimental logs are available at: this https URL.

---


### 95. [Ultra-Fast Neural Video Compression](https://arxiv.org/abs/2606.04410)

**<font color=#1a73e8>作者：</font>** Jiahao Li, Wenxuan Xie, Zhaoyang Jia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While neural video codecs (NVCs) have demonstrated superior compression ratio, their prohibitive computational complexity remains a critical barrier to real-world deployment. This paper introduces a chunk-based coding framework designed to significantly improve the rate-distortion-complexity trade-off. Instead of processing frames sequentially, our approach encodes a chunk of multiple frames into a single compact latent representation and decodes them simultaneously. This is enabled by cross-frame interaction modules for joint spatial-temporal modeling and frame-specific decoders for parallel reconstruction. This paradigm not only dramatically enhances coding throughput but also facilitates more effective modeling of long-term temporal correlations. To further boost speed, we propose a streamlined entropy coding mechanism that consolidates bit-stream interactions into a single step, substantially reducing decoding overhead. Building on these innovations, we present DCVC-UF (Ultra-Fast), a new NVC that sets a new SOTA in performance. Our experiments show that DCVC-UF can achieve ultra-fast encoding and decoding speeds, significantly outperforming previous leading codecs. DCVC-UF serves as a notable landmark in the journey of NVC evolution. The code is at this https URL.

---


### 96. [Pepper: High-bandwidth and Scalable Anonymous Broadcast with Cryptographic Privacy](https://arxiv.org/abs/2606.04411)

**<font color=#1a73e8>作者：</font>** Chenghao Li, Haoyuan Wang, Xianghang Mi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present Pepper, a high-bandwidth anonymous broadcast protocol that provides cryptographic sender anonymity against global adversaries. Pepper builds on a two-server DC-net architecture but introduces three key innovations: a self-contained anonymous registration subprotocol using verifiable distributed point functions, support for batch messaging via distributed multi-point functions, and a lightweight access control mechanism based on secret-shared proofs. Unlike prior systems, Pepper eliminates the need for external dialing services and allows each broadcaster to send multiple messages per epoch with a single audit, significantly improving throughput for large data transfers. Our implementation demonstrates that Pepper achieves millisecond-level registration audits, scales efficiently to thousands of channels, and delivers 1.2--20$\times$ higher effective messaging rates than state-of-the-art alternatives. Furthermore, Pepper is designed for practical deployment, with natural compatibility for co-deployment alongside Tor and federated social networks.

---


### 97. [Motion-Guided Causal Disentanglement for Robust Multi-View Cine Cardiac MRI Diagnosis](https://arxiv.org/abs/2606.04414)

**<font color=#1a73e8>作者：</font>** Chuankai Xu, Cristiane De Carvalho Singulane, Mohammad Abuannadi 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-view cardiac magnetic resonance (CMR) imaging provides complementary anatomical information and is widely used for noninvasive disease assessment. Recent transformer-based models have demonstrated strong representation learning capabilities for CMR analysis; however, they typically learn unified latent embeddings that entangle view-specific anatomical variations with disease-related features. Such entanglement biases classifiers toward structural attributes rather than view-invariant pathological patterns. This issue is exacerbated in low-data regimes, particularly for underrepresented cardiac conditions, where limited samples increase the susceptibility to shortcut learning and view-dependent decision boundaries. To address this, we propose a Motion-Guided View--Disease Disentanglement framework MoViD built upon a ViT-MAE backbone. The model explicitly factorizes latent representations into view-specific and disease-discriminative components using dual-branch supervised contrastive objectives and a gradient-reversal adversarial constraint that minimizes disease leakage into the view embedding. Additionally, an annotation-free temporal motion feature, derived from inter-frame difference maps, is introduced to localize the beating heart region and suppress background artifacts. A focal reweighting mechanism is incorporated into the contrastive loss to mitigate class imbalance. We evaluate the framework on a private clinical venous thrombosis dataset and two public benchmarks (M&Ms, M&Ms2). Across disease classification and cardiac segmentation tasks, our approach consistently outperforms standard transformer baselines and demonstrates competitive performance against large-scale pretrained foundation models, validating the efficacy of structural disentanglement in medical image analysis.

---


### 98. [Loss-Conditional PINNs for Parametric PDE Families](https://arxiv.org/abs/2606.04420)

**<font color=#1a73e8>作者：</font>** Anna Lazareva, Alexander Tarakanov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) approximate solutions of ODEs and PDEs by minimising a weighted combination of residual, boundary, initial, and data losses. Their performance is often dominated by the choice of loss weights: a poor weighting can drive training to a degenerate solution in which one physical constraint is satisfied while another is ignored. Existing methods select or adapt a single good set of weights. We take a different view: instead of tuning one weight vector, we explore the entire weight space during training.
We introduce LC-PINN, which adapts the loss-conditional training of Dosovitskiy and Djolonga (2020) to the PDE-residual setting: the conditioning vector (either the loss weights or a scalar physical coefficient) is treated as a network input and sampled from a simple prior at every optimisation step. This turns PINN training into learning a continuous family of solutions indexed by that vector, with no solver-generated paired data. LC-PINN thus lies between classical PINNs and operator learning: it stays fully physics-informed but amortises training over a parametric family. Our contribution is not the loss-conditional construction itself, but its extension to PINNs, the unification of the loss-weight and parametric-coefficient regimes under one architecture (concatenation for loss weights, FiLM for coefficients), and a fixed-quadrature L-BFGS finishing protocol that makes the parametric-coefficient regime trainable.
We give a lambda-invariance result for the conditional optimum and study LC-PINN on parametric Helmholtz, Schrodinger, viscous Burgers, and Buckley-Leverett equations. A single LC-PINN matches or improves retrained per-weight PINN baselines while parameterising the full family in one model, at a total cost that amortises favourably against per-instance retraining.

---


### 99. [Trivium: Temporal Regret as a First-Class Objective for Causal-Memory Controllers](https://arxiv.org/abs/2606.04421)

**<font color=#1a73e8>作者：</font>** Edward Y. Chang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many current agentic systems and LLM pipelines correct mistakes by optimizing outcome reward. This addresses only the what of failure: when an outcome diverges from prediction, the why and when of the mismatch are not systematically logged, reviewed, or corrected, so the same error can recur episode after episode. We argue that this is a structural problem, not merely a model-capacity one. We propose long-horizon temporal regret as a first-class objective alongside outcome regret and epistemic regret over the working causal model. Temporal regret captures when failure persists: how long a miscalibrated causal model is tolerated before correction. Epistemic regret captures why failure persists: residual uncertainty or error in the working causal model. Together, the three regrets give a falsifiable account of what, why, and when a long-lived agent can fail. Modeling the agent as a stream of E episodes, we prove three conditional results under explicit causal-probing, persistence, and detectability assumptions. First, under observationally equivalent confounding, outcome-only learning cannot distinguish causal from spurious structure without an intervention channel, so temporal miscalibration can persist linearly even after outcome regret is driven to zero. Second, with a persistent causal log and budgeted probes, total probe complexity is logarithmic in the episode horizon, inducing O(log E) temporal regret. Third, under K detectable change-points, the rate extends to O(K log E). We instantiate Trivium and pre-register five falsifiable predictions. On CausalBench-Seq, Trivium follows the predicted logarithmic envelope while outcome-only baselines grow linearly. A pilot real-LLM stream provides preliminary external-validity evidence across one full E = 500 run and three E = 100 frontier-model pilots. Self-learning here means revising an external causal model, not retraining LLM weights.

---


### 100. [The price of multi-group transductive learning](https://arxiv.org/abs/2606.04423)

**<font color=#1a73e8>作者：</font>** Noah Bergam, Samuel Deng, Daniel Hsu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We show every multi-group learner in the transductive setting may incur a multiplicative penalty in its error rate on some group relative to the error rate achievable in the single-group setting, and the penalty can increasing linearly with the number of groups, up to roughly the square-root of the sample size. This stands in stark contrast to optimal multi-group learners in an analogous (group-realizable) statistical setting, where the penalty is always at most logarithmic in the sample size and independent of the number of groups.

---


> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-265](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
