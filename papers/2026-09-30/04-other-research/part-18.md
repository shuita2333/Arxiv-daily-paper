# 📦 其他研究 | 2026年09月30日

> 本类共 **908** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**851-900**（第 18/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | **851-900** | [901-908](./part-19.md)

---

### 851. [Physics-Guided Conditional Diffusion Model for Rare Event Synthesis and Diagnosis for the Water-Gas Shift Reaction](https://arxiv.org/abs/2609.35499)

**<font color=#1a73e8>作者：</font>** Md Abrar Rafid Siddique, Bibek Aryal, Qiugang Lu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As the world moves towards sustainable energy sources, hydrogen (H2) can be treated as an eco-friendly alternative to fossil fuels due to its high energy density and zero carbon emissions. The water-gas shift (WGS) reaction is a widely used industrial process for hydrogen production by converting carbon monoxide and steam into hydrogen and carbon dioxide. However, occurrences like severe fouling, catalyst deterioration, and thermal runaway can hamper the reaction kinetics/process safety and decrease the yield of H2. These incidents are rare, and gathering process data under such abnormal conditions is challenging. In this work, we propose a physics-guided conditional diffusion model to generate realistic rare-event trajectories for the WGS reaction. The proposed model integrates a conditional denoising diffusion probabilistic model (CDDPM) with governing laws of the reaction to generate physically consistent process trajectories. The conditioning features allow the model to produce high-quality synthetic profiles for rare-event domains that are typically beyond the training regimes. The generated rare-event trajectories then augment the raw dataset for a balanced distribution between normal and abnormal conditions. We further propose a hazard score to assess the risk severity of the operating condition based on the operating trajectory. Deep learning models are trained with the augmented dataset to diagnose the health status of the reaction. Simulation results show that the proposed physics-guided diffusion model outperforms data-driven models in terms of the quality of synthetic data and diagnosis performance for rare events.

---


### 852. [Structured Latent Modeling for Supervised Multimodal Information Decomposition](https://arxiv.org/abs/2609.35502)

**<font color=#1a73e8>作者：</font>** Wanting Huang, Sanvesh Srivastava, Weiran Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal prediction relies on diverse forms of evidence: information repeated across modalities, cues specific to a single source, and complex cross-modal dependencies that emerge only when inputs are considered together. While recent methods promote richer interactions, they lack a principled way to isolate these target-relative contributions within learned continuous representations. We introduce a framework that applies contrastive or masked objectives at intermediate layers, coupled with source-wise invertible normalizing flows and a supervised, low-rank latent variable model. This architecture explicitly factorizes the joint distribution into shared task-relevant variation, modality-specific predictive variation, and task-irrelevant dependence. Drawing connections to prior multimodal learning assumptions, our approach evaluates how modalities independently and jointly contribute to the target. Ultimately, this framework unites intermediate representation learning with structured likelihood-based guidance, offering a practical latent-variable lens for characterizing continuous multimodal interactions. Empirically, we demonstrate the effectiveness of our approach across diverse multimodal benchmarks, showing robust improvements in predictive performance.

---


### 853. [Detecting False Data Injection and Unstable Operation in Smart Grid via System-Aware Graph Boundary Learning](https://arxiv.org/abs/2609.35506)

**<font color=#1a73e8>作者：</font>** Emad Efatinasab, Denis Donadel, Mirco Rampazzo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cyber-physical power systems increasingly rely on data-driven tools to detect instability and support reliable grid operation. However, reliable stability prediction is difficult when unstable operating configurations are rare, sensitive, or unavailable during model development, since collecting such data safely and at scale is often impractical. At the same time, False Data Injection (FDI) attacks can manipulate reported system parameters to trigger false instability alarms or conceal unsafe operation, and such threats in Decentral Smart Grid Control (DSGC) systems remain largely unexplored. These challenges are rarely addressed jointly, leaving a gap between stability prediction and attack detection that this work aims to close. In this paper, we introduce StarGNN, a graph learning framework that learns the stable operating region exclusively from clean stable configurations and uses a single abnormality score to flag reported configurations that should not be trusted as evidence of safe operation, covering both genuine instability and unseen FDI manipulations. Each configuration is represented as a producer-consumer star graph and processed by a role aware graph neural network, with physics constrained pseudo-negatives generated by perturbing reaction time and price response parameters standing in for the unavailable unstable and attack data. A single threshold, calibrated only on held-out stable data, is used without task or attack specific adjustment. Evaluated on nine unseen FDI scenarios, StarGNN detects between 0.780 and 0.973 of attacks on stable configurations and retains a post attack instability recall between 0.972 and 0.999 on unstable ones, with 0.899 recall against a stronger adaptive attacker, showing that stable-only boundary learning can support both stability prediction and attack detection without access to genuine unstable labels or attack samples during training.

---


### 854. [Improving Generative Model Self-Training with Geometrically Modified Outputs](https://arxiv.org/abs/2609.35512)

**<font color=#1a73e8>作者：</font>** Patrick Batsell, Thomas Walker, Richard Baraniuk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-training generative models - the continued improvement of a model using its own outputs - is becoming increasingly important as high-quality training data becomes scarce. However, naively finetuning on model-generated samples leads to degradation through model collapse and the model autophagy disorder. Negative-guidance self-training methods turn this degradation into a useful signal, using a model finetuned on its own outputs to guide the original model toward improved generation. Existing methods, however, take the negative signal in standard model outputs as given. We instead ask whether this signal can be explicitly strengthened. We introduce Geometrically Modified Outputs (GMOs), which reweight the singular values of the generator's input-output Jacobian to increase the influence of its leading singular directions. This geometric modification amplifies the mode-seeking behavior and distortions of standard outputs, providing a stronger and more targeted negative signal for self-training. Across a range of one-step generative models, GMOs consistently improve the performance of negative-guidance methods, including Neon and SIMS, compared with using standard model outputs.

---


### 855. [One Proposal for Every Margin: Zero-Shot Amortized Sequential Importance Sampling for Binary Matrices](https://arxiv.org/abs/2609.35514)

**<font color=#1a73e8>作者：</font>** Ruishuo Chen, Weijia Li, Xun Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In ecology, psychometrics, and the analysis of social and financial networks, binary matrices are often analyzed conditional on their observed row and column sums, which restricts the problem to a finite sample space of matrices with the same margins. Two fundamental problems are to count this space and to sample uniformly from it. Sequential importance sampling (SIS) addresses both with independent weighted samples and an unbiased count estimator, but its efficiency depends critically on the proposal distribution. Existing proposals are analytically designed, and their accuracy can vary substantially with the margins. We show that the ideal SIS proposal, under which every weight equals the count and the variance vanishes, is exactly the policy of a generative flow network (GFlowNet) with unit reward on every matrix that has the given margins. We therefore propose MarginFlow, a framework that turns the design of the proposal into a learning problem and amortizes it across margins by exploiting their self-similarity. Every partial matrix is itself an instance with reduced margins, so one set transformer that reads the remaining margins serves every margin. We train MarginFlow on a pool of 1904 margins and evaluate it zero-shot on 1190 held-out margins, synthetic and real, from $3\times3$ to $870\times6$. On 1187 of the 1190 margins it matches or beats the best of 31 analytically designed configurations, chosen post hoc for each margin, and its median effective sample fraction is 99.8%. On the 56 margins where that best loses more than one nat of effective sample size, MarginFlow wins every one and raises the median effective sample fraction from 10.3% to 94.1%.

---


### 856. [Deep Epistemic Value Functions for Optimistic Exploration](https://arxiv.org/abs/2609.35525)

**<font color=#1a73e8>作者：</font>** Leander Diaz-Bone, Marco Bagatella, Jonas Hübotter 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Principled exploration in reinforcement learning requires an agent to quantify its epistemic uncertainty and act to resolve it. Uncertainty over the value function provides a natural signal for exploration, yet existing deep approximations remain brittle and perform inconsistently. The central challenge is therefore to scale these ideas robustly. We conduct a systematic empirical study of how epistemic uncertainty is represented, propagated, and optimized in deep epistemic value functions, and uncover distinct failure modes along each of these axes. These findings motivate DEVOTE, a model-free reinforcement learning algorithm that controls how uncertainty generalizes beyond observed data, stabilizes its temporal propagation, and preserves adaptation to the resulting non-stationary exploration objective. Across reward-free exploration and challenging continuous-control tasks, DEVOTE reaches novel states more effectively and achieves higher task return than strong model-free and model-based exploration baselines. These results provide evidence that deep epistemic value functions are a promising path toward scalable, principled exploration.

