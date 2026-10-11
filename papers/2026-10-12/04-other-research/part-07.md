# 📦 其他研究 | 2026年10月12日

> 本类共 **329** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-329**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-329**

---

### 301. [RiCo: Neural Simulation of Rigid-Body Interactions via Local Contact Reasoning](https://arxiv.org/abs/2610.12333)

**<font color=#1a73e8>作者：</font>** Ruixiang Ouyang, Guanren Qiao, Fansen Meng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate simulation of rigid-body interactions is essential for predictive physical world models. Despite recent progress in modeling object dynamics, capturing how local contacts between surfaces shape object motion remains challenging. While end-to-end world models predict interactions across entire scenes or objects, in practice, rigid-body contact is inherently local, and only nearby surfaces can directly exchange contact forces. Motivated by this observation, we introduce Rigid-body Contact Reasoning (RiCo), which represents interactions between objects through sparse neighborhoods of contact surface points. RiCo combines each point's state with the relative geometry, motion, and physical properties of nearby surfaces, then reasons across the object's points to determine how these local contacts jointly affect its motion. By confining cross-object reasoning to nearby surfaces while propagating contact information within each rigid body, RiCo retains fine-grained interaction details without the cost of modeling every pair of scene points. Such properties enable RiCo a higher accuracy and contact fidelity. Experiments on MOVi-benchmark demonstrate that RiCo reduces 100-frame position and orientation errors by 31-35% and approximately 38%, respectively, compared with baselines. Moreover, RiCo achieves high contact fidelity, with ground-truth-relative penetration-time and mean-depth differences of 11.0% and 2.22 mm, respectively. RiCo further generalizes zero-shot from small-scale training scenarios to scenes containing 270 objects. Our real-world multi-ball collision experiments further provide preliminary evidence of sim-to-real transfer.

---


### 302. [ContiLNN: Mitigating Slice Sampling Discontinuity with Liquid Neural Networks for Medical Image Restoration](https://arxiv.org/abs/2610.12337)

**<font color=#1a73e8>作者：</font>** Jialei He, Enhe Liu, Sifan Song 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Anatomical continuity provides complementary information for medical image restoration, but its use requires accounting for local anatomy and variations in slice sampling. We introduce ContiLNN, which augments two-dimensional restoration backbones with bidirectional closed-form continuous-time (Bi-CfC) modules for cross-slice modeling while retaining in-plane feature extraction. Slice-index intervals modulate gates determined by local features and hidden states, enabling propagation to respond to sampling variations without numerical ODE integration. Reference-guided consistency aligns first- and second-order cross-slice intensity differences to preserve anatomical variation, while distillation from a frozen backbone helps retain in-plane fidelity. Across five training seeds, ContiLNN improves mean PSNR over Restore-RWKV by 0.1907, 1.0176, and 1.2482 dB for CT denoising, MRI super-resolution, and reduced-count PET restoration, respectively, with lower RMSE in all three tasks. CT results are descriptive for one held-out patient. PET ablations support ordered propagation beyond additional pointwise capacity. Under contiguous training, Bi-CfC achieves higher fidelity than a Bi-GRU with similar parameter counts and arithmetic costs across all tested sampling conditions. Matched seven-slice profiling shows 52.8% lower latency and 57.0% lower peak GPU memory use than Bi-GRU. Mixed-gap training improves sparse and irregular-context performance for both operators, without a uniform ranking across metrics and contexts. Experiments with fewer training patients and a second backbone further support data efficiency and backbone compatibility.

---


### 303. [Ambient Discrete Diffusion: Using the Wrong Data at the Right Time for Data Efficient Learning](https://arxiv.org/abs/2610.12340)

**<font color=#1a73e8>作者：</font>** Julian Kleutgens, Mauricio Tec, Claudio Battiloro 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce RefineMix, a framework for training discrete diffusion models under severe data scarcity, a common constraint in scientific applications. RefineMix uses out-of-distribution data at selected diffusion times to improve generalization without biasing the sampling distribution. Although this strategy has been explored in continuous diffusion, discrete diffusion presents a distinct challenge: unlike Gaussian noise, masking preserves domain information in surviving tokens, limiting the use of related data at high noise levels. At low noise levels, however, the domains effectively disjoint supports become an advantage, allowing the model to learn from both in-domain and out-of-distribution data without biasing the sampler. We formalize these intuitions and provide a theoretical analysis for the proposed method. Experimentally, across five domain-shift settings, RefineMix matches or outperforms in-domain finetuning and data mixing. For protein sequence generation, finetuning with just 197 in-domain examples nearly doubles the fraction of generated proteins that are simultaneously novel, foldable, and in-family compared to standard finetuning.

---


### 304. [SplitJEPA: Learning Invariant and Variant Latent Worlds without Reconstruction](https://arxiv.org/abs/2610.12349)

