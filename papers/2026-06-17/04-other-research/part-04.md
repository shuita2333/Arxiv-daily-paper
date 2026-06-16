# 📦 其他研究 | 2026年06月17日

> 本类共 **509** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-509](./part-11.md)

---

### 151. [Cognitive Trajectory Modeling: Quantifying Human-AI Co-Creation through Cognitively Grounded Interaction Trajectories](https://arxiv.org/abs/2606.15358)

**<font color=#1a73e8>作者：</font>** Nicholas Davis  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Co-creative AI research increasingly seeks methods capable of representing how interaction dynamics evolve through time. While many existing approaches focus on observable interaction characteristics, interaction metrics, behavioral coding schemes, or activity traces, these methods often struggle to capture higher-order interaction dynamics, including how collaborative processes reorganize, stabilize, regulate, and evolve through time. This paper introduces Cognitive Trajectory Modeling (CTM) as a cognitive theory of interaction dynamics that conceptualizes cognition, interaction, and creative processes as temporally organized trajectories unfolding across cognitively meaningful attractor landscapes. CTM builds upon the theoretical foundations of the Enactive Model of Creativity and Creative Sense-Making (CSM), revisiting the role of sense-making curves and cognitive trajectories in representing co-creative interaction dynamics. We formalize this perspective through the Cognitive Trajectory Principle, which states that temporal representations are only theoretically interpretable as cognitive trajectories when their underlying states possess directional cognitive meaning. Building on this principle, CTM generalizes the notion of cognitive trajectories beyond any particular coding scheme and provides a broader framework for modeling interaction dynamics through trajectories unfolding across meaningful attractor landscapes. We further distinguish cognitive trajectories from interaction traces and situate CTM within a broader hierarchy of cognitive, interaction, and domain dynamics. More broadly, we argue that understanding co-creative systems requires methods capable of modeling how cognition and interaction dynamics unfold through time. CTM provides a foundation for studying interaction dynamics across co-creative AI and human-AI interaction.

---


### 152. [DiRecT: Safe Diffusion-Based Planning via Receding-Horizon Denoising](https://arxiv.org/abs/2606.15359)

**<font color=#1a73e8>作者：</font>** Paolo Giaretta, Zeyang Li, Navid Azizan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models have emerged as powerful tools for planning and control by learning multimodal distributions over actions and trajectories. Yet reliable inference-time safety enforcement remains a key barrier to their deployment in safety-critical tasks. Existing approaches typically project each denoising iterate onto the feasible set, even though constraints are defined only on the final clean trajectory. Enforcing feasibility on noisy intermediate samples can therefore overconstrain the sampling dynamics, substantially degrading sample quality. To address this limitation, we introduce DiRecT (Diffusion-based planning via Receding-horizon denoising with Terminal constraints), a training-free algorithm for constrained sampling from diffusion models via stochastic optimal control (SOC). DiRecT enforces constraints only on the final clean sample, avoiding unnecessary restrictions on the intermediate denoising dynamics. Inspired by model predictive control, we derive a principled receding-horizon surrogate for the otherwise intractable constrained SOC formulation, yielding an efficient algorithm that cleanly separates stochastic denoising from constraint satisfaction, progressively steering samples toward feasible final trajectories without distorting the learned diffusion dynamics. Furthermore, DiRecT is highly flexible: it can leverage off-the-shelf or domain-specific optimizers, incorporate priors over environment dynamics, and optimize additional soft rewards. Extensive experiments on safe planning benchmarks demonstrate that DiRecT substantially improves deployment safety and task performance over existing diffusion-based planning baselines.

---


### 153. [APEX: Adaptive Principle EXtraction A Three-Layer Self-Evolution Framework for Production AI Agents](https://arxiv.org/abs/2606.15363)

**<font color=#1a73e8>作者：</font>** Ya-Chuan Chen, Tien-Jen Lai, Hsiang-Wei Hu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-improvement in AI agents has emerged as a key research frontier: systems that modify their own prompts, workflows, and decision rules based on accumulated operational experience. The state-of-the-art Self-Harness framework [1] achieves 14--21% improvement on Terminal-Bench-2.0 by mining failure clusters and patching the agent harness. However, Self-Harness optimises only one dimension -- the prompt harness -- leaving behavioural principles and workflow topology unchanged. We propose APEX (Adaptive Principle EXtraction), a three-layer co-evolution framework that simultaneously evolves: (L1) the harness via failure-mode patching, (L2) behavioural principles via success-trace distillation [2], and (L3) the agent workflow topology via structural fitness-based selection [6]. We implement APEX on Joe [13], a production-grade super AI Agent built on NVIDIA Nemotron and designed as an Edge AI Agent Factory for the NVIDIA Agent Challenge 2026, managing a 15-node compute fleet using 114 real task traces collected over 18 days. APEX achieves an APEX Health Score of 0.570 (+90% vs. baseline 0.300) in a single evolutionary run, distilling 6 novel reusable principles and selecting a research-first workflow topology scoring 0.900 (+20%). Our results demonstrate that multi-dimensional co-evolution substantially outperforms single-axis harness optimisation, at a cost of only 4 LLM calls (~270 s) on a local qwen2.5-coder:32b instance.

---


### 154. [S1-DeepResearch: Beyond Search, Toward Real-World Long-Horizon Research Agents](https://arxiv.org/abs/2606.15367)

**<font color=#1a73e8>作者：</font>** Yao Dong, Xinglin Xiao, Liwei Dong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep research agents aim to solve complex knowledge-intensive tasks through long-horizon planning, evidence gathering, reasoning, and report generation. While recent progress in search agents has demonstrated strong capabilities in information retrieval and answer verification, most existing training datasets remain search-centric, focusing primarily on closed-ended question answering and information localization. As a result, they mainly train information-seeking behavior while providing limited coverage of key deep research capabilities, including evidence integration, knowledge synthesis, planning, file understanding, and structured report generation. In this work, we propose a unified trajectory construction paradigm for deep research agents that combines closed-ended QA and open-ended exploration. The proposed framework consists of graph-grounded task formulation, agentic trajectory rollout, and multi-dimensional trajectory verification, enabling scalable synthesis of high-quality agentic trajectories spanning long-chain complex reasoning, deep research instruction following, report writing, file understanding and generation, and skills usage. Compared with existing search-oriented datasets, our synthesized trajectories place greater emphasis on knowledge synthesis, complex reasoning, and planning. S1-DeepResearch-32B achieves state-of-the-art performance among open-source models of comparable scale across 20 benchmarks spanning five capability dimensions, including complex reasoning, instruction following, report generation, file understanding, and skills usage. On several challenging deep research benchmarks, it approaches the performance of leading proprietary frontier models. These results highlight the importance of jointly modeling information acquisition, knowledge synthesis, and planning-oriented agent behaviors for building effective deep research agents.

---


### 155. [Repeated Bilateral Trade: The Quest for Fairness](https://arxiv.org/abs/2606.15369)

**<font color=#1a73e8>作者：</font>** François Bachoc, Roberto Colomboni, Emilie Kaufmann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study repeated bilateral trade from a fairness perspective. At each round, a fresh seller-buyer pair arrives, and the platform posts a price before observing the traders' valuations. Trade occurs only if both agents accept the price. Rather than maximizing only the gain from trade, we consider platforms that seek balanced divisions of the generated surplus. We show that natural fairness desiderata lead to a one-parameter Rawls-to-Nash family of fair-gain objectives, obtained by aggregating the seller's and buyer's net gains through nonpositive Hölder means. Unlike the standard gain-from-trade objective and the Rawlsian fair-gain objective studied in prior work, our proposed objectives induce a new statistical structure in which expected rewards are recovered from threshold feedback through a two-dimensional singular-kernel integral identity. This leads to a nonstandard pure-exploration problem whose natural estimators are rectangular double sums with row-column dependence and singular weights. Assuming independent i.i.d. seller and buyer valuation sequences with arbitrary unknown marginals, we characterize the optimal learning rates for the whole Rawls-to-Nash family of fair-gain objectives, giving matching fixed-confidence sample-complexity and regret bounds up to polylogarithmic factors.

---


### 156. [MNet++: Extended 2D/3D Networks for Anisotropic Medical Image Segmentation](https://arxiv.org/abs/2606.15370)

