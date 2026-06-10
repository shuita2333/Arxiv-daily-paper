# 📦 其他研究 | 2026年06月11日

> 本类共 **269** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-269**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-269**

---

### 251. [VISTA: A Versatile Interactive User Simulation Toolkit for Agent Evaluation](https://arxiv.org/abs/2606.11079)

**<font color=#1a73e8>作者：</font>** Yunan Lu, Ryan Shea, Yusen Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluation remains a critical bottleneck for interactive agent development. Existing evaluation methods often rely on static benchmarks, which fail to capture the dynamic, multi-step nature of agentic behavior and struggle to expose meaningful failure modes. While user-simulation-based evaluation offers a promising alternative, existing simulation frameworks suffer from two major limitations. First, they provide limited mechanisms for evaluating the quality and comprehensiveness of simulated interactions, making it difficult to assess whether a simulator sufficiently explores an agent's capabilities and failure modes. Second, most frameworks are restricted to either UI-only actions or API-only actions, limiting their ability to model the full range of realistic user behaviors. To address these limitations, we propose VISTA, a Versatile Interactive user Simulation Toolkit for Agent evaluation. Our toolkit includes a suite of six metrics for measuring the realism, capability coverage, and interaction effectiveness of simulated interactions. In addition, we develop a hybrid user simulator that integrates both UI-based interactions and API-based interactions, enabling more realistic and comprehensive evaluation across diverse interactive environments. We evaluate VISTA in e-commerce shopping and education customer service settings and demonstrate that it produces more realistic and comprehensive evaluations than existing methods.

---


### 252. [Test-Time Gradient Guidance of Flow Policies in Reinforcement Learning](https://arxiv.org/abs/2606.11087)

**<font color=#1a73e8>作者：</font>** Zhiyuan Zhou, Andy Peng, Charles Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Expressive continuous control policies, such as diffusion and flow models, form the backbone of recent advances in scaling imitation learning for simulated and real robot control. While they are known to scale stably in the supervised imitation learning setting, incorporating them into reinforcement learning (RL) pipelines for policy improvement has proven more difficult. It often requires specialized training objectives or backpropagating through denoising processes, which cause well-known issues with stability and affect scalability. In this paper we study the question of whether simple policy improvement schemes at test time alone, leaving stable supervised policy training intact, can be a competitive alternative which sidesteps these issues. To this end, we propose QGF (Q-Guided Flow), an RL algorithm that performs policy optimization entirely at test time. QGF works by pre-training both a reference flow policy (via a standard behavioral cloning objective) and a value function critic and, at test time, using the value gradient to guide the reference policy to generate higher-value actions without any additional policy learning. Empirically, QGF outperforms prior test-time RL methods on single-task and goal-conditioned offline RL benchmarks with high-dimensional action spaces, and is competitive with state-of-the-art training-time algorithms while being much cheaper to run. Moreover, it exhibits favorable scaling with model size by avoiding the instability of actor-critic training, offering a practical and effective alternative RL algorithm with expressive policies.

---


### 253. [Do Transformers Actually Help Intrusion Detection? A Temporal Sequence Evaluation on CIC-IDS2017](https://arxiv.org/abs/2606.11098)

