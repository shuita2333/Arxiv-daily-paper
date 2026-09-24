# 🧠 大模型相关研究 | 2026年09月25日

> 本类共 **172** 篇论文：已确认 **158** 篇，待复核 **14** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-172**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-172**

---

### 151. [AnchorReasoning: A Visual Grounding and Causal Reasoning Dataset in Long-Tail Autonomous Driving Scenarios](https://arxiv.org/abs/2609.28366)

**<font color=#1a73e8>作者：</font>** Zhipeng Bao, Wenjie Zhao, Tianle Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) offer a promising approach to long-tail autonomous driving, but existing driving datasets provide limited supervision for connecting decision-critical visual evidence with reasoning and planning. We introduce AnchorReasoning, a visually grounded reasoning dataset built on WOD-E2E, containing 416,119 annotated frames and 395,379 decision-critical elements across four major categories and 19 fine-grained types. Each frame is organized as a visually grounded chain-of-thought (VG-CoT) that links decision-critical element identification and localization, element attributes and implications, driving-action rationale, and action and trajectory planning. We further develop a curriculum supervised fine-tuning strategy that progressively learns these hierarchical capabilities, together with an object-size-aware grounding metric for evaluating localization quality. Experiments across eight general-purpose, embodied-AI, and AV-specific backbones show that VG-CoT supervision improves grounded reasoning and trajectory prediction. Across models, 5-s ADE and FDE decrease by 7.84 and 11.86, while RFS Frame and Cluster improve by 1.66 and 1.70. These gains are achieved with 18.5 fewer reasoning tokens and 0.32 s/frame lower inference latency on average, demonstrating the value of visually grounded, decision-focused supervision for VLM reasoning and planning in long-tail autonomous driving.

---


### 152. [When and Where to Trust the Teacher: Unifying On-Policy Distillation and GRPO through Entropy-Calibrated Credit Assignment](https://arxiv.org/abs/2609.28385)

**<font color=#1a73e8>作者：</font>** Jie Zhang, Jingxiao Yang, Zhehao Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) supervises mathematical reasoning through final-answer correctness, but provides little guidance on individual tokens. On-policy distillation (OPD) supplies dense feedback on student-generated responses, yet teacher preference need not reflect correctness. Recent hybrids combine OPD and verifier-derived advantages or reweight task credit using teacher ratios. However, teacher guidance enters after verifier-based group normalization, and token reweighting need not preserve the total task credit assigned to each response. We introduce Unified Entropy-Calibrated Credit Redistribution for GRPO (UECR-GRPO), which integrates verifier and teacher signals within a single GRPO-style update at both the response and token levels. \emph{Path-Utility Unification} (PUU) combines verifier reward and a teacher-to-anchor path log-ratio in a single KL-regularized objective. Its on-policy implementation uses a length-normalized teacher score and combines both rewards before group normalization and PPO clipping, allowing teacher evidence to influence the response ranking. \emph{Entropy-Calibrated Redistribution} (ECR) then uses the signed teacher--old-policy token gap to redistribute the verifier-derived component. Full-vocabulary teacher entropy attenuates uncertain guidance, while a response-wise zero-sum projection preserves the total task credit and its token-wise sign before clipping. Across five mathematical reasoning benchmarks, UECR-GRPO achieves average \(\mathrm{Avg@12}\) accuracies of 17.21\% and 65.09\% with Qwen3-1.7B and Qwen3-4B students, respectively, exceeding the strongest baseline at each scale by 0.89 and 0.56 percentage points.

---


### 153. [Fine-Tuning LLMs for Translation: General Forgetting Mitigation Does Not Preserve MT-Specific Instruction Following](https://arxiv.org/abs/2609.28395)

**<font color=#1a73e8>作者：</font>** Niklas Scholz, David Thulke, Abdallah Nasir 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fine-tuning large language models on parallel data improves translation quality but can cause catastrophic forgetting. Mitigation methods are generally evaluated by retention on general benchmarks. We ask whether these findings transfer to machine translation (MT) fine-tuning and to MT-specific instruction following (MT-IF): instructions that modify a translation, such as formality, grammatical gender, and length control. We compare methods anchored to auxiliary data, to model outputs, and to the base model parameters, first in a screening study with Llama 3.2 1B Instruct, then on Llama 3.1 8B Instruct fine-tuned on bidirectional Arabic-English or Spanish-English data. Elastic Weight Consolidation preserves general capabilities best in both stages; on the 8B Spanish model the average score on general benchmarks drops 1.7 points versus 11.0 for standard fine-tuning, yet its scores for formality and grammatical gender control remain close to standard fine-tuning. Only data mixing with control-task examples preserves these controls, but its gains do not transfer to unseen prompts for the same task.