**<font color=#1a73e8>作者：</font>** Kirsten Odendaal, Rade Bajic  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work demonstrates a full reproduction and extension of MNet, a hybrid 2D/3D convolutional network designed for anisotropic medical image segmentation. The original architecture was re-implemented within the nnU-Net framework to verify its reported performance and robustness to variable voxel spacing, known as anisotropy. Experiments were conducted on PROMISE prostate MRI and a controlled subset of LiTS liver CT under matched preprocessing and compute constraints. The reproduced MNet achieved a Dice similarity coefficient (DSC) of 89.0 +/- 0.9% on PROMISE, within 0.8% of the published result, and 94.3 +/- 1.9% / 54.6 +/- 3.1% for liver and tumor segmentation on LiTS, respectively. Two lightweight extensions were further introduced: (1) a learned Fusion Gating mechanism enabling adaptive 2D-3D feature blending, and (2) a VMamba state-space module for efficient long-range depth modelling. The Spatial Gating variant improved DSC by +0.8% with less than 3% inference overhead, while VMamba improved performance consistency, reducing PROMISE Dice variation to +/- 0.7% and achieving the strongest LiTS liver performance at 95.8% Dice. Both extensions preserved MNet robustness to anisotropy, with delta Dice = 1.5% across 1-4 mm voxel spacing. Overall, the study confirms MNet reproducibility and demonstrates that adaptive fusion and state-space modelling have the potential to further strengthen segmentation reliability under anisotropic conditions. However, further tests are required to provide definitive conclusions.

---


### 157. [Learning Earthquake Wave Arrival Time Picking from Labels with Inaccuracies](https://arxiv.org/abs/2606.15377)

**<font color=#1a73e8>作者：</font>** Sen Li, Xu Yang, S. Mostafa Mousavi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inaccurately labeled training data, or "label noise", poses a significant threat to the integrity of supervised machine learning models. This corruption directly degrades performance by teaching the model erroneous mappings between features and labels, which leads to poor generalization and reduced accuracy on properly labeled validation and test data. Current seismological applications mainly rely on large-scale training sets or data augmentation to reduce the label-noise impact, which can be labor-intensive and costly. Here, we introduce a Label Noise-Contrastive Robust Learning (LaNCoR) approach that can effectively handle noisy labels in seismic signal processing tasks, without requiring large-scale training datasets. In this approach, the input waveform feature and label representation distributions are aligned in the feature space to correct mislabeling and reduce its impact on the training process. We present LaNCoR's performance on the task of P-phase arrival-time picking of real microseismic data using two baseline models and training approaches. Our results indicate that LaNCoR can improve performance by up to 28.8% across performance metrics. This approach holds great promise for model training in seismology and geosciences.

---


### 158. [Rethinking the Role of Efficient Attention in Hybrid Architectures](https://arxiv.org/abs/2606.15378)

**<font color=#1a73e8>作者：</font>** Ziqing Qiao, Yinuo Xu, Chaojun Xiao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern language models increasingly adopt hybrid architectures that combine full attention with efficient attention modules, such as sliding-window attention (SWA) and recurrent sequence mixers. However, how these efficient modules shape model capabilities remains poorly understood. To address this gap, we conduct a systematic analysis across hybrid architectures from three perspectives: scaling behavior, mechanism analysis, and architecture design. First, from a scaling perspective, we find that efficient-attention design primarily affects how fast long-context capability emerges, while different hybrids eventually converge to comparable long-context performance under sufficient training. Second, mechanistically, we show that long-range retrieval is mainly carried by full attention, whereas efficient attention shapes its optimization trajectory. This explains a counter-intuitive phenomenon we call Large-Window Laziness: larger SWA windows can delay the formation of retrieval heads in full-attention layers. Third, guided by this mechanism, we show that applying NoPE to only the full-attention layers of a small-window SWA hybrid substantially improves long-context performance with negligible impact on short-context performance.

---


### 159. [A Compositional Framework for Open-ended Intelligence](https://arxiv.org/abs/2606.15386)

**<font color=#1a73e8>作者：</font>** Ida Momennejad, Roberta Raileanu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Open-ended intelligence is the capacity to adapt to novel problems and environments that are substantially different from those in training. We formalize open-ended intelligence as the closure induced by a finite primitive set \(P\) and a set of composition operators \(C\). We characterize properties of the induced closure \(\mathcal{L}(P,C)\) that support unbounded compositional generation across families of tasks and worlds. A mathematics of open-ended intelligence requires two pillars: a minimal set of representational primitives (e.g., states, actions) and algorithmic primitives (e.g., nearest neighbor), together with composition motifs (e.g., recursion, sequencing) that reflect an acquired compositional grammar. The closure of these two pillars enables the generation of infinite adaptive responses across a wide range of settings. The mathematics supports complementary research agendas, including evaluation metrics for explanation and interpretability, as well as building architectures where compositional generalization is native. We propose next primitive prediction as a novel architectural objective, where the training objective encourages the acquisition of reusable algorithmic primitives and their compositional grammar, such that new solutions are generated through recombination. Curriculum learning and self-play enable lifelong learning and expansion of the closure by discovering reusable primitives and transition motifs across families of tasks and worlds. We ground the framework through case studies in physics, evolution, and neuroscience.

---


### 160. [Timestep Rescheduling in Diffusion Inversion](https://arxiv.org/abs/2606.15389)

**<font color=#1a73e8>作者：</font>** Shangquan Sun, Ting Gong, Zhirui Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion inversion, which maps images back to the Gaussian latent space of a diffusion model, is a critical task for image reconstruction and editing. While DDIM enables fast deterministic inversion, it inherently introduces deviations that accumulate into noticeable inversion errors. Existing methods often address this by solving a fixed-point problem but largely overlook how the selection of the diffusion timestep in the noise scheduler influences inversion fidelity. In this work, we reveal that the deviation scale in diffusion inversion is strongly dependent on the timestep size, and exhibits a parabolic trend, with larger errors concentrated at both small and large timesteps. Based on this finding, we propose a simple yet effective nonuniform timestep scheduler that integrates a global rescaling with a local dynamic programming based rescheduling, enabling a strategic allocation of computational effort that minimizes the overall inversion error and preserves higher inversion accuracy. Our method serves as an off-the-shelf enhancement for existing inversion techniques and requires no extra parameters or computational overhead. Through extensive experiments, we verify that integrating our scheduler consistently boosts the performance of existing inversion methods, achieving superior results in image reconstruction and editing.

---


### 161. [T-Mem: Memory That Anticipates, Not Archives](https://arxiv.org/abs/2606.15405)

**<font color=#1a73e8>作者：</font>** Weidong Guo, Dakai Wang, Zixuan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term memory is essential for conversational agents to remain coherent across extended dialogues, follow through on commitments made many sessions earlier, and adapt their behaviour to each user. Current LLM-backed long-term conversational memory, however, is reachability-bounded by the similarity between a query and stored content, both lexical and dense-vector. The approach is effective when query and memory share surface features such as wording or named entities (we call this descriptive). But it misses another, equally valuable class of cases, where query and memory do not share surface features and are tied only by a latent semantic arc (associative). On this regime prevailing long-term memory systems collectively fail. Covering this other half is what allows an assistant, for the first time, to actively draw on past dialogue as a semantic asset. On the memory side, this is the engineering counterpart of what cognitive science calls episodic future thinking: rehearsing past experience for the future contexts under which it will need to be found. We call these write-time rehearsals triggers. We propose T-Mem, the first long-term conversational memory architecture that covers both descriptive and associative recall. At each of two evidence granularities, single facts and full exchanges, T-Mem instantiates one descriptive trigger family and one associative trigger family, so that every memory remains reachable from both surface-similar and relevance-bound queries. As empirical validation, T-Mem reaches state-of-the-art on both LoCoMo and LoCoMo-Plus.

---


### 162. [Segmentation-based Detection for Efficient Multi-Task Spacecraft Perception](https://arxiv.org/abs/2606.15409)

**<font color=#1a73e8>作者：</font>** Sivaperuman Muniyasamy, Surendar Devasundaram  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-based perception is fundamental to Space Situational Awareness and autonomous on-orbit operations such as rendezvous, docking, servicing, and navigation. However, progress in this area is limited by the scarcity of annotated space imagery and by challenging visual-domain characteristics including severe illumination changes, low signal-to-noise ratio, and high contrast. We address Stream 1 of the SPARK 2026 Challenge, which requires a single model for spacecraft classification, detection, and fine-grained component segmentation across multiple target types. We propose a compact architecture that integrates a MobileNetV3 encoder with a U-Net-style decoder, combining computational efficiency with accurate dense prediction. Detection is derived analytically from the union of predicted component masks, avoiding a separate bounding-box regression head in the single-spacecraft setting. Our method achieved an overall leaderboard score of 0.9482, with task-specific scores of 1.0000 in classification, 0.9788 in detection, and 0.8917 in segmentation. The proposed approach ranked second overall in the SPARK 2026 Challenge, demonstrating that lightweight encoder-decoder architectures can deliver strong multi-task performance for practical onboard space vision systems.

---


### 163. [Pepti-Agent: An AI Agent for Peptide Design and Optimization](https://arxiv.org/abs/2606.15422)

