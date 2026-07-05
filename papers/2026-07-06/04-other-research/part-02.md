# 📦 其他研究 | 2026年07月06日

> 本类共 **266** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-266](./part-06.md)

---

### 51. [Towards Learning Representations of Policies in Two-Player Zero-Sum Imperfect-Information Games](https://arxiv.org/abs/2607.01498)

**<font color=#1a73e8>作者：</font>** Kevin Wang, Kevin Yang, Arjun Prakash 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate the problem of learning useful policy representations (embeddings) in two-player zero-sum imperfect-information games. We make three contributions: First, we introduce methods of creating datasets of policies for a given game. Second, we propose methods to learn policy representations. Third, we introduce downstream tasks to evaluate the effectiveness of such representations.
We evaluate each dataset method, embedding method, and downstream task on Kuhn and Leduc Poker. Although our methods are very basic, we demonstrate that useful behavioral representations are present in the learned embeddings. To our knowledge, this work is among the first to systematically compare self-supervised learning techniques for learning policy representations in games. Our code is available at this https URL for others to extend.

---


### 52. [Anti-Prompt: Image Protection against Text-Guided Image-to-Video Generation](https://arxiv.org/abs/2607.01499)

**<font color=#1a73e8>作者：</font>** Yeonghwan Song, Chanhui Lee, Jinsoo Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Image-to-Video generation allow a single image to be animated into a convincing video under text guidance, raising serious copyright and privacy risks. We propose Anti-Prompt, an image protection approach that injects imperceptible perturbations into an image, inducing visible inconsistencies and structural failures in text-guided I2V generation. Our method is motivated by a simple empirical observation. When text guidance is removed from modern I2V models, generation quality degrades markedly, not only in motion realism but also in subject preservation, structural coherence, and temporal consistency. Building on this insight, Anti-Prompt exploits the model reliance on textual guidance by attenuating text-conditioned interactions during denoising while strengthening visual-only pathways. To further systematically evaluate protection effectiveness, we introduce a Video-LLM-assisted evaluation protocol that provides interpretable, frame-grounded analyses of generation artifacts and inconsistencies. Experiments on two representative I2V architectures demonstrate that our method achieves strong protection performance while improving efficiency and cross-model transferability.

---


### 53. [From Monolingual to Multilingual: Evaluating Mamba for ASR in South African Languages](https://arxiv.org/abs/2607.01502)

**<font color=#1a73e8>作者：</font>** Jesujoba O. Alabi, Julian Herreilers, Badr M. Abdullah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in automatic speech recognition (ASR) have explored different sequence models, including Conformer-based models and newer state space models such as Mamba. Although prior work has evaluated these architectures in multiple languages, their effectiveness in African languages remains underexplored. In this work, we evaluate Mamba for ASR on seven South African languages. In monolingual experiments, each model is trained on 50 hours of speech per language, and we compare Mamba to a Conformer baseline of similar parameter scale. Mamba achieves similar recognition accuracy to Conformer while using fewer computational resources and training faster. We further evaluate generalization in this setting and find that both models struggle to generalize to speech that is much longer than what they were trained on. We then study multilingual ASR using Mamba models, where the baseline is pooling all languages together. On top of this, we tested three extensions: training with language-family information by adding both language and language-family embeddings as biases to the downsampled acoustic representations, and multitask learning with a CTC ASR objective and a language identification (LID) head. We find that multilingual training consistently improves performance over monolingual training. However, adding explicit language information does not improve in-domain performance but does improve cross-corpus robustness. We conducted ablation studies in low-resource multilingual settings using 5-hour and 10-hour per-language training data, where we observed gains from using language embeddings and further demonstrated that removing or altering them hurt model performance. Lastly, we analysed these embeddings and find that they do not capture linguistic similarity in a typological sense, but instead act as task-specific control vectors.

---


### 54. [Disentangling Pictorial Cue Understanding from Language Bias in VLMs via Depth Ordering Task](https://arxiv.org/abs/2607.01503)

**<font color=#1a73e8>作者：</font>** Yiqian Liu, Iuliia Kotseruba, John K. Tsotsos  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we study depth perception of vision-language models (VLMs) to isolate the effects of pictorial depth cues and disentangle vision and language influences on model performance. To this end, we combine depth-ordering and odd-one-out psychophysical tasks: the VLMs are presented with images where one object is at different depth relative to other, otherwise identical, objects, and must determine whether the odd-one-out target is closer or farther to the observer. To create stimuli, we generate 2D views from simulated and real 3D scenes while controlling the presence of individual pictorial depth cues, enabling a fine-grained analysis of cue-level contributions. Language effects are examined by varying referring expression clarity. We also introduce a novel metric to quantify vision-vs-language sensitivities. Applying this methodology, we create the Odd-One-Out Depth (O3-D) dataset with 37K real and synthetic images and 147K image-question pairs. Evaluation of 12 open-source and commercial models on O3-D shows under-utilization of depth cues and depth-ordering accuracies between 47% and 56%, with no model above chance level. At the same time, our metric reveals strong linguistic bias in the answers. Neither chain-of-thought (CoT) nor in-context learning (ICL) significantly improves performance, suggesting that static image data alone may be insufficient for depth understanding. All code, the image generation pipeline, and the O3-D dataset are publicly released at this https URL.

---


### 55. [Revisiting Chain-of-Thought Reasoning under Limited Supervision: Semi-supervised Chain-of-Thought Learning](https://arxiv.org/abs/2607.01511)

**<font color=#1a73e8>作者：</font>** Hongyang He, Jiuming Liu, Victor Sanchez  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) reasoning has emerged as an effective approach for activating latent reasoning capabilities in large language models. However, most existing CoT methods use reasoning chains mainly as inference-time prompts, while the generated reasoning traces are rarely reused as semi-supervised learning signals. In this report, we define \textbf{Semi-supervised Chain-of-Thought Learning} and propose \textbf{Semi-CoT}, a simple framework that uses unlabeled questions to construct pseudo reasoning supervision. Semi-CoT samples multiple pseudo-CoTs for each unlabeled question, estimates answer-level semantic entropy, and selects low-entropy reasoning chains as reliable pseudo-CoT demonstrations. This extends the self-training view of CoT from inference-time refinement to semi-supervised pseudo-supervision. Pilot experiments on AQuA, SVAMP, GSM8K, and MultiArith show that the entropy gate selects high-precision pseudo-CoTs, with pseudo-answer precision ranging from $91.36\%$ to $100\%$. Semi-CoT also gives small gains on SVAMP and GSM8K, while AQuA shows negative transfer and MultiArith reaches a ceiling. These results suggest that unlabeled questions can provide reliable pseudo reasoning signals, but their effective use still requires stronger demonstration selection or student training.

---


### 56. [Parameter Golf: What Really Works?](https://arxiv.org/abs/2607.01517)

**<font color=#1a73e8>作者：</font>** Prashanna Mani Paudel, Shivanand Venkanna Sheshappanavar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How far can a language model improve under a strict artifact budget? Parameter Golf posed this question as an open community challenge in which participants trained the best language model, with the complete artifact (training code + compressed weights) required to fit within 16 MB and be trained in under ten minutes on 8xH100 SXM GPUs. Quality was measured in bits-per-byte (BPB), the average number of bits required to encode each byte of unseen text. We analyze 2,037 pull requests and 1,430 clean scored submissions from the contest, build a taxonomy of 84 optimization techniques, and measure each technique's contribution to BPB. The verified leaderboard score dropped from 1.2244 to 1.058 BPB across three phases -- a 13.6% reduction, despite individual techniques rarely improving BPB by more than 1%. We show that most gains in techniques shrink across competitive submissions, isolating the few methods that improve performance across stacks.

---


### 57. [The risk of KV cache compression](https://arxiv.org/abs/2607.01520)

**<font color=#1a73e8>作者：</font>** Lukas Haverbeck, Carmen Amo Alonso, Andres Felipe Posada-Moreno 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer inference on long sequences is expensive because softmax attention repeatedly reads from a large KV cache. The prevalent approach to this bottleneck is KV cache compression, which replaces the full cache with a compact summary. Despite its practical importance, the design of such summaries is largely driven by empirical experimentation. On the theoretical side, existing results show that KV cache compression can be impossible in the worst case, but offer little systematic guidance for designing algorithms in regimes where accurate compression is possible. We bridge this gap by characterizing the minimax risk of KV cache compression in terms of the intrinsic compressibility of a cache, revealing when and how accurate compression is possible. These results yield novel design principles for KV cache compression under causal masking that map efficiently to prefill and autoregressive decoding while achieving minimax-optimal risk. We instantiate these principles in a practical algorithm and report promising performance on LongBench in targeted experiments. Overall, our results provide a principled avenue for practical KV cache compression with theoretical guarantees.