**<font color=#1a73e8>作者：</font>** Zach Moczkodan, Hany Ragab  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent deep learning approaches for network intrusion detection increasingly incorporate temporal architectures such as recurrent networks and Transformers, often reporting near-perfect performance on CIC-IDS2017. However, many existing studies neither supply their temporal modules with genuine sequence inputs nor evaluate under realistic, leakage-free conditions, making it unclear whether reported gains arise from true sequence-modeling capability. In this work, we reformulate CIC-IDS2017 as a temporal intrusion-detection task by constructing ordered flow sequences from network conversations and benchmarking nine classical and deep learning architectures under a random split, two leakage-free splits, and a padding-scheme ablation. The central finding is that padding convention, not architecture, determines the Transformer's performance: on genuinely sequential (non-padded) windows the Transformer achieves the highest macro-F1 of any model in the experiment (0.89); under zero-pad+mask evaluation it drops markedly (-0.24 macro-F1), while LSTM, GRU, and 1D-CNN remain stable. Under leakage-free group evaluation the Random Forest is the most robust model (+0.009), while the Transformer's false-alarm rate grows from 0.04% to 2.7%, a 67-fold increase invisible under conventional protocols. These findings demonstrate that evaluation methodology -- specifically padding convention and split protocol -- has a larger effect on reported performance than architectural choice, and that widely used random splits with repeat-last padding can overestimate model robustness by up to 0.24 macro-F1. We advocate leakage-free splits, explicit padding disclosure, and sequence-aware benchmarking as standard practice in future IDS research. Code and implementation details are available at this https URL.

---


### 254. [Limitations of Learning Tanh Neural Networks with Finite Precision](https://arxiv.org/abs/2606.11104)

**<font color=#1a73e8>作者：</font>** Philipp Grohs, Matěj Trödler  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate limitations of learning $\tanh$ neural networks from point evaluations under finite-precision computations and $L^p$ accuracy guarantees, building on Berner, Grohs, and Voigtländer (2023). Our approach is based on a novel construction of sharply localized bump functions via iterated $\tanh$ activations. Using this mechanism, we show that, in a finite-precision setting, no adaptive randomized algorithm based on $m$ samples can achieve a convergence rate higher than the Monte Carlo rate $O(m^{-1/p})$ in the $L^p$ norm, unless the sampling budget grows exponentially with the size of the network parameters and architecture. The results reveal fundamental limitations imposed by finite precision on the learnability of classes containing localized bump functions, extending previous results for ReLU networks to the $\tanh$ setting.

---


### 255. [A Longitudinal Study of Recently Observed Malicious Domains: Characteristics, Infrastructure, and Abuse Patterns](https://arxiv.org/abs/2606.11111)

**<font color=#1a73e8>作者：</font>** Fathima Mashood, Mohamed Nabeel  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present a longitudinal study of approximately 1.52 million malicious domains observed on VirusTotal (VT) between January and May 2026. Domains were selected on the basis of detection by at least five independent VT scanning engines and a first-seen date within the study window. We group the dataset into compromised domains and attacker created domains, which account for approximately 89.3% of the dataset. Combining WHOIS registration records and passive DNS (PDNS) data with the VT dataset, we characterise attacker behaviour across eight dimensions: temporal distribution, this http URL classification, domain age at first detection, registrar and TLD preferences, DNS query volume as a damage proxy, hosting infrastructure concentration (IP and ASN level), bulk registration patterns, and brand impersonation. Key findings include: the majority of attacker created domains are short lived registrations used within weeks of creation; a small number of registrars and TLDs account for most abuse; Cloudflare infrastructure is heavily exploited for domain fronting; bulk registration events involving thousands of domains from a single registrar on a single day are widespread; and several global brands, particularly WhatsApp and Google, are heavily impersonated. We share the annotated dataset in the GitHub repo this https URL
for further research.

---


### 256. [Data-Driven Dynamic Assortment in Online Platforms: Learning about Two Sides](https://arxiv.org/abs/2606.11118)

**<font color=#1a73e8>作者：</font>** Rahul Roy, Nur Sunar, Jayashankar M. Swaminathan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study a dynamic assortment problem on a two-sided service platform with incomplete information and heterogeneous customers in a discrete-time setting. In each period, a customer arrives seeking service, and the platform chooses an assortment of sellers to display. The customer then proposes a transaction to at most one seller in the assortment according to a multinomial logit choice model. After a fixed number of periods, sellers review the proposals they have received and each chooses at most one customer according to another multinomial logit choice model, after which the cycle repeats. A key challenge is that the platform does not know the choice-model parameters of either customers or sellers in advance. To our knowledge, this is the first study of a dynamic assortment problem in which both sides' choice parameters are unknown. We develop a data-driven algorithm that learns these parameters while optimizing the platform's objective over time. We evaluate performance using regret, which measures revenue loss relative to a clairvoyant benchmark that knows all parameters and customer arrivals in advance. We show that the algorithm's worst-case regret grows polylogarithmically over time, and we derive a matching lower bound, establishing its rate optimality.