---


### 154. [Memory Attention](https://arxiv.org/abs/2609.28399)

**<font color=#1a73e8>作者：</font>** Jiale Kang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models typically construct attention values from contextual hidden states, even when some of their content may be reusable across contexts. We investigate whether token-indexed memory can replace the dedicated value projection when complemented by contextual information. We propose Memory Attention (MA), which forms values by combining layer-specific token memory with contextual keys. The memory supplies token-specific representations, while the keys preserve context dependence. At inference, normalization can be folded into the memory tables, reducing value construction to lookup and addition. Token-indexed retrieval also enables CPU offloading with prefetching, reducing GPU parameter storage. Under matched training token budgets and with additional memory parameters, experiments across attention configurations show improved language modeling and average downstream performance.

---


### 155. [Agent-Editing World Model: Rethinking World Modeling for LLM Agents](https://arxiv.org/abs/2609.28416)

**<font color=#1a73e8>作者：</font>** Shuang Sun, Guoxin Chen, Fanzhe Meng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have enabled agents to tackle long-horizon tasks across diverse environments. To further improve agent performance, existing language world models typically predict environment observations, yet reconstructing high-entropy, execution-dependent tool responses offers limited value when real feedback is available. Meanwhile, agents suffer from \emph{task-state contamination}, where unsupported assumptions and outdated plans persist in history and distort subsequent decisions. We propose the \textbf{Agent-Editing World Model (AEWM)}, which models how reasoning and actions shape future task progress rather than simulating tool responses. AEWM combines \textbf{Action Judge} to distinguish \textsc{Critical}, \textsc{Exploratory}, and \textsc{Noisy} decisions with \textbf{State Revision} to edit noisy reasoning--action continuations from the same observed history. \textbf{EditAct} integrates these capabilities with real execution, directly changing the state underlying subsequent decisions rather than merely providing critiques. We train AEWM across Search, Terminal, and Software Engineering through mid-training and supervised fine-tuning. AEWM achieves 70.5\% macro-F1 on our Action Judge benchmark, exceeding the strongest frontier baseline by 10.6 points. Across six benchmarks and three agent backbones, EditAct improves average scores by 3.2--6.7 points over the strongest baseline. Furthermore, rejection sampling fine-tuning on verified EditAct trajectories, termed \textbf{AEWM-RFT}, improves over Self-RFT by 2.2--2.6 points across three domains without online AEWM guidance.

---


### 156. [Cross-Scale Transfer Learning for Depression Severity Prediction: From PHQ-8 to HAMD-17 Across Languages and Clinical Paradigms](https://arxiv.org/abs/2609.28430)

**<font color=#1a73e8>作者：</font>** Wenjie Feng, Sahba Zojaji, Satoshi Nakamura  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This work addresses continuous depression-severity score prediction from clinical interview transcripts under data scarcity. We propose a sequential low-rank adaptation (LoRA) protocol for cross-scale transfer: a Qwen3 backbone with a bounded regression head is first fine-tuned on the English DAIC-WOZ dataset (189 avatar-mediated sessions, PHQ-8), and the adapter then initializes fine-tuning on the Chinese PDCH dataset (100 real clinical consultations, HAMD-17), where a reinitialised, scale-specific head predicts the clinician-assigned score. All configurations use patient-level stratified 5-fold, 2-repeat cross-validation. On the data-scarce HAMD-17 target, the sequential protocol attains the best point-estimate MAE , RMSE, and macro-$F_1$ on both 0.6B and 1.7B backbones, outperforming target-only training and non-LLM baselines---4.96/6.59/0.36 with Qwen3-0.6B and 4.38/5.62/0.46 with Qwen3-1.7B. Ablations suggest that correctly aligned source supervision gives the best point estimates (unsupervised exposure and shuffled-label controls also show partial gains), that native-Chinese target input outperforms machine-translated English input, and that the reversed order yields no clear gain within run-to-run variance. The study is an exploratory, single-site internal evaluation: it does not establish screening or diagnostic utility, nor separately identify the contribution of the scale, language, or paradigm shifts. To our knowledge, no prior study evaluates this specific DAIC-WOZ-to-PDCH sequential transfer setting.