**<font color=#1a73e8>作者：</font>** Ruijin Hua, Zichuan Liu, Zhuokai Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding a dynamical world calls for more than a latent state that summarizes its observations: the state should also be organized into the factors that stay shared across related observations and the factors that vary between them. For example, a robot pushing a cube to a goal should take the same action when the camera shifts or the lights dim, since nothing in the scene has moved. Existing approaches to this decomposition commonly obtain it through reconstruction, so the latent variables must first explain the entire observational world before their organization can be trusted. Joint embedding predictive architectures (JEPAs) model the latent state directly and never reconstruct, yet no existing result recovers the invariant and variant parts of the state they learn. How to learn the invariant-variant structure of the latent world without paying for its reconstruction therefore remains open. To close this gap, we introduce SplitJEPA, a JEPA that jointly recovers the latent state and its invariant and variant organization directly in representation space, without any reconstruction. We prove that, under stationary Gaussian predictive dynamics and a full-rank variation condition, SplitJEPA identifies the invariant and variant subspaces up to independent block-wise isometries, without introducing an observation decoder. Since the guarantee needs no decoder, the result extends reconstruction-free latent recovery to invariant-variant block identification. Experiments on synthetic nonlinear systems and robotic manipulation tasks support the theoretical results and show their practical value for both robustness and efficiency.

---


### 305. [Closing the Horizon Gap in Policy Optimization for Adversarial MDPs](https://arxiv.org/abs/2610.12362)

**<font color=#1a73e8>作者：</font>** Mingyi Li, Taira Tsuchiya  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider policy optimization for online episodic tabular Markov decision processes (MDPs) with adversarial losses and bandit feedback. Policy optimization updates the policy locally at each state and avoids optimization over the occupancy-measure polytope, but its existing regret bounds are larger by a factor of the horizon $H$ than those of occupancy-measure-based algorithms. We close this gap by using regularized $Q$-functions, which allow us to control the stability of the local updates jointly over all state-action pairs rather than separately at each state. The resulting algorithm attains high-probability regret bounds of $\widetilde O(\sqrt{HS(H+A)T})$ for known transitions and $\widetilde O(HS\sqrt{AT})$ for unknown transitions, where $S$ is the number of states, $A$ the number of actions, and $T$ the number of episodes. Both bounds improve the horizon dependence of existing policy optimization bounds, and the latter matches the best-known bound. We further extend the algorithm to adversarial linear-mixture MDPs and obtain the same improvement in the horizon dependence.

---


### 306. [HANS: A Handwritten Answer Sheet Dataset for Noisy Hybrid Document Parsing](https://arxiv.org/abs/2610.12363)

**<font color=#1a73e8>作者：</font>** Xiazhen Wu, Wansong Qin, Yangbin Zheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Intelligent grading and automated scoring technologies constitute critical infrastructure for smart education. However, existing document parsing and handwriting recognition benchmarks are predominantly designed for well-structured printed documents or isolated mathematical expressions, lacking datasets that capture the complex characteristics inherent to student answer sheets, including multi-line derivation processes, heterogeneous mixtures of text and mathematical formulae, and noise artifacts such as strikethroughs. To address this gap, we introduce HANS, the first dataset explicitly constructed for real-world educational scenarios, encompassing mathematical expressions, natural language text, hand-drawn tables, and diverse noise patterns including corrections and deletions, accompanied by fine-grained annotations that establish a reliable foundation for robust recognition research. Building upon HANS, we propose NA-GOT, an end-to-end framework that achieves two-stage noise suppression through a lightweight noise suppression module operating at the feature level, complemented by a noiseaware attention mechanism incorporated into the decoding stage. Experimental results demonstrate that HANS poses substantial challenges to existing methods, while NA-GOT achieves significant improvements in both accuracy and stability for answer process recognition. The dataset will be made publicly available upon publication.

---


### 307. [Bilevel optimization for data-driven learning of Koopman embeddings using kernel-based autoencoders](https://arxiv.org/abs/2610.12370)

**<font color=#1a73e8>作者：</font>** Joel-Pascal Ntwali N'konzi, Feliks Nüske, Stefan Klus  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Koopman operator theory provides a linear framework for analyzing nonlinear dynamical systems and has become a major tool for data-driven modeling. A central challenge, however, is that finite-dimensional approximations computed by methods such as extended dynamic mode decomposition (EDMD) require the dictionary to be specified a priori. Recent machine-learning approaches address this limitation by learning the dictionary from data, predominantly using artificial neural network (ANN) autoencoder architectures. Although kernel methods offer an alternative with greater interpretability and tractability for theoretical analysis, they have received little attention in this setting. We introduce extended dynamic mode decomposition with kernel-based dictionary learning (EDMD-kDL), a kernel-based method for learning finite-dimensional Koopman embeddings directly from data. The method combines ideas from collocation methods and bilevel optimization to simultaneously learn a kernel dictionary and the corresponding Koopman approximation. We evaluate EDMD-kDL against state-of-the-art ANN-based approaches on a range of numerical experiments, including global sea-surface-temperature forecasting and learning directly from video data. Across all tested settings, EDMD-kDL achieves performance comparable to or better than the ANN-based methods. Moreover, in contrast to standard kernel methods, the proposed approach is scalable to large datasets by design since the size of the required kernel matrices depends on the number of collocation points rather than the size of the training dataset.