---


### 58. [Multi-Head Recurrent Memory Agents](https://arxiv.org/abs/2607.01523)

**<font color=#1a73e8>作者：</font>** Jiatong Li, Samuel Yeh, Sharon Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recurrent memory agents extend LLMs to arbitrarily long contexts by iteratively consolidating input into a fixed-size memory window. Despite their scalability, these agents exhibit a well-documented reliability problem: end-to-end performance degrades systematically as context length grows. We diagnose this failure by decomposing performance into two factors--memory capture and memory retention--and quantitatively confirm that retention is the dominant bottleneck. Retention collapses because existing designs maintain memory as a monolithic text block, forcing every update to risk overwriting previously retained content. Motivated by this diagnosis, we propose Multi-Head Recurrent Memory (MHM), a general, training-free framework that partitions memory into independent heads governed by a stage-wise select-then-update strategy. At each step, exactly one head is selected for update while the remaining heads are structurally shielded from overwriting, shifting the burden of retention from model behavior to architectural design. As a lightweight instantiation, we introduce Least-Recently-Updated MHM (MHM-LRU), which guarantees uniform head utilization with zero additional token overhead. Extensive experiments on long-context benchmarks show that MHM-LRU substantially improves both retention and end-to-end accuracy across the 100K--1M token range, where baselines degrade sharply. On RULER-HQA at 896K tokens, MHM-LRU improves the memory retention rate from less than 30% to 73.96%. These gains generalize across model families, scales, and task types, positioning architectural optimization as a practical and cost-efficient path toward reliable long-context recurrent memory.

---


### 59. [LIB-TRAP: Standard Cell Library Hardware Trojan Risk Assessment and Prevention](https://arxiv.org/abs/2607.01526)

**<font color=#1a73e8>作者：</font>** Harish Kumar Dharavath, Md Muhtasim Alam Chowdhury, Rozhin Yasaei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vulnerabilities inherent to the fabless semiconductor manufacturing model have significantly increased the risk of malicious Hardware Trojan (HT) insertion, posing severe threats to hardware security. Several HT mitigation and detection strategies have been developed, and existing works explore the insertion of HTs in the space between standard cells in an integrated circuit. However, there is a lack of research into the vulnerabilities posed by the building blocks of most digital designs on the market today, the standard cells. This work investigates a novel threat model in which standard cells are considered untrusted. Our proposed threat model provides the design house with a tampered standard cell library. The intended netlist is synthesized and implemented using the tampered library. During fabrication, a nefarious foundry replaces the library's deactivated HT cells with activated counterparts. Using open-source and industry-standard Electronic Design Automation (EDA) tools, existing standard cell libraries, Saed32nm and Sky130nm, are converted into malicious libraries capable of masking the presence of arbitrary HTs from IC designers. The malicious library is then applied and characterized in multiple standard benchmark designs. To demonstrate the efficacy and stealthiness of this standard cell-based attack vector, three benchmark circuits, an AES-128 encryption core, an Ethernet controller, and a WISHBONE DMA engine, were synthesized using both clean and Trojan-infected libraries across Synopsys 32nm and SkyWater 130nm technologies. Design-level features, including total cell count, total area, dynamic power consumption, and static power, were extracted from these synthesized circuits to serve as inputs for binary classification

---


### 60. [Wind-Aware Reinforcement Learning Control of a Small Quadrotor Using Learned Onboard Wind Estimation in Simulated Atmospheric Turbulence](https://arxiv.org/abs/2607.01528)

**<font color=#1a73e8>作者：</font>** Abdullah Al Tasim, Wei Sun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Small multirotor aircraft are increasingly tasked with operations in the atmospheric boundary layer, where turbulent winds comparable to the vehicle's airspeed degrade trajectory tracking and can defeat conventional feedback control. This work illustrates a two-stage learning pipeline that first estimates the local wind from onboard kinematics and dynamics and then exploits that estimate inside a reinforcement learning (RL) flight controller. The wind estimator, an attention-augmented gated recurrent network trained on thousands of simulated flights through von Karman turbulence with power-law shear and veer, recovers the horizontal wind vector with a per-flight root-mean-square error of 0.40 m/s and a direction error of 3.2 degrees on unseen wind regimes, an accuracy near the floor imposed by unresolved turbulence, and generalizes to vertical ascent profiles with a skill score of 0.861 over a constant-wind reference. A proximal policy optimization controller receiving the frozen estimator's output reduces horizontal trajectory tracking error by 48% relative to a wind-blind proportional-derivative baseline across mean winds of 4 m/s to 12 m/s, winning on 100% of evaluation episodes. A three-way ablation decomposes this improvement into a kinematic component, available without wind information, and a wind-perception component; the perception share rises with wind speed, from small in light winds toward roughly half the total benefit in strong winds, consistent with the quadratic scaling of aerodynamic drag. The controller degrades gracefully on out-of-distribution winds of 13 m/s to 15 m/s, where the baseline fails catastrophically.

---


### 61. [Hidden-Shot: Towards One-Shot Task Generalization for Low-Level Vision Generalist Models](https://arxiv.org/abs/2607.01535)

**<font color=#1a73e8>作者：</font>** Shao-Jun Xia, Xianzheng Ma, Zichong Meng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the intense engagement surrounding low-level vision generalist models, their effectiveness in zero/few-shot scenarios beyond learned tasks remains unverified. The primary challenge of developing an ideal generalist lies in achieving the ability to generalize from new unseen tasks, which also can be assessed by matched quantitative criteria. Existing methods have made some progress in prompt engineering but have not systematically explored this gap across a wide range of low-level visual tasks. Stimulated by the problem, we propose Hidden-Shot, an implicit prompt mechanism aimed at exploring low-level task adaptation in a vision generalist model. Specifically, the method extracts implicit visual task-based information, utilizes a global task-aware textural prompt, and selectively merges implicit information with in-task processing information to enhance one-shot capabilities in new tasks. The overall design performs direct injection in a cost-effective manner, while minimally altering the architecture of the original generalist model. Additionally, we introduce a data-driven evaluation framework termed C/U assessment to cover two basic scenarios, 3C4U (3 conventional and 4 unconventional tasks) for retraining existing models and 3C7U (3 conventional and 7 unconventional tasks) for training from scratch, as a comprehensive assessment to systematically test the generalization ability of low-level generalist models. Experiments on seven and ten datasets outperform the state-of-the-art vision generalist model, respectively verified by 3C4U and 3C7U framework. Our presented Hidden-Shot approach demonstrates superior performance on one-shot new tasks while maintaining consistent performance on existing tasks.

---


### 62. [X-LogSMask: Expand Transformer for Graph-Structured Data](https://arxiv.org/abs/2607.01553)

**<font color=#1a73e8>作者：</font>** Leyan Li, Rennong Yang, Zhenxing Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers have become general-purpose architectures, but their all-to-all self-attention is poorly matched to graph data, whose interactions are sparse, structured and multi-scale. Existing Graph Transformers address this mismatch through structural encodings, hybrid message-passing modules or learned attention constraints, often introducing additional complexity and limited interpretability. Here we introduce X-LogSMask, an explainable multi-head logarithmic structural mask that injects symmetrically normalized graph topology directly into attention logits. The logarithmic transform converts structural connectivity into a topology-aware gating signal, suppressing unsupported node interactions while preserving feature-dependent attention. By assigning different powers of the normalized adjacency matrix to different attention heads, X-LogSMask gives each head a defined structural radius and supports multi-hop information propagation within a single layer. We further show that a standard Transformer encoder can be interpreted as one-step message passing on a complete graph, motivating X-LogSMask as a topology-constrained alternative to unrestricted self-attention. Across 20 node-, edge- and graph-level benchmarks, Transformers equipped with X-LogSMask achieve state-of-the-art performance on 13 datasets and remain competitive in a lightweight one-layer configuration. These results show that simple, interpretable structural masks can make self-attention an effective graph-learning operator without changing the Transformer architecture. The code is available at this https URL.