---


### 157. [Order-Invariant Answers, Order-Sensitive Representations in Mathematical Reasoning](https://arxiv.org/abs/2609.28442)

**<font color=#1a73e8>作者：</font>** Zhixu Silvia Tao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reordering a set of mathematical rules without changing its meaning should preserve the correct answer, but must a model's internal representations stay invariant too? We investigate this question using synthetic multi-step function-composition problems, each presented under multiple rule orderings with the same correct answer. We measure accuracy and permutation signal-to-noise ratio (SNR), which quantifies how distinctly ordering patterns are represented relative to variation across problem instances. Across 16 language models ranging from 1B to 8B parameters, we find a pattern: models that solve reordered problems more accurately represent different rule orderings more distinctly. Layer-averaged permutation SNR is positively rank-correlated with accuracy in every synthetic setting we evaluate, with Spearman correlations reaching 0.86. These findings highlight a distinction between answer invariance and representation invariance: successful mathematical rule composition can accompany distinct internal representations between equivalent rule orderings. This motivates distinguishing answer invariance from representation invariance, and offers a representational perspective on mathematical reasoning beyond answer accuracy alone.

---


### 158. [StudentBench: AI and human tutoring yield equivalent GRE learning gains](https://arxiv.org/abs/2609.28470)

**<font color=#1a73e8>作者：</font>** Curtis Northcutt, Inaara Hasmani, Kevin Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence offers an unprecedented opportunity to augment human capabilities, yet progress at the frontier has focused primarily on advancing model capabilities. We introduce StudentBench, a suite of AI teaching evaluations and a public platform that enables large-scale data collection with over 175,000 student-AI messages to study whether large language models (LLMs) produce learning gains equivalent to human tutoring. Using StudentBench, we measured learning gains on Quantitative and Verbal GRE questions across 2,383 human participants receiving AI tutoring, human tutoring, or no tutoring. We establish that AI tutoring is statistically equivalent to expert human tutoring for GRE learning gains (p = .015), and in five of the seven GRE domains, the best performing AI tutor surpassed the human tutor, on average. In a second study, expert human tutors compared LLM-generated lesson plans and practice problems through 2,028 pairwise rubric evaluations. Together, the two studies clearly separate AI tutors across: (1) lesson planning, (2) practice-problem creation, (3) conversational pedagogy, (4) cost, and (5) engagement. Surprisingly, one AI tutor achieved learning gains equivalent to human tutoring (p = .044) at 918 times lower cost (USD 0.0052 for AI versus USD 4.81 for human, per percentage point gained). For Quantitative GRE sessions, faster AI replies correlated with more student messages, more messages with more correct practice, and more correct practice with larger learning gains (all p < .002). The StudentBench platform is freely available at this https URL.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 159. [nnFoundation: 3D Foundation Models for Radiology](https://arxiv.org/abs/2609.26924)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Constantin Ulrich Harsy, Tassilo Wald, Karol Gotkowski 等 83 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiological artificial intelligence has advanced rapidly, yet most systems remain narrowly task-specific, data-intensive, and fragile under domain shift. Foundation models promise more transferable and data-efficient solutions, but existing approaches are limited in scale, evaluated narrowly, and often assume that a single pretrained model can support diverse downstream tasks. Here we present nnFoundation, complementary convolutional and transformer-based 3D radiological foundation models. Developed within the Human Radiome Project (THRP), nnFoundation is trained on 2.1 million CT, MRI, and PET image volumes from 125 institutional and public datasets. We evaluate them across 108 tasks spanning segmentation, detection, classification, report generation, and image retrieval, including evaluations under domain shift, by external partners and in low-data and low-compute regimes. Across all task types, our convolution- and transformer-based nnFoundation models consistently outperform both prior 3D foundation models and training from scratch, establishing state-of-the-art performance for radiological imaging. However, performance follows a consistent task-dependent structure: the convolutional nnFoundation model dominates spatially localized tasks, whereas the transformer-based nnFoundation model excels in tasks requiring global semantic reasoning and in frozen-feature settings. Dynamically aligning the foundation model topology with the dataset characteristics post-hoc further improves transfer across heterogeneous 3D settings. These results show that transferable 3D radiological performance is governed not by a single universal model, but by the interplay of scalable pretraining, complementary architectures, and dataset-aware adaptation. We release nnFoundation models integrated into nnU-Net and nnDetection, enabling immediate application across established radiology workflows.