---


### 257. [Monte Carlo Pass Search: Using Trajectory Generation for 3D Counterfactual Pass Evaluation in Football](https://arxiv.org/abs/2606.11120)

**<font color=#1a73e8>作者：</font>** Andrew Kang, Priya Narasimhan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We recast pass evaluation in football (soccer) as a Monte Carlo Tree Search (MCTS)-like evaluation problem whose components mostly exist in the literature under different names: a value model (possession value), a world model (multi-agent trajectories with ball interactions), and a policy over counterfactual actions (sampling pass variants with noise). Building on the first public high-fidelity tracking dataset with 3D ball trajectories from the Bundesliga, we introduce Monte Carlo Pass Search (MCPS), which infers kick parameters for each observed pass, samples execution variants and option variants, rolls each candidate forward with a ball-conditioned world model until the next ball interaction, and scores outcomes with a learned value model to obtain a distribution over gained value. This distribution enables distribution-aware attribution with two complementary execution-surplus scores used for analysis and ranking: mean-based and percentile-based scores. To make the world model sample-efficient under limited public data, we adapt a discrete-token, autoregressive trajectory generator from autonomous driving (SMART) and show it yields strong best-of-20 forecasting accuracy compared to baselines, while supporting fully hypothetical rollouts for downstream evaluation. We have released model checkpoints and code.

---


### 258. [Robust Regression of General ReLUs with Queries](https://arxiv.org/abs/2606.11130)

**<font color=#1a73e8>作者：</font>** Ilias Diakonikolas, Daniel M. Kane, Mingchen Ma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the task of agnostically learning general (as opposed to homogeneous) ReLUs under the Gaussian distribution with respect to the squared loss. In the passive learning setting, recent work gave a computationally efficient algorithm that uses $poly(d,1/\epsilon)$ labeled examples and outputs a hypothesis with error $O(opt)+\epsilon$, where $opt$ is the squared loss of the best fit ReLU. Here we focus on the interactive setting, where the learner has some form of query access to the labels of unlabeled examples. Our main result is the first computationally efficient learner that uses $d polylog(1/\epsilon)+\tilde{O}(\min\{1/p, 1/\epsilon\})$ black-box label queries, where $p$ is the bias of the target function, and achieves error $O(opt)+\epsilon$. We complement our algorithmic result by showing that its query complexity bound is qualitatively near-optimal, even ignoring computational constraints. Finally, we establish that query access is essentially necessary to improve on the label complexity of passive learning. Specifically, for pool-based active learning, any active learner requires $\tilde{\Omega}(d/\epsilon)$ labels, unless it draws a super-polynomial number of unlabeled examples.

---


### 259. [UniPET: a universal network for high-quality PET image denoising across varied dose reduction factors](https://arxiv.org/abs/2606.11131)