**<font color=#1a73e8>作者：</font>** Houxu Chen, Achuth Chandrasekhar, Amir Barati Farimani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Therapeutic peptides occupy a valuable design space between small molecules and biologics, but their development requires satisfying several competing constraints at once: solubility, hemolytic activity, and nonspecific surface fouling are governed by overlapping sequence features, so improving one property often degrades another. Computational design addresses this by pairing generative models with sequence-based property predictors, iteratively proposing and refining candidates. However, these components are typically wired together as monolithic scripts that are difficult to inspect, extend, or reuse, and they often refine sequences by natural-language reasoning rather than by tracking the evolving multi-property state of each candidate. We present Pepti-Agent, a closed-loop, peptide-specific framework that exposes generation, property prediction, and single-residue mutation as independently inspectable Model Context Protocol (MCP) tools. A large language model controller invokes these tools and consults live predictor output between calls, so refinement is guided by each sequence's current property profile rather than by language reasoning alone. Task-specific PeptideGPT models generate candidates, ProtBERT-based classifiers score solubility, hemolysis, and non-fouling, and two interchangeable mutation operators propose sequence edits. By recording a per-step trace of controller decisions, predictor outputs, and accepted mutations, Pepti-Agent offers a reproducible substrate for benchmarking multi-objective design strategies and for prioritizing candidates for experimental validation.

---


### 164. [Transfer Learning for FHIR Questionnaire Terminology Binding](https://arxiv.org/abs/2606.15449)

**<font color=#1a73e8>作者：</font>** Maxim Gorshkov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Electronic prior authorization workflows require FHIR Questionnaire items to carry LOINC codes, yet most items in the HL7 Da Vinci CDS-Library lack these bindings. We treat this as a retrieval problem: given a Questionnaire item's text, find the correct LOINC code in a pool of 97,314 active codes. We compare six methods (TF-IDF, frozen MiniLM, BioBERT, BioLORD, contrastively fine-tuned MiniLM, and a TF-IDF+GPT reranker) on a 54-item evaluation set spanning three query styles (natural question, medium, and terse). No single method wins on every metric. BioLORD, a frozen encoder pre-trained on biomedical ontology definitions, has the best top-rank accuracy (R@1 = 0.185, MRR = 0.246) despite seeing no task-specific data, while a contrastive fine-tune on raw LHC-Forms pairs takes R@5 (0.389) and R@10 (0.426). A distribution-shift ablation shows why the fine-tune in our main table is not the strongest one: adding GPT-generated paraphrases to the raw pairs drops R@5 from 0.389 to 0.296, so the augmented union underperforms raw-only training on every metric except R@1. Performance peaks at 5k training pairs. Error analysis on BioLORD's R@1 failures shows that wrong-specificity and ambiguous-text cases together account for 59% of errors.

---


### 165. [PHINN: Persistent Homology Inspired Neural Network for Rare-Event Time Series Generation](https://arxiv.org/abs/2606.15452)

**<font color=#1a73e8>作者：</font>** Emre Yusuf, Ren Takahashi, Jayabrata Bhaduri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rare events in time series are critical to model but hard to learn due to data scarcity. Current generative models struggle with extreme values. We observe that rare events leave distinct topological fingerprints - transitions in Betti numbers from point-cloud embeddings - that are more stable and discriminative than statistical moments.
We introduce PHINN, a flow-matching framework using dynamic Betti curves as conditioning signals and a persistence landscape loss for homology consistency. It scales to multivariate data, includes a natural-language interface to set Betti targets, supports cross-domain meta-learning and few-shot generation, and provides certified adversarial robustness.
On financial, epidemiological, and multi-modal benchmarks, PHINN outperforms statistical and diffusion baselines in topological fidelity (beta-RMSE down 41-63%, transition accuracy up 84%) and matches jump-diffusion models in tail coverage while exceeding them in shape fidelity. All results have 95% confidence intervals.

---


### 166. [Understanding Diversity Collapse in RLVR via the Lens of Overtraining](https://arxiv.org/abs/2606.15455)

**<font color=#1a73e8>作者：</font>** Suqin Yuan, Jinkun Chen, Jiyang Zheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has become a key approach for enhancing the reasoning abilities of large language models. However, RLVR often suffers from \emph{diversity collapse}: Pass@$1$ improves while high-$k$ Pass@$k$ degrades, which is viewed as a narrowing of the model's reasoning boundary. We formalize this diversity collapse through the lens of \emph{overtraining}: once a problem's contribution to the reference metric has effectively saturated, further updates no longer expand what the model can solve but still concentrate probability mass on the trajectories favored by on-policy sampling. Under a standard setup with few rollouts per problem, even a single observed success places a problem in a nearly saturated regime for high-$k$ Pass@$k$, so most updates in standard RLVR are overtraining from the boundary perspective. This perspective also suggests a reading of whether RLVR can expand the model's reasoning abilities beyond the base model: since RLVR is structurally biased against high-$k$ Pass@$k$, its aggregate decline does not by itself mean that no new reasoning gains occurred. Interventionally, restricting updates to problems with zero observed success lifts Pass@$256$ above the base model on difficult benchmarks; observationally, a non-trivial fraction of initially unsolvable problems become solvable during standard RLVR training. Building on these findings, we propose \emph{Bayesian Boundary Gating} (BBG), which redirects optimization away from overtraining by estimating each problem's marginal contribution to the reasoning boundary. Across multiple reasoning benchmarks, BBG improves average Pass@$k$ across a wide range of $k$.

---


### 167. [Lesion-DDPM: Lesion-Enhanced 3D Diffusion for MS MRI Synthesis](https://arxiv.org/abs/2606.15457)

**<font color=#1a73e8>作者：</font>** Weidong Zhang, Yongchan Jung, Shafayat Mowla Anik 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D FLAIR MRI is widely recommended as one of the standard MRI sequences for brain imaging in multiple sclerosis (MS), but publicly available MS datasets remain relatively small and vary across scanners, acquisition protocols, and lesion patterns. This scarcity and variability hinder the development of robust neuroimaging machine learning models and are particularly challenging for generative models that aim to synthesize images while preserving small, sparse lesions. We propose Lesion-DDPM, a 3D conditional diffusion framework for lesion-aware FLAIR synthesis that incorporates multi-level anatomical mask injection together with a lesion-weighted reconstruction loss to emphasize lesion voxels while maintaining global brain structure. Using a curated subset of the MSLesSeg dataset, we compare Lesion-DDPM with representative state-of-the-art GAN- and diffusion-based models, assessing both image-generation metrics and downstream 3D U-Net segmentation. In our experiments, Lesion-DDPM achieved the lowest lesion-region reconstruction error among all methods. In a downstream 3D U-Net lesion segmentation task, a model trained only on Lesion-DDPM-generated scans and evaluated on real MRIs reached a Dice score of 0.616 compared with 0.569 for the best competing synthetic dataset. When Lesion-DDPM images were added to the real training set, the Dice score further increased to 0.685.

---


### 168. [ESBMC-PLC: Formal Verification of IEC 61131-3 Ladder Diagram Programs Using SMT-Based Model Checking](https://arxiv.org/abs/2606.15461)

**<font color=#1a73e8>作者：</font>** Pierre Dantas, Lucas Cordeiro, Waldir Junior  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> PLCs execute safety-critical programs across industrial sectors. The dominant PLC notation, ladder diagram (LD) per IEC 61131-3, remains absent from formal verification: SMT-based model checkers cannot process LD's rung-and-coil graphics. This paper presents ESBMC-PLC, the first open-source formal verifier with native LD support (PLCopen XML format), implemented as a new ESBMC frontend. ESBMC-PLC translates LD rungs to GOTO IR, models the PLC scan cycle as a while(true) loop with nondeterministic inputs, and checks safety properties via SMT-based bounded model checking or k-induction. A five-property YAML language (mutual_exclusion, invariant, absence, response, reachability) avoids temporal logic. A survey of 22 studies (2020-2026) identifies four research gaps; ESBMC-PLC closes two of them. Evaluation on 13 benchmarks (6 domains, 3 sources - including deployed CONTROLLINO PLCs and MathWorks Simulink PLC Coder) shows correct classification across 61 properties: all 9 author-constructed programs (Categories A/B) as expected, all 4 vendor programs (Category C) correctly unlabeled, with 8 bugs found (actionable counterexamples), 7 unbounded k-induction proofs, all runs under 60ms on Apple Silicon. Feature comparison with PLCverif shows that ESBMC-PLC is the only open-source tool that combines native LD, k-induction, and SMT bit-vector semantics.

---