---


### 160. [The Like Trap: Multi-Stage Poisoning against Agents in Similarity-based Recommendation Systems](https://arxiv.org/abs/2609.27155)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yue Xing, Pengfei He, Zitao Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With recent advancements in large language models (LLMs) and LLM-based agents, these agents are becoming increasingly autonomous and gaining broader access to act on users' behalf on the internet. However, the vulnerability of automated agents deployed on social media platforms (e.g., for managing a user's personal account) remains underexplored. Existing studies on agent poisoning typically assume that the adversary can expose poisoned content to the agent. Although such an attack is direct and effective, it is more easily detected and mitigated. In the context of social media platforms, this leaves open whether the recommendation system itself would surface such content to the agent in a more subtle manner. Through theoretical analysis, we show that the like-score mechanism used in OASIS can be exploited, and we characterize the conditions under which a multi-stage chain of poisoned posts can steer the agent's feed. Based on these insights, we further develop an algorithm that crafts realistic poisoned posts. Experiments support our theoretical findings and demonstrate the effectiveness of the proposed algorithm. Notably, by exploiting the like-score feedback loop, the attack causes the recommendation system to select poisoned posts even when their user-post similarity falls below the retrieval threshold.

---


### 161. [A Scaling Study for fMRI Foundation Models](https://arxiv.org/abs/2609.27232)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Wenhao Ye, Xuanye Pan, Junfeng Xia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling laws have guided large-model development in computer vision and natural language processing, but the relationships among data, model size, and compute remain unclear for functional magnetic resonance imaging (fMRI) foundation models. Here, we conduct a controlled empirical study using pretraining data from more than 200 source datasets and over 10,000 GPU-hours of experiments. Holding the pretraining framework and downstream protocol fixed, we vary pretraining data size, model size, and training duration. Downstream performance generally improves with compute, yet models using similar compute can perform substantially differently. Additional pretraining data bring larger gains at larger model sizes, suggesting that data and model size should be scaled together. At matched compute, increasing pretraining data benefits more tasks than increasing model size, although the pattern varies across tasks. We then use in-distribution (ID) downstream performance to select the combination of pretraining data size, model size, and training duration at two fixed compute budgets. The resulting models are locked before out-of-distribution (OOD) evaluation. They achieve the highest average performance across the evaluated OOD tasks among the compared fMRI foundation models while using less pretraining compute. Overall, our results show that compute alone does not characterize fMRI scaling: performance depends on how pretraining data, model size, and training duration are combined.

---


### 162. [UniDataAgent: An Ontology-Grounded Agent for Enterprise Question-to-Report Automation](https://arxiv.org/abs/2609.27257)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yutai Duan, Yahui Zhao, Zhangti Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Enterprise data agents must preserve organization specific semantics, not just translate questions into queries. We present ChinaUnicom DataAgent (UniDataAgent), an ontology grounded system for reusable question-to-report analysis that separates semantic acquisition from online execution. Ontology Acquisition and Validation stage (OAV) builds versioned enterprise ontologies from metadata, business knowledge, and supporting materials through expert authored business skills, constrained generation, question verification, and selected expert review. Question-to-Report Execution (QRE) stage retrieves semantic contracts for each question, coordinates skills and data tools, validates results, and produces evidence linked reports. Across 27 enterprise tables and roughly thousands of metric types, ontology construction took a few hours instead of about one week manually. It took just a few minutes to generate the reports, instead of several working days. Ontology grounding achieved 95.0\% strict accuracy on real business questions, versus 72.5\% for document RAG, especially on structured and compositional tasks. The system has already been deployed to generate cost savings and has the potential to be replicated in other enterprises.

---


### 163. [A generalizable structural brain MRI foundation model built through dual-priority federated pretraining](https://arxiv.org/abs/2609.27611)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhen Yu, Yang Liu, Xiahai Zhuang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models hold promise for generalizable analysis of structural brain magnetic resonance imaging (MRI) across development, aging and disease. However, existing models are typically built through centralized pretraining on pooled data, despite privacy and governance constraints. Such pooling optimization can overemphasize cohort size and overlook complementary information from smaller, specialized cohorts. Here we present BrainFedFM, a structural brain MRI foundation model federatively pretrained on 164,707 three-dimensional scans drawn from diverse real-world data distributions and organized across 42 federated sites. BrainFedFM uses dual-priority federated pretraining, coupling spatial-priority masking at each site with site-priority aggregation at the server to emphasize informative anatomical regions locally and prioritize site contributions globally. Across 20 downstream datasets spanning 17 classification, regression and segmentation tasks, BrainFedFM achieved the state-of-the-art performance (mean rank 1.68, 50\% gain) across seven models, including four centralized foundation models, while showing particularly consistent advantages in classification and regression and robustness across underrepresented populations. These findings demonstrate the generalizability of BrainFedFM and highlight federated pretraining as a practical strategy for developing neuroimaging foundation models from distributed data without pooling raw images.