---


### 63. [Boosting Infrared Small Target Detection via Logit-Domain Contrast and Adaptive Shape Refinement](https://arxiv.org/abs/2607.01555)

**<font color=#1a73e8>作者：</font>** Handong Zeng, Zhengeng Yang, Shuai Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared small target detection (IRSTD) remains challenging due to tiny target size, low signal-to-noise ratio, severe foreground-background imbalance, and blurred boundaries in complex scenes. Existing methods usually rely on post-activation probability-domain supervision for discrimination, where weak targets and strong clutter may produce saturated and close probabilities, limiting weak-target discrimination. Meanwhile, blurred boundaries and halo-like predictions mainly stem from thermal diffusion, tiny target scale, boundary uncertainty, and insufficient explicit contour constraints. To address these issues, we propose Adaptive-Contrastive SLSIoU (AC-SLSIoU), a plug-and-play discriminative and shape-aware loss for IRSTD. Specifically, a Logit-Domain Margin Constraint (LDMC) is introduced to enlarge the response gap between targets and informative hard negatives in the logit space, thereby enhancing weak-target discrimination. Adaptive Boundary Suppression (ABS) applies scale-aware annular penalties to refine target contours and suppress halo-like overflow responses. In addition, False-Alarm Focal Loss assigns larger weights to high-probability negative samples, further penalizing persistent high-confidence false alarms. Without introducing extra inference overhead, the proposed method can be seamlessly integrated into existing detectors and consistently improves both detection accuracy and shape quality. Extensive experiments and cross-backbone evaluations demonstrate the effectiveness, robustness, and generalization ability of the proposed method for infrared small target detection.

---


### 64. [Mind the Gap: Standard 3DGS Evaluation Primarily Measures Near-Trajectory Interpolation](https://arxiv.org/abs/2607.01556)

**<font color=#1a73e8>作者：</font>** Gaoxiang Jia, Vikram Appia  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Standard MipNeRF360-style 3D Gaussian Splatting (3DGS) evaluation holds out every N-th frame -- but these frames have trained neighbors on both sides, so the metric measures near-trajectory interpolation rather than spatial generalization. We introduce a fair matched-count protocol that isolates this effect: both arms train on the same number of images and differ only in whether the holdout is spread evenly (interpolation) or forms a contiguous spatial sector (extrapolation). Our primary finding is a large, consistent interpolation-extrapolation gap of 3~12dB -- several times the differences typically reported between competing methods. The gap is robust to training noise, is in two cases large enough to flip a method ranking under multi-seed confirmation, and -- crucially -- persists across three representation families, including a non-Gaussian volumetric neural radiance field (NeRF), so it reflects spatial coverage rather than any one representation. Diagnostically, it is dominated by a diffuse/geometry-proxy component and tracks each view's angular distance to its nearest training view, a zero-cost signal that also guides capture planning; loss-side regularization yields only marginal gains. Standard holdouts remain useful for near-trajectory rendering but should not, alone, be read as evidence of spatial generalization. Prior work notes protocol sensitivity; ours is, to our knowledge, the first to combine matched-count paired holdout, cross-representation quantification, and a diagnostic analysis Table 1. We describe a spatial-holdout benchmark toolkit with standardized splits and baselines for 16 scenes, which we are preparing for public release.

---


### 65. [Scaling Trends for Lie Detector Oversight in Preference Learning](https://arxiv.org/abs/2607.01567)

**<font color=#1a73e8>作者：</font>** Oskar J. Hollinsworth, Ann-Kathrin Dombrowski, Sam Adam-Day 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deceptive behavior in LLMs is costly to monitor and prevent, motivating approaches such as Scalable Oversight via Lie Detectors (SOLiD) (Cundy & Gleave, 2025), which uses lie detectors to identify responses for review by high-cost labelers. In this paper, we scale SOLiD to larger models and evaluate it in more diverse and realistic preference-learning settings. We find favorable scaling: undetected deception drops from 34% for 1B-parameter models to 14% for 405B-parameter models at a detector true positive rate of 99%, and expensive human labelers can be removed entirely from the fine-tuning phase without a statistically significant increase in deception. However, SOLiD is sensitive to distribution shift between detector training and preference-training data, which can drive detector false positive rates to impractical levels.

---


### 66. [Geometric Signatures of Reasoning: A Spectral Perspective on Task Hardness](https://arxiv.org/abs/2607.01571)

**<font color=#1a73e8>作者：</font>** Aria Masoomi, Mahsa Bazzaz, Adel Javanmard 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) reasoning enables large language models (LLMs) to solve complex problems by generating intermediate reasoning steps. While much attention has been paid to the length and content of these reasoning chains, far less is known about their internal geometry. We study the \emph{geometry} of CoT trajectories in the hidden state space of transformer models, formalizing each reasoning chain as a discrete curve in $\mathbb{R}^d$ and characterizing it through spectral, positional, and kinematic geometric functionals. We introduce the effective dimension $d_\rho$ as a measure of trajectory complexity and show theoretically that trajectories with flatter eigenvalue spectra correspond to harder tasks, as they explore more of the hidden dimensions. Lastly, we explore how kinematic features of the trajectory, mean position, positional dispersion, initial and current hidden states, mean velocity, mean speed, and speed dispersion, can be used to predict solution correctness before generation is complete, and may inform future early-stopping strategies. Experimentally, on mathematical reasoning problems from the MATH500 dataset, $d_\rho$ achieves $0.93$ AUC in distinguishing easy from hard problems, while kinematic features potentially can predict correctness from only the first $20\%$ of generated tokens. These correctness signatures transfer across questions of varying difficulty, establishing that the shape of a model's internal reasoning trajectory is a principled window into both task hardness and solution quality.

---


### 67. [MVFusion-GS: Motion-Variance Guided Temporal Attention for High-Quality Dynamic Gaussian Splatting](https://arxiv.org/abs/2607.01578)

**<font color=#1a73e8>作者：</font>** Jianwei Hu, Tingxuan Huang, Hengyu Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) enables real-time novel view synthesis for static scenes. Extending it to dynamic scenes via deformation fields has recently attracted significant attention, particularly for dynamic scene reconstructionband distractor-free. However, existing deformation networks lack explicit motion awareness: they neither capture long-term motion intensity nor exploit short-term temporal coherence, leading to inaccurate foreground deformation and pseudo-static residuals in the background. We present MVFusion-GS, a method that enhances deformation networks with two complementary motion-aware mechanisms. The Motion-Variance Guided Refinement aggregates per-Gaussian deformation statistics across time to estimate motion variance and uses it to guide dynamic-static separation during deformation prediction. The MotionFormer Temporal Attention module applies Transformer self-attention over neighboring timesteps to model local motion dependencies and improve temporal consistency. Extensive experiments on both dynamic scene reconstruction and distractor-free reconstruction benchmarks demonstrate state-of-the-art performance, showing that explicit motion awareness improves both foreground motion modeling and static background reconstruction.

---


### 68. [OrchestrXR: A Multi-Agent System for Idea-to-Prototype XR Study Authoring](https://arxiv.org/abs/2607.01588)

**<font color=#1a73e8>作者：</font>** Shuqi Liao, Chenfei Zhu, Karthik Ramani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Extended Reality (XR) has become an important interaction paradigm in Human-Computer Interaction (HCI). XR studies are used to investigate interaction, perception, and user behavior in immersive environments, and typically involve experimental tasks, 3D scenes, and interactive logic. However, turning an initial XR study idea into a runnable prototype remains fragmented across study design, scene construction, and interaction implementation. We present OrchestrXR, a multi-agent human-AI workflow for early-stage idea-to-prototype XR study authoring. Rather than treating XR study creation as one-shot generation, OrchestrXR supports a controllable workflow across study design, scene generation, and interaction generation through structured schemas, multi-agent orchestration, and interactive human-agent interfaces, producing a Unity-based prototype from a researcher's idea. A user study with 12 XR researchers suggests that OrchestrXR provides effective support for early-stage XR study authoring with strong intent preservation across stages.

---


### 69. [Made to Feel: How Designers Bring Emotions into Affective Visualization](https://arxiv.org/abs/2607.01593)

