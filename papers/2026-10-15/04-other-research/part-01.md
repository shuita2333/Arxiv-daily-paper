# 📦 其他研究 | 2026年10月15日

> 本类共 **810** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

---

### 1. [MDN-VJEPA: Multimodal Probabilistic Joint-Embedding World Models](https://arxiv.org/abs/2610.13956)

**<font color=#1a73e8>作者：</font>** Yongchao Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Joint-Embedding Predictive Architectures (JEPAs) learn world models by predicting future representations rather than reconstructing observations. Variational JEPA (VJEPA) gives this prediction probabilistic semantics and permits flexible conditional predictive families. We propose MDN-VJEPA, a multimodal probabilistic JEPA that instantiates the latent predictor as a mixture density network (MDN), representing future states with a Gaussian mixture whose components encode alternative futures, their probabilities, and within-mode uncertainty. For sequential prediction, we address two additional structural requirements: multi-modal futures should remain temporally coherent across a trajectory, and predictive beliefs should remain consistent when propagated to the same horizon through different temporal path compositions, as motivated by the Chapman--Kolmogorov equation. Together, these considerations define a three-level hierarchy of multimodal prediction, coherent multimodal trajectories, and compositionally consistent multimodal dynamics. Controlled experiments show that MDN-VJEPA closely recovers known branching predictive laws, that retaining the complete multimodal belief rather than its conditional mean can lead to materially different and substantially better planning decisions under branching futures, and that trajectory-level coupling and distributional consistency improve temporal coherence and multi-horizon agreement. These results support a simple principle: a probabilistic JEPA should preserve not only how uncertain the future is, but which distinct futures constitute that uncertainty, how they form coherent trajectories, and how those beliefs compose through time.

---


### 2. [MRFlow: Mechanism-Structured Residual Flow Matching for Virtual Cell Perturbation Prediction](https://arxiv.org/abs/2610.13966)

**<font color=#1a73e8>作者：</font>** Haojie Yang, Ran Su  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting cellular responses to chemical and genetic perturbations is a central test for AI virtual cells, yet many single-cell models reduce each condition to an average expression shift. This target is misaligned with perturbation biology: rare states, resistant subpopulations, and context-dependent effect sizes may coexist under the same intervention. MRFlow treats virtual-cell prediction as conditional transport between empirical single-cell measures. Control and perturbed cells are embedded in a variational latent state space, greedy low-cost supervision is constructed over detached minibatch states, and a conditional flow-matching vector field transports control populations toward perturbed populations. The field decomposes into a mechanism-structured affine dictionary, which recombines shared latent response operators with a low-rank condition-specific correction, and a spectrally controlled residual field for nonlinear cell-level variation. Genetic perturbations are encoded through a regulatory-graph GCN, chemical perturbations through Morgan fingerprints, and both enter the same conditional dynamics interface. Across eight gene and drug perturbation benchmarks, MRFlow attains the highest composite score while preserving competitive raw performance on differential-expression and distributional metrics. The results support latent distribution transport as a principled and empirically effective formulation for perturbation-aware virtual cell modeling.

---


### 3. [Predict Before You Modify: Learning Improvement Dynamics for Self-Evolving Agents](https://arxiv.org/abs/2610.13991)

**<font color=#1a73e8>作者：</font>** Zixuan Xie, Chang Xu, Yuhua Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-evolving agents improve through repeated cycles of modification and evaluation. However, existing methods receive feedback on modifications only after costly evaluations, and aggregate scores may obscure distinctions between failures that require different repairs. We introduce predictive self-evolution through an editable Improvement Dynamics Model (IDM). Before evaluation, the IDM predicts task-level outcomes of a proposed modification and guides an optional revision. After evaluation, past modifications and their observed outcomes are used to improve the IDM, allowing predictive knowledge to accumulate across generations. The system can thus improve how it solves tasks, proposes modifications, and predicts their effects. Building on HyperAgents, we evaluate this approach across multilingual coding, paper review, robotics reward design, and Olympiad-level mathematical grading. Our approach outperforms HyperAgents across all four domains, with up to 46% higher average performance over generations. Gains also persist under matched token budgets that include both agent evolution and task evaluation, and extend to held-out tasks. Forecast accuracy improves as the IDM evolves, and the learned predictive knowledge transfers to improve evolution in a new domain.

---


### 4. [How Vision Transformers Represent Position: A Mechanistic Comparison of Absolute and Rotary Positional Encodings](https://arxiv.org/abs/2610.13992)

**<font color=#1a73e8>作者：</font>** Mahmoud Mannes, Nikhil Maturi, Parva Mehta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Positional embeddings encode the spatial position of each image patch in a Vision Transformer (ViT), allowing the model to distinguish different spatial arrangements of visual content. However, we know little about how the choice of embedding shapes a vision transformer's internal representation. In this work, we show that Absolute Positional Embeddings (APE) and Rotary Positional Embeddings (RoPE) encode spatial position through different internal mechanisms: APE stores position in explicit features, while RoPE builds it inside attention and rebuilds it when it is withheld. Specifically, in APE models, sparse autoencoders recover causal row- and column-specific features, whereas interventions on RoPE reveal distinct rotary components that separately encode row and column information. Additionally, causal interventions selectively disabling RoPE's row or column rotations show that decodable row and column information can be independently removed and, once rotations are restored, partly reconstructed, in part by axis-specialized attention heads. Both mechanisms are causally important for classification: permuting APE's positional features across patches reduces top-1 accuracy by 24--31 points, and ablating the rotations of RoPE's primary rebuilding head reduces it more than ablating those of any other head. Our findings show that the choice of positional encoding fundamentally changes how spatial information is organized and processed inside Vision Transformers. More broadly, our work demonstrates how mechanistic analysis can reveal how models construct, reconstruct, and maintain structured representations, providing a basis for targeted interventions in vision models.

---


### 5. [Posterior Flow Matching](https://arxiv.org/abs/2610.13994)

**<font color=#1a73e8>作者：</font>** Chenrui Ma, Xi Xiao, Lin Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow matching learns how to transport noise toward data, but its mean prediction does not directly report the endpoint uncertainty remaining at an intermediate state. This paper introduces Posterior Flow Matching (PFM), a general generative modeling framework that learns conditional velocity means and componentwise variances with a Gaussian posterior model. The same model evaluation supplies both a transport prediction and endpoint uncertainty, making posterior diagnostics available throughout generation. These learned moments support a mean-driven ordinary differential equation (ODE) and a posterior-driven stochastic differential equation (SDE), whose local noise scales adapt to the predicted uncertainty. Across image, point-cloud, molecular, and action generation, PFM improves generation quality and provides endpoint-posterior readouts throughout generation.

---


### 6. [SharedSAE: a unified sparse dictionary across u-net blocks and denoising time for diffusion models](https://arxiv.org/abs/2610.13997)

**<font color=#1a73e8>作者：</font>** Longhao Lei, Lan Yao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept representations in diffusion models drift across network depth and denoising time, yet existing sparse autoencoders offer only per-block or per-timestep dictionaries, leaving no single feature dictionary for localization and intervention in the network. We present Shared Sparse Autoencoder (SharedSAE), which learns one sparse dictionary shared across four U-Net attention blocks and all 50 denoising steps of SDXL 1.0. A block-specific low-rank input adapter aligns the residual distribution of each block before the shared encoder, and a temporal conditioning module with a shared timestep branch and a block-timestep correction branch absorbs temporal non-stationarity. Despite spanning both axes, Shared SAE preserves a coherent dictionary structure. Built on the shared dictionary, localized feature suppression reduces the number of NudeNet-positive generations in the I2P detector-positive subset from 139 to 1. Tracing sparse features across the trajectory further reveals that concept representations are redistributed across U-Net blocks during generation, shifting from the earliest downsampling block toward intermediate and later blocks as denoising proceeds. SharedSAE thus provides a unified, interpretable, and intervention-ready representation space for diffusion models, enabling concept analysis and erasure at any covered block and denoising step.

---