---


### 164. [InGuard: Towards Generalized Inner Guardrail for Safe Text-to-Image Generation](https://arxiv.org/abs/2609.27620)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zeyu Wang, Xiaodan Li, Zhiwen Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern text-to-image (T2I) models generate high-quality images from arbitrary user prompts, yet they can just as easily produce not-safe-for-work (NSFW) content. Conventional outer guardrails consist of two components: a prompt classifier that checks for risk before generation, and a post-hoc image classifier that checks the fully generated image. In this design, both classifiers operate outside the generation pipeline and do not use the model's own representations. This separation can limit prompt-screening accuracy, while the image-side check runs only after the full generation cost has been spent. Moreover, a flagged prompt can only be rejected, even when it could be adjusted to produce a safe image. In this work, we propose the Inner Guardrail (InGuard), a safety framework that works inside the pipeline on the model's own representations, leaving base-model parameters untouched. First, a risk classifier grades each prompt as unsafe, risky, or benign based on the text encoder's embeddings, with no external language model. Second, SAGE (Soft-gated Asymmetric Guardrail for Embeddings) modifies the embeddings of risky prompts, aiming to return a safe image instead of a refusal. Third, a latent detector checks the one-step clean latent estimate midway through denoising, reaching nearly image-level performance and halting generation when risk is detected. We also construct the RevGen Safety Benchmark to evaluate T2I safety under realistic conditions: 10,000 prompts built through real-image reverse generation, with a rewriting step that supplies controlled intellectual-property (IP) characters, covering graded porn/gore risks, categorical IP risks, and benign negatives. Across five open-weight T2I models, InGuard reaches 97.9-98.8% safety rate, matching or exceeding the outer guardrail, with 57.5-73.5% less benign disturbance, ~3.7x fewer parameters, and 50-55.6% of denoising steps skipped.

---


### 165. [What Do Tabular Foundation Models Compute In Context? In-Situ Representation Refinement through Attention-Gated Updates](https://arxiv.org/abs/2609.27679)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Tian Zhou, Beverly Jin, Linxiao Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> What reusable computation should a tabular foundation model learn when every table defines a new supervised task? We develop in-situ representation refinement: support labels guide updates to the episode's representations, and these updates transfer to unlabeled queries without changing model parameters. A regularized leave-one-out objective yields a support correction and its query extension. The leading term separates attention-based reading from state-dependent scaling, motivating RefineICL: an attention-gated, FFN-free contextual stack with selected low-rank feature interaction and typed memory. RefineICL-L24 reaches 0.93836 OVR-AUC and 0.87173 accuracy on AMLB29. A benchmark-informed continuation reaches 1644.8 Elo on the 38-dataset TabArena snapshot, 31.4 Elo above TabPFN-3 under the same evaluation. It also improves all four reported metrics over TabPFN-v3 on both TabZilla views. In a matched 100K-update depth grid, an expanded FFN gives no consistent validation benefit and uses 60.2% more peak inference memory at L8. Internal interventions show that support representations are more than a static source of labels: removing one intermediate support update, while preserving the query output, increases final query cross-entropy in all 72 tested episodes. Together, the derivation and interventions explain how attention-gated updates can construct a task-specific predictor in context.

---