### 169. [The Audit Gap in Blockchain Security: A Four-Year Empirical Study of Public Audit Findings and Real-World Exploit Incidents](https://arxiv.org/abs/2606.15465)

**<font color=#1a73e8>作者：</font>** Stefan Beyer  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper presents an empirical analysis of the Web3 security landscape over the four-year and three-month period from 1 January 2022 to 27 March 2026. The dataset combines 23,818 public audit findings produced by 22 independent security firms with 218 real-world exploit incidents documented by this http URL, representing aggregate losses of approximately US$7.76 billion. We report three central findings. First, the distribution of audit findings (by severity, category, and technology stack) is substantially stable across the observation window, with the Critical-plus-High share remaining within a 15-17% band in every complete year. Second, the categorical distribution of realised exploit losses does not correspond to the categorical distribution of audit findings: private-key compromise, phishing, and social-engineering vectors account for approximately 49.6% of cumulative losses yet represent a negligible share of published audit findings. Third, realised losses exhibit extreme concentration: the eight largest incidents account for 50.6% of cumulative dollar losses and the twenty largest for 71.4%, a distributional shape inconsistent with Gaussian assumptions. Throughout, we adopt the analytical convention that audit outputs and exploit outputs describe different populations and present the two datasets in parallel rather than as directly comparable samples.

---


### 170. [Analyzing Visual Aircraft Representations with Sparse Autoencoders](https://arxiv.org/abs/2606.15468)

**<font color=#1a73e8>作者：</font>** Deepshik Sharma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision models can achieve strong performance on classification tasks, but the internal representations supporting their predictions are often difficult to interpret. This work investigates whether sparse autoencoders can decompose intermediate representations of a vision model into interpretable features. We train a ConvNeXt classifier on the FGVC-Aircraft dataset, extract spatial activations from its final feature stage, and train a sparse autoencoder on these activations. The learned sparse features are analyzed using top-activating image patches, activation strength, and class selectivity. Qualitative visual inspection reveals that several features correspond to recognizable aircraft structures and visual patterns. We evaluate a subset of selected features using input-space and feature-space ablations, measuring how blurring image patches and suppressing sparse features affect class logits, classification margins, and prediction confidence. The results suggest that sparse autoencoders can reveal partially interpretable, class-relevant visual features associated with aircraft recognition, while also exposing limitations such as polysemanticity and coarse spatial localization.

---


### 171. [Bayesian 3D Steerable CNNs: Enabling Equivariance and Uncertainty Quantification Simultaneously](https://arxiv.org/abs/2606.15479)

**<font color=#1a73e8>作者：</font>** Abhishek Keripale, Ponkrshnan Thiagarajan, Susanta Ghosh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Steerable convolutional neural networks (Steerable-CNNs) guarantee SE(3)-equivariance by parameterizing kernels as linear combinations of steerable basis functions, but their deterministic nature precludes uncertainty quantification - limiting their use in settings where confidence estimates are essential. We propose a Bayesian Steerable-CNN that places posterior distributions over the basis coefficients, yielding stochastic kernels while preserving equivariance exactly. The loss function of the model is obtained via variational inference and minimized by Bayes-by-Backpropagation. The framework admits a decomposition of predictive uncertainty into epistemic and aleatoric components. Empirically, the model attains competitive classification accuracy alongside an expected calibration error of 0.0263 and outperforms its deterministic counterpart by up to 6.17% under distributional shift induced by additive Gaussian noise. Furthermore, we leverage the model's uncertainty estimates to enhance its performance significantly, achieving a notable gain - approximately 4% higher accuracy across 84% of the test dataset. A statistically significant negative correlation between epistemic uncertainty and prediction error confirms that the learned posterior variance is semantically meaningful. The framework unifies Bayesian uncertainty quantification with the inductive bias of equivariant CNNs.

---


### 172. [Evaluative Judgement in Teaching AI-based Translation: A Class-room Case Study of AI-Mediated Translation and Post-Editing](https://arxiv.org/abs/2606.15483)

**<font color=#1a73e8>作者：</font>** Gokhan Dogru  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Drawing on 23 anonymized student pro-jects from a fourth-year Machine Transla-tion and Post-editing course in a BA-level translation programme, this paper exam-ines how structured comparison of gen-eral-purpose LLMs and online MT sys-tems can elicit evaluative judgement in AI-mediated translation. Students translat-ed short specialised English Wikipedia texts into Catalan or Spanish, generated four system outputs, evaluated them using automatic metrics and human adequa-cy/fluency assessment, selected one output for post-editing, and justified their deci-sion in written reports. Descriptive counts are reported for all 23 projects, while qualitative interpretation is based on the 22 cases accompanied by written reports. Results show that students did not treat automatic metrics as final authority: final post-editing selections often diverged from metric rankings and were justified through adequacy, fluency, terminology, naturalness, and expected post-editing ef-fort. The study therefore does not bench-mark systems under controlled conditions; it analyses how students justified system choice within an authentic classroom as-signment.

---


### 173. [ST-DiffEye: Diffusion-based Continuous Gaze Generation via Joint Scanpath-Trajectory Modeling](https://arxiv.org/abs/2606.15486)

**<font color=#1a73e8>作者：</font>** Brian Nlong Zhao, Ozgur Kara, Junho Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study the problem of human gaze modeling, which aims to generate the gaze patterns a viewer produces while observing a visual stimulus. Gaze is primarily captured through two modalities: continuous eye-tracking trajectories, which describe fine-grained motion dynamics, and discrete scanpaths, which describe high-level fixation structure. Because gaze varies substantially across viewers and trials, we treat this variability as a defining property rather than noise and model gaze as a stochastic generative process. Existing generative gaze models supervise on only one of these two representations in isolation. We hypothesize that trajectories and scanpaths describe gaze at complementary scales and are jointly informative during training, and test this hypothesis through ST-DiffEye, a joint trajectory-scanpath diffusion framework that couples both modalities by concatenating them as an additional raw input channel, requiring no architectural overhead beyond an input and output channel expansion. We further introduce a principled evaluation framework based on the Continuous Ranked Probability Score (CRPS), which generalizes any existing sequence similarity metric into a proper scoring rule that jointly assesses the accuracy and diversity of generated gaze. Experiments on task-driven visual search, covering both target-present and target-absent scenarios, and on free-viewing benchmarks demonstrate state-of-the-art performance. These results, along with detailed ablations, confirm the benefit of joint modeling and the value of distribution-aware evaluation in capturing the intrinsic variability of human gaze. Project webpage: this https URL

---


### 174. [Model Stealing Through the Lens of Model Multiplicity](https://arxiv.org/abs/2606.15493)

**<font color=#1a73e8>作者：</font>** Eliott Baltz, Satoshi Hara, Ulrich Aïvodji  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model stealing attacks, where adversaries create high-fidelity surrogate models, are a significant threat to the intellectual property of machine learning services. Conventional wisdom suggests these surrogates could provide adversaries with economic leverage comparable to the original service providers. This paper challenges this assumption by evaluating model stealing attacks beyond mere fidelity to the target model. Because query-based extraction provides only partial supervision of the target's input-output behavior, the surrogate is not uniquely identified: many near-optimal surrogates can achieve comparable fidelity while differing in deployment-relevant properties. Instead of performing a classic learning-based model stealing attack, we compute the Rashomon Set (i.e., the set of almost-equally-accurate models) of surrogate models, and evaluate its diversity using multiplicity metrics (ambiguity, discrepancy, and Rashomon Capacity) and group fairness metrics. Across tabular, medical imaging, and NLP tasks, our experiments on real-world datasets reveal that despite exhibiting similar fidelity to the target model, surrogate models can display significant variances in other critical performance metrics. These findings cast doubt on the presumed equivalence between high-fidelity surrogates and the target model in practical deployment scenarios.

---


### 175. [Towards End-to-End Automation of AI Research](https://arxiv.org/abs/2606.15497)

**<font color=#1a73e8>作者：</font>** Yutaro Yamada, Robert Tjarko Lange, Cong Lu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The automation of science is a long-standing ambition in the field of AI. While the community has made significant progress in automating individual components of the scientific process, a system that autonomously navigates the entire research lifecycle -- from conception to publication -- has remained out of reach. Here, we present the strongest demonstration to date toward automating the entire process end-to-end. We present The AI Scientist, which creates research ideas, writes code, runs experiments, plots and analyzes data, writes the entire scientific manuscript and performs its own peer review. Its ideas, execution, and presentation are of sufficient quality to produce a manuscript generated by an AI system that passes the first round of peer review at a major machine learning conference workshop. The workshop has an acceptance rate of 70 percent. Our system leverages modern foundation models within a complex agentic system. We evaluate The AI Scientist in two settings: a focused mode using human-provided code templates as an initial scaffold to conduct research on a specific topic, and a template-free, open-ended mode that leverages agentic search for wider scientific exploration. Both settings produce diverse ideas and automatically test, report on, and evaluate them. This achievement demonstrates AI's growing capacity for scientific contribution and signifies a potential paradigm shift in how research is conducted. As with any impactful new technology, there could be significant risks, including taxing overwhelmed review systems and adding noise to scientific literature. However, if developed responsibly, such autonomous systems could greatly accelerate scientific discovery.