---


### 857. [GeoGAE: Scalable Graph-Level Autoencoding via Hyperball Cloud Representations](https://arxiv.org/abs/2609.35527)

**<font color=#1a73e8>作者：</font>** Radosław Nowak, Anna Bielawska, Bogusz Stefańczyk 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Embedding structured objects into Euclidean spaces has enabled a wide range of successful machine learning applications. Such objects include words, documents, image patches, time series, and graph nodes. In contrast, embedding entire graphs remains a challenging problem. Existing methods either sustain the original order of the graph nodes or match the output nodes to the input ones, both of which create scalability issues. In this work, we propose a graph representation as a cloud of hyperballs, which allows us to define a specific, typically unique, node ordering. Based on this representation, we propose GeoGAE, an autoencoder, in which the Transformer encoder translates a hyperball cloud into a graph-level embedding, and the Transformer decoder translates the graph-level embedding back into the graph. This formulation enables the model to capture both the global graph structure and local relational patterns. We evaluate our method on multiple graph datasets, spanning various domains. The results demonstrate effectiveness of our method in encoding and reconstructing graphs from their embeddings.

---


### 858. [Let the Neurons Die: Exploiting ReLU-Induced Model Degradation](https://arxiv.org/abs/2609.35528)

**<font color=#1a73e8>作者：</font>** Kexin Li, Wenjun Qiu, Joshua Abraham 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rectified linear unit (ReLU) networks can suffer from dying neurons, where units with persistently negative pre-activations produce zero outputs, blocking gradients through their activations. To exploit this failure mode, we present three training-time availability attacks based on data ordering and poisoning. We begin with the basic dynamic data-ordering attack (DOA), which greedily constructs a training prefix by selecting the next example that minimizes the target layer's post-update weight sum, aiming to push ReLU units toward negative pre-activations without modifying training samples or labels. We then develop two poisoning attacks, IG-DOA and IG-SKA, which use gradient inversion to synthesize class-conditioned samples by matching reference gradients in adverse model states constructed through data ordering or soft knockout, respectively. Soft knockout rearranges weights across adjacent layers to concentrate negative contributions. On a fully connected ReLU network trained on MNIST, ordering 100 of 60,000 training examples reduces test accuracy from 96% to 95% after only five epochs. Adding 200 poisoned samples from a single class reduces test accuracy to approximately 86-88% after five epochs in most evaluated conditions, compared with approximately 96% under clean training. These results demonstrate that ReLU-targeted data ordering and poisoning can impair learning without directly modifying the victim model's parameters.

---


### 859. [Optimal Networks for Agentic Information Aggregation](https://arxiv.org/abs/2609.35537)

**<font color=#1a73e8>作者：</font>** MohammadHossein Bateni, Zahra Hadizadeh, MohammadTaghi Hajiaghayi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study information aggregation in the networked learning model introduced by Kearns, Roth, and Ryu (SODA 2026). There is a fixed distribution over $d$ features and a common label. Agents learn in topological order on a directed acyclic graph. Each observes a subset of the features and its parents' predictions, fits a linear predictor to minimize mean squared error, and passes only its prediction forward. The global predictor is the best linear predictor using all features. Kearns, Roth, and Ryu show that the output agent's error approaches the global predictor's error along sufficiently deep paths with suitable feature coverage, while insufficient depth can prevent aggregation even in large networks.
In contrast to their main focus on a given graph and feature allocation, we consider the limits of the model under two settings. In the adaptive designer setting, a designer chooses the graph, feature allocation, and output agent knowing the distribution. In the oblivious designer setting, the designer fixes all three before an adversary chooses the distribution. Each agent observes one feature and receives predictions from a limited number of parents.
We call the aggregation exact when the output agent matches the global predictor exactly. For $d\ge3$, we show that no finite depth guarantees exact aggregation for every distribution with one parent per agent, even when the designer knows the distribution.
In contrast, two parents per agent suffice for exact aggregation even in the oblivious designer setting. A fixed graph, feature allocation, and output agent achieve this for every distribution at depth $O(d\log d)$. Knowing the distribution reduces the depth to $O(d)$. Both constructions use $O(d^2)$ agents, with a very large constant for two parents. We show the bounds on the depth and number of agents are all optimal up to constant factors.

---


### 860. [Learning to Reason with Persistent Object States for Video Instance Segmentation](https://arxiv.org/abs/2609.35539)

**<font color=#1a73e8>作者：</font>** Yongxue Xu, Boxue Yang, Ziqian Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video segmentation models maintain object identities by carrying instance information across frames. Under prolonged occlusion, reappearance, or interactions between similar instances, however, an unreliable update can overwrite a valid history and cause persistent identity drift. We introduce POSReasoner, a trainable, plug-and-play framework that explicitly decides when an observation should change an object's state. Each persistent state records identity, confidence, and absence history. A sparse state-observation graph supports Propose-Verify reasoning: provisional associations are revisited using object history, predicted presence, and competition among identities. The verified decisions determine whether to retain, update, reactivate, or suppress each state, while a learned gate controls the evidence written back to memory. Only verified transitions update the persistent state used in subsequent frames. POSReasoner uses standard video annotations and keeps the base model frozen, enabling integration with diverse VOS and VIS architectures. Experiments across long-term VOS and VIS benchmarks show consistent improvements over strong baselines, with the largest gains under occlusion and object reappearance.

---


### 861. [Learning the Robustness Mechanism with Bilevel Optimization](https://arxiv.org/abs/2609.35541)

**<font color=#1a73e8>作者：</font>** Yiyang Shen, Qihang Lin, Weiran Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a distributionally robust learning framework where parameters defining the robustness mechanism are learned from held-out data instead of extensively tuned. Using bilevel optimization with both upper and lower level minimax problems, we create two instances of our framework to tackle setups with and without group labels in the training set. Theoretically, we provide sample complexity analysis for our robustness mechanism learning paradigm, showing that it achieves generalization guarantees comparable to exhaustive grid search while being more computationally efficient. Empirically, we evaluate our framework under a challenging setup when both intra-group and inter-group test distribution shifts occur at the same time, thereby demonstrating the efficacy and scalability of our method.

---


### 862. [Graph World Models for Constrained Epidemic Policy Planning](https://arxiv.org/abs/2609.35545)

**<font color=#1a73e8>作者：</font>** Yiqi Su, Rashed Shelim, Lingyi Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Epidemic policy planning often requires coordination between geographical regions, taking into account mobility-driven spillovers and how to make use of limited resources. Existing methods either lack action-conditioned models of coupled dynamics or cannot guarantee per-period feasibility. We present EpiMind, a graph world model framework for constrained epidemic policy planning across regions. A graph-factored recurrent state-space model generates joint policy-conditioned rollouts from regional latent beliefs, while graph-temporal ADMM optimizes regional interventions, enforces shared-resource feasibility through projection, and evaluates temporal specifications under the learned model. EpiMind reduces admission RMSE by 29% relative to graph-free dynamics modeling, plans within 1-5% of the best feasible constant policy with guaranteed shared-budget feasibility, and outperforms all deployable baselines across three resource budgets in real-context evaluation. These results demonstrate that graph-structured policy imagination with explicit constrained coordination supports effective epidemic interventions from learned dynamics.

---


### 863. [BaRe-Mem: Bayesian Reliability Memory for Robust and Adaptive Agent Consultation](https://arxiv.org/abs/2609.35551)

**<font color=#1a73e8>作者：</font>** Peilin Feng, Zhengyang Huang, Soujanya Poria  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In multi-agent systems, reliable consultation is challenging because advisor capabilities vary across tasks, and misleading information can make consultation worse than autonomous reasoning. We introduce BaRe-Mem, an online Bayesian reliability memory for multi-agent consultation. It estimates advisor reliability based on the central model's internal belief representations and updates these estimates from historical interactions. These estimates modulate the influence of advisor responses and guide the choice between consultation and autonomous reasoning. Across nine benchmarks and six central models, BaRe-Mem is more robust to misleading advisor information than debate and majority voting. On the more challenging tasks, it remains above autonomous reasoning across all tested misleading levels. Moreover, we extend the BaRe-Mem mechanism to worker allocation in agent teams. On the MuSiQue benchmark, BaRe-Mem improves task completion over routing by historical success counts and identifies capable workers earlier.