### 166. [Alignment of LRMs via Counter-Aligned Few-Shot Conversation Exposure](https://arxiv.org/abs/2609.27763)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xiangyu Zhou, Saleh Zare Zade, Dongxiao Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) rely on explicit chain-of-thought (CoT) reasoning and large context windows to achieve strong performance on complex tasks, but these features also introduce new attack surfaces. We show that LRMs' reasoning processes can be systematically steered by prepending counter-aligned few-shot conversations containing explicit CoT traces, leading to unsafe generations on harmful queries and unwarranted refusals on benign ones. We formalize this attack as SRCF (Steering Reasoning via Counter-Aligned Few-shot Conversations) that operates solely through a flexible conversational interface and requires no access to the model's parameters and gradients. Our key insight is that SRCF exploits an adversarial generalization issue that induces a representation drift, causing the representations of benign and harmful inputs to shift in a similar direction. This observation motivates our post-training defense, ARCF (Aligning Reasoning via Counter-Aligned Few-Shot Conversations), which exposes models to counter-aligned conversational contexts while enforcing aligned targets. ARCF is compatible with existing post-training methods and consistently improves safety and helpfulness without degrading utility.

---


### 167. [Learning What to Activate: Combinatorial Capability Allocation for Long-Horizon Multimodal Agents](https://arxiv.org/abs/2609.27869)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Wenhao Yuan, Chenchen Lin, Jian Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon multimodal agents rely on specialized capabilities for perception, retrieval, reasoning, verification, and execution. Existing designs typically activate a fixed capability set or invoke a predefined workflow, incurring substantial computational overhead while failing to accommodate stage-dependent capability demands. In this paper, we study the \textit{combinatorial capability allocation} problem for long-horizon multimodal agent systems, where the system selects a cost-sensitive subset of specialized capabilities at each interaction stage, which is nontrivial since capability values depend on the selected subset, while previous allocations alter the states encountered by subsequent decisions. We introduce \textsc{CoCA}, an on-policy learning framework that recovers a deployable capability-subset policy from sparse conditional comparisons. On states visited by the student policy, the stronger teacher compares the marginal net values of candidate capabilities, conditioned on the currently selected subset. Then, we adopt a conditional utility model to transform such comparisons into an autoregressive capability-subset policy, avoiding explicit enumeration. We further introduce dual-level on-policy distillation to address distribution mismatch both across environment states and within the partial subsets encountered during set construction. Finally, trajectory-level reinforcement learning refines the distilled policy toward task success, activation cost, and allocation stability. At inference time, allocation is performed solely by the lightweight student policy without teacher queries or online updates. Experiments on long-horizon multimodal environments and controlled capability-demand shifts demonstrate the superiority of our method over the state-of-the-art baseline methods.

---


### 168. [Compliant with Local Controls, Collectively Discriminatory. A Governance Architecture for Multi-Agent AI in Regulated Finance](https://arxiv.org/abs/2609.27994)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jose Manuel de la Chica Rodriguez, Juan Manuel Vera Diaz, Pablo Delgado Romero  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Financial institutions are beginning to deploy agentic workflows in credit, fraud, collections, compliance, and operational control. Governance remains largely component-centric: each model or agent is specified, tested, authorized, and monitored locally. That is insufficient when institutional risk arises from the joint behavior of many locally acceptable components. We call this gap constitutional non-compositionality: local compliance checks need not compose into acceptable collective outcomes such as bounded disparate impact, market integrity, or traceable accountability. We propose ARIA as a finance-specific reference architecture and falsifiable research agenda for agent-population governance. It organizes six capabilities across normative-accountability, execution-control, and assurance-learning planes: policy specification, population-level observed-versus-expected behavior monitoring (M2), bounded authority, runtime containment, adaptive policy change, and preserved human oversight competence. Two simulations illustrate shared-signal thin-file exclusion under local controls and earlier warning from observed-versus-expected distributional monitoring in a constructed drift regime. The contribution maps these controls to fair-lending, EU AI Act, model-risk, and conduct-supervision evidence needs, and closes with a validation agenda rather than a production-effectiveness claim.

---


### 169. [Controlled Attribute-Specific Summarization of Interrogative Dialogues](https://arxiv.org/abs/2609.28004)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** A Aditya Bhardwaj, Arjit Singh Arora, Md Shad Akhtar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Effective summarization of interrogative dialogues is a critical task in forensic and investigative settings, requiring high factual accuracy, coherence, and attribute-specific relevance. In this work, we introduce CASPER, a novel Chain-of-Thought Attribute-Specific Prompting for Evaluative Summarization framework that leverages structured prompting and iterative refinement to generate high-quality summaries of interrogator-witness interactions. We construct MINDSum, a dataset extending the MIND corpus, comprising 6,000 utterance pairs annotated with event details, factual statements, character descriptions, and fillers. CASPER employs RoleEval, a hierarchical evaluation mechanism where multiple roles (officer, inspector, senior inspector) iteratively assess summaries based on predefined criteria. By integrating entity extraction and structured feedback loops, CASPER significantly improves factual consistency and contextual completeness compared to existing baselines. Experimental results demonstrate that our framework outperforms standard summarization models on both lexical (ROUGE) and semantic (BERTScore) metrics, while human evaluation confirms its alignment with expert reasoning. Our findings underscore the potential of controlled summarization in high-stakes domains, paving the way for AI-driven forensic intelligence.