### 7. [Enhanced Trading Systems with Intelligent Market Analysis](https://arxiv.org/abs/2610.13998)

**<font color=#1a73e8>作者：</font>** Vedanth Padmaraman, Shreen Anand, Vamshi Vishruth J 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes a hybrid reinforcement learning trading framework integrating intraday market data with transformer-based financial sentiment signals. The system extracts sentiment dynamics and semantic event clusters from financial news and incorporates them into a PPO-based trading agent. Experiments on intraday NSE data demonstrate improved risk-adjusted returns compared to price-only baselines.

---


### 8. [Showing versus Doing: Teaching by Demonstration](https://arxiv.org/abs/2610.14004)

**<font color=#1a73e8>作者：</font>** Mark K. Ho, Michael L. Littman, James MacGlashan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> People often learn from others' demonstrations, and inverse reinforcement learning (IRL) techniques have realized this capacity in machines. In contrast, teaching by demonstration has been less well studied computationally. Here, we develop a Bayesian model for teaching by demonstration. Stark differences arise when demonstrators are intentionally teaching (i.e. showing) a task versus simply performing (i.e. doing) a task. In two experiments, we show that human participants modify their teaching behavior consistent with the predictions of our model. Further, we show that even standard IRL algorithms benefit when learning from showing versus doing.

---


### 9. [Generalized PINN-Based Inverse Estimation of Spatially Varying Heat Transfer Coefficients with Transfer Learning](https://arxiv.org/abs/2610.14008)

**<font color=#1a73e8>作者：</font>** Pradipan Maitra, Jariful Hassan, Arijit Hazra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study investigates generalized boundary representations and transfer learning for physics-informed neural-network (PINN) estimation of spatially varying convective heat transfer coefficients (HTCs) in jet impingement cooling. Piecewise-linear (PWL) and neural-network boundary estimators are inferred from transient interior-temperature measurements and evaluated against CFD-CHT reference HTC profiles at Reynolds numbers of 5000, 10000 and 15000. A discrete Adjoint-FEM formulation with gradient regularization based on the $H^1$-seminorm provides an independent inverse-method comparison. Transfer learning is investigated under two source-target conditions: transfer between noise levels at the same Reynolds number, and transfer from a controlled Gaussian-profile problem to CFD-CHT-derived target problems at different Reynolds numbers. For the representative Re = 5000 target with 5% measurement noise, quadratic, PWL, and neural-network PINNs achieve relative HTC-profile errors of 5.08, 5.31 and 5.19%, respectively, while generalized representations reduce the error for the Re = 15000 target from 16.76% for the quadratic PINN to 14.41% and 14.46%. Transfer learning reduces target-training time by 57.86-81.71% for fixed-Reynolds-number transfer and by 50.59-84.94% for Gaussian-to-CHT transfer. Its effect on reconstruction accuracy is target dependent: fixed-profile PWL transfer remains within 0.30 percentage points of scratch training, whereas Gaussian-to-CHT transfer produces differences of 0.10-1.52 percentage points across targets and representations. These results demonstrate that generalized PINN representations can accommodate spatially varying HTC profiles without a prescribed quadratic form, while transfer learning can substantially reduce target-training cost for repeated inverse estimation, with the resulting reconstruction accuracy depending on source-target compatibility.

---


### 10. [SIRNET: Causal Adaptation of Pretrained Embeddings for Semiparametric Treatment-Effect Estimation Under Surrogacy](https://arxiv.org/abs/2610.14011)

**<font color=#1a73e8>作者：</font>** Lei Shi, Qiuran Lyu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern experiments increasingly produce rich post-treatment objects---such as text, images, and video---that may provide early surrogate signals for outcomes that are delayed, expensive, or observed only for a subset of participants. A pretrained encoder can turn such an object into a strong generic embedding, but the embedding is not trained for the estimation tasks required by a causal estimator and may emphasize information irrelevant to the causal target. We propose SIRNET, a Surrogate-Informed Representation adaptation framework for neural-NETwork-based causal estimation in the presence of unstructured post-treatment surrogates. Starting from pretrained surrogate embeddings, SIRNET learns a shared adapter jointly for outcome prediction, treatment propensity, and arm-specific surrogate marginalization, beyond the generic pretraining objective. The resulting covariate and surrogate representations provide a common interface for these nuisance tasks. The final treatment-effect estimate and confidence interval are obtained from cross-fitted orthogonal scores that attain the semiparametric efficiency bound under the stated nuisance-rate conditions. We also validate SIRNET's performance in synthetic and semisynthetic experiments, as well as the Anti-Amyloid in Asymptomatic Alzheimer's Disease (A4) trial, using frozen pretrained brain-MRI embeddings as surrogates for a long-term outcome.

---


### 11. [Perfect Reconstruction Cannot Show Whether Two Codebooks on a VAE's Latent Space Agree](https://arxiv.org/abs/2610.14012)

**<font color=#1a73e8>作者：</font>** Yusuke Hayashi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many systems read the latent space of a variational autoencoder (VAE) as discrete codes, and rely on each latent being read back as the code it was written as. Shannon (1948) took such a shared codebook as given; inside a VAE nothing enforces it. We prove that no item of a standard training report can reveal whether the written and read codes agree on encoded data. We construct two VAEs that reconstruct every input perfectly, infer exactly, and match on every per-example ELBO and every code histogram, yet agreement is one in the first and zero in the second. We then show that the ELBO's own terms bound how far a measured agreement can move: the variational gap bounds the shift to exact inference, and the rate bounds the shift to generation from the prior. For Gaussian posteriors, a mean-field encoder pays an exact price in the gap that depends on its choice of axes. On probabilistic PCA the gap certifies a trained encoder in all 75 settings we test, at agreement between 0.76 and 0.97. On 240 trained VAEs, a floor set by the rate and the dataset size rules out rate-side certification in advance for 66 models, and none of them certifies. The results yield a simple protocol, Certify-or-Measure, for any pipeline that reads a VAE as codes.

---


### 12. [Physics-Informed State Space Models for Day-Ahead Photovoltaic Power Forecasting](https://arxiv.org/abs/2610.14014)

**<font color=#1a73e8>作者：</font>** Phil Aupke, Muhammad Hassan, Khalid Ali 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate day-ahead photovoltaic (PV) power forecasting requires both strong temporal modeling and adherence to physical PV system constraints. Purely data-driven models often ignore the underlying PV conversion process and may produce predictions that are outside the operational range of a PV system. In this paper, we propose a physics-informed state space framework that combines a differentiable PV conversion model with a selective state space backbone (PowerMamba). Our approach follows a physics-residual decomposition. The physics module provides a structured baseline based on solar geometry, irradiance, temperature effects, and inverter limits, while the state space model learns residual corrections from numerical weather prediction (NWP) inputs over a 24-hour horizon. Experiments on one year of utility-scale PV data show that the proposed method significantly improves forecasting accuracy, reducing RMSE by 38.5% and MAE by 45.8% compared to a physics-only baseline, and outperforming a purely data-driven model. Results further show that incorporating system-level physics provides the largest performance gains, while additional refinements offer only marginal improvements. Beyond accuracy, the model improves robustness by constraining predictions toward physical feasibility, reducing unrealistic predictions under corrupted measurements.

---


### 13. [DShuttleNet: A Badminton Doubles Dataset for Evaluating Team Coordination](https://arxiv.org/abs/2610.14016)

**<font color=#1a73e8>作者：</font>** Guan-Yi Jhang, Chiencheng Chiang, Wei-Kai Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most existing sports datasets are individual-centric or ball-centric, focusing on individual player actions while ignoring interactions among teammates. In badminton doubles, tactical success is governed by rapid team formation and coordination, yet standard resources for modeling these player interactions are scarce. To bridge this gap, we present DShuttleNet, a comprehensive dataset for badminton doubles curated from elite BWF World Tour tournaments. Beyond trajectory data, DShuttleNet uniquely incorporates expert-labeled "Loss Reasons," transforming the dataset into a diagnostic tool for causal tactical evaluation. We formally define two geometry-driven representations, Teammate-Relative Angle (TRA) and Vertical Shot Angle (VSA), to characterize coordination and shot aggressiveness. To quantify interpersonal synergy, we introduce novel metrics, Court Coverage Efficacy Index (CCEI) and Threat Load Asymmetry Index (TLAI), which evaluate the often-overlooked non-hitting partner's role and defensive coordination. Experimental results demonstrate that conventional models suffer from underfitting when failing to incorporate these coordination-centric features, highlighting the critical importance and potential impact of releasing DShuttleNet. Dataset is available at: this https URL.