**<font color=#1a73e8>作者：</font>** Zhiwen Yang, Yang Zhou, Haowei Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most existing deep learning-based PET image denoising methods assume a fixed and known dose reduction factor (DRF) for low-dose PET images. However, these methods encounter significant performance degradation when the DRF varies beyond the assumed one in practical applications. To address the challenge posed by varied DRFs, several preliminary studies focus on the task of universal PET image denoising, aiming to train a universal model over low-dose data across DRFs. Nonetheless, these vanilla universal models often struggle with misaligned styles present in different DRF data, leading to the \textit{style elimination issue} with a significant over-smoothing effect. To deal with this issue, we innovatively introduce domain generalization to PET image denoising and propose a universal PET image denoising network (UniPET) to achieve high-quality PET image denoising across diverse DRFs. UniPET comprises two primary innovations: a style alignment network (SAN) and a region-aware learning strategy (RALS). Specifically, SAN utilizes style alignment techniques derived from domain generalization to align and recover styles across different DRFs, ensuring the model's generalizability across various DRFs while effectively preserving styles. Furthermore, to enhance style recovery, RALS distinguishes between flat and stylized regions, exclusively conducting adversarial learning on the latter, thereby more effectively guiding the model's focus towards learning stylized regions. It is demonstrated that our proposed UniPET can adaptively recover different DRF styles and achieve high-quality PET image denoising across DRFs. Comprehensive experiments show that UniPET exhibits comparable performance to individual DRF-specific models at specific DRFs and realizes state-of-the-art performance in universal PET image denoising quantitatively, perceptually, and clinically.

---


### 260. [First-Order Trajectory Matching: Fast Ensemble Predictions of Chaotic, Turbulent, Stochastic Systems](https://arxiv.org/abs/2606.11138)

**<font color=#1a73e8>作者：</font>** Shreya Jha, Timo Schorlepp, Nicholas Geissler 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce First-Order Trajectory Matching (FTM), a surrogate-modeling method that learns the first-order local transport of probability mass from trajectories of stochastic systems. By matching the symmetric first-order motion of trajectories, FTM learns the probability current velocity, whose flow preserves time marginals to match ensemble averages, while also capturing current-like trajectory quantities such as fluxes, circulations, and barrier-crossing currents. FTM learns the current velocity directly from trajectories, avoiding drift, diffusion, and score estimation. Our stability analysis separates discretization error from sampling variance and shows that the one-step simulation-free FTM loss is stable when temporal resolution and sample size are properly balanced. Across stochastic dynamical systems and PDE examples, we empirically demonstrate that FTM provides trajectory-aware ensemble predictions at low, deterministic-rollout cost.

---


### 261. [OncoTraj: a public benchmark for longitudinal resistance prediction in EGFR-mutant non-small-cell lung cancer on osimertinib](https://arxiv.org/abs/2606.11144)

**<font color=#1a73e8>作者：</font>** Abhijoy Sarkar, Aarchi Singh Thakur  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Resistance to first-line osimertinib in EGFR-mutant non-small-cell lung cancer (NSCLC) is the canonical example of predictable clonal evolution under therapeutic pressure, yet no public benchmark exists for training or evaluating computational models on the corresponding longitudinal patient trajectories. We introduce OncoTraj, a public benchmark of 813 EGFR-mutant NSCLC patients receiving first-line osimertinib, harmonized from three real-world clinical-genomic sources: MSK-CHORD (672 patients), AACR Project GENIE BPC NSCLC (34 patients), and the FLAURA molecular-resistance supplement (107 patients). OncoTraj defines three locked tasks: (A) binary classification of progression by a fixed 12-month landmark, (B) regression of time-to-first-progression in days, and (C) six-class classification of the dominant resistance mechanism. We release the harmonized dataset, patient-level train/validation/test splits with an audited no-leakage guarantee, an open-source evaluation harness, and six reference baselines spanning a majority-class predictor, logistic regression, random forest, XGBoost, an LSTM, and a multi-task transformer. With v1's single-timepoint snapshot features, no task clears chance on clean within-source evaluation: the uniformity of this ceiling across every model class localizes the limit to the input modality (single-snapshot tissue NGS rather than serial ctDNA), not the algorithm. The benchmark does recover a reproducible literature-consistent association: TP53 co-mutation raises the 12-month progression rate from 29% to 59% cohort-wide. OncoTraj establishes a reproducible, leakage-audited baseline and converts the modality limit into concrete design requirements for a serial-ctDNA-enriched v2.

---


