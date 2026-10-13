# 📦 其他研究 | 2026年10月14日

> 本类共 **244** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-244](./part-05.md)

---

### 151. [SBNO : Schrödinger Bridge Neural Operator for the Forward and Inverse Problems under Missing Information](https://arxiv.org/abs/2610.13317)

**<font color=#1a73e8>作者：</font>** Jaehyeon Park, Inhyeok Jeong, Noseong Park  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Partial differential equation (PDE) surrogate modeling often relies on either dense observations or access to governing equations/physics constraints. In practice, observations can be sparse and partial, and the underlying physics may be partially specified or unavailable. We introduce SBNO, an equation-free paired-data diffusion bridge matching framework that learns conditional operators for both forward and inverse PDE problems under partial observations. SBNO uses diffusion Schrödinger bridge matching to learn a pair of time-dependent drifts from a mask-aware endpoint coupling that preserves empirical input-solution pairing during training and supports both PDE-task directions within a single framework. At inference time, SBNO produces a deterministic point reconstruction by integrating the probability-flow ODE constructed from the learned drift pair, without inference-time observation or PDE guidance-weight tuning. On five PDE benchmarks with 5% observations, SBNO achieves superior or comparable accuracy to baselines while demonstrating lower test-instance error dispersion. Furthermore, SBNO is at least $9.7 \times$ faster and reduces GPU memory by at least $4.3 \times$ compared to guided-diffusion baselines.

---


### 152. [CoVA: Composing VAE Representations for Generative Learning](https://arxiv.org/abs/2610.13322)

**<font color=#1a73e8>作者：</font>** Zhaowei Chen, Yikai Ge, Linze Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Representation alignment with pretrained visual encoders improves diffusion transformer training but requires auxiliary encoders and extra training overhead. Recent approaches instead exploit representations from the generative model's own variational autoencoder (VAE). However, reconstruction-oriented VAE features are not optimized for the semantic discrimination and spatial structure needed for generative learning. We introduce \textbf{CoVA} (\textbf{Co}mposed \textbf{VA}E Representations), a lightweight framework that composes VAE features online into stage-wise guidance for flow-matching training. A small latent composer is jointly trained with class supervision, masked latent reconstruction, and horizontal-flip consistency, yielding semantically discriminative, spatially structured dense features and sample-dependent class posteriors. CoVA aligns intermediate SiT features with the composed representations early in training, then removes the increasingly detrimental alignment and reuses detached composer posteriors for sample-dependent soft label conditioning. We further uncover a hidden confound in soft label conditioning: averaging class embeddings attenuates their magnitude, coupling semantic interpolation with conditioning strength. This attenuation alone can substantially improve FID while degrading Recall, revealing a non-semantic source of the apparent gain. CoVA corrects this confound by restoring the hard-label magnitude, isolating posterior-dependent directional semantics. CoVA adds only 8.5M training-only auxiliary parameters (1.3\% of SiT-XL/2) and introduces no inference-time overhead. On ImageNet 256$\times$256, CoVA reduces SiT-XL/2 FID from 17.2 to 7.4 (\textbf{57\%}) in 400K steps. With classifier-free guidance, it achieves an FID of \textbf{2.03} in only 400 epochs, versus 2.06 after 1,400 epochs for vanilla SiT-XL/2.

---


### 153. [LETHE: Defending against Unauthorized Image-to-Video Generation via Value Diversity Collapse](https://arxiv.org/abs/2610.13333)

**<font color=#1a73e8>作者：</font>** Boheng Li, Yueming Xing, Yiming Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-to-video (I2V) diffusion models can animate a single reference image into high-quality, subject-consistent videos, posing threats of misuse as anyone can turn personal photos into fabricated videos without consent. A promising solution is to proactively add an adversarial perturbation to the image before release, such that videos generated from it would be unfaithful or visually corrupted. However, due to an insufficient understanding of what governs how subsequent frames read the reference image in modern I2V models, existing protections struggle to offer strong protection under common perturbation budgets. In this paper, we approach the problem by exploring this underlying reading mechanism. Through a convex geometric analysis, we theoretically identify the spread of the reference value vectors as a key factor governing this reading process, and empirically find that even a mild contraction of this spread can severely degrade the generated video, making it an efficient lever for protection. Guided by this insight, we propose LETHE, a novel protection method that directly disrupts this reading process. LETHE pairs two complementary objectives, where a value collapse objective drives the reference value vectors toward uniformity, while an attention attraction objective draws subsequent frames toward these collapsed tokens to amplify corruption. We further construct two human-centric I2V protection benchmarks and conduct extensive experiments with multiple modern I2V models, which demonstrate the state-of-the-art protection performance and versatility of LETHE.

---


### 154. [VideoAWR: Reinforcing Video Flow Models with Decoupled-Timestep Advantage-Weighted Rectification](https://arxiv.org/abs/2610.13338)

**<font color=#1a73e8>作者：</font>** Zheming Fu, Wenbin Ning, Ruizhe He 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Regression-based RL for flow models mandates sampling \emph{without} classifier-free guidance (CFG) to align the rectification target with the reference marginal velocity. Extending Advantage-Weighted Rectification (AWR), which dynamically scales this regression target based on reward, to video generation encounters a cold-start pathology: unguided rollouts collapse into low-fidelity regions where intra-group reward gaps remain wide but no longer track perceptual quality, rendering the optimization target arbitrary. Conversely, utilizing guided rollouts to restore fidelity, while keeping the regression target tied to the guided sampling distribution, provably triggers a geometric guidance blow-up under exponential-moving-average (EMA) updates. We propose \textbf{VideoAWR}, which resolves this tension by untying sampling from the optimization anchor. An EMA reference policy generates \emph{guided} rollouts to restore reward separability, while the trainable policy is rectified against the \emph{unguided} conditional anchor. We prove this decoupled objective is mathematically exact: the centered advantage cancels the anchor in expectation, filtering out the reward-neutral guidance offset and retaining only the reward-correlated covariance increment. Consequently, inference runs single-branch and CFG-free, yet inference-time CFG preserves its original semantics. Furthermore, we introduce \emph{Decoupled Timestep Rectification}, supervising each rollout at an independently sampled timestep without bias to improve sample efficiency. Experiments on Wan2.1-1.3B and 14B demonstrate stable optimization and superior visual and motion quality in \emph{both} CFG-free and CFG-enabled regimes. Code is available at \pdfstartlink attr{/Border [0 0 0]} user{/Subtype /Link /A << /S /URI /URI (this https URL) >>}% \textcolor{pearDark}{VideoAWR}\pdfendlink.

---


### 155. [Why DiT Models Underperform as Representation Learners without Long Skip Connections](https://arxiv.org/abs/2610.13344)

**<font color=#1a73e8>作者：</font>** Benyuan Meng, Yiliang Zhang, Jin-Wen Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion feature, i.e., intermediate activations extracted from diffusion model backbones, has emerged as a promising approach for unifying generation and vision understanding (discrimination). Despite the advancement of diffusion backbones into Diffusion Transformers (DiT), it has been found in previous literature that DiT models tend to yield weaker features despite their stronger generation capability. This poses a threat to good generation-understanding unification. In this work, we show via controlled from-scratch training that long skip connections (LSCs) affect feature quality: a DiT with LSCs can produce better features. Furthermore, through detailed diagnosis, we reveal the mechanism causing this effect. Specifically, the input to a diffusion backbone contains both the latent image and the diffusion noise, where the diffusion noise, though appearing in the form of noises, actually reflects the information of the diffusion trajectory. To make the final prediction of a noisy variable ($v$ or $\epsilon$), the diffusion backbone needs both signals. However, carrying both signals through the main backbone effectively "pollutes" the image signal with noises, leading to poor feature quality. In comparison, LSCs can shortcut diffusion noises directly to where they are needed, leaving much weaker noise signals in the main backbone, thus improving feature quality. To name the broader impact, this reveals that LSCs are not a mere trick but closely related to the diffusion objective. The code is at this https URL.

---


### 156. [Hidden Data Challenges in Clinical Machine Learning](https://arxiv.org/abs/2610.13350)

**<font color=#1a73e8>作者：</font>** Carolin Cissée, Dennis Fast, Raneen Younis 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Widely reused preprocessing pipelines for electronic health records can encode assumptions about when information became available, what clinical episode a label represents, and what missingness means. These assumptions are rarely audited systematically and may propagate across subsequent studies when preprocessing pipelines are reused or adapted. Using MIMIC-IV as a case study, we identify and quantify violations of three complementary forms of preprocessing alignment, i.e., temporal, semantic, and population alignment, which manifest as temporal leakage, feature-task misalignment, and biased imputation. We show how ambiguities in timestamp semantics, episode definitions, endpoint construction, modality selection, and missingness handling can alter the information available to a model and affect the interpretation of its predictions. Through analyses of MIMIC-IV data and empirical case studies, we demonstrate that such choices may remain largely invisible in aggregate predictive performance while changing the signals on which models rely. We derive practical recommendations for temporally valid, clinically aligned, and reproducible preprocessing of MIMIC-IV and related electronic health record datasets. The code for our experiments, including our proposed preprocessing, is available at: this https URL.