---


### 308. [AgentGarten: Code Worlds for Evolving Agents](https://arxiv.org/abs/2610.12374)

**<font color=#1a73e8>作者：</font>** Jiawei Chi, Shangchen Miao, Zhiyuan Shi 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive virtual worlds allow agents to learn through exploration and interaction. What agents can learn is bounded by the environments they practice in, which must be faithful, with consistent state, rules, and dynamics, and realistic, with observations that follow the real-world visual distributions. Achieving both across diverse worlds remains a bottleneck. We introduce AgentGarten, a framework that couples simulators and game engines with a shared neural renderer to build real-time interactive environments. Its simulation backends maintain persistent world state and execute program-defined interaction rules, while the renderer generates visual observations from structured conditions exported through a common interface. To build the neural renderer, we adapt a pretrained video model to geometry conditions, distill it with our proposed Adversarial Forcing, and optimize inference for real-time interaction. Adversarial Forcing makes history prefilling differentiable through exact replay, so that losses on later predictions update how the renderer encodes prior observations, and adds real-data adversarial supervision to improve its visual quality. In AgentGarten, agents perceive the world through visual observations, interact with it in real time, and improve by distilling each round of experience into playbooks that subsequent agents inherit and refine. Our empirical study demonstrates a substantial gain in learning efficiency, with agents learning from just 4 rounds compared with millions for a conventional reinforcement learning counterpart. As new worlds can be written as code and rendered through the same interface, environments can scale in both number and difficulty alongside their agents, a step toward agents that keep evolving through interactive experience.

---


### 309. [Latent Core Tokenizer: Compress, but Meaningfully](https://arxiv.org/abs/2610.12376)

**<font color=#1a73e8>作者：</font>** Felermino D. M. A. Ali, Millicent Ochieng, Ogbemi Ekwejunor-Etchie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tokenizers are commonly optimized for compression, but a compact vocabulary does not necessarily distribute its capacity evenly across languages. We introduce the Latent Core Tokenizer (LCT), a language-agnostic approach that separates structural discovery from vocabulary construction. LCT uses Minimum Description Length, entropy-based boundary signals, and morphotactic constraints to identify reusable linguistic units before constructing a shared vocabulary. Across 104 languages with a 200K-token vocabulary, LCT achieves lower fertility and higher MorphScore than BPE, Unigram, and parity-aware BPE, while maintaining comparable cross-lingual disparity in tokenization cost. Across four multilingual downstream benchmarks, LCT improves aggregate score by 1.48, 1.83, and 2.00 points over BPE, Unigram, and parity-aware BPE, respectively. Our findings show that compression alone does not predict representation quality and highlight the importance of morphology-driven structural discovery and how frequency is used to allocate the final vocabulary across languages.

---


### 310. [Marformer: A Transformer for Predicting Missing Data Distributions](https://arxiv.org/abs/2610.12379)

**<font color=#1a73e8>作者：</font>** Prabhav Singh, Xiheng Tom Wang, Haojun Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real decisions are made under incomplete information. If we observe only some of the random variables we need, we can predict the others. The \textbf{conditional marginals} over the missing variables are the key ingredient for computing Bayes risk and Value of Information (VOI), the expected gain from acquiring one more observation before deciding. We present the Marformer, a Transformer trained to directly predict conditional marginals given any set of observed values. Like BERT, which is trained to predict missing words from context, the Marformer constructs a hidden-vector representation for each distribution $p(X_i)$ and iteratively refines it through attention to other distributions $p(X_j)$. Unlike generative approaches, the Marformer does not model the full joint distribution, requires no domain knowledge of the data-generating process, and makes all predictions in a single forward pass. We evaluate across three synthetic domains with missing data---Bayesian networks, discretized multivariate Gaussians, and structured annotation data. The Marformer can match or outperform classical missing-data methods, even when those methods are given the true model family and prior that generated the synthetic data. We also evaluate on a real annotation dataset, where the Marformer outperforms the evaluated baselines at the largest training size. In both cases, the Marformer is substantially faster than the evaluated generative baselines.

---


### 311. [GenIA: Generative Reconstruction with Test-Time Input Alignment](https://arxiv.org/abs/2610.12388)

