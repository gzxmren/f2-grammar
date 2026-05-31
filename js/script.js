// ============================================
// F2 English Grammar — 互动脚本
// ============================================

(function() {
  'use strict';

  // ===== 多选题处理 =====
  function initMultipleChoice() {
    document.querySelectorAll('.options').forEach(group => {
      const radio = group.querySelector('input[type="radio"]');
      if (!radio) return;
      const name = radio.getAttribute('name');
      const qDiv = group.closest('.question');
      if (!qDiv) return;
      const data = qDiv.dataset;
      
      group.querySelectorAll('label').forEach(label => {
        label.addEventListener('click', function(e) {
          // 清除同组选中状态
          group.querySelectorAll('label').forEach(l => l.classList.remove('selected'));
          this.classList.add('selected');
        });
      });
    });
  }

  // ===== 显示答案（多选题） =====
  function showMultChoiceAnswers(qDiv) {
    const group = qDiv.querySelector('.options');
    if (!group) return;
    const correct = qDiv.dataset.correct;
    
    group.querySelectorAll('label').forEach(label => {
      const input = label.querySelector('input');
      const val = input ? input.value : '';
      
      if (val === correct) {
        label.classList.add('correct');
      } else if (label.classList.contains('selected') && val !== correct) {
        label.classList.add('wrong');
      }
    });
    
    // 显示答案提示
    const reveal = qDiv.querySelector('.answer-reveal');
    if (reveal) reveal.classList.add('show');
  }

  // ===== 填空题处理 =====
  function initFillBlanks() {
    document.querySelectorAll('.fill-input').forEach(input => {
      input.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') {
          e.preventDefault();
          checkFillBlank(this);
        }
      });
      input.addEventListener('blur', function() {
        checkFillBlank(this);
      });
    });
  }

  function checkFillBlank(input) {
    const qDiv = input.closest('.question');
    if (!qDiv) return;
    const correct = (qDiv.dataset.correct || '').toLowerCase().trim();
    const answer = (input.value || '').toLowerCase().trim().replace(/\s+/g, ' ');
    const correctNorm = correct.replace(/\s+/g, ' ');
    
    input.classList.remove('correct', 'wrong');
    
    if (!answer) return;
    
    // 允许多个正确答案（用 || 分隔）
    const validAnswers = correctNorm.split('||').map(a => a.trim());
    
    if (validAnswers.includes(answer) || validAnswers.includes(answer + '.') || validAnswers.includes(answer.replace(/^'|'$/g, ''))) {
      input.classList.add('correct');
    } else {
      input.classList.add('wrong');
    }
  }

  // ===== 显示所有答案 =====
  function showAllAnswers() {
    // 多选题
    document.querySelectorAll('.question[data-correct]').forEach(q => {
      if (q.querySelector('.options')) {
        showMultChoiceAnswers(q);
      }
    });
    
    // 填空题 - 显示答案
    document.querySelectorAll('.fill-input').forEach(input => {
      const qDiv = input.closest('.question');
      if (!qDiv) return;
      const correct = qDiv.dataset.correct || '';
      const reveal = qDiv.querySelector('.answer-reveal');
      if (reveal) reveal.classList.add('show');
      checkFillBlank(input);
    });
    
    // 改错题
    document.querySelectorAll('.question[data-answer]').forEach(q => {
      const reveal = q.querySelector('.answer-reveal');
      if (reveal) reveal.classList.add('show');
    });
  }

  // ===== 隐藏所有答案 =====
  function hideAllAnswers() {
    document.querySelectorAll('.answer-reveal').forEach(el => el.classList.remove('show'));
    document.querySelectorAll('.options label').forEach(l => {
      l.classList.remove('correct', 'wrong');
    });
    document.querySelectorAll('.fill-input').forEach(i => {
      i.classList.remove('correct', 'wrong');
    });
  }

  // ===== 计算分数 =====
  function calculateScore() {
    let total = 0;
    let correct = 0;
    
    // 多选题计分
    document.querySelectorAll('.question[data-correct]').forEach(q => {
      if (!q.querySelector('.options')) return;
      total++;
      const selected = q.querySelector('.options label.selected input');
      if (selected && selected.value === q.dataset.correct) {
        correct++;
      }
    });
    
    // 填空题 - 手动检查
    document.querySelectorAll('.fill-input').forEach(input => {
      const qDiv = input.closest('.question');
      if (!qDiv) return;
      total++;
      const correctAns = (qDiv.dataset.correct || '').toLowerCase().trim();
      const answer = (input.value || '').toLowerCase().trim().replace(/\s+/g, ' ');
      const correctNorm = correctAns.replace(/\s+/g, ' ');
      const validAnswers = correctNorm.split('||').map(a => a.trim());
      
      if (validAnswers.includes(answer) || validAnswers.includes(answer + '.')) {
        correct++;
      }
    });
    
    return { correct, total };
  }

  function showScore() {
    const result = calculateScore();
    const scoreBox = document.getElementById('score-box');
    if (!scoreBox) return;
    
    scoreBox.querySelector('.score-num').textContent = result.total > 0 
      ? Math.round(result.correct / result.total * 100) + '%'
      : '—';
    scoreBox.querySelector('.score-detail').textContent = `${result.correct} / ${result.total}`;
    scoreBox.classList.add('show');
  }

  // ===== 初始化 =====
  function init() {
    initMultipleChoice();
    initFillBlanks();
    
    // 绑定按钮事件
    const showBtn = document.getElementById('btn-show-answers');
    if (showBtn) showBtn.addEventListener('click', showAllAnswers);
    
    const hideBtn = document.getElementById('btn-hide-answers');
    if (hideBtn) hideBtn.addEventListener('click', hideAllAnswers);
    
    const scoreBtn = document.getElementById('btn-calc-score');
    if (scoreBtn) scoreBtn.addEventListener('click', showScore);
  }

  // DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