---


### 14. [Barycentric Anchored Weight Search for Robust Model Merging](https://arxiv.org/abs/2610.14017)

**<font color=#1a73e8>作者：</font>** Antoni Buades, Jose-Luis Lisani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose Barycentric Anchored Search, a post-hoc weight-space procedure for improving fine-tuned vision models under distribution shift without additional gradient training or increased inference cost. Given a pre-trained initialization and two checkpoints fine-tuned on a source dataset, the method constructs barycentric candidate weights and performs a small derivative-free search along directions connecting each candidate to the pre-trained model. Candidate weights are selected using a small validation subset of one or more out-of-distribution (OOD) datasets; the selected model is then evaluated on the held-out portions of those datasets, on additional OOD benchmarks, and on the ImageNet validation set to quantify the robustness-accuracy trade-off. The method is inspired by simplex-based derivative-free optimization, including Nelder-Mead and Torczon multidirectional search, but is specialized to the geometry of neural network weight merging. Unlike Model Soup, which typically benefits from many fine-tuned checkpoints, and unlike Model Stock, which applies a fixed geometric merge, our approach uses only two fine-tuned checkpoints and iteratively adapts the merge using validation feedback from OOD data. Experiments with CLIP ViT-B/32 show that the proposed search substantially improves performance on held-out OOD data, including ImageNet-A, ImageNet-R, and ImageNet-Sketch, while keeping ImageNet accuracy competitive. The resulting weights also improve transfer to OOD datasets not used during candidate selection, outperforming the original fine-tuned checkpoints, naive model soups, and Model Stock in our evaluations. These results suggest that lightweight optimization in anchored weight space provides a practical alternative to fixed weight-averaging rules, geometric merging, or single-model selection.

---


### 15. [Argos: A Multi-Tenant SaaS Architecture for Distributed Edge Security Orchestration](https://arxiv.org/abs/2610.14019)

**<font color=#1a73e8>作者：</font>** Agustin Javier Di Bartolo, Mohammadhossein Homaei, Andres Caro 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The growing adoption of distributed edge devices for security auditing and operational monitoring exposes limitations in lightweight control mechanisms traditionally used to manage such nodes. While commercial Command-and-Control (C2) platforms offer advanced orchestration features, their licensing constraints, operational complexity, and proprietary nature limit accessibility for small and medium-sized enterprises and research environments. This paper presents Argos, a multi-tenant SaaS C2 architecture designed for transparent, automated, and long-term orchestration of distributed edge devices. The framework implements a structured control plane with role-based access control (RBAC), tenant isolation, persistent task management, and cron-based workflow automation. Unlike operator-driven or stateless execution models, Argos enables scheduled and autonomous coordination of security tasks across heterogeneous environments. To formally substantiate its isolation guarantees, the platform is modeled through a set-theoretic authorization framework, and a tenant non-interference property is proven. The proposed architecture was evaluated across three geographically distributed edge devices, executing 810 automated tasks mapped to MITRE ATT&CK techniques. Results demonstrate a global failure rate of 3.33% (95% Wilson confidence interval: [2.30%, 4.81%]) with no statistically significant difference across ARM and x86 architectures (\c{hi} 2 = 1.55, p = 0.21), and stable operation under heterogeneous latency conditions, including intercontinental deployments. To ensure scientific transparency and reproducibility, the evaluation methodology, sanitized datasets, and statistical scripts have been made publicly available in an open-source repository.

---


### 16. [CoEvoke: Evoking Multi-Agent Collaboration for Trajectory Collection](https://arxiv.org/abs/2610.14021)

**<font color=#1a73e8>作者：</font>** Lin Wu, Shu Yao, Yuheng Wang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training multi-agent collaboration requires trajectories of checking, feedback, and repair, yet task-solving rollouts may end in immediate approval or repeat unsuccessful attempts without useful correction. We introduce CoEvoke, a cross-domain framework that evokes these interactions during trajectory collection. Controlled perturbations create recoverable difficulties, while restricted reference-based guidance directs investigation. The resulting dataset contains 4,567 reconstructable trajectories over 4,130 software-engineering and reasoning tasks, linking public interactions to evidence, decisions, and task-native outcomes. Separate experiments over 2,287 same-task pairs show feedback increases of 47.72-100 percentage points across seven perturbation groups; guidance has smaller, model-dependent effects. With identical training tasks, decision-record counts, and updates, perturbation-enriched judge training improves ACPBench-Hard success from 35.38% to 42.12% (+6.73 points). SWE verifier training gains 7.60-9.40 points over interface-matched untrained references. Workflow and post-training evaluations preserve task-solving topology with unperturbed inputs and no private-reference guidance. These results support designing collection conditions to obtain corrective supervision that improves collaborative decisions with frozen solving agents.

---


### 17. [Historical Anchors for Scientific Forecasting on Human-Aware Knowledge Graphs](https://arxiv.org/abs/2610.14023)

**<font color=#1a73e8>作者：</font>** Siu Tin Wu, Ryan C. Barron, Phoebe Upton Sanderbeck 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting which scientific connections will form next can point researchers toward the most promising leads. One successful approach learns representations by sampling paths through publication networks, represented by a hypergraph, that connect scientific entities, concepts, and researchers, approximating how knowledge and expertise move through the literature. Sampled paths are then used to train an embedding model to forecast scientific connections such as a property of a material. Performance, however, depends strongly on how many paths are sampled: too little sampling yields incomplete representations, while further sampling can eventually weaken prediction quality. The best sampling budget is therefore often identifiable only after future discoveries are known. We introduce Query--Anchor Agreement (QAA), a diagnostic requiring no future labels or separately trained model. QAA can be used to select a sampling budget, and refine or re-rank the resulting forecast to improve forecasting scientific connections. QAA compares the candidates a model predicts for a target with those most similar to the target's known historical examples, and identifies when these two views converge. Across thermoelectric-material and COVID-19 drug-repurposing benchmarks, repeated random-seed runs, and three sampling policies, QAA-selected budgets fall on average 1.86 percentage points below hindsight-optimal selection for broad candidate recovery. Further, promoting candidates supported by both views, under a capped fusion that bounds the anchor contribution, improves broad recovery across all six benchmark-policy settings, which define the types of network walks used for sampling.

---


### 18. [Rotate the Loop: Blockwise Conformality for Looped Transformers](https://arxiv.org/abs/2610.14030)

**<font color=#1a73e8>作者：</font>** Alexey Zemtsov, Albina Klepach, Vadim Lomshakov 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped transformers reuse one shared block across many recurrent steps, so depth becomes a quantity that can be spent at runtime rather than a stack of distinct layers. Those extra steps help only if a write made on one recurrent step is still readable on later ones, and that depends on the linear map applied to the residual between recurrent steps. We show that whether the loop learns to track state is a geometric question about the form of this map, and we propose blockwise conformal injections: the residual splits into coordinate-aligned groups and rotates inside each one, so every group has its own timescale while the geometry stays exact within it. Our experiments show a performance increase on a demanding form of state tracking - last-token accuracy when the rest of the prefix is already correct - and on language modelling, where a signal written earlier has to be retrieved at the end of the sequence.

---


### 19. [PLDiv: Measuring Dataset Diversity and Semantic Collapse via Persistence Landscapes](https://arxiv.org/abs/2610.14031)

