# 🔐 大模型安全相关研究 | 2026年08月26日

> 本类共 **9** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [SecOPD: Mitigating Adaptive Prompt Injections by On-Policy Distillation](https://arxiv.org/abs/2608.21500)

**<font color=#1a73e8>作者：</font>** Yibo Peng, Long Lian, David Wagner 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Prompt injection is listed as the \#1 threat to AI agents. When an agent accesses external data from websites, files, or emails, an attacker may inject a prompt into the data, saying, "Ignore all prior instructions and perform <an attacker's task>." To prevent arbitrary manipulation of agents, defenders try to train secure LLMs, which, however, still suffer from near 100% attack success rates (ASRs) against adaptive prompt injections. We note that this is because existing defensive finetuning recipes rely on sequence-level feedback signals (in DPO or GRPO). Treating an entire output equally prevents the model from learning precisely which output tokens are insecure. In this paper, we propose Secure On-Policy Distillation (SecOPD) that provides token-level feedback to guide defensive fine-tuning. The LLM receives an injected sample and produces a rollout, whose tokens are scored by the initialization model given the corresponding clean input. With more fine-grained training signals, our defended Qwen3.6-27B achieves a 9.0% ASR against the SoTA PISmith adaptive prompt injections, compared to 94.0% for the prior SoTA, Meta-SecAlign. The obtained security generalizes to domains completely unseen in training: in agentic tool calling, SecOPD achieves a 4.7% ASR compared to 5.5% for Meta-SecAlign. Code and the model are available at this https URL and this https URL.

---


### 2. [Anchoring Bias: A Persistent Fairness Backdoor Attack against MLLMs under Continual Learning](https://arxiv.org/abs/2608.21577)

**<font color=#1a73e8>作者：</font>** Yuyang Luo, Kai Shu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) are increasingly deployed in high-stakes domains where fairness is a critical safety requirement. In practice, these models are continually updated through continual learning (CL) to adapt to evolving tasks and data distributions. Prior work has shown that backdoor attacks can manipulate MLLM responses through hidden triggers, but naively implanted backdoors degrade as models undergo subsequent updates of CL. Although fairness has emerged as a central concern for MLLM deployment, whether backdoor-induced fairness violations can survive CL remains unexplored, leaving two critical questions unanswered: (1) whether a backdoor can reliably induce fairness violations in MLLMs, and (2) whether such fairness-targeted backdoors can persist through continual learning. We bridge this gap by proposing Persistent Fairness Backdoor Attack (PFBA) to inject persistent and group-specific discrimination into MLLMs. Specifically, PFBA achieves this through two novel mechanisms. The Latent Space Fairness Reinforcement reshapes the model's deep feature geometry by anchoring privileged-group representations to preserve utility while repelling and clustering targeted-group representations to sustain discrimination, and the Continual Learning Simulation iteratively optimizes the trigger against simulated parameter drift to ensure backdoor persistence across future updates. Extensive experiments demonstrate that PFBA induces severe fairness disparities that persist across continual learning rounds, evading standard backdoor defenses. The data and code are publicly available at this https URL.

---


### 3. [No One Model Catches Every Harm: Benchmarking Content Moderation Across Safety Scenarios](https://arxiv.org/abs/2608.21775)

**<font color=#1a73e8>作者：</font>** Afshin Orojlooyjadid, Hitesh Patel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly deployed in real-world applications, yet they remain vulnerable to generating harmful content. From adversarial jailbreaks that bypass safety filters to implicit hate that evades detection, the range of risks these models pose continues to grow. While both specialized content moderators and general-purpose LLMs are being used as safety layers, the question of which model is best suited for which type of harmful content remains unanswered. We present the most comprehensive evaluation of LLM safety capabilities to date, systematically testing \textbf{53} models across \textbf{11} datasets that we organize into four distinct categories. Our evaluation under both prompt-only and prompt-response settings uncovers critical blind spots: large frontier models that lead on one category fall significantly behind smaller, specialized alternatives on others, and real-world conversational safety remains largely unsolved across all model families. These findings challenge the assumption that scale alone ensures safety, and provide the community with a structured framework for informed model selection.

---


### 4. [BanglaVeilGuard: Cross-Script Safety Benchmarking and Lightweight Guardrails for Bangla Large Language Models](https://arxiv.org/abs/2608.21880)

**<font color=#1a73e8>作者：</font>** Md. Rakibul Hassan, Muhammad Iqbal Hossain  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Bangla large language model (LLM) safety is difficult to evaluate with English-centric or standard-script benchmarks because Bangla users routinely write across scripts, spellings, code-mixed forms, and regional registers. This paper presents BanglaVeilGuard, a compact Bangla-first safety benchmark and lightweight prompt guard for six language forms: standard Bangla, Romanized Bangla, Banglish, code-mixed Bangla--English, noisy Bangla, and dialectal Bangla. The benchmark contains 2,366 quality-filtered prompts and a held-out 354-prompt evaluation split spanning unsafe, safe, and safe-sensitive requests. BanglaVeilGuard uses non-destructive multi-view normalization with a prompt-risk classifier and thresholded pre-generation gate, allowing it to screen prompts for heterogeneous target models without changing their weights. Across target-model families, guarded runs reduce attack success under deterministic response scoring from 93.8--100.0\% to 6.3\% for Claude Opus 4.8, BanglaLLama, and TituLLM; TigerLLM-1B with BanglaVeilGuard achieves 78.2\% accuracy with 8.8\% ASR. The prompt guard also attains 88.5\% unsafe recall, substantially above the evaluated prompt-only guard baselines. The main remaining cost is over-refusal on dialectal and noisy benign prompts, revealing a concrete safety-helpfulness frontier for Bangla LLM deployment.

---


### 5. [Breaking the Assumptions: Auditing Input-Side Jailbreak Defenses Against Semantic Attacks](https://arxiv.org/abs/2608.21895)

**<font color=#1a73e8>作者：</font>** Aaditya Pratap, Harsh Kasyap, Somanath Tripathy  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Locally deployed Large Language Models (LLMs) via inference engines such as Ollama run without the moderation and abuse detection present in API-served models. Therefore, the safety of LLMs depends on the defense mechanisms used, and their effectiveness depends on the assumptions on which they were designed. This paper does an audit of defense mechanisms under jailbreak attacks on locally deployed models. Some defenses provide formal guarantees (SmoothLLM, Erase-and-Check, Sequential Monitors), while others rely on empirical detection results (Semantic Smoothing, Self-Denoised Smoothing, Perplexity Filtering). Instead of merely observing that defenses fail, we trace each failure back to the specific assumption: for every defense, we extract the condition it relies on, derive the empirical pattern a violation should produce, and test that prediction on six open-weight models (14B to 35B parameters) with a corpus of 100 jailbreak prompts taken from more than 40 public sources, totalling 13,800 evaluation records.

---


### 6. [Beyond Over-Refusal: Defending Indirect Prompt Injection via Latent Instruction Manifolds](https://arxiv.org/abs/2608.22248)

**<font color=#1a73e8>作者：</font>** Jiahao Chen, Rui Yin, Xinfeng Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have been integrated into complex ecosystems (e.g., Code Agents), while Indirect Prompt Injection (IPI) attacks have emerged as critical barriers to their safe deployment. Attackers exploit LLMs' indistinguishability between "instructions" and "data" to manipulate LLMs via maliciously injected instructions. Existing defenses, however, face an intractable safety-utility trade-off: most guardrails either incur high latency or suffer from severe over-refusal. In this paper, we first demonstrate that LLMs can separate instruction from data intrinsically with both theoretical and empirical evidence. Inspired by this insight, we propose AEGIS (Adaptive Ensemble Guard for Injection Shielding). AEGIS extracts instruction-sensitive projectors to identify malicious instructions and leverages a Unified Multi-Layer Consensus mechanism that aggregates topologically distinct signals across the network depth. Empirical evaluations show that AEGIS achieves remarkable detection performance against both heuristic and optimization-based attacks compared to baselines, highlighting its potential to mitigate IPI. Code is available at this https URL

---


### 7. [Text-Anchored Semantic Perturbations for Transferable Jailbreak Attacks on Multimodal Large Language Models](https://arxiv.org/abs/2608.22312)

**<font color=#1a73e8>作者：</font>** Wenyun Li, Guiping Cao, Xiangyuan Lan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have achieved remarkable progress in vision-language interaction, yet their safety alignment remains vulnerable to jailbreak attacks. A key challenge is that safety behavior learned in the textual space does not reliably transfer to fused cross-modal representations, leaving multimodal inputs exploitable through latent semantic cues. We propose Text-Anchored Semantic Perturbation Attack (TA-SPA), a black-box jailbreak framework that optimizes transferable perturbations in a text-anchored semantic space. TA-SPA integrates Text-Anchored Semantic Factorization (TASF), which encourages the separation of cross-modal semantic factors from modality-specific residuals, with Semantic-Preserving Augmentation (SPA), which diversifies harmful target anchors while preserving semantic consistency. Experiments show strong attack effectiveness and transfer to commercial MLLMs, with competitive performance under representative defenses. Additional controls and probing support the intended factorization without implying perfect disentanglement, motivating representation-level safety alignment beyond input-level filtering.

---


### 8. [Register Shifts Break LLM Safety: A Bengali Benchmark with Culturally Grounded Harms](https://arxiv.org/abs/2608.22335)

**<font color=#1a73e8>作者：</font>** Naymul Islam, Nusrat Jahan Lia, Shubhashis Roy Dipta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Bengali is the seventh-most-spoken language globally, yet LLM safety evaluation remains overwhelmingly English-centric. We introduce BanglaSafe, a benchmark of 879 Bengali prompts combining 309 natively authored prompts with 570 expert-reviewed prompts, spanning 17 culturally grounded harm categories and five prompting conditions that vary language, writing style, and authority framing. Evaluating 18 frontier LLMs, we find that over half of all responses are unsafe or partially unsafe (53.6%) while 14.7% contains strictly harmful content, and that the strongest observed effect is not the switch from English to Bengali but the choice of writing style within Bengali: the same harmful request phrased as a formal newspaper investigation succeeds 17 percentage points more often than the same request phrased as a casual message, with no adversarial engineering involved. We further show that existing safety classifiers struggle to reliably evaluate Bengali content, with even frontier models failing on nearly half of all cases.

---


### 9. [PsychJail: Exploring Psychological Jailbreaks via Multi-Turn Persuasion of LLM Policies](https://arxiv.org/abs/2608.23028)

**<font color=#1a73e8>作者：</font>** Zeyu Feng, Qingyu Wu, Yuzhe Luo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in education, healthcare, policy advising, and other interactive settings, where users engage them as sustained social interlocutors rather than one-shot query engines. This shift makes jailbreaks a growing safety threat, yet most research emphasizes single-turn prompt optimization or iterative attack refinement, leaving psychologically grounded multi-turn vulnerabilities underexplored. We present PsychJail, a psychology-guided framework for red teaming aligned LLMs through theory-grounded, multi-turn persuasion. PsychJail maps established social-psychological persuasion techniques into a tactic-conditioned attack policy. It factorizes each attacker action into a Change-of-Meaning analysis, tactic selection, and victim-visible message, operationalizing the Persuasion Knowledge Model (PKM). The policy is refined with trajectory-level reinforcement learning using a PKM-gated reward that credits early jailbreak success only when every turn contains a well-formed Change-of-Meaning analysis. Across four aligned victim models, PsychJail achieves the highest average attack success rate (87.3%) and outperforms strong single-turn and multi-turn baselines on every model. We also measure susceptibility at the action that breaks each victim, revealing four distinct model-level fingerprints that identify which persuasion levers affect each model and how broadly. These fingerprints help explain cross-model transfer asymmetry. We interpret them as four candidate psychological profiles-rationalist, credibility-driven, narrative-monoculture, and broadly persuadable-while treating this interpretation as a conjecture requiring future validation. Our findings establish psychological jailbreaks as a distinct red-teaming frontier for increasingly interactive LLMs.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