---


### 176. [Synthetic Counteradaptation: A Principle of Human-AI Co-evolution](https://arxiv.org/abs/2606.15503)

**<font color=#1a73e8>作者：</font>** Ivar Frisch, Jackie Kay, Philip Moreira Tomei  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this paper, we introduce the concept of synthetic counteradaptation, a process where human and AI systems co-evolve by adapting to each other's strategies and behaviors. Synthetic counteradaptation occurs when AI systems develop novel strategies or social protocols, prompting humans to extract insights and adapt their own behaviors in response, leading to the emergence of new agent interaction dynamics. To illustrate these dynamics, we analyze examples from various contexts, including the game of Go, mixed-motive social interactions, and geopolitical simulations. By exploring these cases, we demonstrate how synthetic counteradaptation provides a framework for understanding the recursive and co-evolutionary nature of human-AI interactions in multi-agent environments.

---


### 177. [Toward Vibe Medicine: A Self-Evolving Multi-Agent Framework for Clinical Decision Support](https://arxiv.org/abs/2606.15504)

**<font color=#1a73e8>作者：</font>** Qianxue Zhang, Yiming Ren, Shihuan Qin 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In recent years, the advances of large language models and autonomous agents have revolutionized the healthcare field, facilitating diagnosis and improving treatment results. However, most existing AI systems rely on pre-trained knowledge and predefined pipelines, which struggle to learn dynamically from the interactive chat session history that contains patient outcomes and past failures. To address this limitation, we propose VIBEMed, a multi-agent framework with a built-in self-evolution mechanism and architecture-level safety sandbox for robust clinical decision support. The system integrates three specialized agents, including a Clinical Diagnostic Agent (CDA) for hypothesis generation, a Therapeutic Execution Agent (TEA) for treatment planning, and a Clinical Evolution Manager Agent (CEMA) that distills longitudinal clinical feedback into reusable knowledge, transforming multimodal patient information into personalized medical decisions. Through self-evolution mechanism, the framework enables iterative updates across memory, model behavior, and decision strategies, allowing the system to improve over time. Experimental results show that VIBEMed demonstrates superior performance through its evolving mechanism in complex clinical cases, particularly in tasks that require integrated decision-making and longitudinal planning. The framework also supports reliable end-to-end decisions in challenging scenarios such as oncology treatment planning, highlighting its feasibility in real-world clinical contexts. Overall, VIBEMed provides a practical path beyond static AI systems toward adaptive, experience-driven clinical decision support, demonstrating the value of combining multi-agent collaboration with continuous evolution for advancing precision medicine.

---


### 178. [What do you mean by human-AI collaboration: Prerequisite functions and the affordances needed to achieve it](https://arxiv.org/abs/2606.15509)

**<font color=#1a73e8>作者：</font>** Mutlu Cukurova  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The concept of 'collaboration' has been extended rapidly to describe what people now do with conversational agents, intelligent tutors, adaptive platforms, and generative artificial intelligence (AI) tools in general. This chapter asks what is gained and lost when a demanding concept from the learning sciences is applied so freely. Returning to long-standing accounts of collaborative learning, it reconstructs the requirements that a situation, an interaction, and a set of cognitive processes have historically had to meet before being called collaborative. Human-AI collaboration requires a partly symmetric and negotiated relationship, shared and negotiable goals, a low and shifting division of labour, interactive and synchronous exchange, and mutual modelling, grounding, and socially shared regulation. Reviewing process-sensitive empirical studies of writing and problem solving, the chapter shows that most current human-AI interaction is better described as consultation, governance, delegation, or instruction rather than as collaboration. To make these distinctions functional, the chapter introduces a five-level diagnostic taxonomy of human-AI teaming (i.e. transactional, situational, operational, praxical, and synergistic) defined by the affordances an AI system exhibits. It shows that only the highest level begins to satisfy the conditions the tradition places on collaboration. The chapter derives the functions an AI system must possess for collaboration to be achievable, argues that most of these are present-day engineering choices rather than capabilities to be awaited, and sets out the implications for research, measurement, and responsible practice of human-AI collaboration in education.

---


### 179. [AthDGC: An Open Diachronic Greek Treebank with Indo-European Parallels](https://arxiv.org/abs/2606.15510)

**<font color=#1a73e8>作者：</font>** Nikolaos Lavidas, Kiki Nikiforidou, Dag Haug 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AthDGC ("Athens-PROIEL") is an open, end-to-end workflow and dataset. It is, to the best of our knowledge, the first openly licensed dependency-parsed treebank of Greek that spans eight diachronic periods, namely Archaic, Classical, Koine, Late Antique, Byzantine, Late Byzantine, Early Modern, and Modern Greek, under a single PROIEL XML 2.0 schema, with verse-level cross-alignment of the New Testament to Latin (Vulgate), Gothic (Wulfila), Old Church Slavonic (Marianus), and Classical Armenian. AthDGC builds on the PROIEL Treebank Family (Haug and Johndal 2008; Eckhoff et al. 2018), which established the schema and the Koine-Greek reference set for the project. Annotation uses the Stanford Stanza PROIEL-trained workflow; sentence-level alignment uses LaBSE, a multilingual sentence-embedding model; word-level alignment uses multilingual-BERT attention through the AwesomeAlign procedure. The v0.4 release provides curated samples and the open-source toolkit; the full annotated corpus partitions remain under v0.5 audit on the Greek national HPC. Quantitative scale, per-witness verse counts, and per-period annotated-row counts are reported in the v0.5 release notes, after the audit pass completes. Concept DOI: https://doi.org/10.5281/zenodo.20439182.

---


### 180. [Towards Data-Efficient Cross-Device Generalization of Grad-Shafranov Equilibria via Transfer Learning Neural Operator](https://arxiv.org/abs/2606.15512)

**<font color=#1a73e8>作者：</font>** Jay Phil Yoo, William Howes, Yashika Ghai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-time reconstruction of magnetohydrodynamic equilibria is essential for plasma shaping, stability assessment and feedback control in magnetic confinement fusion. However, Grad-Shafranov equilibrium calculations remain largely device-specific and iterative, limiting their use in latency-constrained control settings. Existing neural approaches can accelerate individual equilibrium predictions, but they do not generally provide reusable models across changing plasma boundaries or tokamak geometries. Here we show that equilibrium reconstruction can be recast as a cross-device operator learning problem. We develop a domain-specific neural operator framework that maps geometry and profile parameters directly to the poloidal flux field, replacing repeated solve-on-demand computation with amortized operator inference. Using the analytically tractable Solov'ev family as a controlled Grad-Shafranov testbed, we generate equilibria across eight geometrically distinct tokamak-like configurations and benchmark five neural operator architectures under four transfer-learning strategies. Single-geometry pretraining gives poor transfer to unseen devices, whereas multi-geometry pretraining enables data-efficient adaptation. The Wavelet Neural Operator gives the strongest cross-geometry performance, reaching mean relative L2 errors below 4% with 100 labelled target equilibria and below 2% with full fine-tuning. The predicted magnetic fields satisfy the divergence-free constraint to numerical precision, and four architectures achieve millisecond or sub-millisecond inference. These results identify neural operator pretraining as a route towards reusable, real-time equilibrium inference across fusion device configurations.

---


### 181. [A Prototypical Decision-Support Tool for Household Energy Management: A New Zealand Case Study](https://arxiv.org/abs/2606.15513)

**<font color=#1a73e8>作者：</font>** Abdollah Baghaei Daemei  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper presents the system architecture and operating logic of The Home-Energy Check-Up (New Zealand), a web-based public decision-support prototype designed to help New Zealand households identify avoidable energy-cost leakage, complete a short guided home inspection, and generate a prioritized behavior-first energy roadmap. The application is implemented as a single-file Python Streamlit system with session-state navigation, a household input dataclass, conservative low-high saving estimators, a seven-check inspection layer, a recommendation-ranking layer, visual analytics, anonymous Google Sheets persistence, downloadable reports, and a certificate-of-completion interface. The system does not claim to be a certified energy audit, New Zealand Building Code H1 verification method, Healthy Homes compliance statement, or guaranteed bill-forecasting engine. Instead, it operationalizes a practical educational workflow: start with money, collect only the minimum required household profile, convert user answers into a score and action set, estimate annual savings using transparent formulas, and convert behavior savings into a staged save-to-upgrade pathway. The manuscript details the front-end, state-management, calculation, data-storage, visualization, recommendation, deployment, privacy, and limitation layers of the prototype. It also identifies research-grade improvements required before the tool is used for validated impact assessment, including external validation against measured energy data, robust concurrent data writes, clearer uncertainty calibration, accessibility testing, and formal user evaluation. The contribution is a reproducible architecture for translating household energy advice into an interactive, gamified, data-light decision-support pathway for New Zealand homes.