---


### 864. [Simplex Diffusion Models](https://arxiv.org/abs/2609.35553)

**<font color=#1a73e8>作者：</font>** Justin Deschenaux, Alexandre Galashov, Andrew Campbell 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models have revolutionized generative modeling for continuous data through the gradual refinement of a belief state. This iterative refinement has not yet carried over to discrete diffusion models, which discard uncertainty at intermediate steps through categorical sampling (information collapse). We propose Simplex Diffusion Models (SDMs), a framework that lifts the diffusion process to the probability simplex to represent beliefs over categories. SDMs admit probability paths with closed-form reverse transitions and can be trained with a simple cross-entropy loss. Contrary to earlier proposals such as Dirichlet Flow Matching which requires integrating an ordinary differential equation, we introduce a DDIM-like sampler with a tunable level of stochasticity. Because SDMs operate on samples on the simplex, they can carry uncertainty across denoising steps, which mitigates information collapse. On OpenWebText, SDMs are competitive with strong Discrete Diffusion baselines, achieving $17.0$ GenPPL at $5.46$ unigram entropy in 64 sampling steps, close to real validation data. Even without Self-Conditioning (SC), SDMs outperform masked and uniform diffusion (with SC or predictor-corrector sampling) on code generation (TinyGSM, $T=0.1$; $49.0\%$ vs. $45.8\%$). Distilled down to 8 steps, SDMs solve $32.1\%$ of GSM8K problems, more than distilled Discrete Diffusion models with 128 steps ($21.4\%$).

---


### 865. [Positional choice and robust collective behavior in fish schools: biohybrid experiments and modeling](https://arxiv.org/abs/2609.35554)

**<font color=#1a73e8>作者：</font>** Vahagn Grigoryan, Donato Romano, Cesare Stefanini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Collective behavior of fish schools is usually modeled on the assumption that each individual follows specific rules of motion that depend on its position and velocity relative to its neighbors. Although these models reproduce many schooling patterns observed in nature, it remains unclear whether the assumed rules are realistic at the individual level. To address this question, we first analyzed a set of experiments in which a live fish interacted with four moving robotic fish in a tank, and measured the time it spent in each position relative to the robots. We then simulated this experiment, replacing the fish with an agent, and assessed the extent to which classical models agree with the experimental observations. An extensive exploration of the parameter space showed that these models closely matched the experimental observations, with a very specific choice of parameters. However, they were highly sensitive to the parameter values: a minor perturbation caused them to fail completely. To resolve this, we propose a new model that incorporates an additional exploratory term characterizing the agent's positional preference at every moment. This model proved robust to small errors in the parameters while successfully replicating the experiments. Furthermore, when generalised to multiple fish, the model reproduced schooling behaviour and common schooling patterns, while also exhibiting exploratory behaviour at both the individual and the school level. This shows that social cohesion coexists with individual exploratory behaviour, and that realistic models of collective behaviour should account for both social interactions and this exploratory component.

---


### 866. [WorldPlay2: Extending Real-Time Interactive World Models in Control and Horizon](https://arxiv.org/abs/2609.35560)

**<font color=#1a73e8>作者：</font>** Haiyu Zhang, Wenqiang Sun, Tengfei Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive world models require responding in real time to versatile controls and maintaining long-horizon consistency. However, modeling heterogeneous controls remains difficult, while explosive contexts and unstable distillation impede achieving both long-horizon consistency and real-time responsiveness. In this paper, we present WorldPlay2, an interactive world model that couples a factorized hybrid control interface with a co-design of compressed memory and stable distillation. 1) Our factorized hybrid control interface integrates frame-aligned action control with structured semantic control that explicitly disentangles scene appearance, character identity, and dynamic semantic events, thereby facilitating effective control learning. 2) To achieve efficient long-horizon modeling, we compress historical contexts into compact memory tokens shared by the autoregressive student and the bidirectional teacher. This design enables clip-wise, memory-conditioned score evaluation instead of jointly processing an entire long rollout, substantially reducing distillation overhead. 3) We further propose Stable Forcing, which initializes the autoregressive student via a few-step strategy and leverages full-rollout replay to preserve the quality of long-horizon rollouts, ensuring robust and stable distillation. Extensive experiments demonstrate the strong generalizability of our model and its superior performance compared to existing methods.

---


### 867. [Revisiting Risky Tackle Detection with Vision Transformers](https://arxiv.org/abs/2609.35562)

**<font color=#1a73e8>作者：</font>** Syed Ahsan Masud Zaidi, Lior Shamir, Scott Dietrich  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper is a Track 2 reproducibility companion to an ICPR 2026 study on risky tackle detection in American football prac- tice videos. The original work fine-tuned a Video Vision Transformer (ViViT) on 733 clips labeled with the SATT-3 rubric. It used focal loss, Taguchi L18 augmentation, and 5-fold cross-validation. It reported risky- class recall of 0.67 and risky-class F1 of 0.59. This companion documents the released artifact and traces those numbers to specific scripts, fold out- puts, and aggregation files. The reproduced headline is run_15. It com- bines Gaussian noise with static brightness decrease and uses no rotation and no flip. Its fold-mean risky recall is 0.667 and its fold-mean risky F1 is 0.588. These values match the published headline after rounding. The ablation shows that brightness is the dominant factor. Its risky-recall main-effect range is 0.055, which is larger than the ranges for rotation, flip, and noise. Without augmentation, ViViT reaches risky recall of 0.545 and does not exceed the C3D baseline of 0.583. The raw clips show iden- tifiable student athletes, so they cannot be redistributed. The artifact provides a public sample for pipeline checks and a controlled route for full-data review.

---


### 868. [Less Is More: Genetic Frame Selection for Efficient Novel View Synthesis](https://arxiv.org/abs/2609.35573)

**<font color=#1a73e8>作者：</font>** Diego E. Farchione, Ramzi Idoughi, Alberto Jaspe-Villanueva 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward novel view synthesis reconstructs a scene from many input images in a single forward pass, yet more views do not necessarily improve performance: redundant or poorly chosen frames increase computational cost and may degrade reconstruction quality. We address the problem of selecting, from an already captured sequence, a fixed-size subset of input views that is most informative for reconstructing specified target viewpoints. We propose a render-free view selector that scores candidate frames based on three complementary criteria: target-view coverage, measured against observed frames that stand in for the targets, redundancy with previously selected views, and image sharpness. A lightweight scoring network then selects the most informative frames without rendering, reconstruction, or per-scene optimization at inference time. To train the selector, we distill an expensive offline search procedure in which a genetic algorithm identifies high-quality subsets by directly optimizing reconstruction performance on training scenes. The selector learns to reproduce these choices from geometric and image-level features alone. Across six datasets and multiple input budgets, our method consistently outperforms both geometric and reconstruction-aware view-selection baselines while incurring significantly lower selection costs than reconstruction-based alternatives. Moreover, carefully selected subsets can outperform feed-forward reconstruction from the full input sequence. The learned selector generalizes across diverse reconstruction paradigms (feed-forward, 3D Gaussian Splatting, and NeRF), to object-targeted reconstruction and to a cross-capture setting in which the target views come from a separate acquisition pass. More broadly, our results indicate that explicitly reasoning about target relevance and inter-view redundancy is a fundamental factor in efficient scene reconstruction.

---


### 869. [What Paired Evaluations Reveal under Visual Perturbations](https://arxiv.org/abs/2609.35583)

**<font color=#1a73e8>作者：</font>** Yongda Wei, Chen Zhang, Yifei Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robustness evaluation must examine diverse visual perturbations, while benchmarks cover only some real-world conditions and physical testing is costly. Paired evaluations link clean and perturbed predictions for the same image, capturing changes in correctness, confidence, and acceptance beyond aggregate accuracy. We investigate how this image correspondence supports two needs in robustness evaluation: interpreting paired evaluation results and prioritizing samples for physical testing. To interpret paired evaluation results, we fix both sets of prediction records and vary their correspondence within each class. We prove that classwise correct-correct counts give the same sharp bounds on lost acceptance and mean true-class probability decrease among retained-correct inputs as any feasible five-state refinement. Distinguishing persistent from changed wrong answers can further constrain accepted-error transitions, while shared correspondence can establish policy orderings left unresolved by separate cost intervals. To prioritize samples for physical testing, we retain each image's synthetic responses and rank clean-correct images by their mean true-class probability under corruption. Across 44 classifiers, testing the highest-risk 20% finds 67% and 45% of failures under mild screen and print recaptures, versus 58% and 36% for clean confidence and 60% and 37% for an equal-size natural-transformation average. With both probability averaging and an A3Rank scoring adaptation, the tested corruption set yields higher mean failure recall than the natural-transform set; differences between scores depend on the source and budget. Together, these findings show that the value of correspondence depends on the evaluation objective: classwise counts suffice for specified reliability bounds, while image-specific synthetic responses improve the allocation of physical tests within the evaluated pool.