**<font color=#1a73e8>作者：</font>** Yixin Bai, Ziyi Wang, Keke Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Affective visualization is increasingly studied in visualization research, yet how designers bring emotions into their visualization work remains unexplored. This paper addresses this gap through semi-structured interviews with 15 visualization practitioners. Using hybrid thematic analysis, we identify: (1) three functions that emotions can serve for viewers (entry, engagement, outcome); (2) three facets of how designers work with emotion (data, design, audience), along with design strategies; and (3) ethical considerations in the design process. We also observe that affective intent often emerges during the design process rather than being planned from the outset, and that emotional impact arises from accumulated design choices rather than isolated visual elements. Finally, we highlight evaluation as a key challenge identified by our participants.

---


### 70. [ProWAFT: A ROMA-LPD Instance for Workload-Aware and Dynamic Fault Tolerance in FPGA-Based CNN Accelerators](https://arxiv.org/abs/2607.01602)

**<font color=#1a73e8>作者：</font>** Xinxin Chen, Haoran Qiao, Yiming Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> SRAM-based FPGAs provide an attractive platform for energy- and latency-constrained CNN inference at the network edge, yet transient faults can lead to silent errors that compromise reliability. Always-on redundancy (e.g., full TMR) improves correctness but incurs substantial performance and energy overhead, while reactive recovery may introduce unacceptable latency on the critical path. We propose \textbf{ProWAFT}, a proactive workload-aware fault-tolerance framework for FPGA-based CNN accelerators that uses partial reconfiguration to selectively apply TMR across reconfigurable partitions. ProWAFT quantifies workload criticality, models fault propagation and reconfiguration overhead, and selects configurations that minimize a composite objective over latency, energy, and reliability risk. Implemented on a Xilinx Zynq UltraScale+ ZCU104 platform with six reconfigurable regions and evaluated on a 500-task trace derived from ResNet-18, MobileNetV2, and EfficientNet-Lite under time-varying SEU injection, ProWAFT achieves lower composite cost than static TMR and reactive reconfiguration while maintaining high task success rate and near-baseline throughput with low online decision overhead.

---


### 71. [Profit-Based Counterfactual Explanations for Product Improvement: A Case Study of Manga Sales in Japan](https://arxiv.org/abs/2607.01610)

**<font color=#1a73e8>作者：</font>** Keita Kinjo, Takeshi Ebina  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Counterfactual explanation (CE) is widely used to enhance the interpretability of machine learning models and support data-driven decision-making based on model predictions. However, existing CE methods typically require two exogenously specified inputs: a desired output value (target) and a distance function that quantifies changes in explanatory variables. In regression settings, neither the validity of target specification nor the practical interpretation of the distance metric has been sufficiently addressed. Furthermore, most existing CE methods focus on altering predictions rather than optimizing a decision objective, even though real-world decision-making often requires explicit objective maximization. To address these limitations, we formulate CE as a profit maximization problem in management and marketing contexts and propose a framework termed profit-based counterfactual explanation (PBCE). PBCE eliminates the need for exogenous target specification by directly maximizing profit as the primary optimization objective. Concurrently, the distance term is reinterpreted as the cost of modifying product attributes, providing a clear and economically grounded interpretation.

---


### 72. [Evaluating Glanceable Multi-Device Family Health Tracking with Smartwatches and Home Displays](https://arxiv.org/abs/2607.01618)

**<font color=#1a73e8>作者：</font>** Lucas M. Silva, Evropi Stefanidi, Aehong Min 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> While ubiquitous computing research has explored diverse devices for personal health tracking, we know less about multi-device designs for family informatics, where health management is inherently collaborative. To understand how families adopt and perceive ubiquitous access to shared health data across contexts, we evaluated smartwatch-only, home display-only, and combined designs for tracking moods and goals, domains central to family health behavior regulation. 44 people across 12 families alternated between these designs over nine weeks. Log analysis revealed that mood tracking and goal reporting were significantly more frequent with the home display present compared to smartwatch-only use, despite an overall decline in mood tracking over time. Tracking peaked in afternoons, dropped on weekends, and occurred 2.6X more at home, with children tracking more consistently than adults across all designs. From interview analysis, we learned how family data glanceability on smartwatches supported opportunistic tracking and awareness while apart, whereas displays reminded families to self-track and collaborate during home routines including members that avoided wearables (e.g., non-participants). Multi-device redundancy accommodated diversity in routines, mobility patterns, and device preferences among members in the same family. We discuss opportunities for multi-device family informatics that accommodates different preferences through inclusive, glanceable, and adaptable ubiquitous data sharing.

---


### 73. [Spatial Support Matters: Geometry-Aware Graph Fusion for Rainfall Field Reconstruction](https://arxiv.org/abs/2607.01621)

**<font color=#1a73e8>作者：</font>** Low Jun Yu, Niramay Kachhadiya, Herath Mudiyanselage Viraj Vidura Herath 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fine-scale rainfall reconstruction is critical for urban flood modeling, but real rainfall sensing systems observe the field through incompatible spatial supports: gauges measure points, microwave links measure paths, and radar/satellite products measure gridded areas. These differences in measurement support impose geometrically distinct constraints on the rainfall field, yet existing heterogeneous graph approaches reconcile such sources in feature space, giving each its own embedding while discarding the geometry of its support. We propose a geometry-aware multi-support heterogeneous graph neural network that represents each observation according to its support type (0D point, 1D line, or 2D grid) as a distinct node layer, and fuses them through cross-support message passing into a point-support prediction layer from which the field is reconstructed. An inductive masked-node formulation decouples prediction resolution from sensing resolution, allowing the same trained model to reconstruct the field at user-defined target locations or display grids. On Singapore data, the proposed method reduces RMSE by 23.2\% over the classical interpolation baseline, inverse-distance weighting, and consistently outperforms other neural architectures such as convolutional fusion and support-agnostic heterogeneous graph baselines. A generalization study using data from Sydney, Australia lets us characterize when multi-support fusion helps: the available skill appears to depend on gauge spacing relative to the spatial correlation length of the field, so fusion delivers the largest gains where the field is under-sampled relative to its correlation length and little when it is already resolved. Code and models will be open-sourced upon paper acceptance.

---


### 74. [Multi-THuMBS: Multi-person Tracking of 3D Human Meshes Beyond Video Shots](https://arxiv.org/abs/2607.01626)

**<font color=#1a73e8>作者：</font>** Jeongwan On, Muhammad Salman Ali, Muneeb A. Khan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tracking multi-person 3D human meshes from in-the-wild videos is a highly challenging problem due to complex interactions, frequent occlusions, and severe truncation inherent in unconstrained environments. While recent approaches have improved robustness against these issues, they largely overlook the critical challenge prevalent in real-world footage: frequent shot changes. These abrupt transitions in camera viewpoints often cause existing methods to lose track of human identities and fail in reconstructing temporally coherent trajectories. Although several recent works have explored 3D human mesh tracking under shot changes, they are still limited to single-person scenarios, making them inadequate for real-world videos where multiple people interact and appear simultaneously. To address this limitation, we propose Multi-THuMBS (Multi-person Tracking of 3D Human Meshes Beyond Video Shots) that leverages a state-of-the-art 3D scene prior to reconstruct the two boundary frames in a single shared 3D space. Human meshes are then registered within the shared 3D space, maintaining per-person identity and motion consistency across shot changes. Extensive experiments demonstrate that our approach yields significant improvements in 3D human mesh recovery, camera pose estimation, and identity tracking, thereby ensuring high-fidelity motion reconstruction with consistent identity preservation across shots compared to previous state-of-the-art methods.

---


### 75. [Online Segment 3D Gaussians via Launching Virtual Drones](https://arxiv.org/abs/2607.01628)

**<font color=#1a73e8>作者：</font>** Liwei Liao, Rongjie Wang, Ronggang Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive segmentation of 3D Gaussians offers a compelling opportunity for real-time manipulation of 3D scenes, thanks to the real-time rendering capability of 3D Gaussian Splatting (3DGS). However, existing methods require a time-consuming per-scene setup - typically tens of seconds or even minutes - before interactive segmentation can begin on a raw 3DGS scene. This setup involves multi-view mask preparation, mask lifting, and feature distillation, creating a major bottleneck for online applications.
To address this limitation, we aim to completely eliminate the setup stage for interactive 3DGS segmentation while keeping the segmentation time practical (under 1 second). In this work, we present SAGO (Segment Any Gaussians Online), a novel setup-free framework for interactive 3DGS segmentation. By introducing virtual drones, our method reframes the 3D segmentation problem as an online Next-Best-View (NBV) planning task formulated within a Markov process. Extensive experiments demonstrate that SAGO can extract clean 3D assets directly from 3D Gaussians with sub-second latency, thereby enabling a broad range of downstream applications such as object manipulation and scene editing. Moreover, our method achieves over a 50x speedup compared to the previous setup-free 3DGS segmentation frameworks.