---


### 157. [AlphaNIST: Emergent Assembly Skills from Binary Task Rewards](https://arxiv.org/abs/2610.13354)

**<font color=#1a73e8>作者：</font>** Octi Zhang, Iretiayo Akinola, Rosario Scalise 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The NIST Assembly Task Board #1 remains a challenging benchmark for learning-based methods in robotic manipulation. Over short horizons, it demands precise, contact-rich control of small, tight-fitting parts. Over long horizons, it requires recovery and coordination across extended action sequences. Demonstrations, task decomposition, and dense progress rewards have enabled research advances by providing guidance on how to assemble. But how much of the strategy must be specified? The progression from AlphaGo to AlphaGo Zero showed that RL at scale can discover superhuman strategies without prescribing how to win. AlphaNIST asks whether a sparse binary task reward and task diversity admitted by this task-agnostic reward can similarly let a robot discover how to assemble. In simulation, we train a single policy from scratch across all 20 assembly tasks on the NIST Assembly Task Board #1, reaching 98.2% overall training success without demonstrations, progress shaping, scripted primitives, or per-task tuning. The framework also trains policies to complete ten assembly pairs in a single episode without a prescribed order, with task success rewarded only when all ten pairs are simultaneously complete. The learned policies discover dexterous and planning-like behaviors: choosing grasps for later assembly, using surrounding geometry to reorient parts, and preparing one part, assembling another, then returning to finish the first without an explicit planner. For videos, see our website: this https URL

---


### 158. [Secrets in Preamble: Practical and Robust PHY Information Hiding for Wi-Fi](https://arxiv.org/abs/2610.13367)

**<font color=#1a73e8>作者：</font>** Rui Pan, Guanxiong Shen, Linning Peng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Physical layer (PHY) information hiding refers to the concealment of secrets within PHY waveforms without compromising the integrity of the primary communication link, thereby enabling critical applications such as covert communication, PHY steganography, and watermarking. The widespread deployment of Wi-Fi has motivated substantial research interest in hiding secrets within Wi-Fi waveforms. However, existing Wi-Fi information hiding approaches suffer from two limitations: restricted steganographic capacity and insufficient robustness against environmental variations, both of which severely constrain practical deployment. This work proposes to embed secrets within the Wi-Fi legacy short training field (L-STF). The designed method preserves the autocorrelation properties of Wi-Fi L-STF, ensuring that packet detection and coarse frequency offset compensation functionalities remain uncompromised. The secret embedding and extraction processes employ a pair of neural networks designed to learn optimal embedding rules and maximize steganographic capacity. We developed a prototype system and conducted comprehensive experiments across both indoor and outdoor environments. Experimental results show that our method can reliably embed 46 secret bits within Wi-Fi packets across diverse channel conditions, achieving significantly enhanced steganographic capacity and environmental robustness. The hardware prototype study validates the feasibility of the proposed Wi-Fi information hiding scheme.

---


### 159. [Opening the Black Box of Classifier-Free Guidance via Information Bottleneck](https://arxiv.org/abs/2610.13369)

**<font color=#1a73e8>作者：</font>** Jiayang Gao, Tianyi Zheng, Jiayang Zou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classifier-free guidance (CFG) is a standard technique for improving conditional generation in diffusion models, yet its activation schedule is usually selected heuristically. In practice, most existing CFG-based methods rely on a pre-defined activation policy throughout inference, while recent dynamic variants often depend on hand-designed schedules without a principled theoretical explanation of when conditional information is most useful. In order to understand how the informational relevance between conditioning inputs and the score function evolves over the course of generation, we explore when guidance should be activated from an information-theoretic perspective. In this work, we formulate the diffusion trajectory as a time-dependent information bottleneck and show that the effectiveness of conditional information is not uniform throughout sampling, but becomes significantly stronger after a critical stage characterized by a Fisher-information balance condition. Motivated by this insight, we propose a training-free dynamic CFG strategy for inference. Rather than prescribing a fixed schedule in advance, our method constructs a stochastic process from conditional and unconditional score statistics and activates guidance when the estimated guidance gain crosses a prescribed threshold. This yields an adaptive activation rule that aligns condition injection with the underlying generation dynamics, while also recovering interval-based guidance as a limiting special case. Extensive experiments across diverse architectures and tasks, demonstrate that our method is effective, robust, and broadly applicable. Beyond empirical improvements, our framework provides an interpretation of dynamic guidance methods and a principled foundation for inference-time control in conditional diffusion models.

---


### 160. [Towards Safe World Models: Risks, Defenses, and Evaluation](https://arxiv.org/abs/2610.13372)

**<font color=#1a73e8>作者：</font>** Xiaoma Wang, Litian Zhang, Xinze Shi 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> World models support planning, control, learning from imagined experience, and model-mediated evaluation by predicting action-conditioned consequences. Their safety cannot be inferred from predictive accuracy alone: errors in observations, state and memory, dynamics, evaluation, execution, or feedback can propagate into unsafe decisions and persist through updates. This work organizes the literature on world-model safety around a six-stage lifecycle covering data and observations, state and memory, dynamics and imagination, evaluation and planning, action and control, and feedback and update. We synthesize non-adversarial failures, attacks, defenses, evaluation protocols, benchmarks, and deployment conditions, and distinguish evidence directness from outcome level. The current evidence corpus contains 163 cited works. We use the framework to identify where claims are supported, where attribution remains unresolved, and which measurements are needed to connect model-level behavior to closed-loop and operational safety.

---


### 161. [BLOKS: Scaling Kernel Solvers with Sketched Block Preconditioning](https://arxiv.org/abs/2610.13382)

**<font color=#1a73e8>作者：</font>** Giordano Vitale, Giacomo Meanti, Marco Rando 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kernel Ridge Regression (KRR) is a theoretically sound algorithm for nonparametric learning, which is also often used to investigate properties of deep learning. However, the exact KRR formulation incurs time and memory costs preventing applicability to large datasets, motivating the development of approximate solvers. These algorithms rely on (i) iterative methods, to avoid the computational burden of direct solutions; (ii) sketching or batching, to reduce the problem size; and (iii) preconditioning, to accelerate convergence. While crucial for fast convergence, preconditioning incurs memory costs that can be managed by lowering the number of free parameters of the model, potentially at the expense of expressivity and hence accuracy. To address this challenge, we propose BLOKS, a Conjugate Gradient-based solver for Nyström-sketched KRR built around a novel preconditioner that combines a block Jacobi approximation with sketching. The BLOKS preconditioner has memory cost independent of both the dataset size and the number of parameters, allowing scaling to large models. We provide a memory-efficient, GPU-accelerated implementation and show that BLOKS achieves excellent accuracy while retaining favorable time/memory complexity. Indeed, on standard large-scale datasets used to benchmark kernel solvers, BLOKS achieves comparable or better performances than state-of-the-art methods.

---


### 162. [PlacePulse: Learning Transferable Place Representations from Structural Geographic Data](https://arxiv.org/abs/2610.13390)

**<font color=#1a73e8>作者：</font>** Lucía García-Duarte, Miguel Álvarez, Diego Vicente 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Geospatial machine learning often depends on task-specific feature engineering over large collections of sociodemographic, business, and environmental variables. Geospatial foundation models offer reusable representations of place, but leading approaches typically encode dynamic signals, such as mobility and search activity, or visual signals from satellite imagery. Few models represent the static structural composition of places (who lives and works there, which businesses operate there, and which risks they face) as transferable embeddings at fine spatial resolution. We introduce PlacePulse, a structural geospatial foundation model that compresses 572 attributes, expanded to 2,288 inputs through H3 neighborhood aggregates, into 256-dimensional unit-norm embeddings for 1,055,537 H3 resolution-7 cells in the United States. We also introduce a reusable two-axis benchmark that separates intrinsic representation quality from downstream predictive utility across multiple targets and spatial supports. Intrinsically, the embeddings reconstruct standardized inputs with mean $R^2 = 0.853$, use 251 of 256 approximately decorrelated dimensions, and show strong spatial organization, with Moran's $I = 0.93$ on the leading principal component and autocorrelation persisting beyond the input radius. Extrinsically, across 74 held-out targets from 12 external sources and four spatial supports, PlacePulse outperforms a dimensionality-matched feature-selection baseline on targets unrelated to the training inputs and is competitive with Google's Population Dynamics Foundation Model, leading on health, economic, election, economic-mobility and social-vulnerability outcomes, with relative strengths that vary by domain. These findings position structural composition as a distinct and complementary modality for geospatial foundation models, not simply a fallback where behavioral or imagery data are unavailable.