---


### 870. [Hardware-Aware Features for CUTLASS Kernel Selection](https://arxiv.org/abs/2609.35587)

**<font color=#1a73e8>作者：</font>** Shriram Chandran, Dominic Rinderer, Yakup Budanaz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> GPU libraries such as CUTLASS expose tens of thousands of semantically equivalent kernels for a single operation, making exhaustive autotuning expensive and execution-free selection difficult. Existing analytical selectors require hand-designed performance rules, while learned selectors operate on raw configuration parameters and must infer hardware consequences from data. We introduce a hardware-aware representation for CUTLASS kernel selection that augments candidate configurations with statically computable estimates of induced hardware behavior. We construct a dataset of 4.9 million CUTLASS kernels and train gradient-boosted and neural learning-to-rank models to rank candidates within each problem. On held-out exhaustive evaluation problems, hardware-aware representations reduce selection regret by up to 40\% relative to structural baselines and 64.2\% relative to NVIDIA's matrix-multiply heuristics. We further evaluate data-efficient cross-precision and epilogue-fusion transfer within CUTLASS GEMM, showing that explicitly representing candidate-induced hardware behavior provides a useful inductive bias for learned kernel selection.

---


### 871. [Source-preserving alignment for robust evidence localization in scientific PDFS](https://arxiv.org/abs/2609.35588)

**<font color=#1a73e8>作者：</font>** Zihao Liu, Wei Yang, Zixiao Dong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific information-extraction systems often return a claim with an evidence string, which users must locate in the original PDF. This is challenging because the extracted evidence and PDF text layer are different representations: line wrapping, Unicode variants, superscripts, citation markers, and fragmented items alter text sequences and geometry. We present a source-preserving alignment framework: normalize text for robust matching while preserving provenance for accurate localization. It aligns evidence with normalized page text, maps matches back to source-character spans, and renders only their geometry. When exact alignment fails, line-break-aware token alignment recovers supported spans while excluding unmatched noise. Experiments on 1,020 chemistry papers show that the framework achieves a 92.6\% quote-level automatic localization rate, compared with 43.6\% for text search and 19.1\% for a precomputed bounding-box baseline. Component ablation confirms distinct contributions from normalization and approximate token alignment, while human verification assesses the visual correctness of returned highlights. Overall, these results demonstrate that reliable evidence verification requires robust matching and precise localization within a shared source-preserving alignment representation.

---


### 872. [ReSS: Residual-Restoring Sparse Attention for 3D Vision Transformers](https://arxiv.org/abs/2609.35593)

**<font color=#1a73e8>作者：</font>** Yongsung Kim, Jaehoon Lee, Minjun Park 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D vision transformers such as VGGT predict camera poses and scene geometry from multi-view images in a single forward pass, but their global attention over all concatenated view tokens dominates computation as the number of views grows. To reduce this cost, SparseVGGT and HeSS sparsify attention at the block level, and both retain blocks with high attention probability. However, we observe that attention probability poorly predicts how much the model's behavior actually changes when a block is removed, and we show that this mismatch is why performance collapses as sparsity increases. In this paper, we propose ReSS (ReSidual-ReStoring Sparse Attention), which recasts block selection from a problem of maximizing the retained attention mass to one of minimizing the drift that sparsification leaves in the residual stream. We introduce a drift score that quantifies how much each block shifts the residual, and, since the drift of a drop set depends on the directions of the contribution vectors rather than on their magnitudes alone, an iterative residual restoration procedure that refines the drop set as a whole. Across three backbones and five datasets, ReSS preserves dense performance better than prior methods at matched sparsity. Two further results support drift as the quantity that governs the cost of sparsification: maximizing drift degrades performance faster than random selection, and plotted against realized drift instead of sparsity, all methods fall approximately onto a single curve. Code is available at this https URL.

---


### 873. [Control-Geometry Straightening for Sampling-Based Latent Planning](https://arxiv.org/abs/2609.35603)

**<font color=#1a73e8>作者：</font>** Ziang Fu, Ning Ning  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Joint-embedding predictive architectures enable planning with latent world models, but accurate transition prediction alone does not ensure that the planning objective is easy to optimize. We introduce Control-Geometry Straightening (CGS), a single auxiliary loss that learns planner-friendly representations by directly straightening control geometry for sampling-efficient planning. CGS matches pairwise cosine similarities among actions to those among corresponding latent differences only using local transitions from pixel-action pairs. The loss can be applied across world-model architectures using end-to-end learned or pretrained representations. Under linear-dynamics, our theoretical analysis connects this objective to temporal straightening and more balanced terminal-cost curvature across the full planning horizon, yielding finite-budget guarantees for MPPI, local contraction results for CEM, and convergence bounds for gradient descent. Across four control environments and multiple planners, CGS improves planning with fewer sampled candidates and refinement steps, achieving success-rate gains up to 20 and 12.6 percentage points over LeWorldModel (LeWM) and its temporal-straightening variant (LeWM+TS), respectively, with sampling-based planners using 128 candidates per update. Probes, comparisons with DINO-WM architecture, and planner-side ablations clarify how latent motion organization, state dependence, and dynamical context shape planning behavior. Straightening control geometry thus makes good action sequences easier to find under limited planning budgets.

---


### 874. [Simultaneous Translation between Sign Languages](https://arxiv.org/abs/2609.35608)

**<font color=#1a73e8>作者：</font>** Zetian Wu, Bowen Xie, Stefan Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deaf and hard-of-hearing (DHH) signers cannot converse in real time across different sign languages today: existing sign-to-sign translation systems run offline, requiring the full source clip before any target sign is emitted. Live use cases - e.g. broadcast interpretation and two-way video calls - instead demand simultaneous output, while the source signer is still signing. We present, to our knowledge, the first simultaneous sign-to-sign (S2S) translation system, with two wait-k regimes: test-time wait-k inference applied directly to a full-sentence model, and a trained wait-k model via stochastic multi-path supervision. We further introduce ca-Stream-AL, a computation-aware latency metric for streaming output. Averaged across six S2S directions on both a smaller human-verified test set and a larger synthetic S2S corpus, our streaming system achieves a 38% ca-Stream-AL reduction while staying within a 9% DTW-PA-MPJPE increase and a 2.1 BLEU-4 drop compared to the full-sentence baseline. A word-order case study probes how the streaming model handles word order mismatch between different sign languages - a consequence of simultaneous translation.

---


### 875. [On-Policy Self-Distillation for Multi-Turn Image Editing](https://arxiv.org/abs/2609.35611)

**<font color=#1a73e8>作者：</font>** Liangbing Zhao, Le Zhuo, Mohamed Elhoseiny  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instruction-based image editing has achieved strong performance in single-turn settings, yet practical editing is often iterative, with each instruction applied to the output of the previous turn. We find that existing editing models degrade rapidly under recursive editing and attribute this failure to a train-test mismatch in the conditioning distribution: models are trained on clean source images but must repeatedly condition on their own imperfect outputs at inference time. To address this, we propose MT-OPSD, an on-policy self-distillation framework that trains the model on self-generated conditioning states with editing supervision from a clean-conditioned teacher, without requiring multi-turn annotations. We further introduce LME-Bench, a benchmark of 100 ten-turn editing sessions for evaluating long-horizon robustness. Experiments across three editing backbones show that MT-OPSD substantially improves long-horizon editing success and reduces multi-turn collapse while largely preserving single-turn editing quality.

---


### 876. [Remote Sensing Sparse-View 3D Gaussian Splatting via Depth Image-Based Rendering](https://arxiv.org/abs/2609.35612)