---


### 76. [DRDN: Decoupled Representation Dynamic Network for From-Scratch ViT Class-Incremental Learning](https://arxiv.org/abs/2607.01630)

**<font color=#1a73e8>作者：</font>** Bingchen Huang, Yifu Chen, Zhiling Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic expansion methods for class-incremental learning (CIL) protect task-specific knowledge by growing dedicated tokens or subnetworks, yet our analyses suggest that classification supervision alone does not sufficiently preserve task-agnostic shared backbone representations over long incremental sequences. We identify two intertwined challenges: cross-task confusion from sequential training on predominantly current-task data, which biases decision boundaries toward recent tasks; and under-optimized shared representations in the backbone that cap long-term discriminability as tasks accumulate.
We propose the Decoupled Representation Dynamic Network (DRDN), which addresses these challenges via two orthogonal mechanisms. For shared backbone representations, DRDN continuously applies masked image modeling (MIM) at every incremental step, with reconstruction gradients routed exclusively through the backbone, encouraging it to retain general visual structure beyond class-discriminative cues. For task-specific discrimination, DRDN employs hierarchical task token expansion across all transformer layers, with a modified per-task attention rule that reduces inter-task interference. We support this design with accuracy degradation analysis and cross-task confusion rate measurements.
In the from-scratch ViT CIL setting (no external pretraining), DRDN consistently improves over strong token-expansion baselines with comparable backbone scale. On CIFAR100-B0 (10 steps), DRDN achieves 77.19% average accuracy, outperforming DKT by 1.36 points and DyTox by 3.53 points, with an advantage that grows at longer incremental sequences. Multi-seed validation confirms stability (+/-0.31%). The MIM decoder is active only during training, adding no inference-time parameters or computation.

---


### 77. [Bridging 3D Gaussians and Semantic Occupancy for Comprehensive Open-Vocabulary Scene Understanding from Unposed Images](https://arxiv.org/abs/2607.01633)

**<font color=#1a73e8>作者：</font>** Hu Zhu, Bohan Li, Xianda Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Comprehensive 3D scene understanding from sparse, unposed images requires a model to recover renderable geometry, open-vocabulary semantics, and free/occupied 3D space without relying on external camera calibration. Recent feed-forward Gaussian methods improve pose-free reconstruction and semantic rendering, but their Gaussian primitives are mainly optimized through image-space objectives and remain weakly constrained in unobserved regions. We propose \textit{COVScene}, a pose-free semantic Gaussian framework that couples renderable Gaussian primitives with a dense semantic occupancy field through differentiable volumetric lifting. Instead of converting Gaussians to voxels only at evaluation time, COVScene lifts the predicted semantic Gaussians inside the training computation graph, so volumetric regularization provides gradients to Gaussian opacity, geometry, and semantic features. The framework combines a semantic-aware Geometry Transformer, multi-task Gaussian decoding, geometric foundation distillation, and occupancy entropy regularization to support novel view synthesis, open-vocabulary semantic querying, and semantic occupancy prediction within a single representation. Experiments on ScanNet and ScanNet++ show that COVScene maintains competitive rendering quality, improves open-vocabulary segmentation, and achieves stronger semantic occupancy prediction than the self-supervised baseline without direct voxel-level supervision.

---


### 78. [Autonomous discovery of traffic laws with AI traffic scientists](https://arxiv.org/abs/2607.01639)

**<font color=#1a73e8>作者：</font>** Xingyuan Dai, Yue Liu, Xiaoyan Gong 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Universal traffic laws describe recurrent patterns in congestion, mobility and driving behavior across cities, providing a scientific basis for transportation planning, management and control. Their discovery, however, remains expert-driven, requiring candidate regularities to be identified from heterogeneous observational evidence or validated through intervention experiments. Although autonomous artificial intelligence (AI) systems have advanced scientific discovery in controlled laboratory settings, extending them to complex transportation domains remains a challenge. Here we present TrafficSci, an agentic AI system that formulates traffic-law discovery as an iterative, auditable workflow integrating evidence scoping, critic-judge hypothesis induction, and observational-interventional validation. Across four case studies spanning population, network, control and trajectory scales, TrafficSci autonomously rediscovers three established traffic laws and identifies an unreported intrinsic temporal memory scale in urban driving behavior, statistically consistent across eight cities and two trajectory datasets. TrafficSci provides a route for extending AI-driven scientific discovery from controlled domains to complex urban systems.

---


### 79. [Multi-Resolution Flow Matching: Training-Free Diffusion Acceleration via Staged Sampling](https://arxiv.org/abs/2607.01642)

**<font color=#1a73e8>作者：</font>** Xingyu Zheng, Xianglong Liu, Yifu Ding 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hardware-agnostic strategies for accelerating text-to-image diffusion, such as timestep distillation and feature caching, can reduce inference time without custom kernels or system-level optimization. Among them, multi-resolution generation strategies have recently received broad attention, attaining more than 5x speedup without any training. However, the design of performing upsampling in the latent space, together with the selective modification of partial regions, causes these methods to exhibit noticeable blurring or artifacts. To this end, we propose MrFlow, a training-free multi-resolution acceleration strategy for pretrained flow-matching models built upon a staged low-to-high-resolution pipeline. MrFlow first rapidly generates the main structure at low resolution, then performs super-resolution in the pixel space using a lightweight pretrained GAN-based model, subsequently injects low-strength noise to enable high-frequency resampling, and finally refines the details at high resolution. Quantitative and qualitative results on FLUX.1-dev and Qwen-Image show that MrFlow exploits the quadratic token reduction and reduced step requirement of low-resolution sampling to achieve 10x end-to-end acceleration while keeping OneIG within a 1% gap relative to that before acceleration, significantly surpassing other training-free acceleration strategies, and requiring no training or runtime dynamic identification whatsoever. MrFlow can further be directly combined orthogonally with pre-trained timestep distillation strategies, achieving even higher generation acceleration of up to 25x.

---


### 80. [Boosting Ultrasound Image Classification via Attribute-Guided Dual-Branch Framework](https://arxiv.org/abs/2607.01648)

**<font color=#1a73e8>作者：</font>** Bo Zhao, Yapeng Li, Juhua Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ultrasound image classification is essential for computer-aided diagnosis. However, current methods often neglect clinical priors, leading to poor generalization in challenging scenarios and a lack of interpretability that limits clinical adoption. To address these issues, we aim to develop a medical-prior module that can be seamlessly integrated into existing pipelines to enhance both diagnostic performance and interpretability. In this paper, we propose an attribute-guided dual-branch framework for ultrasound classification that introduces domain-agnostic medical attribute priors, improving generalization while offering interpretable evidence. Specifically, a baseline branch follows conventional architectures and predicts image categories via a fully connected classifier. An attribute-guided branch injects domain-agnostic attributes as priors and produces human-interpretable decision cues. Finally, an adaptive decision module fuses the two branches in a data-dependent manner to yield the final prediction. Experiments across diverse ultrasound classification tasks demonstrate that our approach can be integrated into multiple backbones and state-of-the-art methods with low overhead, consistently improving accuracy and interpretability. Code is available at: this https URL.

---


### 81. [Plug-and-Play Volumetric Reconstruction for Compressive Sensing Light-Sheet Microscopy](https://arxiv.org/abs/2607.01654)

**<font color=#1a73e8>作者：</font>** Jianqing Jia, Yi Gong, Xinyuan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We investigate volumetric reconstruction for compressive sensing light-sheet microscopy (CS-LSM), where fast volumetric imaging is achieved by encoding multiple axial planes into each camera exposure. To recover the underlying volume from highly multiplexed measurements, we propose a plug-and-play (PnP) framework that flexibly incorporates any user-specified denoiser into the reconstruction process. Building on a slice-based formulation, we further introduce an axial-coupled model that exploits correlations between adjacent slices to improve volumetric continuity. For efficient computation, we derive a Woodbury-based update for the data-consistency step in both the slice-based and axial-coupled formulations, and employ a Gauss-Seidel sweep for the denoising step in the axial-coupled model. Under a weakly convex regularization assumption, we establish subsequential convergence of the proposed algorithm. Experiments on synthetic and real zebrafish-heart data demonstrate that the proposed framework successfully recovers cellular structures from compressed measurements, and provide practical insights into the comparative performance of commonly used denoisers within the PnP framework under the CS-LSM setup.