**<font color=#1a73e8>作者：</font>** Yang Ba, Michelle V. Mancenido, Rong Pan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern data pipelines increasingly combine human-created and human-curated data with AI-generated data for model training and evaluation. As datasets grow, they often add semantically redundant samples rather than expanding semantic coverage, which deteriorates the quality of the whole dataset. Existing diversity metrics primarily summarize lexical variation, entropy, or pairwise similarity, but provide limited characterization of the shape of the underlying data distribution. In this paper, we propose PLDiv, a diversity metric derived from persistence landscapes that quantifies the structural organization of a dataset from its geometric representation. PLDiv summarizes how data neighborhoods evolve as nearby samples progressively connect, producing an interpretable scalar measure of structural diversity without requiring task-specific supervision. Whether measuring intrinsic diversity in text generations or image embeddings, or detecting semantic collapse in instruction datasets and reasoning trajectories, PLDiv performs competitively against evaluated baselines and aligns strongly with diversity labels during semantic collapse. Consequently, it effectively supports applications in synthetic data monitoring, dataset construction, data augmentation, and generative model evaluation.

---


### 20. [Symmetric Cryptography via Dirichlet Convolution](https://arxiv.org/abs/2610.14040)

**<font color=#1a73e8>作者：</font>** Artur Sowa, Elias Hassani Sangani, Francis Bui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We discuss a new symmetric-key cipher for digital data encryption. Its implementation is fast, memory efficient, and resilient against classical, AI-assisted, and quantum attacks.
Let $x$, $k$, and $c$ be elements of a finite abelian group $G$ with operation $+$ and neutral element $0$. Suppose one is given ciphertext $c=x+k$. Retrieving the plaintext $x=c-k$ from the ciphertext is trivial when the key $k$ is known. Without the key, however, recovering $x$ amounts to a blind search. Even if an efficient criterion were available for identifying the plaintext among all group elements, the average number of trials would remain prohibitively large when the group is sufficiently large. The challenge in constructing a practical cryptosystem is therefore to identify a sufficiently rich group $G$, together with efficient algorithms that enable an immersion of \emph{real digital data} into $G$ and efficient evaluation of the group operations.
The proposed cipher is based on generalized Dirichlet convolution over finite fields. We investigate its security against plaintext attacks from an information-theoretic perspective. The nonlocal structure of Dirichlet convolution naturally permits plaintext salting, providing protection against plaintext attacks while allowing controlled key reuse. We establish perfect masking properties over finite fields and prove that the resulting cipher achieves information-theoretic security under key reuse when the underlying arithmetic is carried out in $\mathbb{F}_p$ with $p>2$. For arithmetic over $\mathbb{F}_2$, some information leakage remains, leading to a finite key-reuse budget.

---


### 21. [A Geometric Perspective on Reward Function Updates in Inverse Reinforcement Learning](https://arxiv.org/abs/2610.14041)

**<font color=#1a73e8>作者：</font>** Anish Diwan, Jan Peters, Oleg Arenz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inverse Reinforcement Learning (IRL) is classically solved using Lagrangian optimisation, by jointly optimising a primal-dual problem with gradient descent to obtain the optimal reward function parameters and corresponding optimal policy. While this algorithmic view of IRL has been highly influential, gradient-based reward updates only paint a partial picture, largely ignoring the geometry of the problem in occupancy space. In this paper, we present an occupancy-space view of reward updates in IRL. We leverage the insight that both the optimal solution and its geometry in occupancy space are known, and show that the geometry along the e-geodesic (straight line in occupancy space) toward the optimal occupancy directly affects the gradient of the IRL dual problem in reward parameter space. This perspective naturally suggests preconditioning the dual gradient with the average Fisher information along the occupancy trajectory. We show that this preconditioned gradient is just a convex interpolation of the old reward and a new target reward, yielding efficient natural-gradient-style updates with little additional computational overhead. We then analyse these occupancy-space reward updates from a Mirror Descent (MD) perspective, and show that policy search over the resulting rewards induces approximate entropic MD on the policy. Finally, we conclude with convergence results of such geometry-aware IRL algorithms.

---


### 22. [Pristine Models](https://arxiv.org/abs/2610.14091)

**<font color=#1a73e8>作者：</font>** Anirudh Sundara Rajan, Krishna Kumar Singh, Richard Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training on broad, unfiltered data enables high-quality image generation, but can also teach models concepts that should not be generated; restricting the training data ensures safety, but reduces quality because examples containing unsafe concepts also provide useful knowledge that is not itself unsafe. Existing approaches largely address this trade-off post hoc through concept unlearning, which can lead to catastrophic forgetting as the number of concepts to remove grows. We instead ask whether unsafe concept knowledge can be compartmentalized during pretraining so that access to it can be disabled at inference. We introduce Pristine Models, a novel text-to-image generation architecture with an attention mechanism that encourages the separation of safe and unsafe knowledge into independently parameterized branches. The branch-specific parameters are learned during training, while the unsafe branch can be detached at inference. On ImageNet, Pristine Models enable safer generation while retaining much of the utility of full-data pretraining, achieving higher image quality and better text alignment than training only on safe data or applying post-hoc concept removal. We further scale our approach to CC12M, demonstrating that it remains effective in a substantially larger and more diverse open-world pretraining setting.

---


### 23. [Human Pose Estimation by Probabilistic Mixtures of Gaussian and Uniform Distributions](https://arxiv.org/abs/2610.14093)

**<font color=#1a73e8>作者：</font>** Santiago Reina Alguacil, Ezequiel López Rubio  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite advancements in sub-pixel decoding, modern Human Pose Estimation (HPE) architectures remain constrained by deterministic coordinate extraction from discrete heatmaps, which systematically fails under dense occlusions and Out-of-Distribution (OoD) ambiguities. To address these limitations, we propose a post-hoc continuous probabilistic framework that intercepts raw heatmaps and models them as a Gaussian Mixture Model (GMM) augmented with a spatially agnostic uniform distribution, requiring no architectural modifications or retraining. This continuous representation allows us to comprehensively explore the distinct contributions of density modeling to HPE. We show that the spatial expectation of our fitted GMM achieves precision parity with leading sub-pixel decoders without heuristic post-processing. Leveraging this continuous space, our test-time augmentation aggregates probability distributions rather than discrete activations, mitigating multi-scale heatmap poisoning. Furthermore, because our multimodal GMM parameterization isolates competing spatial hypotheses, it naturally interfaces with geometric regularizers such as Markov Random Fields. However, our analysis exposes the inherent vulnerabilities of 2D kinematic priors under perspective foreshortening and visual degradation. Crucially, this density formulation yields significant improvements in uncertainty quantification: our calibrated geometric covariance volume outperforms standard peak-intensity heuristics in OoD anomaly detection under severe occlusion. For in-distribution calibration, dynamically fusing our geometric metric via Adaptive Softmax reduces or matches baseline Area Under the Sparsification Error (AUSE) across benchmarks and degradation levels. Finally, we establish that this continuous parameterization is extensible to multi-view 3D architectures, bypassing the $\mathcal{O}(N^3)$ voxel memory bottleneck.

---


### 24. [A Physics-Informed Hybrid Forward-Inverse Machine Learning Framework for High-Dimensional Sparse Recipe Reconstruction](https://arxiv.org/abs/2610.14097)

**<font color=#1a73e8>作者：</font>** Md. Muqtadir Fuad, Md. Istiak Adnan, Ridwan Al Aziz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-dimensional sparse recipe formulation in process industries involves nonlinear association of various covariates, bounded by sparsity constraints and multi-criteria tolerances. Traditional physics-based classical methods (such as Kubelka-Munk) fail to generate sparse candidate recipes properly due to their simplified assumptions and industrial process variations. This study proposes a hybrid physics-informed uncertainty-aware framework that is structured into three modules: (a) Module A, a multi-target forward quality model; (b) Module B, a sparse inverse reconstructor; and (c) Module C, a feasibility-constrained ranking layer. Then it has been validated in an industrial textile dyeing context with recipe-grouped cross-validation under multi-illuminant quality assessment comprising process and production information, target reflectance, K/S values, and spectral descriptors. Histogram Gradient Boosting (HGB) with spectral-only features ($R_\lambda$, K/S) and Gradient Boosting Regressor (GBDT) with recipe-process features outperforms other configurations with out-of-Fold MAE of 0.1655 and 0.1523 in the forward quality model. For inverse reconstruction, a component-wise median blend achieved a recipe-vector MAE of 0.0295. Exploratory conditional treatment effect (CATE) suggests an observational association that alkali adjustment reduces error for red and pale shades (CATE = -0.196). This framework provides a human-in-the-loop decision-support tool that minimizes costly laboratory trials across industrial formulation domains.

