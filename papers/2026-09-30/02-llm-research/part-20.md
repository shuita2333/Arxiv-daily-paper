# 🧠 大模型相关研究 | 2026年09月30日

> 本类共 **992** 篇论文：已确认 **928** 篇，待复核 **64** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**951-992**（第 20/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | **951-992**

---

### 951. [PlanGuard: A Guardrail for Multi-Step Plan Safety in Embodied Agents](https://arxiv.org/abs/2609.32801)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Junchi Chen, Changtao Miao, Yuxiao Xiang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Embodied task planners may produce multi-step plans whose subtask dependencies and interactions with the environment create physical risks during execution. Yet existing safeguards overlook such compositional risks, as general-purpose guardrails focus on semantic harm and embodied safety detectors assess subtasks in isolation. To address this gap, we introduce PlanGuard, the first pre-execution detector that evaluates the physical safety of a complete multi-step plan in its current environment. For training and evaluation, we construct a Multi-Step Plan Safety (MSP-Safe) dataset through paired task construction, plan generation using diverse planners, and safety annotation by three judges. Task-oriented SFT on MSP-Safe establishes fundamental plan-safety assessment capabilities, yet a substantial gap remains between compact models suitable for real-time deployment and stronger but costlier large models. Accordingly, we propose Strong-Teacher Adaptive Compensation for On-Policy Distillation (STAC-OPD), which provides compact models with adaptive strong-teacher supervision along their on-policy trajectories. It combines token-level distribution transfer from a fine-tuned strong teacher with probability-routed sequence-level compensation, retaining student-generated targets when the student favors the reference safety decision and using teacher-reconstructed targets otherwise. Across all test subsets, PlanGuard-2B achieves average 87.15% ACC and 87.21% F1, demonstrating effective whole-plan physical-risk detection at compact model scale. Code and dataset will be publicly released.

---


### 952. [Counterfactual Self-Evolving Agents for Evidence-Grounded Reasoning](https://arxiv.org/abs/2609.32870)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xing Han, Yuxin Wang, Chen Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-play proposer--solver methods improve reasoning by generating tasks and learning from verified solutions. However, for evidence-identifiable tasks, where case-specific evidence and domain knowledge determine a checkable answer, self-play requires generating plausible cases whose answers can be independently verified. We introduce counterfactual self-evolution, which generates counterfactual context for reconsidering the original case. A trainable Proposer constructs targeted evidence edits and describes potential outcome changes with causal explanations. We handcraft an expert-verified counterfactual instruction-tuning dataset to teach the Proposer to generate high-quality counterfactuals across a broad range of action--outcome scenarios. Each counterfactual instruction-tuning example specifies an edit within a defined category and explains its hypothesized causal effect on the decision, teaching the Proposer to reason systematically about what changes and why. We instruction-tune the Proposer on these examples, then formulate a fine-tuning reward that integrates feedback from the Solver and Verifier. Across diverse counterfactual scenarios, this reward favors high-quality counterfactuals and warranted revisions, while penalizing changes that overturn correct decisions. The counterfactual context aims to correct errors and strengthen confidence in correct decisions. Accepted counterfactuals accumulate in memory that supplies in-context evidence to the frozen Solver; the Solver adapts through evolving context rather than weight updates. We apply the framework to clinical reasoning, fact verification, and business reasoning. Our evaluation tracks performance over successive rounds as counterfactual memory grows, including transfer to harder cases. Our method achieves superior results across diverse frontier models.

---


### 953. [Leaky Students: Membership Inference against On-Policy Distillation](https://arxiv.org/abs/2609.33136)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhexi Lu, Mingzhi Zhu, Stacy Patterson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student to match a teacher's next-token distributions on student-generated trajectories. However, privileged information supplied to the teacher for OPD training may contain sensitive data. Whether the student leaks private information about the records supplied to the teacher during distillation remains poorly understood. To the best of our knowledge, we present the first systematic study of membership inference in this setting. We find that fresh student trajectories expose sparse membership signals that fixed reference-answer losses often miss. These signals are mixed with probability changes caused by training on other records. We introduce Leaky, which samples fresh trajectories from the target model and compares its token log-probabilities with the maximum across matched reference models trained without the candidate records. It applies Leaky ReLU to the resulting gaps, preserving positive gaps and downweighting negative gaps as an approximate correction for incidental positive gaps in non-members. Across fifteen targets spanning mathematics, medical question answering, and code generation, Leaky outperforms all evaluated baselines and achieves mean AUROC 0.875, compared with 0.614 for the strongest baseline on each target in the main evaluation. On the same sampled trajectories, the strongest baseline achieves mean AUROC 0.826. These results show that students trained through OPD can expose the membership of records used for teacher supervision, even when fixed reference-answer losses provide little evidence of membership.

---


### 954. [Generalization Dynamics of LM Pre-training](https://arxiv.org/abs/2609.33150)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jiaxin Wen, Zhengxuan Wu, Dawn Song 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> People typically assume that LMs stably mature from pattern-matching parrots to generalizable intelligence during pre-training. We build a toy eval suite and show this mental model is wrong: throughout pre-training, LMs frequently and suddenly hop between parrot-like and intelligence-like computations. We call this mode-hopping. Across our suite, LMs suddenly latch onto memorized or in-context patterns instead of in-context learning, use System 1 instead of System 2 thinking, pick up what sounds true instead of what is true, fail at multi-hop persona QA, out-of-context reasoning, and emergent misalignment -- then just as suddenly revert and generalize. Mode-hopping is not explained by standard optimization dynamics: it is locally stable and cannot be fixed by checkpoint averaging. We instead think of it as a capacity allocation problem: in a capacity-bounded model, generalizable circuits must compete with the shallow ones learned early in training, and the data in each pre-training window may decide which circuits win. Our suite provides a new efficient lens on generalization. We demonstrate two concrete applications: (i) select intermediate pre-training checkpoints that strongly generalize reasoning and alignment, better than the final pre- or mid-training checkpoints, and (ii) select pre-training data that controls and stabilizes generalization dynamics.

---


### 955. [Can Protein-Derived Knowledge Improve Pathology Foundation Models?](https://arxiv.org/abs/2609.33178)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Di Zhang, Zhangpeng Gong, Jiashuai Liu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Molecularly guided pathology foundation models (PFMs) exploit transcriptomic or proteomic information to enrich whole-slide image (WSI) representations, yet effectively leveraging large standalone molecular corpora remains challenging. First, existing molecular foundation models encode protein sequences or single-cell states, not the patient-level bulk expression profiles paired with WSIs. Second, because cross-modal supervision is restricted to paired WSI-omics samples, knowledge from standalone molecular corpora reaches the pathology encoder only indirectly, creating a paired-support bottleneck. To address these challenges, we propose a three-stage framework that decouples proteomic knowledge acquisition from cross-modal transfer, yielding ProSlide, a slide-level hierarchical pathology foundation model. First, to close the modality gap, we pretrain a Proteomic Foundation Encoder (PFE) on 12,695 sample-level bulk protein profiles using virtual profile generation and expression-space multi-view pretraining. Second, we pretrain ProSlide, a patch-region-slide encoder, to predict protein expression from paired WSI-protein samples. Third, to relax the paired-support bottleneck, we introduce Prot2Path, a cross-modal relational distillation objective. For each paired sample, it aligns the similarity distributions of the WSI and its protein profile over a shared, frozen bank of PFE-encoded paired and standalone profiles. We evaluate ProSlide on 12 downstream tasks across breast, lung, and renal cancers. Despite being pretrained with only 2,229 WSIs and 12,695 sample-level protein profiles, ProSlide achieves the highest mean accuracy and AUC within each cancer group.