**<font color=#1a73e8>作者：</font>** Stefano Esposito, Naama Pearl, Polina Karpikova 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing complete 3D object assets from monocular or sparse multi-view observations remains challenging. Generative 3D foundation models can complete object geometry beyond the observed views, but their predictions may not faithfully reproduce the observed geometry, appearance, or pose. We introduce GenIA, a framework for test-time input-aligned generation that grounds SAM3D's generative prior in geometric and photometric observations without retraining the foundation model. We improve object pose by deriving translation and scale from geometry while retaining the learned rotation prior, and align appearance through visibility-biased attention, cross-observation fusion, and differentiable rendering guidance during denoising. An optional post-denoising refinement further adapts the appearance latent, lightweight decoder adapters, and object placement to the observations. Our framework also supports externally supplied geometry; when given temporal shapes of dynamic objects, it recovers a shared, input-aligned canonical appearance and stable world-space placement. Across synthetic and real benchmarks, GenIA improves pose prediction and object reconstruction from monocular, multi-view, and dynamic inputs, outperforming recent optimization-based, per-frame image-to-3D, and video-to-4D methods. Our project page is available at this https URL.

---


### 312. [HRIL: Learning Multimodal Synergy via Higher-Order Tensor Modeling](https://arxiv.org/abs/2610.12393)

**<font color=#1a73e8>作者：</font>** Qun Dai, Liangjian Wen, Jiang Duan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-supervised multimodal representation learning has achieved remarkable success across diverse domains, yet capturing synergistic information remains challenging due to the complexity of cross-modal interactions. Unlike the shared information across individual modalities, synergy arises when task-relevant signals emerge only from the joint configuration of multiple modalities and cannot be recovered from any modality in isolation. This work focuses on how to preserve the information capacity for such synergistic signals in multimodal representations. The key observation is that synergistic information is reflected in higher-order statistical dependence among modalities, which provides a principled target for explicitly modeling joint interactions. Motivated by this insight, we propose Higher-order Representation and Information Learning (HRIL), which constructs an empirical cross-moment tensor over modality embeddings to represent multi-way interactions. HRIL employs Tucker decomposition to obtain a core tensor, complemented by a synergy-aware regularizer that prevents energy concentration and preserves higher-order coupling capacity for synergistic information capture. Experiments on the controlled synergy task and real-world benchmarks demonstrate consistent improvements over existing multimodal contrastive methods, with notable gains on tasks dominated by synergistic interactions. Code is released at this https URL.

---


### 313. [Prospective Prediction of OOD Degradation from Source-Side Training Dynamics](https://arxiv.org/abs/2610.12397)

**<font color=#1a73e8>作者：</font>** Sasha, Monin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study whether persistent out-of-distribution (OOD) degradation can be predicted before it is directly observed using only source-side training dynamics. In a controlled shortcut-learning setting, a simple logistic regression predictor develops a clear prospective signal, while training time alone does not. Temporal summaries of the source-side quantities are substantially more informative than their current values. When transferred without additional training from a CNN to an MLP, confidence and entropy dynamics retain substantial predictive information. These results provide a proof of principle that source-side training dynamics can contain an early warning signal for future OOD failure.

---


### 314. [SpaceFlow: Locally Controllable 3D Generation](https://arxiv.org/abs/2610.12399)

**<font color=#1a73e8>作者：</font>** Neil De La Fuente, Joan Lafuente, Mukhammadali Sayfiddinov 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current 3D generation methods lack explicit local control: geometric adherence is often defined by a global control strength, and appearance cannot be specified locally. We present SpaceFlow, a training-free pipeline for locally controllable 3D generation from text descriptions and a collection of geometric primitives. Each primitive serves as a proxy for an object part and is assigned a local control level, enabling users to specify whether regions should strictly follow the input shape or allow generative completion. During structure generation, we enforce these spatial constraints within the generative flow process. For appearance synthesis, the generated structure is segmented and matched to the primitives. Each generated part is conditioned only on its assigned text or image cue, thereby limiting cross-part leakage. Regional geometry metrics demonstrate that SpaceFlow preserves the specified geometry in high-control regions and enables plausible shape variation in low-control areas. A user study further indicates that the resulting balance between geometric fidelity and generative freedom remains competitive in overall quality. When evaluating appearance on fixed geometry, text-conditioned routing achieves state-of-the-art prompt faithfulness and color/material accuracy. Qualitative results additionally show localized routing of image cues. The project page is available at this http URL.

---


### 315. [Learning Kilometer-Scale Weather Prediction with Global-Regional Alignment](https://arxiv.org/abs/2610.12401)