---


### 82. [Domain Generalization via Text-Anchored Information Bottleneck](https://arxiv.org/abs/2607.01657)

**<font color=#1a73e8>作者：</font>** Eunyi Lyou, Yunjeong Choi, Junho Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual recognition models often fail when deployed in new environments. Domain Generalization (DG) addresses this by learning representations that remain invariant to environment-specific variations. Recent approaches increasingly rely on large vision-language models, assuming that preserving their expressive visual representations improves robustness. However, we show that such visual expressiveness can instead propagate spurious cues that tie representations to the training environments, hindering invariant learning. We therefore discard visual guidance and instead treat the language embedding space as the primary source of domain invariance, naturally acting as an information bottleneck that preserves core semantics while suppressing domain-specific variations. Extensive experiments across diverse backbones exhibit state-of-the-art performance and further analyze what makes guidance effective for robust generalization. These findings shift the focus of DG from improving representations to designing supervision that enforces invariance.

---


### 83. [Teaching Vision-Language-Action Models What to See and Where to Look](https://arxiv.org/abs/2607.01658)

**<font color=#1a73e8>作者：</font>** Yuguang Yang, Canyu Chen, Zhewen Tan 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving. However, existing VLAs' training relies heavily on text-centric visual question answering and chain-of-thought reasoning data, which emphasizes linguistic reasoning rather than action-grounded planning. As a result, the learned representations capture semantic knowledge but lack spatial dependencies crucial for reliable trajectory prediction. We propose DriveTeach-VLA, a framework that explicitly teaches VLAs what to see and where to look. Driving-aware Vision Distillation (DVD) injects driving-specific perceptual priors into the vision encoder, while 2D Trajectory-Guided Prompts (2D-TGP) provide spatial conditioning aligned with feasible driving trajectories. Together, they form a vision-guided learning pipeline: what to see (DVD pretraining) - where to look (TGP-guided SFT) - how to act (TGP-guided GRPO). DriveTeach-VLA achieves the state-of-the-art performance on NAVSIM and nuScenes. Our code is available at: this https URL.

---


### 84. [Message Passing Based Two-Timescale Bayesian Learning for Joint Channel and Memory Hardware Impairments Tracking](https://arxiv.org/abs/2607.01660)

**<font color=#1a73e8>作者：</font>** Wei Xu, An Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hardware impairments in massive multiple-input multiple-output (MIMO) receivers introduce inter-symbol memory and inter-element coupling, severely degrading channel estimation. This paper employs a residual recurrent gated unit (RGRU) to model the intra-slot memory of the hardware impairments and proposes a message-passing-based two-timescale Bayesian deep learning (MP-TTBDL) framework for joint channel and impairment tracking. Owing to small-scale fading, the wireless channel varies rapidly across slots, whereas hardware impairments drift slowly due to hardware aging and environmental variations. To capture these distinct physical timescales, a fastvarying Markov prior and a slow-varying Gaussian Markov prior are assigned to the sparse channel and the network parameters, respectively. Based on a multi-slot factor graph formulation, a message-passing algorithm is developed. Specifically, the inter-slot messages admit closed-form updates, while the intra-slot factor graph, due to its complex recurrent structure, is partitioned into a channel tracking module and an impairments calibration module. The channel tracking module performs sparse channel estimation via turbo orthogonal approximate message passing (Turbo-OAMP), and the impairments calibration module updates the impairment parameters via a specially designed deep approximate message passing (DAMP) procedure, with the two modules iteratively exchanging extrinsic information through expectation propagation (EP) until convergence. Simulation results show that the proposed framework robustly achieves lower channel estimation error than conventional compensators followed by channel estimation across different online impairment scenarios and signal-to-noise ratio (SNR) conditions.

---


### 85. [Diverse Evidence, Better Forecasts: Multi-Agent Deliberation Under Information Asymmetry](https://arxiv.org/abs/2607.01661)

**<font color=#1a73e8>作者：</font>** Yuante Li, Yicheng Tao, Kate Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems are increasingly used for forecasting future events, as deliberation among multiple LLMs is believed to improve reasoning and calibration. Yet existing approaches overlook a critical design choice: what information each agent receives. When all agents are given identical evidence, deliberation collapses into herding rather than genuine belief revision, leaving multi-agent systems little better than a single agent. We identify this as a fundamental gap and propose designed information asymmetry to close it: by partitioning evidence into shared public and disjoint private subsets, each agent holds exclusive knowledge that can only reach others through deliberation. We theoretically show that this decomposition reduces inter-agent error correlation, and instantiate it in InfoDelphi, a framework combining relevance-aware evidence routing, rationale-based iterative deliberation, and confidence-weighted aggregation. On PolyGym, a benchmark of 375 binary forecasting questions derived from real-world prediction markets, InfoDelphi outperforms the strongest single-agent and multi-agent baselines by 12--18% in Brier score and 4--8 percentage points in accuracy. More detailed experiments confirm that removing information asymmetry eliminates most deliberation gains, establishing diversity of input as the key enabler of effective multi-agent reasoning.

---


### 86. [Unified Panoramic-Gaussian Representation for Monocular 4D Scene Synthesis](https://arxiv.org/abs/2607.01663)

**<font color=#1a73e8>作者：</font>** Yuankun Yang, Yi Wei, Wenyang Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 4D scene synthesis from monocular videos has made significant progress in recent years. However, existing methods are typically constrained by view interpolation. As a result, they struggle to infer unseen regions beyond the observed views. In this paper, we reformulate the task as 4D scene synthesis with unseen regions, which extends beyond traditional interpolation settings. Camera-conditioned video generation enables unseen region synthesis by guiding generation along specified cameras. However, these methods lack explicit 3D priors and are optimized with random camera trajectories. This design leads to severe inconsistencies under large trajectory deviations. To address this limitation, we build a unified training and inference framework with panoramic trajectory guidance. While this design improves cross-view consistency, the panoramic representation alone fails to model dynamic content effectively. Object motion in panoramic space introduces scale and shape distortions. To address this, we propose PanoGaussian, a unified Panoramic-Gaussian representation that distills the panoramic representation into an explicit dynamic Gaussian representation to capture dynamic physical priors of the 4D scene. Experiments demonstrate that PanoGaussian achieves consistent 4D scene synthesis even under large viewpoint variations.

---


### 87. [Revisiting Decentralized Online Convex Optimization with Compressed Communication](https://arxiv.org/abs/2607.01665)

**<font color=#1a73e8>作者：</font>** Hao Zhou, Xiaoyu Wang, Chang Yao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decentralized online convex optimization (D-OCO) is a popular framework for distributed applications with streaming data. To tackle the communication bottleneck, previous studies have investigated D-OCO with compressed communication and proposed several algorithms that are variants of online gradient descent (OGD). However, for D-OCO with exact communication, the best existing algorithms are variants of follow-the-regularized-leader (FTRL). In this paper, for the first time, we propose two FTRL-type algorithms for D-OCO with compressed communication. Compared with OGD-type algorithms, our algorithms are more elegant in both algorithmic design and theoretical analysis. The key insight is that the dual update mechanism of FTRL allows us to make a simple application of the technique for average consensus with communication compression. More specifically, our first algorithm considers the full-information setting, and can match the existing regret bounds. Our second algorithm is designed for the bandit setting, and can significantly improve both the regret bounds and communication costs of existing algorithms.

---


### 88. [UniWind: Toward Unified Day-Ahead Wind Power Forecasting via Physics-Informed State Routing](https://arxiv.org/abs/2607.01670)