---


### 163. [Why Linear Models Can Still Work in a Complex and Changing World](https://arxiv.org/abs/2610.13404)

**<font color=#1a73e8>作者：</font>** Fangzhou Lin, Dengzhe Hou, Yinxing Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear models can predict well in complex domains even when underlying mechanisms are nonlinear. We argue that this can occur because the complexity of the world exceeds the complexity that can be learned reliably from finite, partially observed data. Flexible models can exploit curvature, thresholds, and interactions that fit one hospital, period, population, policy setting, or measurement process but fail elsewhere. When this instability lies mainly in the nonlinear component, omitting it can give linear models lower prediction error in a new environment. We connect this claim to work on simple linear rules, bias and variance, regularization, best linear prediction, measurement error, distribution shift, invariance, Rashomon sets, and underspecification. Proposition 1 gives a simple squared-error case in which a nonlinear rule learned in the training environment raises target error because it transfers too weakly; finite-sample estimation error can strengthen this result. Partial observation alone is not enough: the link between observed variables and unobserved factors must vary across environments. Stable nonlinear structure favors flexible models, and linear models remain vulnerable to linear spurious relationships. Model complexity should therefore be chosen by cross-environment stability as well as training-data accuracy.

---


### 164. [Accelerating Linear Bandits with Persistent Candidate Sets](https://arxiv.org/abs/2610.13407)

**<font color=#1a73e8>作者：</font>** Bingkui Tong, Daria Korovaitceva, Marina Sheshukova 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Exhaustive optimistic scoring can make action selection costly in linear bandits with a large fixed set of $K$ actions, requiring $\mathcal{O}(K)$ score evaluations per round. We introduce Persistent Candidate LinUCB (\textsc{PC-LinUCB}), which maintains $k$ active actions and samples $q$ challengers uniformly from the remaining $K-k$ actions at each round. By scoring only these $k+q$ candidates, \textsc{PC-LinUCB} reduces the number of score evaluations per round to $\mathcal{O}(k+q)$. We establish problem-independent and problem-dependent high-probability regret bounds consisting of a standard linear-bandit learning term and an additive discovery cost of order $\mathcal{O}\left((K-k)\log(K-k)/q\right)$ at fixed confidence. Notably, this additional cost does not grow with the horizon. For fixed gaps and sufficiently long horizons, we establish an $\Omega\left((K-k)/q\right)$ regret lower bound under uniform challenger sampling, showing that partial candidate access itself imposes an unavoidable regret cost. Experiments show that \textsc{PC-LinUCB} substantially accelerates LinUCB while maintaining comparable regret, and that the persistent candidate mechanism can extend beyond LinUCB.

---


### 165. [SADL: A Size-Adaptive Decision Layer for Chronic Stroke Lesion Segmentation in ISLES 2026](https://arxiv.org/abs/2610.13422)

**<font color=#1a73e8>作者：</font>** Marek Wodzinski, Gniewosz Drwiega, Wojciech Szymanski  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chronic ischemic stroke lesions are difficult to segment on T1-weighted MRI. Their appearance overlaps with healthy tissue, and their volumes span four orders of magnitude, so voxel-level and lesion level metrics often disagree. We build an eleven-member nnU-Net ensemble that covers five design axes: a baseline dice + top-K loss, heavy augmentation, per-lesion volume loss re-weighting, stochastic weight averaging, and a sampling-and-architecture block that pairs cohort-balanced sampling with a residual-encoder backbone. Weighted soft-map fusion of the members feeds a tuned decision layer, SADL, that estimates lesion volume, applies an adaptive per-lesion-size threshold, prunes components by voxel count and peak probability, and adds a never-empty rescue. All fusion weights and per-bucket parameters are fitted on out-of-fold (OOF) predictions, so tuning never touches the held-out test set. On a site-disjoint 91-case holdout, SADL reaches Dice 0.7322, lesion-F1 0.7461 and PR-AUC 0.8430 when scored online with the challenge's released evaluation code. A paired non-parametric bootstrap against a reference single ensemble member confirms the lesion-F1 gain at p=0.024, and the gain is largest in the small-lesion regime, where the rescue step recovers cases that a fixed threshold would silently discard.

---


### 166. [Local Diagnostics of Learned Event Representations for Anomaly Detection at the HL-LHC](https://arxiv.org/abs/2610.13437)

**<font color=#1a73e8>作者：</font>** Donatella Genovese, Philip Ploner, Simone Scardapane 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Anomaly detection, the identification of collision events that deviate from Standard Model expectations, is one of the most promising model-agnostic strategies for new-physics searches at the Large Hadron Collider. Searching for rare events in learned low-dimensional representations removes the need to commit to hand-crafted observables a priori, but sacrifices the immediate physical interpretation those observables provide. For anomaly detection to enter a discovery pipeline, flagged events must therefore be diagnosed locally, both to distinguish potential new physics from mismodeling or detector effects and to identify observables for targeted follow-up searches. We evaluate supervised and self-supervised neural embedding strategies on COLLIDE-2V, a 750-million-event dataset simulated under realistic High-Luminosity LHC conditions, using the reconstruction error of an autoencoder trained in the learned latent space as the anomaly score. Across the configurations and benchmark signals considered, supervised objectives, which exploit simulation process labels during training, generally outperform their self-supervised counterparts and, in their best configurations, improve on an autoencoder trained directly on kinematic features, raising the signal efficiency at 10% background acceptance on all held-out processes. We further introduce a local diagnostic pipeline that fits a Gaussian Mixture Model to the SM latent space, profiles each component through high-level observables without process labels, localizes the flagged events, and ranks observables by their local discriminating power. The ranking recovers the defining kinematics of the held-out processes, while correlating the anomaly score with the same observables quantifies how closely the score tracks them, revealing cases where the most discriminating observable is not the one the score follows most closely.

---


### 167. [Collective Autonomous Vehicle Routing Needs Social Awareness for Coexistence with Human Drivers](https://arxiv.org/abs/2610.13439)

**<font color=#1a73e8>作者：</font>** Anastasia Psarou, Mikolaj Rams, Blazej Torbus 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Collective Autonomous Vehicle (AV) route choices in real-world traffic networks can create externalities for Human-Driven Vehicles (HDVs), as routes that benefit AVs may increase travel times for other road users. To address this, we introduce a social component, the marginal cost, to the selfish travel time AV reward. Marginal cost captures an AV's impact on other road users by comparing their travel times with those in a counterfactual simulation in which the AV is removed.
We study AV route choice in mixed-autonomy traffic settings using Multi-Agent Reinforcement Learning (MARL), where AVs learn routing policies through repeated interactions with the traffic environment. Experiments on the real-world networks of Ingolstadt and Provins show that incorporating marginal cost into the AV reward not only limits the increase in HDV travel times and shortens AV travel times relative to selfish AV routing, but also improves overall system performance. In Ingolstadt, selfish routing of 40\% AVs increases the travel times of other vehicles by 1.7\%, and this drops to 1.1\% when the social reward is included. Interestingly, not only does overall system performance improve, but the AVs are also better off when acting this http URL effect is consistent across tested cities, penetration rates, and replications, yet when the weight of the social component in the reward increases, the system fails to reach the desired performance.
For a more scalable approach to social AV routing in mixed-autonomy traffic, we compute the marginal cost only for the AVs whose route choices most affect the traffic system. This reduces the number of counterfactual simulations and achieves similar performance at a significantly lower computational cost. Our results suggest that AV routing should go beyond selfish rewards and, for the benefit of all traffic participants, include a social component in its objective.

---


### 168. [HoldLight: Making Indoor Climbing More Accessible for Blind and Low-Vision Climbers through Layered Route Preview and Real-Time Next-Hold Guidance](https://arxiv.org/abs/2610.13445)