**<font color=#1a73e8>作者：</font>** Jiaming Kang, Zhengxia Zou, Zhenwei Shi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing novel view synthesis under sparse observations remains challenging due to insufficient geometric constraints and limited cross-view supervision. Existing Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) methods are prone to overfitting and face challenges of depth ambiguities, missing cross-view information, and insufficient constraints in under-observed regions. To address these challenges, we propose DIBR-GS, a neural Gaussian Splatting framework that exploits Depth Image-Based Rendering (DIBR) to generate pseudo views for cross-view consistency supervision. Specifically, reliable geometric initialization is constructed by aligning monocular depth priors with sparse SfM reconstruction, and cross-view appearance priors are incorporated into neural Gaussian representations to enhance appearance modeling under sparse observations. Furthermore, we introduce a progressive DIBR-based pseudo-view supervision strategy to provide additional geometric and appearance constraints, enabling more complete reconstruction of weakly observed regions. In addition, a height-constrained anchor growth strategy is designed to suppress unreasonable Gaussian expansion. Experiments demonstrate that the proposed method achieves superior performance over existing approaches when training with only 3 input views. Compared with the previous best-performing method, it improves PSNR by 6.83 dB, with relative gains of 14\% in SSIM and 60\% in LPIPS, while maintaining competitive computational efficiency. Our code is available at this https URL

---


### 877. [EvolvingAvatar: Interactive 3D Head Generation That Adapts as Conversations Unfold](https://arxiv.org/abs/2609.35616)

**<font color=#1a73e8>作者：</font>** Junjie Chen, Fei Wang, Kun Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive 3D head generation requires coordinated speaking and listening motion that responds to an evolving conversation. Existing generators use incoming observations as context but keep their parameters fixed, leaving conversational patterns unused as a learning signal. We introduce EvolvingAvatar, a causal generator that uses test-time training to adapt to user face video and dyadic audio during interaction. Its dyadic context prediction objective provides a self-supervised learning signal from audiovisual context without target motion labels at test time. Persistent fast weights accumulate these updates within each conversation to guide motion generation, while transient jaw adaptation responds to current audiovisual context. Predicted speech activity controls how persistent adaptation guides motion. We also introduce InterHead-Bench, a unified 455.95-hour benchmark built from single-view and dual-view conversation videos. Experiments show improved conversational motion statistics over strong baselines. On the hardest out-of-distribution split, generation improves as conversations unfold, reducing mismatch with recorded user-avatar expression statistics by up to 11.1% from the first interval.

---


### 878. [Attention Graphons: A Graph Limit Perspective on Graph Transformers](https://arxiv.org/abs/2609.35620)

**<font color=#1a73e8>作者：</font>** Caio F. Deberaldini Netto, Moshe Eliasof, Luana Ruiz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Transformers produce, for each attention head, a dense $n\times n$ matrix of learned pairwise interactions. We ask a fundamental question: do these attention-induced graphs converge to a stable limit object as $n$ grows, or does the learned interaction pattern remain unstructured and size-dependent? We answer this using dense graph limit theory, treating each attention matrix as a finite sample from an underlying kernel---an \emph{attention graphon}---and studying concentration around this limit under the cut-distance. We derive a worst-case variance bound requiring no assumptions on the graphon, and a sharper regularity-aware bound based on nonparametric estimation theory. To operationalize the theory, we propose a canonicalize-then-block-average pipeline for estimating dataset-level attention graphons, and a variance-based diagnostic for testing whether attention admits a stable continuum description. Experiments across multiple graph benchmarks show that learned attention stabilizes to dataset-specific graphon structure on several datasets; that empirical cut-distance and cut-norm variance decreases with $n$ consistent with our bounds; and that attention graphons transfer to larger graph sizes with error decreasing in $n$.

---


### 879. [RIDE: Reference-Anchored Inference-Time Diffusion Editing for Scaffold Hopping](https://arxiv.org/abs/2609.35623)

**<font color=#1a73e8>作者：</font>** Ruoxi Gao, Frazier N. Baker, Trieu Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scaffold hopping is a critical task in drug discovery, which seeks to discover new, structurally distinct molecules that share key functional groups and similar 3D shape with a reference binding ligand. Existing diffusion-based scaffold hopping methods formulate the problem as conditional generation of scaffolds given the functional groups. However, they lack a principled mechanism to jointly enforce 2D structural novelty and preserve the 3D shape of the reference ligand. Here, we introduce RIDE, a Reference-anchored Inference-time Diffusion Editing framework for scaffold hopping. RIDE recovers the reference diffusion noise trajectory conditioned on the binding pocket and functional groups, selects an optimal trajectory segment for editing via noise perturbation, and conducts a value-guided scaffold sampling to generate new scaffolds. Extensive experimental results demonstrate that, compared to baselines, RIDE consistently generates scaffolds with lower 2D similarity and higher 3D similarity to the reference, with an average improvements of 11.7% and 7.3%, respectively. Further analysis reveals that RIDE can accommodate various reward functions, and can preserve 3D similarity even when this is not explicitly included in the reward. Two case studies illustrate RIDE's ability to generate distinct scaffolds with different structures and properties, and its ability to introduce substantial 2D variation while maintaining very high 3D similarity. RIDE is publicly available at this https URL.

---


### 880. [Arbitrary-Accuracy Neural Approximation with Optimal Neuron Count and Near-Optimal Bit Complexity](https://arxiv.org/abs/2609.35628)

**<font color=#1a73e8>作者：</font>** Zilan Cheng, Li-Lian Wang, Zhongjian Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the minimum number of hidden neurons required for arbitrary-accuracy approximation of multivariate Hölder-continuous functions on $[0,1]^d$ and the associated encoding complexity. For $d\geq 2$, we construct a fixed, explicitly defined activation function for which a closed-form network with two hidden layers of widths $d$ and $1$ achieves arbitrary accuracy in the uniform norm. We prove that $d+1$ is the exact minimum total number of hidden neurons among standard feedforward networks with locally integrable activations and affine outputs. We further give a simpler construction using a single elementary activation that combines the floor and exponential functions. This construction requires three hidden layers of widths $d$, $1$, and $2$, only two neurons above the minimum. If a skip connection is allowed, widths $d$, $1$, and $1$ suffice. These constructions use explicit grid addressing and integer encoding of quantized function values. For a bounded $\alpha$-Hölder class, they require $O(\varepsilon^{-d/\alpha}\log(1/\varepsilon))$ bits, matching the metric-entropy lower bound up to a logarithmic factor.

---


### 881. [Which the Eye Fears: Writing with Read-Blindness Explains Massive Activations in Transformers](https://arxiv.org/abs/2609.35630)

**<font color=#1a73e8>作者：</font>** Swagatam Mukhopadhyay, Vishal Vivek Saley, Vraj Parikh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Massive activation features (MAs) in Transformers are extreme-value residual-stream features that persist across layers despite the model's ability to suppress them. Why do they survive? Our investigation using an operator-level mechanistic analysis of attention and feed-forward (FFN) blocks reveals that these blocks systematically ignore MA coordinates while reading, but not while writing; creating a read-write asymmetry that blocks corrective feedback while allowing continued accumulation. We find that both attention and feed-forward layers have this read-blindness, and contribute to the emergence and persistence of MAs.
To validate prior work that hypothesized that FFN's amplification abilities is the primary reason for MAs (Sun et al., 2026), we analyze the model checkpoints during learning. Contrary to our expectation, read-blindness emerges before FFN amplification, suggesting that it acts upstream in the MA mechanism. We further contribute gradient analysis to link this behavior to surprising asymmetries in the loss landscape, concluding that the model actively maintains this read-blindness. Finally, we find that removing read-blocking at different locations induces compensatory shifts elsewhere, but MAs still persist.

---


### 882. [DR-net-Mamba: Selective State-Space Modeling for Long-Range ECG Time-Series Denoising](https://arxiv.org/abs/2609.35634)

**<font color=#1a73e8>作者：</font>** Basile Morel, Samuel Ruiperez-Campillo, Andreas P. Streich 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electrocardiogram (ECG) recordings are corrupted by non-stationary noise sources that degrade diagnostic reliability, particularly in ambulatory and long-duration recordings. Deep learning denoisers exist, but convolutional architectures are limited by their receptive field, transformer-based models scale quadratically with sequence length, and diffusion-based approaches incur prohibitive inference cost. We propose a Mamba-augmented model that inserts selective state-space blocks at the convolutional bottleneck, combining local feature extraction with long-range temporal modeling at linear complexity. We comprehensively evaluate the proposed model with respect to reconstruction fidelity, noise robustness, recording-length scaling, and downstream diagnostic classification across over 40 pathology classes. On synthetic and real datasets, our model achieves the highest SNR and lowest RMSE, with the Mamba advantage increasing with sequence length and in low-SNR regimes. On classification with two independent classifiers, the proposed Mamba-based models achieve the best macro AUROC among all denoisers and improve over their convolutional base models. Calibration is more nuanced and classifier-dependent: denoising improves Binary Cross-Entropy and Brier score on Inception1D but often fails to beat the noisy input on ResNet1D-Wang, and the lead-specific Mamba variant is the only denoiser to improve both calibration metrics over the noisy baseline on both classifiers. Per-class analysis reveals a morphology-dependent benefit: Mamba substantially improves ST/T-change diagnoses, which depend on broad, context-sensitive waveforms.