---


### 956. [FocusDrive: Reasoning with Visual Focus for Autonomous Driving](https://arxiv.org/abs/2609.33190)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhiyuan Liu, Zehong Ke, Yuanxin Tian 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driving decisions depend on both where to focus and how to act on what is seen. Effective driving reasoning must establish which objects matter, where they are, and how they inform the intended action. Text-based rationales can describe a driving response while leaving its correspondence to specific visual evidence implicit. Visual focus provides a concrete starting point for this connection by identifying what matters in the scene and where it is. We propose FocusDrive, a structured multimodal reasoning framework that organizes end-to-end planning around explicit visual focus. It pairs descriptions of decision-relevant objects with image-patch references, bringing explicit visual focus into the reasoning that generates driving plans and trajectories. We first assess this focus representation through driver gaze prediction, then investigate its role in planning reasoning using driving-focus annotations within existing NAVSIM training scenes. Experiments on W3DA and NAVSIM demonstrate competitive gaze prediction and end-to-end planning performance, with FocusDrive improving over text-based chain-of-thought. These results support visual focus as an effective link between scene understanding and driving action.

---


### 957. [Teach Yourself Where to Look: On-Policy Attention Self-Distillation for Reasoning](https://arxiv.org/abs/2609.33200)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Safaeid Hossain Arib, Rabeya Akter, Ismam Nur Swapnil 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation trains reasoning models on their own trajectories using dense token distribution guidance from a privileged teacher with access to a verified solution. This supervision transfers what the teacher predicts without directly transferring where it attends within the preceding context. We introduce On-Policy Attention Self-Distillation (OPASD), which complements token-level supervision with solution-conditioned attention distillation. Because the privileged teacher can attend to verified solution tokens unavailable to the student, OPASD projects teacher attention onto student-visible positions and renormalizes the resulting distribution before alignment. Across three model sizes and four competition-level mathematics benchmarks, OPASD consistently outperforms token-only OPSD, improving average accuracy by 4.98 to 8.40 percentage points. OPASD also avoids the response-length inflation and performance degradation observed with token-only distillation, reducing generated rollout tokens by 73.9% and estimated model compute by 72.6% while training 1.53x faster. These results show that solution-conditioned attention provides a complementary supervision signal that makes on-policy self-distillation more accurate, stable, and compute-efficient.

---


### 958. [When Do Models Admit They Are Wrong? Failure Disclosure Is Unstable Under Reinforcement Learning](https://arxiv.org/abs/2609.33220)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Steven Y. Feng, Noah D. Goodman, Michael C. Frank 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Outcome-based reinforcement learning can produce models with similar task performance but very different ways of communicating about their mistakes. We study failure disclosure: whether a model admits that an attempted solution failed rather than staying silent or presenting it as successful. Across repeated outcome-only GRPO training runs, failure disclosure varies far more than task accuracy. The pattern extends to a second reasoning task and stabilized PPO, persists at 7B, and also appears in an instruction-conditioned 32B setting. We also find that small floating-point and sampling differences during training can redirect reporting behavior even when the task objective and earlier training history are held fixed. Additional tests show that failure disclosure is not a single decision: Checking the answer, entering a report, and completing the admission can separate, and the weak point depends on the task and response format. Further, experiments with neutral controls show more broadly that behaviors left weakly constrained by training are especially likely to vary across runs, of which failure disclosure is an example. We can reduce variability in failure disclosure by discouraging the model from drifting from its starting policy on failed, well-formed responses. This makes reporting substantially more consistent, though its effect on task performance depends on the setting. Stable task accuracy therefore does not guarantee stable safety-relevant behavior: Researchers should measure these behaviors directly across runs and design training methods that keep them reliable.

---


### 959. [MIC: Explaining Image-Claim Inconsistencies in AI-Generated Multimodal Misinformation](https://arxiv.org/abs/2609.33441)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ruihong Zeng, Jonathan Tonglet, Preslav Nakov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Claims paired with AI-generated images are a rapidly growing form of misinformation. Existing automated fact-checking (AFC) methods mainly treat this as a provenance problem, detecting low-level synthesis artifacts to decide whether an image is AI-generated. However, such methods do not verify what human fact-checkers often check: whether an image's content is consistent with the context implied by its accompanying claim. To address this gap, we introduce MIC (Multimodal Inconsistency Checking), an AFC framework that assists human fact-checkers by detecting AI-generated multimodal misinformation and explaining inconsistencies using world knowledge. MIC first uses supervised fine-tuning (SFT) for task adaptation and then applies Group Relative Policy Optimization (GRPO) to directly optimize component-level verifiable rewards for verdict prediction, inconsistency type classification, visual evidence description, and world-knowledge explanation. We further introduce MIC-Bench, a benchmark comprising 8,812 image-claim instances derived from 4,406 claims, where each claim is paired with an authentic image and an AI-generated counterpart that introduces a controlled contextual inconsistency. Compared with SFT alone, GRPO further improves Macro-F1 by 4.67 and 4.11 points in the in-distribution and out-of-distribution settings, respectively, while also improving the semantic similarity of visual evidence descriptions and world-knowledge explanations to reference annotations. Our code and data are available at this https URL.

---


### 960. [What masking geometry works best for EEG foundation models?](https://arxiv.org/abs/2609.33487)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Pierre Guetschel, Bruno Aristimunha, Yassine El Ouahidi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> EEG foundation models hold promise for scalable brain-signal decoding across clinical and cognitive neuroscience applications, yet their pre-training pipelines remain poorly understood. Among design choices, the masking strategy is particularly critical: it determines what the network must predict and from which context. Yet it has never been ablated in isolation, as each new model bundles a new masking strategy with a new backbone and objective. In this paper, we formalize the design choices for spatio-temporal masking strategies and train various models with a single pipeline under varying masking configurations across two SSL frameworks (MAE and JEPA). We then systematically evaluate the resulting 58 pre-trained models on the 12 datasets of OpenEEGBench under a linear probe. Both frameworks agree on an optimal masking configuration and on shared failure modes. Outside these, performance is robust: 11 MAE and 9 JEPA configurations are statistically indistinguishable from the best. We further identify a novel JEPA-specific failure mode, tagged bias-inflation collapse, invisible to standard detectors. With a well-chosen mask, our pipeline reaches REVE-level downstream performance at a fraction of REVE's pre-training compute.

---