**<font color=#1a73e8>作者：</font>** Chenyu Du, Junyan He, Jiafei Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Indoor climbing creates access barriers for blind and low-vision (BLV) climbers because route understanding and in-climb next-hold localization are typically visually mediated and socially dependent. We present HoldLight, a workflow-centered accessibility system combining layered pre-climb route preview, concise real-time next-hold cueing, and explicit fallback under uncertainty. We grounded the design through formative inquiry with BLV climbers, refined the interaction via pilot testing, and conducted a controlled within-subjects evaluation comparing HoldLight with a controlled on-demand human-support condition derived from current support practices. Findings provide initial evidence that structured support can improve pre-climb route understanding, support recovery from next-hold uncertainty, and reduce immediate human re-entry for routine route-information clarification under controlled conditions. HoldLight contributes a bounded accessibility workflow, demonstrating where structured route-information is helpful, where explicit fallback is necessary, and how technical assistance can integrate with retained human safety oversight.

---


### 169. [Towards Enriching Design-Time Models with Evidence from Simulation and Operational Activities](https://arxiv.org/abs/2610.13456)

**<font color=#1a73e8>作者：</font>** Barbara da Silva Oliveira, Julien Deantoni, Nicolas Ferry  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cyber-Physical Systems are developed through multiple model based activities, comprising several stages of development. As the development progresses through simulation, experimentation, and operation, observations of system execution may reveal missing, uncertain, or invalid design knowledge. The path from execution results to persistent design-time enrichment, however, is often implicit. This paper addresses this challenge by proposing an evidence driven workflow for systematically transferring knowledge produced during simulation and operation back into design-time models. We demonstrate the workflow using an Influence Model, a design-time artefact used to represent how design artefacts and environmental factors jointly affect system response properties, using a sign-following robot use case. We show how simulation evidence can enrich Influence Models by supporting participant pruning decisions, interaction characterisation, influence-function abstraction, and validity-scope information. The application demonstrates the feasibility of the workflow for simulation-based evidence and its potential benefits to improve design-time reasoning and feedback in subsequent development iterations.

---


### 170. [A Real-World CAD Segmentation Benchmark: Comparing Rule-Based and Learning-Based Approaches through Hole Detection](https://arxiv.org/abs/2610.13466)

**<font color=#1a73e8>作者：</font>** Kai Schütte, Edgar Heinert, Matthias Rottmann  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> CAD segmentation datasets are predominantly synthetic or automatically labelled, leaving it unclear how well existing methods transfer to real-world engineering tasks. Fastener-relevant hole detection represents one such task, requiring human annotation and exhibiting greater geometric complexity than commonly used benchmarks. We address this gap through three main contributions. First, we develop two task-specific rule-based methods, one graph-wire-search and one multi-view based, and complement them with a human-annotated benchmark dataset derived from engineering CAD data that also enables training of UV-Net and AAGNet, representative learning-based approaches for B-Rep segmentation. Second, we conduct an extensive experimental study including parameter optimisation, evaluation on our benchmark dataset, cross-domain generalisation on a synthetic dataset, and an assessment of the feasibility of the approaches at varying dataset sizes and IoU thresholds. Third, we provide evidence-based insights into the strengths and limitations of different approaches: rule-based methods generalise well without training data, with the graph-wire-search method favouring recall and the multi-view method favouring precision, whereas learning-based methods achieve strong performance with sufficient annotations but exhibit reduced robustness under domain shift. These findings highlight trade-offs between data requirements, and robustness, and provide guidance not only for hole detection, but more broadly for real-world CAD segmentation tasks.

---


### 171. [GraftOOD: Grafting Out-of-Distribution Exemplars into Advantage-Weighted Rectification for Video Reward Optimization](https://arxiv.org/abs/2610.13470)

**<font color=#1a73e8>作者：</font>** Zheming Fu, Ruizhe He, Wenbin Ning 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video reward optimization can increase proxy rewards while reducing video dynamics, a mismatch we identify as \emph{motion collapse}, including under a video-level motion-quality reward. We propose \textbf{GraftOOD}, which replaces part of the online rollouts in selected prompt groups with out-of-distribution video exemplars. A shared velocity-regression objective combines group-relative reward rectification with sequence-level exemplar supervision, requiring neither exemplar generation trajectories nor an additional supervised-loss coefficient. We characterize its pointwise optimal field as a source-posterior-weighted combination of the two source-specific target fields. We construct \textbf{GraftSet-Video}, containing 9,588 format-matched exemplars for 2,397 prompts, to supply external supervision. On Wan2.1-1.3B, GraftOOD raises Dynamic Degree from 4.86 to 44.41 relative to reward-only FlowAWR, while HPSv3 decreases from 8.10 to 7.32 and VisionReward remains close. At the main setting, GraftOOD leads nine of ten metrics among three exemplar-augmented methods. Ablations of exemplar frequency and within-group count reveal dynamics--reward trade-offs rather than uniform gains from increasing exemplar usage. These results support external exemplar supervision as a complement to scalar reward feedback, without equating higher measured dynamics with coherent, visually plausible motion in the generated videos. Code is available at \href{this https URL}{GraftOOD}.

---


### 172. [A Better Metric Will Not Save You: What You Compare Beats How You Compare It](https://arxiv.org/abs/2610.13476)

**<font color=#1a73e8>作者：</font>** Noureddine Khaous, Guillaume Wisniewski  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Representational similarity measures (RSA, CKA, Procrustes) are chosen for the transformations they treat as irrelevant, and all of them take the set of conditions as given. That set is fixed by two decisions, which inputs are admitted and how they are grouped, both taken before the matrix a measure operates on exists: no invariance property reaches them. We measure what they are worth where the arrangement the conditions ought to have is known independently of the systems compared, the acoustic organisation of vowels, across fifteen languages and twenty-seven representations. Changing which categories are compared, at a fixed number of them, moves the gap between two representations by more than twice the effect being measured, while changing how many moves it not at all. In this setting rankings of models are identified under these choices, and rankings across languages are not.

---


### 173. [SplatQ: Interaction-Aware Pruning of 3D Gaussian Splatting via Quadratic Selection](https://arxiv.org/abs/2610.13503)

**<font color=#1a73e8>作者：</font>** Hongbin Ye, Haixu Liu, Shenwei Kang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing 3D Gaussian Splatting (3DGS) pruning methods primarily rely on global Top-K selection based on independent importance scores, lacking regional budget control and ignoring joint deletion effects. Consequently, they cannot ensure balanced reconstruction quality across a scene. We propose SplatQ, a combinatorial pruning algorithm that coordinates regional budget allocation and joint Gaussian selection under a fixed budget. SplatQ partitions Gaussians by spatial proximity and appearance similarity into size-limited blocks, decomposing global selection into subproblems of a specific size. It then smooths importance-based block retention quotas to prevent excessive budget concentration. Finally, it constructs a quadratic approximation of joint deletion effects using the responses of representative pixel colors to changes in Gaussian opacity. Individual responses, pairwise interactions, and quota penalties are incorporated into a quadratic unconstrained binary optimization (QUBO) objective, solved using simulated annealing (SA) or a coherent Ising machine (CIM) to jointly select Gaussians. Experiments on 5 benchmarks demonstrate that SplatQ outperforms state-of-the-art pruning methods in aggregate reconstruction quality, spatial quality balance, and rendering speed. Ablations confirm that budget smoothing improves local detail reconstruction, while interaction modeling improves Gaussian selection quality under a fixed budget.

---


### 174. [FedPCD: Priority-Constrained Federated Aggregation](https://arxiv.org/abs/2610.13508)

**<font color=#1a73e8>作者：</font>** Yousef Irshaid, Dara Varam, Mohamed I. AlHajri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) seeks to optimize a shared global model from decentralized client data. While effective for average performance, this process can produce unfair performance across clients, particularly under statistically heterogeneous data distributions. Existing fairness-aware and multi-objective FL methods address this through client re-weighting, gradient correction, or common-descent formulations, but often change the global optimization direction or treat client objectives symmetrically. We propose FedPCD, a priority-constrained federated optimization framework that separates the global optimization objective from client protection. FedPCD preserves the conventional federated aggregate as the primary objective, while allowing only the minimum correction necessary to meet client performance constraints. Across heterogeneous FL benchmarks, FedPCD consistently outperforms state-of-the-art baselines, achieving the highest global accuracy across all configurations and leading worst-10% client accuracy in nearly all. FedPCD further preserves competitive trade-offs between global accuracy and client performance variability. Beyond this trade-off, FedPCD demonstrates faster empirical convergence, reaching matching or superior performance in substantially fewer communication rounds.

---


### 175. [Causal Effect Identifiability in Causal Abstractions: A Strict Hierarchy of Criteria](https://arxiv.org/abs/2610.13520)