---


### 883. [Bounding Retraining Equivalence and the Deletion Floor in Materials Machine Unlearning](https://arxiv.org/abs/2609.35635)

**<font color=#1a73e8>作者：</font>** Can Polat, Mustafa Kurban, Erchin Serpedin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In materials machine learning, closely related retained structures can sustain accurate property predictions even after removing a specific record, rendering post-deletion prediction error an ambiguous metric for machine unlearning. To resolve this ambiguity, we define the deletion floor as the expected target loss under a specified retraining procedure at the deleted request. Standard indistinguishability constraints yield a sharp interval bounding an update's target loss around this baseline reference. Theoretically, a conditional neighbor bound links a low deletion floor directly to retained fit, prediction regularity, and local label agreement, while an exact ridge identity isolates residual fit from the prediction change induced by record deletion. Empirically, controlled redundancy sweeps show an $\approx 8\times$ drop in median normalized retraining loss when one retained relative remains after deletion. Across two distinct fitting regimes in a paired Materials Project study, the lower-floor regime also exhibits a larger prediction change on more than 50% of the shared requests. Systematic comparisons against approximate updates and the original model decouple deliberate target suppression from preserved overall model utility. Consequently, request-level unlearning evaluations should report reference loss, prediction change, and retained utility together, interpreting post-deletion accuracy against what retraining itself leaves behind.

---


### 884. [RT-Super: Learning Tumor Segmentation from Longitudinal Images and Reports](https://arxiv.org/abs/2609.35637)

**<font color=#1a73e8>作者：</font>** Pedro R. A. S. Bassi, Wenxuan Li, Hanxue Gu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-tumor segmentation is important for early cancer detection and allows radiologists to visualize, verify, and understand AI predictions. However, tumor segmentation masks are expensive, time-consuming, and unavailable for many tumor types in public data. Instead, hospitals have vast, readily available data that can guide segmentation: radiology reports, longitudinal images, and multi-phase images. We use this readily available data to substitute for tumor masks in training AI for tumor segmentation. To this end, we propose a new architecture, RT-Super. It has a teacher network, which analyzes the patient's longitudinal images and reports to create high-quality tumor masks. These masks train a student network, which sees a single image and no report. At inference, when longitudinal images and reports are unavailable, we use the student. RT-Super uses a new CNN-Transformer architecture and novel Consistency Losses that exploit tumor location consistency across longitudinal images. We train RT-Super to segment esophagus, uterus and spleen tumors, which have few or no public masks. Even without training masks, RT-Super can segment these tumors and surpass public AI models. Overall, we demonstrate that learning from longitudinal images, multi-phase images, and reports can overcome mask scarcity and advance multi-cancer detection and segmentation. Code: this https URL

---


### 885. [Transferable Mass Spectrum Prediction via Reference-Guided Test-time Specialization](https://arxiv.org/abs/2609.35649)

**<font color=#1a73e8>作者：</font>** Yunhua Zhong, Runting Li, Yifan Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tandem mass spectrum prediction supports compound identification across metabolomics, natural-product discovery, and environmental analysis. However, pretrained predictors often degrade under shifts in chemical space and acquisition conditions, while retraining domain-specific models from scratch is costly. We introduce SPARC, a retrieval-guided test-time specialization framework that adapts a pretrained predictor using a spectral reference library without accessing test-query spectra. For each target query, SPARC retrieves chemically related reference spectra to recalibrate fragment intensities within the learned fragmentation space. During Transfer, SPARC combines reference-guided spectral adaptation with reliability-aware consistency, using reconstruction behavior on retrieved spectra to selectively preserve trustworthy predictions during continual specialization. Across MassSpecGym, NPLIB1 and application-specific GNPS libraries, SPARC improves spectral prediction under multiple transfer settings. These results establish retrieval-guided test-time specialization as a practical strategy for extending pretrained MS/MS predictors to specific chemical and acquisition domains, with continual test-time training providing further refinement during deployment.

---


### 886. [Many Eyes, One World: Feed-Forward 3D Reconstruction from Mixed Cameras](https://arxiv.org/abs/2609.35658)

**<font color=#1a73e8>作者：</font>** Qiaoge Li, Yifan Zhan, Haijun Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world capture is heterogeneous: perspective, fisheye, and $360^\circ$ panoramic images can coexist within a single reconstruction task, yet most feed-forward 3D reconstruction models assume perspective imagery and a uniform input representation. Recent models handling several camera types are either informed of the camera type for each view or reconstruct one image pair at a time. No single-pass method reconstructs mixed-camera tuples containing full panoramas from images alone. We present MEOW, a feed-forward system that jointly reconstructs metric pointmaps and camera poses from one N-view tuple mixing perspective, fisheye and full-panorama images, in a single forward pass from images alone: no calibration, distortion parameters, camera-type labels or poses are supplied for any view. Our guiding design philosophy is to treat heterogeneous-camera reconstruction as a data-adaptation problem rather than an architectural redesign. MEOW retains a perspective-pretrained backbone and learns heterogeneous cameras entirely from a procedural data engine, which renders each scene across a continuous manifold of camera models with exact rays and depth, and certifies covisibility for every camera-sampled training tuple. Trained on synthetic tuples only, MEOW transfers zero-shot to real captures: on heterogeneous 2D3DS tuples it achieves 79.9 mAA@30 against 53.8 for Wid3R given the camera type of every view; on our laser-scanned mixed-camera benchmark it registers every four-view mixed tuple with 79.4 AUC@30. The data engine, benchmark, and complete evaluation pipeline will be released.

---


### 887. [MS-GLA: Multi-Scale Gated Linear Attention for Addressing Representational Bottlenecks via Multi-Temporal Resolution](https://arxiv.org/abs/2609.35664)

**<font color=#1a73e8>作者：</font>** Prasoon Dev, Anirudh Sankar, Vasudeva Varma  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Gated Linear Attention (GLA) Transformers advance linear recurrent models through data-dependent gating, but face a core limitation: the fixed-capacity memory matrices across all heads operate at a single temporal resolution, where each token is processed individually, forcing them to simultaneously encode local syntactic patterns and long-range semantic structure, creating a representational bottleneck that gating alone is insufficient to resolve. We introduce Multi-Scale Gated Linear Attention (MS-GLA), which addresses this by distributing attention heads across multiple temporal resolutions. Coarser resolutions pool longer token spans naturally specializing toward long-range dependencies, while finer head groups retain sensitivity to local syntactic structure. A learnable, input-dependent fusion layer dynamically recombines head group outputs at each timestep, expanding effective memory capacity without increasing per-head state size. This multi-resolution decomposition draws on principles from Multi-Scale State-Space Models (MS-SSM), adapting them to the gated linear attention setting. We evaluate MS-GLA on language modeling, recall-intensive tasks, and long-context generalization. Across all settings, MS-GLA consistently achieves higher accuracy and lower perplexity than GLA at matched parameter counts, with up to 18.9% improvement on recall-intensive tasks and 9.5% lower average perplexity on language modeling benchmarks, validating multi-temporal resolution decomposition as a principled and effective extension of Gated Linear Attention.

---


### 888. [Tracing the Evolution of Oracle Bone Characters Across Three Millennia](https://arxiv.org/abs/2609.35674)