### 961. [OSCC: Certified Observation-Safe Coupling Optimization for Gradient-Noise Control in Imperfect-Information Learning](https://arxiv.org/abs/2609.33543)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Miaobo Hu, Shuhao Hu, Xiaobo Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coupled rollouts can reduce the noise of counterfactual action comparisons, but two issues prevent standard common-random-number constructions from serving as a general learning primitive in imperfect-information environments. First, an invalid coupling may expose hidden state, synchronize endogenous policy randomness, or misalign chance events after counterfactual histories diverge. Second, in multi-action policy optimization, lower return-contrast variance is not by itself the relevant objective: the optimizer depends on the return covariance matrix after projection through the local policy-gradient geometry. We introduce observation-safe counterfactual coupling (OSCC), a framework that defines an admissible class through marginal preservation, information-state safety, branch-local policy randomness, semantic event alignment, and trace-before-oracle replay. We derive a gradient-aware coupling criterion showing that, for marginal-preserving couplings, policy-gradient noise changes are determined by policy-Jacobian-weighted off-diagonal return covariance. This motivates OSCC-Select, a calibration-only selector that chooses among independent, root-only, continuation-only, and fully coupled rollouts using separate safety and gain certificates. Its gain target combines projected gradient noise with measured physical sampling cost and falls back to independent sampling whenever a simultaneous lower confidence bound does not certify improvement. On 100,000 fixed-root Leduc comparisons, the fully coupled CP-GRPO instantiation reduces return-contrast variance from 41.1158 to 18.1441, a 55.87% reduction, while preserving the declared branch marginals. With three actions, OSCC-Select chooses continuation coupling and attains gradient-noise trace 0.0783 versus 0.0917 for return-variance selection. Increasing calibration from 64 to 2,048 groups raises certification from 0.327 to 0.995.

---


### 962. [Safety Reconstructed: Generative Modeling via Masked Diffusion Builds Strong Safety Guardrails](https://arxiv.org/abs/2609.33634)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Gert Lek, Abele Malan, Chaoyi Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Guard models are the last line of defense between a language model and a harmful output, yet their training objective is surprisingly narrow. Existing guards learn to predict a single verdict token from a conversational context, concentrating supervision on a single target. The consequences are structural: models latch onto shortcut features, are overconfident, and remain sensitive to where safety evidence appears in the sequence rather than its role in the full context. We propose a different framing. Rather than predicting a label from text, our LLaDA-Guard asks which label better explains the text: scoring the prompt or response under each label hypothesis and classifying based on their difference. This shifts supervision to every token in the moderated region, forcing the model to account for full content rather than its most discriminative fragments. We instantiate this idea with a masked diffusion language model, fine-tuning LLaDA-8B-Instruct with a class-conditional reconstruction objective using LoRA and requiring no architectural changes beyond the base model. LLaDA-Guard leads on average rank against discriminative baselines trained on stronger backbones across seven held-out safety benchmarks, while exhibiting substantially better confidence calibration (ECE 0.0875 vs. 0.1384 for Qwen3Guard), less over-defense on benign prompts with unsafe-looking cues, and less prompt leakage when moderating responses. Its generative nature further enables token-level risk localization as a natural byproduct, yielding a pipeline for rewriting unsafe prompts into safe equivalents without additional training and achieving a 60.7% average conversion-to-safe rate.

---


### 963. [SafeMol: Dual-Modality Safety Alignment for Molecular Multimodal Models](https://arxiv.org/abs/2609.33640)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xinmiao Wang, Ruijie Wang, Menghui Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular multimodal models support diverse understanding and generation tasks but may introduce safety vulnerabilities when handling hazardous molecules. In this work, We reveal substantial jailbreak vulnerabilities under both text-only and graph-conditioned settings. Our analysis further shows that safety robustness must hold across input modalities while balancing safety, over-refusal, and utility. To address these challenges, we construct SafeMolBench, a molecular multimodal safety-alignment benchmark with 3702 samples covering 618 unique hazardous molecules and safe molecular tasks, organized into hazardous-harmful, hazardous-allowed, and utility-replay subsets to support unified training and evaluation of safety, over-refusal, and utility. Based on SafeMolBench, we propose SafeMol, a parameter-efficient safety alignment framework that jointly optimizes lightweight modules across text-only and graph-conditioned inputs, uses MMD for distribution-level representation alignment to reduce modality-induced discrepancies, and explicitly models molecular hazardousness and harmful operational intent. Experiments on SafeMolBench show that SafeMol reduces attack success by several tens of percentage points while largely maintaining low over-refusal and preserving molecular-task utility.

---


### 964. [Selecting Diverse SFT Traces Improves Post-RL Generalization](https://arxiv.org/abs/2609.33780)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Dylan Zhang, Mingyuan Wu, Jinning Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Verified solutions are not equally useful for preparing reasoning models for reinforcement learning (RL). We present a comprehensive study of route diversity, the variation in the sequences of reasoning steps in supervised fine-tuning (SFT) data, and propose a lightweight, rule-based fingerprint to select for it. From one pool at one budget, with matched training recipes and checkpoints, selecting diverse rather than similar routes improves post-RL problem coverage across puzzles and mathematics, including on problems harder than those seen in either training stage. In synthetic experiments, route-diverse SFT improves OLMo3-7B's pass@8 by 16.9 points on environments held out from SFT. In a single-model condition, where one model writes every candidate, diverse selection gains up to 6.2 points of mean pass@8 across 10 mathematics benchmarks. Pre-RL diagnostics suggest why: diverse SFT can produce both successful and failed attempts on more prompts despite slightly lower mean accuracy, giving group-relative RL more prompts with a learning signal. On 3 open-source corpora, our CPU-only selector, without model calls, outperforms more expensive alternatives in every comparison of mean post-RL performance. These results identify reasoning-route diversity as a practical criterion for selecting SFT data that better prepares models for RL.

---


### 965. [Video, Ergo Genero: Unifying Video Tasks via Spatiotemporal Analogy](https://arxiv.org/abs/2609.33935)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Chia-Hsiang Kao, Belinda Zeng, Bharath Hariharan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adapting video models to new tasks typically requires dedicated data curation and fine-tuning. While visual analogy provides a training-free alternative by specifying tasks in-context, it remains restricted to the image domain. To explore whether analogy-based methods can unify diverse video tasks and generalize to out-of-distribution scenarios, we introduce ViGeo, a framework that extends visual in-context learning to the video domain via spatiotemporal canvas completion. Evaluated on a diverse task taxonomy with a strict train-test split, ViGeo generalizes to unseen video manipulations and zero-shot modalities (e.g., event cameras). Finally, we identify task internalization, where a query format associated with a pretrained task overrides the demonstration, and show that this shortcut can be removed with a small amount of task-unrelated data, highlighting the need to decorrelate prompt format from task identity.

---


### 966. [When Is an SAE Feature Interpretable? A Validation Ladder for EEG Foundation Models](https://arxiv.org/abs/2609.34091)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yucong Cao, Chenqi Li, Tingting Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) decompose dense model activations into discrete latents, making individual features easy to interpret--and easy to misinterpret. In EEG foundation models, this creates a tempting inference: if removing alpha-band activity strongly changes a latent's activation, one might conclude that the latent represents alpha activity. Across 27 settings spanning three backbones, three EEG datasets, and three network depths, this interpretation initially appears compelling: alpha removal changes latent firing 7.3 times more than an equal-width sham notch (95% CI [6.2, 8.7], bootstrapped over settings). However, the alpha filter also deletes far more signal than the sham. After normalizing by removed spectral energy, the ratio falls to 0.28 (95% CI [0.22, 0.36]) and exceeds one in none of the 27 settings. Latents selected for their response to alpha removal are, on clean EEG, slightly anti-correlated with relative alpha power (mean r = -0.073), giving no support for a simple alpha-detector reading. Motivated by this failure case, we propose a validation ladder for semantic interpretations of SAE latents: it asks in turn whether a latent responds, whether that response survives controlling for how much signal the intervention removes, whether it is specific rather than broadly fragile, and whether the proposed property is visible on unperturbed data--while separately testing the stronger claim that the latent matters to a task classifier. Perturbation sensitivity alone does not establish what an SAE latent represents.