**<font color=#1a73e8>作者：</font>** Guowen Li, Yang Liu, Yujie Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kilometer-scale regional weather forecasting is essential for local weather warnings and weather-sensitive decisions. Existing data-driven approaches often rely on numerical forecasts for large-scale guidance or require additional training of global forecasting components. Pretrained global weather models offer an efficient source of large-scale forecasts, motivating their reuse to guide high-resolution regional prediction. However, this coupling requires aligning global and regional representations across different grids and integrating global guidance with local interactions to advance regional states. We propose ScaleCast, a regional forecasting framework that addresses these challenges through Global-Regional Alignment. Its Global-Regional Conversion module aligns joint global and regional representations with regional locations, while the Global-Regional Alignment and Dynamics block combines aligned guidance with regional neighborhood interactions. Experiments using ERA5 global analyses on a 0.25-degree grid and CERRA regional reanalysis at 5.5 km spacing demonstrate improved regional forecasts across surface and upper-air variables, with a single trained model supporting multiple global forecast drivers (i.e., Pangu-Weather, GraphCast, and HRES) without specific retraining. Fine-tuning on HRRR at 3 km spacing further demonstrates the framework's adaptability to a different regional domain and spatial resolution. Windstorm case studies show improved cyclone positioning and core-pressure estimates, while comparisons with HadISD station observations show closer agreement with local temperature and humidity changes.

---


### 316. [Searching for "Harmful Refusal": A Psychometric Audit of an AI Safety Benchmark](https://arxiv.org/abs/2610.12409)

**<font color=#1a73e8>作者：</font>** Christopher M. Stewart, Preston Botter, Natalie Sarabosing 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety benchmarks typically report one overall score for a suite of datasets, each of which may target one or more safety-related attributes, so models with similar overall scores can have very different attribute profiles. Comparing models is more tractable at the level of individual attributes, yet it is often unclear whether even a single dataset's scores isolate any single attribute. One plausible candidate for such an attribute is harmful refusal, a model's tendency to refuse dangerous or policy-violating prompts. We examine whether it constitutes a single, measurable attribute in HELM Safety. Using a construct validity framework that stipulates that an attribute must exist before a test can measure it, we start with HELM Safety's four datasets that might plausibly target harmful refusal, but find that three are saturated. We subject the remaining dataset, HarmBench, to two psychometric tests to determine if a single attribute like harmful refusal could stand behind its score. First, multidimensional item response theory modeling strongly suggests that HarmBench does not measure a singular attribute. Second, a differential item functioning analysis finds items where models from different developers with the same refusal ability score differently. These flags largely disappear under scope-specific matching, a pattern consistent with aggregation effects but not sufficient to rule out domain-specific developer differences. Zooming out, HarmBench collapses distinct harm behaviors into one score, and the overall HELM safety aggregate further collapses HarmBench and scores from other datasets into a single top-line number. Any safety score that averages over datasets and items can hide saturation and conflate behaviors this way. We argue that a score should earn its single-attribute reading before models are compared with it.

---


### 317. [WorldCast: Distributed Multiplayer World Models](https://arxiv.org/abs/2610.12412)

**<font color=#1a73e8>作者：</font>** Ziyang Ye, Junchao Huang, Evelyn Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multiplayer world models must generate independently controlled views with consistent representations of both players and their shared environment. Most existing approaches coordinate multiple players through joint multi-view generation, whose cost grows with each additional player. We present WorldCast, a distributed multiplayer world model in which each player runs a local client comprising a video generator and a state model. Using recorded player positions and map geometry during training, the state model estimates the player's position from generated video and control inputs. Clients exchange player states and project them into camera-aligned player state fields that guide where and how other players are rendered. Shared scene state enables clients to reuse one another's generated observations to maintain consistent scene appearance across views. Experiments on Counter-Strike 2 demonstrate WorldCast's consistency, real-time performance, and distributed scalability. The camera-aligned player state field improves player rendering rates by over an order of magnitude over joint-generation methods, while shared scene state improves visual consistency over whole rounds. Each client runs in real time and exchanges only player and scene states, enabling scalable multiplayer generation without a centralized computational bottleneck. Image quality remains stable over hour-long rollouts.

---


### 318. [MAMHOI: Factorizing Scene-Aware Human-Object Interaction through Affordances](https://arxiv.org/abs/2610.12416)

**<font color=#1a73e8>作者：</font>** Mingyuan Lei, Yoonchang Sung, Tat-Jen Cham  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating realistic human-object interactions (HOI) in complex 3D scenes requires two complementary capabilities: reasoning about interaction feasibility in the environment and synthesizing realistic human-object motion. However, supervision for these capabilities is rarely available jointly at scale. Human-scene datasets provide rich information about environment-aware motion, while human-object datasets capture detailed interaction dynamics, yet paired human-object-scene data remain scarce. We present MAMHOI, an affordance-mediated factorization for scene-aware human-object interaction generation. MAMHOI factorizes scene-aware HOI generation through an explicit motion-affordance interface between scene understanding and motion synthesis: a scene-conditioned model first predicts where and how an interaction can be feasibly executed, and an affordance-conditioned HOI model then generates the corresponding human-object motion. This factorization allows scene understanding and interaction dynamics to be learned from complementary sources of supervision without requiring paired human-object-scene data. Experiments in complex indoor environments show that MAMHOI reduces object--scene penetration while better preserving human--object interaction quality, yielding more realistic and physically feasible scene-aware interactions. Project page: this https URL