### 262. [MOFA-VTON: More Fashion Possibilities with Fine-Grained Adaptations in Virtual Try-On](https://arxiv.org/abs/2606.11148)

**<font color=#1a73e8>作者：</font>** Xiaoyu Han, Chenyang Wang, Jing Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Virtual try-on aims to fit an in-shop clothing image onto a specific human body. An optimal virtual try-on method should provide diverse and flexible dressing options, accurately reflecting the varied wearing styles encountered in real-life scenarios, tailored to individual preferences and fashion aspirations. However, current methods predominantly perform a direct replacement of the original clothing with the target clothing, following the same dressing pattern. This limited control over clothing adaptation may result in fixed and monotonous try-on outputs. To delve into More Fashion Possibilities with Fine-Grained Adaptations in Virtual Try-On, we propose a novel virtual try-on method, termed MOFA-VTON, which allows adjustment for clothing adaptations in try-on results through simple sketches by users. Specifically, we first design a mask construction strategy that transforms user-drawn curve sketches into a dual-region mask, replacing the traditional clothing-agnostic mask and providing fine-grained layout guidance for the subsequent generation process. Further, we propose layout adjustment blocks that utilize the cross-attention mechanism to independently learn layout correspondences for upper and lower regions of the human body, refining the spatial arrangement of the two regions. With these implementations, our method enables flexible and fine-grained adaptations of target clothing, overcoming the constraints of a fixed layout. Extensive experiments on VITON-HD and DressCode datasets demonstrate that our proposed MOFA-VTON outperforms previous state-of-the-art methods and provides more fashion possibilities for virtual try-on.

---


### 263. [Efficiently Learning Drifting Halfspaces with Massart Noise](https://arxiv.org/abs/2606.11149)

**<font color=#1a73e8>作者：</font>** Mingchen Ma, Guyang Cao, Jelena Diakonikolas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the problem of learning a drifting concept in the presence of Massart noise. In this framework, an online learner has access to a history of independent samples whose labels are noisy versions of a target concept that may change from round to round. The goal is to output, in each round, a hypothesis with small prediction error. We study the complexity of this learning problem for the fundamental class of margin-separable linear classifiers (halfspaces). On the positive side, we give a computationally efficient learner achieving error $\eta + \tilde O(\Delta^{1/3}/\gamma)$, where $\eta$ upper bounds the Massart noise rate, $\Delta$ is the drift rate, and $\gamma$ is the margin. Interestingly, in the realizable setting, an adaptation of our techniques yields an efficient learner with an improved error rate over prior work. On the lower-bound side, we provide formal evidence of an information-computation tradeoff, strongly suggesting that our algorithm's performance is essentially optimal. Specifically, while the information-theoretically optimal error scales with $\Delta^{1/2}$, we prove that $\Delta^{1/3}$-scaling is unavoidable for low-degree polynomial tests, even in the special case of random classification noise.

---


### 264. [Mean Flow Distillation: Robust and Stable Distillation for Flow Matching Models](https://arxiv.org/abs/2606.11155)

**<font color=#1a73e8>作者：</font>** An Zhao, Shengyuan Zhang, Zhongjian Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flow Matching models have demonstrated strong performance across a wide range of generative tasks. However, their reliance on ODE-based iterative sampling incurs substantial computational overhead in inference, which limits their applicability in real-time scenes. While distillation is a promising solution, existing approaches largely borrow from diffusion-based score matching, often failing to exploit the intrinsic geometric structure of flows and suffering from training instability, high variance, and degraded generation quality. In this paper, we propose Mean Flow Distillation (MFD), a novel distillation framework tailored for flow matching models. We theoretically demonstrate that MFD acts as a temporal low-pass filter, effectively suppressing the high-frequency optimization noise inherent in variational score distillation (VSD) while ensuring global trajectory consistency. We further prove the Mean Flow Matching Theorem, establishing that matching expected average velocities is sufficient for strict distribution alignment. Empirically, on challenging tasks of high-dimensional manifolds including 4D occupancy forecasting and text-to-image generation, MFD achieves state-of-the-art performance, enabling high-fidelity single-step generation.