---


### 967. [WorldGraph: Graph-Native World Modeling](https://arxiv.org/abs/2609.34159)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zezhong Ding, Yipeng Li, Xike Xie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models infer latent states of an environment to capture its underlying dynamics and predict future evolution. Many real-world environments, however, are inherently relational and observed as evolving graphs, where entities, relations, and their properties change over time. Prior graph-related world models use graph structures to organize internal states or support task-specific reasoning, rather than treating an evolving graph itself as the modeled world. We instead study graph world modeling (GWM), where graph evolution itself constitutes the world dynamics. We formulate graph world modeling over observed graph evolution, latent graph states, and heterogeneous graph-transition predictions. Based on this formulation, we construct GWM-Zero, a benchmark covering node-, edge-, and graph-level transitions over eight temporal graph datasets. We propose WorldGraph, which combines a state-aware graph transformer for multi-granularity structural and transition-conditioned evolution modeling with transition-aware GRPO using dynamic grouping and structure-aware verifiable rewards. Extensive experiments on GWM-Zero show that WorldGraph consistently outperforms representative graph representation, temporal graph learning, graph pretraining, and graph world-model baselines across all three transition granularities.

---


### 968. [Efficient Reasoning via Constrained Optimization in Latent Space](https://arxiv.org/abs/2609.34181)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhinan Hou, XingChen Li, Keyou You  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) have shown remarkable reasoning capabilities, yet they still suffer from overthinking, generating redundant reasoning steps which incur substantial token consumption. Existing methods, such as suppressing reflective keywords or forcing shorter reasoning lengths, attempt to mitigate this issue but inevitably truncate necessary steps and induce underthinking, thereby compromising performance. To address this dilemma, we investigate the latent representations and observe that efficient reasoning steps naturally cluster into a concentrated region in latent space, while those deviating from this region tend to produce verbose sequences. To leverage this, we keep reasoning focused within this region via a quadratic program which projects deviating hidden states back into the region. Then we propose a novel training-free framework to achieve efficient reasoning that reduces token generation costs without sacrificing performance. Extensive experiments conducted on four models ranging from 1.5B to 14B, and across six benchmarks in math reasoning, coding, and scientific QA, validate the effectiveness of our method, up to a 12.1\% improvement in accuracy while reducing generated tokens by 11.8\% to 52.8\%. Codes are available at \href{this https URL}{this https URL}.

---


### 969. [X-MoD: Practical Scaling Laws for Sparse-Depth Routing Beyond Mixture-of-Depths](https://arxiv.org/abs/2609.34212)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Bowen Dong, Yilong Fan, Tengyu Pan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Depths (MoD) enables conditional computation across Transformer depth by routing only a subset of tokens through selected layers, but its original one-sparse--one-dense alternation tightly couples total capacity to active capacity and limits sparse-depth scaling. We introduce X-MoD, a scalable sparse-depth architecture that decouples token sparsity from anchor stride, allowing total parameter count to grow while keeping active-equivalent capacity nearly fixed. To make deep sparse routing trainable, X-MoD combines dense anchors with variance-scaled layer-wise gating and depth-wise token balancing. To make this regime analyzable and usable, we formulate sparse-depth routing as a conditional architecture-design problem: given compute, context length, and active-equivalent backbone size, how should the routing configuration be chosen? We develop a practical scaling-law framework by fitting X-MoD relative to FLOP-matched dense baselines, yielding an interpretable law that decomposes performance into sparse-capacity gain, sparse-context correction, and anchor-stride interaction. The law predicts validation loss across routing configurations and reveals how context length, model scale, and anchor stride shape sparse-depth performance. We validate the architecture and law through pretraining sweeps, held-out scaling-law prediction, ablations, downstream evaluations, and comparisons with Dense, MoD, and representative MoE baselines.

---


### 970. [Dr.Credit: Rubric-Grounded Process Credit Assignment for Deep Research Agents](https://arxiv.org/abs/2609.34296)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yingjian Zhu, Zhenyi Wang, Jiaxin Guo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rubric-based tasks are increasingly addressed through reinforcement learning (RL), with rubric scores used as training rewards. However, these rewards typically supervise final answers without distinguishing the contributions of intermediate decisions. Many existing credit assignment methods rely on ground-truth answers to define process rewards, limiting their applicability to open-ended tasks without canonical solutions. To address this limitation, the proposed rubric-grounded credit uses task requirements as a shared reference for final answer evaluation and process supervision. The information returned by tools is assessed for the additional support it provides toward satisfying each rubric relative to that rubric's history of accepted support. By referencing these histories, credit distinguishes new support from evidence already present in the trajectory while recognizing partial support for each rubric. this http URL uses rubric-grounded credit to supervise intermediate tool turns in an RL framework for deep research agents. The resulting process advantages are combined with GRPO outcome advantages to guide research decisions while retaining supervision of final-report quality. Evaluations on four in-domain and out-of-domain benchmarks show that this http URL outperforms the evaluated open deep research baselines on every primary metric and submetric. Meanwhile, with an 8B-parameter backbone, the trained agent achieves average performance competitive with the evaluated frontier proprietary models. Further analyses suggest more efficient evidence acquisition and higher-quality reports under limited research-turn budgets, motivating the extension of rubric-grounded process supervision to a broader range of rubric-based tasks.

---


### 971. [Dynamical Parameters: An Interpretability Framework for Time-Series Foundation Models](https://arxiv.org/abs/2609.34316)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Kang Yang, Gaofeng Dong, Liying Han 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This work studies a central gap in interpreting time-series foundation models (TSFMs): a dynamical property may be accessible in a hidden state even when the forecast fails to respond correctly as that property changes. We formalize these properties as Dynamical Parameters, including trend slope, oscillation frequency, and autoregressive dependence. We compare their representation accessibility, measured by recovery from hidden states, with their forecast response, measured by agreement with the expected forecast change. Across nine frozen TSFMs and thirteen laws, 42 of 63 model-parameter cells achieve accessibility above 0.95, whereas their median reference-aligned response relative to the conditional reference is only 0.46. To explain this gap, causal geometry compares the hidden-state change required to produce the reference response with the change induced by the parameter intervention. Directly modifying the hidden state recovers the reference response, but the parameter intervention often moves the state in a different direction. These results show that accessible parameter information need not be expressed in forecasts when input changes miss the required hidden-state direction.

---