**<font color=#1a73e8>作者：</font>** Tianhao Fu, Xinxin Xu, Spike Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Of the approximately 4,500 Oracle Bone Inscription (OBI) characters discovered from the Shang dynasty, only about 1,600 have been deciphered. Many computational approaches compare OBI with glyphs from one historical period at a time. However, during the evolution of Chinese characters, significant structural or semantic changes often occur in uncertain dynasties. A single-period reference may be insufficient when relevant forms change substantially between observed eras. Therefore, we propose the \textbf{Manifold-based Script Evolution Framework (MSEF)}, a framework that models the evolution series (OBI, Bronze, Seal, Clerical, Regular) of Chinese characters as the continual evolution of a manifold space. MSEF represents each character as an era-specific manifold point and learns continuous inter-era transition rules via Neural Ordinary Differential Equations. Both manifold space and transition dynamics can be trained end-to-end through character evolution pairs across any two eras.

---


### 889. [Provable Benefits of Regularization: Fast Rates for Adversarial Imitation Learning](https://arxiv.org/abs/2609.35698)

**<font color=#1a73e8>作者：</font>** Hanbin Zhou, Shangzhe Li, Alexander Braverman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study adversarial imitation learning (AIL), in which an agent learns to imitate expert demonstrations by optimizing a policy against an adversarial reward that distinguishes expert and learner behavior. Historically, reward regularization and entropy-based policy regularization are key components of empirically successful methods such as GAIL and LS-IQ, yet their finite-sample benefits remain underexplored. We establish fast rates for jointly regularized AIL in finite-horizon Markov decision processes with general function approximation. Our model-free algorithm, Dually Regularized AIL, combines KL policy regularization with a quadratic reward penalty weighted by expert and learner occupancies. With K online episodes and N expert trajectories, we prove a $\widetilde{O}\left(\frac{1}{K}+\frac{1}{N}\right)$ bound on the regularized imitation gap for fixed regularization parameters. Our analysis combines an online mirror descent construction for general convex reward classes to control estimation error from finite expert data and stochastic learner feedback, with a sharp analysis of optimistic KL-regularized policy learning. To the best of our knowledge, Dually Regularized AIL is the first algorithm to simultaneously achieve $\widetilde{O}\left(\frac{1}{\epsilon}\right)$ sample complexity in both expert demonstrations and online interactions for this regularized AIL objective, even with stochastic experts. These results provide a rigorous characterization of the complementary statistical benefits of reward and policy regularization in AIL.

---


### 890. [A Unified Uncertainty Representation for Graph Neural Networks via Doubly-Spectral Stochastic Expansion](https://arxiv.org/abs/2609.35703)

**<font color=#1a73e8>作者：</font>** Fred Xu, Thomas Markovich, Florence Regol 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable deployment of graph neural networks requires calibration, out-of-distribution (OOD) detection, and robustness to distribution shift, yet existing methods address these needs with separate models and
objectives. We model uncertain node embeddings as random graph signals: graph Fourier filters capture structural variation, and a scalar orthogonal-polynomial chaos coordinate captures latent stochastic
variation. The resulting doubly-spectral stochastic (DSS) expansion supplies task-matched readouts from one representation: the mean coefficient encodes class evidence for the energy-based OOD score, the
higher-order coefficients encode structured logit variation, and quadrature averaging over the chaos coordinate defines the single predictive distribution used for prediction and calibration. A capacity theorem
shows that, under a full-rank feature assumption, a restricted subfamily matches the chaos coefficients of any Gaussian-latent random graph signal, with exponentially decaying truncation error under a growth
condition; the task-level claims are established empirically. DSS-GNN has two deployment modes: standalone, or as a residual branch beside a deterministic encoder (DSS-Hybrid). Standalone DSS-GNN achieves the
lowest Brier score among the compared uncertainty-aware baselines on all 14 node classification benchmarks without post-hoc correction; DSS-Hybrid achieves the best AUROC on most node-OOD settings, competitive
cross-graph OOD detection, and the strongest shifted accuracy on all 7 GOOD concept-shift benchmarks under standard empirical risk minimization (ERM). Cross-evaluating both modes on all three tasks shows that
each remains effective on the other's tasks, with documented exceptions, and yields explicit deployment guidance.

---


### 891. [DynaTokens: Teaching Dynamics to Camera-Controlled Video Models at Test Time](https://arxiv.org/abs/2609.35704)

**<font color=#1a73e8>作者：</font>** Ziqi Ma, Hongqiao Chen, Georgia Gkioxari  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation must account for two sources of motion, one induced by the observer's camera path and the other caused by scene dynamics. An ideal camera-controlled video model should account for both motions: let users move the camera while evolving the scene dynamics. While current models handle camera-induced motion well in static settings, they struggle for dynamic scenes: objects are static, move incorrectly, or degrade in generation quality. We introduce DynaTokens, a lightweight set of learnable scene-specific tokens that teach dynamics to an existing camera-controlled world model. Our method is motivated by a simple asymmetry between the two sources of motion: whereas camera motion affects the generated view globally, object dynamics are spatially localized. Through cross-attention, DynaTokens trains the learnable tokens from a few example trajectories for a scene while keeping the base model frozen, and enables dynamics under new query camera paths. DynaTokens achieves a better simultaneous dynamics-camera tradeoff on VBench2 and WorldScore evaluations than LoRA, block finetuning, and specialized trainable-layer baselines. Analyses of token attention, ablations, and motion temporality suggest that matching the trainable interface to the structure of the learning target is important for effective adaptation. Project website: this https URL

---


### 892. [Mind the RefGAP: Correcting Reference Attention in Diffusion-Based Visual Editing](https://arxiv.org/abs/2609.35708)

**<font color=#1a73e8>作者：</font>** Yanan Wang, Shengcai Liao, Guangyi Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reference-guided diffusion editors struggle to faithfully reproduce user-provided references. We identify a potential bottleneck in diffusion editors: many methods provide limited reference-attention allocation. For example, in LoomVideo, edit-region queries assign less than 1% of their attention mass to the reference. We introduce RefGAP, a training-free correction that determines logit-offset magnitudes online at each layer from the reference-attention mass measured during the forward pass. Positive offsets to reference logits strengthen reference usage by edit-region queries, while negative offsets for keep-region queries limit reference-induced changes outside the edit. Two global coefficients control the correction; they are selected once on validation data from four development diffusion editors and held fixed. Across seven diffusion-based image/video editors, RefGAP improves identity fidelity in head swapping and face swapping. RefGAP achieves a fidelity-preservation trade-off comparable to separately tuned constant edit-side biases, without per-approach strength sweeps. Additional experiments on virtual try-on and background replacement evaluate transfer beyond identity editing.

---


### 893. [Lagrangian--Hamiltonian Flows for Video Prediction and Image Generation: A Symplectic Perspective](https://arxiv.org/abs/2609.35710)

**<font color=#1a73e8>作者：</font>** Jiawei Hu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce LHFM, a geometric framework for learning image dynamics. Drawing on structures central to classical mechanics, symplectic geometry, and geometric quantization, LHFM represents each image as an exact Lagrangian graph and models its evolution through image-dependent Hamiltonian flows, which yield a transport--source parameterization of image velocities. Our primary application is deterministic video prediction: LHFM-V is a recurrent model that advances frames by integrating predicted transport and source fields, and achieves the lowest reported FLOP count among the compared recurrent models with similar prediction accuracy. The image variant, LHFM-I, shows that the same construction is compatible with flow matching: in a matched experiment, it attains a lower FID than the flow-matching baseline.

---


### 894. [X-Reset: Scaling Object-Centric Reinforcement Learning via Cross-Embodiment Resets](https://arxiv.org/abs/2609.35715)

**<font color=#1a73e8>作者：</font>** Prithwish Dan, Chenyang Ma, Wei Zhan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) in simulation can train dexterous manipulation policies without robot demonstrations, but training a single generalist policy with task-agnostic rewards faces a severe exploration problem: approaching, grasping, and reorienting diverse objects with many degrees of freedom is difficult to discover from scratch. Prior works make exploration tractable with high-quality robot demonstrations, per-task reward shaping, or by restricting policies to narrow modes of behavior. We propose X-Reset, a framework that instead resolves exploration with human hand-object demonstrations. Rather than imitating or tracking retargeted human motion, X-Reset kinematically retargets hand-object states to noisy robot states, filters out states that are unstable in simulation, and samples the remainder as resets during RL training with general-purpose object-centric rewards. The resulting policy depends only on object state and goal, with demonstrations entering training through the reset distribution. We show that X-Reset trains generalist policies on 20 objects across three embodiments---a 22-DoF hand on two different arms and a parallel-jaw gripper---and resolves the exploration challenges of RL from scratch. X-Reset scales with the number of training objects, generalizes to unseen objects, can learn from imperfect hand-pose estimates, and transfers behaviors zero-shot from sim-to-real.