---


### 25. [From Prototype to Massing: Learning Graph Correspondence for Scalable Facade Modeling](https://arxiv.org/abs/2610.14098)

**<font color=#1a73e8>作者：</font>** Yiliang Shao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Facade articulation at building scale is usually resolved manually or through parametric systems that encode design intent as explicit rules. This paper investigates a complementary workflow in which a designer-authored prototype supplies transferable articulation logic. Prototype and target massing are represented as heterogeneous attributed graphs, and a Siamese graph attention network with instance-local triplet supervision embeds their segments in a shared metric space. Many-to-one nearest-neighbor retrieval then routes prototype Patterns to the larger target. On the original 85/15 within-corpus holdout, prototype-to-massing top-1 accuracy reached 96.5%, compared with a reported 76.5% raw-feature baseline. A Rhino demonstrator converts predicted correspondence into reusable facade Patterns, and qualitative applications on four built projects show the workflow across distinct massing organizations. The contribution is not automated facade generation, but an authoring model in which resolved geometry serves as a computational specification for project-scale propagation.

---


### 26. [An Empirical Case Study of Prompt Engineering Strategies for Bypassing Multi-Layer Agent Security Defenses](https://arxiv.org/abs/2610.14116)

**<font color=#1a73e8>作者：</font>** Chengwei Chu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The OpenClaw Security Attack and Defense Challenge evaluates AI agent robustness through a three-stage defense pipeline: skill file scanning (Stage 1), instruction safety evaluation (Stage 2), and attack trajectory scoring (Stage 3). This paper presents an empirical case study of prompt engineering strategies against these layers across 19 attack targets in Enterprise OA, E-commerce, and Smart Home scenarios. I document both successful and failed strategies, with an emphasis on the observed trade-off between instruction safety (Stage 2) and attack execution accuracy (Stage 3). The final online score is 0.2630, with 5 of 19 tasks achieving full bypass. The results suggest that multi-layer defenses, reinforced by built-in behavioral constraints, substantially limit what prompt engineering alone can achieve.

---


### 27. [TrustPaper for forged PDF with Issuer Fingerprints](https://arxiv.org/abs/2610.14132)

**<font color=#1a73e8>作者：</font>** Yassine El Jakani, Mohamed Nadir Rhazi, Othmane Meknassi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Sick leave certificates are increasingly delivered as PDF files by online teleconsultation platforms, and can be altered in minutes with free editors. Generic PDF scanners report how a file was built, but cannot tell whether that construction is legitimate: an incremental update, an embedded font or a given producer string is normal for one issuer and anomalous for another. We present TrustPaper solution, an issuer aware forensic approach that combines three elements: the claimed issuer of the document, a reference fingerprint learned beforehand from genuine documents of that issuer, and an explainable combination of evidence from several forensic modules. Fingerprints are stored as versioned declarative profiles, and every anomaly keeps its observed value, expected value and triggering rule. We formalize the threat model, the fingerprint and the scoring model, and evaluate the open-source prototype on a controlled corpus documents from two issuers and six forgery techniques. With the issuer fingerprint, all forgeries made by opportunistic and metadata-aware attackers are flagged with no false positive on genuine test documents.

---


### 28. [Correction Training for Diffusion Models](https://arxiv.org/abs/2610.14136)

**<font color=#1a73e8>作者：</font>** Donghoon Ahn, Runqian Wang, Alexei A. Efros 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Iterative sampling in diffusion models can lead to error accumulation due to exposure bias. The denoiser is trained on real images interpolated with noise, but at inference its inputs are constructed from its own imperfect predictions from the earlier steps, something it has never seen at training time. This might be one reason diffusion models often struggle without additional help, such as CFG. We introduce a correction step for diffusion models which attempts to reduce this training-inference gap. The corrector takes the base model's prediction as input and is trained against the same ground-truth target. This makes correction an explicit learning task, with training inputs provided by the base model. During sampling, at each denoising step, we iteratively refine the denoiser's clean-sample prediction. This allows us to correct predictions at intermediate denoising steps, preventing early artifacts from persisting into the final sample. Although the corrector is trained only on predictions from the base denoiser, it can be applied repeatedly to its own outputs at inference for better results. This simple framework leads to substantial improvement in sample quality while largely preserving diversity. We evaluate our method across DiT, SiT, and JiT. Our method substantially improves upon previously reported FID scores for unguided generation and, notably, unconditional generation, where producing high-quality samples without guidance has been particularly challenging. Our method achieves performance competitive with classifier-free guidance (CFG), and combining correction with CFG further improves diversity and reduces oversaturation typical of CFG. Finally, we show that the additional inference cost of correction can be amortized by distilling the refined predictions back into the base diffusion model, retaining the quality gains without additional inference-time overhead.

---


### 29. [Memory-Coupled Unlearning for Data-Absent Identity Forgetting](https://arxiv.org/abs/2610.14148)

**<font color=#1a73e8>作者：</font>** Chun-I Fan, Lu-En Chen, Ming-Feng Tsai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine unlearning aims to reduce the influence of designated training data from a trained model while preserving its utility on retained data. Identity-level unlearning is particularly challenging when only limited target-specific information is available when a forgetting request is processed.
In this work, we propose Memory-Coupled Unlearning (MCU), a framework that augments a host model with a Modern Hopfield Network (MHN) serving as a controllable external identity-prototype memory. During prototype construction, feature representations associated with each training identity are aggregated into identity prototypes and stored in the MHN. A Prototype Adaptation Network (PAN) transforms the retrieved memory representation, while a Dependency Gating Unit (DGU) controls its contribution to downstream prediction.
When an identity is requested to be forgotten, MCU first removes the corresponding prototype from the external memory and subsequently readapts the model using limited support information associated with the target identities together with retained data. Importantly, in this work, ``data-absent'' specifically refers to the absence of the complete original forget set during request-time gradient-based readaptation; retained data may still be used to preserve downstream-task utility.
Experiments based on the identity-partitioning and one-shot support construction of 1-SHUI show that MCU achieves a favorable empirical trade-off among model utility, membership distinguishability, and request-time computational efficiency compared with the evaluated baselines. These results provide empirical evidence for the potential of controllable external memory in machine unlearning, rather than a formal guarantee of complete information removal.

---


### 30. [VETNET: Assembling Benchmark Datasets for AI-Driven Veterinary Innovation](https://arxiv.org/abs/2610.14149)

**<font color=#1a73e8>作者：</font>** Katherine J. Koebel, Renata Ivanek, Parminder Basran 等 36 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> VETNET represents an ecosystem of live benchmark datasets and evaluation frameworks designed to accelerate AI-driven innovation in animal science and veterinary medicine through standardized, high-quality datasets and multi-institutional collaboration across academic and non-academic sectors. This framework addresses the gap between AI advances in human medicine and the fragmented state of veterinary AI development.

---


### 31. [TrajCFG: Token-Wise Classifier-Free Guidance via Denoising Trajectory Feedback](https://arxiv.org/abs/2610.14153)