---


### 265. [COGENT: Continuous Graph Emulators with Neural Ordinary Differential Equations for Long-Term Physical Forecasting](https://arxiv.org/abs/2606.11162)

**<font color=#1a73e8>作者：</font>** Zesheng Liu, Maryam Rahnemoonfar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we present COGENT, a continuous graph emulator with Neural Ordinary Differential Equations for long-term physical forecasting on irregular geospatial meshes. COGENT encodes a finite history of system states and associated forcing fields and external forcings with a graph-based history encoder, producing node-wise context vectors that capture both local spatial interactions and temporal evolution. These context vectors initialize and condition a latent Neural Ordinary Differential Equation whose dynamics are driven by interpolated future forcings and explicit relative rollout time. By modeling the forecast trajectory as a continuous latent dynamical system, COGENT can generate predictions at arbitrary future times rather than being restricted to a fixed temporal discretization. A residual decoder maps the resulting latent trajectories back to future physical states, enabling direct multi-step forecasting without repeatedly feeding predicted states back into the model. This formulation combines graph-based spatial representation, history-conditioned latent dynamics, and continuous-time rollout in a unified framework for mesh-based physical simulation emulation. In order to stabilize training with long-horizon supervision, we also propose effective rollout-horizon sampling and a progressive rollout-horizon scheduling strategy. We evaluate COGENT on transient ice-sheet simulations generated by the Ice-sheet and Sea-level System Model, demonstrating improved long-range stability over autoregressive graph baselines. These results suggest that continuous graph Neural ODEs provide a promising methodology for scalable physical forecasting on irregular geospatial meshes, particularly in applications that require stable long-horizon predictions and the ability to query system states at arbitrary times.

---


### 266. [Algorithmic and Minimax Complexities in Kernel Bandits](https://arxiv.org/abs/2606.11171)

**<font color=#1a73e8>作者：</font>** Yunbei Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gaussian-process upper confidence bound (GP-UCB) and decision-estimation-coefficient (DEC) methods may appear, at first sight, to belong to different theories. This paper places the two viewpoints in a common algorithmic-information language for frequentist RKHS bandits. GP-UCB fixes an algorithmic, rather than true, Gaussian-process prior and exploits realized-trajectory complexity together with computational tractability, whereas MAMS optimizes a robust class-wide MAIR/DEC envelope. Through the unified MAIR framework and heterogeneous positive-semidefinite algorithmic priors, we generalize both the GP-UCB analysis and the MAMS algorithm, propose a safeguarded master that combines their advantages, and provide a kernel-bandit construction showing that algorithmic complexity can be more informative than class-wide minimax or DEC certificates in overparameterized models. The resulting message is that algorithmic information and class-wide minimax coefficients answer different questions and can lead to different gaps; kernel bandits provide a clean setting in which this distinction becomes mathematically visible.

---


### 267. [Anchors that Don't Lift: Understanding Supply Chain Driven Kernel Lock-In and Governance-Mediated Mitigation Strategies in SOHO Devices](https://arxiv.org/abs/2606.11175)