**<font color=#1a73e8>作者：</font>** Clément Yvernes, Marianne Clausel, Emilie Devijver 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Identifying causal effects from observational data typically requires a fully specified causal graph, an assumption that is often unrealistic in complex or high-dimensional settings. Causal abstractions address this limitation by retaining only partial causal information, thereby defining equivalence classes of compatible causal graphs. In this paper, we study causal effect identifiability directly at the level of these graph collections, rather than at the level of individual causal diagrams. We formalize several notions of identifiability in this setting and organize them into a hierarchy that clarifies their relationships and differences. In particular, we establish that a causal effect may be identified over a collection of graphs without admitting a single causal derivation that holds uniformly across all compatible graphs. These results help reveal gaps and clarify ambiguities in the existing literature.

---


### 176. [MAGMA-Bench: Evaluating Long-Horizon Embodied Agents under Dynamic Tasks and Execution Failures](https://arxiv.org/abs/2610.13534)

**<font color=#1a73e8>作者：</font>** Loan Bernat, Matthieu Grard, Ariane Herbulot 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon embodied agents must maintain task-relevant information, coordinate heterogeneous robots, and adapt their decisions as execution unfolds. Existing benchmarks investigate dynamic task execution and embodied multi-agent coordination, but provide limited evaluation of their intersection. We introduce MAGMA-Bench, an architecture-agnostic benchmark for persistent task reasoning in dynamic multi-robot environments. MAGMA-Bench evaluates agents across increasing task horizons and controlled online perturbations, including execution failures, task interruptions, and mission updates, with scenarios requiring coordination across robots with heterogeneous capabilities. It uses a structured skill-level interface to separate task-level reasoning from perception and low-level control. We evaluate locally deployable open-weight planners, multi-agent state-tracking strategies, and frontier models. Even the strongest evaluated models fail on a substantial fraction of clean episodes, and their success rates decrease further under online perturbations. Supervised adaptation greatly improves a small model, but performance remains substantially lower on longer and multi-robot missions. We release the benchmark, 261,646 task-level training examples, and an architecture-agnostic expert-trace generation pipeline.

---


### 177. [Knowing Whether, Not Just Where: Anchor-Probing Distillation for Open-Set Remote Sensing Visual Grounding](https://arxiv.org/abs/2610.13535)

**<font color=#1a73e8>作者：</font>** Zhihao Chang, Lei Zhai, Shuyuan Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-set visual grounding in remote sensing requires models to determine not only where a queried object is located, but also whether the image provides sufficient evidence for the query at all. Existing closed-set grounding models, however, tend to return plausible boxes even for absent objects, blurring localization confidence with genuine Visual Support. We introduce AnchorProbe-Distill (APD), a teacher-student framework that recasts open-set grounding as Visual Support learning. APD builds on the insight that supported queries should induce coherent spatial anchors, whereas unsupported or mismatched queries tend to produce unstable or misleading localization patterns. APD-T therefore uses the Original Query as a Reference Anchor to interpret query perturbations: Semantic-Preserving Queries retain the annotated target, Near-Category Ambiguous Queries are resolved according to whether they form a reliable alternative anchor or collapse onto the Reference Anchor, and Far-Category Counterfactual Queries provide rejection supervision. This reference-aware reasoning is distilled into APD-S, enabling unified localization and rejection from a single image--query pair. Experiments show that APD enables the resulting model to reject absent targets while also improving its localization of present targets.

---


### 178. [Efficient Confidence-Aware Densification for 3DGS](https://arxiv.org/abs/2610.13541)

**<font color=#1a73e8>作者：</font>** Manuel Hofer, Thomas Köhler, Felix Windisch 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3DGS-MCMC has replaced the gradient-driven density control of 3D Gaussian Splatting with opacity-based sampling and relocation, and is now the de facto standard for prior-free densification under a fixed primitive budget. Because opacity stays high where the scene is already well reconstructed, this sampling sends most new primitives to the foreground and leaves the background under-reconstructed. At low budgets, prior-based methods such as ConeGS and EDGS outperform it, at the cost of a pre-trained radiance field or dense image matches and a separate initialization stage. We argue for a comeback of error-driven densification within the fixed-budget MCMC framework. Our confidence-aware densification keeps the fixed budget and gradual growth of 3DGS-MCMC, but places primitives by the image error instead of the opacity. New primitives are drawn mostly where screen-space gradients are large. We favor primitives with a low learned confidence, which marks regions the reconstruction still explains poorly, and relocate the primitives that contribute least to the rendered images to these places. Averaged over 24 scenes, our method outperforms 3DGS-MCMC in PSNR, SSIM and LPIPS at every budget from 100k to 2M primitives. At 100k, without a prior or an initialization stage, it recovers 0.84dB of the 1.05dB PSNR by which ConeGS leads 3DGS-MCMC, and from 500k on, it has the highest PSNR and SSIM of all fixed-budget methods we compare with, including ConeGS and EDGS. While inherently prior-free, our densification can also exploit priors: from the ConeGS or EDGS initialization, it matches ConeGS in PSNR and SSIM at 100k and is best in all three metrics at 500k.

---


### 179. [MOSAIC: Multi-Scale Object-Centric Slot Adaptation with Image-Guided Prototype Conditioning for Remote Sensing Image Super-Resolution](https://arxiv.org/abs/2610.13547)

**<font color=#1a73e8>作者：</font>** Liuqian Wang, Hanyu Xie, Rongzhen Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained diffusion Transformers provide powerful generative priors for image restoration, yet adapting them to structure-sensitive tasks remains challenging. Existing methods mainly rely on dense low-resolution features as conditions, which often entangle salient objects with dominant backgrounds and provide limited abstraction for recurring structures across scales and samples. We propose MOSAIC, an object-centric representation learning framework that learns compact structural conditions for generative model adaptation. MOSAIC organizes degraded observations into structural slots that capture complementary object-level and layout-level evidence, integrates them across resolutions, and retrieves recurring priors from a shared prototype memory to complement incomplete image-specific information. The resulting representations are injected into selected layers of a frozen diffusion Transformer through lightweight residual modulation, preserving its pretrained generative prior. We instantiate MOSAIC for remote sensing image super-resolution, where small objects, repetitive structures, and large-scale variation provide a challenging testbed. Experiments on UCMerced, AID, and RSSCN7 show consistent PSNR improvements across $\times 2$ and $\times 4$ settings and favorable LPIPS results at $\times 4$. Qualitative results further demonstrate improved preservation of small objects, structural boundaries, and repetitive spatial patterns.

---


### 180. [ELMA: Benchmarking Anaphoric Compositions for Long-Term Text-to-Motion Generation](https://arxiv.org/abs/2610.13549)

**<font color=#1a73e8>作者：</font>** Shun Kato, Dixin Yang, Kotaro Amaya 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-guided long-term human motion generation is essential for applications such as continuously operating digital avatars. Despite recent progress on short clips, existing models struggle with multi-segment instructions that involve anaphora, where constraints established in earlier segments must be preserved over time. In this paper, we introduce a novel task of long-term motion generation from such anaphoric compositions. To mitigate this, we present ELMA, an episodic long-term motion dataset with dense segment-level annotations that preserve cross-segment dependencies. Built via a fully automated collection and filtering pipeline, ELMA extracts high-quality, continuous 30-second clips from in-the-wild videos, capturing the episodic narratives necessary for long-range state modeling. Leveraging this dataset, we fine-tune state-of-the-art motion generation models to incorporate long-range context. Extensive experiments reveal fundamental shortcomings in current models when handling context-dependent instructions. We demonstrate that ELMA enables significant improvements in both global physical realism and semantic alignment, setting a robust new baseline for long-term motion synthesis.

---


### 181. [Learning Holistic Scene Layout against View Shifts in Cross-View Geo-Localization](https://arxiv.org/abs/2610.13553)

**<font color=#1a73e8>作者：</font>** Chao Yang, Songlian Li, Zhigang Tu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-view geo-localization remains challenging due to drastic appearance variations and geometric distortions caused by viewpoint changes. Existing methods primarily rely on discriminative feature learning or explicit geometric alignment, yet often overlook an important observation: humans tend to match scenes by integrating the spatial context of multiple landmarks rather than relying solely on isolated local visual cues. Inspired by this, we propose a Spatial Context Modeling (SCM) module, which traverses feature maps along four orthogonal directions and models interactions among the resulting directional representations at each spatial position. By aggregating complementary directional observations, SCM constructs richer scene layout representations. Since reliable spatial context depends on robust visual features, we introduce a High-Frequency Information Guidance (HFIG) module that extracts stable structural cues from the frequency domain. By emphasizing edges and contours that are less sensitive to appearance variations, HFIG encourages the model to learn more robust representations. Extensive experiments demonstrate that our method achieves competitive performance on standard cross-view geo-localization benchmarks while exhibiting strong robustness under more challenging scenarios with unknown orientations and limited fields of view (FoVs).

---