---


### 170. [Support-Compiled Feature Folding: More Evidence at Lower Memory Across Tabular Foundation Models](https://arxiv.org/abs/2609.28208)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Tian Zhou, Beverly Jin, Xue Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models face a feature-side scaling dilemma: full-width pairwise mixing grows quadratically with the number of columns, whereas feature selection saves memory by discarding evidence. We introduce Support-Compiled Feature Folding (SCFF), a training-free inference framework that resolves this dilemma without changing the frozen backbone. SCFF routes support-ranked features through bounded leaves of the native feature encoder, support-checks the residual evidence, and merges the encoded messages before a single contextual prediction. It thereby converts quadratic feature-interaction work into linear-in-width work with a bounded local working set, without ensembling predictions or training new parameters. On the exhaustive 18-dataset wide-table slice of fixed AMLB-29, TabZilla, and TabArena snapshots, SCFF improves dataset-macro accuracy and NLL on all six evaluated backbones. All four matched-width comparisons retain favorable 95 percent dataset-bootstrap intervals on locked folds, with relative error reductions up to 26.1 percent. Median paired GPU-memory savings are 2.09x to 2.36x, and the ratio of separately observed maximum peaks reaches 34.3x. Under a measured peak-memory ceiling, SCFF uses the saved budget to preserve more support-selected evidence, improving accuracy by 4.06 and 3.72 points over the widest feasible single leaf on predeclared wide-Core strata of TabICLv2 and TabPFN-3.

---


### 171. [Do Center Biases Propagate? Robustness of Pathology Foundation Models in Whole-Slide Image Classification](https://arxiv.org/abs/2609.28231)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ilán Carretero, Pablo Meseguer, Rocío del Amor 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathology foundation models (PFMs) have transformed computational pathology through powerful representation learning from histopathological images. PFMs provide rich, discriminative representations for whole slide image (WSI) analysis, enabling tasks such as slide-level classification under multiple instance learning (MIL). However, these representations may also encode non-biological signals associated with acquisition centers, potentially introducing spurious shortcuts into downstream predictions. In this work, we evaluate center-associated robustness in WSI classification using a controlled training setting with increasing class-center correlations quantified by Cramér's V. We benchmark six PFMs across four datasets and two MIL aggregators, while evaluating ComBat as a robustification strategy. We further introduce the Area Under the Cramér's V Curve (AUCC) to jointly capture absolute classification performance and its degradation as spurious correlation increases. Results show that center-related information encoded by PFMs propagates to WSI-level predictions, with robustness depending on both the PFM representation and MIL aggregation strategy. Additionally, ComBat harmonization does not provide consistent robustness gains across datasets.

---


### 172. [Benchmarking Hyperspectral Foundation Models for Hyperspectral Unmixing](https://arxiv.org/abs/2609.28283)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Edgard Dabier, Christophe Kervazo, Pietro Gori 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Several foundation models dedicated to hyperspectral images have recently been made available. These models are trained on large unlabeled datasets and exhibit strong performance on many hyperspectral imaging tasks, such as classification or denoising. Nonetheless, their performance for hyperspectral unmixing -- the task of separating mixed spectra of overlapping materials in a hyperspectral image -- remain understudied. This might partly be due to the fact that most of them rely on vision transformer backbones, including patchification, leading to a feature resolution problem. While hyperspectral unmixing already arises from the low resolution of hyperspectral images, this patchification step potentially makes the problem even more ill-posed. Therefore, in this work, we aim to answer two questions: 1) \emph{how do foundation models perform in hyperspectral unmixing?}; 2) \emph{how to tackle the feature-level loss of resolution?} To answer the first question, we benchmark foundation models for unmixing, showing that they can reach state-of-the-art performance on four hyperspectral unmixing datasets. To answer the second question, we compare several feature upsampling approaches and empirically show that using a simple one can lead to high performance results. The code is available at this https URL.

---


> [!TIP]
> 当前位于：**151-172**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-172**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