**<font color=#1a73e8>作者：</font>** Ritwik Badola, Rajdeep Ghosh, Ashita Gupta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Small Office/Home Office (SOHO) devices are widely popular, yet often attacked due to security vulnerabilities in their firmware, affecting thousands of devices. These security vulnerabilities often stem from outdated Linux kernel versions included in SOHO device firmware. Naturally, prior work audited the extent and impact of this issue by simple Linux version extraction and version number based vulnerability mapping. However, it is unclear how many of these anticipated vulnerabilities actually exist in the heavily customized SOHO kernels and if there are any barriers towards updating Linux kernels in SOHO firmwares.
To address this gap, we uncover actual kernel-related vulnerabilities found in 306 SOHO devices using a high-precision template-based CVE detection mechanism on GPL source releases of more than 900 firmwares from these devices. Next, as a first, we traced the supply chain of these vulnerable SOHO devices at scale and identify kernel lock-in as a significant security issue -- SOHO vendors are effectively locked to specific (often older) kernel versions due to the system-on-chip (SoC) SDKs they use. This kernel lock-in produces a vulnerability debt that is inherited along the supply chain from SoC vendor to firmware creators (ODM/OEM) to router/IP-camera vendor and ultimately borne by end users. All five SoC vendors in our dataset had used SDKs with Linux kernels that had reached EoL more than a year before their usage in a SOHO device. Finally, we explore the mitigation-potential of individual, regulatory and community governance by analyzing social media posts, regulations and community efforts. Our results show that regulation compliance is insufficient and only SoC vendors who engage with communities for kernel upgradation offered a viable path towards mitigation. The data and code for this work is available at this https URL

---


### 268. [Lip Forcing: Few-Step Autoregressive Diffusion for Real-time Lip Synchronization](https://arxiv.org/abs/2606.11180)

**<font color=#1a73e8>作者：</font>** Paul Hyunbin Cho, Jinhyuk Jang, SeokYoung Lee 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based lip synchronization models achieve strong visual quality and audio-visual alignment, but full-sequence bidirectional attention and many denoising steps make them impractical for real-time inference. We present Lip Forcing, to our knowledge the first autoregressive diffusion method for video-to-video (V2V) lip synchronization, which distills a 14B audio-conditioned bidirectional video diffusion teacher into causal students. At inference, the students generate each chunk in only two denoising steps without inference-time CFG, enabling real-time lip synchronization. A lip-sync-specific teacher-trajectory analysis reveals a CFG fidelity-sync tradeoff: no-CFG predictions favor reference fidelity, whereas CFG-guided predictions favor synchronization within a mid-trajectory band. Lip Forcing translates this finding into three analysis-derived components: Sync-Window DMD, a two-step inference schedule, and a SyncNet-based reward. We validate Lip Forcing at two student scales, both distilled from the 14B teacher. The 1.3B student crosses into real-time streaming at 31 FPS, $17.6\times$ faster than its same-scale bidirectional model. The 14B student, the largest diffusion model reported for V2V lip synchronization, runs $39.8\times$ faster than its teacher at comparable reference fidelity. Time-to-first-frame is sub-millisecond at both scales, far below every diffusion baseline.

---


### 269. [AnyMod-LLVE: Low-Light Video Enhancement with Modality-Agnostic Inference](https://arxiv.org/abs/2606.11186)

**<font color=#1a73e8>作者：</font>** Hangfeng Liang, Yutao Hu, Yanhan Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-light video enhancement (LLVE) remains a challenging task due to severe information degradation under low-illumination conditions. Recent multimodal approaches have significantly improved enhancement performance by incorporating auxiliary modalities, such as event streams and infrared images. However, these methods typically assume the availability of these modalities at inference, which is often not feasible in real-world scenarios. To solve this problem, in this work, we propose AMNet, a unified multimodal framework for LLVE, to support flexible modality-agnostic inference, where auxiliary modalities may be unavailable. To address the issue of modality absence, we introduce a Spatial-Spectral Dual-Gated Translator that learns the correspondence between auxiliary modalities and RGB inputs, producing implicit auxiliary representations to support the robust enhancement. Additionally, to fully facilitate the learning of cross-modal correspondence, we conduct large-scale multimodal pretraining based on the RGB-only dataset with synthetic auxiliary modalities. Extensive experiments demonstrate that AMNet could handle arbitrary inference-time modality combinations and exhibits superior performance for LLVE under modality absence conditions. Code and models are available on the project page.

---


> [!TIP]
> 当前位于：**251-269**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-269**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