---


### 895. [Superquadric Primitive Decomposition of 3D point clouds via Geometric-Aware Inlier Refinement](https://arxiv.org/abs/2609.35725)

**<font color=#1a73e8>作者：</font>** Alessandro Rinaldi, Edoardo Tedesco, Andrea Ferraris 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The decomposition of 3D point clouds into interpretable geometric primitives remains a longstanding challenge in Computer Vision and Computer Graphics. Among the available representations, superquadrics offer a compact and expressive model capable of capturing a wide range of shapes. However, their estimation is inherently challenging, as it requires solving a non-linear optimization problem and is particularly sensitive to noise, outliers, and overlapping structures. While robust estimation methods such as RANSAC and its variants achieve strong performance, they rely primarily on spatial proximity and residual-based criteria, often leading to incorrect inlier assignments across adjacent or complex arrangements of primitives. In this work, we introduce a geometric-aware framework for primitive decomposition that explicitly incorporates local surface properties into the fitting process. Specifically, we propose an inlier refinement step formulated as an energy minimization problem and solved via graph-cut optimization. Our formulation integrates geometric priors, such as normal consistency, enabling more reliable inlier selection beyond purely residual-based criteria. The approach naturally applies to both single-model estimation and multi-model decomposition. By leveraging geometric information beyond point-wise residuals, our method reduces erroneous inlier propagation and stabilizes parameter estimation. Experiments on synthetic and real datasets show consistent improvements in geometric accuracy, robustness to noise and outliers, and convergence efficiency compared to state-of-the-art RANSAC-based methods.

---


### 896. [Impact of Patient Orientation in Single- and Multi-View Camera Environments for AI-based Rehabilitation Monitoring](https://arxiv.org/abs/2609.35726)

**<font color=#1a73e8>作者：</font>** Miriama Jánošová, Andreas Lang, Petra Budikova 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated quality assessment of rehabilitation exercises relies heavily on accurate human pose estimation from video data. Although numerous RGB-based pose estimation methods have been proposed, the impact of camera placement on detecting clinically relevant movement errors remains insufficiently explored. To address this gap, we introduce REHAB26-ViewAngles, a dataset comprising correct and incorrect rehabilitation exercise executions captured from a wide range of camera angles. Furthermore, we propose a novel separability metric to quantify an algorithm's ability to distinguish between valid and faulty exercise repetitions. Using these tools, we analyze how various RGB-based pose-estimation strategies are suitable for exercise quality assessment under varying camera placements. In particular, we analyze single-camera 2D and 3D pose estimation and four multi-camera strategies: a combination of two orthogonal 2D views, 3D triangulation, weighted 3D fusion, and an AI-based pose-estimation transformer model specifically trained from two synchronized cameras. Our findings reveal that an optimally placed 2D camera can improve the separability by 16.9\,\% over the commonly used $0^\circ$ frontal view and frequently outperforms single-camera 3D estimation, while combining two views can further improve accuracy by up to 13.1\,\%. These results offer practical guidance for deploying rehabilitation monitoring in both home and clinical settings.

---


### 897. [FlowAct-R2: Beyond Talking Avatar via Streaming Multimodal References and Proactive Agent Planning](https://arxiv.org/abs/2609.35728)

**<font color=#1a73e8>作者：</font>** Ziyao Huang, Zhengkun Rong, Shiyang Qin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present FlowAct-R2, a framework for interactive humanoid video generation that combines continuous multimodal control with proactive agent planning. Our method consists of two coupled components. First, a Streaming Multimodal Reference Diffusion Transformer adapts the pretrained Seedance 2.0 Mini reference-to-video backbone to accept rolling action prompts, streaming audio, and dynamically updated image, audio, and video references. Video-driven rotary positional embeddings align reference chunks with the generation timeline, while reference-plus-image conditioning and partially noised historical motion frames preserve appearance and avoid accumulated drift. Second, a Proactive Interaction Agent separates pre-online planning from online scheduling and response: it prepares a persona, a long-horizon agenda, and reusable multimodal skills in advance, then autonomously schedules behaviors, responds to audience input, and handles interruptions during a live session. FlowAct-R2 supports real-time 720p generation and hour-scale streaming across entertainment streaming, live shopping, video chatting, and live vlogging.

---


### 898. [GeoVerse: World-Consistent Novel View Synthesis in Geometric Latent Space](https://arxiv.org/abs/2609.35734)

**<font color=#1a73e8>作者：</font>** Kerui Ren, Tao Lu, Linning Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Novel view synthesis from sparse images must reconcile faithful reconstruction of observed regions with plausible completion of unseen content, while maintaining world consistency across viewpoints. Existing geometry-based methods preserve observed scene structure but often struggle to complete unseen regions, whereas video generative models offer rich appearance priors but accumulate inconsistencies during sequential view generation. We propose GeoVerse, a framework that synthesizes world-consistent novel views by performing generation within the geometric latent space of a pretrained 3D foundation model and injecting appearance priors from a video generative model. Specifically, GeoVerse extracts multilevel features from Wan2.2 VACE and injects them into the geometric latent diffusion model via a ControlNet-style adapter, incorporating video-learned appearance priors to enhance structural completion. To enforce cross-view coherence, a global spatial memory continuously aggregates observed and synthesized content, reprojecting target-aligned guidance to anchor subsequent predictions to a shared scene representation. Extensive experiments across diverse datasets demonstrate improved visual quality and geometric consistency, with a 2.23 dB higher PSNR on DL3DV and 32.4% lower ATE on Mip-NeRF360 compared to GLD.

---


### 899. [InfiniHand: Streaming World-Space Hand Motion Estimation from Egocentric Video](https://arxiv.org/abs/2609.35743)

**<font color=#1a73e8>作者：</font>** Kerui Ren, Kaiwen Song, Weiguang Zhao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World-space hand motion estimation from egocentric video requires recovering 3D articulated hand geometry while tracking camera egomotion. Existing approaches heavily rely on cascading independent hand pose estimators and SLAM systems, resulting in error accumulation, complex pipelines, and severe computational overhead. To address these limitations, we present InfiniHand, an end-to-end streaming feed-forward framework that jointly estimates MANO parameters, camera trajectories, and hand locations directly from uncalibrated egocentric video. InfiniHand integrates persistent spatiotemporal memory with hand-centered visual features, explicitly coupling camera motion with local hand geometry within a unified architecture. We train InfiniHand in two progressive stages by first learning robust camera-space hand priors and then extending to streaming world-space reconstruction. To support this process, we aggregate a pretraining corpus of approximately 5,000 hours of egocentric data across multiple public datasets. Extensive evaluations demonstrate that InfiniHand outperforms state-of-the-art baselines on in-domain benchmarks, achieving a 21.4% reduction in ARCTIC PA-p compared to ViDiHand while substantially mitigating world-space drift. Furthermore, InfiniHand generalizes robustly to in-the-wild videos and operates at 11.19 FPS, delivering more than twice the throughput of HaWoR.

---


### 900. [FinAutoRubric: Expert-Guided Automatic Rubric Generation for Evaluating Financial Research Agents](https://arxiv.org/abs/2609.35744)

**<font color=#1a73e8>作者：</font>** Hoyoung Lee, Suyeol Yun, Jack Haverty 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating finance research agents requires rubrics that reflect expert standards and fix the values correct as of an information cutoff. Expert-reviewed finance benchmarks rely on fixed, per-item rubrics, which are costly to extend and cannot encode each institution's own standard. In FinAutoRubric, experts specify reusable evaluation guidance, while agents and code carry out query-specific rubric generation, review, and validation. This expert guidance governs every agent, as prompts and as rules that code enforces, and a Task Bank of reusable criteria carries it across tasks. In long-horizon loops that follow the expert guidance, a writer agent researches every expected value and a reviewer agent verifies it, and failures escalate to a human. On three expert-authored finance benchmarks, its rubrics track expert scoring as closely as the strongest evaluated generator while stating the expert rubric's expected value for more criteria, their scores agree with human grading, and in-house analysts prefer them in a blind review. The released 100-query FinAutoRubric Benchmark, built from in-house analysts' key questions across 78 tasks and eight asset classes, shows that rubrics from an earlier model generation still leave headroom for a later one.

---


> [!TIP]
> 当前位于：**851-900**（第 18/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | **851-900** | [901-908](./part-19.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