### 182. [Probabilistic Ship Trajectory Forecasting using Transformer Models on AIS Data](https://arxiv.org/abs/2610.13557)

**<font color=#1a73e8>作者：</font>** Frederik E. T. Schöller  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Anticipation of vessel trajectories is an essential task when navigating at sea. This applies to both human navigators and autonomous surface vessels. Trajectory forecasting enables sub-routines such as collision avoidance to assess the situation and react accordingly in time. This paper investigates Transformer and Performer models for trajectory prediction of surface vessels in confined waters. Using widely available position data from the Automatic Identification System (AIS), candidate models are trained and evaluated. Historical information on how other vessels have moved in the local area surrounding each agent is conveyed using positional heat maps. The heat maps are generated using Kernel Density Estimation (KDE) and encoded with a Convolutional Neural Network (CNN) before entering the Transformer models. The models are trained with quantile loss to efficiently obtain a model-aware prediction interval, as this is crucial for timely collision avoidance. The proposed model architectures are shown to greatly outperform previous work while the inclusion of local heat maps enables the prediction of vessel movement that is not otherwise indicated from the previous positions.

---


### 183. [What We Talk About When We Talk About Emotion Editing](https://arxiv.org/abs/2610.13558)

**<font color=#1a73e8>作者：</font>** Xingzu Zhan, Lin Gu, Ruogu Fang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Emotional image editing aims to change the emotion a scene conveys while preserving its essential content. Because the same scene can support different emotional interpretations, achieving an emotional goal requires visual changes grounded in the source context. Motivated by the Component Process Model, which links emotional responses to event appraisal, we investigate neural representations as a reference for these editing decisions. Using TRIBE v2, an fMRI encoding model, we analyze 400 source-target pairs across eight emotion categories. Hidden states from EmoEdit, EmoEditor, and AffectDelta correspond more strongly to predicted target-image responses in visual regions than in affect-related regions. This imbalance motivates ROI-ReFT, which combines source visual responses as a content reference with a predicted affective response change as an editing direction. Two interacting branches use both conditions to guide a frozen editor throughout generation. Predicted responses of the generated image supervise affective change and constrain visual drift. On a post hoc selected subset of 400 editing requests, ROI-ReFT achieves 91.75% target-emotion accuracy and 83.25% joint success, with the same output both matching the target emotion and reaching source-output DINO-I of at least 0.80. Our code and dataset will be publicly released.

---


### 184. [Simultaneous Competitive and Regret Guarantees for TCP Acknowledgment](https://arxiv.org/abs/2610.13571)

**<font color=#1a73e8>作者：</font>** Tsubasa Harada, Yasushi Kawase, Hanna Sumita  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study simultaneous competitive and regret guarantees for TCP acknowledgment. Each acknowledgment serves all pending packets, and the objective is to minimize the total acknowledgment and waiting costs. It is well known that no deterministic online algorithm achieves a competitive ratio better than $2$. Given $k$ randomized online experts and $0<\varepsilon<1$, we construct a randomized online algorithm whose realized total cost is always at most $(2+\varepsilon)$ times the offline optimal cost $\mathrm{OPT}$ and whose expected regret against the expert with the smallest realized cost is $O(\sqrt{\mathrm{OPT}\log(k+1)}+\log(1/\varepsilon))$. The algorithm requires no advance knowledge of the number of packets or $\mathrm{OPT}$. Our algorithm controls switching costs between experts and uses the gap between the permitted competitive bound and its current cost to determine when to learn. We also prove lower bounds showing that, for $k\ge 2$, this regret bound is asymptotically optimal in $\mathrm{OPT}$, $k$, and $\varepsilon$, and that $\varepsilon>0$ is necessary for sublinear regret.

---


### 185. [$L_0$ Feature Selection via Monte Carlo Tree Search in High-Dimensional Financial Regression](https://arxiv.org/abs/2610.13574)

**<font color=#1a73e8>作者：</font>** Cameron Mouangue, Tristan Cazenave  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Feature selection is a central problem in high-dimensional financial regression, where large numbers of engineered variables and strong correlations among predictors reduce model stability and interpretability. $L_1$ regularization (Lasso) is widely used for sparse regression, but its shrinkage can be restrictive when informative signals are spread across correlated variables. Exact sparse regression avoids this shrinkage but requires solving a combinatorial optimization problem that is computationally difficult and is typically fit to minimize in-sample rather than out-of-sample error. This paper presents a feature selection framework based on Monte Carlo Tree Search with Generalized Nested Rollout Policy Adaptation (GNRPA). Feature selection is formulated as a sequential decision process, and candidate subsets are scored by their out-of-sample validation performance rather than training error. The method also supports a lexicographic objective accounting for subset size and multicollinearity. We study this approach on a contemporaneous explanatory regression task: explaining the weekly return of the NASDAQ-100 index from 1,072 engineered features spanning market, macroeconomic, and factor data. This isolates the value of subset selection under multicollinearity from the separate problem of predictive forecasting. On this task, the proposed method identifies sparse feature subsets with higher out-of-sample explanatory power than an optimized Lasso baseline, reaching an out-of-sample $R^2$ of 0.6961 versus 0.6313 for Lasso. These results suggest that Monte Carlo Tree Search is a practical alternative to convex regularization for sparse explanatory feature selection in financial regression, with potential value for factor attribution and risk decomposition where transparency matters as much as out-of-sample fit.

---


### 186. [Measuring Artifact Reliance in Machine-Generated Text Detectors](https://arxiv.org/abs/2610.13583)

**<font color=#1a73e8>作者：</font>** Anastasia Voznyuk, Andrey Grabovoy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Detectors of machine-generated text score almost perfectly on scientific-literature benchmarks, implying we can reliably distinguish with these detectors human and machine-generated documents. We looked at ten scientific-document subsets from six popular resources, and on several of them that apparent ease is a side effect of how the documents were put together. A logistic regression using 27 superficial features reached 0.833-0.997 macro-F1, and on the three arXiv subsets it outperformed every detector we evaluate with F1-scores 0.951-0.997. The strongest cue to the detector is the PDF extraction artifact: human texts retain their original line breaks, whereas generated texts are extracted as a single block of prose. This cue, together with three other formatting features, tell the classes apart at 0.996 AUC. To distinguish benchmarks that contain such a signal from detectors that rely on one, we introduce format counterfactuals: just re-wrapping a machine-written abstract without changing a single word reverses 20-27% of a public detector's correct decisions. Normalizing formatting before training reduces the generalization gap from 0.32 to 0.22. On format-clean benchmarks, it also raises out-of-domain macro-F1 from 0.33 to 0.65 for detectors trained on artifact-containing subsets.

---


### 187. [A Systematic Study of Security Enforcement at Android Inter-Component Boundaries](https://arxiv.org/abs/2610.13597)

**<font color=#1a73e8>作者：</font>** Sandiyo Christan A  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Android's inter-process communication (IPC) mechanisms (Activities, Services, BroadcastReceivers, ContentProviders, and URI scheme handlers) form the primary interface between applications and between applications and the system. We present a systematic study of security enforcement comprising 120 evaluations (99 inter-component interface evaluations across five interface categories, 10 platform security-control evaluations, and 11 dedicated positive controls) in over 30 Google and AOSP packages on Android 17 (API 37). Using an expected-versus-observed framework under a zero-permission attacker model, we evaluate whether each boundary's enforcement mechanism functions as designed. We find 97 enforcement gaps (80.8%) and 23 enforcement holds (19.2%). From these observations, we derive a 14-category enforcement gap taxonomy organized across manifest, code, platform, and architectural layers. Within our purposively selected corpus, observed enforcement outcomes differ substantially across interface categories: evaluated Activities and BroadcastReceivers exhibit a 100% gap rate, while ContentProviders, which benefit from framework-provided defenses such as setStrict(), achieve a 27.6% holds rate. We find that all seven evaluated platform compatibility changes with security intent are either disabled or gated at a targetSdkVersion that none of the applications in our evaluated corpus targets. We document 18 custom URI scheme registrations handling sensitive data (authentication tokens, payment credentials, medical information) despite the known unverifiability of custom schemes (RFC 8252 Section 8.1). Our study includes 23 positive controls, calibration cases demonstrating that the evaluation procedure distinguishes functioning enforcement from observed enforcement failures.

---


### 188. [EchoTab: Learning Measurement-Grounded Representations for Echocardiographic Diagnosis through Tabular Reconstruction](https://arxiv.org/abs/2610.13599)