**<font color=#1a73e8>作者：</font>** Ronghui Xu, Tongxin Wu, Guozhen Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Day-ahead wind power forecasting is essential for cost-effective power-system operation. It is primarily driven by future meteorological conditions while retaining temporal dependencies in power generation. In practice, observed wind-farm power often entangles physically available power with local environmental effects and latent operational states, such as shutdowns and curtailment. Existing physical models provide useful constraints but adapt poorly across wind farms, whereas data-driven models can capture rich correlations but often conflate meteorological effects with state-induced deviations. In this study, we propose UniWind, a wind power forecasting model based on physics-informed state routing. UniWind first employs a Physical Prior Estimator to construct a site-calibrated physical prior by combining site-conditioned monotonic warping with a shared physical power curve. It further applies a physical upper-bound constraint to shape this prior as a soft envelope of available wind power generation. UniWind then proposes a Latent State Encoder to model operating-state embeddings and transforms the physical prior into final power forecasts through a State-aware Power Corrector, which uses knowledge-guided supervised state routing and bounded, state-specific expert correction. Full-shot and cross-farm zero-shot experiments on more than 20 real-world datasets demonstrate the accuracy and robustness of UniWind.

---


### 89. [Separating Expert Retention from Autonomous Source Inference in Raw-ECG-Replay-Free Continual ECG Deployment](https://arxiv.org/abs/2607.01674)

**<font color=#1a73e8>作者：</font>** Yufan Lu, Xinhui Liu, Chenyang Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In multi-source ECG deployment, models may need to incorporate new data sources when earlier raw ECGs cannot be retained or replayed. Freezing a pretrained backbone and assigning each source an isolated classifier prevents parameter interference, but deployment still requires selecting an expert when source metadata are unavailable. We study this distinction through \ours{}, an incremental expert bank built on frozen 1024-dimensional ECGFounder features. Each arriving domain adds a balanced-softmax linear expert, while a lightweight router is fitted only on retained training features and domain labels from sources observed so far. A validation-calibrated margin rule fuses the two most likely experts instead of committing to a single routed expert.
On CPSC, PTB-XL, Georgia, and Chapman-Shaoxing, source-aware expert selection reaches $0.7915\pm0.0036$ Macro-F1 and a matched offline independent-head reference reaches $0.7885\pm0.0009$, supporting strong source-aware expert retention. Without source IDs, an MLP router reaches $0.7756\pm0.0027$ and top-2 margin fusion reaches $0.7782\pm0.0022$. The top-2 gain over hard MLP routing is small ($+0.0026$), with a 95\% confidence interval from paired bootstrap that includes zero. Across three domain orders, the top-2-to-oracle gap remains $0.0111$--$0.0133$, identifying autonomous source inference as the main remaining bottleneck. No raw ECGs are replayed, but frozen training features are retained for router updates; the method is therefore not memory-free.

---


### 90. [HistoSeg++: Delving deeper with attention and multiscale feature fusion for biomarker segmentation](https://arxiv.org/abs/2607.01675)

**<font color=#1a73e8>作者：</font>** Saad Wazir, Rao Faizan, Daeyoung Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Segmentation of biomarkers in medical images is frequently viewed as a first step towards medical image analysis in any bioinformatics or biomedical application. Despite progress, existing methods still struggle to capture information at multiple scales and to perform upsampling effectively across different datasets. These shortcomings often result in suboptimal generalization capabilities. Recently, architectures belonging to the Nested-UNet family excel in capturing multiscale contextual information and upsample them effectively. In this work, We propose a novel Nested-UNet architecture that effectively captures multi-scale contextual information. It includes inner and outer attention units to enhance focus during upsampling, along with channel-wise feature recalibration using squeeze-and-excitation modules, leading to improved segmentation performance. Additionally, the architecture integrates an edge-aware loss to emphasize boundary accuracy by assigning greater importance to edge regions. Tested extensively on three publicly available benchmark datasets. Our method demonstrates a generalization performance superior to existing Nested-UNet methods. Code: this https URL

---


### 91. [ICDepth: Taming Video Diffusion Models for Video Depth Estimation via In-Context Conditioning](https://arxiv.org/abs/2607.01677)

**<font color=#1a73e8>作者：</font>** Xuanhua He, Jiaxin Xie, Mingzhe Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular video depth estimation requires temporal consistency, geometric accuracy, and generalization across diverse scenarios, yet existing methods struggle to achieve all three simultaneously. Discriminative models excel at per-frame accuracy but suffer from temporal drift due to limited context windows, while generative methods improve consistency and generalization at the cost of extensive training data (10M+ samples) and lack of geometric precision. In response to these issues, we introduce \textbf{ICDepth}, a framework that adapts pre-trained text-to-video diffusion transformers for video depth estimation via In-Context Conditioning (ICC), leveraging their rich spatial-temporal priors. To address key challenges in transferring ICC from generation to dense prediction, we propose: (1)~\textbf{SAND-Attention}, which ensures precise spatial-temporal alignment via shared RoPE and enforces unidirectional attention to prevent noise contamination; (2)~\textbf{SRFM}, which injects DINOv2 semantic and resolution priors to enhance geometric precision. ICDepth achieves state-of-the-art results on multiple benchmarks with remarkable data efficiency, trained on only 0.8M frames ($6$--$13\times$ less than competing generative methods), while demonstrating strong zero-shot generalization to diverse domains.

---


### 92. [Beyond Gradient-Based Attacks: Adversarial Robustness and Explainability Stability in Cybersecurity Classifiers](https://arxiv.org/abs/2607.01679)

**<font color=#1a73e8>作者：</font>** Mona Rajhans, Vishal Khawarey  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Adversarial attacks on cybersecurity classifiers pose a dual threat: degrading predictions and destabilising the SHAP-based explanations that security analysts rely on to understand and triage alerts. We extend our prior MLP conference study to Random Forest and XGBoost across four tabular security datasets (phishing URLs, UNSW-NB15, NF-ToN-IoT, HIKARI-2021), evaluating five attacks including three black-box methods applicable to non-differentiable tree models. We introduce the Explainability Stability Index (ESI), a scalar metric computed from TreeSHAP attribution drift under adversarial perturbation, reported on the same [0,1] scale as the Robustness Index (RI). A key finding is that gradient-based black-box attacks (ZOO) produce degenerate results against XGBoost (apparent RI ~0.98) due to piecewise-constant prediction surfaces, while score-based Square Attack reveals genuine vulnerability (RI ~0.36). These degenerate perturbations still drive substantial attribution drift: XGBoost ESI ~0.06-0.16 despite near-perfect ZOO robustness, versus 0.14-0.29 for RF, showing that prediction robustness and explanation stability are distinct axes requiring joint measurement. A two-axis framework (gradient dependence, query efficiency) explains the observed attack ranking and yields practical guidance for tree ensemble evaluation. A step-size ablation explains a counterintuitive PGD anomaly on z-score normalised tabular data.

---


### 93. [WARP: Weight-Space Analysis for Recovering Training Data Portfolios](https://arxiv.org/abs/2607.01686)

**<font color=#1a73e8>作者：</font>** Tzu-Heng Huang, Aditya Goyal, John Cooper 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models are routinely released to the public, yet the data recipes used to train them -- such as domain mixture weights that determine how different sources are sampled -- are rarely disclosed. This creates an access asymmetry: researchers study the resulting models but lack visibility into the training distribution that produces them. Prior works for inferring training data, such as membership inference, detect at the level of individual samples and thus cannot characterize the global composition of the training corpus. We introduce WARP, a framework that recovers a fine-tuned model's training mixtures directly from its released weights. WARP interpolates between the base and fine-tuned models using model merging, generating pseudo-checkpoints that approximate the missing training trajectory and expose a geometric footprint of the training data in the weight space. From these simulated footprints, WARP extracts geometric features and maps them to domain proportions using either a parameter-free softmax readout or an MLP projector trained on synthetic mixtures. In controlled experiments with BERT and GPT-2, WARP recovers domain mixtures with an average MAE as low as 0.046 and 0.104 respectively, outperforming membership inference and a variant with access to the true training trajectory.

---


### 94. [Epistemic Goggles: A Pretrained Module that Induces an Epistemic Frame via Gradient Editing](https://arxiv.org/abs/2607.01690)