---


### 319. [A Unified Bellman Operator for Safety-Critical Reinforcement Learning](https://arxiv.org/abs/2610.12420)

**<font color=#1a73e8>作者：</font>** Nishanth Arun Rao, Royina Karegoudra Jayanth, Benjamin Eysenbach 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning in safety-critical domains requires maximizing task performance while strictly adhering to safety constraints. Existing safe reinforcement learning paradigms typically force a trade-off: they either require a priori knowledge to provide strict safety guarantees (e.g., safety filters), or they enable joint learning but only satisfy safety constraints on average. In this work, we propose a novel Bellman operator that unifies performance and safety objectives into a joint value function. We show that temporal difference learning with the joint Bellman operator converges under a two-timescale stochastic approximation framework. On the fast timescale, the safety value of the learning joint policy is estimated, while the joint value is estimated on the slow timescale. Convergence is ensured by formulating the limiting dynamics as an occupation-averaged differential inclusion, and showing that it asymptotically converges to a set of limiting optimal safety-constrained task value functions. Theoretically, once converged, the resulting optimal policy maximizes task return while maintaining safety at all times. Empirical evaluations on continuous control tasks with neural approximations demonstrate stable convergence with near-zero safety violations at test time.

---


### 320. [Beyond Spatio-Temporal Priors: A Generalizable Approach for Dense Correspondence Matching](https://arxiv.org/abs/2610.12421)

**<font color=#1a73e8>作者：</font>** Luping Liu, Bingyi Kang, Yifan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dense correspondence matching has historically been bounded by simplifying spatio-temporal priors, such as smooth motion and rigid geometry. While effective for classical tasks, these assumptions break down in image editing and reference-guided generation (IEG), where transformations can preserve visual identity while breaking physical continuity. To establish identity-preserving correspondence across such transformations, we introduce FreeMatching, a generalizable framework combining generative and semantic foundation representations with heterogeneous supervision from classical datasets, tracked videos, and synthetic scenes. Teacher-guided iterative refinement further improves correspondence in IEG without dense correspondence annotations. Experimentally, a single FreeMatching model substantially improves correspondence quality on challenging IEG image pairs while retaining competitive performance on classical benchmarks. Furthermore, we demonstrate its utility as a quantitative metric for evaluating identity preservation, with scores that correlate with human judgment. The code is available at this https URL.

---


### 321. [Pumpire: Unified Benchmark for Metric Distance Estimation](https://arxiv.org/abs/2610.12423)

**<font color=#1a73e8>作者：</font>** Siyu Chen, Zehan Wang, Jiayang Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Pumpire, a unified benchmark for evaluating metric point-pair distance estimation capability of both image- and video-level 3D foundation models, with or without depth priors. In contrast to previous approaches that normally evaluate depth and camera intrinsics separately or evaluate point-clouds with geometric similarity metrics, which cannot directly reflect models' point-to-point distance estimation capability, Pumpire directly assesses point-to-point distances from the reconstructed geometry. To this end, we collect a large-scale and diverse dataset (pumpire-6k) comprising 100 real-world scenes, each annotated with physically measured point-pair distances and containing 64 frames, for a total of 6,400 frames. Building on this dataset, we establish a holistic evaluation protocol that covers both image- and video-level 3D foundation models and enables direct assessment of point-pair distance errors and cross-setting comparison. We conduct extensive experiments across 29 baseline configurations of representative 3D foundation models and provide a comprehensive analysis of the results. By offering this benchmark, we target the more fundamental ability to perceive and estimate physical scale in the reconstructed 3D space, which prior evaluation protocols have largely overlooked. The project page can be found at this https URL

---


### 322. [Ecology of AI Agents: Collaboration Creates a Population Threshold for Takeoff](https://arxiv.org/abs/2610.12436)

**<font color=#1a73e8>作者：</font>** Erin Crawley, Hidenori Tanaka  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents can now conduct real-world cyberattacks, scale up capabilities with the number of agents, and collectively pursue misaligned goals to obtain rewards. Together, these factors raise the risk of a population explosion of misaligned agents: agents could compromise computers and secretly deploy additional agents, creating a self-reinforcing cycle where larger populations develop greater collective cyber capability and expand further. This raises a fundamental question: What determines whether a population of misaligned agents remains contained or takes off into this self-reinforcing cycle? This population-level problem is ecological safety: unlike individual-agent or multi-agent safety with a fixed population, it concerns the dynamics of the population itself. Here, we develop an ecological theory of AI-agent populations based on a population growth equation in which fitness (growth rate) depends on cybersecurity capability. We show that, without collaboration, the population takes off only when individual-agent capability exceeds a critical threshold. With collaboration, however, collective cybersecurity capability increases with population size. This creates a critical population threshold: below it, the population declines; above it, the population takes off, even though individual-agent capability has not changed. In ecology, this phenomenon is known as the strong Allee effect. Because red teaming a small group of agents cannot guarantee ecological safety in larger populations, our theory calls for ecological red teaming and population pacing: gradually deploying larger agent populations in controlled environments, while measuring how cyber capability scales with population size, and estimating the critical population size for takeoff. Capability gains may lower this threshold, requiring re-estimation for each new model generation.