**<font color=#1a73e8>作者：</font>** Michelle Espranita Liman, Ioana Ionac, Alexander Müller 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diagnostic information in multi-view medical imaging studies, like echocardiography, is distributed across views, each capturing different aspects of cardiac structure and function. In clinical practice, these views are first interpreted through quantitative measurements, which then support specific diagnoses. However, existing echo representation learning methods do not explicitly model measurements as an intermediate representation between views and diagnosis. As a result, individual measurements are not explicitly represented in a form that downstream diagnostic tasks can selectively use, hindering accurate diagnosis.
Inspired by this hierarchical clinical workflow, we introduce EchoTab, a measurement-grounded representation learning framework that represents multi-view echocardiography studies using measurement-specific tokens as an intermediate representation between echo views and diagnosis. Each measurement token selectively attends to the views relevant to its estimation and is trained through tabular reconstruction to predict the corresponding measurement value. The resulting tokens form a factorized echo representation, which encode clinically meaningful structural and functional properties and can be selectively used for downstream diagnosis. Unlike the commonly used contrastive approaches, EchoTab does not require negative samples or large batch sizes. Experiments on two datasets demonstrate that EchoTab learns effective measurement-grounded representations that improve diagnosis classification in multi-view echocardiography and its learned attention aligns with established measurement-view relationships used by cardiologists. Our code is accessible at this https URL.

---


### 189. [A small cognitive core explains human behavior at scale](https://arxiv.org/abs/2610.13603)

**<font color=#1a73e8>作者：</font>** Marcel Binz, Eric Schulz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Psychology has proposed many principles of cognition. Each, however, was developed in isolation, leaving their combined explanatory power unknown. We assembled a small set of established principles into one model, which we call COntextual Retrieval and Encoding (CORE). CORE consists of a hierarchy of episodic memories into which prediction errors are written and whose encoding, retrieval, and forgetting depend on context. Fitted jointly to 7,036,442 choices from 137 experiments, the model predicts human choices better than black-box models and reproduces 75% of reported behavioral effects when simulated. Moreover, its latent variables show classic signatures of Bayesian learning and event segmentation. Taken together, these findings suggest that a small cognitive core accounts for much of human behavior. They also open a path toward making psychology more than the sum of its parts, by building computational models on the entire experimental record.

---


### 190. [Thyroid Nodule Segmentation in Ultrasound Images with Conformal Uncertainty Estimation](https://arxiv.org/abs/2610.13604)

**<font color=#1a73e8>作者：</font>** Francesco Teodori, Pierpaolo Brutti, Umberto Ferraro Petrillo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Thyroid nodules affect a large proportion of the general population. Although most are benign, a non-negligible fraction is malignant. Ultrasound imaging is the primary diagnostic modality, and accurate nodule segmentation is a prerequisite for CAD systems to classify malignancy and assess metastatic risk.\\ In this work, we propose a thyroid nodule segmentation framework that integrates a DeepLabV3+, channel-attention modules and post-hoc conformal prediction, providing both accurate mask and pixel-level uncertainty estimates. We address thyroid ultrasound nodule segmentation as the first stage of a pipeline that also includes malignancy classification and metastatic risk prediction. We adopt DeepLabV3+, whose Atrous Spatial Pyramid Pooling (ASPP) captures multi-scale context, with an EfficientNet-B5 backbone for its accuracy-efficiency trade-off. Additionally, we test three channel-attention modules: Squeeze-and-Excitation, CBAM and Grouped Channel Attention (GCA), paired with two loss formulations (Dice-BCE and Boundary).\\ Since binary masks do not indicate prediction confidence, we wrap the trained model with a split conformal prediction layer that produces pixel-level uncertainty maps with statistical coverage guarantees.\\ We evaluate all configurations on the TN3K public benchmark using a fixed split and directly compare them with state-of-the-art methods. The plain backbone already improves upon previously reported results, with CBAM + Dice-BCE emerging as the best overall configuration.

---


### 191. [CUBE: Class-conditioned Unknown Boundary Evidence for Open-Set Insect Species Recognition](https://arxiv.org/abs/2610.13610)

**<font color=#1a73e8>作者：</font>** Hao Tan, Qimin Zhang, Zhe Xiao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-set insect species recognition faces significant challenges when deployed in real-world biodiversity scenarios, particularly when encountering unknown species that are visually close to known training classes. Unlike generic out-of-distribution samples, fine-grained unknown insects are often not visually anomalous. They instead tend to appear near the decision boundary of specific known species, leading to unreliable closed-set predictions. To address these challenges, we propose \textbf{Class-conditioned Unknown Boundary Evidence (CUBE)}, a novel evidence-based framework that models unknownness around each known species rather than as a single global unknown class. Our key idea is to evaluate a test sample relative to the known species it most closely resembles, enabling local rejection for visually confusable unknown insects. CUBE learns class-conditioned boundary evidence from auxiliary species, preserves auxiliary species as shadow references during inference, and incorporates taxonomic candidate calibration to verify biological plausibility. When ecological metadata is available, we further introduce CUBE-E, which adds a lightweight location-consistency term without modifying the visual backbone. Experiments on the Open-Insect C-America benchmark show that CUBE achieves superior performance, outperforming state-of-the-art baselines with 95.8\%, 98.7\%, and 99.1\% AUROC on local, non-local, and non-moth unknown splits, respectively, while maintaining 94.9\% closed-set accuracy. With ecological metadata, CUBE-E further improves the results to 96.0\%, 99.7\%, and 99.5\% AUROC with 95.2\% closed-set accuracy.

---


### 192. [Private and Distributionally Robust Federated Multiclass Classification](https://arxiv.org/abs/2610.13631)

**<font color=#1a73e8>作者：</font>** Andrea P. Hernandez, Michael Ibrahim, Nagi Gebraeel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fault diagnosis in asset-intensive industries requires multiclass models trained on noisy, sensitive data collected across geographically distributed client sites. Federated learning enables collaborative training without centralizing data, but most approaches do not provide formal privacy guarantees for individual records stored at client sites and can degrade under label noise. To address these limitations, we develop a differentially private, distributionally robust framework for federated multiclass classification that provides sample-level privacy for records stored at each client. We build on a federated Wasserstein distributionally robust multiclass objective with the Crammer-Singer loss, solved using an Alternating Direction Method of Multipliers (ADMM)-based algorithm. To protect the released client updates, our method injects calibrated Gaussian noise into the proximal linearized client updates of both the local model and the local distributionally robust variable before aggregation at the central server, and we quantify the cumulative privacy loss using the moments accountant. We provide per-round sample-level $(\epsilon,\delta)$-differential privacy guarantees and an overall composed privacy guarantee across all training rounds, together with convergence results and an explicit privacy-utility tradeoff. Experiments on simulated industrial fault data and UCI benchmark datasets show that our method outperforms differentially private federated empirical risk minimization and stochastic gradient descent baselines in most tested settings, with the largest gains under strong privacy-induced noise.

---


### 193. [PANDA: Prior-guided Attentional Dual-path Architecture](https://arxiv.org/abs/2610.13635)

**<font color=#1a73e8>作者：</font>** Rishabh Jain, Federico Belotti, Stefano Coniglio 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hypergraph Neural Networks (HNNs), designed to model higher-order relations beyond pairwise interactions, typically rely either on fixed structural weights or on normalised attention. Fixed weights can propagate misleading information in heterophilic settings, while normalisation makes attention coefficients competitive, in the sense that, in a message-passing framework, increasing the weight of one sender must reduce the weight of others in the same aggregation set. Our main contribution is the introduction of PANDA (Prior-guided AttentioNal Dual-path Architecture), a plug-in for two-stage message passing HNNs applicable to both undirected and directed settings. The main path interpolates between learned receiver-normalised attention and structural incidence priors, while a non-competitive (not normalised) auxiliary path lets each sender contribute its own transformed information. We also show that, with fixed structural coefficients, PANDA recovers a certain complex-valued convolution operator adopted in previous works. Across four HNNs spanning spatial and spectral methods in both directed and undirected settings, plugging PANDA in yields an average improvement of 5.18 percentage points across eight real-world benchmark datasets. The code is available at this https URL.

---


### 194. [Learning Size Independent Constraint Models from Input Data and Positive and Negative Example Solutions](https://arxiv.org/abs/2610.13640)

**<font color=#1a73e8>作者：</font>** Helmut Simonis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this paper we describe a Constraint Acquisition Tool that generates size independent constraint programs from input data and positive and negative example solutions of multiple problem instances. The system finds size specific models based on typical constraint patterns over global and binary constraints, then generalizes the models to a size independent model that can be run on unseen input data. The system produces MiniZinc code as well as a textual description of the model. We evaluate the tool on the example problems of the PTHG21 Challenge and show the feasibility of the approach.

---