### 972. [PhysioTRACE: Provenance-Aware Stress Tests for Physiological Foundation Models](https://arxiv.org/abs/2609.34466)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ayana Mussabayeva, Anuar Aimoldin, Olivier Oullier 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physiological foundation models encode how a signal was recorded alongside the physiology it reflects. When recording conditions are associated with diagnosis, this acquisition provenance can become a shortcut, yet the usual evidence, shifted transfer and provenance decodability, does not show whether a predictor uses it. We introduce PhysioTRACE, a four-axis behavioral audit for frozen encoders that separates what a probe can decode from what a fixed task head relies on. Recover scores how decodable provenance is; Stress reverses only the provenance-target association on the same held-out records; Intervene removes a train-localized provenance component; and Verify certifies that removal only if it beats matched random projections within a declared utility margin. Each audit thus ends in one of three verdicts: no reliance, or reliance with the remedy certified or refused. Across EEG and ECG, five training objectives, and five frozen foundation models, the relation between Recover's calibrated score and out-of-distribution utility changes sign between datasets, so neither can stand in for a reliance test. On paired EEG views where the shortcut is known by construction, the audit detects it (the exposed head loses about 0.2 AUROC when the association is reversed, while a control head is unaffected) and certifies removal of a rank-two component that restores control-level behavior without measurable utility loss, for both encoder objectives tested. On real ECG device metadata it returns all three verdicts: it certifies a remedy that removes 91% of one model's excess vulnerability, finds no reliance where device and diagnosis are barely associated, and refuses the remedy for a second model whose localized direction also carries task signal. Robustness to how inputs were recorded therefore needs a behavioral test, and PhysioTRACE provides one that can pass, fail, or refuse a remedy.

---


### 973. [ConCAD: Constraint-Aware Image-to-CAD Generation with Dual-Granularity Rewards](https://arxiv.org/abs/2609.34494)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Chenxi Zhai, Xi Cheng, Hang Cheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-to-CAD generation seeks executable parametric programs that recover both the geometry and design intent of a reference object. Existing systems are commonly evaluated by validity and shape overlap, although two solids with similar volume can encode different CAD relations. We introduce ConCAD, a constraint-aware image-to-CAD framework optimized via Group Relative Policy Optimization (GRPO) with rewards at two complementary granularities: a code-level constraint reward and an execution-level geometric reward. This complementary design disambiguates structurally distinct yet volumetrically similar shapes while ensuring valid 3D geometry. To verify that these rewards recover geometry and design intent, we introduce a B-rep geometric constraint satisfaction rate (G-CSR), which analytically extracts and evaluates geometric constraints from boundary representations. Experiments on the DeepCAD and Zero2CAD demonstrate that ConCAD achieves the best IoU and Chamfer Distance over competitive baselines, while also outperforming them on G-CSR, validating its superior recovery of both geometric fidelity and parametric design intent.

---


### 974. [KiT: A Foundation Model for Financial Time-Series Forecasting using DiffusionTransformers](https://arxiv.org/abs/2609.34507)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Boyu Zhang, Haorui Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial candlestick forecasting is fundamental to quantitative investment, yet it remains exceptionally challenging due to extremely low signal-to-noise ratios and vast heterogeneity across markets and instruments. Existing approaches have largely attempted to introduce deep learning to capture hidden temporal features, but most adopt an auto-regressive formulation, which leads to error accumulation during inference. Meanwhile, general-purpose time-series foundation models are not tailored to the unique structure of k-line data and yield unsatisfactory performance on downstream candlestick forecasting tasks. To tackle these problems, we introduce KiT, a K-line Diffusion Transformer foundation model, and reformulate future prediction as conditional path generation via flow matching: given a historical context window, the model generates an ensemble of plausible future OHLCV trajectories. We pre-train KiT at multiple parameter scales on billions of candlestick bars spanning multiple markets and timescales. Across three markets and seven resolutions, KiT attains a mean return RankIC of 0.057 and a mean volatility RankIC of 0.66, leading at every timescale and outperforming both task-specific financial forecasters and general time-series foundation models. Code will be available at: this https URL.

---


### 975. [EOPSA: Efficient On-Policy Self-Distilled Safety Alignment](https://arxiv.org/abs/2609.34519)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Qirui Liu, Yichen Sun, Yan Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-Policy Self-Distillation (OPSD) has emerged as a promising paradigm for safety alignment, delivering dense, token-level supervision by distilling from a teacher conditioned on refusal-oriented privileged prompts. However, we reveal that this paradigm suffers from critical inefficiencies that degrade both training efficiency and general reasoning capabilities. Specifically, we diagnose two fundamental bottlenecks: (1) supervisory collapse over extended rollouts, where the teacher's corrective efficacy degrades precipitously as the student's generation prefix lengthens, injecting noisy gradients into late-stage tokens; and (2) gradient dilution from stylistic shifts, where the distillation objective is dominated by safety-irrelevant stylistic discrepancies induced by privileged prompting, washing out genuine safety signals and impairing base reasoning. To resolve these issues, we propose Efficient On-Policy Self-Distilled Safety Alignment (EOPSA), which concentrates computational and gradient budgets exclusively on reliably supervised, safety-critical tokens. EOPSA incorporates two coordinated mechanisms: (i) Adaptive Rollout Scheduling, which dynamically bounds the generation horizon guided by a novel Teacher Rescue Rate (TRR) metric to operate strictly within reliable supervision regimes; and (ii) Selective Distillation, which filters out safety-neutral tokens to restrict gradient updates exclusively to safety-pivotal transitions. Extensive evaluations across reasoning models up to 32B parameters demonstrate that EOPSA slashes rollout computation by $\sim$50% and backpropagates through merely $\sim$2% of tokens, consistently outperforming full-token distillation baselines in both safety compliance and reasoning retention.

---


### 976. [WorldAttention: An Efficient Attention Architecture for Interactive Video World Models](https://arxiv.org/abs/2609.34606)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zeyu Zhang, Jinyuan Mao, Dakai An 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Leveraging the paradigm of autoregressive diffusion, text-conditioned interactive video world models aim to simulate temporally coherent environments guided by textual instructions. While enabling low-latency, long-duration generation is pivotal for embodied AI and simulation-based planning, current frameworks primarily rely on sliding-window mechanisms to bound computational complexity. However, this approach inherently sacrifices historical context, undermining the long-range interactive capabilities. Conversely, maintaining a full-history cache remains computationally prohibitive and memory-intensive: the quadratic complexity of attention leads to excessive computational overhead, while the linear growth of the KV cache inevitably leads to GPU memory saturation. To overcome these limitations, we propose WorldAttention, a system-oriented attention architecture that achieves high efficiency through the co-design of specialized attention kernels and hierarchical KV cache management. First, we introduce Hybrid Sparse Attention (HSA), which integrates linear global attention supplemented with head-adaptive sparse attention. Additionally, we design a Hierarchical KV Cache (HKV) that organizes historical KV pairs into semantically indexed pages across multi-tier memory, enabling fine-grained retrieval and controlled GPU residency. These two designs are supported by tailored kernels to effectively translate their theoretical efficiency into real-world performance. Extensive experiments on VBench-Long and InterVBench demonstrate that WorldAttention consistently surpasses prior state-of-the-art methods, achieving subject consistency scores of 0.9472 on VBench-Long and 0.9668 on InterVBench, respectively.