---


### 182. [Selective Synergistic Learning for Video Object-Centric Learning](https://arxiv.org/abs/2606.15527)

**<font color=#1a73e8>作者：</font>** WonJun Moon, Jae-Pil Heo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Typical video object-centric learning (VOCL) approaches employ slot-based frameworks that rely on reconstruction-driven encoder-decoder architectures, where learning is mediated by two spatial maps: attention maps from the encoder and object maps from the decoder. As these two distinct maps exhibit different properties, a recent dense alignment strategy attempted to reconcile this discrepancy by enforcing agreement across all spatio-temporal patches via contrastive learning. However, this indiscriminate alignment inadvertently propagates the inherent weaknesses of each module, such as noisy encoder predictions and blurred decoder boundaries. Moreover, computing dense similarities across all pairs incurs a computational cost quadratic in the total number of spatio-temporal patches, severely limiting scalability. Motivated by this, we propose Selective Synergistic Learning (SSync). Instead of exhaustive patch-to-patch alignment, SSync prevents error propagation by selectively distilling only the most reliable cues: leveraging the encoder strictly for boundary refinement and the decoder for interior denoising. This is realized via a pseudo-labeling with linear complexity, eliminating the need for quadratic spatial comparisons. Also, to prevent the reinforcement of architectural biases like slot redundancy, we introduce a transitive pseudo-label merging that consolidates overlapping slots based on spatio-temporal activation consistency. Extensive studies demonstrate that SSync improves decomposition quality and serves as a versatile, plug-and-play module while also exhibiting exceptional robustness to slot configurations. Code is available at this http URL.

---


### 183. [Participatory Design for Assistive Mobility in Indian Homes, Grounded in Lived Experience](https://arxiv.org/abs/2606.15528)

**<font color=#1a73e8>作者：</font>** Jyoti Rautela, Abinash Kumar Swain, Madhan kumar Vasudevan  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Assistive mobility devices support independence for people with lower-limb disabilities, yet many are designed and evaluated in clinical or controlled environments. In Indian households, narrow spaces and dense furniture often make assistive devices difficult to use indoors, leading people to rely on improvised movements or support from family members and caregivers. In this work, we explore domestic mobility through a participatory and co-speculative design approach, focusing on how people with lower-limb disabilities navigate and maneuver within their homes. We conducted a series of semi-structured interviews and bespoke booklet-based participatory workshops with 22 participants with lower-limb impairments. To support reflection and discussion, we designed bilingual bespoke booklets grounded in domestic design frictions, using images and scenarios to encourage storytelling, critique, and speculation. Our findings reveal mobility challenges that differ significantly from those typically observed in clinical contexts. Rather than yielding a fixed set of design solutions, the study contributes situated insights into domestic mobility frictions, participant articulation, and the limits of speculative participation in this context.

---


### 184. [Track2View: 4D-Consistent Camera-Controlled Video Generation via Paired 3D Point Tracks](https://arxiv.org/abs/2606.15534)

**<font color=#1a73e8>作者：</font>** Feng Qiao, Zhaochong An, Zhexiao Xiong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Re-rendering an existing video from a novel camera viewpoint requires the output to follow the prescribed camera trajectory while preserving the appearance and dynamics of the original scene across every frame. Existing methods rely on per-frame pose embeddings, noisy point-cloud renderings, or implicit learned correspondences, none of which provides an explicit, temporally continuous link between source and target pixels. We propose Track2View, which conditions a video diffusion transformer on paired 3D point tracks: sparse trajectories of scene points projected into both the source and target camera views. These tracks provide explicit spatiotemporal correspondences that are temporally continuous by construction, encoding what content should appear where and when. At the core of Track2View is a dual-view track conditioner that transfers visual context from source to target view through parameter-free geometric operations and learned temporal aggregation, ensuring generalization to arbitrary camera trajectories without memorizing specific motions. We further introduce a data curation pipeline that extracts one-to-one track correspondences by running a 3D point tracker on temporally concatenated multi-camera view pairs. On a 400-video benchmark spanning static and dynamic scenes, Track2View achieves state-of-the-art results across visual quality, view synchronization, and camera accuracy, reducing rotation error by 30-65% and translation error by 61-72% relative to leading baselines. Project page is available at this https URL: this https URL

---


### 185. [Multi-tier Differential Private Query Release](https://arxiv.org/abs/2606.15543)

**<font color=#1a73e8>作者：</font>** Shaowei Wang, Jinn Li, Yun Peng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Answering statistical queries over sensitive data under differential privacy (DP) is a common task in many settings, including databases, mobile computing, and data markets. In these scenarios, multiple analysts may issue the same query, while receiving answers generated under different privacy budgets due to differences in trust levels or willingness to pay. Existing approaches for such multi-tier DP queries either incur excessive cumulative privacy loss or suffer from suboptimal utility. In this paper, we propose a framework for multi-tier DP query release that simultaneously bound the cumulative privacy loss by the maximum privacy budget among all queries and achieve optimal utility comparable to that of single-tier mechanisms. Our framework applies to different classes of DP mechanisms. For noise-adding mechanisms (e.g., count queries with the two-sided Geometric mechanism in the curator model), we develop a general solution based on the characteristic functions of noise distributions. For other mechanisms (e.g., count queries under the local DP model with the Subset mechanism), we design mechanism-specific primitives for budget transformation and introduce a template-based strategy that attains optimal utility across different privacy regimes. Experimental results demonstrate the effectiveness of our framework.

---


### 186. [EcoBin: A Two-Stage Deep Convolutional Neural Network for Contamination-Aware Waste Classification](https://arxiv.org/abs/2606.15547)

**<font color=#1a73e8>作者：</font>** Raghav Senthil Kumar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Waste classification models have become highly accurate at sorting waste, often exceeding 95% on benchmark datasets. However, these models fail to account for contamination in recyclable waste. We present EcoBin, a two-stage deep convolutional neural network that classifies household waste by its disposal pathway and that explicitly accounts for contamination. The first stage is a base waste classifier built on an EfficientNetV2-S backbone that assigns each of the thirty waste categories in our dataset to one of four disposal pathways. The second stage is a contamination classifier that inspects any item routed toward recycling and overrides the decision to garbage when contamination is detected. Because no public dataset of contaminated recyclables exists, we synthesize one by segmenting images of clean recyclable objects with a U2-Net model and compositing realistic contamination textures onto their surfaces. The first stage achieves 87.42% test accuracy and a 96.13% pathway-adjusted accuracy. Meanwhile, the contamination stage distinguishes clean from contaminated items with a 0.99 ROC-AUC. On a test set of contaminated recyclables, the complete pipeline routes 24 of 25 items correctly, compared with only 1 of 25 for the base classifier alone. A McNemar's test confirms that the improvement contributed by the contamination stage is statistically significant (p < 0.001).

---


### 187. [CmdNeedle: Measuring the Incompleteness of Command Denylists for AI Agents](https://arxiv.org/abs/2606.15549)

**<font color=#1a73e8>作者：</font>** Chuyang Chen, Zhiqiang Lin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The adoption of AI agents is increasing rapidly. Terminal AI agents, i.e., AI agents that run in terminal environments, are a widely used type of AI agents. Terminal AI agents rely heavily on shell command execution to interact with the host systems. They adopt a three-list command-gating mechanism to mitigate security risks introduced by command execution, with denylists serving as the load-bearing component. However, modern operating systems often ship a large, ever-expanding set of shell commands with complex functionalities. Our observation is that even a built-in denylist of Claude Code, well-maintained by its developers, can overlook bypass commands that invalidate its effectiveness. Such negligence leads to fragile command denylists that cannot even block operations that practitioners expect them to block.
This paper presents the first systematic characterization of command denylist fragility in terminal AI agents. The paper formalizes the command denylist fragility problem and proposes an LLM-driven pipeline, CmdNeedle, to detect such fragility. It prompts the LLM to propose possible bypasses and iteratively repairs them using feedback from a validator that executes them in a sandbox. In the evaluation, we applied CmdNeedle to 1,709 real-world command denylists (containing 13,332 denylist rules) collected from GitHub. The evaluation shows several key findings, including that 69.0--98.6% of the denylists are fragile, that this fragility occurs consistently across projects and agents, and the validity of several possible root causes for this fragility. Our pipeline and findings will hopefully facilitate future research and practice regarding the command denylists used by AI agents.