**<font color=#1a73e8>作者：</font>** Joshua Penman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Finetuning a language model on documents that are explicitly annotated as fictional results in a model that still actually believes the documents' core claims, an effect known as Negation Neglect. In our evaluations, models trained on documents prefixed and suffixed with such annotations correctly identify the relevant claims as fictional only about 9% of the time. To address this, we introduce Goggles, a learned module that intervenes on the finetuning gradient rather than the data. During supervised finetuning, a Goggles module edits the gradients an LLM LoRA receives, imparting a chosen epistemic frame (the stance the model takes toward the nature of what it reads) to whatever the documents teach. A Goggles instance is trained once for a given base model, frame, and LoRA configuration, then applied frozen to documents it was never trained on. Trained through Goggles on those same documents, now carrying no fictional annotation, the model flags the content as fictional roughly 91% of the time, while preserving capability (GPQA and TruthfulQA match or exceed baseline). The same architecture supports other frames: a Goggles instance can be trained to treat documents as "part of an AI safety evaluation by Redwood Research" rather than simply as fiction. The imparted frame persists under continued finetuning that pushes back toward the claim, where prior interventions revert. Goggles suggests a path toward training language models on known-misaligned data without absorbing the behaviors that data demonstrates.

---


### 95. [From Answer Generators to Reasoning Facilitators: Designing AI Tutors for Mathematical Reasoning in High-Stakes Environments](https://arxiv.org/abs/2607.01692)

**<font color=#1a73e8>作者：</font>** Yuming Feng, Yuan Tian, Erica Zhao  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The rapid integration of Large Language Models (LLMs) into educational technology threatens to reduce mathematical learning to mere answer generation. This paper presents a generative study, usability study, and 12-participant field deployment of AITutor, an interactive system that translates theoretical pedagogical mechanisms into concrete user interface features. We explore how junior-high students preparing for high-stakes exams (Zhongkao) interact with AI tutoring. Through mixed-methods triangulation (7,379 telemetry events, 8 contextual observations, 10 interviews), we reveal that students actively resist traditional Socratic dialogue under time pressure, repurposing "answer-first" shortcuts as vital diagnostic checkpoints. We demonstrate how features like layered worked examples, step-linked visual grounding, and metacognitive scaffolding lower the interaction cost of reasoning repair. We contribute a "Reasoning-Centered Product Loop," offering actionable implications for designing AI that structurally supports the inspection, local repair, curriculum verification, and delayed retrieval of mathematical reasoning in the wild.

---


### 96. [A Mathematical Introduction to Diffusion Models](https://arxiv.org/abs/2607.01693)

**<font color=#1a73e8>作者：</font>** Jianfeng Lu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> These notes give a proof-oriented introduction to diffusion models from the viewpoint of sampling, tracing a single arc from classical sampling dynamics to modern diffusion samplers, their error analysis, and inference-time control. Throughout, the material is layered into core definitions and identities proved in full, representative estimates proved under simplifying assumptions, and research-level theorems stated with a proof roadmap. The intended audience is beginning graduate students with a background in probability but no prior exposure to stochastic differential equations, stochastic numerics, or diffusion models.

---


### 97. [Frequency Shift Physics-Informed Extreme Learning Machine for Solving High-Frequency Partial Differential Equations](https://arxiv.org/abs/2607.01694)

**<font color=#1a73e8>作者：</font>** Xiong Xiong, Ruonan Zhai, Zheng Zeng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Solving partial differential equations (PDEs) with high-frequency solutions remains a central challenge in physics-informed machine learning due to spectral bias -- the tendency of neural networks to learn low-frequency components preferentially. This paper proposes a Frequency Shift Physics-Informed Extreme Learning Machine (FS-PIELM) framework that addresses this limitation through an additive mechanism for weight initialization. Rather than multiplying random weights by a scaling factor, the method translates the mean of the Gaussian weight distribution while keeping the variance fixed at unity, thereby avoiding the variance amplification inherent in scaling-based methods. Two variants are developed: FS-PIELM-L assigns independent frequency magnitudes to individual neurons, while FS-PIELM-G groups neurons for improved robustness. Theoretical analysis shows that the frequency variance under the proposed framework remains bounded and approaches unity regardless of target frequency, in contrast to the quadratic growth of conventional approaches. The method preserves the computational efficiency of extreme learning machines, requiring only a single linear solve. Experiments on seven benchmark problems spanning six equation types -- Helmholtz, wave, Poisson, Klein-Gordon, heat, and advection-diffusion -- on both regular and complex geometries show that the linear variant achieves the best accuracy in six of seven cases, with improvements of one to nearly five orders of magnitude over existing PIELM variants. The code and data accompanying this manuscript will be made publicly available at this https URL.

---


### 98. [Structure-Aware Gaussian Splatting for Large-Scale Scene Reconstruction](https://arxiv.org/abs/2607.01698)

**<font color=#1a73e8>作者：</font>** Weiyi Xue, Fan Lu, Chi Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting has demonstrated remarkable potential in novel view synthesis. In contrast to small-scale scenes, large-scale scenes inevitably contain sparsely observed regions with excessively sparse initial points. In this case, supervising Gaussians initialized from low-frequency sparse points with high-frequency images often induces uncontrolled densification and redundant primitives, degrading both efficiency and quality. Intuitively, this issue can be mitigated with scheduling strategies, which can be categorized into two paradigms: modulating target signal frequency via densification and modulating sampling frequency via image resolution. However, previous scheduling strategies are primarily hardcoded, failing to perceive the convergence behavior of scene frequency. To address this, we reframe the scene reconstruction problem from the perspective of signal structure recovery and propose SIG, a novel scheduler that synchronizes image supervision with Gaussian frequencies. Specifically, we derive the average sampling frequency and bandwidth of 3D representations, and then regulate the training image resolution and the Gaussian densification process based on scene frequency convergence. Furthermore, we introduce Sphere-Constrained Gaussians, which leverage the spatial prior of initialized point clouds to control Gaussian optimization. Our framework enables frequency-consistent, geometry-aware, and floater-free training, achieving state-of-the-art performance by a substantial margin in both efficiency and rendering quality in large-scale scenes. The code is available at: this https URL

---


### 99. [Pmeta-TLA: Backdoor Attacks for Speech Classification Models via Meta-Learning with Timbre Leakage Attack](https://arxiv.org/abs/2607.01702)

**<font color=#1a73e8>作者：</font>** Yueming Huang, Wenhan Yao, Fen Xiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recently, speech classification methods have gained widespread adoption in intelligent gadgets. Current study indicates that backdoor attacks provide a substantial security concern to these models, underscoring the pressing necessity to investigate additional potential attack techniques to expose and prevent such risks. This work discusses the vulnerability of current speech triggers to detection by deep neural network defenders and introduces the Timbre Leakage Attack (TLA). The suggested trigger disseminates timbre information at the frame level within the deep self-supervised features, producing poisoned samples that appear natural to human perception. Furthermore, we introduce Pmeta-TLA, an innovative training mechanism for embedding numerous backdoors one time. This method proposes a multi-backdoor injection training strategy using meta-learning and Projected Conflicting Gradients (PCGrad) and introduces TLA as a multi-target attack tool within it. We performed tests on data-poisoning backdoor attacks in keyword spotting tasks utilizing some deep neural network models. Experimental results indicate that the proposed strategy attains superior Attack efficacy, enhanced stealthiness, robustness, and a reduced attack cost relative to baseline methods.

---


### 100. [Consistent Scene Understanding in 3D Gaussian Splatting via Multi-Cue Mask Refinement](https://arxiv.org/abs/2607.01708)

**<font color=#1a73e8>作者：</font>** Hyunjoon Park, Donghyeon Cho  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable instance-level scene understanding is a fundamental prerequisite for object-level interactions and high-fidelity 3D representations. While current methods often leverage 2D foundation segmentation models to obtain these priors, their 2D-centric design typically yields fragmented masks and inconsistent predictions across different views. To address these issues, we propose a novel framework that produces consistent 2D instance masks to guide the optimization of 3D Gaussian Splatting (3DGS) feature fields. Our framework consists of three main stages. (1) Multi-Cue Extraction that generates synergistic semantic, geometric, and structural priors from input images. (2) Multi-Cue-Guided Mask Merging process that consolidates fragmented masks using a composite merge score derived from semantic, depth, and edge cues. (3) Cross-View Mask Matching that establishes globally consistent identity assignments across all viewpoints. By transforming viewpoint-specific segments into coherent 3D primitives, our approach enables stable 3D instance segmentation and effective downstream editing tasks. Experiments demonstrate that our method significantly improves cross-view consistency and segmentation stability over existing baselines while maintaining high-fidelity photometric reconstruction.

---


> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-266](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