---


### 977. [A General Harness for Protein Foundation Model Fitness Prediction](https://arxiv.org/abs/2609.34654)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yang Tan, Qijia Tian, Gangyu Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate fitness prediction is central to protein engineering and understanding sequence-function relationships. With advances in deep learning, protein foundation models (PFMs) have become widely used for this task. Recent analyses, however, show that these models share preferences reflecting their training corpora, while unreliable inputs can further distort fitness predictions. Family-specific evolutionary evidence and structural context can help address these limitations by providing complementary constraints on model scores, motivating VenusREM-Harness (VRH), a general, model-agnostic, training-free Retrieval-Enhanced Mutation harness. It fuses frozen model scores with multiple sequence alignment (MSA) evidence according to model uncertainty, then applies gated background correction and score shrinkage based on structural confidence and solvent exposure. Across 1,211 assays and 3.1 million measured variants from ProteinGym, VenusMutHub, and the newly curated viral benchmark VenusViroHub, all 71 configurations improve Spearman correlation on all 3 benchmarks by 0.073 on average, with broad gains across 5 metrics. Extended analyses relate retrieval gains to model-MSA preference differences, assess domain-level gains and immune-escape cases, and quantify computational speedups. Built with VRH, VenusREM2 is the first to rank highest in all function, taxon, MSA-depth, and mutation-depth categories, with a ProteinGym Average Spearman of 0.556, 0.038 above the prior best.

---


### 978. [DBCF: Dual-Branch Complementary Fusion of Foundation Models for Generalized Deepfake Detection](https://arxiv.org/abs/2609.34720)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Fengming Gu, Mingjie He, Zonghui Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As image generation and editing technologies have progressed substantially, facial forgeries pose significant challenges to privacy and public safety. Due to limited ability to capture forgery cues, existing small-scale forgery detection models often struggle to generalize across various domains and unseen manipulations. To address this limitation, researchers have turned to large-scale foundation models, which can provide richer representations and better generalization. Nevertheless, relying on a single foundation model alone remains insufficient for effective forgery detection. While models like CLIP offer robust global semantic cues, they lack the capacity to capture detailed local facial features. In contrast, DINO excels at capturing local structural features of faces, but provides weaker global semantic context. To fully utilize the synergies among multiple foundation models, we propose a hierarchical multi-granular framework that integrates complementary pretrained representations. Specifically, a Global Context Branch (GCB) based on CLIP captures holistic semantic cues, while a Fine-grained Cue Branch (FCB) built on DINOv3 captures localized structural irregularities. In addition, we design a feature fusion module that enables parameter-efficient adaptation of the frozen foundation backbones by adaptively extracting and integrating complementary features from the two models. By jointly leveraging global context and fine-grained cues, our method learns more comprehensive forgery representations and achieves strong cross-manipulation performance. Extensive experiments on multiple benchmarks demonstrate the benefit of the proposed design, particularly under cross-dataset and cross-manipulation settings.

---


### 979. [Privacy-Preserving Full-Body Meshing from mmWave Radar via Mesh Foundation Model Supervision](https://arxiv.org/abs/2609.34768)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Shuxing Zhang, Yongquan Ni, Zhenyu Ding 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Millimeter-wave (mmWave) radar enables privacy-preserving human perception, but the extreme sparsity of point clouds from commercial single-chip sensors (mean ~6.5 points/frame; ~28% empty frames) has confined prior art to body-part keypoints or discrete action classification. We present a cross-modal teacher-student framework that lifts commercial radar to full-body, per-frame, metric 3D mesh reconstruction with per-joint uncertainty. Three innovations: (1) a mesh-foundation-model teacher - SAM 3D Body produces whole-body MHR ground truth (70 joints, 18,439 mesh vertices) from a single RGB frame with zero training, slashing annotation cost by orders of magnitude; (2) StudentPoseFormer - set encoding with masked attention pooling, a temporal Transformer, and a CVAE multi-hypothesis head that outputs both the pose mean and per-joint variance, honestly reporting where the radar cannot see; and (3) a multi-stage ground-truth quality pipeline (confidence gating, depth validation, temporal smoothing, bone-length consistency, bad-frame rejection) plus systematic information-lever ablations. On the public MM-Fi benchmark (same TI IWR6843 sensor, cross-subject), our full configuration reaches 7.45 cm 12-joint MPJPE, with ablations proving the causal value of point accumulation (k = 3, -0.34 cm), Doppler (-0.85 cm; -2 cm at the wrist on fast actions), and velocity loss (-0.27 cm). On our own synchronized radar + RGB-D corpus with block-level held-out splits, the pipeline achieves 21.47 cm end-to-end (per-joint hierarchy from 4.8 cm at the hip to 34.7 cm at the wrist - matching physical information limits), could be improved to 15 cm with ~30k diverse samples, and a scaling law shows sample diversity, not volume, is the binding constraint. Deployment inference is radar-only - no camera, no image.

---


### 980. [Instance-Adaptive Prompts as Context for Time-Series Foundation Models](https://arxiv.org/abs/2609.34786)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zehao Xiao, Shifeng Xie, Lei Zan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Longer histories can improve time-series foundation models (TSFMs), but require substantially higher inference cost. We therefore ask whether contextual information can be provided more efficiently through a compact set of learned token embeddings. We introduce PaCTS, which generates a small set of instance-adaptive latent prompts in the form of continuous embedding tokens conditioned on the visible context. These prompts serve as compact context surrogates for frozen TSFMs. PaCTS constructs them from instance-specific global statistics and further refines them with segment-level temporal information, capturing both global characteristics and local temporal variations. The prompt module is jointly trained and deployed across heterogeneous time series with the frozen backbone. Extensive experiments demonstrate the effectiveness of prompts as context, consistently improving forecasting across context lengths and model architectures. With a shorter input context, PaCTS can outperform the same frozen backbone using double context while requiring substantially less inference computation. Compared with weight-space adaptation methods, PaCTS achieves stronger improvements and better out-of-distribution generalization.

---


### 981. [Separating personal from population gains when calibrating EEG foundation models for new users](https://arxiv.org/abs/2609.34801)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xilin Tao, Kani Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models are increasingly adapted to individual users, but an apparent personalization gain can simply reflect a stronger population model. This distinction matters for brain-computer interfaces, where every new user must be calibrated. We evaluated personal adaptation of three frozen EEG foundation models (CBraMod, REVE and LaBraM) in 235 held-out subjects from three motor-imagery datasets, comparing each subject's adapter with the population model and with adapters fitted to other subjects. Using all first-half session labels, personal adapters improved mean balanced accuracy over the population model by 1.5-5.4 percentage points and outperformed exchanged adapters by 2.3-7.3 points in all nine model-dataset combinations. The size of this benefit depended on population training: with four times the original budget, median gains remained positive (1.0-2.0 points) but were smaller for every model, and no population model reached a confirmed plateau. Acquiring the benefit cheaply was unreliable: few-label calibration was consistently non-negative on only one dataset, and in CBraMod neither unlabeled context nor meta-learned initialization outperformed matched controls. Personalization should therefore be evaluated against both a population reference and exchanged parameters, across population-training budgets.

---