---


### 188. [A Bifurcation Theory Framework for Gradient Descent on the Edge of Stability](https://arxiv.org/abs/2606.15551)

**<font color=#1a73e8>作者：</font>** Eric Gan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Edge of Stability (EoS) phenomenon, where gradient descent operates with sharpness exceeding the classical convergence threshold yet the loss decreases over long timescales, is ubiquitous in modern deep learning but remains poorly understood in realistic settings. Prior rigorous analyses have been largely confined to scalar or low-dimensional losses with specific structural forms. In this work, we develop a bifurcation theory framework for gradient descent on the edge of stability that applies directly to overparameterized neural networks. By decomposing the training dynamics into components normal and tangent to the manifold of minimizers, we show that stable EoS training arises from a flip bifurcation in the normal direction, governed by the sign of the first Lyapunov coefficient, while the tangent dynamics drift toward regions of decreasing sharpness. Under mild spectral and geometric assumptions on the loss landscape, we prove convergence to the minimizing manifold when training at the EoS threshold. As a corollary, we recover and unify prior results: we show that the product-stability condition of Gan (2026) is an instance of our framework.

---


### 189. [Distilling Drifting Transformers with Representation Autoencoders](https://arxiv.org/abs/2606.15553)

**<font color=#1a73e8>作者：</font>** Jiawei Zhang, Mengfei Xia, Gen Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Representation Autoencoders (RAEs) have improved diffusion and flow models by semantically richer latent space owing to the strongly label-wise clustered DINO features in the pretrained encoders. Yet in the distillation stage, the severe anisotropy and large curvatures caused by the rich semantic representations would hinder the convergence and performance, making the trajectory-based distillation unstable. In this work, we argue that the RAE latent space is compatible with distillation via the newly proposed Drifting Models. We first quantitatively study the curvatures and isotropy statistics across different autoencoders, and theoretically reveal that Drifting Model itself is highly likely to fail on extremely scattered spaces like reconstruction-based VAEs. These motivate us to apply the drifting paradigm directly to representation autoencoders. Our proposed method, Drift-RAE, distills pretrained flow models in RAE latent spaces using Drifting, together with insightful modifications that improve training stability by thereotically aligning drifting fields with other frameworks. Regarding the experimental evidences, we achieve 1.77 FID on ImageNet 256 dataset using only 10k distillation steps, surpassing state-of-the-art RAE distillation methods and appearing comparative with the original Drifting Model without requiring an auxiliary MAE feature extractor. The code will be made publicly available.

---


### 190. [RaLMPH: Reliability-aware Learning for Multi-Pathologist Harmonization in Whole-Slide Image Classification](https://arxiv.org/abs/2606.15554)

**<font color=#1a73e8>作者：</font>** Sungrae Hong, Jiwon Jeong, Soeun Cheon 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multiple Instance Learning (MIL) is a standard paradigm for Whole-Slide Image (WSI) analysis and has achieved strong results in computational pathology. However, most MIL pipelines assume a single "gold" label per slide, which conflicts with clinical practice where substantial inter-pathologist variability is common. Existing multi-annotator learning and label-refinement methods typically estimate global annotator reliability or rely on single-instance assumptions, making them poorly suited to MIL and to localized diagnostic contexts where experts disagree. We propose RaLMPH (Reliability-aware Learning for Multi-Pathologist Harmonization), a MIL-based label reconciliation framework for WSIs annotated by multiple pathologists. RaLMPH introduces a reliability field that jointly models (i) local neighborhood structure in WSI feature space and (ii) expert uncertainty (entropy), enabling per-sample identification of trustworthy reference neighborhoods. Leveraging this field, RaLMPH performs sample-wise local annotator ranking to select reliable opinions per slide and applies an adaptive gating mechanism to fuse labels conditioned on local reliability. Experiments on a clinical WSI dataset with labels from six pathologists, as well as controlled simulated benchmarks, show that RaLMPH consistently outperforms existing approaches. Further analyses clarify how our reliability-aware mechanism improves label reconciliation and downstream MIL performance.

---


### 191. [Minimal Oversight: Uncertainty-Aware Governance for Delegated AI Systems](https://arxiv.org/abs/2606.15563)

**<font color=#1a73e8>作者：</font>** Carlos R. B. Azevedo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI systems increasingly delegate decisions to specialized models, evaluators, tools, and supervisory controllers. The central AI problem is no longer only model accuracy, but uncertainty-aware governance: how much autonomy to grant, which evidence should calibrate trust, what performance ceiling a delegated AI system can sustain, and when human intervention becomes necessary. We propose the Minimum Sufficient Oversight Principle (MSO), a variational principle for principled autonomy delegation: minimize governance burden on the Fisher information manifold subject to a delivery constraint. The resulting Euler-Lagrange solution yields a water-filling allocation of governed delegation across the task space. Building on a revealed-action governed delegation channel model, we prove a capacity theorem for stationary symbolwise review policies, derive a local first-order approximation relating workflow complexity to quality degradation, and give a drift-dominated autonomy-time scaling law linking intervention timing to effective capacity, complexity, and drift. Within this framework, masking appears as a structural AI-governance pathology: corrected performance can hide the competence signal needed to calibrate trust. Synthetic simulations and a semi-real reconstructed workflow support design prescriptions including upstream-first correction, sensitivity-based intervention, and explicit feasibility checks before autonomy is expanded. The result is a computable framework for uncertainty, planning, and oversight in delegated AI systems. A companion Python package is available at this https URL.

---


### 192. [A Decision-Theoretic View of Test-Time Training: When, How Far, and Which Directions to Adapt](https://arxiv.org/abs/2606.15569)

**<font color=#1a73e8>作者：</font>** Tomoya Wakayama  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time training (TTT) adapts a pretrained model to each prompt via parameter updates, improving accuracy under pretraining-to-test distribution shifts. Yet, its performance often suffers from instability and sensitivity to hyperparameters such as update steps and subspace. We explain this behavior through a decision-theoretic lens, treating TTT as implicit Bayesian inference in the kernel regime. Under a Gaussian process benchmark, we show that TTT reduces prediction error when updates are spectrally matched to the prompt's signal-to-noise ratio and aligned with query-relevant eigen-directions. This perspective underpins the following results: (1) we show when fixed update steps and subspaces fail under distribution shifts, motivating adaptive strategies; (2) we prove that selecting update steps via prompt evidence admits a PAC-Bayes guarantee against overfitting; and (3) we characterize the Bayes-optimal update subspace under a linear-Gaussian correction model, yielding a scoring rule for selecting Transformer blocks and heads. Our theory helps explain the empirical instability of TTT, taking a step toward principled guidance for when, how far, and which directions to adapt.

---


### 193. [An Extensive Benchmark for Single-round and Multi-round Instruction-based Image Editing](https://arxiv.org/abs/2606.15570)

**<font color=#1a73e8>作者：</font>** Yiwei Ma, Ke Ye, Weihuang Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In recent years, there have been notable advancements in the area of instruction-based image editing (IIE), which focuses on the automatic alteration of input images using a model. Nevertheless, assessing the effectiveness of these editing models poses a considerable challenge due to the intricate nature of instructions and the wide variety of edits. To tackle this problem, one urgent task in this domain is the development of a robust evaluation framework that can precisely gauge the quality of editing outcomes and offer valuable benchmarks to guide future improvements. To address this challenge, we present a comprehensive evaluation benchmark named I2EBench2.0, designed for single-round and multi-round assessment of IIE models. I2EBench2.0 has four key features: 1) Evaluation Across Single and Multi-rounds: I2EBench2.0 simultaneously evaluates both single-round and multi-round instruction-based edits, assessing the precision and consistency of the edits. 2) Extensive Evaluation Criteria: I2EBench2.0 encompasses a broad range of criteria, evaluating both high-level and low-level aspects of each IIE model. Specifically, it incorporates 16 dimensions for single-round evaluations and 7 for multi-round evaluations. 3) Alignment with Human Judgment: To ensure our benchmark aligns with human evaluation, we conducted a comprehensive user study for each criterion. 4) Research-driven Insights: By analyzing the strengths and weaknesses of current IIE models across all 16 single-round and 7 multi-round dimensions, we provide critical insights aimed at directing future research in this area. We tested eight recently developed IIE models using I2EBench2.0 and derived academic insights through meticulous comparison and analysis. The related code, dataset, and images generated by all IIE models are available on GitHub: this https URL.

---


### 194. [Toward the Whole Picture: Accumulative Fingerprint Mapping and Reconstruction for Small-Area Mobile Sensors](https://arxiv.org/abs/2606.15574)