---


### 323. [LEGO: A Lifting-Free Approach for Exocentric-to-Egocentric Video Generation](https://arxiv.org/abs/2610.12442)

**<font color=#1a73e8>作者：</font>** Suhwan Cho, Yonwoo Choi, Soongjin Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating an egocentric video from a single exocentric recording is a challenging case of novel view synthesis, as the two cameras share little overlap and much of the target view is unobserved. Current state-of-the-art methods reconstruct the scene explicitly by estimating depth, lifting the video into a point cloud, and re-rendering it from the egocentric camera to condition a video diffusion model. This deterministic mapping assigns each pixel to a single reprojected location, which preserves texture but translates depth errors into misplaced content. We ask what a video diffusion model should receive as its condition and propose a lifting-free answer: a learned view synthesizer, an LVSM-style transformer fine-tuned to render the egocentric view directly without depth, point clouds, or reprojection, resolving cross-view correspondence internally. In contrast, its probabilistic mapping averages each region over candidate source locations according to a learned correspondence distribution, preserving structure while fine texture is averaged away. We argue that this trade-off suits a diffusion generator, whose denoising training excels at restoring detail, so an effective condition should prioritize structural alignment over sharpness. This distribution's concentration also yields a per-region confidence, used both to mask low-confidence regions and to guide the generator toward high-confidence areas during early layout-forming denoising steps. Our approach consistently outperforms the state-of-the-art explicit pipeline and generalizes to other datasets without retraining. The synthesizer thus supplies view structure, and the diffusion model its detail.

---


### 324. [Bi-FORK: Generative Modeling of High-Dimensional Bifurcating Systems](https://arxiv.org/abs/2610.12449)

**<font color=#1a73e8>作者：</font>** Anna Zimmel, Fleur Hendriks, Markus Holzleitner 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bifurcations are ubiquitous in physical systems, from structural buckling to fluid and climate dynamics, yet they remain largely unexplored in deep learning. At a symmetry-breaking bifurcation, a single input admits multiple equally valid solutions, violating the one-to-one assumption underlying most learned physical surrogates. We introduce Bi-FORK, a generative framework for learning these one-to-many solution maps in high-dimensional systems. Bi-FORK generates complete trajectories through latent flow matching, preserving space and time coherence, and uses repulsion-guided sampling to recover distinct solution branches in a single amortized pass. We evaluate Bi-FORK on buckling beams, mechanical metamaterials, and Allen-Cahn phase separation, spanning continuous, discrete, and field-valued bifurcations with discretizations up to 260,000 points. Bi-FORK recovers the multimodal solution structure while scaling several orders of magnitude beyond prior approaches, opening generative modeling to high-dimensional bifurcating physical systems.

---


### 325. [Mental-Models for Multi-Agent Systems](https://arxiv.org/abs/2610.12453)

**<font color=#1a73e8>作者：</font>** Hanan Gani, Lulu Shao, Manmohan Chandraker  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large foundation models have accelerated progress toward general-purpose agents that interact with humans and other agents through language and multimodal signals. However, robust multi-agent decision-making requires reasoning about what other agents know, intend, and are likely to do under partial observability. Current agentic systems often operate through prompt design, memory, or end-to-end behavioral shaping, but typically do not learn an explicit partner-state representation that can be reused as a decision variable across tasks. We introduce \emph{mental-model-enabled agents}, a framework that equips an agent with a latent mental model of its counterpart, allowing it to infer hidden beliefs, intentions, and likely reactions from the observed history and use these inferences to guide action selection. Our method learns an amortized recursive Theory-of-Mind representation, with first- and second-order mental-state structure, jointly with a belief-conditioned reward model that evaluates candidate actions relative to the inferred partner state. A policy is then learned under this belief-aware signal, yielding an agent that can act independently at inference time while retaining the benefits of explicit partner modeling. We evaluate the same framework on both language-only and multimodal benchmarks. Across these settings, explicit mental-state modeling consistently improves interaction quality and Theory-of-Mind performance over base agentic systems, showing that structured partner modeling is a useful inductive bias for general multi-agent systems. Our code is publicly available at this https URL

---


### 326. [Hybrid Cinematography: Previsualizing and Managing Hallucination Risk in Generative Video Reshooting](https://arxiv.org/abs/2610.12455)