### 982. [QiYao-M: Multimodal Time Series Foundation Model with Role-Aware Modeling of Endogenous and Exogenous Modalities](https://arxiv.org/abs/2609.34842)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hanyin Cheng, Linfeng Wang, Zhengbo Qu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing multimodal time series foundation models (TSFMs) typically model heterogeneous modalities through largely shared mechanisms, overlooking the distinct forecasting roles of endogenous and exogenous modalities. In this work, we propose QiYao-M, a role-aware multimodal TSFM that models the two types of modalities separately. For endogenous modalities, to capture how they evolve along with the underlying temporal dynamics, we introduce an Endo-Multimodal Predictor and Endo-Multimodal Supervision to explicitly learn their evolution from history to the future. For exogenous modalities, to generalize across domains and across various modality types and numbers under the scarcity of exo-multimodal pretraining data, we propose an Exo-Multimodal Retrieval Enhancer that enables rapid downstream adaptation without updating the TSFM parameters. We further introduce Endo-Modality Proxy Training to train this retrieval module without exogenous multimodal pretraining data. Extensive experiments across unimodal and multimodal benchmarks demonstrate strong forecasting performance in scenarios both with and without exogenous modalities.

---


### 983. [Can We Trust the Teacher? Decoupled Credit Direction-Magnitude for Self-Distillation](https://arxiv.org/abs/2609.34848)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yugu Li, Zehong Cao, Peizhen Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> RLVR provides reliable trajectory-level credit, while OPSD offers dense supervision for token-level credit. This exposes a fundamental coupling when updating step-level credit direction and magnitude with teacher supervision, preventing steps from receiving reliable credit directions and contribution magnitudes, while making both vulnerable to teacher judgment errors and preference variance, as supported by our theoretical analysis. To separate credit direction from its contribution magnitude, we introduce \textit{Decoupled Credit Self-Distillation (DCSD)}, which theoretically decouples credit direction and magnitude into two reliable signals and uses them to calibrate privileged teacher supervision. Specifically, we design belief-margin probing to determine credit direction and marginal information gain to quantify credit magnitude, enabling step-to-token credit assignment for policy optimization. Across 11 benchmarks, DCSD achieves the best overall scores against GRPO, OPSD, RLSD, and RLCSD. Compared with base models, DCSD improves the overall score by 8.45 points on mathematical reasoning and 7.01 points on multimodal reasoning, while correcting the credit direction for 6\% of tokens and yielding a 1.5$\times$ reduction in token credit magnitude.

---


### 984. [Learning High-Risk High-Precision Motion Control](https://arxiv.org/abs/2609.34851)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Nam Hee Kim, Markus Kirjonen, Perttu Hämäläinen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep reinforcement learning (DRL) algorithms for movement control are typically evaluated and benchmarked on sequential decision tasks where imprecise actions may be corrected with later actions, thus allowing high returns with noisy actions. In contrast, we focus on an under-researched class of high-risk, high-precision motion control problems where actions carry irreversible outcomes, driving sharp peaks and ridges to plague the state-action reward landscape. Using computational pool as a representative example of such problems, we propose and evaluate State-Conditioned Shooting (SCOOT), a novel DRL algorithm that builds on advantage-weighted regression (AWR) with three key modifications: 1) Performing policy optimization only using elite samples, allowing the policy to better latch on to the rare high-reward action samples; 2) Utilizing a mixture-of-experts (MoE) policy, to allow switching between reward landscape modes depending on the state; 3) Adding a distance regularization term and a learning curriculum to encourage exploring diverse strategies before adapting to the most advantageous samples. We showcase our features' performance in learning physically-based billiard shots demonstrating high action precision and discovering multiple shot strategies for a given ball configuration.

---


### 985. [Beyond Verbalized Confidence: Calibrating Reasoners with Differentiable Readouts](https://arxiv.org/abs/2609.34857)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Chenxiao Fan, Chongming Gao, Gangyi Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) trains reasoning models to produce correct answers, but does not ensure that their stated confidence is calibrated. The resulting models are systematically overconfident. Recent methods train calibration inside the RLVR loop by having the model state a numerical confidence alongside its answer, but they all obtain the confidence by sampling it as text. This choice imposes two costs: a sampled confidence introduces variance and in practice collapses to a handful of distinct values, and sampling makes the confidence non-differentiable, forcing the calibration loss through a scalar reward. We propose CREDO (Confidence REaDOut) to replace sampling with a deterministic readout. While RLVR optimizes correctness, CREDO reads the confidence from a dedicated token pair in the model's output distribution and trains it by differentiable regression. CREDO further turns the trained confidence into a signal for accuracy, weighting rollouts by how far confidence and outcome disagree, so that accuracy and calibration improve together. Across mathematical and code reasoning, CREDO attains the best accuracy and calibration, and the gains extend to abstention and selective prediction.

---


### 986. [Dual-Stream Simultaneous Translation via 2D Grid Attention](https://arxiv.org/abs/2609.34902)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yu Pu, Wei-Qiang Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Simultaneous machine translation must generate target tokens before the source input is complete. Existing approaches address this through post-hoc read-write policies, leaving the attention mechanism unaware of bidirectional stream dependencies. We propose a dual-stream attention framework that represents source and target streams as a two-dimensional grid of hidden states and models their interaction through four structurally distinct attention types merged via joint QK Softmax normalization. Two approximations---broadcast and Hadamard---reduce the per-layer complexity from O(X^2Y+XY^2) to O(X^2+Y^2+XY) with provably decaying error. Training uses a self-guided loop: a per-cell loss heatmap drives dynamic-programming path recovery, which generates read/write decision supervision labels without external alignment. An incremental KV cache with anchored rotary position embeddings enables efficient streaming inference. On Chinese-to-English simultaneous translation, the proposed model outperforms the Wait-k baseline by +5.66 BLEURT and +10.36 COMET at comparable latency, and surpasses the non-streaming reference on COMET at a fraction of the response delay.

---


### 987. [TIDE: Teacher-Student Transition via Informative Distillation and Exploration for Agentic RL](https://arxiv.org/abs/2609.35058)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yibin Huang, Xinming Xu, Conghui Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Effective multi-turn agents require interaction strategies that coordinate information gathering, actions, and feedback over long horizons. GRPO is a reinforcement learning algorithm used to train these agents, but sparse trajectory-level rewards limit early exploration in small models. Recent methods augment RL with on-policy distillation (OPD) from a stronger teacher. However, a fixed mixture assumes that teacher guidance and reward optimization should retain a constant relative role throughout training and across interaction turns. This assumption can fail at two scales. Globally, as training progresses, maintaining strong distillation pressure can constrain the model from moving beyond the teacher's capabilities. Locally, teacher--student disagreement identifies where the student departs from the teacher, but cannot tell whether that departure is exploration supported by better outcomes or low-quality policy drift. Our methodological insight is that teacher guidance and reward optimization should be dynamically rebalanced over training and jointly allocated across turns. We instantiate this insight in \tide. Globally, \tide uses the measured disagreement trend as a practical schedule signal, advancing an OPD-to-RL handoff when discrepancy reduction becomes slow but remains positive and progressively increasing the relative weight of RL. Locally, \tide jointly modulates teacher-guided and reward-driven updates: relative action value and disagreement prioritize the OPD signal, whereas relative action value supplies the RL advantage and normalized disagreement reweights it across turns. Coupled with the global handoff, \tide allocates stronger teacher guidance early and gives reward-driven updates greater relative weight later in training. Experiments across multiple benchmarks, student scales, and controlled ablations support the effectiveness of TIDE's adaptive OPD--RL coordination.