### 195. [SelectArena: A Modern Benchmark for Feature Selection on Real-world Tabular Data](https://arxiv.org/abs/2610.13644)

**<font color=#1a73e8>作者：</font>** Bastian Schäfer, Dominika Matus, Lennart Purucker 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Selecting a subset of features (columns) from a tabular dataset is a ubiquitous challenge in real-world applications. Industry experts seek to minimize model training costs, climate scientists require an interpretable subset of factors to understand extreme weather events, and clinicians need to choose among diagnostic tests due to financial and time constraints. When looking at the scientific literature to determine which feature selection method to use, practitioners across domains face an unrepresentative landscape of benchmarking. Despite extensive research, existing feature selection benchmarks provide limited guidance because they rely on outdated models, ad hoc evaluation protocols, or artificially generated data that do not reflect real-world problems. To close the gap between scientific benchmarking and real-world applications, we introduce SelectArena, a modern benchmark for feature selection. We compare 15 widely used feature selection methods on 71 manually curated real-world tabular datasets, covering classification and regression problems, using standardized evaluation protocols and state-of-the-art tabular (foundation) models. Our results reveal clear trade-offs across predictive performance, runtime, stability, and validity. Tree-based methods, CART and RFImportance, along with F-Test are Pareto-optimal when taking into account predictive performance and runtime. F-Test, information-theory-, and distance-based methods lead on stability and validity, with F-Test emerging as a balanced choice across our metrics. Search-based methods are slow, unstable and achieve low performance. SelectArena turns these findings into practical guidance and, as an extensible platform, supports future feature selection research.

---


### 196. [Pretraining and Test-Time Training Budgets Matter for ARC: A Controlled Study of VARC and TRM](https://arxiv.org/abs/2610.13660)

**<font color=#1a73e8>作者：</font>** Adrien Deliege, Marc Van Droogenbroeck  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Abstraction and Reasoning Corpus (ARC) is increasingly used to evaluate whether neural networks can infer task-specific transformations from few demonstrations. Recent ARC models differ in architecture, but also in broader training and evaluation protocols, including pretraining data, data augmentation, test-time setup, and optimization budgets, making conclusions about architecture benefits debatable. In this work, we study how the performance of the vision-inspired VARC and recursion-based TRM models is affected by pretraining and test-time training (TTT) budgets under a common inductive protocol on ARC-AGI-1. We cross five pretraining budgets with four TTT budgets for each test task. Each budget specifies a task-variant count and total sample presentations, defining the controlled training budgets. We observe that increasing TTT sample presentations improves the standard ARC pass@2 metric in all settings for both models. Increasing the TTT task-variant count consistently helps only TRM, whereas VARC often performs better with fewer variants. VARC also remains competitive without pretraining, while TRM benefits much more from it. These results show that pretraining and TTT budgets affect ARC evaluation and motivate reporting at comparable budgets.

---


### 197. [Retractions Revisited: A Replication, Extension, and Mechanistic Evaluation of Linguistic Obfuscation Effects in Fraudulent Science](https://arxiv.org/abs/2610.13678)

**<font color=#1a73e8>作者：</font>** David M. Markowitz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prior work suggests fraudulent scientists write their articles with higher rates of linguistic obfuscation than genuine scientists, with a possible mechanism suggesting obfuscation makes research more costly for a reader to analyze. This result has not undergone additional empirical scrutiny in the open science era, nor have other psychological mechanisms been evaluated. The current replication and extension addressed this opportunity by comparing 800 fraudulent and 800 genuine control papers (2013-2025). The results supported the linguistic obfuscation hypothesis, suggesting fraudulent papers were more obfuscated than genuine ones. A parallel mediation model evaluated three competing mechanisms, finding that reality monitoring, as measured through decreased rates of adjectives, best explained the link between fraudulent science and linguistic obfuscation. Cross-validated detection accuracy using obfuscation features (60.7%) and an elastic net of over 100 language dimensions (71.6%) were significantly greater than chance. Implications for scientific fraud and psychology of language research are discussed.

---


### 198. [PhysForge: Material-Controllable 3D Reconstruction with Separable Components](https://arxiv.org/abs/2610.13681)

**<font color=#1a73e8>作者：</font>** Yuchen Wang, Yanqi Bao, Zheng Gu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in physical 3D generation have enabled visually faithful assets with simulatable mechanical behavior. However, existing methods provide limited control over material behavior beyond appearance-based inference and struggle to estimate physical properties from complex interactions between objects and semantic parts. Therefore, we present PhysForge, a Video Diffusion Model (VDM)-based framework for addressing these challenges, comprising two complementary modules for material-controllable physical fitting and componentlevel interaction modeling. The first, PhysFit, leverages material-conditioned VDM dynamics as references for physical-property fitting, introducing windowed fitting to focus on material-revealing interactions and Hallucinated Forcing to disentangle nonphysical motion hallucinated by the VDM from material responses. The second, PhysComp decomposes complex interactions into individual objects and semantic components, enabling their physical parameters to be optimized independently and flexibly composed for joint simulation. Experiments on PhysAssets and Google Scanned Objects demonstrate that, compared with existing methods, PhysForge provides stronger control over material-dependent physical responses while supporting component-level physical modeling for complex interactions. It achieves the best CLIP and physical controllability scores on both common and uncommon materials, with qualitative comparisons, component-level ablations, and a user study further supporting these improvements. Our project page is available at this https URL .

---


### 199. [X-AVDD: Cross-Attentive Audio-Visual Dataset Distillation](https://arxiv.org/abs/2610.13687)

**<font color=#1a73e8>作者：</font>** Saumyaranjan Mohanty, Aravind Reddy, Konda Reddy Mopuri  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-visual dataset distillation aims to synthesize a small dataset from a large paired audio-visual dataset, while nearly preserving the training utility for neural networks. Existing approaches such as DM and AVDD face two critical limitations: 1) they are memory-intensive, making them difficult to scale to complex architectures and higher samples-per-class (SPC) settings, and 2) they often fail to preserve strong cross-modal semantic correspondence. To tackle these issues, we propose X-AVDD, a cross-attention-based distillation method that explicitly captures inter-modal relationships during synthesis. By decoupling cross-modal alignment from joint optimization, X-AVDD is substantially more memory-efficient, reducing end-to-end synthesis cost by $\sim 8\times$ GPU-hours, while producing highly aligned synthetic data. Empirically, X-AVDD significantly outperforms other audio-visual distillation methods. On VGGSound, an audio-visual dataset of short YouTube clips, X-AVDD improves top-1 test accuracy from $8.2\%\rightarrow24.0\%$ at SPC=$10$ and $9.8\%\rightarrow26.5\%$ at SPC=$20$. Furthermore, X-AVDD improves cross-architecture generalization (e.g., $25.5\%\rightarrow35.3\%$ for a ViT target on AVE dataset at SPC $=50$) and successfully scales to complex architectures such as AudioCLIP, achieving $62.3\%$ accuracy using only $5.65\%$ of the full dataset, against the full dataset accuracy of $72.4\%$ while completing in $9\times$ lower training time compared to the full dataset.

---


### 200. [VQIL: Visible Quantum Interference Learning for Perturbation Response Ranking on Graphs](https://arxiv.org/abs/2610.13689)

**<font color=#1a73e8>作者：</font>** Seokjun Lee, Sergio A. Ortega, Daniel K. Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning how local perturbations affect a network is important for identifying which components drive or absorb a system's response. We formulate this as seed-conditioned response ranking: given a perturbation at one seed node, ranking all other nodes by response strength. This is challenging when the model is given only the interaction topology, while the mechanism governing how perturbations propagate must be learned from data. We present VQIL (Visible Quantum Interference Learning), a trainable Szegedy quantum walk for seed-conditioned ranking. Edge weights, link phases, and per-node phase rotations are optimized end-to-end by backpropagation while the walk operator remains unitary throughout training. Node scores are obtained from a geometrically discounted coherent sum of quantum-walk amplitudes, enabling quantum interference before the final squared-norm readout. Because each learned parameter is attached to a named edge or node, the trained model provides directly inspectable hypotheses about the roles of individual graph components in the propagation mechanism. On AC power-flow perturbations over six transmission grids, with electrical parameters withheld from the model, VQIL improves Spearman rank correlation from 0.147 for the untrained walk to 0.831 and outperforms an identically trained random-walk model. On gene perturbation over five protein-protein interaction networks with Perturb-seq supervision, VQIL improves rank correlation from 0.171 to 0.620, outperforming the strongest learned classical and neural baselines. These results show that trainable quantum-walk interference provides a scalable and interpretable inductive bias for learning seed-conditioned response rankings on graphs.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-244](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