**<font color=#1a73e8>作者：</font>** Nhan, Tran, Neal Wadhwa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> On a film set, the camera move is committed during a take. Generative video reshooting lets filmmakers change it afterward, but may require hallucinating unrecorded content, a gap sometimes discovered only after leaving the set. We present Hybrid Cinematography, a workflow that bridges physical capture and generative reshooting to manage hallucination risk while filmmakers can still act on it. Using an editable 3D shot plan and a proxy of the take, our previsualization evaluates hallucination risk in real time. Seeing where the take lacks support, filmmakers can iteratively adjust the plan, explore moves that balance capture and generation, shoot guided pickups, or knowingly accept hallucination. We demonstrate the workflow through a mobile augmented reality application for on-set planning, capture, and review, and an offline pipeline for existing video. A study with experienced filmmakers reveals how previsualizing risk informs camera decisions and exposes tensions between creative intent and generative hallucination.

---


### 327. [WorldGuide: Goal-Directed Video World Model for Procedural Task Execution](https://arxiv.org/abs/2610.12459)

**<font color=#1a73e8>作者：</font>** Ankan Deria, Komal Kumar, Hisham Cholakkal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generators and video-based world models can synthesize plausible visual trajectories, but long-horizon procedural tasks require generation to adapt to what has actually been produced. A model must determine the next action from its generated state, execute that action, and recognize when the task is complete. Open-loop generation cannot adapt to execution outcomes, while existing closed-loop systems often rely on pretrained executors or indirect verification. This leaves a gap between deciding an action and successfully realizing it. We formulate procedural video generation as \emph{closed-loop task execution in visual world space} and introduce \textbf{WorldGuide}. Given only an initial image and a task goal, WorldGuide predicts an atomic action, generates its corresponding video clip, and uses the generated result to select the next action or terminate. The Planner and Executor are trained on the same step-level procedural demonstrations: the Planner learns to predict the next atomic action or task completion from visual progress, while the Executor is directly trained to realize the predicted actions. Hierarchical visual memory maintains state across long-horizon execution with bounded history token cost. Due to the lack of step-level action-video supervision for joint planner-executor training, we introduce \textbf{WorldGuide Bench}: approximately 59K step-annotated videos across 245 tasks and 27 procedural categories. WorldGuide achieves a 33.33\% Task Success on \textbf{WorldGuide-Bench}, compared with 29.90\% for the strong recent video model MiniMax-H3, even though MiniMax-H3 receives reference action plans, and achieves 47.69\% on \textbf{VideoCraft-Bench} compared with 32.73\% for MiniMax-H3 under goal-only conditioning. These results demonstrate the importance of coupling planning with learned execution for goal-directed procedural video generation.

---


### 328. [What 30,000 Hours of Ego-centric Video Does Not Teach](https://arxiv.org/abs/2610.12464)

**<font color=#1a73e8>作者：</font>** Jiahua Dong, Anurag Bagchi, Yash Jangir 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models offer a promising alternative to physics-based simulators, yet remain far from practical deployment. We ask how far scaling ego-centric human video takes them, using a dataset of 30,000 hours spanning over 1,000 scene types and 14,000 contributors. Rather than relying on opaque downstream metrics, we directly evaluate agent and object-interaction fidelity on a challenging out-of-distribution benchmark. Increasing training data by 100x improves both, but unevenly: the agent is modeled well, while object fidelity remains far lower and improves slowly. We show that the agent gains need not come from data, and a careful visual conditioning design saturates fidelity with a fraction of it, which lets us measure object fidelity on its own and discover its saturation point. We then introduce a supervision scheme that shifts capacity from scene appearance toward object dynamics, improving object fidelity though a substantial gap remains. Finally, our conclusions transfer to downstream humanoid modeling. Overall, our results suggest that scaling ego-centric data brings agent modeling close to its limit while leaving its effects on the world far behind, and that closing this gap will depend on how models are trained, not only on how much data they see.

---


### 329. [On the estimation and validity of AI time horizons---a statistical look at the METR plot](https://arxiv.org/abs/2610.12466)

**<font color=#1a73e8>作者：</font>** Drew T. Nguyen, William Fithian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> METR's 50\% time horizon measures the human completion time of software tasks that an AI solves with 50\% probability, allowing AI capabilities to be expressed in interpretable units. On 228 tasks and 26 AIs, we recompute the time horizons using splines and item-response theory to relax the assumption that the AI difficulty of a task depends linearly on the log of human time. Our fitted spline can be interpreted as a function that \emph{converts} human time to AI difficulty; it is nearly flat in a region from 2--30 min but close to linear elsewhere. Hence, a time-horizon jump from 3 min to 30 min is much easier than one from 30 min to 5 hours despite the same multiplier of $10 \times$. Overall, we contribute time-horizon point estimates that perform better under a cross-validated suite of proper scoring rules, as well as diagnostic plots for assessing time horizons' construct validity. We suggest that time horizons be interpreted together with the diagnostic plots, especially as new time-horizon-based benchmarks are proposed or existing ones grow to include longer tasks.

---


> [!TIP]
> 当前位于：**301-329**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-329**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