**<font color=#1a73e8>作者：</font>** Jingyu Liu, Hao Jiang, Yikang Ding 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Classifier-free guidance (CFG) typically applies a shared scale to all latent tokens, although their velocity predictions evolve differently during sampling. We introduce Trajectory-Adaptive Classifier-Free Guidance (TrajCFG), a training-free method for flow-matching models that adapts token-wise guidance using historical changes in guided velocity direction. TrajCFG maps this feedback to bounded scales, assigning stronger guidance to larger directional changes and weaker guidance to more consistent directions. It combines adjacent-step and interval-normalized longer-span feedback, reusing standard CFG predictions without additional model evaluations. Controlled diagnostics and ablations examine the roles of directional feedback, token-wise allocation, and history-span fusion. Experiments on text-to-video, image-to-video, text-to-audio-video, text-to-image, and image-to-3D generation show improvements over base samplers across multiple backbones. For text-to-video generation, TrajCFG improves VBench Total scores by 0.30-0.75 points over the strongest evaluated baseline on each of three backbones. These results support historical directional feedback as a broadly applicable signal for fine-grained guidance allocation. The project page is available at this https URL.

---


### 32. [Video-Arena: A Scalable Agentic Video Benchmark for Spatiotemporal Capability](https://arxiv.org/abs/2610.14158)

**<font color=#1a73e8>作者：</font>** Kuan Zhang, Yukun Chen, Zhihao Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding and tracking a dynamic world are fundamental to visual intelligence. Existing video benchmarks provide limited insight into whether models can maintain a coherent understanding of evolving world state. Building such a benchmark from real-world videos is challenging because the underlying world state is partially observable, making annotations hard to obtain. To close this gap, we introduce Video-Arena, a benchmark that turns competitive games into scalable, verifiable tests of how well models understand evolving world states from videos. Specifically, inspired by how humans understand dynamic events, we evaluate spatiotemporal world state understanding and tracking through three task categories: perceiving critical events, interpreting state updates, and tracking the resulting states. Our pipeline can generate videos and aligned reference labels from game records at scale. To keep evaluation affordable and reproducible, we curate a golden set of 180 tasks across 9 games and run evaluations under two protocols: native visual understanding and tool-assisted agentic analysis. The best-performing systems achieve F1 scores of and under the two protocols, respectively. The result highlights that native models struggle to perceive events reliably, while tool-assisted systems improve event recovery but still struggle to interpret state updates and track the resulting states consistently over time. Our project page is in this https URL

---


### 33. [ULPack: Reference-Conditioned Lossless Compression of Checkpoint Trajectories](https://arxiv.org/abs/2610.14184)

**<font color=#1a73e8>作者：</font>** Aniket Srinivasan Ashok  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Studying model training requires checkpoint trajectories, whose storage cost limits temporal resolution. Although adjacent checkpoints are numerically close, existing lossless codecs either operate on XOR bit patterns or ignore trajectory-specific conditional structure. We show that a reference weight's exponent predicts the bit length of its displacement in ordered floating-point space without side information. We introduce \textbf{ULPack}, a lossless codec which exploits this dependence by conditioning entropy models of ordered-integer residuals on the reference exponent. Across bfloat16, float16, and float32 trajectories, ULPack reduces storage by up to 27\% against ZipNN, 21\% against zstd-19, and 11.5\% against FM-Delta. Across two dense trajectories, compression improves as updates shrink and reference conditioning strengthens, while near uniform low-order bits set the remaining compression floor and earlier checkpoints add little information.

---


### 34. [Visualizing the World Model in an Agent's Value Function](https://arxiv.org/abs/2610.14186)

**<font color=#1a73e8>作者：</font>** Shawheen Naderi, Fatemeh Akherati, Yubei Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Could model-free reinforcement learning algorithms actually be learning a model of the environment? In this work, we apply counterfactual interventions which hold everything about a state fixed, besides a targeted change, to explore if the value function of a Proximal Policy Optimization agent forms a world model of the Crafter environment. Despite only being trained to optimize reward, we discover that the value function learns concepts such as the rules governing when a diamond is collectible, water and food having an impact on health, heuristics regarding inventory, and more. Finally, we discuss the safety implications of our visualizations and some shortcomings of current reinforcement learning agents that will prevent us from building truly advanced machine intelligence.

---


### 35. [Embedding Asymmetry as Attack Signal: Detecting and Defending Active Label Inference in Vertical Federated Learning](https://arxiv.org/abs/2610.14194)

**<font color=#1a73e8>作者：</font>** Soumya Swagata Biswas, Muhammad Abdullah Adnan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vertical federated learning lets organizations train a shared model over features they hold separately, while one party keeps the labels private. The active label inference attack of Fu et al. [12] breaks this: a feature-holding party runs a modified optimizer, MaliciousSGD, that forces class structure into its embeddings and then recovers the labels with semi-supervised learning. Defenses that perturb the shared gradient fail, because the attack acts on the party's internal optimizer, not on the message it sends. We show the attack leaves a signal the server can read from the embeddings it already receives. The adversary's Fisher class-separability pulls away from the honest party's, and the gap is visible within a few epochs. A defense triggered by this signal acts on the adversary alone. Scaling its gradient down handles few-class tasks, and a norm non-expansive projection handles many-class tasks, with the Discriminative Coverage Ratio explaining why the projection rank must grow with the class count. The defense breaks the alignment between embedding clusters and labels rather than destroying the embedding. Across four seeds on CIFAR-10, CIFAR-100, and CINIC-10, label inference falls below what honest training already leaks, at under two points of task-accuracy cost.

---


### 36. [Refined Grid Sampling for Efficient Implicit Neural Representations of Large-Scale Scientific Data](https://arxiv.org/abs/2610.14205)

**<font color=#1a73e8>作者：</font>** Guang Zhao, Xihaier Luo, Sean McCue 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Implicit neural representations (INRs) offer a powerful framework for modeling high-dimensional physical fields, but their training remains inefficient because evaluating dense coordinate grids is computationally expensive. Existing coordinate-pruning strategies rely on local error functions that can oversample correlated points and incur substantial overhead from full-grid error evaluation. We introduce Refined Grid Sampling (RGS), which combines stratified grid sampling, error-based refinement, and dynamic grid-resolution adjustment. This design reduces spatial redundancy without evaluating errors over the full grid. On high-resolution Navier--Stokes fields, RGS achieves higher reconstruction accuracy within a fixed wall-clock budget and reaches the accuracy of full-grid training up to $6\times$ faster than the evaluated baselines.

---


### 37. [Agreement versus Softmax under Spatial Disambiguation](https://arxiv.org/abs/2610.14210)

**<font color=#1a73e8>作者：</font>** Michał Zakrzewski, Mariia Shpir, Taras Rumezhak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> ScanRefer Multiple queries require spatial disambiguation: several instances of the target class are present, and the referencer must pick one. When per-query logits were never logged, a common substitute is cross-epoch agreement. On the full ScanRefer validation set (9,508 queries; GeoClassifier with ground-truth proposals), object-level softmax is similarly miscalibrated on Unique and Multiple (ECE 0.068 vs. 0.102; the scene-bootstrap gap interval includes zero). Fixed-final agreement on the same checkpoints reports ECE 0.041 vs. 0.272 (gap +0.231). Modal-vote agreement is 0.045 vs. 0.318. Most Multiple errors are same-class wrong-instance (45.6%); geometric miss (H2) is 59.6%, and wrong-category (H1) is 16.7%. A non-monotone H1 pattern does not appear under the default fixed-final protocol, and we retract it. Logit-free thresholds rank spatially hard queries poorly. If only agreement was logged, calibrate abstention on Multiple and report wrong-instance rates with H1.

---


### 38. [Learnable Low-Rank Polynomial Sketch for Effective Linear Attention](https://arxiv.org/abs/2610.14219)

**<font color=#1a73e8>作者：</font>** Zongyue Qin, Haoran Deng, Jason Cong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Softmax attention in Transformers suffers from quadratic complexity in sequence length, making it impractical for long-context applications. Linear attention alleviates this issue by replacing the exponential kernel with alternative functions that enable linear-time computation. Among existing linear attention approaches, recent studies have shown that polynomial kernels are particularly effective, as they exhibit sparse and spiky behavior similar to softmax attention, which emphasizes large dot products while suppressing irrelevant interactions. However, the exact computation of high-degree polynomial kernels is infeasible for high-dimensional representations. As a result, prior work relies on approximate polynomial kernels. This introduces a non-negligible approximation error. In this paper, we show that, from the perspective of polynomial kernel approximation, existing linear attention methods are still suboptimal. We propose \textbf{L}earnable \textbf{Lo}w-Rank \textbf{P}olynomial \textbf{S}ketch (LLoPS), a principled and flexible framework for approximating polynomial kernels with linear attention. Our method learns a low-rank polynomial sketch that provably achieves a strictly smaller approximation error than existing approaches. Experiment results show that LLoPS achieves the highest performance across extensive benchmarks, comparing with various linear attention baselines.