---


### 988. [Not All Rollouts Are Worth Learning: On Trajectory Valuation for Post-Training Reinforcement Learning](https://arxiv.org/abs/2609.35072)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xuesong Jia, Ziao Yang, Zhanhe Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider the problem of trajectory valuation in reinforcement learning: how to identify and mitigate detrimental trajectories during online training. Unlike classification, where data valuation relies on fixed training and validation sets, reinforcement learning involves dynamically generated trajectories without explicit validation signals, making conventional influence-based methods inapplicable. We propose Dynamic Trajectory Valuation (DTV), a simple and efficient framework that estimates trajectory utility at the mini-batch level and filters detrimental trajectories based solely on gradient information. By operating at the optimization level, DTV integrates seamlessly with existing reinforcement learning pipelines with minimal overhead. Extensive experiments across diverse settings, including PPO, GRPO, and DPO, demonstrate that DTV consistently improves performance, enhances data efficiency, and stabilizes optimization.

---


### 989. [From Migration to Calibration: Preserving Agent Capabilities across Models, Jurisdictions, and Scale](https://arxiv.org/abs/2609.35149)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yaxiao Liu, Pengbo Liu, Yiwen Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agents need calibration when deployment conditions change: replacing a driving model, including a foundation-to-post-trained transition; crossing jurisdictions; or scaling across heterogeneous markets and sources. Interface compatibility alone does not establish capability retention or target-contract satisfaction. We formulate agent calibration as constrained behavioral adaptation across three interacting layers: information preservation, harness adaptation, and user acceptance; the layers apply to every scenario, not one-to-one to the three. The basic objective is non-degradation on prespecified capability measures while satisfying target requirements; aggregate improvement is stronger. Information calibration preserves independently validated source content still applicable to the target task. Harness calibration aligns observable artifacts at semantic checkpoints and repairs them through iteration, tool substitution, or local replanning within explicit budgets. User calibration enforces recipient-specific output contracts: templates, schemas, and section-level preferences. A global e-commerce example shows how shared standards coexist with site- and market-specific adapters and validation. We distinguish trainable policies from frozen-backbone configuration or controller optimization, and evidence verification from relative judgment and DPO/GRPO optimization. Recent harness-transfer and judge-validity studies motivate target-native execution records, separate audits of task validity and near-tie ranking, and matched target-native optimization controls. We propose held-out evaluations for model changes, cross-border adaptation, and scale, including a factorial test of source evidence and checkpoint repair and group-level reporting to prevent aggregate gains from masking local failures. This is a methodological proposal; implementation and empirical validation remain future work.

---


### 990. [G$^3$-LoRA: Organizing Reward-Weighted Video Data with Gradient-Guided Grouped LoRA](https://arxiv.org/abs/2609.35189)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jia Song, Wenhow Li, Lichen Bai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Post-training foundation video models on heterogeneous reward-weighted data usually assume that all data categories induce compatible updates. This assumption is fragile when categories correspond to different skills, domains, or evaluation dimensions. We study this problem in text-to-video post-training, where VBench2.0 dimensions define data buckets and an external multimodal reward pipeline assigns sample weights. We propose G$^3$-LoRA (Gradient-Guided Grouped LoRA), a data organization procedure that probes category-level gradients induced by reward-weighted video samples, removes the shared global update direction, clusters categories by residual gradient compatibility, trains group-specific LoRA experts, and consolidates them into one adapter by weight merging followed by on-policy distillation from the experts. We motivate this procedure by viewing reward-weighted flow matching as velocity-field regression: incompatible reward dimensions may prefer different denoising directions in overlapping noisy latent regions, causing shared LoRA training to average capabilities. On Wan2.1-T2V-1.3B-Diffusers, the merged grouped adapter improves the matched VBench2.0 evaluation over the base model, a joint reward-weighted LoRA baseline, and random, semantic, and raw-gradient partitions trained with the same pipeline; an independent evaluator agrees, and on CogVideoX-2B grouping avoids the negative transfer of joint training. The gain is not uniform: merging compresses the largest specialist gains, distillation recovers part of this loss, and camera motion and several local-quality dimensions remain challenging. Together, these results suggest that gradient compatibility can serve as a practical diagnostic for organizing reward-weighted video post-training data.

---


### 991. [Reduce, Then Encode: Multiscale Volumetric Reduction for 2D Foundation Models in Brain MRI](https://arxiv.org/abs/2609.35405)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Dexuan Ding, Yuankai Qi, Bogong Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained 2D foundation models offer a practical alternative to dedicated 3D pretraining for brain structural magnetic resonance imaging (sMRI), but their use on volumetric data requires bridging the mismatch between a 2D encoder and a 3D volume input. Existing methods typically encode slices independently and integrate their features afterwards. We introduce Multiscale Volumetric Reduction (MVR), a reduce-then-encode approach that compresses each anatomical view from (D) slices into (M << D) complementary 2D components before foundation-model encoding. MVR combines an uncentered-PCA base component derived from the original through-plane intensities with residual detail components constructed from multiscale spatial descriptors. The reduction is estimated from the training volumes without diagnostic labels or gradient-based optimization and remains fixed thereafter. The resulting components are independently processed by a shared frozen 2D foundation model and concatenated for linear probing. Under this frozen-encoder setting, MVR achieves strong overall performance across ADNI, OASIS, and ABIDE relative to the evaluated 2D-to-3D adaptation methods and simple input-reduction baselines, while also generalizing strongly from ADNI to AIBL.

---


### 992. [Reasoning with Continuous Latent Diffusion](https://arxiv.org/abs/2609.35694)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xiang Cheng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Continuous diffusion generates complete reasoning solutions through iterative refinement in latent space. We introduce Latent Flow Reasoning Models (LFRMs), an ELF-based training and inference recipe. Our experiments show that accurate decoding alone does not ensure strong reasoning performance. We therefore learn compact representations from multiple layers of a strong autoregressive teacher. Their decomposition also enables asynchronous denoising at different rates. We show that prompt encodings need only preserve the information required for the correct text-conditional score, rather than exactly match teacher features, and use a staged curriculum to learn a compact prompt encoder that replaces the teacher Transformer at inference. We adapt DiffusionNFT to learned self-conditioning guidance and incorporate gold-solution endpoints to supplement sparse rewards. Our supervised models outperform reported results from recent continuous-diffusion baselines at comparable backbone scales on mathematical reasoning and HumanEval code generation. With a 638M-parameter denoising backbone and learned prompt conditioning, post-NFT LFRM-L achieves 63.74% pass@1 on GSM8K and 24.6% on MATH500 at 64 denoising steps, and 32.85% on HumanEval and 30.18% on HumanEval+ at 128 denoising steps. Code will be available at: this https URL

---


> [!TIP]
> 当前位于：**951-992**（第 20/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | **951-992**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