**<font color=#1a73e8>作者：</font>** Xiongjun Guan, Jianjiang Feng, Jie Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Small-area fingerprint sensing on mobile devices creates a fundamental mismatch between acquisition and recognition: each touch captures only a tiny, pose-varying local patch, while reliable biometric matching ultimately requires a stable and sufficiently complete fingerprint representation. Existing pipelines largely cope with this mismatch by treating repeated touches as independent partial templates, which leads to repeated registration, repeated matching, and no guarantee of adequate global coverage. In this paper, we advocate a different formulation, namely \emph{accumulative fingerprint mapping and reconstruction} for small-area mobile sensing. Rather than matching every partial patch separately, the proposed perspective converts a sequence of local observations into a unified fingerprint state that is progressively refined as new touches arrive and can be matched only once after consolidation. As a concrete baseline, we present a classical pipeline that performs patch-wise structural feature extraction, feature-level registration and fusion, fingerprint map construction, and phase-based ridge reconstruction. More importantly, we position this baseline within a broader mobile fingerprint framework that integrates structured token learning, two-stage pose reasoning, and diffusion-based generative reconstruction. This viewpoint reframes mobile fingerprint recognition from multi-capture multi-match processing to accumulative map building, state refinement, and one-shot matching, offering a principled route toward efficient, pose-robust, and deployment-friendly biometrics for small-area mobile platforms. The baseline implementation has been publicly released at this https URL.

---


### 195. [Do we have the knowledge we need? Rethinking human-AI decision-making in corporations](https://arxiv.org/abs/2606.15575)

**<font color=#1a73e8>作者：</font>** Anne S. R. Marx, Ricardo M. Avelino, Torbjørn Netland 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Organizational knowledge is fragmented across a variety of software systems, tacit expertise, and manual documents that have traditionally been designed for human consumption. As AI systems are increasingly deployed and granted decision-making roles, they require access to this knowledge. This raises two questions: how should organizations store and maintain knowledge so that it remains accessible to both humans and future AI systems, and how should agency be allocated between humans and AI across tasks with different risks and levels of uncertainty? In this position paper, we describe how organizational knowledge evolves and contribute a framework that maps task attributes and knowledge availability to recommended agency allocations and control mechanisms. We illustrate the applicability of the framework on two different manufacturing tasks: a routine operation (visual quality inspection) and a one-off strategic decision (factory location), and conclude with opportunities for future research.

---


### 196. [Process-Oriented Evaluation of AI-Assisted Scientific Writing](https://arxiv.org/abs/2606.15583)

**<font color=#1a73e8>作者：</font>** Patrick Queiroz Da Silva, Sanchaita Hazra, Doeun Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Bad writing hinders the publication of science. The role of artificial intelligence (AI) in generating and editing scientific texts remains unsettled. Abstracts serve as the critical gateway to scientific manuscripts, often shaping readers' interest. We inspect how individuals revise AI-generated abstracts compared to human-authored abstracts when incentivized to communicate scientific content. Using 869 keystroke-level edit logs with 240k total edits, we construct behavioral labels and measure linguistic properties of edit bursts to investigate the edit trajectories. AI abstracts exhibit higher sentence-level agency, whereas human-authored abstracts outperform in global coherence, even with edits. Experts engage in stigmatic behavior, switching their strategy from predominantly restructuring to substitution when AI source is disclosed. Language Models (LMs) improve edit outcomes through a mix of local and global features, but still actively struggle with global coherence. Both humans and LMs often target the weakest sections of abstracts, but fail to improve stronger areas. Our large-scale process-oriented evaluation highlights the perks and pitfalls of both human and LM editing processes as machine-generated texts emerge in scientific communication.

---


### 197. [Is Code Better Than Language for Algorithmic Reasoning](https://arxiv.org/abs/2606.15589)

**<font color=#1a73e8>作者：</font>** Terry Tong, Yu Feng, Surbhi Goel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> For tool-augmented language models, comparing natural-language reasoning with code-execution pipelines is difficult because the comparison changes both the intermediate representation and the execution mechanism. We separate these factors with an intermediate intervention: the model expresses its reasoning as executable code, and the language model simulates that code in context to produce an answer. On a 40-task verifiable algorithmic benchmark, deterministic code execution outperforms natural-language reasoning by +31.6pp. We observe that the intermediate intervention is not meaningfully different from natural-language reasoning (+0.15pp). These results suggest that, in our evaluated setting, changing the intermediate representation alone does not explain the tool-use advantage, providing evidence for the performance gains requiring reliable external execution. We formalize this intuition with a simple statistical decision-theoretic model that characterizes when execution dominates end-to-end risk in our disentangled trace-generation/execution regime. We validate our theory using a reconstruction intervention that leverages a proxy language model to infer natural-language reasoning traces from code representations, recovering performance comparable to the original natural-language reasoning pipeline. All experiments are at this https URL.

---


### 198. [Unlocking Diffusion Hierarchies: Adaptive Timestep Selection for Zero-Shot Segmentation](https://arxiv.org/abs/2606.15590)

**<font color=#1a73e8>作者：</font>** Ramin Nakhli, Mahesh Ramachandran, Luca Ballan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot segmentation has recently shown notable improvement by leveraging the rich visual priors in large-scale text-to-image diffusion models, such as Stable Diffusion. However, current diffusion-based methods often face limitations due to the trade-off between spatial resolution and contextual information, as well as their reliance on a single static timestep for feature extraction. To overcome these challenges, our work introduces two key advancements. First, our Contextual Similarity Maps fuse high-resolution attention maps with rich U-Net encoder features, providing both fine-grained and robust per-pixel representations. Second, we identify an emergent hierarchical semantic progression within the denoising process of various diffusion models: representations transition from part-level abstractions at earlier timesteps to object-level abstractions at later stages. Leveraging this insight, we introduce a mechanism to adaptively select the optimal timestep for each pixel. Extensive experiments demonstrate that our method consistently outperforms existing zero-shot segmentation baselines, validating the efficacy of combining contextual features with dynamic, hierarchical timestep selection.

---


### 199. [DenseControl: Instance-Level Controllable Synthesis of Dense Crowd Image](https://arxiv.org/abs/2606.15592)

**<font color=#1a73e8>作者：</font>** Juncheng Wang, Lei Shang, Wang Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we introduce DenseControl, a novel pipeline for generating dense crowd images. Specifically, DenseControl meticulously positions and sizes each generated instance to align precisely with the predefined coordinates and scales. Based on this, we further allow for control over the background, style, and attributes of instances. The motivation behind DenseControl stems from the observation of two main challenges in synthesizing crowd images: controlling signal embedding and maintaining topological integrity when imparting instance scale guidance. To address these, we first introduce the Isolated Object Embedding (IOE) map, a novel representation that facilitates spatial location control while mitigating the difficulties associated with learning projections for model. Secondly, we propose an Implicit Scale Embedding (ISE) strategy that seamlessly integrates with the IOE map to encode precise scale information. To further enhance the efficacy of combining ISE with the IOE map, we incorporate a Position Shortcut mechanism that enhances cross-attention to alleviate projection challenges. We evaluate DenseControl through two lenses: synthesis quality and applicability in latent applications. Experiments across different control conditions demonstrate DenseControl achieves state-of-the-art results in dense crowd image synthesis. Furthermore, we showcase applications in augmenting crowd analysis under data scarcity, transfer learning, and weather generalization scenes, to highlight the practical utility of DenseControl. The codebase will be released.

---


### 200. [SCAN: A Decision-Making Framework for Effective Task Allocation with Generative AI](https://arxiv.org/abs/2606.15601)

**<font color=#1a73e8>作者：</font>** Fendi Tsim, Alina Gutoreva  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We introduce SCAN -- a human-centric decision-making framework to facilitate learners for effective task allocation with Generative Artificial Intelligence (GenAI) based on Vygotsky's Zone of Proximal Development and Metacognition. In SCAN, we systematize and formalize AI-human interaction by introducing a task-identification approach with four "sub-zones": Substitute, Complement, Aid, and Non-negotiable. After describing the four sub-zones, we demonstrate how SCAN framework can be applied for knowledge workers in the workplace and students in education to metacognitively "scan" their use of Generative AI. We then discuss how such framework can be related to cognitive load theory, cognitive offloading, sycophancy, three decision-making modes in human-AI interactions (automation, augmentation, and collaboration), future of work such as upskilling and deskilling, and how it accounts for both human-human and human-AI learning. We propose that SCAN offers a great starting point before discussing whether GenAI complements or replaces our abilities when completing a task, with a general objective of sustaining lifelong learning, and a specific goal of reaching hybrid intelligence.

---


> [!TIP]
> 当前位于：**151-200**（第 4/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-509](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