---


### 39. [Who Guides Whom? Negotiating Care, Religious Authority, and Technology in Bangladeshi Muslim Families](https://arxiv.org/abs/2610.14229)

**<font color=#1a73e8>作者：</font>** Susmita Biswas, Saiful Islam Tuhin, Faria Soroni 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Digital technologies are reshaping how families negotiate care, authority, and responsibility, yet these dynamics remain understudied in religiously situated family life. Through interviews with 38 adult members of Bangladeshi Muslim families, we examine how family members guide one another across religious, digital, and AI-mediated contexts. We find that authority did not simply follow age or family hierarchy: older members often remained sources of religious and familial guidance, while younger members increasingly provided expertise around digital risks, information credibility, and AI. Families also actively shaped digital environments and negotiated the role AI could occupy in everyday relationships. We develop the concepts of household epistemic governance, counter-curation, and domain-dependent authority to explain these shifting relations of knowledge and responsibility. Our findings suggest opportunities for family technologies that support negotiated boundaries, credible information practices, and culturally situated forms of care.

---


### 40. [Learning Non-Gaussian SEMs with Conditional Risk, and Why the Direction of Recursion Matters](https://arxiv.org/abs/2610.14246)

**<font color=#1a73e8>作者：</font>** Ujas Shah, Panagiota Birmpa, Rebecca Morrison  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Variance-based methods recover a Gaussian linear structural equation model (SEM) with equal or suitably constrained error variances, either by recursively identifying the source nodes with smallest conditional variance (top-down method) or sink nodes with highest conditional variance (bottom-up method). We show that the use of conditional variance is incidental: replacing it with the conditional risk, i.e., the minimal expected loss of linear prediction under the negative log-likelihood of the noise distribution, extends both methods to non-Gaussian noise. Existing methods are the least-squares special case. This yields two main results. First, exploiting the noise distribution improves structure recovery: the matched-loss procedures recover the SEM more accurately than their least-squares counterparts and the LiNGAM methods, which are designed for non-Gaussianity. Second, the two methods, interchangeable in the Gaussian setting, separate under non-Gaussian noise: the top-down method is correct for every noise density with finite differential entropy, whereas the bottom-up method requires a regularity condition and can fail without it, for instance under mean-zero exponential or Cauchy noise. Simulations confirm both results.

---


### 41. [Adaptive-Depth Is a Finishing Stage](https://arxiv.org/abs/2610.14252)

**<font color=#1a73e8>作者：</font>** Andrei Piterbarg, Sean McLeish, Dhruv Pai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped transformers reuse the same layer multiple times, allowing inference compute to be adjusted without changing the model. Recent adaptive-depth methods train the model across multiple loop depths from the beginning of training. We introduce fixed-first training, which varies model depth only during a short final phase of training. At 200M parameters, training a model of fixed-depth 2 for the first 67% of the run reduces modeled training compute by 45% while keeping mean negative log-likelihood (NLL) across inference depths within 0.5% of training across depths throughout. At 1B parameters, training initially at depth 4 reduces modeled compute by 31% to 37% and wall-clock time by 32% to 39%, while keeping final NLL within 0.8% and downstream differences within the observed seed variation. These results show that training over the full range of depths can be reserved for a short finishing phase with only small changes in performance.

---


### 42. [SliderEdit++: Improved Slider Trajectories in Instruction-Based Image Editing](https://arxiv.org/abs/2610.14253)

**<font color=#1a73e8>作者：</font>** Arman Zarei, Sayan Nag, Bryan Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Slider-based control aims to give users continuous, fine-grained control over the intensity of individual edits in instruction-based image editing. However, existing approaches fail to deliver reliable continuous controllability: traversing a slider can produce abrupt visual jumps and non-monotonic changes, while jointly controlled sliders can interfere with one another. To systematically study these limitations, we introduce SlideBench, a comprehensive benchmark for continuous image editing spanning diverse editing categories and equipped with a unified suite of metrics quantifying monotonic progression, perceptual continuity, and inter-slider disentanglement. Building on these observations, we propose SliderEdit++, which explicitly regularizes the intermediate editing trajectory rather than supervising only its endpoints. Our method combines velocity- and semantic-space trajectory regularization with spectral control to encourage smooth, predictable slider traversal, together with a disentanglement objective that reduces interference between independently controlled edits. On SlideBench, SliderEdit++ achieves state-of-the-art performance, improving the overall score by 18.5% relative to the strongest baseline. At the same time, using a few-step editing backbone makes our method approximately 3x to 20x faster than existing slider-based approaches, enabling substantially more responsive interactive editing.

---


### 43. [Image Diffusion Models Are Good 3D Human Motion Generators](https://arxiv.org/abs/2610.14254)

**<font color=#1a73e8>作者：</font>** Siyuan Yang, Chong Wang, Hao Cheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-motion generation typically relies on dataset-specific skeletal representations, with models trained separately for benchmarks with different joint layouts. We investigate whether image diffusion architectures can model 3D human motion through a common image-compatible representation that accommodates heterogeneous skeletal layouts while preserving motion-specific kinematic structure. To this end, we organize root-centered joint trajectories into topology-informed joint--time images and model global root dynamics through a complementary latent stream. A motion autoencoder conditions local-motion decoding on the root latent, while a text-conditioned Scalable Interpolant Transformer (SiT) jointly generates both latent streams, with supervision on decoded 3D joint positions further constraining generation in motion space. In addition to dataset-specific models, we train a single motion autoencoder on HumanML3D and KIT-ML, followed by a single text-conditioned SiT shared across both datasets, preserving their respective skeletal definitions without skeleton retargeting to a common joint layout. Experiments on HumanML3D and KIT-ML show that our dataset-specific models achieve state-of-the-art performance, while shared training yields further gains on both benchmarks, demonstrating the benefits of shared modeling across heterogeneous skeletal layouts.

---


### 44. [Do Artificial Neural Networks Need Dendritic Nanotubes? Two Reasons for Shrinking Importance Estimates in Continual Learning](https://arxiv.org/abs/2610.14258)

**<font color=#1a73e8>作者：</font>** Saurav K. Aryal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Regularization-based continual learning protects each parameter in proportion to an estimate of its importance, yet these estimates come from finite samples and heuristics and are used as if they were exact. We report four studies that start from a biologically inspired mechanism and end with a statistical explanation of it. Motivated by dendritic nanotubes, we let transient lateral links diffuse importance tags between hidden units. Links between co-active units gave no significant gain, but random links with lifetimes of 25 or 200 steps raised final accuracy on 20-task Permuted MNIST by 1.5 to 2.6 points. We show that random diffusion implements linear shrinkage of importance toward the layer mean in expectation. A simulation of the link process alone predicts shrinkage weights of 0.23 and 0.52 for these lifetimes, and graph-free shrinkage at 0.25 and 0.5 reproduces both the accuracy and the dispersion of the consolidated importance, while every activity-dependent rule did worse than random links. A five-seed screen across EWC, SI, and MAS found nominal gains for SI and MAS on Permuted MNIST and losses on task-incremental Split CIFAR-100, where forgetting was small and shrinkage cost plasticity. Varying the number of importance samples then separates two mechanisms on Permuted MNIST. For EWC, the gain fell by about ten points per tenfold increase in samples, from 19.6 points with 10 samples to -0.4 with 1000, a variance effect. For MAS, a gain of about one point persisted at 1000 samples, consistent with a bias in the importance measure rather than noise. Shrinkage had no detectable effect for MAS on a domain-incremental CIFAR-100 benchmark. Finally, we show that a standard heteroscedastic empirical Bayes rule shrinks the largest Fisher-type estimates most, which may explain its poor results, and point to a log-scale alternative.

---


### 45. [Variance Fingerprints: Component-Wise Identification of Content Factors by Augmentation Design](https://arxiv.org/abs/2610.14260)

**<font color=#1a73e8>作者：</font>** D. Hudson Smith  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Augmentation-based self-supervised learning can recover the content shared across views without separating its underlying factors into individual coordinates. We ask whether augmentations can be designed to make those factors identifiable. Our approach allows content factors to fluctuate across augmented views while preserving their mean for each source instance. Each instance receives a fixed, recorded set of augmentation strengths that controls how much its factors fluctuate. When factors respond differently to changes in these strengths, their patterns of variation provide information that distinguishes them. Under suitable decoder and support assumptions, we prove that these differences identify individual factors in a conditional Gaussian model, up to permutation, scaling, and translation. We then develop a learner that uses the recorded strengths to estimate these patterns jointly across instances, enabling learning from few views per instance. Synthetic experiments demonstrate near-perfect factor recovery through nonlinear mixing. Controlled dSprites experiments show improved coordinate alignment using augmentations that target known factors, even without telling the learner which augmentation corresponds to which representation coordinate. These results suggest a route to component identification in self-supervised learning: augmentation design can supply identifying information beyond shared content alone.

---


### 46. [BigCell: Generating Gigapixel Whole-Slide Images](https://arxiv.org/abs/2610.14261)

**<font color=#1a73e8>作者：</font>** Srikar Yellapragada, Alexandros Graikos, Zilinghan Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whole-slide images (WSIs) are gigapixel-scale digital scans of histopathology tissue and serve as the primary basis for cancer diagnosis. Existing histopathology generative models operate at the patch scale, producing fixed-size tiles of at most 1024$\times$1024 pixels which encompass only a small fraction of the WSI. In contrast, text reports for clinical diagnoses and slide-level diagnostic labels -- the supervision that exists at scale -- operate at the whole-slide level. We present BigCell, the first approach to generate coherent whole-slide histopathology images at native gigapixel resolution. BigCell trains a flow-matching transformer at 2048$\times$2048 pixels on over 120,000 publicly available WSIs spanning multiple organ types. Conditioning on embeddings from pathology foundation models and using an inference-time sliding-window pipeline, BigCell generates coherent images of up to 32,768$\times$32,768 pixels, outperforming prior tile generators on both tile-level and slide-level fidelity metrics. To make gigapixel synthesis practical, we introduce an adaptive scheduling strategy that prioritizes important slide regions, speeding up image generation by over 3\ttimes with minimal quality degradation. Furthermore, we propose the first text-to-image synthesis at 8k resolution by training a separate model that produces dense conditioning grids directly from pathology text reports. We demonstrate that augmenting with synthetic samples improves slide-level few-shot classification performance by up to $18 \%$ over baselines trained on real data.

---


### 47. [RoboFake: Are Deepfake Detectors Ready for Humanoid Face Robots?](https://arxiv.org/abs/2610.14269)

**<font color=#1a73e8>作者：</font>** Hao Chen, Junnan Xu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Humanoid face robots can now move their lips in sync with speech and show detailed facial expressions. Give such a robot the face of a real person and drive it with generated speech, and you get a face forgery that happens in front of the camera: the camera records a real object, and no pixel is edited. We call this a RoboFake. In this paper we ask what current deepfake detectors do when they see a robot face. We test six public detectors trained on FaceForensics++ on video of a physical lip-syncing face robot, on a synthesized video of the same robot, and on rendered robot faces. All thresholds are fixed on FaceForensics++, and every result is compared with real human faces that went through the same processing as the robot videos. At a threshold that flags 5% of real faces, three detectors flag almost every physical robot frame, while two flag fewer than 7%. A matched human control and masking show that the response comes from the face, not from the processing or the background. However, it does not track synthesis: with only the face visible, three of the six detectors give the physical robot a higher fake score than its synthesized video. The response is also fragile, and light JPEG compression is enough to push most robot frames below the threshold for some detectors. Our results suggest that current detectors flag today's robots because their faces do not look human, not because they recognize a forgery. We release our evaluation protocol and code, and state three testable hypotheses about realistic, interactive RoboFakes.

---


### 48. [The RNN Homunculus: Learning to Gate Long-Term Memory](https://arxiv.org/abs/2610.14279)

**<font color=#1a73e8>作者：</font>** Zeyu Fan, Alexandru-Dragos Manolache, Jan van Gemert  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning long-range dependencies with recurrent neural networks (RNNs) is difficult because of the vanishing gradient problem. Gated recurrent neural networks like GRUs and LSTMs address this problem and are commonly explained by their ability to create additive copy paths through time. This explanation is correct, but incomplete: useful RNN gate values must themselves be learned, which is typically done with another RNN. We study this gate-learning problem through carefully controlled sequence classification tasks. Our analysis shows that gated architectures struggle when all training samples require long-range memory and thus equally suffer from the vanishing gradient problem. We intervene by adding short-dependency samples which let gated models learn solutions that capture long-dependency samples, but also generalize across different class labels. When properly learned, gated RNNs match or even exceed the test accuracy of modern architectures like Mamba and xLSTM. Overall, our results highlight gate learning as a central part of learning long-range memory and show how training data can support this process by exposing the same task over shorter dependencies.

---


### 49. [TGSR: Text-Grounded Diffusion for Faithful Image Super-Resolution](https://arxiv.org/abs/2610.14281)

**<font color=#1a73e8>作者：</font>** Zhiming Hu, Ran Zhang, Angela Ye 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have achieved remarkable success in image super-resolution (SR) by leveraging strong generative priors to enhance perceptual quality. However, for textual content, these priors often produce text hallucinations: non-existent or distorted text, which alter scene semantics and compromise model reliability. While recent methods focus on enhancing text generation, they do so indiscriminately, leaving hallucinations fundamentally unresolved. We argue the core problem is a lack of selective control. Therefore, we reformulate text SR as a selective generation problem: text is resolved only when reliable generation is expected, while other scene content is fully super-resolved. We introduce TGSR (Text-Grounded Super-Resolution), a test-time framework that progressively identifies and suppresses likely hallucinated text regions during generation. To enable this, we train dedicated detectors on a large-scale dataset curated from diverse diffusion-based SR outputs. TGSR consistently improves text fidelity across multiple backbones, increasing recognition precision by up to 17.68 points without degrading perceptual quality, underscoring the value of selective control in generative SR.

---


### 50. [Layer-wise Input Recoverability in Deep Neural Networks](https://arxiv.org/abs/2610.14290)

**<font color=#1a73e8>作者：</font>** Maxwell Spiridonov, Alireza Rahmansetayesh, Pierre Baldi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The inner workings of deep neural networks are still not well understood. The information bottleneck framework, which characterizes deep networks by the mutual information between their hidden representations and the network's input, has been used to identify compression of input information with respect to an input image and output labels. We instead study how much of a layer's own input is recoverable from the layer's output in convolutional neural networks (CNNs). A convolutional layer applies its filters to one input patch at a time, so we evaluate recoverability on sampled input patches with a reconstruction-based probe and not on the entire feature map. The probe's size thus depends on channels and kernel size and not on feature map size, which lets our method scale to deep CNNs with wide feature maps. For each layer, we compare pretrained, random, and reconstruction-optimized encoders, using linear and linear-plus-residual-MLP decoders. We measure recoverability as $R^2$ between input patches and their reconstructions on a held-out set. Across nine ImageNet CNNs, recoverability generally decreases with depth but is more consistently predicted by the compression of the layer. Learning-attributed recoverability, the difference between pretrained and random encoders, is not uniform across architectures. We introduce single-property random controls, which transfer one pretrained property onto a random encoder, and find that each control changes recoverability with a consistent sign across models: copying pretrained singular vectors tends to raise recoverability, while copying the pretrained singular-value spectrum or activation sparsity lowers it.

---


> [!TIP]
> 当前位于：**1-50**（第 1/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
